"""Generate the hou stub, stubs/hou.pyi.

hou.py is SWIG's wrappers, which take `(*args)`, so hou's signatures and types come from
SideFX's docs: each wrapper's docstring and the C++ signatures in it.  stubgen turns them into
the stub with generic rules, here (C++ to python types) and in hou_cleanup_config.py (type
aliases, enum values, the comparison operators of every class), and the passes below add what
the docs imply: the enum of each `EnumValue`.

Everything else, i.e. whatever is wrong for one member or missing from the docs, is in the
overlay annotations/hou.pyi, which is merged in after them (see annotation_overlays.py and
annotate/README.md): a plain entry retypes a member, a `@replace` entry replaces its signature
(or `@replace` `@overload` entries give its overloads), and a `@type_check_only` entry declares a
member the docs lack.  The generator reports overlay entries whose member is gone.  Then the
parameters typed `Sequence[float]` become the overlay's `_FloatSequence`, which hou's vectors
match too.  Last, the
parameters of the functions that take no keywords are made positional-only, in the overlay's
signatures too: SWIG's overloaded wrappers, and hou's C builtins (`hou.getenv`).
"""

from __future__ import absolute_import, annotations, division, print_function

import ast
import inspect
import re
import sys
import textwrap
from collections.abc import Callable, Mapping, Sequence
from functools import lru_cache

import mypy.stubdoc
import mypy.stubgen
import mypy.stubgenc
from mypy.stubgenc import FunctionContext, FunctionSig, SignatureGenerator

from hou_cleanup_config import (
    ADDITIONAL_ENUM_NAMES,
    NON_OPTIONAL_RETURN_TYPES,
    SPECIAL_METHOD_SIGNATURES,
    TYPE_ALIASES,
)
from stubgenlib.cpptypeconvert import CppTypeConverter
from stubgenlib.siggen import (
    AdvancedSigMatcher,
    AdvancedSignatureGenerator,
    DefaultSigGenerator,
    SignatureFixer,
)

tupleTypeRegex = re.compile("^_([a-zA-Z0-9]+)Tuple$")
tupleGenTypeRegex = re.compile("^_([a-zA-Z0-9]+)TupleGenerator$")


class IsResult:
    """Indicates whether an annotating type is an argument or a return.

    This is used to modify how permissive arguments may be, since we generally want arguments
    to be abstract and returns to be concrete.
    """

    is_set: bool = False


def is_std(node: ast.AST, attr: str) -> bool:
    if (
        isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "std"
        and node.attr == attr
    ):
        return True
    return False


class AnnotationFixer(ast.NodeTransformer):
    """
    This class is used for advance transformations to type annotations.

    For example those that require unwrapping a generic, or altering lists.
    """

    def transform(self, type_str: str) -> str:
        """Entry point to transform a type string"""
        node = ast.parse(type_str)
        # print(ast.dump(node, indent=4))
        new_node = self.visit(node)
        return ast.unparse(new_node)

    def visit_Tuple(self, node: ast.Tuple) -> ast.AST:
        elts = []
        for child in node.elts:
            if isinstance(child, ast.Subscript) and (
                is_std(child.value, "allocator") or is_std(child.value, "less")
            ):
                continue
            else:
                elts.append(child)
        if len(elts) != node.elts:
            if len(elts) == 1:
                return self.visit(elts[0])
            else:
                node = ast.Tuple(elts, ast.Load())
        return self.generic_visit(node)

    def visit_Subscript(self, node: ast.Subscript) -> ast.AST:
        if isinstance(node.value, ast.Name) and node.value.id in (
            "ElemPtr",
            "UT_SharedPtr",
        ):
            # convert:  ElemPtr[Foo]  -->  Foo
            return node.slice

        new_node = self.generic_visit(node)
        if isinstance(new_node, ast.Subscript) and is_std(new_node.value, "vector"):
            if IsResult.is_set:
                # NOTE: we use Tuple instead of tuple because Parm.tuple() method interferes
                #  with the tuple type from parsing properly.
                return ast.Subscript(
                    value=ast.Name(id="Tuple", ctx=ast.Load()),
                    slice=ast.Tuple(
                        elts=[new_node.slice, ast.Constant(value=Ellipsis)],
                        ctx=ast.Load(),
                    ),
                    ctx=ast.Load(),
                )
            else:
                return ast.Subscript(
                    value=ast.Name(id="Sequence", ctx=ast.Load()),
                    slice=new_node.slice,
                    ctx=ast.Load(),
                )
        return new_node


