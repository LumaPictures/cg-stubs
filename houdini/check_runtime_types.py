"""Check the `hou` stub's types against the values hython really returns.

    rez env houdini-22 -- hython check_runtime_types.py [--class REGEX] [--exceptions] </dev/null

or, to also check the UI classes (SceneViewer, NetworkEditor, GeometryViewport, Desktop, panes,
...), in the Python Shell of an interactive Houdini with a new, empty scene:

    import runpy, sys; sys.argv = ["check_runtime_types.py", "--ui"]; runpy.run_path("<this file>", run_name="__main__")

which writes its report to `.annotate/runtime_types_ui.txt` here.  If Houdini crashes, start it
again and rerun the same lines: the call that crashed is skipped from then on.

Builds a scene with nodes in every context, parameters of every template type, keyframes and
expressions, geometry with attributes and groups of every type and size, takes, bundles, network
boxes, sticky notes, dots and an HDA, then walks outward from it: for each object it calls every
method that `stubs/hou-stubs/__init__.pyi` allows to be called without arguments, checks what
it returns against the stub's return type with `typeguard.check_type`, and walks on into the
returned objects, to a bounded depth and number of instances per class.  Lookups that take one
name, index or frame (`Node.parm(name)`, `Geometry.findPointAttrib(name)`, `Node.input(index)`,
`hou.node(path)`, ...) are also called, with real names and with missing ones, since `None`
returns are where stub errors hide.  Methods with side effects (`set*`, `destroy*`, `save*`, ...)
and the UI modules are never called.

The report lists, deduplicated:

- mismatches: `Class.method: annotation  got <runtime type>  (example call -> value)`
- signature errors: calls the stub allows that raise a TypeError about their arguments
- annotations that could not be evaluated, and stub members missing at runtime
- with --exceptions, the other exceptions the calls raised (hou.OperationFailed etc. are expected)
- with --coverage, the members checked, and the getters never reached

Mismatches whose fix is outside the hou stub's sources are listed apart (KNOWN_MISMATCHES).  It
exits non-zero when there are other mismatches or signature errors.  Some HOM calls segfault on
unusual input, so the check runs in a child hython that is restarted without the call that
crashed it; those calls are listed at the end.  typeguard comes from this
directory's venv: like stubgen_houdini.sh, the script puts .venv's site-packages on the path.
"""

from __future__ import annotations

import argparse
import __future__
import ast
import collections
import dataclasses
import functools
import inspect
import itertools
import pathlib
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import types
import typing
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import Any

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(
    0,
    str(HERE / ".venv" / "lib" / f"python{sys.version_info.major}.{sys.version_info.minor}" / "site-packages"),
)

import hou  # noqa: E402
import typeguard  # noqa: E402

STUB = HERE / "stubs" / "hou-stubs" / "__init__.pyi"
MISSING_NAME = "__check_runtime_types_missing__"
NAMESPACE_MODULE = "_hou_stub_types"

# Never called: methods named <prefix> or <prefix><Capital>..., which change the scene, the
# session or files, can block, or open UI.
DENIED_PREFIXES = """
    abort accept activate add allow append apply attach bake begin bind break bypass cancel cd
    change chdir clear close collapse combine commit compile connect convert cook copy create cut
    deactivate delete deselect destroy detach dirty disable disconnect discard display dispose
    duplicate edit enable end ensure evict exec execute exit expand export extract fit flip flush
    force frame free generate grab hide home import increment init initialize insert install
    invalidate jump kill launch layout load lock loop make mark match merge move mute new open
    overwrite paste pause perform pin play pop press process publish purge push quit rebuild
    recompute reconnect record redo redraw refresh regenerate register reinitialize release reload
    remove rename render reorder repaint replace request reserve reset resize restart restore
    resume reverse revert rewind run save scroll scrub select send set setup show simulate sort
    start stash step stop store swap sync toggle trigger turn unbind undo uninstall unload unlock
    unpin unregister unset update upgrade use wait write zoom
""".split()
DENIED_RE = re.compile(rf"^(?:{'|'.join(DENIED_PREFIXES)})(?:[A-Z0-9_]|$)")
# Exceptions to DENIED_RE that only read.
ALLOWED = {"cookCount", "frameRange", "playbackRange", "endFrame", "startFrame", "selectionOwner"}
# Never called, whatever their names.
DENIED = {
    "hou.hscript", "hou.hscriptExpression", "hou.exit", "hou.hipFile.clear",
    # Segfaults hython 22.0.466 once the scene is built.
    "hou.fileReferences", "Node.fileReferences", "OpNode.fileReferences",
    "Node.hdaModule", "Node.hm", "OpNode.hdaModule", "OpNode.hm", "NodeType.hdaModule",
    "HDADefinition.hdaModule",
}
# Segfault hython 22.0.466 when called on the root node, or on the node types of the root and of
# managers (/obj, /out, ...).  The supervisor would find them, at the cost of a restart each.
MANAGER_CRASHES = {
    "OpNode.outputLabel", "OpNode.graphEditorPaneTabType", "OpNodeType.boundHandles",
    "OpNodeType.handleBindings", "OpNodeType.hidden", "OpNodeType.deprecated",
    "OpNodeType.deprecationInfo",
}
# Whole classes (mostly hou's UI modules) whose members are never called.
DENIED_CLASSES = {
    "ui", "qt", "audio", "playbar", "hotkeys", "pypanel", "galleries", "shelves",
    "Desktop", "SceneViewer", "NetworkEditor", "Pane", "PaneTab", "FloatingPanel",
    "logging", "webServer", "perfMon", "undos",
}

# With --ui, the UI classes are walked too, except for these methods, which change the UI, open
# windows or dialogs, or wait for the user, though their names don't say so.
UI_DENIED_PREFIXES = """
    clone draw enter fire flash handle inject post print read schedule split tear translate
""".split()
UI_DENIED_RE = re.compile(rf"^(?:{'|'.join(UI_DENIED_PREFIXES)})(?:[A-Z0-9_]|$)")
UI_DENIED = {
    "undos.disabler", "undos.group", "ui.statusMessage", "ui.shellIO",
    # Renders a flipbook into a new viewer ("flip" doesn't catch it: "b" isn't a capital).
    "SceneViewer.flipbook",
    # Crashed or hung Houdini 22.0.466 on the default desktop.
    "ui.desktops", "ui.packageInfo", "SceneViewer.sceneGraphHighlight", "Pane.isMaximized",
    "Pane.currentTab", "hou.compareNode", "hou.compareHip", "MenuParmTemplate.defaultValueAsString",
}
# Still never walked with --ui: it creates Qt widgets.
UI_DENIED_CLASSES = {"qt"}
UI_JOURNAL = HERE / ".annotate" / "runtime_types_ui.journal"
UI_SKIPS = HERE / ".annotate" / "runtime_types_ui.skips"
UI_REPORT = HERE / ".annotate" / "runtime_types_ui.txt"
ANY = re.compile(r"\bAny\b")

# Mismatches whose fix is not in the hou stub's sources: reported apart, and not failures.
KNOWN_MISMATCHES = {
    # `Self` is deliberate: it is right except across contexts, as for the ROP network in DOPs'
    # File Output, whose rop_dop RopNode is wired to DopNodes.
    "Node.input": "Self, deliberately; wrong only for wiring across contexts",
    "Node.inputFollowingOutputs": "as Node.input",
    "Node.inputs": "as Node.input",
    "Node.outputs": "as Node.input",
}

# Declared on an abstract base class, whose every concrete subclass has it at runtime.
ABSTRACT_MEMBERS = {"ParmTemplate.interfaceType"}

CALLED_DUNDERS = {"__len__", "__getitem__", "__iter__", "__hash__", "__repr__", "__str__"}
INDEX_PARAM = re.compile(r"index|^(?:number|num|id|n|i)$")
FRAME_PARAM = re.compile(r"^(?:frame|time)$")
PER_COLLECTION = 25


class CallTimeout(Exception):
    pass


@dataclasses.dataclass(frozen=True)
class Param:
    name: str
    annotation: str | None
    required: bool


@dataclasses.dataclass(frozen=True)
class Signature:
    params: tuple[Param, ...]
    returns: str | None

    @property
    def required(self) -> list[Param]:
        return [p for p in self.params if p.required]


@dataclasses.dataclass
class Member:
    owner: str
    name: str
    signatures: list[Signature] = dataclasses.field(default_factory=list)
    attribute: str | None = None
    static: bool = False
    is_property: bool = False

    @property
    def label(self) -> str:
        return f"{self.owner}.{self.name}" if self.owner else f"hou.{self.name}"


@dataclasses.dataclass
class StubClass:
    name: str
    bases: list[str]
    members: dict[str, Member]
    nested: set[str]
    type_params: list[str]
    raw_attributes: dict[str, ast.expr]


@dataclasses.dataclass
class Stub:
    classes: dict[str, StubClass]
    functions: dict[str, Member]
    prelude: list[ast.stmt]
    imports: list[ast.stmt]


def signature_of(func: ast.FunctionDef, drop_first: bool) -> Signature:
    a = func.args
    positional = [*a.posonlyargs, *a.args]
    first_default = len(positional) - len(a.defaults)
    params = [
        Param(p.arg, ast.unparse(p.annotation) if p.annotation else None, i < first_default)
        for i, p in enumerate(positional)
    ]
    if drop_first and params:
        params = params[1:]
    for p, default in zip(a.kwonlyargs, a.kw_defaults):
        params.append(Param(p.arg, ast.unparse(p.annotation) if p.annotation else None, default is None))
    return Signature(tuple(params), ast.unparse(func.returns) if func.returns else None)


