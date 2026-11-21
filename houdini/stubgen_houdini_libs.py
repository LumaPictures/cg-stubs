"""Generate stubs for the Python modules Houdini ships alongside `hou`.

This covers everything in $HFS/houdini/pythonX.Ylibs except `hou` itself (see
stubgen_houdini.py): the compiled extensions (`_pdg`, `hapi`, ...) by inspecting them at
runtime, and the pure-python modules and packages (`pdg`, `toolutils`, `husd`, ...) from their
source.

Each top-level module becomes a PEP 561 stub-only package, `stubs/<name>-stubs`.

Must be run with hython, so that the compiled extensions can be imported.
"""

from __future__ import annotations

import ast
import copy
import enum
import functools
import importlib
import io
import os
import pathlib
import re
import shutil
import sys
import tempfile
import tokenize
import traceback
from types import ModuleType
from typing import Any, Iterable

import annotation_overlays
import libcst as cst
import mypy.moduleinspect
import mypy.stubdoc
import mypy.stubgen
import mypy.stubgenc
from mypy.nodes import (
    ClassDef,
    Decorator,
    Expression,
    FuncDef,
    ImportFrom,
    OverloadedFuncDef,
    SymbolNode,
)
from mypy.stubgenc import (
    ArgSig,
    ClassInfo,
    DocstringSignatureGenerator,
    FunctionContext,
    FunctionSig,
    SignatureGenerator,
)
from mypy.types import AnyType, CallableType, Type, get_proper_type

from stubgenlib.siggen import SignatureFixer

HERE = pathlib.Path(__file__).parent
STUBS_DIR = HERE / "stubs"

# Compiled extension modules, stubbed by runtime inspection.
COMPILED_MODULES = [
    "_alembic_hom_extensions",
    "_cop",
    "_gltf_hom_extensions",
    "_haio",
    "_houfs",
    "_houqt",
    "_houshfs",
    "_hwebserver",
    "_parsepeakusagelog",
    "_pdg",
    "_pdgd",
    "_pdgutils",
    "_texturepaint",
    "hapi",
    "hjson",
    # A USD schema module: Tf.PreparePythonModule() moves the contents of its compiled
    # _usdHoudini into the package, so it is the package that must be inspected.
    "husd.UsdHoudini",
    "mantra",
]

# Pure-python modules that are not stubbed from source.
SKIPPED_SOURCE_MODULES = {
    # Generated separately, by stubgen_houdini.py.
    "hou",
}

# Pure-python files that are not stubbed from source, because they are in COMPILED_MODULES.
SKIPPED_SOURCE_FILES = {
    "husd/UsdHoudini/__init__.py",
}

# Stubs that are maintained by hand rather than generated.
HAND_WRITTEN_STUBS = {
    "hou-stubs",
    "houtypes-stubs",
}

# Prefixes that pybind11 leaves on C++ class names it could not map to a python class.
CPP_CLASS_PREFIX = re.compile(r"\b(?:PDGD|PDGT|PDG|PYPDG)_(\w+)\b")

# C++ container and value types that leak into signatures, as (pattern, arg type, result type).
CPP_TYPE_SUBS: list[tuple[re.Pattern[str], str, str]] = [
    (re.compile(r"\bUT_Array\["), "Sequence[", "list["),
    (re.compile(r"\bUT_Set\["), "set[", "set["),
    (re.compile(r"\bUT_OptionsHolder\b"), "dict[str, Any]", "dict[str, Any]"),
    (re.compile(r"\bUT_(?:StringHolder|StringRef|StringView)\b"), "str", "str"),
]

OBJECT_TYPE = re.compile(r"\bobject\b")


def libs_dir() -> pathlib.Path:
    version = f"python{sys.version_info.major}.{sys.version_info.minor}libs"
    return pathlib.Path(os.environ["HFS"]) / "houdini" / version


def drop_defaults_before_required(sig: FunctionSig) -> FunctionSig:
    """Remove defaults from positional args that are followed by a required positional arg.

    nanobind documents an optional leading arg (e.g. hapi's `session: Session | None = None`)
    ahead of required ones, which is not valid python.  The arg can only be omitted when the
    rest are passed by keyword, so typing it as required is the closest valid signature.
    """
    args = list(sig.args)
    seen_required = False
    for i in reversed(range(len(args))):
        arg = args[i]
        if arg.name.startswith("*") or arg.name == "/":
            # Everything after a star arg is keyword-only, so its defaults don't matter here.
            seen_required = False
            continue
        if not arg.default:
            seen_required = True
        elif seen_required:
            args[i] = ArgSig(arg.name, arg.type, default=False)
    return sig._replace(args=args)


class HoudiniLibsTypeFixer(SignatureFixer):
    """Map the C++ type names that pybind11 and nanobind leave in docstrings to python types."""

    def resolve_cpp_class(self, module_name: str, class_name: str) -> str:
        module = sys.modules.get(module_name)
        if module is not None and isinstance(getattr(module, class_name, None), type):
            return class_name
        for other in ("_pdg", "_pdgd"):
            if other == module_name:
                continue
            other_module = importlib.import_module(other)
            if isinstance(getattr(other_module, class_name, None), type):
                return f"{other}.{class_name}"
        return "Any"

    def fix_type(self, type_name: str, module_name: str, is_result: bool) -> str:
        type_name = CPP_CLASS_PREFIX.sub(
            lambda m: self.resolve_cpp_class(module_name, m.group(1)), type_name
        )
        for pattern, arg_type, result_type in CPP_TYPE_SUBS:
            type_name = pattern.sub(result_type if is_result else arg_type, type_name)
        if is_result:
            type_name = OBJECT_TYPE.sub("Any", type_name)
        return type_name

    def cleanup_type(
        self,
        type_name: str,
        ctx: FunctionContext,
        is_result: bool,
        default_value: str | None = None,
    ) -> str:
        return self.fix_type(type_name, ctx.module_name, is_result)

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        sigs = super().get_function_sig(default_sig, ctx)
        if sigs:
            sigs = [drop_defaults_before_required(sig) for sig in sigs]
        return sigs

    def get_property_type(
        self, default_type: str | None, ctx: FunctionContext
    ) -> str | None:
        prop_type = self.sig_gen.get_property_type(default_type, ctx)
        if prop_type:
            prop_type = self.fix_type(prop_type, ctx.module_name, is_result=True)
        return prop_type


CPP_SCOPED_NAME = re.compile(r"\b(\w+)::(\w+)\b")
CPP_NAME_PREFIX = re.compile(r"^(?:PDGD|PDGT|PDGN|PDG|PYPDG)_")


def python_name_of_scoped(module_name: str, outer: str, inner: str) -> str | None:
    """The python name of a scoped C++ name a pybind11 docstring gives (`PDGN::PDGN_Message`
    for `_pdgutils.PDGNMessage`, `PDGD_Message::PDGD_MessageType` for
    `_pdgd.Message.MessageType`)."""
    module = sys.modules.get(module_name)
    outer_name = CPP_NAME_PREFIX.sub("", outer)
    inner_name = CPP_NAME_PREFIX.sub("", inner)
    for candidate in (f"{outer_name}.{inner_name}", f"{outer_name}{inner_name}"):
        obj: Any = module
        for part in candidate.split("."):
            obj = getattr(obj, part, None)
        if isinstance(obj, type):
            # Qualified, or stubgen would import `Message` of `Message.MessageType` as a module.
            return f"{module_name}.{candidate}"
    return None


class CppScopedDocstringSignatureGenerator(DocstringSignatureGenerator):
    """Read the signatures whose types pybind11 leaves as scoped C++ names, which mypy's
    docstring parser rejects, by naming their python classes instead."""

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        if ctx.docstring and "::" in ctx.docstring:
            ctx = copy.copy(ctx)
            ctx.docstring = CPP_SCOPED_NAME.sub(
                lambda m: python_name_of_scoped(ctx.module_name, m.group(1), m.group(2))
                or m.group(0),
                ctx.docstring,
            )
        return super().get_function_sig(default_sig, ctx)


# Compiled USD schema modules.  Their Boost.Python functions have no docstrings, so their
# signatures come from USD's naming conventions instead (see UsdSchemaSignatureGenerator).
USD_SCHEMA_MODULES = {"husd.UsdHoudini"}

# Signatures of the methods that USD generates for schema classes, by method name pattern.
# `{cls}` is the schema class.  Multiple-apply API schemas take an instance name as well.
USD_SCHEMA_SIGNATURES: list[tuple[re.Pattern[str], list[str], list[str]]] = [
    # (pattern, single-apply or typed schema signatures, multiple-apply schema signatures)
    (
        re.compile(r"__init__"),
        [
            "(self) -> None",
            "(self, prim: pxr.Usd.Prim) -> None",
            "(self, schemaObj: pxr.Usd.SchemaBase) -> None",
        ],
        [
            "(self) -> None",
            "(self, prim: pxr.Usd.Prim, name: str) -> None",
            "(self, schemaObj: pxr.Usd.SchemaBase, name: str) -> None",
        ],
    ),
    (
        re.compile(r"Get"),
        ["(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> {cls}"],
        [
            "(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> {cls}",
            "(prim: pxr.Usd.Prim, name: str) -> {cls}",
        ],
    ),
    (
        re.compile(r"Define"),
        ["(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> {cls}"],
        ["(stage: pxr.Usd.Stage, path: pxr.Sdf.Path | str) -> {cls}"],
    ),
    (
        re.compile(r"Apply"),
        ["(prim: pxr.Usd.Prim) -> {cls}"],
        ["(prim: pxr.Usd.Prim, name: str) -> {cls}"],
    ),
    (
        re.compile(r"CanApply"),
        ["(prim: pxr.Usd.Prim) -> _CanApplyResult"],
        ["(prim: pxr.Usd.Prim, name: str) -> _CanApplyResult"],
    ),
    (re.compile(r"GetAll"), [], ["(prim: pxr.Usd.Prim) -> list[{cls}]"]),
    (re.compile(r"Is\w+Path"), [], ["(path: pxr.Sdf.Path | str) -> bool"]),
    (
        re.compile(r"GetSchemaAttributeNames"),
        ["(includeInherited: bool = ...) -> list[str]"],
        ["(includeInherited: bool = ..., instanceName: str = ...) -> list[str]"],
    ),
    (
        re.compile(r"Get\w+Attr"),
        ["(self) -> pxr.Usd.Attribute"],
        ["(self) -> pxr.Usd.Attribute"],
    ),
    (
        re.compile(r"Create\w+Attr"),
        [
            "(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute"
        ],
        [
            "(self, defaultValue: Any = ..., writeSparsely: bool = ...) -> pxr.Usd.Attribute"
        ],
    ),
    (
        re.compile(r"(?:Get|Create)\w+Rel"),
        ["(self) -> pxr.Usd.Relationship"],
        ["(self) -> pxr.Usd.Relationship"],
    ),
    (re.compile(r"__bool__"), ["(self) -> bool"], ["(self) -> bool"]),
]


class UsdSchemaSignatureGenerator(SignatureGenerator):
    """Signatures for the methods of USD schema classes, from USD's naming conventions."""

    def get_function_sig(
        self, default_sig: FunctionSig, ctx: FunctionContext
    ) -> list[FunctionSig] | None:
        cls = ctx.class_info.cls if ctx.class_info else None
        if ctx.module_name not in USD_SCHEMA_MODULES or cls is None:
            return None
        if not any(base.__name__ == "SchemaBase" for base in cls.__mro__):
            return None
        multiple_apply = hasattr(cls, "GetAll")
        for pattern, single_sigs, multiple_sigs in USD_SCHEMA_SIGNATURES:
            if pattern.fullmatch(ctx.name):
                sigs = multiple_sigs if multiple_apply else single_sigs
                if not sigs:
                    return None
                docstring = "\n".join(
                    ctx.name + sig.format(cls=cls.__name__) for sig in sigs
                )
                return mypy.stubdoc.infer_sig_from_docstring(docstring, ctx.name)
        return None

    def get_property_type(
        self, default_type: str | None, ctx: FunctionContext
    ) -> str | None:
        if ctx.module_name in USD_SCHEMA_MODULES and ctx.class_info:
            if ctx.class_info.name == "Tokens":
                return "str"
            if ctx.class_info.name == "_CanApplyResult" and ctx.name == "whyNot":
                return "str"
        return None