class HoudiniCppTypeConverter(CppTypeConverter):
    TUPLE_TYPES = {
        "_StringTuple": "str",
        "_StringTupleTuple": "Sequence[str]",
        "_IntTuple": "int",
        "_IntTupleTuple": "Sequence[int]",
        "_Int64Tuple": "int",
        "_BoolTuple": "bool",
        "_FloatTuple": "float",
        "_FloatTupleTuple": "Sequence[float]",
        "_DoubleTuple": "float",
        "_DoubleTupleTuple": "Sequence[float]",
        "_PointTupleTuple": "Sequence[Point]",
        "_IKTargetTuple": "_ik_Target",
        "_EnumTuple": "EnumValue",
    }

    TYPE_MAP = [
        # HOM_IterableList is a sequence, not an iterator: SWIG wraps each in a _*TupleGenerator.
        (
            r"\bHOM_IterableList<\s*HOM_AgentTransformGroup\s*>",
            "_AgentGroupTupleGenerator",
        ),
        (r"\bHOM_IterableList<\s*HOM_ik_Joint\s*>", "_IKJointTupleGenerator"),
        (r"\bHOM_IterableList<\s*HOM_logging_LogEntry\s*>", "_LogEntryTupleGenerator"),
        (r"\bHOM_IterableList<\s*HOM_(\w+)\s*>", r"_\1TupleGenerator"),
        (r"\bHOM_PtrOrNull\b", "Optional"),
        (r"\bHOM_OptionalDouble\b", "Optional[float]"),
        (r"\bHOM_OptionalInt\b", "Optional[int]"),
        (r"\bHOM_OptionalIntInterval\b", "Optional[Tuple[int, int]]"),
        (r"\bHOM_IntInterval\b", "Tuple[int, int]"),
        (r"\bHOM_BinaryString\b", "bytes"),
        # HOM classes that have underscores
        (r"\bHOM_logging_LogEntry\b", "_logging_LogEntry"),
        (r"\bHOM_logging_MemorySink\b", "_logging_MemorySink"),
        (r"\bHOM_ik_Joint\b", "_ik_Joint"),
        (r"\bHOM_ik_Skeleton\b", "_ik_Skeleton"),
        (r"\bHOM_ik_Target\b", "_ik_Target"),
        (r"\bHOM_clone_Connection\b", "_clone_Connection"),
        (r"\bHOM_logging_FileSink\b", '"_logging_FileSink"'),
        # other
        (r"\bHOM_IterableList\b", "Iterator"),
        (r"\bHOM_NodeBundle\b", "Bundle"),
        (r"\bInterpreterObject\b", "Any"),
        (r"\bhboost::any\b", "Any"),
        (r"\bPyObject\b", "Any"),
        (r"\bPY_OpaqueObject\b", "Any"),
        (r"\bUT_Tuple\b", "Tuple"),
        (r"\bswig::SwigPyIterator\b", "Self"),
        (r"\bUT_InfoTree\b", "NodeInfoTree"),
        # NOTE: Overriding std::pair to return Tuple instead of tuple
        (r"\bstd::pair\b", "Tuple"),
    ] + CppTypeConverter.TYPE_MAP

    # Don't replace vector with list.  Instead, we'll replace std.vector with
    # Tuple in AnnotationFixer
    RESULT_TYPE_MAP: list[tuple[str, str]] = []

    def to_python_id(self, cpp_type):
        py_type = cpp_type.replace("HOM_", "")
        sub_type = self.TUPLE_TYPES.get(py_type)
        if sub_type is not None:
            py_type = f"Sequence[{sub_type}]"
        else:
            match = tupleTypeRegex.match(py_type)
            if match:
                sub_type = match.groups()[0]
                py_type = f"Sequence[{sub_type}]"
        return py_type

    @lru_cache
    def cpp_arg_to_py_type(self, cpp_type: str, is_result: bool) -> str:
        """Reimplemented to keep pointer results of NON_OPTIONAL_RETURN_TYPES from being Optional."""
        typestr = cpp_type
        is_ptr = "*" in typestr

        typestr = self._replace_typedefs(typestr)

        parts = typestr.split()

        # remove extraneous bits
        parts = [
            re.sub(self.STRIP, "", x).replace("*", "").replace("&", "").strip()
            for x in parts
        ]
        parts = [x for x in parts if not self.should_strip_part(x)]
        typestr = " ".join(parts)

        renames = dict(self.RENAMES)
        new_typestr = renames.get(typestr.replace(" ", ""))
        if new_typestr is not None:
            return new_typestr

        for pattern, replace in self.TYPE_MAP + (
            self.RESULT_TYPE_MAP if is_ptr or is_result else self.ARG_TYPE_MAP
        ):
            typestr = re.sub(pattern, replace, typestr)

        # swap container syntax
        typestr = typestr.replace("<", "[")
        typestr = typestr.replace(">", "]")

        # convert to python identifers
        parts = [x for x in re.split(self.IDENTIFIER, typestr) if x]
        parts = [(self.to_python_id(x) or x) for x in parts]

        typestr = "".join(parts)
        typestr = typestr.replace("::", ".")
        typestr = typestr.replace(" ", "")
        typestr = typestr.replace(",", ", ")

        if is_ptr:
            typestr = self.process_ptr(typestr, is_result)
        return typestr

    def process_ptr(self, converted_type: str, is_result: bool) -> str:
        if is_result:
            converted_type_start = converted_type.split("[", 1)[0]
            if converted_type_start in NON_OPTIONAL_RETURN_TYPES:
                # Houdini functions that return iterators or tuples are not "or None".
                # WARNING: This is often the result of having a std.vector of pointer types,
                #  but since `is_ptr = "*" in typestr` this is triggered for the outer type.
                #  Luckily, we do not ever have Optional pointers to the inner type, but
                #  ideally the is_ptr code would only be True if the container is also a pointer.
                return converted_type
            return f"Optional[{converted_type}]"
        else:
            return converted_type


class HoudiniTypeFixer(SignatureFixer):
    converter = HoudiniCppTypeConverter()
    transfomer = AnnotationFixer()

    def maybe_add_optional(self, type_name: str, default_value: str | None) -> str:
        if default_value == "None" and not (
            type_name.startswith("Optional[")
            or type_name.startswith("typing.Optional[")
        ):
            return f"Optional[{type_name}]"
        else:
            return type_name

    def cleanup_type(
        self,
        type_name: str,
        ctx: FunctionContext,
        is_result: bool,
        default_value: str | None = None,
    ) -> str:
        if type_name.startswith("'") and type_name.endswith("'"):
            type_name = type_name[1:-1]

        new_type = self.converter.cpp_arg_to_py_type(type_name, is_result)

        # We need to indicate to the transformer whether we expect an argument (abstract) or
        # return (concrete) type for sequences, so set IsResult.is_set appropriately.
        # Since the transformer has a lot of indirect calls, setting this global scope override
        # allows us to change this behavior without redefining the whole transformer class.
        IsResult.is_set = is_result
        new_type = self.transfomer.transform(new_type)
        IsResult.is_set = False

        new_type = self.maybe_add_optional(new_type, default_value)

        return new_type


class HoudiniSignatureGenerator(AdvancedSignatureGenerator):
    sig_matcher = AdvancedSigMatcher(
        signature_overrides={
            f"*.{name}": signature
            for name, signature in SPECIAL_METHOD_SIGNATURES.items()
        }
    )