def decorator_names(func: ast.FunctionDef) -> set[str]:
    return {ast.unparse(d).rsplit(".", 1)[-1] for d in func.decorator_list}


def parse_class(node: ast.ClassDef, qualname: str, stub: Stub) -> None:
    bases = []
    type_params = []
    for base in node.bases:
        if isinstance(base, ast.Subscript) and ast.unparse(base.value) in ("Protocol", "Generic"):
            elts = base.slice.elts if isinstance(base.slice, ast.Tuple) else [base.slice]
            type_params.extend(ast.unparse(e) for e in elts)
        else:
            bases.append(ast.unparse(base))
    cls = StubClass(qualname, bases, {}, set(), type_params, {})
    stub.classes[qualname] = cls
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            decorators = decorator_names(item)
            static = "staticmethod" in decorators
            member = cls.members.setdefault(item.name, Member(qualname, item.name, static=static))
            member.is_property = member.is_property or "property" in decorators
            member.signatures.append(signature_of(item, drop_first=not static))
        elif isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
            cls.raw_attributes[item.target.id] = item.annotation
        elif isinstance(item, ast.ClassDef):
            cls.nested.add(item.name)
            parse_class(item, f"{qualname}.{item.name}", stub)


def parse_stub(path: pathlib.Path) -> Stub:
    tree = ast.parse(path.read_text())
    stub = Stub({}, {}, [], [])
    module_attributes: dict[str, ast.expr] = {}
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            parse_class(node, node.name, stub)
        elif isinstance(node, ast.FunctionDef):
            member = stub.functions.setdefault(node.name, Member("", node.name))
            member.signatures.append(signature_of(node, drop_first=False))
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            stub.imports.append(node)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if ast.unparse(node.annotation) == "TypeAlias":
                stub.prelude.append(node)
            else:
                module_attributes[node.target.id] = node.annotation
        elif isinstance(node, ast.Assign):
            stub.prelude.append(node)
    for cls in stub.classes.values():
        for name, annotation in cls.raw_attributes.items():
            if name not in cls.members:
                cls.members[name] = attribute_member(stub, cls.name, name, annotation)
    for name, annotation in module_attributes.items():
        stub.functions.setdefault(name, attribute_member(stub, "", name, annotation))
    return stub


def attribute_member(stub: Stub, owner: str, name: str, annotation: ast.expr) -> Member:
    """An attribute; one typed as a callable (`Callable[[...], R]` or a Protocol with __call__)
    is treated as a method."""
    member = Member(owner, name)
    sig = callable_signature(stub, annotation)
    if sig is None:
        member.attribute = ast.unparse(annotation)
    elif sig is not ...:
        member.signatures.append(sig)
    return member


def callable_signature(stub: Stub, annotation: ast.expr) -> Signature | None | types.EllipsisType:
    """The signature of a callable annotation: None if it is not callable, ... if its parameters
    are unknown (`Callable[..., R]`)."""
    if isinstance(annotation, ast.Subscript) and ast.unparse(annotation.value) == "Callable":
        args, ret = annotation.slice.elts  # type: ignore[attr-defined]
        if not isinstance(args, ast.List):
            return ...
        params = tuple(Param(f"arg{i}", ast.unparse(a), True) for i, a in enumerate(args.elts))
        return Signature(params, ast.unparse(ret))
    base, args = annotation, []
    if isinstance(annotation, ast.Subscript):
        base = annotation.value
        args = annotation.slice.elts if isinstance(annotation.slice, ast.Tuple) else [annotation.slice]
    cls = stub.classes.get(ast.unparse(base))
    if cls is None or "__call__" not in cls.members or not cls.members["__call__"].signatures:
        return None
    sig = cls.members["__call__"].signatures[0]
    substitutions = dict(zip(cls.type_params, (ast.unparse(a) for a in args)))
    if not substitutions or sig.returns is None:
        return sig
    returns = re.sub(r"\b\w+\b", lambda m: substitutions.get(m.group(), m.group()), sig.returns)
    return Signature(sig.params, returns)


class Unquote(ast.NodeTransformer):
    """Replace string forward references with the expressions they name (except in Literal),
    so that annotations evaluate to real types that typeguard can check without a frame."""

    def __init__(self, keep: Iterable[str] = ()) -> None:
        self.keep = set(keep)

    def visit_Subscript(self, node: ast.Subscript) -> ast.AST:
        if ast.unparse(node.value).rsplit(".", 1)[-1] == "Literal":
            return node
        return self.generic_visit(node)

    def visit_Constant(self, node: ast.Constant) -> ast.AST:
        if isinstance(node.value, str) and node.value not in self.keep:
            try:
                return self.visit(ast.parse(node.value, mode="eval").body)
            except SyntaxError:
                pass
        return node

    def annotations(self, node: ast.stmt) -> ast.stmt:
        """Unquote only the annotations in a statement (and the field types of a functional
        TypedDict), not its other strings."""
        for child in ast.walk(node):
            if isinstance(child, ast.arg) and child.annotation:
                child.annotation = self.visit(child.annotation)
            elif isinstance(child, ast.FunctionDef) and child.returns:
                child.returns = self.visit(child.returns)
            elif isinstance(child, ast.AnnAssign):
                child.annotation = self.visit(child.annotation)
                if child.value is not None and ast.unparse(child.annotation) == "TypeAlias":
                    child.value = self.visit(child.value)
            elif isinstance(child, ast.Call) and ast.unparse(child.func) == "TypedDict":
                for arg in child.args[1:]:
                    if isinstance(arg, ast.Dict):
                        arg.values = [self.visit(v) for v in arg.values]
        return node


_EnumT = typing.TypeVar("_EnumT")


class StubEnumValue(typing.Generic[_EnumT]):
    """The stub's `EnumValue` in the annotations the walker evaluates: `EnumValue[enum]` is a
    hou.EnumValue of that enum, a bare `EnumValue` one of any enum (see check_enum_value)."""


def enum_of(value: Any) -> str:
    """The name of the enum an EnumValue belongs to, which its repr gives: `parmData.Float`."""
    return repr(value).partition(".")[0]


def check_enum_value(value: object, origin_type: Any, args: tuple[Any, ...], memo: typeguard.TypeCheckMemo) -> None:
    if not isinstance(value, hou.EnumValue):
        raise typeguard.TypeCheckError("is not a hou.EnumValue")
    if not args or isinstance(args[0], typing.TypeVar) or args[0] is Any:
        return
    enum = args[0]
    member = repr(value).partition(".")[2]
    if enum_of(value) != enum.__name__ or getattr(enum, member, None) != value:
        raise typeguard.TypeCheckError(f"is {short_repr(value)}, not a hou.{enum.__name__} value")


def lookup_enum_value(origin_type: Any, args: tuple[Any, ...], extras: tuple[Any, ...]) -> typeguard.TypeCheckerCallable | None:
    return check_enum_value if origin_type is StubEnumValue else None


typeguard.checker_lookup_functions.insert(0, lookup_enum_value)


RECURSIVE_ALIAS_DEPTH = 4
TYPED_DICT_NAMES = {"TypedDict", "NotRequired", "Required", "ReadOnly"}


def load_houtypes() -> None:
    """Make `houtypes`, which only exists as a stub, importable; its annotations (hou.EnumValue[...])
    stay unevaluated."""
    if "houtypes" in sys.modules:
        return
    houtypes = types.ModuleType("houtypes")
    source = "from __future__ import annotations\n" + (HERE / "stubs" / "houtypes-stubs" / "__init__.pyi").read_text()
    exec(compile(source, "houtypes", "exec"), houtypes.__dict__)
    sys.modules["houtypes"] = houtypes


def stub_path(module: str) -> pathlib.Path | None:
    """The generated stub of a module, if there is one."""
    top, *rest = module.split(".")
    base = HERE / "stubs" / f"{top}-stubs"
    for candidate in (base.joinpath(*rest, "__init__.pyi"), base.joinpath(*rest).with_suffix(".pyi") if rest else base / "__init__.pyi"):
        if candidate.is_file():
            return candidate
    return None


# Stub statements that couldn't run yet (a name defined later, or in a stub module that is still
# loading): (module, path, module name, statement).
PARKED_STUB_STATEMENTS: list[tuple[types.ModuleType, pathlib.Path, str, ast.stmt]] = []


def stub_module(name: str, path: pathlib.Path, module_name: str) -> types.ModuleType:
    """A stub exec'd as a module of its own (registered, so typeguard resolves its annotations).
    Call finish_stub_modules() once the top-level one has loaded."""
    load_houtypes()
    if name in sys.modules:
        return sys.modules[name]
    lines = [line for line in path.read_text().splitlines() if not line.startswith("from _typeshed import")]
    module = types.ModuleType(name)
    sys.modules[name] = module
    exec("from typing import Any as Incomplete", module.__dict__)
    pending = ast.parse("\n".join(lines)).body
    while pending:
        failed = [node for node in pending if not run_stub_statement(module, path, module_name, node)]
        if len(failed) == len(pending):
            PARKED_STUB_STATEMENTS.extend((module, path, module_name, node) for node in failed)
            break
        pending = failed
    return module