def is_nanobind_routine(obj: object) -> bool:
    return type(obj).__name__ in ("nb_func", "nb_method")


# Compiled modules whose classes report another module as theirs.  _houqt's classes are
# `hou.qt.QT_Gallery` etc. (houpythonportion.qt adds some to hou.qt), but hou.qt does not have
# them all, so they are stubbed in _houqt.
CLASS_MODULE_ALIASES = {"_houqt": "hou.qt"}


class InspectionStubGenerator(mypy.stubgenc.InspectionStubGenerator):
    def __init__(self, module_name: str, *args: Any, **kwargs: Any) -> None:
        super().__init__(module_name, *args, **kwargs)
        if module_name in USD_SCHEMA_MODULES:
            # A python package, but its contents come from a Boost.Python extension.
            self.is_c_module = True

    def get_obj_module(self, obj: object) -> str | None:
        module = super().get_obj_module(obj)
        if module is not None and module == CLASS_MODULE_ALIASES.get(self.module_name):
            return self.module_name
        return module

    def get_sig_generators(self) -> list[SignatureGenerator]:
        return [
            UsdSchemaSignatureGenerator(),
            HoudiniLibsTypeFixer(
                CppScopedDocstringSignatureGenerator(), default_sig_handling="merge"
            ),
        ]

    def get_members(self, obj: object) -> list[tuple[str, Any]]:
        # _pdgd registers a class under a name with spaces, which cannot be written in a stub.
        return [
            (name, value)
            for name, value in super().get_members(obj)
            if name.isidentifier()
        ]

    def is_function(self, obj: object) -> bool:
        return super().is_function(obj) or is_nanobind_routine(obj)

    def is_method(self, class_info: ClassInfo, name: str, obj: object) -> bool:
        return super().is_method(class_info, name, obj) or is_nanobind_routine(obj)

    def strip_or_import(self, type_name: str) -> str:
        # Types from the other pdg extensions are referenced by module, so import it.
        module, _, _ = type_name.rpartition(".")
        if module in ("_pdg", "_pdgd") and module != self.module_name:
            self.import_tracker.add_import(module)
            return type_name
        return super().strip_or_import(type_name)


class ASTStubGenerator(mypy.stubgen.ASTStubGenerator):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._in_method = False
        self._overlay_private_names: set[str] | None = None

    def visit_import_from(self, o: ImportFrom) -> None:
        super().visit_import_from(o)
        # An overlay's `from m import X as X` re-exports X, for code that uses it through this
        # module.  The source's own `from m import X`, merged in after it, would otherwise undo
        # the alias.
        for name, as_name in o.names:
            if as_name == name:
                self.import_tracker.reexport(name)

    def is_not_in_all(self, name: str) -> bool:
        # `__all__` only limits `import *`: a module's other public definitions are still its
        # API (`hud.hudCommand(...)`), and a stub exports every public name it defines.
        return False

    def is_private_name(self, name: str, fullname: str | None = None) -> bool:
        if not super().is_private_name(name, fullname):
            return False
        # Keep the private names an overlay declares: they are used from outside the module
        # (by SideFX's HDAs, states and subclasses).
        qualname = ".".join([*(c.name for c in self._class_stack), name])
        return qualname not in self.overlay_private_names()

    def overlay_private_names(self) -> set[str]:
        """The qualified names of the private definitions the module's overlay declares."""
        if self._overlay_private_names is None:
            self._overlay_private_names = set()
            path = getattr(self, "path", None)
            overlay = annotation_overlays.overlay_path(path) if path else None
            if overlay is not None and overlay.exists():
                parsed = annotation_overlays.Overlay.parse(overlay.read_text())
                self._overlay_private_names = {
                    qualname
                    for qualname in [
                        *parsed.functions,
                        *parsed.overloads,
                        *parsed.variables,
                    ]
                    if qualname.rpartition(".")[2].startswith("_")
                    and not qualname.endswith("__")
                }
        return self._overlay_private_names

    def visit_func_def(self, o: FuncDef) -> None:
        # The only initializers stubgen generates while visiting a method are its
        # `self.x = ...` assignments (see get_init).
        self._in_method = True
        try:
            super().visit_func_def(o)
        finally:
            self._in_method = False

    def get_init(
        self, lvalue: str, rvalue: Expression, annotation: Type | None = None
    ) -> str | None:
        # stubgen declares a dataclass's unannotated `self.x = ...` assignments as `x = ...`,
        # which overrides the type of a field the dataclass inherits with EllipsisType.
        info = self._current_class.info if self._current_class else None
        if (
            self._in_method
            and annotation is None
            and info is not None
            and any(
                lvalue in base.names
                and (self.processing_dataclass or is_property(base.names[lvalue].node))
                for base in info.mro[1:]
            )
        ):
            return None
        return super().get_init(lvalue, rvalue, annotation)

    def _get_func_args(self, o: FuncDef, ctx: FunctionContext) -> list[ArgSig]:
        args = super()._get_func_args(o, ctx)
        # stubgen drops the annotation of `self` and `cls`, which overloads use to pick a
        # signature by the class they are called on (`cls: type[_P]`).
        if args and o.arguments and isinstance(o.unanalyzed_type, CallableType):
            first = o.unanalyzed_type.arg_types[0]
            if (
                args[0].name in ("self", "cls")
                and first is not None
                and not isinstance(get_proper_type(first), AnyType)
            ):
                args[0] = ArgSig(
                    args[0].name,
                    self.print_annotation(first),
                    default=args[0].default,
                    default_value=args[0].default_value,
                )
        # Houdini's sources rely on implicit Optional (`x: int = None`), which type checkers
        # no longer allow, so make it explicit.
        return [
            ArgSig(arg.name, f"{arg.type} | None", default=True, default_value="None")
            if arg.default_value == "None" and arg.type and not accepts_none(arg.type)
            else arg
            for arg in args
        ]


def is_property(node: SymbolNode | None) -> bool:
    """Whether a class member is a property, which a subclass's `self.x = ...` sets.

    stubgen would otherwise declare an attribute that overrides the property.
    """
    if isinstance(node, Decorator):
        return node.func.is_property
    if isinstance(node, (FuncDef, OverloadedFuncDef)):
        return node.is_property
    return False


def accepts_none(type_name: str) -> bool:
    return any(
        re.fullmatch(r"None|(?:typing\.)?(?:Optional\[.*\]|Any)|object", member.strip())
        for member in split_union(type_name)
    )


def split_union(type_name: str) -> list[str]:
    """Split a type at its top-level `|`s."""
    members = []
    depth = 0
    start = 0
    for i, char in enumerate(type_name):
        if char in "[(":
            depth += 1
        elif char in "])":
            depth -= 1
        elif char == "|" and depth == 0:
            members.append(type_name[start:i])
            start = i + 1
    members.append(type_name[start:])
    return members


class SelfTraverser(mypy.stubgen.SelfTraverser):
    """Find a method's `self.x = ...` assignments, but not those of a class nested in it.

    stubgen otherwise declares a nested class's attributes on the class of the method.
    """

    def __init__(self) -> None:
        super().__init__()
        self._root: FuncDef | None = None

    def visit_class_def(self, o: ClassDef) -> None:
        pass

    def visit_func_def(self, o: FuncDef) -> None:
        if self._root is None:
            self._root = o
        elif any(arg.variable.name == "self" for arg in o.arguments):
            # A nested function with its own `self` (e.g. a monkeypatched method).
            return
        super().visit_func_def(o)


class InProcessModuleInspect:
    """Inspect modules in this process, rather than in a subprocess as stubgen does.

    The subprocess cannot be started from hython, and would not have PySide6 loaded, which
    _houqt needs.
    """

    def __enter__(self) -> InProcessModuleInspect:
        return self

    def __exit__(self, *args: object) -> None:
        pass

    def get_package_properties(
        self, package_id: str
    ) -> mypy.moduleinspect.ModuleProperties:
        return mypy.moduleinspect.get_package_properties(package_id)


mypy.stubgen.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]
mypy.stubgenc.InspectionStubGenerator = InspectionStubGenerator  # type: ignore[misc]
mypy.stubgen.ASTStubGenerator = ASTStubGenerator  # type: ignore[misc]
mypy.stubgen.ModuleInspect = InProcessModuleInspect  # type: ignore[misc,assignment]
mypy.stubgen.SelfTraverser = SelfTraverser  # type: ignore[misc]


def stage_sources(libs: pathlib.Path, staging: pathlib.Path) -> list[str]:
    """Stage the pure-python modules to stub in `staging`, and return their files.

    The annotation overlays are merged in (see annotation_overlays.py).  Namespace packages
    (directories without an __init__.py, such as `cop` and `sop`) are given one: stubgen names
    a module after its nearest __init__.py, so it would otherwise mistake `cop/stateutils.py`
    for a top-level `stateutils`, and fail on its relative imports.
    """
    staged = annotation_overlays.stage_tree(
        libs, staging, skip=SKIPPED_SOURCE_MODULES, namespace_inits=True
    )
    resolve_version_checks(staging, staged.files)
    for rel, error in staged.errors.items():
        print(f"Could not apply the overlay for {rel}: {error}")
    for rel, unmatched in staged.unmatched.items():
        # A skipped file's overlay is for its compiled module (see apply_compiled_overlay).
        if rel not in SKIPPED_SOURCE_FILES:
            print(
                f"Overlay entries for {rel} that match nothing: {', '.join(unmatched)}"
            )
    return [f for f in staged.files if f not in SKIPPED_SOURCE_FILES]


def run_stubgen(args: list[str]) -> None:
    try:
        mypy.stubgen.main(args)
    except SystemExit as exc:
        if exc.code:
            raise


def import_compiled_modules() -> list[str]:
    """Import the compiled modules up front, so a failure says why rather than skipping them."""
    if "PySide6" not in sys.modules:
        # _houqt links against shiboken, which is only loaded once PySide6 is.
        importlib.import_module("PySide6.QtWidgets")
    found = []
    for name in COMPILED_MODULES:
        try:
            importlib.import_module(name)
        except ImportError as exc:
            print(f"Skipping {name}: {exc}")
        else:
            found.append(name)
    return found