class ASTStubGenerator(mypy.stubgen.ASTStubGenerator):
    def visit_class_def(self, o) -> None:
        # filter _*Tuple classes, they are not used (See to_python_id).
        if (
            o.name in ("SwigPyIterator", "_AgentDefnMap", "_StringMapMat4")
            or tupleTypeRegex.match(o.name)
            or tupleGenTypeRegex.match(o.name)
        ):
            return

        return super().visit_class_def(o)

    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [
            HoudiniSignatureGenerator(
                fallback_sig_gen=HoudiniTypeFixer(
                    DefaultSigGenerator(), default_sig_handling="ignore"
                )
            )
        ]

    def get_signatures(
        self,
        default_signature: FunctionSig,
        sig_generators: list[SignatureGenerator],
        func_ctx: FunctionContext,
    ) -> list[FunctionSig]:
        if (
            func_ctx.class_info
            and func_ctx.class_info.name[0].islower()
            and not func_ctx.name.startswith("__")
        ):
            self._decorators.append("@staticmethod")
            if default_signature.args[0].name == "self":
                default_signature.args.pop(0)
        return super().get_signatures(default_signature, sig_generators, func_ctx)

    def get_imports(self) -> str:
        import hou  # type: ignore[import]

        # FIXME: Where do we want to pull Qt from?
        #  Houdini ships with PySide2 or PySide6 depending on the version.
        #  We could also use `Qt`, but that doesn't ship with Houdini.
        #  Is this the best way to get the PySide version?
        try:
            import PySide6  # type: ignore[import]
        except ImportError:
            pyside = "PySide2"
        else:
            pyside = "PySide6"

        imports = super().get_imports() + "\n"
        imports += "import datetime\n"
        imports += "import typing\n"
        imports += "from pathlib import Path\n"
        imports += "from types import TracebackType\n"
        imports += (
            "from typing import Any, Callable, Dict, Generic, Iterator, Iterable, Mapping, Never, "
            "Literal, Optional, Sequence, Self, Union, Tuple, TypeAlias\n\n"
        )
        # `hou.X` names an enum in a class with an attribute named X, e.g. Ramp.colorType().
        imports += "import hou\n"
        imports += "import typing_extensions\n"
        # Optional dependencies: types-usd and PySide stubs may not be installed.
        # Modules that houpythonportion adds to hou.  Aliased by assignment, because
        # `import x as y` in a stub is not re-exported.
        imports += "import _houfs\nimport houshfs\nimport hwebserver\n"
        imports += "fs = _houfs\nshfs = houshfs\nwebServer = hwebserver\n"
        imports += "import pxr.Sdf  # type: ignore[import-not-found]\n"
        imports += "import pxr.Usd  # type: ignore[import-not-found]\n"
        imports += f"from {pyside} import QtCore, QtGui, QtWidgets  # type: ignore[import-not-found]\n\n"

        for type_alias_name, type_alias in TYPE_ALIASES.items():
            imports += f"{type_alias_name}: TypeAlias = {type_alias}\n"

        # The enum an EnumValue belongs to (its class in the stub). The default keeps a bare
        # `hou.EnumValue`, meaning a value of any enum, valid under --disallow-any-generics.  An
        # alias, because mypy reports an `Any` written as the default itself as explicit in
        # every bare `hou.EnumValue` under --disallow-any-explicit.
        imports += "_AnyEnum: TypeAlias = Any\n"
        imports += '_EnumT = typing_extensions.TypeVar("_EnumT", default=_AnyEnum)\n'

        imports += "\n"

        return imports

    @staticmethod
    def get_enums_from_docstring(docstring: str | None) -> set[str]:
        """Determine the enumeration values from the docstring, by looking at the names
        indented underneath the 'VALUES' section."""

        if not docstring or "VALUES" not in docstring:
            return set()

        # If 'VALUES' is in the docstring, we will parse it for enumeration values names.
        # header_indent is the indentation level we find "VALUES", and names_indent is where
        # we find the individual enum names.
        header_indent = -1
        names_indent = -1
        reading_values = False
        enum_names = set()
        for line in textwrap.dedent(docstring).split("\n"):
            indent_match = re.match(r"(?P<indentsize>[ \t]*)[\w_]", line)
            if not indent_match:
                continue
            indent = len(indent_match.group("indentsize"))
            if indent == header_indent:
                # We have unindented after reading the VALUES block.
                reading_values = False
                break
            if line.strip() == "VALUES":
                # Once we encounter VALUES, record the indentation of
                # where we see it, so we know when we have exited.
                header_indent = indent
                reading_values = True
                continue

            if reading_values and names_indent == -1:
                # We have entered into the VALUES block.
                names_indent = indent

            if indent == names_indent:
                # We check that the indent matches where we expect to
                # find enum values to avoid reading in the description
                # of an enum value, which will be further indented.

                # Some names are fully qualified (e.g. hou.glShadingType.WireBoundingBox)
                # and others will just be the end, and we only want the member name.
                enum_name = line.rsplit(".", 1)[-1].strip()
                enum_names.add(enum_name)

        return enum_names

    @staticmethod
    def get_runtime_enum_names(class_name: str) -> set[str]:
        """The names of the enumeration values of a hou class, as hou defines them."""
        import hou  # type: ignore[import]

        cls = getattr(hou, class_name, None)
        if cls is None:
            return set()
        return {
            name
            for name, value in vars(cls).items()
            if isinstance(value, hou.EnumValue)
        }

    def dedent(self) -> None:
        """When we exit a class, add its enum values.

        This is the only method of the generator called while the class context still exists.
        """
        if self._current_class:
            class_name = self._current_class.name
            enum_names = self.get_enums_from_docstring(self._current_class.docstring)
            enum_names.update(ADDITIONAL_ENUM_NAMES.get(class_name, {}))
            # The docs have typos (shaderType.CVEX is CVex) and omissions.
            enum_names = self.get_runtime_enum_names(class_name) or enum_names
            if enum_names:
                # self.add(textwrap.indent("\n# Missing enums added by stubgen\n", self._indent))
                for enum_name in sorted(enum_names):
                    self.add(
                        textwrap.indent(
                            f"{enum_name}: EnumValue[{class_name}] = ...\n",
                            self._indent,
                        )
                    )

        super().dedent()