def run_stub_statement(module: types.ModuleType, path: pathlib.Path, module_name: str, node: ast.stmt) -> bool:
    """Run one statement of a stub in its module; False if it needs a name that isn't there yet."""
    flags = __future__.annotations.compiler_flag  # each statement is compiled on its own
    try:
        if isinstance(node, ast.ImportFrom) and node.module == "typing":
            # Runtime typing's TypedDict doesn't take PEP 728's closed=/extra_items=.
            moved = [a for a in node.names if a.name in TYPED_DICT_NAMES]
            if moved:
                node.names = [a for a in node.names if a.name not in TYPED_DICT_NAMES] or [ast.alias("Any")]
                extensions = ast.fix_missing_locations(ast.Module([ast.ImportFrom("typing_extensions", moved, 0)], []))
                exec(compile(extensions, str(path), "exec"), module.__dict__)
        if isinstance(node, ast.ImportFrom) and node.level:
            # A relative import, of a sibling module's stub or of names from one.
            package = module_name if path.name == "__init__.pyi" else module_name.rpartition(".")[0]
            parts = package.split(".")[: len(package.split(".")) - (node.level - 1)]
            base = ".".join(parts + ([node.module] if node.module else []))
            for alias in node.names:
                if (sub := stub_path(f"{base}.{alias.name}")) is not None:
                    value: Any = stub_module(f"{base}.{alias.name}_stub", sub, f"{base}.{alias.name}")
                else:
                    value = getattr(stub_module(f"{base}_stub", stub_path(base) or path, base), alias.name)
                module.__dict__[alias.asname or alias.name] = value
            return True
        node = Unquote().annotations(node)
        ast.fix_missing_locations(node)
        try:
            exec(compile(ast.Module([node], []), str(path), "exec", flags=flags, dont_inherit=True), module.__dict__)
        except ImportError:
            # A stub-only name (an overlay's private TypedDict, say): take it from that module's stub.
            if not (isinstance(node, ast.ImportFrom) and node.module and (other := stub_path(node.module))):
                raise
            stub = stub_module(f"{node.module}_stub", other, node.module)
            for alias in node.names:
                module.__dict__[alias.asname or alias.name] = getattr(stub, alias.name)
        return True
    except (NameError, AttributeError):
        # AttributeError: a name from a stub module that is still loading (an import cycle).
        return False


def finish_stub_modules() -> None:
    """Run the parked stub statements, across modules, until nothing more resolves."""
    while PARKED_STUB_STATEMENTS:
        parked = list(PARKED_STUB_STATEMENTS)
        PARKED_STUB_STATEMENTS.clear()
        failed = [item for item in parked if not run_stub_statement(*item)]
        if len(failed) < len(parked):
            PARKED_STUB_STATEMENTS.extend(failed)
            continue
        # Mutually recursive aliases (ParmUnionData -> ParmDataDict -> ParmUnionData): typeguard
        # doesn't check through lazy `type` aliases, so unroll them a few levels deep instead,
        # starting from Any; only data nested deeper than that goes unchecked.
        names = [defined_name(item[3]) for item in failed]
        if None in names:
            raise NameError("can't resolve: " + ", ".join(ast.unparse(item[3])[:60] for item in failed))
        for (module, *_), name in zip(failed, names):
            module.__dict__[name] = Any
        for _ in range(RECURSIVE_ALIAS_DEPTH):
            for item in failed:
                run_stub_statement(*item)
        break

def build_namespace(stub: Stub) -> tuple[dict[str, Any], list[str]]:
    """The names the stub's annotations use: the stub's imports, hou's classes, and the stub's own
    private aliases, TypedDicts and Protocols (exec'd in a module so typeguard can resolve them).
    Returns the namespace and the definitions that could not be evaluated."""
    module = types.ModuleType(NAMESPACE_MODULE)
    sys.modules[NAMESPACE_MODULE] = module
    ns = module.__dict__
    failures = []
    for node in stub.imports:
        if isinstance(node, ast.ImportFrom) and node.module == "_typeshed":
            ns.update({alias.asname or alias.name: Any for alias in node.names})
            continue
        if isinstance(node, ast.ImportFrom) and node.module == "hrecipes" and [a.name for a in node.names] == ["rtypes"]:
            # Check against the stub's rtypes, whose overlay corrects SideFX's TypedDicts, not the
            # runtime module's.
            ns["rtypes"] = stub_module("hrecipes.rtypes_stub", HERE / "stubs" / "hrecipes-stubs" / "rtypes.pyi", "hrecipes.rtypes")
            finish_stub_modules()
            continue
        if isinstance(node, ast.ImportFrom) and node.module == "houtypes":
            load_houtypes()
        try:
            exec(compile(ast.Module([node], []), "<stub>", "exec"), ns)
        except Exception as e:
            failures.append(f"{ast.unparse(node)}: {e!r}")
    for name in dir(hou):
        if name in stub.classes or name not in ns:
            ns[name] = getattr(hou, name)
    ns["EnumValue"] = StubEnumValue
    pending: list[ast.stmt] = [*stub.prelude]
    tree = ast.parse(STUB.read_text())
    pending += [
        n for n in tree.body if isinstance(n, ast.ClassDef) and not hasattr(hou, n.name)
    ]
    while pending:
        progress = []
        for node in pending:
            target = defined_name(node)
            if target in ("fs", "shfs", "webServer"):
                progress.append(node)
                continue
            node = Unquote(keep={target} if target else ()).annotations(node)
            ast.fix_missing_locations(node)
            try:
                exec(compile(ast.Module([node], []), "<stub>", "exec"), ns)
            except NameError:
                continue
            except Exception as e:
                failures.append(f"{target}: {e!r}")
            progress.append(node)
        if not progress:
            failures += [f"{defined_name(n)}: unresolved names" for n in pending]
            break
        pending = [n for n in pending if all(n is not p for p in progress) and defined_name(n) not in ns]
    for name in nominal_stub_classes(stub, ns):
        ns[name] = Any
    # typeguard resolves string forward references (in recursive aliases) in its caller's globals.
    exec("import typeguard\ndef __check_type(value, expected, **kwargs):\n    return typeguard.check_type(value, expected, **kwargs)\n", ns)
    return ns, failures


def nominal_stub_classes(stub: Stub, ns: Mapping[str, Any]) -> list[str]:
    """Classes only the stub defines (not hou), other than Protocols and TypedDicts.  No runtime
    value is an instance of one, so the walker checks their members instead."""
    result = []
    for name in stub.classes:
        value = ns.get(name)
        if "." in name or hasattr(hou, name) or not isinstance(value, type):
            continue
        if getattr(value, "_is_protocol", False) or typing.is_typeddict(value):
            continue
        result.append(name)
    return result


def defined_name(node: ast.stmt) -> str | None:
    if isinstance(node, ast.ClassDef):
        return node.name
    if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
        return node.target.id
    if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
        return node.targets[0].id
    return None


@dataclasses.dataclass
class Report:
    mismatches: dict[tuple[str, str], dict[str, tuple[int, str]]] = dataclasses.field(
        default_factory=lambda: collections.defaultdict(dict)
    )
    signature_errors: dict[str, tuple[int, str]] = dataclasses.field(default_factory=dict)
    unevaluable: dict[str, str] = dataclasses.field(default_factory=dict)
    missing: set[str] = dataclasses.field(default_factory=set)
    exceptions: dict[tuple[str, str], tuple[int, str]] = dataclasses.field(default_factory=dict)
    timeouts: dict[str, str] = dataclasses.field(default_factory=dict)
    setup_failures: list[str] = dataclasses.field(default_factory=list)
    checked: collections.Counter[str] = dataclasses.field(default_factory=collections.Counter)
    # What values typed with `Any` really held, to tighten those types from.
    any_shapes: dict[tuple[str, str], dict[str, tuple[int, str]]] = dataclasses.field(
        default_factory=lambda: collections.defaultdict(dict)
    )

    def add_mismatch(self, member: str, annotation: str, got: str, example: str) -> None:
        count, first = self.mismatches[(member, annotation)].get(got, (0, example))
        self.mismatches[(member, annotation)][got] = (count + 1, first)


def short_repr(value: object, limit: int = 160) -> str:
    try:
        text = repr(value)
    except Exception as e:
        text = f"<repr failed: {e!r}>"
    text = text.replace("\n", " ")
    return text if len(text) <= limit else text[: limit - 3] + "..."


def type_name(value: object) -> str:
    if isinstance(value, hou.EnumValue):
        return f"hou.EnumValue[{enum_of(value)}]"
    t = type(value)
    if t.__module__ in ("builtins", NAMESPACE_MODULE):
        return t.__qualname__
    if t.__module__ == "hou":
        return f"hou.{t.__qualname__}"
    return f"{t.__module__}.{t.__qualname__}"


def describe(value: object, depth: int = 0) -> str:
    """The structural type of a value, e.g. `tuple[hou.Point, ...]`."""
    if value is None:
        return "None"
    if depth < 3 and isinstance(value, (tuple, list, set, frozenset)):
        name = type(value).__name__
        if not value:
            return "tuple[()]" if isinstance(value, tuple) else f"{name}[<empty>]"
        inner = " | ".join(sorted({describe(v, depth + 1) for v in list(value)[:PER_COLLECTION]}))
        return f"{name}[{inner}, ...]" if isinstance(value, tuple) else f"{name}[{inner}]"
    if depth < 3 and isinstance(value, dict):
        if not value:
            return "dict[<empty>]"
        items = list(value.items())[:PER_COLLECTION]
        keys = " | ".join(sorted({describe(k, depth + 1) for k, _ in items}))
        values = " | ".join(sorted({describe(v, depth + 1) for _, v in items}))
        return f"dict[{keys}, {values}]"
    return type_name(value)


def sample(items: Iterable[object]) -> list[object]:
    """Up to PER_COLLECTION items, at most 3 of each type, so that a geometry's 2000 polygons
    don't hide its one volume."""
    result: list[object] = []
    per_type: collections.Counter[type] = collections.Counter()
    for item in itertools.islice(items, 5000):
        if per_type[type(item)] < 3:
            per_type[type(item)] += 1
            result.append(item)
            if len(result) >= PER_COLLECTION:
                break
    return result