def module_name_of(rel: pathlib.Path) -> str:
    parts = list(rel.with_suffix("").parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def package_stubs(
    raw_dir: pathlib.Path, compiled: Iterable[str], staging: pathlib.Path
) -> None:
    """Move stubgen's output into one `<name>-stubs` package per top-level module."""
    for stale in STUBS_DIR.glob("*-stubs"):
        if stale.name not in HAND_WRITTEN_STUBS:
            shutil.rmtree(stale)

    for path in sorted(raw_dir.rglob("*.pyi")):
        rel = path.relative_to(raw_dir)
        top = rel.parts[0].removesuffix(".pyi")
        package = STUBS_DIR / f"{top}-stubs"
        if len(rel.parts) == 1:
            dest = package / "__init__.pyi"
        else:
            dest = package.joinpath(*rel.parts[1:])
        dest.parent.mkdir(parents=True, exist_ok=True)
        module_name = module_name_of(rel)
        text = path.read_text()
        if module_name in compiled:
            text = apply_compiled_overlay(
                fix_compiled_stub(text, sys.modules[module_name]), module_name
            )
            text = drop_callable_attributes_of_methods(text)
            text = prune_unreachable_overloads(text)
            text = fix_nested_enums(text, sys.modules[module_name])
            text = drop_unsigned_methods(text, sys.modules[module_name])
            text = parameterize_compiled_generics(text, sys.modules[module_name])
            text = type_enum_format(text)
            text = type_constructors(text, sys.modules[module_name])
        else:
            text = fix_source_annotations(remove_undefined_private_decorators(text))
            source = staging / rel.with_suffix(".py")
            if source.exists():
                source_text = source.read_text(errors="replace")
                text = restore_type_definitions(text, source_text)
                text = restore_enum_auto_values(text, source_text)
            text = fix_class_bodies(text)
            overlay = annotation_overlays.overlay_path(str(rel.with_suffix(".py")))
            if overlay.exists():
                text = apply_overlay_type_ignores(text, overlay.read_text())
            if rel.name == "__init__.pyi":
                text = import_all_submodules(text, staging / rel.parent)
            text = unexport_houtypes(text)
            text = elide_container_defaults(text)
            text = reexport_rebound_builtins(text)
        text = ignore_pep728_keywords(text)
        text = OBJECT_ADDRESS.sub(">", text)
        dest.write_text(add_missing_imports(text))

    for package in STUBS_DIR.glob("*-stubs"):
        if package.name in HAND_WRITTEN_STUBS:
            continue
        # Namespace packages, and packages whose __init__ only has an implicit stub.
        for directory in [package, *(d for d in package.rglob("*") if d.is_dir())]:
            init = directory / "__init__.pyi"
            if not init.exists():
                init.write_text("")
        (package / "py.typed").touch()

    add_reexports(staging)


TYPE_FACTORIES = {"TypeVar", "ParamSpec", "TypeVarTuple", "NewType"}


GENERIC_TYPES = {
    "Annotated",
    "Callable",
    "ClassVar",
    "Collection",
    "Container",
    "DefaultDict",
    "Deque",
    "Dict",
    "FrozenSet",
    "Generator",
    "Iterable",
    "Iterator",
    "List",
    "Literal",
    "Mapping",
    "MutableMapping",
    "MutableSequence",
    "MutableSet",
    "Optional",
    "Sequence",
    "Set",
    "Tuple",
    "Type",
    "Union",
    "dict",
    "frozenset",
    "list",
    "set",
    "tuple",
    "type",
}
BUILTIN_TYPES = {"bool", "bytes", "complex", "float", "int", "object", "str", "None"}


def is_type_expression(node: ast.expr) -> bool:
    """Whether a value is clearly a type, as in an implicit alias (`Kind = Literal["a", "b"]`)."""
    if isinstance(node, ast.Subscript):
        base = node.value
        name = (
            base.attr if isinstance(base, ast.Attribute) else getattr(base, "id", None)
        )
        return name in GENERIC_TYPES
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
        return all(
            is_type_expression(side)
            or (isinstance(side, ast.Name) and side.id[:1].isupper())
            or isinstance(side, ast.Attribute)
            for side in (node.left, node.right)
        )
    if isinstance(node, ast.Constant):
        return node.value is None
    return isinstance(node, ast.Name) and node.id in BUILTIN_TYPES


def restore_type_definitions(stub: str, source: str) -> str:
    """Restore the module-level type definitions that stubgen drops or empties.

    stubgen leaves out private TypeVars and ParamSpecs (`_T = TypeVar("_T")`), and reduces
    `Alias: TypeAlias = int | str` to `Alias: TypeAlias`.  Annotation overlays use both.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return stub
    definitions = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            func = node.value.func
            name = (
                func.attr
                if isinstance(func, ast.Attribute)
                else getattr(func, "id", None)
            )
            if name in TYPE_FACTORIES:
                definitions.append(
                    (ast.unparse(node.targets[0]), ast.unparse(node), name)
                )
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            if ast.unparse(node.annotation).endswith("TypeAlias"):
                definitions.append(
                    (ast.unparse(node.target), ast.unparse(node), "TypeAlias")
                )
        elif isinstance(node, ast.TypeAlias):
            definitions.append((node.name.id, ast.unparse(node), None))
    code = strip_docstrings(stub)
    for node in tree.body:
        # Implicit aliases (`_Info = tuple[str, int]`), which stubgen drops when private.
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and isinstance(node.value, (ast.Subscript, ast.BinOp))
        ):
            name = node.targets[0].id
            used = re.search(rf"(?<![\w.]){name}\b", code)
            dropped = used and not re.search(rf"^{name}\s*[:=]", code, re.MULTILINE)
            # A public alias stubgen kept, but as `Name: Incomplete`.
            emptied = re.search(
                rf"^{name}: Incomplete$", code, re.MULTILINE
            ) and is_type_expression(node.value)
            if dropped or emptied:
                value = ast.unparse(node.value)
                definitions.append((name, f"{name}: TypeAlias = {value}", "TypeAlias"))
        # Star imports, which stubgen leaves out; in a stub they re-export the module's names.
        elif isinstance(node, ast.ImportFrom) and any(
            a.name == "*" for a in node.names
        ):
            statement = ast.unparse(node)
            if statement not in code:
                definitions.append(("", statement, None))
    # A name defined more than once keeps its last definition, as at runtime.
    last = {name: i for i, (name, _, _) in enumerate(definitions) if name}
    definitions = [d for i, d in enumerate(definitions) if not d[0] or last[d[0]] == i]
    lines = stub.splitlines()
    if any(name for name, _, _ in definitions):
        names = {name for name, _, _ in definitions if name}
        # Drop stubgen's versions: emptied aliases, and any definitions it did keep.
        lines = [
            line
            for line in lines
            if not re.match(rf"^({'|'.join(map(re.escape, names))})\s*(?::|=)", line)
        ]
    helpers = dropped_helper_classes(
        "\n".join(lines) + "\n".join(c for _, c, _ in definitions), tree
    )
    if not definitions and not helpers:
        return stub
    lines.extend(helpers)
    imports = sorted(
        {f"from typing import {kind}" for _, _, kind in definitions if kind}
    )
    imports += source_imports_for(
        [c for _, c, _ in definitions] + helpers, "\n".join(lines), tree
    )
    body = "\n".join(lines)
    insert = "\n".join([*imports, *(code for _, code, _ in definitions)])
    # After the imports at the top of the stub.
    index = 0
    for i, line in enumerate(lines):
        if (
            line.startswith(("import ", "from "))
            or not line.strip()
            or line.startswith("#")
        ):
            index = i + 1
        else:
            break
    return (
        "\n".join([*lines[:index], insert, *lines[index:]]) + "\n"
        if body
        else insert + "\n"
    )


def is_auto_call(node: ast.expr) -> bool:
    return (
        isinstance(node, ast.Call)
        and not node.args
        and not node.keywords
        and (
            (isinstance(node.func, ast.Name) and node.func.id == "auto")
            or (isinstance(node.func, ast.Attribute) and node.func.attr == "auto")
        )
    )


def class_bodies(
    body: list[ast.stmt], scope: tuple[str, ...] = ()
) -> Iterable[tuple[tuple[str, ...], ast.ClassDef]]:
    """Every class in a module body, nested ones included, with its qualified name."""
    for node in body:
        if isinstance(node, ast.ClassDef):
            yield (*scope, node.name), node
            yield from class_bodies(node.body, (*scope, node.name))


# Enum members that share a name with an Enum property, whose assignment mypy reports as
# incompatible with the property's type (whatever the value).
ENUM_PROPERTY_NAMES = {"name", "value"}
ENUM_BASE = re.compile(r"\b(?:Enum|IntEnum|StrEnum|Flag|IntFlag|ReprEnum)$")


def restore_enum_auto_values(stub: str, source: str) -> str:
    """Write the enum members that the source assigns `auto()` as `enum.auto()`.

    stubgen writes them as `member = ...`, which loses the type of the member's value.  It
    writes combined flags as their expression, which type checkers take for a type alias, so
    those become `member = ...`.
    """
    try:
        source_tree = ast.parse(source)
        stub_tree = ast.parse(stub)
    except SyntaxError:
        return stub
    auto_members: dict[tuple[str, ...], set[str]] = {
        qualname: {
            target.id
            for item in cls.body
            if isinstance(item, ast.Assign) and is_auto_call(item.value)
            for target in item.targets
            if isinstance(target, ast.Name)
        }
        for qualname, cls in class_bodies(source_tree.body)
    }
    lines = stub.splitlines()
    for qualname, cls in class_bodies(stub_tree.body):
        if any(ENUM_BASE.search(ast.unparse(base)) for base in cls.bases):
            for item in cls.body:
                # A combination of flags (`NE = N | E`), which type checkers take for a type.
                if isinstance(item, ast.Assign) and isinstance(item.value, ast.BinOp):
                    line = lines[item.lineno - 1]
                    lines[item.lineno - 1] = line[: item.value.col_offset] + "..."
        names = auto_members.get(qualname)
        if not names:
            continue
        for item in cls.body:
            if (
                isinstance(item, ast.Assign)
                and len(item.targets) == 1
                and isinstance(item.targets[0], ast.Name)
                and item.targets[0].id in names
                and isinstance(item.value, ast.Constant)
                and item.value.value is Ellipsis
            ):
                name = item.targets[0].id
                ignore = (
                    "  # type: ignore[assignment]"
                    if name in ENUM_PROPERTY_NAMES
                    else ""
                )
                indent = " " * item.col_offset
                lines[item.lineno - 1] = f"{indent}{name} = enum.auto(){ignore}"
    return "\n".join(lines) + "\n"


SELF_NAMES = {"self", "cls", "mcs", "mcls", "metacls", "klass"}
ACCESSOR_DECORATORS = {"setter", "getter", "deleter", "register"}


def decorator_names(
    node: ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef,
) -> set[str]:
    names = set()
    for decorator in node.decorator_list:
        target = decorator.func if isinstance(decorator, ast.Call) else decorator
        if isinstance(target, ast.Attribute):
            names.add(target.attr)
        elif isinstance(target, ast.Name):
            names.add(target.id)
    return names


def first_line(node: ast.stmt) -> int:
    decorators = getattr(node, "decorator_list", [])
    return min([node.lineno, *(d.lineno for d in decorators)])


def all_bodies(
    tree: ast.Module,
) -> Iterable[tuple[ast.ClassDef | None, list[ast.stmt]]]:
    yield None, tree.body
    for _, cls in class_bodies(tree.body):
        yield cls, cls.body


def defined_names(node: ast.stmt) -> list[str]:
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
        return [node.name]
    if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
        return [node.target.id]
    if isinstance(node, ast.Assign):
        return [t.id for t in node.targets if isinstance(t, ast.Name)]
    return []


def drop_redefinitions(text: str) -> str:
    """Keep only the last definition of a name that a scope defines more than once.

    That is the one Python ends up with (e.g. a method that replaces a class attribute of the
    same name); type checkers reject the redefinition.
    """
    tree = ast.parse(text)
    removed: list[tuple[int, int]] = []
    special = {"overload", "property", "cached_property", *ACCESSOR_DECORATORS}
    for _, body in all_bodies(tree):
        by_name: dict[str, list[ast.stmt]] = {}
        for node in body:
            for name in defined_names(node):
                by_name.setdefault(name, []).append(node)
        for nodes in by_name.values():
            # A declaration followed by an assignment (`x: int` then `x = y`) is fine.
            if (
                len(nodes) < 2
                or not isinstance(
                    nodes[-1], (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
                )
                or any(
                    isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                    and decorator_names(n) & special
                    for n in nodes
                )
            ):
                continue
            removed += [
                (first_line(n), n.end_lineno or n.lineno)
                for n in nodes[:-1]
                if len(defined_names(n)) == 1
            ]
    if not removed:
        return text
    lines = text.splitlines()
    for start, end in sorted(set(removed), reverse=True):
        del lines[start - 1 : end]
    return "\n".join(lines) + "\n"


def add_missing_staticmethods(text: str) -> str:
    """Mark the methods that take no `self` as static.

    Some of Houdini's classes have helpers that are only called through the class (or used as
    decorators in its body), without `@staticmethod`.
    """
    tree = ast.parse(text)
    inserts: list[tuple[int, str]] = []
    for cls, body in all_bodies(tree):
        if cls is None:
            continue
        for node in body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name.startswith("__") or decorator_names(node) & {
                "staticmethod",
                "classmethod",
                "property",
                "cached_property",
                *ACCESSOR_DECORATORS,
            }:
                continue
            positional = [*node.args.posonlyargs, *node.args.args]
            if positional:
                first = positional[0]
                annotation = ast.unparse(first.annotation) if first.annotation else ""
                if (
                    first.arg in SELF_NAMES
                    or not annotation
                    or re.search(rf"\b(?:{cls.name}|Self)\b", annotation)
                ):
                    continue
            elif node.args.vararg:
                continue
            inserts.append((first_line(node), " " * node.col_offset + "@staticmethod"))
    if not inserts:
        return text
    lines = text.splitlines()
    for line, code in sorted(inserts, reverse=True):
        lines.insert(line - 1, code)
    return "\n".join(lines) + "\n"


def subclass_new_results(text: str) -> str:
    """Make a class whose `__new__` returns another class's instance a subclass of it.

    Some of Houdini's classes are factories: `hou.qt.Dialog()` returns a `QDialog`.  Type
    checkers other than pyright reject a `__new__` that returns an unrelated type, and fall
    back to the class itself, so describe the result as an instance of the class.
    """
    tree = ast.parse(text)
    lines = text.splitlines()
    changed = False
    removed: list[tuple[int, int]] = []
    module_classes = {n.name: n for n in tree.body if isinstance(n, ast.ClassDef)}
    for _, cls in class_bodies(tree.body):
        if any(not (isinstance(b, ast.Name) and b.id == "object") for b in cls.bases):
            continue
        for node in cls.body:
            if not (
                isinstance(node, ast.FunctionDef)
                and node.name == "__new__"
                and isinstance(node.returns, (ast.Name, ast.Attribute))
                and node.returns.lineno == node.returns.end_lineno
            ):
                continue
            result = ast.unparse(node.returns)
            if result in (cls.name, "Self", "typing.Self") or result.startswith(
                cls.name + "."
            ):
                continue
            line = lines[node.returns.lineno - 1]
            lines[node.returns.lineno - 1] = (
                line[: node.returns.col_offset]
                + "Self"
                + line[node.returns.end_col_offset :]
            )
            # `Self` cannot be combined with an annotated `cls`.
            first = (node.args.posonlyargs + node.args.args)[:1]
            if first and first[0].annotation and first[0].lineno == first[0].end_lineno:
                arg = first[0]
                line = lines[arg.lineno - 1]
                lines[arg.lineno - 1] = (
                    line[: arg.col_offset] + arg.arg + line[arg.end_col_offset :]
                )
            # Methods the factory binds onto its result (ParmDialog.setNode) are the result's.
            result_class = module_classes.get(result)
            if result_class is not None:
                result_methods = {
                    n.name for n in result_class.body if isinstance(n, ast.FunctionDef)
                }
                removed += [
                    (first_line(n), n.end_lineno or n.lineno)
                    for n in cls.body
                    if isinstance(n, ast.FunctionDef)
                    and n.name in result_methods
                    and n.name != "__new__"
                ]
            class_line = lines[cls.lineno - 1]
            lines[cls.lineno - 1] = re.sub(
                rf"\bclass {cls.name}\b(?:\(\s*(?:object)?\s*\))?",
                f"class {cls.name}({result})",
                class_line,
                count=1,
            )
            changed = True
    for start, end in sorted(removed, reverse=True):
        del lines[start - 1 : end]
    return "\n".join(lines) + "\n" if changed else text


def move_attributes_after_nested_classes(text: str) -> str:
    """Declare the attributes typed with a nested class after the nested classes.

    mypy fails to resolve `Outer.Nested` in an attribute declared before `Nested` when the
    module is part of a large import cycle (e.g. curvestate.drawablemanager).
    """
    while True:
        tree = ast.parse(text)
        for _, cls in class_bodies(tree.body):
            if cls.decorator_list or any(
                re.search(r"NamedTuple|TypedDict|Enum|Flag", ast.unparse(b))
                for b in cls.bases
            ):
                continue
            nested = {n.name: n for n in cls.body if isinstance(n, ast.ClassDef)}
            if not nested:
                continue
            last_nested = max(n.end_lineno or n.lineno for n in nested.values())
            moved = [
                item
                for item in cls.body
                if isinstance(item, ast.AnnAssign)
                and item.lineno == item.end_lineno
                and item.lineno < last_nested
                and any(
                    re.search(
                        rf"(?<![\w.]){name}\b|\b{cls.name}\.{name}\b",
                        ast.unparse(item.annotation),
                    )
                    and nested[name].lineno > item.lineno
                    for name in nested
                )
            ]
            if moved:
                break
        else:
            return text
        lines = text.splitlines()
        moved_lines = [lines[item.lineno - 1] for item in moved]
        lines[last_nested:last_nested] = moved_lines
        for item in sorted(moved, key=lambda i: i.lineno, reverse=True):
            del lines[item.lineno - 1]
        text = "\n".join(lines) + "\n"


def fix_class_bodies(text: str) -> str:
    try:
        ast.parse(text)
    except SyntaxError:
        return text
    for fix in (
        drop_redefinitions,
        add_missing_staticmethods,
        subclass_new_results,
        move_attributes_after_nested_classes,
        ignore_namedtuple_method_fields,
    ):
        text = fix(text)
    return text


def ignore_namedtuple_method_fields(text: str) -> str:
    """Silence the override error of a NamedTuple field that shadows a tuple method.

    A namedtuple field named `index` or `count` really does replace the method, as typeshed
    also writes it (`inspect.FrameInfo.index`).
    """
    lines = text.splitlines()
    for node in ast.walk(ast.parse(text)):
        if not isinstance(node, ast.ClassDef) or not any(
            (
                base.attr
                if isinstance(base, ast.Attribute)
                else getattr(base, "id", None)
            )
            == "NamedTuple"
            for base in node.bases
        ):
            continue
        for statement in node.body:
            if (
                isinstance(statement, ast.AnnAssign)
                and isinstance(statement.target, ast.Name)
                and statement.target.id in ("index", "count")
                and statement.end_lineno == statement.lineno
                and "type: ignore" not in lines[statement.lineno - 1]
            ):
                lines[statement.lineno - 1] += "  # type: ignore[assignment]"
    return "\n".join(lines) + "\n"


def function_defs(
    body: list[ast.stmt], scope: tuple[str, ...] = ()
) -> Iterable[tuple[str, ast.FunctionDef | ast.AsyncFunctionDef]]:
    """Every function and method in a module body, with its qualified name, in order."""
    for node in body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            yield ".".join((*scope, node.name)), node
        elif isinstance(node, ast.ClassDef):
            yield from function_defs(node.body, (*scope, node.name))


def overload_keys(
    tree: ast.Module,
) -> dict[tuple[str, bool, int], ast.FunctionDef | ast.AsyncFunctionDef]:
    """Functions by qualified name, whether an overload, and position among those."""
    counts: dict[tuple[str, bool], int] = {}
    keys = {}
    for qualname, node in function_defs(tree.body):
        is_overload = "overload" in decorator_names(node)
        index = counts.get((qualname, is_overload), 0)
        counts[(qualname, is_overload)] = index + 1
        keys[(qualname, is_overload, index)] = node
    return keys


def class_attributes(tree: ast.Module) -> dict[tuple[str, str], ast.AnnAssign]:
    """The annotated attributes of a module's top-level classes, by class and attribute name."""
    return {
        (cls.name, node.target.id): node
        for cls in tree.body
        if isinstance(cls, ast.ClassDef)
        for node in cls.body
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name)
    }