mypy.stubgen.ASTStubGenerator = ASTStubGenerator  # type: ignore[attr-defined,misc]
# mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]


def enableHouModule():
    """Set up the environment so that "import hou" works."""
    import os
    import sys

    # Importing hou will load Houdini's libraries and initialize Houdini.
    # This will cause Houdini to load any HDK extensions written in C++.
    # These extensions need to link against Houdini's libraries,
    # so the symbols from Houdini's libraries must be visible to other
    # libraries that Houdini loads.  To make the symbols visible, we add the
    # RTLD_GLOBAL dlopen flag.
    if hasattr(sys, "setdlopenflags"):
        old_dlopen_flags = sys.getdlopenflags()
        sys.setdlopenflags(old_dlopen_flags | os.RTLD_GLOBAL)

    # For Windows only.
    # Add %HFS%/bin to the DLL search path so that Python can locate
    # the hou module's Houdini library dependencies.  Note that
    # os.add_dll_directory() does not exist in older Python versions.
    # Python 3.7 users are expected to add %HFS%/bin to the PATH environment
    # variable instead prior to launching Python.
    if sys.platform == "win32" and hasattr(os, "add_dll_directory"):
        os.add_dll_directory("{}/bin".format(os.environ["HFS"]))

    try:
        pass
    finally:
        # Reset dlopen flags back to their original value.
        if hasattr(sys, "setdlopenflags"):
            sys.setdlopenflags(old_dlopen_flags)


enableHouModule()


SWIG_ATTRIBUTE_FIXES = [
    # SWIG's ownership flag on every wrapped object.
    (re.compile(r"^(\s+)thisown: Incomplete$", re.MULTILINE), r"\1thisown: bool"),
    # SWIG's destructor hook: an implementation detail, not for callers.
    (re.compile(r"^\s+__swig_destroy__: Incomplete\n", re.MULTILINE), ""),
    # _SwigNonDynamicMeta's attribute setter, which only lets existing class attributes be set.
    (
        re.compile(r"^(\s+)__setattr__: Incomplete$", re.MULTILINE),
        r"\1def __setattr__(cls, name: str, value: object, /) -> None: ...",
    ),
]


def fix_swig_attributes(path: str) -> None:
    with open(path) as f:
        text = f.read()
    for pattern, repl in SWIG_ATTRIBUTE_FIXES:
        text = pattern.sub(repl, text)
    with open(path, "w") as f:
        f.write(text)


UNTYPED_INIT = re.compile(r"(\s*def __init__\()self, \*args, \*\*kwargs(\) -> None:.*)")
# A required keyword-only parameter no caller can pass: unlike `*args: Never` it rejects a call
# without arguments, and unlike a positional `Never` parameter (which pyright reads as Unknown)
# it rejects any positional argument, in both mypy and pyright. Subclasses can still define
# their own `__init__`, as Houdini's do (imagefilterlist.FakePane(hou.PathBasedPaneTab)).
# The overlay gives the same form to classes whose C++ constructor only takes types python has
# no class for.
NO_CONSTRUCTOR_INIT = r"\1self, *, no_constructor: Never\2"


def hou_runtime_class(name: str) -> object:
    """The hou class a top-level stub class stands for."""
    import hou

    if hasattr(hou, name):
        return getattr(hou, name)
    # Classes of submodules are stubbed as `_<module>_<class>`, e.g. `_ik_Joint`.
    module, _, cls = name[1:].partition("_")
    return getattr(getattr(hou, module, None), cls, None)


@lru_cache(maxsize=None)
def source_classes_without_constructor() -> frozenset[str]:
    """The classes in hou.py whose `__init__` raises SWIG's "No constructor defined"."""
    import hou

    with open(hou.__file__) as f:
        tree = ast.parse(f.read())
    found = set()
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        for func in node.body:
            if isinstance(func, ast.FunctionDef) and func.name == "__init__":
                raised = [n.exc for n in ast.walk(func) if isinstance(n, ast.Raise)]
                if any(
                    isinstance(exc, ast.Call)
                    and ast.unparse(exc.func) == "AttributeError"
                    and exc.args
                    and isinstance(exc.args[0], ast.Constant)
                    and str(exc.args[0].value).startswith("No constructor defined")
                    for exc in raised
                ):
                    found.add(node.name)
    return frozenset(found)


def has_no_constructor(name: str) -> bool:
    """Whether a stub class's SWIG class raises "No constructor defined" when called.

    hou's submodules (`hou.anim`, `hou.hipFile`, ...), which the stub writes as classes, are
    instances of such classes; those that only exist in a graphical session (`hou.ui`) are
    checked in hou.py's source instead.
    """
    runtime = hou_runtime_class(name)
    if runtime is None:
        return name in source_classes_without_constructor()
    cls = runtime if isinstance(runtime, type) else type(runtime)
    try:
        cls()
    except AttributeError as exc:
        return str(exc).startswith("No constructor defined")
    except Exception:
        return False
    return False


def untyped_constructors(text: str) -> list[tuple[ast.ClassDef, int]]:
    """The classes whose `__init__` is SWIG's untyped `(self, *args, **kwargs)`, with the line
    number (0-based) of each."""
    found = []
    lines = text.split("\n")
    for node in ast.parse(text).body:
        if isinstance(node, ast.ClassDef):
            for func in node.body:
                if (
                    isinstance(func, ast.FunctionDef)
                    and func.name == "__init__"
                    and UNTYPED_INIT.fullmatch(lines[func.lineno - 1])
                ):
                    found.append((node, func.lineno - 1))
    return found