def hou_objects(value: object, depth: int = 0) -> Iterator[object]:
    """The hou objects in a value, looking into containers."""
    if type(value).__module__ == "hou":
        yield value
    elif depth < 3 and isinstance(value, (tuple, list, set, frozenset)):
        for item in sample(value):
            yield from hou_objects(item, depth + 1)
    elif depth < 3 and isinstance(value, dict):
        for k, v in list(value.items())[:PER_COLLECTION]:
            yield from hou_objects(k, depth + 1)
            yield from hou_objects(v, depth + 1)


UI_MODE = False
# The type of an enum's members (`Float: EnumValue[parmTemplateType]`), which aren't walked.
ENUM_MEMBER = re.compile(r"EnumValue(?:\[.*\])?")


def is_denied(member: Member) -> bool:
    if UI_MODE and (UI_DENIED_RE.match(member.name) or member.label in UI_DENIED):
        return True
    if member.label in DENIED or member.owner.split(".")[0] in DENIED_CLASSES:
        return True
    if member.name in ALLOWED:
        return False
    return bool(DENIED_RE.match(member.name))


def is_manager(obj: object) -> bool:
    try:
        node_type = obj if isinstance(obj, hou.NodeType) else obj.type()  # type: ignore[attr-defined]
        return node_type.category().name() in ("Manager", "Director")
    except Exception:
        return False


def on_timeout(signum: int, frame: types.FrameType | None) -> None:
    # With --ui, a HOM call that processes UI events runs Houdini's own python (data sources,
    # callbacks) inside it, and the signal can land there: raising would break that code, not the
    # call.  Try again once this script's code is running, which is when the call returns.  (So in
    # an interactive Houdini, calls written in python don't time out.)
    if UI_MODE and frame is not None and frame.f_code.co_filename != __file__:
        signal.setitimer(signal.ITIMER_REAL, 0.1)
        return
    raise CallTimeout()


class Walker:
    def __init__(self, stub: Stub, ns: dict[str, Any], args: argparse.Namespace, report: Report) -> None:
        self.stub = stub
        self.ns = ns
        self.args = args
        self.report = report
        self.seen: set[object] = set()
        self.per_class: collections.Counter[str] = collections.Counter()
        self.queue: collections.deque[tuple[object, str, int]] = collections.deque()
        self.journal = open(args.journal, "w") if args.journal else None
        self.nominal = set(nominal_stub_classes(stub, ns))
        self.eval_cache: dict[tuple[str, str, str | None], Any] = {}
        # The stub class of the object being visited, which a `Self` return means.
        self.receiver_class: str | None = None

    def stub_class(self, obj: object) -> str | None:
        for t in type(obj).__mro__:
            if t.__module__ == "hou" and t.__qualname__ in self.stub.classes:
                return t.__qualname__
        return None

    @functools.cache
    def mro(self, cls_name: str) -> list[str]:
        """The C3 linearization of a stub class, over the bases the stub defines."""
        bases = [b for b in self.stub.classes[cls_name].bases if b in self.stub.classes]
        sequences = [self.mro(b) for b in bases] + [bases]
        result = [cls_name]
        while any(sequences):
            for seq in sequences:
                head = seq[0] if seq else None
                if head and not any(head in other[1:] for other in sequences):
                    break
            else:
                raise TypeError(f"inconsistent stub hierarchy for {cls_name}")
            result.append(head)
            sequences = [[c for c in seq if c != head] for seq in sequences]
        return result

    @functools.cache
    def members(self, cls_name: str) -> dict[str, Member]:
        """The members of a stub class, including inherited ones, by the stub's MRO."""
        result: dict[str, Member] = {}
        for name in self.mro(cls_name):
            for member_name, member in self.stub.classes[name].members.items():
                result.setdefault(member_name, member)
        return result

    def evaluate(self, annotation: str, owner: str) -> Any:
        key = (annotation, owner, self.receiver_class)
        if key in self.eval_cache:
            return self.eval_cache[key]
        node = Unquote().visit(ast.parse(annotation, mode="eval"))
        ast.fix_missing_locations(node)
        local: dict[str, Any] = {}
        if owner:
            runtime: Any = hou
            for part in owner.split("."):
                runtime = getattr(runtime, part, None)
            local["Self"] = runtime
            if self.receiver_class:
                local["Self"] = getattr(hou, self.receiver_class, runtime)
            for nested in self.stub.classes[owner].nested:
                local[nested] = getattr(runtime, nested, None)
        try:
            value = eval(compile(node, "<annotation>", "eval"), self.ns, local)
        except Exception as e:
            value = e
        self.eval_cache[key] = value
        return value

    def expected(self, member: Member, annotations: Sequence[str]) -> Any:
        """The union of the annotations, or None (after recording why) if one can't be evaluated."""
        types_ = []
        for annotation in annotations:
            value = self.evaluate(annotation, member.owner)
            if isinstance(value, Exception):
                self.report.unevaluable[f"{member.label}: {annotation}"] = repr(value)
                return None
            types_.append(value)
        if len(types_) == 1:
            return types_[0]
        return typing.Union[tuple(types_)]  # noqa: UP007

    def check(self, member: Member, value: object, annotations: Sequence[str], example: str) -> None:
        if self.args.cls and not re.search(self.args.cls, member.owner or "hou"):
            return
        expected = self.expected(member, annotations)
        if expected is None:
            return
        self.report.checked[member.label] += 1
        try:
            self.ns["__check_type"](
                value,
                expected,
                collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS,
                forward_ref_policy=typeguard.ForwardRefPolicy.ERROR,
            )
        except typeguard.TypeCheckError as e:
            self.report.add_mismatch(
                member.label,
                " | ".join(dict.fromkeys(annotations)),
                describe(value),
                f"{example} -> {short_repr(value)}  [{short_repr(str(e), 200)}]",
            )
        except Exception as e:
            self.report.unevaluable[f"{member.label}: {' | '.join(annotations)}"] = f"typeguard: {e!r}"
        else:
            annotation = " | ".join(dict.fromkeys(annotations))
            if ANY.search(annotation):
                shapes = self.report.any_shapes[(member.label, annotation)]
                got = describe(value)
                count, first = shapes.get(got, (0, f"{example} -> {short_repr(value)}"))
                shapes[got] = (count + 1, first)
            if len(annotations) == 1 and annotations[0] in self.nominal:
                self.enqueue(value, 0, seed=True, cls=annotations[0])

    def call(self, member: Member, func: Callable[..., object], args: Sequence[object], example: str) -> tuple[bool, object]:
        key = f"{member.label}({'...' if args else ''})"
        if key in self.args.skip:
            return False, None
        if self.journal is not None:
            self.journal.write(f"{key}\t{example}\n")
            self.journal.flush()
        signal.setitimer(signal.ITIMER_REAL, self.args.timeout)
        try:
            return True, func(*args)
        except CallTimeout:
            self.report.timeouts[member.label] = example
        except TypeError as e:
            message = str(e)
            if re.search(r"argument|positional|Wrong number", message):
                count, first = self.report.signature_errors.get(member.label, (0, f"{example}: {message}"))
                self.report.signature_errors[member.label] = (count + 1, first)
            else:
                self.record_exception(member, e, example)
        except Exception as e:
            self.record_exception(member, e, example)
        finally:
            signal.setitimer(signal.ITIMER_REAL, 0)
        return False, None

    def record_exception(self, member: Member, e: Exception, example: str) -> None:
        key = (member.label, type(e).__name__)
        count, first = self.report.exceptions.get(key, (0, f"{example}: {short_repr(e)}"))
        self.report.exceptions[key] = (count + 1, first)
        if count == 0 and isinstance(e, hou.Error):
            self.enqueue(e, 1)

    def enqueue(self, value: object, depth: int, seed: bool = False, cls: str | None = None) -> None:
        for obj in [value] if cls else hou_objects(value):
            obj_cls = cls or self.stub_class(obj)
            if obj_cls is None:
                continue
            try:
                key: object = (type(obj), obj)
                hash(key)
            except Exception:
                key = (type(obj), id(obj))
            if key in self.seen:
                continue
            if not seed and (depth > self.args.depth or self.per_class[obj_cls] >= self.args.per_class):
                continue
            self.seen.add(key)
            self.per_class[obj_cls] += 1
            self.queue.append((obj, obj_cls, depth))

    def run(self, seeds: Iterable[object]) -> None:
        for seed in seeds:
            self.enqueue(seed, 0, seed=True)
        while self.queue:
            obj, cls, depth = self.queue.popleft()
            self.visit(obj, cls, depth)

    def visit(self, obj: object, cls: str, depth: int) -> None:
        try:
            repr(obj)
        except hou.ObjectWasDeleted:
            return
        except Exception:
            pass
        receiver = short_repr(obj, 80)
        self.receiver_class = cls
        manager = is_manager(obj)
        for member in self.members(cls).values():
            if manager and member.label in MANAGER_CRASHES:
                continue
            if member.name.startswith("__") and member.name not in CALLED_DUNDERS:
                continue
            if member.attribute is not None:
                if member.name == "thisown" or ENUM_MEMBER.fullmatch(member.attribute) and member.name[0].isupper():
                    continue
                try:
                    value = getattr(obj, member.name)
                except Exception as e:
                    self.record_exception(member, e, f"{receiver}.{member.name}")
                    continue
                self.check(member, value, [member.attribute], f"{receiver}.{member.name}")
                self.enqueue(value, depth + 1)
                continue
            if is_denied(member) or not member.signatures:
                continue
            func = getattr(obj, member.name, None)
            if func is None:
                continue
            if member.is_property:
                self.check(member, func, [s.returns or "Any" for s in member.signatures], f"{receiver}.{member.name}")
                continue
            self.exercise(member, func, obj, receiver, depth)

    def exercise(self, member: Member, func: Callable[..., object], receiver_obj: object, receiver: str, depth: int) -> None:
        """Call a method without arguments if the stub allows it, and with each candidate argument
        if it takes one."""
        getter = [s.returns for s in member.signatures if not s.required and s.returns]
        if getter:
            ok, value = self.call(member, func, (), f"{receiver}.{member.name}()")
            if ok:
                self.check(member, value, getter, f"{receiver}.{member.name}()")
                self.enqueue(value, depth + 1)
        one_arg = [s for s in member.signatures if len(s.required) == 1 and s.params[0].required and s.returns]
        if not one_arg:
            return
        if member.name == "__getitem__" and not self.sized(receiver_obj):
            return
        returns = [s.returns for s in one_arg if s.returns]
        for arg in arg_candidates(receiver_obj, member, one_arg[0].params[0]):
            example = f"{receiver}.{member.name}({short_repr(arg, 60)})"
            ok, value = self.call(member, func, (arg,), example)
            if ok:
                self.check(member, value, returns, example)
                self.enqueue(value, depth + 1)

    @staticmethod
    def sized(obj: object) -> bool:
        try:
            return len(obj) > 0  # type: ignore[arg-type]
        except Exception:
            return False

    def check_declared(self) -> None:
        """Record the stub members that hou's classes and module do not have."""
        for name, cls in [("", None), *self.stub.classes.items()]:
            if name.split(".")[0] in ("qt", "ui") or name.startswith("_") and not hasattr(hou, name):
                continue
            runtime: Any = hou
            for part in name.split(".") if name else ():
                runtime = getattr(runtime, part, None)
            if runtime is None:
                continue
            members = cls.members.values() if cls else self.stub.functions.values()
            for member in members:
                if member.name == "thisown" or member.label in ABSTRACT_MEMBERS:
                    continue
                # Declared so that type checkers see what the __getitem__ protocol provides.
                if member.name in ("__iter__", "__contains__", "__reversed__") and hasattr(runtime, "__getitem__"):
                    continue
                if not hasattr(runtime, member.name):
                    self.report.missing.add(member.label)

    def run_module(self) -> None:
        """Call hou's module-level functions and the functions of its namespace classes (hou.hda,
        hou.hipFile, ...), and check its module-level attributes."""
        self.receiver_class = None
        for member in self.stub.functions.values():
            if member.attribute is not None:
                if hasattr(hou, member.name):
                    self.check(member, getattr(hou, member.name), [member.attribute], f"hou.{member.name}")
                continue
            func = getattr(hou, member.name, None)
            if func is None:
                continue
            if not is_denied(member):
                self.exercise(member, func, hou, "hou", 1)
        for name, cls in self.stub.classes.items():
            if not name[0].islower() or name.split(".")[0] in DENIED_CLASSES or name.startswith("_"):
                continue
            runtime: Any = hou
            for part in name.split("."):
                runtime = getattr(runtime, part, None)
            if runtime is None:
                continue
            for member in cls.members.values():
                if member.attribute is not None:
                    static = inspect.getattr_static(runtime, member.name, None)
                    if static is None or isinstance(static, property) or member.name == "thisown":
                        continue
                    self.check(member, getattr(runtime, member.name), [member.attribute], f"hou.{name}.{member.name}")
                elif member.static and not is_denied(member):
                    func = getattr(runtime, member.name, None)
                    if func is None:
                        continue
                    self.exercise(member, func, runtime, f"hou.{name}", 1)