def apply_overlay_type_ignores(stub: str, overlay: str) -> str:
    """Copy the `# type: ignore[...]` comments on an overlay's functions and class attributes
    to the stub.

    For overloads that intentionally overlap, e.g. `str` before `Iterable[str]`, and TypedDict
    fields that mypy doesn't accept yet.
    """
    try:
        overlay_tree = ast.parse(overlay, type_comments=True)
        stub_tree = ast.parse(stub)
    except SyntaxError:
        return stub
    if not overlay_tree.type_ignores:
        return stub
    overlay_keys: dict[int, tuple[str, bool, int]] = {}
    for key, node in overload_keys(overlay_tree).items():
        for line in range(node.lineno, (node.end_lineno or node.lineno) + 1):
            overlay_keys[line] = key
    stub_keys = overload_keys(stub_tree)
    overlay_attributes = {
        node.lineno: key for key, node in class_attributes(overlay_tree).items()
    }
    stub_attributes = class_attributes(stub_tree)
    lines = stub.splitlines()
    for ignore in overlay_tree.type_ignores:
        overlay_key = overlay_keys.get(ignore.lineno)
        stub_node: ast.stmt | None = stub_keys.get(overlay_key) if overlay_key else None
        if stub_node is None and ignore.lineno in overlay_attributes:
            stub_node = stub_attributes.get(overlay_attributes[ignore.lineno])
        if stub_node is None:
            continue
        line = stub_node.lineno
        if (
            "override" in ignore.tag
            and isinstance(stub_node, ast.FunctionDef)
            and stub_node.decorator_list
            and any("overload" in ast.unparse(d) for d in stub_node.decorator_list)
        ):
            # mypy reports an overloaded method's override error on its first decorator.
            line = stub_node.decorator_list[0].lineno
        if "type: ignore" not in lines[line - 1]:
            lines[line - 1] += f"  # type: ignore{ignore.tag}"
    return "\n".join(lines) + "\n"


def runtime_class(module: ModuleType, qualname: tuple[str, ...]) -> Any:
    obj: Any = module
    for name in qualname:
        obj = getattr(obj, name, None)
    return obj


ENUM_INTERNAL_NAME = re.compile(r"_\w+_|__new__|__nb_enum__")


def fix_nested_enums(text: str, module: ModuleType) -> str:
    """Write the members of nested enum classes as values, as fix_compiled_stub does."""
    tree = ast.parse(text)
    lines = text.splitlines()
    edits: list[tuple[int, int, list[str]]] = []
    for qualname, cls in class_bodies(tree.body):
        if len(qualname) < 2 or not any(
            ENUM_BASE.search(ast.unparse(b)) for b in cls.bases
        ):
            continue
        enum_class = runtime_class(module, qualname)
        if not (isinstance(enum_class, type) and issubclass(enum_class, enum.Enum)):
            continue
        for item in cls.body:
            if not (
                isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name)
            ):
                continue
            name = item.target.id
            indent = " " * item.col_offset
            member = enum_class.__dict__.get(name)
            if ENUM_INTERNAL_NAME.fullmatch(name):
                edits.append((item.lineno, item.end_lineno or item.lineno, []))
            elif isinstance(member, enum.Enum):
                edits.append(
                    (
                        item.lineno,
                        item.end_lineno or item.lineno,
                        [f"{indent}{name} = {member.value!r}"],
                    )
                )
    for start, end, replacement in sorted(edits, reverse=True):
        lines[start - 1 : end] = replacement
    return "\n".join(lines) + "\n"


BARE_ITERABLE = re.compile(r"\bIterable\b(?!\[)")
BARE_LIST_RESULT = re.compile(r"-> list:")
# `dict` as a type, not as a parameter named `dict`.
BARE_DICT = re.compile(
    r"(?:(?<=: )|(?<=\[)|(?<=\| )|(?<=-> )|(?<=, ))dict\b(?!\[|:| =)"
)


def pdg_dict_types(line: str) -> str:
    """Type a _pdg signature's bare dicts: an argument is converted to a pdg.Dictionary (see
    _DictArg in its overlay), a result is an arbitrary python dict."""
    params, arrow, result = line.rpartition(" -> ")
    if not arrow:
        return line
    return (
        BARE_DICT.sub("Mapping[str, _DictArg]", params)
        + arrow
        + BARE_DICT.sub("dict[str, Any]", result)
    )