def type_unconstructible_classes(path: str) -> None:
    """Make constructing a class that SWIG gives no constructor a type error.

    SWIG writes `def __init__(self, *args, **kwargs): raise AttributeError("No constructor
    defined")` for the classes whose objects only Houdini creates. The constructors of the
    others have signatures, from the docs or the overlay (see `report_untyped_constructors`).
    """
    import pathlib

    stub = pathlib.Path(path)
    text = stub.read_text()
    lines = text.split("\n")
    for node, lineno in untyped_constructors(text):
        if has_no_constructor(node.name):
            lines[lineno] = UNTYPED_INIT.sub(NO_CONSTRUCTOR_INIT, lines[lineno])
    stub.write_text("\n".join(lines))


def type_exception_messages(path: str) -> None:
    """Let hou's exceptions take a message of None, as SWIG passes None for a `char *`."""
    import ast
    import pathlib

    import hou

    stub = pathlib.Path(path)
    text = stub.read_text()
    lines = text.split("\n")
    for node in ast.parse(text).body:
        if not isinstance(node, ast.ClassDef):
            continue
        cls = getattr(hou, node.name, None)
        if not (isinstance(cls, type) and issubclass(cls, hou.Error)):
            continue
        for func in node.body:
            if isinstance(func, ast.FunctionDef) and func.name == "__init__":
                line = lines[func.lineno - 1]
                lines[func.lineno - 1] = line.replace(
                    "(self, message: str = ...", "(self, message: str | None = ..."
                )
    stub.write_text("\n".join(lines))


# The hou classes that _FloatSequence matches, made redundant beside it in a union.
FLOAT_SEQUENCE_CLASSES = {"Vector2", "Vector3", "Vector4", "Quaternion"}


class FloatSequenceTaker(ast.NodeTransformer):
    """Turn `Sequence[float]` into `_FloatSequence` in an annotation, dropping the classes it
    already matches from the unions it is in."""

    def visit_Subscript(self, node: ast.Subscript) -> ast.AST:
        node = self.generic_visit(node)
        if ast.unparse(node) == "Sequence[float]":
            return ast.Name(id="_FloatSequence", ctx=ast.Load())
        return node

    def visit_BinOp(self, node: ast.BinOp) -> ast.AST:
        if not isinstance(node.op, ast.BitOr):
            return self.generic_visit(node)
        members = [self.visit(m) for m in union_members(node)]
        names = [ast.unparse(m) for m in members]
        if "_FloatSequence" in names:
            members = [
                m
                for i, (m, name) in enumerate(zip(members, names))
                if name not in FLOAT_SEQUENCE_CLASSES and name not in names[:i]
            ]
        union = members[0]
        for member in members[1:]:
            union = ast.BinOp(left=union, op=ast.BitOr(), right=member)
        return union


def union_members(node: ast.expr) -> list[ast.expr]:
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        return union_members(node.left) + union_members(node.right)
    return [node]


def take_float_sequences(path: str) -> None:
    """Type the parameters that take a sequence of floats as `_FloatSequence` (see the overlay),
    so that they take hou's vectors, which SWIG accepts there."""
    import pathlib

    stub = pathlib.Path(path)
    text = stub.read_text()
    lines = text.split("\n")
    edits = []
    for node in ast.walk(ast.parse(text)):
        if not isinstance(node, ast.FunctionDef):
            continue
        args = node.args
        for arg in [*args.posonlyargs, *args.args, *args.kwonlyargs]:
            ann = arg.annotation
            if ann is None or "Sequence[float]" not in ast.unparse(ann):
                continue
            assert ann.lineno == ann.end_lineno, f"multi-line annotation: {node.name}"
            new = ast.unparse(FloatSequenceTaker().visit(ann))
            edits.append((ann.lineno - 1, ann.col_offset, ann.end_col_offset, new))
    # From the end of each line, so the earlier offsets (in UTF-8 bytes) stay right.
    for lineno, start, end, new in sorted(edits, reverse=True):
        line = lines[lineno].encode()
        lines[lineno] = (line[:start] + new.encode() + line[end:]).decode()
    stub.write_text("\n".join(lines))


def report_untyped_constructors(path: str) -> None:
    """List the untyped constructors left, which hython does not reject."""
    import pathlib

    untyped = [
        node.name for node, _ in untyped_constructors(pathlib.Path(path).read_text())
    ]
    if untyped:
        print(f"Untyped constructors that hython does not reject: {', '.join(untyped)}")


def main(outdir: str):
    mypy.stubgen.main(
        ["-m=hou", "--verbose", "--parse-only", "--include-docstrings", "-o=stubs"]
    )
    fix_swig_attributes("stubs/hou.pyi")
    type_unconstructible_classes("stubs/hou.pyi")
    type_exception_messages("stubs/hou.pyi")
    type_enum_values("stubs/hou.pyi")
    apply_overlay("stubs/hou.pyi")
    take_float_sequences("stubs/hou.pyi")
    # After the overlay, whose replaced signatures must take no keywords either.
    mark_positional_only("stubs/hou.pyi")
    report_untyped_constructors("stubs/hou.pyi")
    report_bare_enum_values("stubs/hou.pyi")


def split_params(params: str) -> list[str]:
    """Split a parameter list at its top-level commas."""
    parts, depth, current = [], 0, ""
    for char in params:
        if char in "[(":
            depth += 1
        elif char in "])":
            depth -= 1
        if char == "," and depth == 0:
            parts.append(current.strip())
            current = ""
        else:
            current += char
    return [*parts, current.strip()] if current.strip() else parts