def first_names(values: Iterable[object], limit: int = 40) -> list[str]:
    result = []
    for v in values:
        try:
            result.append(v.name())  # type: ignore[attr-defined]
        except Exception:
            continue
        if len(result) >= limit:
            break
    return result


def geometry_of(obj: object) -> Any:
    if isinstance(obj, hou.Geometry):
        return obj
    try:
        return obj.geometry()  # type: ignore[attr-defined]
    except Exception:
        return None


def attrib_names(geo: Any) -> list[str]:
    names = []
    for attribs in (geo.pointAttribs, geo.primAttribs, geo.vertexAttribs, geo.globalAttribs):
        try:
            names += [a.name() for a in attribs()]
        except Exception:
            pass
    return list(dict.fromkeys(names))


def group_names(geo: Any) -> list[str]:
    names = []
    for groups in (geo.pointGroups, geo.primGroups, geo.vertexGroups, geo.edgeGroups):
        try:
            names += [g.name() for g in groups()]
        except Exception:
            pass
    return names


def arg_candidates(obj: object, member: Member, param: Param) -> list[object]:
    """Arguments to call a one-argument lookup with: real names, indices or frames for the
    receiver, and missing ones."""
    if member.name == "__getitem__":
        return [0]
    annotation = param.annotation or ""
    alternatives = {a.strip() for a in annotation.split("|")} if annotation.count("[") <= 1 else set()
    if "str" in alternatives:
        return string_candidates(obj, member, param)
    if "Sequence[str]" in alternatives:
        names = string_candidates(obj, member, param)
        return [names[1:3] + names[:1]]
    if annotation == "int" and INDEX_PARAM.search(param.name):
        return [0, 1, 9999]
    if annotation == "float" and FRAME_PARAM.search(param.name):
        return [1.0, 12.5]
    return []


def string_candidates(obj: object, member: Member, param: Param) -> list[str]:
    """Real names for a one-argument lookup on obj, after a missing one."""
    method = member.name
    lowered = f"{method} {param.name}".lower()
    names: list[str] = [MISSING_NAME]
    geo = geometry_of(obj) if type(obj).__module__ == "hou" else None
    try:
        if geo is not None and "attrib" in lowered:
            names += attrib_names(geo)
        elif geo is not None and "group" in lowered:
            names += group_names(geo)
        elif "intrinsic" in lowered and hasattr(obj, "intrinsicNames"):
            names += list(obj.intrinsicNames())  # type: ignore[attr-defined]
        elif isinstance(obj, hou.Node) and "parm" in lowered:
            names += first_names(obj.parms(), 200) + first_names(obj.parmTuples(), 100)
        elif isinstance(obj, hou.Node) and "userdata" in lowered:
            names += list(obj.userDataDict())
        elif isinstance(obj, hou.Node) and re.search("node|item|child|path", lowered):
            names += ["..", "."] + first_names(obj.children(), 10)
        elif isinstance(obj, hou.HDADefinition) and "section" in lowered:
            names += list(obj.sections())
        elif isinstance(obj, hou.DopSimulation) and "object" in lowered:
            names += first_names(obj.objects(), 10)
        elif obj is hou and re.search("node|item|path", lowered):
            names += ["/obj", "/obj/geo", "/obj/geo/scene", "/obj/geo/scene/tx"]
        elif obj is hou and "parm" in lowered:
            names += ["/obj/geo/tx", "/obj/geo/t", "/obj/parms/s4", "/obj/parms/f4", "/obj/parms/ramp"]
        elif obj is hou and re.search("env|var", lowered):
            names += ["HIP", "HFS", "HOUDINI_VERSION"]
    except Exception:
        pass
    return names


# --- the scene ---------------------------------------------------------------------------------

POINT_ATTRIB_CODE = r"""
node = hou.pwd()
geo = node.geometry()
for kind, create in (("point", hou.attribType.Point), ("prim", hou.attribType.Prim),
                     ("vertex", hou.attribType.Vertex), ("detail", hou.attribType.Global)):
    for size in (1, 2, 3, 4):
        geo.addAttrib(create, f"{kind}_i{size}", (1,) * size if size > 1 else 1)
        geo.addAttrib(create, f"{kind}_f{size}", (1.5,) * size if size > 1 else 1.5)
        geo.addAttrib(create, f"{kind}_s{size}", ("a",) * size if size > 1 else "a")
    geo.addAttrib(create, f"{kind}_m3", (1.0,) * 9)
    geo.addAttrib(create, f"{kind}_m4", (1.0,) * 16)
    geo.addAttrib(create, f"{kind}_d", {"a": 1, "b": [1.5, 2.5], "c": "x"})
    geo.addArrayAttrib(create, f"{kind}_ia", hou.attribData.Int)
    geo.addArrayAttrib(create, f"{kind}_fa", hou.attribData.Float)
    geo.addArrayAttrib(create, f"{kind}_fa3", hou.attribData.Float, 3)
    geo.addArrayAttrib(create, f"{kind}_sa", hou.attribData.String)
    geo.addArrayAttrib(create, f"{kind}_da", hou.attribData.Dict)
for p in geo.points():
    p.setAttribValue("point_ia", (1, 2, 3))
    p.setAttribValue("point_fa", (1.0, 2.0))
    p.setAttribValue("point_fa3", (1.0, 2.0, 3.0, 4.0, 5.0, 6.0))
    p.setAttribValue("point_sa", ("a", "b"))
    p.setAttribValue("point_da", ({"a": 1}, {"b": "c"}))
for pr in geo.prims():
    pr.setAttribValue("prim_ia", (1, 2))
    pr.setAttribValue("prim_sa", ("x",))
    pr.setAttribValue("prim_da", ({"a": 1},))
geo.setGlobalAttribValue("detail_ia", (4, 5))
geo.setGlobalAttribValue("detail_fa", (4.5,))
geo.setGlobalAttribValue("detail_sa", ("q", "r"))
geo.setGlobalAttribValue("detail_da", ({"k": 1},))
geo.addAttrib(hou.attribType.Point, "N", (0.0, 1.0, 0.0), transform_as_normal=True)
geo.addAttrib(hou.attribType.Point, "Cd", (1.0, 0.5, 0.25))
geo.addAttrib(hou.attribType.Point, "orient", (0.0, 0.0, 0.0, 1.0))
pg = geo.createPointGroup("pgroup")
pg.add(geo.points()[:3])
geo.createPointGroup("pgroup_empty")
prg = geo.createPrimGroup("primgroup")
prg.add(geo.prims()[:2])
eg = geo.createEdgeGroup("egroup")
eg.add(geo.globEdges("p0-1"))
vg = geo.createVertexGroup("vgroup")
vg.add([geo.prims()[0].vertex(0)])
"""