def parameterize_compiled_generics(text: str, module: ModuleType) -> str:
    """Give the bare containers that pybind11 and Boost.Python leave their element types.

    - pybind11 enums' `__entries` maps each name to the member and its docstring.
    - Tf enums' `allValues` is a tuple of the members.
    - pybind11 bound vectors take any iterable of their items, and slice into a list of them.
    - pdg converts a dict argument to a pdg.Dictionary, whose keys are strings.
    """
    tree = ast.parse(text)
    lines = text.splitlines()
    for qualname, cls in class_bodies(tree.body):
        runtime = runtime_class(module, qualname)
        name = ".".join(qualname)
        item_type = None
        for item in cls.body:
            if (
                isinstance(item, ast.FunctionDef)
                and item.name == "__getitem__"
                and len(item.args.args) == 2
                and ast.unparse(item.args.args[1].annotation or ast.Constant(None))
                == "int"
                and item.returns is not None
            ):
                item_type = ast.unparse(item.returns)
        for item in cls.body:
            line = lines[item.lineno - 1]
            if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                value = (
                    runtime.__dict__.get(item.target.id)
                    if isinstance(runtime, type)
                    else None
                )
                if item.target.id == "__entries" and isinstance(value, dict):
                    line = line.replace(
                        "ClassVar[dict]",
                        f"ClassVar[dict[str, tuple[{name}, str | None]]]",
                    )
                elif item.target.id == "allValues" and isinstance(value, tuple):
                    if all(isinstance(member, runtime) for member in value):
                        line = line.replace(
                            "ClassVar[tuple]", f"ClassVar[tuple[{name}, ...]]"
                        )
            elif isinstance(item, ast.FunctionDef) and item_type is not None:
                line = BARE_ITERABLE.sub(f"Iterable[{item_type}]", line)
                line = BARE_LIST_RESULT.sub(f"-> list[{item_type}]:", line)
            lines[item.lineno - 1] = line
    if module.__name__ == "_pdg":
        lines = [
            pdg_dict_types(line) if line.lstrip().startswith("def ") else line
            for line in lines
        ]
    return "\n".join(lines) + "\n"


# What a binding raises when a class has no constructor python can call: pybind11's default
# __init__, Boost.Python's no_init, Shiboken's tp_new for a class it can't create.
NO_CONSTRUCTOR_MESSAGE = re.compile(
    r": no constructor defined!$|^This class cannot be instantiated from Python$"
    r"|^cannot create '[\w.]+' instances",
    re.IGNORECASE,
)
BOOST_SIGNATURE = re.compile(r"^\s*__init__\(_object\*(.*)\)$", re.MULTILINE)
BOOST_ARG_TYPES = [
    (re.compile(r"^bool$"), "bool"),
    (re.compile(r"^(?:unsigned )?(?:int|long|long long|short)$"), "int"),
    (re.compile(r"^(?:double|float)$"), "float"),
    (re.compile(r"^std::(?:__cxx11::)?basic_string<char\b.*>$|^std::string$"), "str"),
]


def binding_of(cls: type) -> str:
    """The binding generator of a compiled class: pybind11, nanobind, Boost.Python or Shiboken."""
    metaclass = type(cls)
    name = f"{metaclass.__module__}.{metaclass.__qualname__}"
    if "pybind11" in name:
        return "pybind11"
    if name.startswith("nanobind."):
        return "nanobind"
    if name.startswith("Boost.Python"):
        return "Boost.Python"
    if "Shiboken" in name:
        return "Shiboken"
    return name


def constructor_signatures(cls: type) -> list[str] | None:
    """The `__init__` parameters of a compiled class without a signature, from what calling it
    raises: [] if python can't construct it, None if that isn't known.

    Nothing is constructed: pybind11, nanobind and Boost.Python check the arguments first, and
    Shiboken's classes are only allocated (`__new__`), which raises for those it can't create.
    """
    binding = binding_of(cls)
    try:
        if binding == "Shiboken":
            # The class's own __new__ (Shiboken's), which mypy takes for the metaclass's.
            cls.__new__(cls)  # type: ignore[call-overload]
        elif binding in ("pybind11", "nanobind", "Boost.Python"):
            cls()
        else:
            return None
    except Exception as exc:
        message = str(exc)
    else:
        return None
    if NO_CONSTRUCTOR_MESSAGE.search(message):
        return []
    # Boost.Python lists the C++ signatures the arguments did not match.
    signatures = []
    for match in BOOST_SIGNATURE.finditer(
        message.partition("did not match C++ signature:")[2]
    ):
        cpp_types = [t for t in split_template_args(match.group(1)) if t]
        types = [
            next((py for pattern, py in BOOST_ARG_TYPES if pattern.match(t)), None)
            for t in cpp_types
        ]
        if None in types:
            return None
        params = [f"arg{i}: {t}" for i, t in enumerate(types)]
        signatures.append(", ".join(["self", *params, "/"] if params else ["self"]))
    return signatures or None


def split_template_args(text: str) -> list[str]:
    """Split a C++ parameter list at its top-level commas."""
    parts, depth, current = [], 0, ""
    for char in text:
        depth += {"<": 1, ">": -1}.get(char, 0)
        if char == "," and depth == 0:
            parts.append(current.strip())
            current = ""
        else:
            current += char
    return [*parts, current.strip()]


UNTYPED_INIT_ARGS = {("self", "args", "kwargs"), ("cls", "args", "kwargs")}


def drop_callable_attributes_of_methods(text: str) -> str:
    """Leave out the `name: ClassVar[Callable] = ...` stubgen writes for a python function a
    module assigns to a compiled class (pdg's `Node.setParameter`, ...) that the overlay
    declares as a method."""
    tree = ast.parse(text)
    removed: list[tuple[int, int]] = []
    for _, cls in class_bodies(tree.body):
        methods = {n.name for n in cls.body if isinstance(n, ast.FunctionDef)}
        removed += [
            (n.lineno, n.end_lineno or n.lineno)
            for n in cls.body
            if isinstance(n, ast.AnnAssign)
            and isinstance(n.target, ast.Name)
            and n.target.id in methods
            and re.fullmatch(
                r"ClassVar\[Callable(?:\[.*\])?\]", ast.unparse(n.annotation)
            )
        ]
    lines = text.splitlines()
    for start, end in sorted(removed, reverse=True):
        del lines[start - 1 : end]
    return "\n".join(lines) + "\n"


def type_constructors(text: str, module: ModuleType) -> str:
    """Type the `__init__(self, *args, **kwargs)` stubgen leaves on classes without a signature.

    A class python can't construct gets an `__init__` that rejects every call (a required
    keyword-only parameter no caller can pass: unlike `*args: Never` it rejects a call without
    arguments, and unlike a positional `Never` parameter, which pyright reads as Unknown, any
    positional one). Boost.Python's constructors get the C++ signatures it reports, and one
    inherited from a base (a PySide class's) is left to the base. Shiboken's constructors that
    python can call have no signature at runtime: their overlay types them.
    """
    tree = ast.parse(text)
    lines = text.splitlines()
    edits: list[tuple[int, int, list[str]]] = []
    unknown = []
    for qualname, cls in class_bodies(tree.body):
        for item in cls.body:
            if not (isinstance(item, ast.FunctionDef) and item.name == "__init__"):
                continue
            a = item.args
            names = (
                *(p.arg for p in a.posonlyargs + a.args),
                *(p.arg for p in (a.vararg, a.kwarg) if p and p.annotation is None),
            )
            if names not in UNTYPED_INIT_ARGS or a.kwonlyargs:
                continue
            runtime = runtime_class(module, qualname)
            signatures = (
                constructor_signatures(runtime) if isinstance(runtime, type) else None
            )
            if (
                signatures is None
                and isinstance(runtime, type)
                and "__init__" not in vars(runtime)
            ):
                # Inherited, e.g. from a PySide class, whose stub types it.
                edits.append((first_line(item), item.end_lineno or item.lineno, []))
                continue
            if signatures is None:
                unknown.append(".".join(qualname))
                continue
            indent = " " * item.col_offset
            # A class member named Never (a pdg enum's) would shadow typing's.
            members = {name for node in cls.body for name in defined_names(node)}
            never = "typing.Never" if "Never" in members else "Never"
            if not signatures:
                replacement = [
                    f"{indent}def __init__(self, *, no_constructor: {never}) -> None: ..."
                ]
            else:
                overload = [f"{indent}@overload"] if len(signatures) > 1 else []
                replacement = [
                    line
                    for params in signatures
                    for line in [
                        *overload,
                        f"{indent}def __init__({params}) -> None: ...",
                    ]
                ]
            edits.append(
                (first_line(item), item.end_lineno or item.lineno, replacement)
            )
    for start, end, replacement in sorted(edits, reverse=True):
        lines[start - 1 : end] = replacement
    if unknown:
        print(f"Untyped constructors in {module.__name__}: {', '.join(unknown)}")
    return "\n".join(lines) + "\n"


UNTYPED_FORMAT = re.compile(
    r"^(\s+)def __format__\(self, \*args, \*\*kwargs\) -> str:", re.MULTILINE
)


def type_enum_format(text: str) -> str:
    """Give the `__format__` that compiled IntEnums inherit from int its signature."""
    return UNTYPED_FORMAT.sub(
        r"\1def __format__(self, format_spec: str, /) -> str:", text
    )


def drop_unsigned_methods(text: str, module: ModuleType) -> str:
    """Leave out the methods with no signature from the classes a module attributes elsewhere.

    _houqt's `hou.qt` classes (see CLASS_MODULE_ALIASES) have no signatures for their own
    methods, which would be untyped; the stubs give their names and Qt base classes.
    """
    alias = CLASS_MODULE_ALIASES.get(module.__name__)
    if alias is None:
        return text
    tree = ast.parse(text)
    lines = text.splitlines()
    edits: list[tuple[int, int, list[str]]] = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        runtime = getattr(module, node.name, None)
        if getattr(runtime, "__module__", None) != alias:
            continue
        unsigned = [
            item
            for item in node.body
            if isinstance(item, ast.FunctionDef)
            and item.returns is None
            and all(
                a.annotation is None
                for a in [
                    *item.args.posonlyargs,
                    *item.args.args,
                    *item.args.kwonlyargs,
                ][1:]
                + [a for a in (item.args.vararg, item.args.kwarg) if a]
            )
        ]
        if not unsigned:
            continue
        if len(unsigned) == len([n for n in node.body if not isinstance(n, ast.Expr)]):
            end = node.end_lineno or node.lineno
            edits.append((end + 1, end, ["    ..."]))
        edits += [
            (first_line(item), item.end_lineno or item.lineno, []) for item in unsigned
        ]
    for start, end, replacement in sorted(edits, reverse=True):
        lines[start - 1 : end] = replacement
    return "\n".join(lines) + "\n"


SIMPLE_TYPE_ORDER = {"bool": 0, "int": 1, "float": 2, "complex": 3}


def type_covers(broad: str, narrow: str) -> bool:
    """Whether every value of the type `narrow` is also a `broad`, by simple rules."""
    broad_members = {m.strip() for m in split_union(broad)}
    for member in (m.strip() for m in split_union(narrow)):
        if member in broad_members or "object" in broad_members:
            continue
        rank = SIMPLE_TYPE_ORDER.get(member)
        if rank is not None and any(
            SIMPLE_TYPE_ORDER.get(b, -1) > rank for b in broad_members
        ):
            continue
        return False
    return True


def signature_covers(earlier: ast.FunctionDef, later: ast.FunctionDef) -> bool:
    """Whether every call matching `later` also matches `earlier`."""
    a, b = earlier.args, later.args
    a_params = [*a.posonlyargs, *a.args]
    b_params = [*b.posonlyargs, *b.args]
    if (
        [p.arg for p in a_params] != [p.arg for p in b_params]
        or len(a.defaults) != len(b.defaults)
        or [p.arg for p in a.kwonlyargs] != [p.arg for p in b.kwonlyargs]
        or [d is None for d in a.kw_defaults] != [d is None for d in b.kw_defaults]
        or bool(a.vararg) != bool(b.vararg)
        or bool(a.kwarg) != bool(b.kwarg)
    ):
        return False
    pairs = list(zip(a_params + a.kwonlyargs, b_params + b.kwonlyargs))
    pairs += [(x, y) for x, y in ((a.vararg, b.vararg), (a.kwarg, b.kwarg)) if x and y]
    for x, y in pairs:
        if x.annotation is None:
            continue
        if y.annotation is None or not type_covers(
            ast.unparse(x.annotation), ast.unparse(y.annotation)
        ):
            return False
    return True