def mark_positional_only(path: str) -> None:
    """Make the parameters of the functions that take no keywords positional-only.

    SWIG wraps an overloaded C++ method as `def name(self, *args)`, which takes no keywords, and
    some of hou's functions are C builtins that take none (`hou.getenv`).
    """
    import pathlib

    stub = pathlib.Path(path)
    text = stub.read_text()
    lines = text.split("\n")
    for lineno in swig_positional_only_lines(text):
        match = re.match(r"(\s*def \w+\()(.*)(\) ->.*)", lines[lineno])
        if not match:
            continue
        params = split_params(match.group(2))
        named = [
            i
            for i, p in enumerate(params)
            if p not in ("self", "cls") and not p.startswith("*")
        ]
        if named and "/" not in params:
            params.insert(named[-1] + 1, "/")
            lines[lineno] = match.group(1) + ", ".join(params) + match.group(3)
    stub.write_text("\n".join(lines))


def swig_positional_only_lines(text: str) -> list[int]:
    """The (0-based) line numbers of the stub's functions whose SWIG wrapper takes only `*args`,
    and of those that are C builtins that take no keywords."""
    import ast
    import inspect
    import types

    import hou

    def takes_only_args(func: object) -> bool:
        if isinstance(func, types.BuiltinFunctionType):
            return rejects_keywords(func)
        try:
            params = list(inspect.signature(func).parameters.values())  # type: ignore[arg-type]
        except (TypeError, ValueError):
            return False
        kinds = {p.kind for p in params if p.name != "self"}
        return kinds == {inspect.Parameter.VAR_POSITIONAL}

    def runtime_class(name: str) -> object:
        if hasattr(hou, name):
            return getattr(hou, name)
        # Classes of submodules are stubbed as `_<module>_<class>`, e.g. `_ik_Joint`.
        module, _, cls = name[1:].partition("_")
        return getattr(getattr(hou, module, None), cls, None)

    found = []
    for node in ast.parse(text).body:
        if isinstance(node, ast.FunctionDef) and takes_only_args(
            getattr(hou, node.name, None)
        ):
            found.append(node.lineno - 1)
        elif isinstance(node, ast.ClassDef):
            cls = runtime_class(node.name)
            for func in node.body:
                if isinstance(func, ast.FunctionDef) and func.name != "__init__":
                    runtime = getattr(cls, "__dict__", {}).get(func.name)
                    if runtime is not None and takes_only_args(runtime):
                        found.append(func.lineno - 1)
    return found


def rejects_keywords(func: Callable[..., object]) -> bool:
    """Whether a C builtin takes no keyword arguments.

    Without a text signature to tell, it is called with an unknown keyword: CPython rejects
    keywords for a builtin that takes none before calling it, and one that takes keywords fails
    on the unknown name in its argument parsing.
    """
    try:
        params = inspect.signature(func).parameters.values()
    except ValueError:
        try:
            func(__no_such_keyword__=None)
        except TypeError as e:
            return "takes no keyword arguments" in str(e)
        return False
    return all(p.kind is inspect.Parameter.POSITIONAL_ONLY for p in params)


BARE_ENUM_VALUE = re.compile(r"\bEnumValue\b(?!\[)")
TYPED_ENUM_VALUE = re.compile(r"\bEnumValue\[(?:hou\.)?(\w+)\]")
DOC_HOU_NAME = re.compile(r"\bhou\.([A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*)")


def hou_enum_classes() -> dict[str, str]:
    """The stub class of each hou enum, by the name the docs give it (`ik.targetType` for
    `_ik_targetType`)."""
    import hou

    enums = {}
    for name, cls in vars(hou).items():
        if isinstance(cls, type) and any(
            isinstance(v, hou.EnumValue) for v in vars(cls).values()
        ):
            module, sep, nested = name[1:].partition("_")
            enums[f"{module}.{nested}" if name.startswith("_") and sep else name] = name
    return enums