PRIMS_CODE = r"""
geo = hou.pwd().geometry()
poly = geo.createPolygon()
for pos in ((0, 0, 0), (1, 0, 0), (1, 1, 0)):
    point = geo.createPoint()
    point.setPosition(pos)
    poly.addVertex(point)
poly.setIsClosed(False)
geo.createNURBSCurve(4, False)
geo.createBezierCurve(4, False)
geo.createNURBSSurface(4, 4)
geo.createBezierSurface(4, 4)
geo.createMeshSurface(3, 3)
geo.createVolume(4, 4, 4)
geo.createTetrahedron()
geo.createHexahedron()
geo.createCameraPrim()
geo.createChannelPrim()
inner = hou.Geometry()
inner.createPolygon()
geo.createPackedGeometry(inner)
rig = hou.AgentRig("rig", ["root", "child"], [[1], []])
library = hou.AgentShapeLibrary()
shape = library.addShape("shape", inner)
definition = hou.AgentDefinition(rig, library)
definition.addLayer(hou.AgentLayer("default", rig, library, [hou.AgentShapeBinding(0, shape, False)]))
definition.addClip(hou.AgentClip("clip", rig, 10))
definition.addTransformGroup(hou.AgentTransformGroup("group", [0], rig))
agent = geo.createPacked("PackedAgent")
agent.setDefinition(definition)
agent.setCurrentLayer(definition.layers()[0])
"""