def prune_unreachable_overloads(text: str) -> str:
    """Drop the overloads of a compiled function that an earlier overload always matches.

    pybind11 tries the overloads in order, so `f(x: float)` before `f(x: int)` takes every
    int, and type checkers reject the overload that can never match.
    """
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return text
    removed: list[tuple[int, int]] = []
    single: list[ast.FunctionDef] = []
    for _, body in all_bodies(tree):
        groups: dict[str, list[ast.FunctionDef]] = {}
        for node in body:
            if isinstance(node, ast.FunctionDef) and "overload" in decorator_names(
                node
            ):
                groups.setdefault(node.name, []).append(node)
        for variants in groups.values():
            kept: list[ast.FunctionDef] = []
            for variant in variants:
                if any(signature_covers(earlier, variant) for earlier in kept):
                    removed.append(
                        (first_line(variant), variant.end_lineno or variant.lineno)
                    )
                else:
                    kept.append(variant)
            if len(kept) == 1 and len(variants) > 1:
                single.append(kept[0])
    if not removed:
        return text
    lines = text.splitlines()
    for node in single:
        for decorator in node.decorator_list:
            if ast.unparse(decorator) in ("overload", "typing.overload"):
                removed.append((decorator.lineno, decorator.lineno))
    for start, end in sorted(removed, reverse=True):
        del lines[start - 1 : end]
    return "\n".join(lines) + "\n"


MISSING_ALL_NAME = re.compile(r"^#   (\w+)$")


def import_all_submodules(text: str, package_dir: pathlib.Path) -> str:
    """Import the submodules a package's `__all__` names, so `package.submodule` resolves.

    stubgen lists the names in `__all__` it found no definition for in a comment.
    """
    lines = text.splitlines()
    imports = []
    for i, line in enumerate(lines):
        match = MISSING_ALL_NAME.match(line)
        if not match:
            continue
        name = match.group(1)
        if (package_dir / f"{name}.py").exists() or (package_dir / name).is_dir():
            imports.append(f"from . import {name} as {name}")
            lines[i] = ""
    if not imports:
        return text
    lines = [
        line
        for line in lines
        if not (
            line == "# Names in __all__ with no definition:"
            and not any(MISSING_ALL_NAME.match(other) for other in lines)
        )
    ]
    return insert_after_imports("\n".join(lines) + "\n", imports)


def insert_after_imports(text: str, statements: Iterable[str]) -> str:
    """Insert statements after a stub's top-level imports."""
    statements = list(statements)
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return text
    ends = [
        n.end_lineno or n.lineno
        for n in tree.body
        if isinstance(n, (ast.Import, ast.ImportFrom))
    ]
    lines = text.splitlines()
    index = (
        max(ends)
        if ends
        else next(
            (
                i
                for i, line in enumerate(lines)
                if line.strip() and not line.startswith("#")
            ),
            len(lines),
        )
    )
    lines[index:index] = statements
    return "\n".join(lines) + "\n"


def stub_module_paths() -> dict[str, pathlib.Path]:
    """The generated stub of every module, by module name."""
    paths = {}
    for package in STUBS_DIR.glob("*-stubs"):
        if package.name in HAND_WRITTEN_STUBS:
            continue
        top = package.name.removesuffix("-stubs")
        for path in package.rglob("*.pyi"):
            rel = path.relative_to(package)
            paths[module_name_of(pathlib.Path(top, *rel.parts))] = path
    return paths


def resolve_import(module: str, is_package: bool, node: ast.ImportFrom) -> str:
    if not node.level:
        return node.module or ""
    parts = module.split(".")
    if not is_package:
        parts.pop()
    if node.level > 1:
        parts = parts[: len(parts) - (node.level - 1)]
    return ".".join([*parts, *([node.module] if node.module else [])])


def top_level_imports(body: list[ast.stmt]) -> Iterable[ast.Import | ast.ImportFrom]:
    """The imports a module body makes, including those in `if` and `try` blocks."""
    for node in body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            yield node
        elif isinstance(node, ast.If):
            yield from top_level_imports(node.body)
            yield from top_level_imports(node.orelse)
        elif isinstance(node, ast.Try):
            for block in (
                node.body,
                *(h.body for h in node.handlers),
                node.orelse,
                node.finalbody,
            ):
                yield from top_level_imports(block)


def stub_bindings(tree: ast.Module) -> dict[str, bool]:
    """The names a stub defines, and whether each is exported (not a plain import)."""
    bound: dict[str, bool] = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            bound[node.name] = True
        elif isinstance(node, ast.Assign):
            bound.update((t.id, True) for t in node.targets if isinstance(t, ast.Name))
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            bound[node.target.id] = True
        elif isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.asname or alias.name.split(".")[0]
                bound.setdefault(name, alias.asname == alias.name)
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                name = alias.asname or alias.name
                bound[name] = bound.get(name, False) or alias.asname == alias.name
    return bound


def reexport_statements(
    name: str,
    module: str,
    is_package: bool,
    stub: ast.Module,
    source: ast.Module | None,
) -> list[str]:
    """Statements that make a stub export `name`, as its source binds it by an import."""
    for tree in (stub, source):
        if tree is None:
            continue
        imports = (
            top_level_imports(tree.body)
            if tree is source
            else (n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom)))
        )
        for node in imports:
            for alias in node.names:
                if (
                    isinstance(node, ast.ImportFrom)
                    and (alias.asname or alias.name) == name
                ):
                    origin = resolve_import(module, is_package, node)
                    if alias.name == name:
                        return [f"from {origin} import {name} as {name}"]
                    return [
                        f"from {origin} import {alias.name} as {alias.name}",
                        f"{name} = {alias.name}",
                    ]
                if isinstance(node, ast.Import) and alias.asname == name:
                    # A module alias: `import html.parser as htmlparser`.
                    return [f"import {alias.name}", f"{name} = {alias.name}"]
                if (
                    isinstance(node, ast.Import)
                    and alias.asname is None
                    and alias.name == name
                ):
                    return [f"import {name} as {name}"]
    return []


def add_reexports(staging: pathlib.Path) -> None:
    """Export the names that other stubs import from a module and its stub leaves out.

    stubgen drops imports a module does not use itself (`import html.parser as htmlparser`,
    or an import in a `try` block), and does not re-export the ones it keeps, but other
    modules import those names from it.  Unused imports of names a module does not have at
    all (stale `if TYPE_CHECKING:` imports) are removed.
    """
    paths = stub_module_paths()
    wanted: dict[str, dict[str, list[pathlib.Path]]] = {}
    for module, path in paths.items():
        try:
            tree = ast.parse(path.read_text())
        except SyntaxError:
            continue
        for node in tree.body:
            if not isinstance(node, ast.ImportFrom):
                continue
            origin = resolve_import(module, path.name == "__init__.pyi", node)
            if origin not in paths:
                continue
            for alias in node.names:
                if alias.name != "*" and f"{origin}.{alias.name}" not in paths:
                    wanted.setdefault(origin, {}).setdefault(alias.name, []).append(
                        path
                    )
    unresolved: dict[pathlib.Path, set[tuple[str, str]]] = {}
    for module, names in sorted(wanted.items()):
        path = paths[module]
        text = path.read_text()
        try:
            stub = ast.parse(text)
        except SyntaxError:
            continue
        is_package = path.name == "__init__.pyi"
        source = None
        for rel in (
            pathlib.Path(*module.split("."), "__init__.py"),
            pathlib.Path(*module.split(".")).with_suffix(".py"),
        ):
            if (staging / rel).exists():
                try:
                    source = ast.parse((staging / rel).read_text(errors="replace"))
                except SyntaxError:
                    pass
                break
        bound = stub_bindings(stub)
        # Names the stub imports without re-exporting them; a second, re-exporting import
        # would not do, as mypy goes by the first.
        implicit = {
            alias.name
            for node in stub.body
            if isinstance(node, ast.ImportFrom)
            for alias in node.names
            if alias.asname is None
            and alias.name in names
            and bound.get(alias.name) is False
        }
        if implicit:
            text = export_imports(text, stub, implicit)
            stub = ast.parse(text)
            bound = stub_bindings(stub)
        statements: list[str] = []
        for name, importers in sorted(names.items()):
            if bound.get(name):
                continue
            found = reexport_statements(
                name, module, is_package, stub, None if name in bound else source
            )
            statements += found
            if not found and name not in bound and source is not None:
                for importer in importers:
                    unresolved.setdefault(importer, set()).add((module, name))
        if statements:
            text = insert_after_imports(text, dict.fromkeys(statements))
        if statements or implicit:
            path.write_text(text)
    for importer, missing in unresolved.items():
        importer_module = next(m for m, p in paths.items() if p == importer)
        text = importer.read_text()
        importer.write_text(
            remove_unused_imports(
                text, importer_module, importer.name == "__init__.pyi", missing
            )
        )


def export_imports(text: str, tree: ast.Module, names: set[str]) -> str:
    """Make a stub's `from m import name` imports of the given names re-export them."""
    lines = text.splitlines()
    for node in sorted(tree.body, key=lambda n: n.lineno, reverse=True):
        if not isinstance(node, ast.ImportFrom) or not any(
            a.asname is None and a.name in names for a in node.names
        ):
            continue
        aliases = [
            ast.alias(a.name, a.name) if a.asname is None and a.name in names else a
            for a in node.names
        ]
        statement = ast.unparse(ast.ImportFrom(node.module, aliases, node.level))
        lines[node.lineno - 1 : node.end_lineno] = [statement]
    return "\n".join(lines) + "\n"


def remove_unused_imports(
    text: str, module: str, is_package: bool, names: set[tuple[str, str]]
) -> str:
    """Remove the given `from origin import name`s from a stub, where the stub does not use them."""
    tree = ast.parse(text)
    code = strip_strings_and_comments(text)
    lines = text.splitlines()
    for node in sorted(tree.body, key=lambda n: n.lineno, reverse=True):
        if not isinstance(node, ast.ImportFrom):
            continue
        origin = resolve_import(module, is_package, node)
        statement = ast.unparse(node)
        unused = [
            alias
            for alias in node.names
            if (origin, alias.name) in names
            and len(re.findall(rf"(?<![\w.]){alias.asname or alias.name}\b", code))
            == len(re.findall(rf"(?<![\w.]){alias.asname or alias.name}\b", statement))
        ]
        if not unused:
            continue
        kept = [alias for alias in node.names if alias not in unused]
        replacement = (
            [ast.unparse(ast.ImportFrom(node.module, kept, node.level))] if kept else []
        )
        lines[node.lineno - 1 : node.end_lineno] = replacement
    return "\n".join(lines) + "\n"


PYTHON_VERSION_CHECK = re.compile(r"isPy[23]\(\)|version_info|\bsix\.PY[23]\b")


def evaluate_version_check(node: ast.expr) -> Any:
    """Evaluate a check of the python or Qt version, e.g. `hutil.py23.isPy3()`.

    Raises ValueError for anything else.
    """
    text = ast.unparse(node)
    if re.fullmatch(r"(?:[\w.]+\.)?isPy3\(\)|six\.PY3", text):
        return True
    if re.fullmatch(r"(?:[\w.]+\.)?isPy2\(\)|six\.PY2", text):
        return False
    if text == "sys.version_info":
        return tuple(sys.version_info[:3])
    if text in ("sys.version_info.major", "sys.version_info[0]"):
        return sys.version_info.major
    if text in ("sys.version_info.minor", "sys.version_info[1]"):
        return sys.version_info.minor
    if re.fullmatch(r"(?:[\w.]+\.)?QtCore\.__version_info__", text):
        return tuple(importlib.import_module("PySide6.QtCore").__version_info__)
    if isinstance(node, ast.Subscript) and isinstance(node.slice, ast.Constant):
        return evaluate_version_check(node.value)[node.slice.value]
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Tuple):
        return tuple(evaluate_version_check(e) for e in node.elts)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.Not):
        return not evaluate_version_check(node.operand)
    if isinstance(node, ast.BoolOp):
        values = [evaluate_version_check(v) for v in node.values]
        return all(values) if isinstance(node.op, ast.And) else any(values)
    if isinstance(node, ast.Compare):
        compare = {
            ast.Lt: lambda a, b: a < b,
            ast.LtE: lambda a, b: a <= b,
            ast.Gt: lambda a, b: a > b,
            ast.GtE: lambda a, b: a >= b,
            ast.Eq: lambda a, b: a == b,
            ast.NotEq: lambda a, b: a != b,
        }
        left = evaluate_version_check(node.left)
        for op, comparator in zip(node.ops, node.comparators):
            right = evaluate_version_check(comparator)
            if type(op) not in compare:
                raise ValueError(text)
            if not compare[type(op)](left, right):
                return False
            left = right
        return True
    raise ValueError(text)