class EnumValueTyper:
    """Finds the enums of the stub's bare `EnumValue` parameters and returns.

    It looks in the docs (the method's docstring, its runtime docstring if the stub has none,
    and every overload in the help sources): the enum of a parameter's default value, the enums
    its description names, the enums the signature's return type or a "Returns ..." sentence
    names, the one enum the docs name if the method has a single enum parameter, and last the
    enum of a getter's setter or a setter's getter.  What none of them names stays a bare
    `EnumValue`, a value of any enum, unless the overlay types it.
    """

    def __init__(self, enums: Mapping[str, str]) -> None:
        import zipfile

        import hou

        self.hou = hou
        self.enums = enums
        with zipfile.ZipFile(
            f"{hou.text.expandString('$HFS')}/houdini/help/hom.zip"
        ) as help_zip:
            self.help = {
                name: help_zip.read(name).decode("utf-8", "replace")
                for name in help_zip.namelist()
                if name.startswith("hou/") and name.endswith(".txt")
            }

    def doc_enums(self, text: str) -> list[str]:
        """The enums `hou.X` names in some text, preferring those not named by a value
        (`hou.rampParmType.Color` in "... if the type is hou.rampParmType.Color")."""
        whole: list[str] = []
        by_value: list[str] = []
        for match in DOC_HOU_NAME.finditer(text):
            parts = match.group(1).split(".")
            for i in range(1, len(parts) + 1):
                cls = self.enums.get(".".join(parts[:i]))
                if cls:
                    found = whole if i == len(parts) else by_value
                    if cls not in found:
                        found.append(cls)
                    break
        return whole or by_value

    @staticmethod
    def split_docstring(doc: str) -> tuple[str, list[str]]:
        """The signature lines of a docstring, and the lines of its description."""
        lines = [
            line
            for line in inspect.cleandoc(doc).split("\n")
            if not line.lstrip().startswith(">")
        ]
        sig = [
            lines[i + 1] for i, line in enumerate(lines[:-1]) if line.strip() == "USAGE"
        ]
        i = 0
        while i < len(lines) and lines[i].strip() and not lines[i].startswith(" "):
            sig.append(lines[i])
            i += 1
        return " ".join(sig), lines[i:]

    def docs(
        self, scope: str, name: str, docstring: str | None
    ) -> list[tuple[str, list[str]]]:
        """The (signature, description lines) of a function's docstring and help entries."""
        docs = []
        if not docstring:
            runtime = getattr(self.hou, scope, self.hou) if scope else self.hou
            docstring = getattr(getattr(runtime, name, None), "__doc__", None)
        if docstring:
            docs.append(self.split_docstring(docstring))
        # Classes of submodules are stubbed as `_<module>_<class>`, e.g. `_ik_Target`.
        module, sep, nested = scope[1:].partition("_")
        help_name = (
            f"{module}/{nested}" if scope.startswith("_") and sep else scope or name
        )
        lines = self.help.get(f"hou/{help_name}.txt", "").split("\n")
        lines = [line for line in lines if not line.lstrip().startswith(">")]
        if not scope:
            sig = " ".join(line for line in lines if line.startswith(":usage:"))
            return docs + [(sig, lines)] if sig else docs
        for i, line in enumerate(lines):
            if re.match(rf"::\s*`{re.escape(name)}\(", line):
                end = next(
                    (
                        j
                        for j in range(i + 1, len(lines))
                        if re.match(r"::|@|=", lines[j])
                    ),
                    len(lines),
                )
                docs.append((line, lines[i + 1 : end]))
        return docs

    @staticmethod
    def parameter_doc(body: Sequence[str], name: str) -> str | None:
        """The description of a parameter: the lines indented below its name."""
        for i, line in enumerate(body):
            if line.strip().strip("`:") == name:
                indent = len(line.expandtabs()) - len(line.lstrip())
                described = []
                for following in body[i + 1 :]:
                    if (
                        following.strip()
                        and len(following.expandtabs()) - len(following.lstrip())
                        <= indent
                    ):
                        break
                    described.append(following)
                return "\n".join(described)
        return None

    def parameter(
        self,
        name: str,
        default: str | None,
        docs: Sequence[tuple[str, Sequence[str]]],
        sole: bool,
    ) -> list[str]:
        if default and (found := self.doc_enums(f"hou.{default}")):
            return found
        for sig, body in docs:
            # e.g. `severity=hou.severityType.Message`, `type_hint = hou.fieldType::NoSuchField`
            # or `position_type=positionType.WorldSpace`.
            match = re.search(
                rf"\b{re.escape(name)}\s*=\s*(?:Hom:)?(?:hou\.)?([\w.:]+)", sig
            )
            if match and (
                found := self.doc_enums(f"hou.{match.group(1).replace('::', '.')}")
            ):
                return found
        for sig, body in docs:
            described = self.parameter_doc(body, name)
            if described and (found := self.doc_enums(described)):
                return found
        if sole:
            for sig, body in docs:
                found = self.doc_enums("\n".join([sig, *body]))
                if len(found) == 1:
                    return found
        return []

    def result(self, docs: Sequence[tuple[str, Sequence[str]]]) -> list[str]:
        for sig, body in docs:
            if "->" in sig and (found := self.doc_enums(sig.split("->", 1)[1])):
                return found
        for sig, body in docs:
            described = " ".join(line.strip() for line in body)
            # The sentence, which ends at a full stop, not at one in `hou.X`.
            for match in re.finditer(
                r"\b[Rr]eturns?\b(.*?)(?:\.(?:\s|$)|$)", described
            ):
                if found := self.doc_enums(match.group(1)):
                    return found
        return []