class Scene:
    def __init__(self, report: Report, tmp: pathlib.Path) -> None:
        self.report = report
        self.tmp = tmp
        self.seeds: list[object] = []

    def attempt(self, what: str, func: Callable[[], object]) -> Any:
        try:
            result = func()
        except Exception as e:
            self.report.setup_failures.append(f"{what}: {e!r}")
            return None
        if result is not None:
            self.seeds.append(result)
        return result

    def node(self, parent: Any, type_name: str, name: str | None = None) -> Any:
        if parent is None:
            return None
        return self.attempt(f"{parent.path()}/{type_name}", lambda: parent.createNode(type_name, name))

    def build(self) -> list[object]:
        obj = hou.node("/obj")
        for step in (
            self.build_parms, self.build_sops, self.build_objects, self.build_lops, self.build_dops,
            self.build_cops, self.build_tops, self.build_chops, self.build_rops, self.build_vops,
            self.build_network_items, self.build_hda, self.build_values,
        ):
            try:
                step(obj)
            except Exception as e:
                self.report.setup_failures.append(f"{step.__name__}: {e!r}")
        for node in hou.node("/").allSubChildren():
            try:
                node.cook()
            except Exception:
                pass
        return self.seeds

    def build_parms(self, obj: Any) -> None:
        node = self.node(obj, "null", "parms")
        if node is None:
            return
        group = node.parmTemplateGroup()
        templates: list[Any] = []
        for size in (1, 2, 3, 4):
            templates.append(hou.IntParmTemplate(f"i{size}", f"Int {size}", size))
            templates.append(hou.FloatParmTemplate(f"f{size}", f"Float {size}", size))
            templates.append(hou.StringParmTemplate(f"s{size}", f"String {size}", size))
        templates += [
            hou.FloatParmTemplate("color", "Color", 3, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA),
            hou.StringParmTemplate("file", "File", 1, string_type=hou.stringParmType.FileReference, default_value=("$HIP/x.bgeo",)),
            hou.StringParmTemplate("noderef", "Node", 1, string_type=hou.stringParmType.NodeReference, default_value=("/obj/geo",)),
            hou.StringParmTemplate("nodelist", "Nodes", 1, string_type=hou.stringParmType.NodeReferenceList, default_value=("/obj/geo /obj/cam",)),
            hou.StringParmTemplate("smenu", "String Menu", 1, menu_items=("a", "b"), menu_labels=("A", "B")),
            hou.StringParmTemplate("sscript", "String Script", 1, item_generator_script="['a', 'A', 'b', 'B']", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace),
            hou.ToggleParmTemplate("toggle", "Toggle", True),
            hou.MenuParmTemplate("menu", "Menu", ("x", "y", "z"), ("X", "Y", "Z")),
            hou.ButtonParmTemplate("button", "Button"),
            hou.LabelParmTemplate("label", "Label", ("text",)),
            hou.SeparatorParmTemplate("sep"),
            hou.RampParmTemplate("ramp", "Ramp", hou.rampParmType.Float),
            hou.RampParmTemplate("cramp", "Color Ramp", hou.rampParmType.Color),
            hou.DataParmTemplate("geodata", "Geometry Data", 1, data_parm_type=hou.dataParmType.Geometry),
            hou.DataParmTemplate("kvdata", "Key-Value Data", 1, data_parm_type=hou.dataParmType.KeyValueDictionary),
        ]
        folder = hou.FolderParmTemplate("folder", "Folder", folder_type=hou.folderType.Tabs)
        folder.addParmTemplate(hou.FloatParmTemplate("infolder", "In Folder", 1))
        multi = hou.FolderParmTemplate("multi", "Multi", folder_type=hou.folderType.MultiparmBlock)
        multi.addParmTemplate(hou.FloatParmTemplate("item#", "Item #", 2))
        multi.addParmTemplate(hou.StringParmTemplate("sitem#", "String Item #", 1))
        collapsible = hou.FolderParmTemplate("collapsible", "Collapsible", folder_type=hou.folderType.Collapsible)
        collapsible.addParmTemplate(hou.IntParmTemplate("incollapsible", "In Collapsible", 1))
        templates += [folder, multi, collapsible]
        for template in templates:
            group.append(template)
            self.seeds.append(template)
        self.attempt("parm templates", lambda: node.setParmTemplateGroup(group))
        self.seeds.append(group)

        def values() -> None:
            node.parm("multi").set(2)
            node.parm("f1").setExpression("$F * 2")
            node.parm("f2x").setExpression("hou.frame()", hou.exprLanguage.Python)
            node.parm("f3x").setKeyframe(hou.Keyframe(1.0, hou.frameToTime(1)))
            node.parm("f3x").setKeyframe(hou.Keyframe(5.0, hou.frameToTime(10)))
            key = hou.StringKeyframe()
            key.setFrame(1)
            key.setExpression("'a'", hou.exprLanguage.Python)
            node.parm("s1").setKeyframe(key)
            node.parm("i2x").set(hou.parm("/obj/parms/i1"))
            node.parm("geodata").set(hou.Geometry())
            node.parm("kvdata").set({"a": "b"})
            node.setUserData("key", "value")
            node.setCachedUserData("cached", [1, 2])
            node.setComment("comment")

        self.attempt("parm values", values)
        self.seeds += list(node.parms())

    def build_sops(self, obj: Any) -> None:
        geo = self.node(obj, "geo", "geo")
        if geo is None:
            return
        box = self.node(geo, "box", "box")
        attribs = self.node(geo, "python", "attribs")
        if attribs is not None:
            attribs.setInput(0, box)
            attribs.parm("python").set(POINT_ATTRIB_CODE)
        prims = self.node(geo, "python", "prims")
        if prims is not None:
            prims.parm("python").set(PRIMS_CODE)
        sources = [attribs, prims]
        for type_name, parms in (
            ("sphere", {"type": "prim"}),
            ("tube", {"type": "prim"}),
            ("circle", {"type": "prim"}),
            ("metaball", {}),
            ("polysoup", {}),
            ("volume", {"divsize": 0.5}),
            ("vdbfrompolygons", {}),
            ("pack", {}),
            ("testgeometry_crag", {}),
        ):
            node = self.node(geo, type_name)
            if node is None:
                continue
            for name, value in parms.items():
                if node.parm(name) is not None:
                    node.parm(name).set(value)
            if type_name in ("polysoup", "vdbfrompolygons", "pack"):
                node.setInput(0, box)
            sources.append(node)
        merge = self.node(geo, "merge", "scene")
        if merge is not None:
            for i, source in enumerate(s for s in sources if s is not None):
                merge.setInput(i, source)
            merge.setDisplayFlag(True)
            merge.setRenderFlag(True)
            self.attempt("scene geometry", merge.geometry)
            if merge.errors():
                self.report.setup_failures.append(f"{merge.path()}: {merge.errors()}")
        gap = self.node(geo, "merge", "input_gap")
        if gap is not None:
            gap.setInput(1, box)
        bad = self.node(geo, "file", "missing_file")
        if bad is not None:
            bad.parm("file").set("/nonexistent/missing.bgeo")
        self.node(geo, "null", "empty")
        wrangle = self.node(geo, "attribwrangle", "wrangle")
        if wrangle is not None:
            wrangle.setInput(0, box)
            wrangle.parm("snippet").set("v@v = @P; i[]@ia = array(1, 2);")
        self.node(geo, "attribvop", "attribvop")
        self.node(geo, "subnet", "subnet")
        if box is not None:
            self.attempt("detached geometry", lambda: self.detached_geometry(box))

    def detached_geometry(self, box: Any) -> Any:
        geo = hou.Geometry()
        geo.merge(box.geometry())
        self.seeds.append(geo.freeze())
        self.seeds += list(geo.globEdges("*"))[:4]
        self.seeds.append(hou.Geometry())
        return geo

    def build_objects(self, obj: Any) -> None:
        for type_name in ("cam", "hlight::2.0", "null", "subnet", "bone", "instance", "fetch", "ambient", "envlight", "lopimportcam", "chopnet", "shopnet", "ropnet", "matnet", "copnet", "cop2net", "topnet", "dopnet", "vopnet"):
            self.node(obj, type_name)
        subnet = hou.node("/obj/subnet1")
        if subnet is not None:
            self.node(subnet, "null", "inside")

    def build_lops(self, obj: Any) -> None:
        stage = hou.node("/stage")
        previous = None
        for type_name in ("sphere", "cube", "camera", "light::2.0", "materiallibrary", "sopimport", "configureprimitive", "null"):
            node = self.node(stage, type_name)
            if node is not None and previous is not None and node.type().maxNumInputs() > 0:
                node.setInput(0, previous)
            previous = node or previous
        if previous is not None:
            previous.setDisplayFlag(True)
            self.attempt("lop stage", previous.stage)

    def build_dops(self, obj: Any) -> None:
        dopnet = self.node(obj, "dopnet", "dops")
        if dopnet is None:
            return
        rbd = self.node(dopnet, "rbdobject")
        ground = self.node(dopnet, "groundplane")
        solver = self.node(dopnet, "rigidbodysolver")
        merge = self.node(dopnet, "merge")
        gravity = self.node(dopnet, "gravity")
        output = self.node(dopnet, "output")
        try:
            merge.setInput(0, rbd)
            merge.setInput(1, ground)
            solver.setInput(0, merge)
            gravity.setInput(0, solver)
            output.setInput(0, gravity)
            output.setDisplayFlag(True)
        except Exception as e:
            self.report.setup_failures.append(f"dop wiring: {e!r}")
        self.attempt("dop simulation", dopnet.simulation)
        self.attempt("dop frame", lambda: hou.setFrame(3))

    def build_cops(self, obj: Any) -> None:
        copnet = self.node(obj, "copnet", "cops")
        constant = self.node(copnet, "constant")
        noise = self.node(copnet, "fractalnoise")
        for node in (constant, noise):
            if node is not None:
                self.attempt("cop layer", node.layer)
                self.attempt("cop cable", node.cable)
        cop2net = self.node(obj, "cop2net", "cop2s")
        color = self.node(cop2net, "color")
        if color is not None:
            for parm, value in (("size1", 8), ("size2", 8)):
                if color.parm(parm) is not None:
                    color.parm(parm).set(value)

    def build_tops(self, obj: Any) -> None:
        topnet = self.node(obj, "topnet", "tops")
        generator = self.node(topnet, "genericgenerator")
        attrib = self.node(topnet, "attributecreate")
        if generator is not None and attrib is not None:
            attrib.setInput(0, generator)

    def build_chops(self, obj: Any) -> None:
        chopnet = self.node(hou.node("/obj"), "chopnet", "chops")
        wave = self.node(chopnet, "wave")
        constant = self.node(chopnet, "constant")
        if wave is not None:
            self.attempt("chop tracks", wave.tracks)
        if constant is not None:
            self.attempt("chop clip", lambda: constant.clip())

    def build_rops(self, obj: Any) -> None:
        out = hou.node("/out")
        for type_name in ("geometry", "opengl", "alembic", "usdrender", "karma", "ifd", "merge", "fetch"):
            self.node(out, type_name)

    def build_vops(self, obj: Any) -> None:
        mat = hou.node("/mat")
        self.node(mat, "principledshader::2.0")
        builder = self.node(mat, "materialbuilder")
        if builder is not None:
            bind = self.node(builder, "bind")
            add = self.node(builder, "add")
            parm = self.node(builder, "parameter")
            if add is not None and bind is not None:
                add.setInput(0, bind)
            if parm is not None and add is not None:
                add.setInput(1, parm)
        self.node(mat, "mtlxstandard_surface")
        self.node(mat, "subnet")
        shopnet = hou.node("/obj/shopnet1")
        self.node(shopnet, "vopmaterial")

    def build_network_items(self, obj: Any) -> None:
        geo = hou.node("/obj/geo")
        if geo is None:
            return
        box = self.attempt("network box", geo.createNetworkBox)
        if box is not None:
            box.addNode(geo.node("box"))
        self.attempt("empty network box", geo.createNetworkBox)
        self.attempt("sticky note", geo.createStickyNote)
        if geo.node("box") is not None and geo.node("attribs") is not None:
            self.attempt("dot", lambda: geo.node("attribs").inputConnections()[0])
            dot = self.attempt("network dot", geo.createNetworkDot)
            if dot is not None:
                dot.setInput(geo.node("box"))
        subnet = geo.node("subnet")
        if subnet is not None:
            self.seeds += list(subnet.indirectInputs())
        bundle = self.attempt("bundle", lambda: hou.addNodeBundle("check_bundle"))
        if bundle is not None:
            bundle.addNode(geo)
        self.attempt("empty bundle", lambda: hou.addNodeBundle("check_bundle_empty"))
        take = self.attempt("take", lambda: hou.takes.rootTake().addChildTake("check_take"))
        if take is not None and geo.parmTuple("t") is not None:

            def include() -> None:
                hou.takes.setCurrentTake(take)
                take.addParmTuple(geo.parmTuple("t"))
                hou.takes.setCurrentTake(hou.takes.rootTake())

            self.attempt("take parms", include)
        self.attempt("root take", hou.takes.rootTake)

    def build_hda(self, obj: Any) -> None:
        geo = hou.node("/obj/geo")
        if geo is None:
            return
        subnet = self.node(geo, "subnet", "asset")
        if subnet is None:
            return
        self.node(subnet, "box")

        def create() -> Any:
            asset = subnet.createDigitalAsset(
                name="check_runtime_types_asset",
                hda_file_name=str(self.tmp / "check_runtime_types.hda"),
                description="Check Runtime Types",
            )
            definition = asset.type().definition()
            definition.addSection("Extra", "contents")
            self.seeds += [definition, definition.options()] + list(definition.sections().values())
            return asset

        self.attempt("hda", create)
        self.node(geo, "testgeometry_pighead")

    def build_values(self, obj: Any) -> None:
        self.seeds += [
            hou.Vector2(1, 2), hou.Vector3(1, 2, 3), hou.Vector4(1, 2, 3, 4),
            hou.Matrix2(), hou.Matrix3(), hou.Matrix4(), hou.hmath.identityTransform(),
            hou.Quaternion(), hou.BoundingBox(0, 0, 0, 1, 1, 1), hou.Color(1, 0, 0),
            hou.Ramp((hou.rampBasis.Linear, hou.rampBasis.Linear), (0, 1), (0, 1)),
            hou.Ramp((hou.rampBasis.Linear, hou.rampBasis.Linear), (0, 1), ((0, 0, 0), (1, 1, 1))),
            hou.Keyframe(1.0), hou.StringKeyframe(), hou.ParmTemplateGroup(),
            hou.nodeTypeCategories()["Sop"], hou.sopNodeTypeCategory().nodeType("box"),
        ]
        self.attempt("oriented bbox", lambda: hou.OrientedBoundingBox())
        # Empty ones, which no node in the scene outputs, for the enums they return.
        self.attempt("nanovdb", lambda: hou.NanoVDB())
        self.attempt("detached attrib", lambda: hou.DetachedAttrib())
        self.attempt("ik target", lambda: hou.ik.Target())
        self.attempt("log entry", lambda: hou.logging.LogEntry(severity=hou.severityType.Warning))

        def agent() -> Any:
            rig = hou.AgentRig("rig", ["root", "child"], [[1], []])
            definition = hou.AgentDefinition(rig, hou.AgentShapeLibrary())
            definition.addTransformGroup(hou.AgentTransformGroup("group", [0], rig))
            self.seeds.append(rig)
            return definition

        self.attempt("agent definition", agent)

        def skeleton() -> Any:
            skeleton = hou.ik.Skeleton()
            skeleton.addJoint()
            return skeleton

        self.attempt("ik skeleton", skeleton)
        self.attempt("agent metadata", lambda: hou.AgentMetadata({"key": 1, "nested": {"a": [1.5]}}))

        def channel_list() -> Any:
            channels = hou.ChannelList()
            channels.addParm(hou.parm("/obj/parms/f3x"))
            return channels

        self.attempt("channel list", channel_list)
        self.attempt("bookmark", lambda: hou.anim.newBookmark("check_bookmark", 1, 10))
        box = hou.node("/obj/geo/box")
        if box is not None:
            self.attempt("selection", lambda: hou.Selection(box.geometry().points()[:2]))

            def profile() -> Any:
                result = hou.perfMon.startProfile("check_runtime_types")
                box.cook(force=True)
                result.stop()
                return result

            self.attempt("perfmon profile", profile)
            self.attempt("node group", lambda: box.parent().addNodeGroup("check_group")).addNode(box)
        lop = hou.node("/stage/sphere1")
        if lop is not None:
            self.attempt("viewport overrides", lambda: hou.node("/stage").viewportOverrides(lop))


def unchecked_getters(stub: Stub, report: Report) -> list[str]:
    """The members the walker could have called without arguments but never checked."""
    result = []
    members = [*stub.functions.values()] + [m for c in stub.classes.values() for m in c.members.values()]
    for member in members:
        if member.label in report.checked or is_denied(member) or member.name.startswith("_") or member.name == "thisown":
            continue
        if member.owner.startswith("_") or member.attribute is not None and member.name[0].isupper():
            continue
        if member.attribute is not None or any(not s.required for s in member.signatures):
            result.append(member.label)
    return sorted(result)


