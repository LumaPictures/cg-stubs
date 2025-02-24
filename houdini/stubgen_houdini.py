from __future__ import absolute_import, annotations, division, print_function

import ast
import re
import textwrap
from functools import lru_cache

import mypy.stubgen
import mypy.stubgenc
import mypy.stubdoc
from mypy.stubgenc import FunctionContext, FunctionSig, SignatureGenerator

from hou_cleanup_config import (
    ADDITIONAL_ENUM_NAMES,
    EXPLICIT_DEFINITIONS,
    EXPLICIT_RETURN_TYPES,
    MISSING_DEFINITIONS,
    NON_OPTIONAL_RETURN_FUNCTIONS,
    NON_OPTIONAL_RETURN_TYPES,
    TYPE_ALIASES,
)

from stubgenlib import (
    AdvancedSignatureGenerator,
    AdvancedSigMatcher,
    SignatureFixer,
    CppTypeConverter,
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
                        elts=[new_node.slice, ast.Constant(value=Ellipsis)], ctx=ast.Load()
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


class DefaultSigGenerator(SignatureGenerator):
    """Sig Gen that uses the signature extracted from the source code"""

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        return [default_sig]


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
        (r"\bHOM_PtrOrNull\b", "Optional"),
        (r"\bHOM_OptionalDouble\b", "Optional[float]"),
        (r"\bHOM_OptionalInt\b", "Optional[int]"),
        (r"\bHOM_BinaryString\b", "bytes"),
        # HOM classes that have underscores
        (r"\bHOM_logging_LogEntry\b", "_logging_LogEntry"),
        (r"\bHOM_logging_MemorySink\b", "_logging_MemorySink"),
        (r"\bHOM_ik_Joint\b", "_ik_Joint"),
        (r"\bHOM_ik_Skeleton\b", "_ik_Skeleton"),
        (r"\bHOM_ik_Target\b", "_ik_Target"),
        (r"\bHOM_clone_Connection\b", "_clone_Connection"),
        (r"\bHOM_logging_FileSink\b", "\"_logging_FileSink\""),
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
    RESULT_TYPE_MAP = []

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
    def cpp_arg_to_py_type(self, cpp_type: str, is_result: bool, allow_optional_result: bool = True) -> str:
        """Reimplemented to provide an option to prevent pointer results from being Optional."""
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
            typestr = self.process_ptr(typestr, is_result, allow_optional_result)
        return typestr

    def process_ptr(self, converted_type: str, is_result: bool, allow_optional_result: bool = True) -> str:
        if is_result and allow_optional_result:
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

        class_name = ctx.class_info.name if ctx.class_info else None
        if is_result:
            explicit_return_type = EXPLICIT_RETURN_TYPES.get(class_name, {}).get(ctx.name)
            if explicit_return_type:
                return explicit_return_type

        allow_optional_result = ctx.name not in NON_OPTIONAL_RETURN_FUNCTIONS.get(class_name, {})

        new_type = self.converter.cpp_arg_to_py_type(type_name, is_result, allow_optional_result)

        # We need to indicate to the transformer whether we expect an argument (abstract) or
        # return (concrete) type for sequences, so set IsResult.is_set appropriately.
        # Since the transformer has a lot of indirect calls, setting this global scope override
        # allows us to change this behavior without redefining the whole transformer class.
        IsResult.is_set = is_result
        new_type = self.transfomer.transform(new_type)
        IsResult.is_set = False

        new_type = self.maybe_add_optional(new_type, default_value)

        return new_type


def get_signature_overrides() -> dict[str, str]:
    overrides = {}

    for cls, functions in EXPLICIT_DEFINITIONS.items():
        for function_name, function_spec in functions.items():
            if cls == "__hou__":
                # Modules at the root hou level
                key = f"hou.{function_name}"
            elif cls is not None:
                # Specific class overrides
                key = f"*.{cls}.{function_name}"
            else:
                # Overrides that should apply to all classes
                key = f"*.{function_name}"
            overrides[key] = function_spec

    return overrides


class HoudiniSignatureGenerator(AdvancedSignatureGenerator):
    sig_matcher = AdvancedSigMatcher(
        signature_overrides=get_signature_overrides()
    )


class ASTStubGenerator(mypy.stubgen.ASTStubGenerator):
    def visit_class_def(self, o) -> None:
        # filter _*Tuple classes, they are not used (See to_python_id).
        if (
            o.name in ("SwigPyIterator", "_AgentDefnMap")
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
        import hou

        # FIXME: Where do we want to pull Qt from?
        #  Houdini ships with PySide2 or PySide6 depending on the version.
        #  We could also use `Qt`, but that doesn't ship with Houdini.
        #  Is this the best way to get the PySide version?
        try:
            import PySide6
        except ImportError:
            pyside = "PySide2"
        else:
            pyside = "PySide6"

        # The import block goes at the top, so this is where we can add module level notes.
        imports = f"# Houdini stubs generated from Houdini {hou.applicationVersionString()}\n\n"

        imports += super().get_imports() + "\n"
        imports += "import datetime\n"
        imports += "import typing\n"
        imports += "from types import TracebackType\n"
        imports += ("from typing import Any, Callable, Dict, Iterator, Iterable, Mapping, "
                    "Literal, Optional, Sequence, Self, Union, Tuple, TypeAlias\n\n")
        imports += "import pxr.Sdf\n"
        imports += "import pxr.Usd\n"
        imports += f"from {pyside} import QtGui, QtWidgets\n\n"

        for type_alias_name, type_alias in TYPE_ALIASES.items():
            imports += f"{type_alias_name}: TypeAlias = {type_alias}\n"

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
        for line in textwrap.dedent(docstring).split('\n'):
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
                enum_name = line.rsplit('.', 1)[-1].strip()
                enum_names.add(enum_name)

        return enum_names

    def dedent(self) -> None:
        """When we exit the class, add any missing methods or enums we have flagged above.

        We override tlhis method to inject missing methods as we exit the class, because
        it is the only method on the generator called while the class context still exists.
        """
        if self._current_class:
            class_name = self._current_class.name
            for missing_definition in MISSING_DEFINITIONS.get(class_name, {}):
                self.add(textwrap.indent(f"{missing_definition}: ...\n", self._indent))

            enum_names = self.get_enums_from_docstring(self._current_class.docstring)
            enum_names.update(ADDITIONAL_ENUM_NAMES.get(class_name, {}))
            for enum_name in sorted(enum_names):
                self.add(f"{self._indent}{enum_name}: EnumValue = ...\n")
        super().dedent()

    def output(self) -> str:
        """Add module level missing imports to the end of the stub file."""
        for missing_definition in MISSING_DEFINITIONS.get(None, {}):
            self.add(textwrap.indent(f"{missing_definition}: ...\n", self._indent))
        return super().output()


mypy.stubgen.ASTStubGenerator = ASTStubGenerator  # type: ignore[attr-defined,misc]
# mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]


def enableHouModule():
    """Set up the environment so that "import hou" works."""
    import sys, os

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
        import hou
    finally:
        # Reset dlopen flags back to their original value.
        if hasattr(sys, "setdlopenflags"):
            sys.setdlopenflags(old_dlopen_flags)


enableHouModule()


def main(outdir: str):
    mypy.stubgen.main(
        ["-m=hou", "--verbose", "--parse-only", "--include-docstrings", "-o", outdir]
    )

    # print(AnnotationFixer().transform('Tuple[str, ...]'))
    # print(AnnotationFixer().transform('std.vector[str]'))