def type_enum_values(path: str) -> None:
    """Give each `EnumValue` parameter and return in the stub its enum, `EnumValue[enum]`, and
    make `EnumValue` generic.

    Enum members are typed by their class as stubgen writes them (see `dedent`).  An
    annotation that already gives an enum is kept.
    """
    import pathlib

    stub = pathlib.Path(path)
    text = stub.read_text()
    typer = EnumValueTyper(hou_enum_classes())
    tree = ast.parse(text)

    def bare(node: ast.expr | None) -> bool:
        return node is not None and bool(BARE_ENUM_VALUE.search(ast.unparse(node)))

    # (function, the names its class defines, "Class.method",
    #  {parameter or "return": its enums, [] if not found})
    found: list[tuple[ast.FunctionDef, set[str], str, dict[str, list[str]]]] = []
    for scope in scopes_of(tree):
        scope_name = scope.name if isinstance(scope, ast.ClassDef) else ""
        names = class_member_names(scope) if isinstance(scope, ast.ClassDef) else set()
        for func in scope.body:
            if not isinstance(func, ast.FunctionDef):
                continue
            args = func.args
            params = [*args.posonlyargs, *args.args, *args.kwonlyargs]
            params += [a for a in (args.vararg, args.kwarg) if a]
            enum_params = [a for a in params if bare(a.annotation)]
            if not enum_params and not bare(func.returns):
                continue
            positional = [*args.posonlyargs, *args.args]
            defaults = {
                a.arg: ast.unparse(d)
                for a, d in [
                    *zip(
                        positional[len(positional) - len(args.defaults) :],
                        args.defaults,
                    ),
                    *zip(args.kwonlyargs, args.kw_defaults),
                ]
                if d is not None
            }
            key = f"{scope_name}.{func.name}" if scope_name else func.name
            docs = typer.docs(
                scope_name, func.name, ast.get_docstring(func, clean=False)
            )
            resolved = {
                param.arg: typer.parameter(
                    param.arg, defaults.get(param.arg), docs, len(enum_params) == 1
                )
                for param in enum_params
            }
            if bare(func.returns):
                resolved["return"] = typer.result(docs)
            found.append((func, names, key, resolved))

    # A getter returns the enum its setter takes, and the other way round, and a constructor's
    # parameter takes what its getter returns (`label_parm_type`, `labelParmType()`), looking
    # in the class and then its base classes.
    returns: dict[str, list[str]] = {}
    bases: dict[str, list[str]] = {}
    for cls in [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]:
        bases[cls.name] = [ast.unparse(b) for b in cls.bases]
        for func in cls.body:
            if isinstance(func, ast.FunctionDef) and func.returns is not None:
                if typed := TYPED_ENUM_VALUE.findall(ast.unparse(func.returns)):
                    returns[f"{cls.name}.{func.name}"] = list(dict.fromkeys(typed))
    setter_params: dict[str, list[str]] = {}
    for _, _, key, resolved in found:
        if resolved.get("return"):
            returns[key] = resolved["return"]
        param_enums = [enums for name, enums in resolved.items() if name != "return"]
        if len(param_enums) == 1 and param_enums[0]:
            setter_params[key] = param_enums[0]

    def inherited(
        table: Mapping[str, list[str]], scope: str, names: Sequence[str]
    ) -> list[str]:
        scopes = [scope]
        for cls in scopes:
            for name in names:
                if f"{cls}.{name}" in table:
                    return table[f"{cls}.{name}"]
            scopes += [b for b in bases.get(cls, []) if b not in scopes]
        return []

    for _, _, key, resolved in found:
        class_name, _, name = key.rpartition(".")
        if not class_name:
            continue
        attribute = name[3:] if name.startswith(("get", "set")) else name
        attribute = attribute[:1].lower() + attribute[1:]
        capitalized = attribute[:1].upper() + attribute[1:]
        if resolved.get("return") == []:
            resolved["return"] = inherited(
                setter_params, class_name, [f"set{capitalized}", name]
            )
        param_names = [p for p in resolved if p != "return"]
        for param in param_names:
            if resolved[param] != []:
                continue
            if name.startswith("set") and len(param_names) == 1:
                getters = [attribute, f"get{capitalized}"]
            elif name == "__init__":
                first, *rest = param.split("_")
                getters = [first + "".join(word.capitalize() for word in rest)]
            else:
                continue
            resolved[param] = inherited(returns, class_name, getters)

    offsets = [0]
    for line in text.split("\n"):
        offsets.append(offsets[-1] + len(line) + 1)
    edits: list[tuple[int, int, str]] = []
    for func, names, key, resolved in found:
        args = func.args
        annotations = {
            a.arg: a.annotation
            for a in [
                *args.posonlyargs,
                *args.args,
                *args.kwonlyargs,
                args.vararg,
                args.kwarg,
            ]
            if a is not None
        }
        annotations["return"] = func.returns
        for name, enums in resolved.items():
            node = annotations[name]
            if (
                not enums
                or node is None
                or node.end_lineno is None
                or node.end_col_offset is None
            ):
                continue
            # Class scope shadows the module: Ramp.colorType() is not the colorType enum.
            typed_enums = " | ".join(
                f"EnumValue[{'hou.' if e in names else ''}{e}]" for e in enums
            )
            start = offsets[node.lineno - 1] + node.col_offset
            end = offsets[node.end_lineno - 1] + node.end_col_offset
            edits.append(
                (start, end, BARE_ENUM_VALUE.sub(typed_enums, text[start:end]))
            )

    for start, end, replacement in sorted(edits, reverse=True):
        text = text[:start] + replacement + text[end:]
    text = re.sub(
        r"^class EnumValue:",
        "class EnumValue(Generic[_EnumT]):",
        text,
        flags=re.MULTILINE,
    )
    stub.write_text(text)


def scopes_of(tree: ast.Module) -> list[ast.Module | ast.ClassDef]:
    """A module and every class in it."""
    return [tree, *(n for n in ast.walk(tree) if isinstance(n, ast.ClassDef))]


def class_member_names(cls: ast.ClassDef) -> set[str]:
    """The names a class body defines or declares."""
    names = set()
    for node in cls.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)) and isinstance(
            node.target, ast.Name
        ):
            names.add(node.target.id)
    return names


def bare_enum_values(tree: ast.Module) -> set[str]:
    """The parameters and returns typed as a bare `EnumValue`, as `Class.method(parameter)`."""
    bare = set()
    for scope in scopes_of(tree):
        scope_name = scope.name if isinstance(scope, ast.ClassDef) else ""
        for func in scope.body:
            if not isinstance(func, ast.FunctionDef):
                continue
            key = f"{scope_name}.{func.name}" if scope_name else func.name
            args = func.args
            annotated = [
                (a.arg, a.annotation)
                for a in [
                    *args.posonlyargs,
                    *args.args,
                    *args.kwonlyargs,
                    args.vararg,
                    args.kwarg,
                ]
                if a is not None
            ]
            for name, node in [*annotated, ("return", func.returns)]:
                if node is not None and BARE_ENUM_VALUE.search(ast.unparse(node)):
                    bare.add(f"{key}({name})")
    return bare


def report_bare_enum_values(path: str) -> None:
    """List the parameters and returns that are still a bare `EnumValue` (a value of any
    enum), but for those the overlay says are."""
    import pathlib

    import annotation_overlays

    overlay = annotation_overlays.overlay_path("hou.py")
    bare = bare_enum_values(ast.parse(pathlib.Path(path).read_text()))
    bare -= bare_enum_values(ast.parse(overlay.read_text()))
    if bare:
        print(
            "EnumValues of unknown enum (type them in annotations/hou.pyi): "
            + ", ".join(sorted(bare))
        )


def apply_overlay(path: str) -> None:
    """Merge annotations/hou.pyi, the hand-maintained annotations, into the stub."""
    import pathlib

    import annotation_overlays

    overlay = annotation_overlays.overlay_path("hou.py")
    if not overlay.exists():
        return
    stub = pathlib.Path(path)
    merged = annotation_overlays.merge(stub.read_text(), overlay.read_text(), stub=True)
    if merged.unmatched:
        print(
            f"Overlay entries for hou that match nothing: {', '.join(merged.unmatched)}"
        )
    stub.write_text(merged.code)


if __name__ == "__main__":
    main(sys.argv[0])