def unchecked_enum_returns(stub: Stub, report: Report) -> list[str]:
    """The members whose (return) type names an enum, but which were never checked."""
    result = []
    members = [*stub.functions.values()] + [m for c in stub.classes.values() for m in c.members.values()]
    for member in members:
        if member.label in report.checked or member.attribute is not None and member.name[0].isupper():
            continue
        types_ = [member.attribute] if member.attribute is not None else [s.returns or "" for s in member.signatures]
        if any("EnumValue[" in t for t in types_):
            result.append(member.label)
    return sorted(result)


def print_report(report: Report, args: argparse.Namespace, stub: Stub) -> int:
    def section(title: str, count: int) -> None:
        print(f"\n== {title}: {count}")

    def mismatches(known: bool) -> list[tuple[str, str]]:
        return sorted(k for k in report.mismatches if (k[0] in KNOWN_MISMATCHES) == known)

    failures = mismatches(known=False)
    for title, keys in (("mismatches", failures), ("known mismatches (not in the hou stub)", mismatches(known=True))):
        section(title, len(keys))
        for member, annotation in keys:
            reason = f"  ({KNOWN_MISMATCHES[member]})" if member in KNOWN_MISMATCHES else ""
            print(f"{member}: {annotation}{reason}")
            for got, (count, example) in sorted(report.mismatches[(member, annotation)].items()):
                print(f"    got {got}  ({count}x, e.g. {example})")
    section("signature errors (calls the stub allows raised TypeError)", len(report.signature_errors))
    for member, (count, example) in sorted(report.signature_errors.items()):
        print(f"{member}  ({count}x, e.g. {example})")
    section("annotations that could not be evaluated", len(report.unevaluable))
    for item, error in sorted(report.unevaluable.items()):
        print(f"{item}  ({error})")
    section("stub members missing at runtime", len(report.missing))
    if args.missing:
        for item in sorted(report.missing):
            print(item)
    section("timeouts", len(report.timeouts))
    for member, example in sorted(report.timeouts.items()):
        print(f"{member}  ({example})")
    section("scene setup failures", len(report.setup_failures))
    for failure in report.setup_failures:
        print(failure)
    section("exceptions", len(report.exceptions))
    if args.exceptions:
        for (member, name), (count, example) in sorted(report.exceptions.items()):
            print(f"{member}: {name}  ({count}x, e.g. {example})")
    if args.coverage:
        section("members checked", len(report.checked))
        for member, count in sorted(report.checked.items()):
            print(f"{member}  {count}x")
        unchecked = unchecked_getters(stub, report)
        section("getters never checked (not reached, or always raised)", len(unchecked))
        for member in unchecked:
            print(member)
    section("values typed with Any (what they held, to tighten them from)", len(report.any_shapes))
    for member, annotation in sorted(report.any_shapes):
        print(f"{member}: {annotation}")
        for got, (count, example) in sorted(report.any_shapes[(member, annotation)].items()):
            print(f"    got {got}  ({count}x, e.g. {example})")
    unchecked_enums = unchecked_enum_returns(stub, report)
    section("enum returns never checked (listed with --coverage)", len(unchecked_enums))
    if args.coverage:
        for member in unchecked_enums:
            print(member)
    print(f"\nchecked {sum(report.checked.values())} values from {len(report.checked)} members")
    return 1 if failures or report.signature_errors else 0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--class", dest="cls", help="only report members of classes matching this regex ('hou' for module level)")
    parser.add_argument("--depth", type=int, default=6, help="how far to walk from the scene (default 6)")
    parser.add_argument("--per-class", type=int, default=40, help="objects to walk into per class, beyond the scene's own (default 40)")
    parser.add_argument("--timeout", type=float, default=10.0, help="seconds per call before it is reported (default 10)")
    parser.add_argument("--exceptions", action="store_true", help="list the exceptions calls raised")
    parser.add_argument("--missing", action="store_true", help="list the stub members missing at runtime")
    parser.add_argument("--coverage", action="store_true", help="list the members checked, and the getters never checked")
    parser.add_argument("--stub", type=pathlib.Path, default=STUB)
    parser.add_argument("--ui", action="store_true", help="also walk the UI classes; run in an interactive Houdini (see above)")
    parser.add_argument("--journal", help=argparse.SUPPRESS)
    parser.add_argument("--skip", action="append", default=[], help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.ui:
        run_ui(args)
        return
    if not args.journal:
        sys.exit(supervise(sys.argv[1:]))

    signal.signal(signal.SIGALRM, on_timeout)
    stub = parse_stub(args.stub)
    ns, failures = build_namespace(stub)
    report = Report()
    report.setup_failures += [f"stub definition {f}" for f in failures]
    tmp = pathlib.Path(args.journal).parent / "scene"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir()
    try:
        seeds = Scene(report, tmp).build()
        walker = Walker(stub, ns, args, report)
        walker.check_declared()
        walker.run_module()
        walker.run(seeds)
        for node in (hou.node("/obj/geo/box"), hou.node("/obj/geo"), hou.node("/obj/parms")):
            if node is not None:
                node.setSelected(True)
        hou.node("/obj/geo").setCurrent(True)
        walker.run_module()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    sys.stdout.flush()
    sys.exit(print_report(report, args, stub))


def run_ui(args: argparse.Namespace) -> None:
    """The check, in an interactive Houdini, with the UI classes too.

    It can't restart Houdini when a call crashes it, so it journals each call: when it starts and
    the journal of the previous run doesn't end with DONE, that run's last call crashed it, and
    is skipped from then on.
    """
    global UI_MODE
    import contextlib

    if not hou.isUIAvailable():
        print("--ui needs an interactive Houdini; run this in its Python Shell")
        return
    if any(hou.node(path).children() for path in ("/obj", "/out", "/stage", "/mat", "/tasks") if hou.node(path)):
        print("Run this in a new, empty scene (File > New): it builds its own scene.")
        return
    skips = UI_SKIPS.read_text().splitlines() if UI_SKIPS.exists() else []
    if UI_JOURNAL.exists():
        lines = UI_JOURNAL.read_text().splitlines()
        if lines and lines[-1] != "DONE":
            skips.append(lines[-1].split("\t")[0])
            print(f"The last run crashed in {lines[-1].split(chr(9), 1)[-1]}; skipping it from now on.")
    UI_SKIPS.parent.mkdir(exist_ok=True)
    UI_SKIPS.write_text("".join(f"{s}\n" for s in dict.fromkeys(skips)))
    args.skip += skips
    args.journal = str(UI_JOURNAL)
    UI_MODE = True
    DENIED_CLASSES.intersection_update(UI_DENIED_CLASSES)
    try:
        signal.signal(signal.SIGALRM, on_timeout)
    except ValueError:  # not in the main thread: no timeouts
        pass

    stub = parse_stub(args.stub)
    ns, failures = build_namespace(stub)
    report = Report()
    report.setup_failures += [f"stub definition {f}" for f in failures]
    tmp = UI_JOURNAL.parent / "runtime_types_ui_scene"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir()
    try:
        seeds = Scene(report, tmp).build()
        desktop = hou.ui.curDesktop()
        seeds += [desktop, *desktop.panes(), *desktop.paneTabs(), *hou.ui.floatingPanels()]
        for tab in desktop.paneTabs():
            if isinstance(tab, hou.SceneViewer):
                seeds += [*tab.viewports(), tab.curViewport().settings(), tab.flipbookSettings()]
        walker = Walker(stub, ns, args, report)
        walker.check_declared()
        walker.run_module()
        walker.run(seeds)
        walker.run_module()
        if walker.journal is not None:
            walker.journal.write("DONE\n")
            walker.journal.close()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    with open(UI_REPORT, "w") as out, contextlib.redirect_stdout(out):
        print_report(report, args, stub)
        print(f"\n== calls skipped because they crashed Houdini: {len(skips)}")
        for key in dict.fromkeys(skips):
            print(key)
    print(f"Wrote {UI_REPORT}")


def supervise(argv: Sequence[str]) -> int:
    """Run the check in a child hython, restarting it without the call that crashed it (some HOM
    calls segfault on unusual input, e.g. an out-of-range index) until it completes."""
    hython = shutil.which("hython") or sys.executable
    crashes: dict[str, str] = {}
    with tempfile.TemporaryDirectory(prefix="check_runtime_types_") as tmp:
        journal = pathlib.Path(tmp, "journal")
        while True:
            skips = [f"--skip={key}" for key in crashes]
            proc = subprocess.run(
                [hython, __file__, *argv, f"--journal={journal}", *skips],
                stdin=subprocess.DEVNULL, capture_output=True, text=True,
            )
            if proc.returncode in (0, 1):
                if "== mismatches" not in proc.stdout:
                    # A traceback also exits with 1: report it rather than an empty report.
                    print(proc.stdout, proc.stderr[-3000:], sep="\n")
                    print("the check failed before it reported")
                    return 2
                print(proc.stdout, end="")
                print(f"\n== calls that crashed hython (skipped): {len(crashes)}")
                for key, example in crashes.items():
                    print(f"{key}  (e.g. {example})")
                return proc.returncode
            lines = journal.read_text().splitlines() if journal.exists() else []
            if not lines or lines[-1].split("\t")[0] in crashes:
                print(proc.stdout, proc.stderr[-3000:], sep="\n")
                print(f"hython failed with status {proc.returncode}")
                return 2
            key, example = lines[-1].split("\t", 1)
            crashes[key] = example
            print(f"hython crashed (status {proc.returncode}) in {example}; restarting without {key}", flush=True)


if __name__ == "__main__":
    main()