class VersionCheckResolver(cst.CSTTransformer):
    """Keep only the branch a module- or class-level python or Qt version check takes.

    stubgen keeps both branches of `if isPy3(): ... else: ...`, so the stub would define a
    name twice, the second time for python 2.
    """

    def __init__(self) -> None:
        super().__init__()
        self.function_depth = 0
        # The `elif` branches, by id: they are resolved with the `if` they belong to.
        self.elifs: set[int] = set()

    def visit_FunctionDef(self, node: cst.FunctionDef) -> bool:
        self.function_depth += 1
        return True

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, updated_node: cst.FunctionDef
    ) -> cst.FunctionDef:
        self.function_depth -= 1
        return updated_node

    def visit_If(self, node: cst.If) -> bool:
        if isinstance(node.orelse, cst.If):
            self.elifs.add(id(node.orelse))
        return True

    def leave_If(
        self, original_node: cst.If, updated_node: cst.If
    ) -> (
        cst.BaseStatement | cst.FlattenSentinel[cst.BaseStatement] | cst.RemovalSentinel
    ):
        if self.function_depth or id(original_node) in self.elifs:
            return updated_node
        return self.resolve(updated_node)

    def resolve(
        self, node: cst.If
    ) -> (
        cst.BaseStatement | cst.FlattenSentinel[cst.BaseStatement] | cst.RemovalSentinel
    ):
        test = cst.Module([]).code_for_node(node.test)
        if not PYTHON_VERSION_CHECK.search(test):
            return node
        try:
            taken = bool(
                evaluate_version_check(ast.parse(test.strip(), mode="eval").body)
            )
        except (
            ValueError,
            SyntaxError,
            TypeError,
            IndexError,
            ImportError,
            AttributeError,
        ):
            return node
        branch = node.body if taken else node.orelse
        if branch is None:
            return cst.RemoveFromParent()
        if isinstance(branch, cst.If):
            return self.resolve(branch)
        block = (
            branch
            if isinstance(branch, (cst.IndentedBlock, cst.SimpleStatementSuite))
            else branch.body
        )
        if isinstance(block, cst.SimpleStatementSuite):
            return cst.SimpleStatementLine(block.body)
        return cst.FlattenSentinel(block.body)


def resolve_version_checks(staging: pathlib.Path, files: Iterable[str]) -> None:
    for rel in files:
        path = staging / rel
        text = path.read_text(encoding="utf-8", errors="surrogateescape")
        if not PYTHON_VERSION_CHECK.search(text):
            continue
        try:
            resolved = cst.parse_module(text).visit(VersionCheckResolver()).code
        except Exception as exc:  # noqa: BLE001
            print(f"Could not resolve the version checks in {rel}: {exc}")
            continue
        if resolved != text:
            path.unlink()
            path.write_text(resolved, encoding="utf-8", errors="surrogateescape")


def add_qt_shim_stubs(libs: pathlib.Path) -> None:
    """Stub the members of Houdini's Qt shims, which create them at runtime.

    hutil.PySide imports PySide6 (or PySide2) submodules dynamically. SideFX ships a copy of
    PySide6's own stubs for them, which are not ours to redistribute, so re-export PySide6's
    instead. hutil.Qt is Qt.py, which builds QtCore, QtWidgets, etc. from the binding it finds.
    """
    pyside_stubs = STUBS_DIR / "hutil-stubs" / "PySide"
    for shipped in sorted((libs / "hutil" / "PySide").glob("Qt*.pyi")):
        (pyside_stubs / shipped.name).write_text(
            f"from PySide6.{shipped.stem} import *\n"
        )

    qt_py = libs / "hutil" / "Qt.py"
    qt_stub = STUBS_DIR / "hutil-stubs" / "Qt.pyi"
    if qt_py.exists() and qt_stub.exists():
        # Only those PySide6 has (Qt.py also maps Qt5-only modules, e.g. QtX11Extras).
        pyside6 = {
            shipped.stem for shipped in (libs / "hutil" / "PySide").glob("Qt*.pyi")
        }
        members = [name for name in qt_py_members(qt_py.read_text()) if name in pyside6]
        exports = "".join(f"from PySide6 import {name} as {name}\n" for name in members)
        # Qt.py also registers its members as submodules (`from hutil.Qt.QtCore import Qt`),
        # so the stub is a package.
        qt_package = qt_stub.with_suffix("")
        qt_package.mkdir(exist_ok=True)
        (qt_package / "__init__.pyi").write_text(
            qt_stub.read_text() + "\n# Created at runtime by Qt.py.\n" + exports
        )
        qt_stub.unlink()
        for name in members:
            (qt_package / f"{name}.pyi").write_text(f"from PySide6.{name} import *\n")


def qt_py_members(source: str) -> list[str]:
    """The Qt modules Qt.py exposes: the keys of its _common_members table."""
    for node in ast.parse(source).body:
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(t, ast.Name) and t.id == "_common_members"
                for t in node.targets
            )
            and isinstance(node.value, ast.Dict)
        ):
            return sorted(
                key.value
                for key in node.value.keys
                if isinstance(key, ast.Constant) and isinstance(key.value, str)
            )
    return []


def source_imports_for(codes: list[str], stub: str, source: ast.Module) -> list[str]:
    """The source's imports of names that restored definitions use and the stub lacks."""
    bindings: dict[str, str] = {}
    for node in source.body:
        if isinstance(node, ast.ImportFrom) and node.module and not node.level:
            for alias in node.names:
                if alias.name != "*":
                    as_ = f" as {alias.asname}" if alias.asname else ""
                    bindings[alias.asname or alias.name] = (
                        f"from {node.module} import {alias.name}{as_}"
                    )
        elif isinstance(node, ast.Import):
            for alias in node.names:
                bound = alias.asname or alias.name.split(".")[0]
                as_ = f" as {alias.asname}" if alias.asname else ""
                bindings[bound] = f"import {alias.name}{as_}"
    used: set[str] = set()
    for code in codes:
        try:
            used |= {n.id for n in ast.walk(ast.parse(code)) if isinstance(n, ast.Name)}
        except SyntaxError:
            continue
    stub_code = strip_docstrings(stub)
    needed = []
    for name in sorted(used):
        if name not in bindings:
            continue
        defined = re.search(
            rf"^(?:(?:class|def) {name}\b|{name}\s*[:=])|^(?:import|from) .*\b{name}\b",
            stub_code,
            re.MULTILINE,
        )
        if not defined:
            needed.append(bindings[name])
    return sorted(set(needed))


def is_stub_like(node: ast.ClassDef) -> bool:
    """Whether a class has only declarations: an overlay's helper class, not SideFX code."""
    for item in node.body:
        if isinstance(item, (ast.AnnAssign, ast.Pass)):
            continue
        if isinstance(item, ast.Expr) and isinstance(item.value, ast.Constant):
            continue
        if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)) and all(
            isinstance(b, (ast.Pass, ast.Expr))
            and (not isinstance(b, ast.Expr) or isinstance(b.value, ast.Constant))
            for b in item.body
        ):
            continue
        return False
    return True


def dropped_helper_classes(stub: str, source: ast.Module) -> list[str]:
    """Private helper classes from overlays that stubgen dropped but the stub refers to."""
    helpers = {
        node.name: node
        for node in source.body
        if isinstance(node, ast.ClassDef)
        and node.name.startswith("_")
        and is_stub_like(node)
    }
    added: list[str] = []
    text = strip_docstrings(stub)
    while True:
        missing = [
            name
            for name in helpers
            if re.search(rf"(?<![\w.]){name}\b", text)
            and not re.search(rf"^class {name}\b", text, re.MULTILINE)
        ]
        if not missing:
            return added
        for name in missing:
            code = ast.unparse(helpers[name])
            added.append(code)
            text += "\n" + code


def apply_compiled_overlay(text: str, module_name: str) -> str:
    """Merge the annotation overlay for a compiled module into its generated stub."""
    module = sys.modules[module_name]
    is_package = hasattr(module, "__path__")
    rel = module_name.replace(".", "/") + ("/__init__.py" if is_package else ".py")
    overlay = annotation_overlays.overlay_path(rel)
    if not overlay.exists():
        return text
    merged = annotation_overlays.merge(text, overlay.read_text(), stub=True)
    if merged.unmatched:
        print(
            f"Overlay entries for {module_name} that match nothing: {', '.join(merged.unmatched)}"
        )
    return merged.code


CLASS_LINE = re.compile(r"^class (\w+)(?:\((.*)\))?:")
MEMBER_LINE = re.compile(r"^    (?:def (\w+)\(|(\w+):)")
ENUM_MEMBER_LINE = re.compile(r"^    (\w+): ClassVar\[\w+\] = \.\.\.$")
ENUM_INTERNAL_LINE = re.compile(
    r"^    (?:_\w+_|__new__|__nb_enum__): ClassVar\[.*\] = \.\.\.$"
)
SIGNATURE_LINE = re.compile(r"^    (?:def \w+\(|\w+: )")


def fix_compiled_stub(text: str, module: ModuleType) -> str:
    """Fix up the stub of a compiled module, using the module itself to resolve names."""
    module_classes = {
        name for name, value in vars(module).items() if isinstance(value, type)
    }
    lines = text.splitlines()

    # Members of each top-level class, including inherited ones, so that types they shadow
    # can be qualified.
    own_members: dict[str, set[str]] = {}
    bases: dict[str, list[str]] = {}
    current = None
    for line in lines:
        if match := CLASS_LINE.match(line):
            current = own_members.setdefault(match.group(1), set())
            bases[match.group(1)] = [
                b.strip() for b in (match.group(2) or "").split(",")
            ]
        elif not line.startswith(" ") and line.strip():
            current = None
        elif current is not None and (match := MEMBER_LINE.match(line)):
            current.add(match.group(1) or match.group(2))

    def all_members(name: str) -> set[str]:
        members = set(own_members.get(name, ()))
        for base in bases.get(name, ()):
            members |= all_members(base)
        return members

    class_members = {name: all_members(name) for name in own_members}

    result = []
    class_name = None
    enum_class = None
    imports_itself = False
    for line in lines:
        if match := CLASS_LINE.match(line):
            class_name = match.group(1)
            is_enum = "enum." in (match.group(2) or "")
            enum_class = getattr(module, class_name, None) if is_enum else None
        elif not line.startswith(" ") and line.strip():
            class_name = enum_class = None

        if enum_class is not None:
            # Enum members must be unannotated for type checkers to treat them as members.
            if ENUM_INTERNAL_LINE.match(line):
                continue
            match = ENUM_MEMBER_LINE.match(line)
            # The ClassVar may name the class by an alias, as with hapi.pdgWorkitemState.
            member = getattr(enum_class, match.group(1), None) if match else None
            if match and isinstance(member, enum.Enum):
                result.append(f"    {match.group(1)} = {member.value!r}")
                continue

        if class_name and SIGNATURE_LINE.match(line):
            # A method named after a class (`AttributeOwner.attribType`) shadows it in the
            # class body, so refer to the class through the module instead.
            for shadowed in class_members.get(class_name, set()) & module_classes:
                line, count = re.subn(
                    rf"(?<=[\[(,:|>] ){shadowed}\b(?!\()|(?<=\[){shadowed}\b",
                    f"{module.__name__}.{shadowed}",
                    line,
                )
                imports_itself = imports_itself or count > 0
        result.append(line)
    if imports_itself:
        result.insert(0, f"import {module.__name__}")
    return "\n".join(result) + "\n"


DECORATOR_LINE = re.compile(r"^\s*@(_\w+)\s*$", re.MULTILINE)


def remove_undefined_private_decorators(text: str) -> str:
    """Remove decorators that refer to private helpers, which stubgen leaves out."""

    def replace(match: re.Match[str]) -> str:
        name = match.group(1)
        definition = rf"^\s*(?:(?:def|class)\s+{name}\b|{name}\s*[:=])|^(?:from|import)\b.*\b{name}\b"
        return match.group(0) if re.search(definition, text, re.MULTILINE) else ""

    return DECORATOR_LINE.sub(replace, text)


# Mistakes in the annotations of Houdini's python sources, as (wrong type, right type).
ANNOTATION_FIXES = [
    ("hou.parmTuple", "hou.ParmTuple"),
    ("hou.hdaDefinition", "hou.HDADefinition"),
    ("hou.NetworkMovableItems", "hou.NetworkMovableItem"),
    ("any", "Any"),
    # Qt 5 names, which PySide6 renames.
    ("Qt.Alignment", "Qt.AlignmentFlag"),
]
ANNOTATION_LINE = re.compile(r"^\s*(?:async def |def |\w+: )")


def fix_source_annotations(text: str) -> str:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not ANNOTATION_LINE.match(line):
            continue
        for wrong, right in ANNOTATION_FIXES:
            # Only where a type is expected: after `: `, `-> `, `[`, `, ` or `| `.
            line = re.sub(
                rf"(?:(?<=: )|(?<=> )|(?<=\[)|(?<=, )|(?<=\| )){re.escape(wrong)}\b(?![.(])",
                right,
                line,
            )
        lines[i] = line
    return "\n".join(lines) + "\n"


# Names that the generated stubs use without importing, as (usage, binding, import statement).
IMPLICIT_IMPORTS = [
    (r"(?<![\w.])Sequence\[", r"\bSequence\b", "from collections.abc import Sequence"),
    (r"(?<![\w.])Any\b", r"\bAny\b", "from typing import Any"),
    (r"(?<![\w.])types\.\w", r"\btypes\b", "import types"),
    (r"(?<![\w.])hou\.\w", r"\bhou\b", "import hou"),
    (r"(?<![\w.])_pdg\.\w", r"\b_pdg\b", "import _pdg"),
    (r"(?<![\w.])_pdgd\.\w", r"\b_pdgd\b", "import _pdgd"),
]
# Typing names that definitions restored after stubgen (aliases, TypeVars, helper classes) use.
IMPLICIT_IMPORTS += (
    [
        (rf"(?<![\w.]){name}\b", rf"\b{name}\b", f"from collections.abc import {name}")
        for name in (
            "Callable",
            "Collection",
            "Generator",
            "Hashable",
            "Iterable",
            "Iterator",
            "Mapping",
            "MutableMapping",
            "MutableSequence",
            "MutableSet",
        )
    ]
    + [
        (rf"(?<![\w.]){name}\.\w", rf"\b{name}\b", f"import {name}")
        for name in (
            "collections",
            "datetime",
            "enum",
            "io",
            "json",
            "logging",
            "os",
            "pathlib",
            "re",
            "socket",
            "subprocess",
            "threading",
            "typing",
            "uuid",
        )
    ]
    + [
        (rf"(?<![\w.]){name}\.\w", rf"\b{name}\b", f"from pxr import {name}")
        for name in (
            "Ar",
            "CameraUtil",
            "Gf",
            "Glf",
            "Kind",
            "Ndr",
            "Pcp",
            "Plug",
            "Sdf",
            "Sdr",
            "Tf",
            "Usd",
            "UsdGeom",
            "UsdLux",
            "UsdPhysics",
            "UsdRender",
            "UsdShade",
            "UsdSkel",
            "UsdUtils",
            "UsdVol",
            "Vt",
            "Work",
        )
    ]
    + [
        (rf"(?<![\w.]){name}\b", rf"\b{name}\b", f"from typing import {name}")
        for name in (
            "ClassVar",
            "Concatenate",
            "Final",
            "Literal",
            "NamedTuple",
            "Never",
            "NoReturn",
            "NotRequired",
            "ParamSpec",
            "Protocol",
            "Required",
            "Self",
            "TypeAlias",
            "TypedDict",
            "TypeVar",
            "Unpack",
            "overload",
        )
    ]
)


@functools.cache
def stub_modules() -> list[str]:
    """The top-level modules with stubs, which an annotation may refer to without importing."""
    libs = libs_dir()
    names = {p.stem for p in libs.glob("*.py")} | {
        p.name for p in libs.iterdir() if p.is_dir()
    }
    names |= {name.split(".")[0] for name in COMPILED_MODULES}
    return sorted(
        n
        for n in names
        if n.isidentifier() and n not in SKIPPED_SOURCE_MODULES | {"hou"}
    )


HOUTYPES_IMPORT = re.compile(r"(?m)^from houtypes import .*$")


EMPTY_CONTAINER_DEFAULT = re.compile(
    r"(?<=[\w\]]) = (?:\{\}|\[\]|\(\)|\[\{\}\])(?=[,)])"
)


# Object addresses pybind11 writes in default values (`<_pdg.Filter object at 0x7fc...>`),
# which change on every run.
OBJECT_ADDRESS = re.compile(r" at 0x[0-9a-f]+>")

PEP728_KEYWORDS = {"closed", "extra_items"}


def ignore_pep728_keywords(text: str) -> str:
    """Mark the TypedDicts that use PEP 728's `closed=` or `extra_items=` for mypy, which doesn't
    support them yet (pyright does), so it doesn't report them as unexpected keywords.
    """
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return text
    lines = text.splitlines()
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            keywords = node.keywords
        elif isinstance(node, (ast.Assign, ast.AnnAssign)) and isinstance(
            node.value, ast.Call
        ):
            keywords = (
                node.value.keywords
                if ast.unparse(node.value.func).endswith("TypedDict")
                else []
            )
        else:
            continue
        if (
            any(k.arg in PEP728_KEYWORDS for k in keywords)
            and "type: ignore" not in lines[node.lineno - 1]
        ):
            # mypy reports the class form as call-arg, the functional form as misc.
            code = "call-arg" if isinstance(node, ast.ClassDef) else "misc"
            lines[node.lineno - 1] += f"  # type: ignore[{code}]"
    return "\n".join(lines) + "\n"


def elide_container_defaults(text: str) -> str:
    """Write the `{}`, `[]`, `()` and `[{}]` defaults stubgen copies from the source as `...`.

    Stubs only give simple defaults (flake8-pyi Y011), and a `{}` isn't a valid default for a
    parameter typed with a TypedDict, such as a callback's kwargs (nor `[{}]` for a list of them).
    """
    return EMPTY_CONTAINER_DEFAULT.sub(" = ...", text)


REBOUND_NAME = re.compile(r"^(\w+) = \1$", re.MULTILINE)


def reexport_rebound_builtins(text: str) -> str:
    """Write a module's `next = next` (a builtin bound to its own name) as a re-export.

    stubgen copies the assignment, which a type checker reads as the name referring to itself:
    pyright takes it for a circular type alias.
    """
    import builtins

    return REBOUND_NAME.sub(
        lambda m: f"from builtins import {m[1]} as {m[1]}"
        if hasattr(builtins, m[1])
        else m[0],
        text,
    )


def unexport_houtypes(text: str) -> str:
    """Keep the stub-only `houtypes` names that overlays import from being re-exported.

    stubgen takes an import whose name it cannot resolve for an unused one, and re-exports it
    (`from houtypes import XKwargs as XKwargs`), as there is no `houtypes` module at runtime.
    """
    return HOUTYPES_IMPORT.sub(
        lambda m: re.sub(r"\b(\w+) as \1\b", r"\1", m.group(0)), text
    )


def add_missing_imports(text: str) -> str:
    """Import the names that stubgen and the fixes above use without importing."""
    code = strip_strings_and_comments(text)
    import_lines = "\n".join(
        line for line in code.splitlines() if line.startswith(("import ", "from "))
    )
    body = "\n".join(
        line for line in code.splitlines() if not line.startswith(("import ", "from "))
    )
    missing = []
    module_imports = [
        (rf"(?<![\w.]){name}\.\w", rf"\b{name}\b", f"import {name}")
        for name in stub_modules()
    ]
    for usage, binding, statement in IMPLICIT_IMPORTS + module_imports:
        name = statement.split()[-1]
        if statement.startswith("import "):
            # Any import that binds the name, but not `from name.sub import x`.
            binding = (
                rf"(?m)^import (?:.*, *)?{name}(?:\.[\w.]+)?(?:,|$)|\bas {name}\b"
                rf"|^from \S+ import (?:.*, *)?{name}(?:,|$)"
            )
        defined = re.search(
            rf"^(?:(?:class|def) {name}\b|{name}\s*[:=])", code, re.MULTILINE
        )
        if (
            re.search(usage, body)
            and not defined
            and not re.search(binding, import_lines)
        ):
            missing.append(statement)
    if not missing:
        return text
    return "\n".join(missing) + "\n" + text


DOCSTRING = re.compile(r'"""(?:.|\n)*?"""')


def strip_strings_and_comments(text: str) -> str:
    """A stub without its docstrings, comments and `__all__` entries.

    So that only real uses of a name match (stubgen comments on `__all__` entries such as
    "enum.py"); strings in annotations are kept, as they are forward references.
    """
    text = strip_docstrings(text)
    try:
        tokens = list(tokenize.generate_tokens(io.StringIO(text).readline))
    except (tokenize.TokenError, SyntaxError):
        return text
    blanked = []
    in_all = False
    line_start = True
    for token in tokens:
        if line_start and token.type == tokenize.NAME:
            in_all = token.string == "__all__"
        line_start = token.type in (
            tokenize.NEWLINE,
            tokenize.NL,
            tokenize.INDENT,
            tokenize.DEDENT,
        )
        if token.type == tokenize.COMMENT or (token.type == tokenize.STRING and in_all):
            blanked.append(token)
    lines = text.splitlines(keepends=True)
    # Last first, so that the positions of earlier tokens stay valid.
    for token in reversed(blanked):
        (start_row, start_col), (end_row, end_col) = token.start, token.end
        replacement = "" if token.type == tokenize.COMMENT else '""'
        first = lines[start_row - 1][:start_col] + replacement
        last = lines[end_row - 1][end_col:]
        lines[start_row - 1 : end_row] = [first + last]
    return "".join(lines)


def strip_docstrings(text: str) -> str:
    return DOCSTRING.sub('""""""', text)


def main() -> None:
    # Load hou before the compiled modules, some of which expect it.
    import hou  # type: ignore[import-not-found]  # noqa: F401

    libs = libs_dir()
    compiled = import_compiled_modules()

    with tempfile.TemporaryDirectory() as tmp:
        raw_dir = pathlib.Path(tmp) / "raw"
        compiled_args = [arg for name in compiled for arg in ("-m", name)]
        run_stubgen(
            ["--inspect-mode", "--include-docstrings", "-o", str(raw_dir)]
            + compiled_args
        )

        staging = pathlib.Path(tmp) / "staging"
        staging.mkdir()
        files = stage_sources(libs, staging)
        cwd = os.getcwd()
        os.chdir(staging)
        try:
            run_stubgen(
                ["--no-import", "--include-docstrings", "-o", str(raw_dir)] + files
            )
        finally:
            os.chdir(cwd)

        package_stubs(raw_dir, compiled, staging)
        add_qt_shim_stubs(libs)


if __name__ == "__main__":
    exit_code = 1
    try:
        main()
        exit_code = 0
    except BaseException:
        traceback.print_exc()
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
        # hython discards the exit code, so report it in a file for stubgen_houdini.sh to check.
        status_file = os.environ.get("STUBGEN_STATUS_FILE")
        if status_file:
            pathlib.Path(status_file).write_text(str(exit_code))
        # hython can hang on exit while Houdini shuts down; there is nothing left to clean up.
        os._exit(exit_code)
