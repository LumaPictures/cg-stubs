"""Optional mypy plugin that improves type checking of PySide6 signals.

The plugin provides three features that cannot be expressed in the stubs
alone:

1. ``Signal(object)`` means ``typing.Any``.

   ``Signal(object)`` is a common PySide idiom for declaring a signal that
   emits an arbitrary/complex value (Qt registers it as ``PyObject``), so its
   idiomatic meaning is ``typing.Any`` rather than ``builtins.object``.  The
   distinction matters to a type checker: a slot annotated with a specific
   type is not compatible with an ``object`` argument (callables are
   contravariant in their arguments), so without this plugin
   ``Signal(object).connect(slot)`` is an error for any slot more specific
   than ``object``.

   This cannot be fixed in the stubs: any ``Signal.__init__`` overload that
   accepts ``type[object]`` also accepts every other ``type[X]``, and mypy
   matches ``SignalInstance[tuple[X]]`` covariantly against
   ``SignalInstance[tuple[object]]``, so a stub-level special case would erase
   the type checking of every other signal.  The plugin instead rewrites the
   type at the declaration site, which is precise: only arguments declared as
   ``object`` become ``Any``; all other arguments of the same signal remain
   strictly checked.  Arguments declared as ``typing.Any`` (a real,
   instantiable class at runtime since Python 3.11, which PySide6 likewise
   registers as ``PyObject``) are treated the same way, since mypy otherwise
   treats the *value* ``Any`` nominally.

   This feature can be disabled with the ``object_as_any`` option (below).

2. ``signal[...]`` is validated against every declared signature, and the
   result is narrowed to the selected signature.

   At runtime, subscripting a signal selects one of its declared signatures
   (raising ``IndexError`` when none matches), and ``connect``/``emit`` on the
   result use exactly that signature.  The stubs can only validate an index
   against the signal's *first or last* signature: an index selecting a middle
   signature of a three-plus-signature signal is a false positive, and an
   index that matches no signature at all falls through to an unchecked
   catch-all that returns an unparametrized (unchecked) ``SignalInstance``.
   The plugin replaces the stub overloads and instead compares a literal index
   against every declared signature: a match narrows the result to
   ``SignalInstance[<matched signature>]`` (so subsequent ``connect``/``emit``
   are checked against the signature the index selected, mirroring runtime
   dispatch), and a literal index that matches no declared signature is
   reported (it raises ``IndexError`` at runtime).  Non-literal indexes (e.g.
   a variable of type ``tuple[type, ...]``) are left unchecked.

3. A native signal with a defaulted trailing C++ parameter is treated as
   having optional trailing arguments.

   Qt registers one signature per defaulted parameter of a C++ signal, so
   ``void clicked(bool checked = false)`` and ``void dataChanged(a, b,
   roles = {})`` reach the stubs as multi-signature signals, exactly like a
   Python signal declared with genuinely distinct signatures::

       clicked:     Signal[tuple[()], tuple[bool]]
       dataChanged: Signal[tuple[QModelIndex, QModelIndex, Any],
                           tuple[QModelIndex, QModelIndex]]
       s:           Signal[tuple[int, int], tuple[str, str]]  # Signal((int, int), (str, str))

   The two cases behave differently at runtime, and the difference is
   visible in the stubs only as one signature being a *prefix* of another:
   no dispatch happens for a C++ default argument, C++ simply fills the
   default in.  Concretely, on a native signal whose signatures form a
   prefix chain:

   - ``emit`` may omit the trailing arguments that a shorter registered
     signature drops (``dataChanged.emit(a, b)`` is valid; the stubs bind
     ``emit`` to the default signature only, so they report "too few
     arguments");
   - ``connect`` accepts a slot with as many arguments as the *longest*
     signature, because PySide picks the registered signature whose
     argument count matches the slot's (``clicked.connect(slot_taking_a_bool)``
     is valid, and the slot does receive the ``checked`` value).

   Neither relaxation is applied to a Python-declared signal, where a
   prefix relation between signatures carries no such meaning: ``Signal(
   (int, str), (int,)).emit(1)`` raises TypeError at runtime, because
   unsubscripted ``emit`` uses the default signature and nothing fills in
   the missing argument.  The plugin therefore relaxes only signals
   declared in the ``PySide6`` package itself, which are all C++ signals.
   The signal must be accessed directly on its owner (``obj.sig.emit(...)``,
   ``self.sig.connect(...)``) for the plugin to see where it was declared;
   a signal first stored in a local variable is checked strictly.

Unsubscripted ``connect``/``emit`` on a signal with genuinely distinct
signatures use only the default (first) signature at runtime -- PySide does
not dispatch across such signatures by argument type -- and the stubs
already check them against the first signature, so the plugin leaves them
alone.

Usage (mypy configuration)::

    [tool.mypy]
    plugins = ["types_pyside6_mypy_plugin"]

Plugin options are read from the same config file that mypy was invoked with:
a ``[tool.types-pyside6-mypy]`` table in pyproject.toml, or a
``[types-pyside6-mypy]`` section in ini-style files (mypy.ini / setup.cfg)::

    [tool.types-pyside6-mypy]
    # Set to false to opt out of rewriting object/typing.Any arguments of
    # Signal(...) declarations to typing.Any (feature 1 above).
    object_as_any = true
"""

from __future__ import annotations

import configparser
import dataclasses
import functools
import os
from typing import Any, Callable, Optional

from mypy import errorcodes
from mypy.nodes import ARG_OPT, ARG_POS, CallExpr, Context, Expression, MemberExpr, Var
from mypy.options import Options
from mypy.plugin import (
    CheckerPluginInterface,
    FunctionContext,
    MethodContext,
    MethodSigContext,
    Plugin,
    ReportConfigContext,
)
from mypy.types import (
    AnyType,
    CallableType,
    FunctionLike,
    Instance,
    Overloaded,
    ProperType,
    TupleType,
    Type,
    TypeOfAny,
    TypeType,
    UnionType,
    get_proper_type,
)

try:
    import tomllib
except ImportError:  # python < 3.11
    try:
        import tomli as tomllib  # type: ignore[import-not-found, no-redef]
    except ImportError:
        tomllib = None  # type: ignore[assignment]

SIGNAL = "PySide6.QtCore.Signal"
SIGNAL_INSTANCE = "PySide6.QtCore.SignalInstance"
# The protocols the stubs use to describe an acceptable slot: a callable with
# the signature's arguments, or another signal that emits them.
_SLOT_PROTOCOLS = ("PySide6.QtCore._SlotFunc", "PySide6.QtCore._SignalEmitter")

# Type arguments to Signal(...) that idiomatically mean "anything".
_ANY_CLASSES = frozenset({"builtins.object", "typing.Any"})

# Signals declared inside this package are C++ signals, where a signature
# that is a prefix of another means a defaulted trailing parameter.
_NATIVE_PACKAGE = "PySide6."

TOML_TABLE = "types-pyside6-mypy"  # [tool.types-pyside6-mypy]
INI_SECTION = "types-pyside6-mypy"  # [types-pyside6-mypy]


@dataclasses.dataclass
class PluginConfig:
    """Plugin options, read from mypy's own config file."""

    # Rewrite object/typing.Any arguments of Signal(...) declarations to
    # typing.Any.
    object_as_any: bool = True


def _read_config(config_file: Optional[str]) -> PluginConfig:
    config = PluginConfig()
    if not config_file or not os.path.exists(config_file):
        return config
    if config_file.endswith(".toml"):
        if tomllib is None:
            raise ValueError(
                f"types-pyside6-mypy: reading options from {config_file} requires "
                "tomllib (python 3.11+) or tomli to be installed"
            )
        with open(config_file, "rb") as fh:
            data = tomllib.load(fh)
        section = data.get("tool", {}).get(TOML_TABLE, {})
        if "object_as_any" in section:
            value = section["object_as_any"]
            if not isinstance(value, bool):
                raise ValueError(
                    f"types-pyside6-mypy: object_as_any must be a boolean, "
                    f"got {value!r} in {config_file}"
                )
            config.object_as_any = value
    else:
        parser = configparser.ConfigParser()
        parser.read(config_file)
        if parser.has_section(INI_SECTION):
            try:
                config.object_as_any = parser.getboolean(
                    INI_SECTION, "object_as_any", fallback=config.object_as_any
                )
            except ValueError as err:
                raise ValueError(
                    f"types-pyside6-mypy: object_as_any must be a boolean "
                    f"in {config_file}: {err}"
                ) from None
    return config


def _rewrite_signature(sig: TupleType) -> TupleType:
    """Replace object/Any-class items of one signature tuple with Any."""
    items: list[Type] = []
    for item in sig.items:
        proper_item = get_proper_type(item)
        if (
            isinstance(proper_item, Instance)
            and proper_item.type.fullname in _ANY_CLASSES
        ):
            items.append(AnyType(TypeOfAny.explicit))
        else:
            items.append(item)
    return sig.copy_modified(items=items)


def _signal_hook(ctx: FunctionContext) -> Type:
    """Rewrite the inferred type of a ``Signal(...)`` call.

    ``Signal(object)`` infers as ``Signal[tuple[object]]``; this returns
    ``Signal[tuple[Any]]`` instead (likewise for any ``object`` argument in
    any signature of a multi-signature signal).
    """
    ret = get_proper_type(ctx.default_return_type)
    if isinstance(ret, Instance) and ret.type.fullname == SIGNAL:
        new_args: list[Type] = []
        for sig in ret.args:
            proper_sig = get_proper_type(sig)
            if isinstance(proper_sig, TupleType):
                new_args.append(_rewrite_signature(proper_sig))
            else:
                new_args.append(sig)
        return ret.copy_modified(args=new_args)
    return ctx.default_return_type


def _declared_signatures(receiver: Type) -> Optional[list[TupleType]]:
    """The declared signatures of a parametrized SignalInstance.

    Returns None for anything else -- an unparametrized or irregular
    SignalInstance gets the stubs' fully permissive fallback.
    """
    proper_receiver = get_proper_type(receiver)
    if (
        not isinstance(proper_receiver, Instance)
        or proper_receiver.type.fullname != SIGNAL_INSTANCE
        or not proper_receiver.args
    ):
        return None
    sigs = []
    for sig in proper_receiver.args:
        proper_sig = get_proper_type(sig)
        if not isinstance(proper_sig, TupleType):
            return None
        sigs.append(proper_sig)
    return sigs


def _index_arg_types(index: Type) -> Optional[list[ProperType]]:
    """The per-argument class types of a literal signal index.

    Handles the ``sig[str]``, ``sig[str, int]`` and ``sig[(str,)]`` forms,
    where each element is a reference to a class.  Returns None when the
    index is not literal enough to validate (e.g. a variable of type
    ``tuple[type, ...]``).
    """
    proper_index = get_proper_type(index)
    if isinstance(proper_index, TupleType):
        elements = proper_index.items
    else:
        elements = [proper_index]
    result = []
    for element in elements:
        proper_element = get_proper_type(element)
        if isinstance(proper_element, TypeType):
            # a variable annotated as type[X]
            result.append(get_proper_type(proper_element.item))
        elif (
            isinstance(proper_element, (CallableType, Overloaded))
            and proper_element.is_type_obj()
        ):
            # a direct reference to a class, e.g. the `str` in `sig[str]`
            item = (
                proper_element.items[0]
                if isinstance(proper_element, Overloaded)
                else proper_element
            )
            result.append(get_proper_type(item.ret_type))
        else:
            return None
    return result


def _index_matches_signature(sig: TupleType, index_types: list[ProperType]) -> bool:
    """Whether an index selects this signature.

    Runtime lookup is by the C++ signature string, i.e. by argument count and
    exact argument types (a subclass does not match: ``sig[bool]`` raises
    IndexError on a ``Signal(int)``).  Signature arguments that are ``Any``
    (e.g. rewritten ``Signal(object)`` arguments) accept any index element.
    """
    if len(sig.items) != len(index_types):
        return False
    for declared, provided in zip(sig.items, index_types):
        proper_declared = get_proper_type(declared)
        if isinstance(proper_declared, AnyType) or isinstance(provided, AnyType):
            continue
        if not (
            isinstance(proper_declared, Instance)
            and isinstance(provided, Instance)
            and proper_declared.type.fullname == provided.type.fullname
        ):
            return False
    return True


def _getitem_signature_hook(ctx: MethodSigContext) -> FunctionLike:
    """Relax the stub overloads of ``SignalInstance.__getitem__``.

    The stubs can only validate an index against the first or last declared
    signature, which both misses invalid indexes (the catch-all overload
    accepts any tuple) and produces false positives (an index selecting a
    middle signature matches no overload).  Replace them with a fully
    permissive signature; the real validation and result narrowing happen in
    ``_getitem_hook``, which sees the inferred index type.
    """
    if _declared_signatures(ctx.type) is None:
        return ctx.default_signature
    any_type = AnyType(TypeOfAny.implementation_artifact)
    return ctx.default_signature.copy_modified(
        arg_types=[any_type],
        arg_kinds=[ARG_POS],
        arg_names=[None],
        ret_type=any_type,
    )


def _getitem_hook(ctx: MethodContext) -> Type:
    """Validate a signal index and narrow the result to the selected signature.

    A literal index matching a declared signature returns
    ``SignalInstance[<matched signature>]``, so subsequent ``connect``/``emit``
    calls are checked against the signature the index selected -- exactly what
    runtime dispatch does.  A literal index matching no declared signature is
    an error (``IndexError`` at runtime).  A non-literal index cannot be
    validated and stays fully permissive.
    """
    receiver = get_proper_type(ctx.type)
    sigs = _declared_signatures(receiver)
    if sigs is None or not ctx.arg_types or not ctx.arg_types[0]:
        return ctx.default_return_type
    index_types = _index_arg_types(ctx.arg_types[0][0])
    if index_types is None:
        return ctx.default_return_type
    for sig in sigs:
        if _index_matches_signature(sig, index_types):
            assert isinstance(receiver, Instance)
            return Instance(receiver.type, [sig])
    ctx.api.fail(
        "Signal index matches no declared signature (raises IndexError at runtime)",
        ctx.context,
        code=errorcodes.INDEX,
    )
    return AnyType(TypeOfAny.from_error)


def _same_arg(left: Type, right: Type) -> bool:
    """Whether two signature arguments are the same declared type.

    Deliberately conservative: anything this cannot compare structurally is
    reported as different, which only ever means a signal is *not* treated
    as having optional trailing arguments.
    """
    proper_left = get_proper_type(left)
    proper_right = get_proper_type(right)
    if isinstance(proper_left, AnyType) or isinstance(proper_right, AnyType):
        # `Any` is the stubs' translation of a C++ type PySide passes through
        # as PyObject; it is the same argument only as another such argument
        # (it must not compare equal to every type, as subtyping would).
        return isinstance(proper_left, AnyType) and isinstance(proper_right, AnyType)
    if isinstance(proper_left, Instance) and isinstance(proper_right, Instance):
        return (
            proper_left.type.fullname == proper_right.type.fullname
            and len(proper_left.args) == len(proper_right.args)
            and all(
                _same_arg(x, y) for x, y in zip(proper_left.args, proper_right.args)
            )
        )
    return False


def _prefix_chain(sigs: list[TupleType]) -> Optional[list[TupleType]]:
    """The signatures sorted by length, if each is a prefix of the next.

    A prefix relation between the registered signatures of a *native* signal
    means a defaulted trailing C++ parameter: Qt registers one signature per
    default argument, so the shortest signature holds the arguments C++
    requires and the longest holds every argument it accepts.  Signatures
    that are not prefix-related are genuinely distinct overloads, which
    runtime does not dispatch between.
    """
    ordered = sorted(sigs, key=lambda sig: len(sig.items))
    for shorter, longer in zip(ordered, ordered[1:]):
        if not all(_same_arg(x, y) for x, y in zip(shorter.items, longer.items)):
            return None
    return ordered


def _declaring_var(api: CheckerPluginInterface, expr: Expression) -> Optional[Var]:
    """The variable that ``expr`` reads, if it reads an attribute of a class.

    Resolved through the type of the object the attribute is read from, so
    that the *declaring* class is found even when the attribute is inherited
    (``self.dataChanged`` in a QAbstractItemModel subclass).
    """
    if not isinstance(expr, MemberExpr):
        return None
    # The receiver of the call has already been type checked at this point,
    # so its type is in the checker's type map; looking it up avoids
    # re-checking (and re-reporting) the expression.
    lookup = getattr(api, "lookup_type", None)
    if lookup is None:  # pragma: no cover - not a real TypeChecker
        return None
    try:
        base = lookup(expr.expr)
    except KeyError:  # pragma: no cover - defensive
        return None
    proper_base = get_proper_type(base)
    if not isinstance(proper_base, Instance):
        return None
    # TypeInfo.get() searches the MRO, and returns the node of the class that
    # declares the name -- an override in a subclass shadows it, as it does
    # at runtime.
    sym = proper_base.type.get(expr.name)
    node = sym.node if sym is not None else None
    return node if isinstance(node, Var) else None


def _receiver_expr(context: Context, method: str) -> Optional[Expression]:
    """The expression the hooked method is called on, e.g. ``self.clicked``."""
    if isinstance(context, CallExpr) and isinstance(context.callee, MemberExpr):
        # `sig.emit(...)` -> `sig`; an implicit `sig(...)` -> `sig`
        callee = context.callee
        return callee.expr if callee.name == method else callee
    return None


def _is_native_signal(ctx: MethodSigContext, method: str) -> bool:
    """Whether the signal called here is declared in the PySide6 package.

    Only C++ signals gain a signature per defaulted parameter, so only they
    may be relaxed.  A signal that is not read directly from the object that
    declares it (e.g. one stored in a local variable first) cannot be traced
    back to its declaration, and is treated as non-native, i.e. checked
    strictly.
    """
    expr = _receiver_expr(ctx.context, method)
    if expr is None:
        return False
    var = _declaring_var(ctx.api, expr)
    return var is not None and (var.fullname or "").startswith(_NATIVE_PACKAGE)


def _default_arg_signatures(
    ctx: MethodSigContext, method: str
) -> Optional[tuple[list[TupleType], TupleType]]:
    """The signatures of the signal called here, shortest first, and its default.

    Returns None unless the receiver is a native signal whose signatures form
    a prefix chain, i.e. a C++ signal with defaulted trailing parameters.
    """
    sigs = _declared_signatures(ctx.type)
    if sigs is None or len(sigs) < 2:
        return None
    ordered = _prefix_chain(sigs)
    if ordered is None:
        return None
    if not _is_native_signal(ctx, method):
        return None
    return ordered, sigs[0]


def _emit_signature_hook(ctx: MethodSigContext) -> FunctionLike:
    """Make the trailing C++ default arguments of ``emit`` optional.

    ``emit`` uses the signal's default (first) signature at runtime, and any
    trailing argument that a shorter registered signature drops is filled in
    by C++, so it may be omitted.  The stubs bind ``emit`` to the default
    signature with every argument required.
    """
    result = _default_arg_signatures(ctx, "emit")
    if result is None:
        return ctx.default_signature
    ordered, _ = result
    # The number of arguments C++ requires: those of the shortest signature.
    required = len(ordered[0].items)
    # The bound signature's arguments are the default signature's, expanded
    # from `*args: *tuple[...]` into one positional argument each.
    sig = ctx.default_signature
    if not all(kind == ARG_POS for kind in sig.arg_kinds):  # pragma: no cover
        return ctx.default_signature
    if required >= len(sig.arg_types):
        # The default signature is the shortest one: emit() cannot pass more
        # arguments than the signature it dispatches to declares (e.g.
        # `clicked.emit(True)` raises TypeError; only `clicked[bool].emit(True)`
        # emits the argument).
        return ctx.default_signature
    return sig.copy_modified(
        arg_kinds=[ARG_POS] * required + [ARG_OPT] * (len(sig.arg_types) - required),
        imprecise_arg_kinds=False,
    )


def _connect_signature_hook(ctx: MethodSigContext, method: str) -> FunctionLike:
    """Let ``connect``/``disconnect`` accept the longest C++ signature.

    PySide connects a slot to the registered signature whose argument count
    matches the slot's, so a slot may take as many arguments as the longest
    signature -- ``clicked.connect(slot)`` passes ``checked`` to a slot that
    takes it -- while the stubs only allow up to the default signature's
    argument count.  The extra arities are added to the slot union of every
    overload item, leaving the rest of the signature (and the arities the
    stubs already accept) untouched.
    """
    result = _default_arg_signatures(ctx, method)
    if result is None:
        return ctx.default_signature
    ordered, default = result
    longest = ordered[-1]
    # The default signature's arguments are what the stubs check the slot
    # against.
    default_args = default.items
    if len(longest.items) <= len(default_args):
        # The default signature is the longest: the stubs already accept every
        # slot arity the signal can be connected to.
        return ctx.default_signature
    sig = ctx.default_signature
    if not sig.arg_types:  # pragma: no cover - defensive
        return ctx.default_signature
    slot_arg = get_proper_type(sig.arg_types[0])
    items = list(slot_arg.items) if isinstance(slot_arg, UnionType) else [slot_arg]
    # Group the accepted arities by protocol, so that the new union reads like
    # the one the stubs declare, e.g.
    # `_SlotFunc[()] | _SlotFunc[bool] | _SignalEmitter[()] | _SignalEmitter[bool]`.
    arities: dict[str, set[int]] = {}
    infos: dict[str, Instance] = {}
    others: list[Type] = []
    for item in items:
        proper_item = get_proper_type(item)
        if (
            isinstance(proper_item, Instance)
            and proper_item.type.fullname in _SLOT_PROTOCOLS
        ):
            infos[proper_item.type.fullname] = proper_item
            arities.setdefault(proper_item.type.fullname, set()).add(
                len(proper_item.args)
            )
        else:
            # e.g. the `| None` of disconnect(); left as it is, at the end.
            others.append(item)
    if not infos:  # pragma: no cover - defensive
        return ctx.default_signature
    extra = set(range(len(default_args) + 1, len(longest.items) + 1))
    new_items: list[Type] = []
    for fullname in _SLOT_PROTOCOLS:
        instance = infos.get(fullname)
        if instance is None:
            continue
        for arity in sorted(arities[fullname] | extra):
            new_items.append(Instance(instance.type, list(longest.items[:arity])))
    return sig.copy_modified(
        arg_types=[UnionType.make_union(new_items + others)] + list(sig.arg_types[1:])
    )


class TypesPySide6Plugin(Plugin):
    def __init__(self, options: Options) -> None:
        super().__init__(options)
        self._config = _read_config(options.config_file)

    def report_config_data(self, ctx: ReportConfigContext) -> Any:
        # stored in mypy's cache metadata: invalidates the incremental cache
        # when the plugin options change between runs
        return dataclasses.asdict(self._config)

    def get_function_hook(
        self, fullname: str
    ) -> Optional[Callable[[FunctionContext], Type]]:
        if fullname == SIGNAL and self._config.object_as_any:
            return _signal_hook
        return None

    def get_method_signature_hook(
        self, fullname: str
    ) -> Optional[Callable[[MethodSigContext], FunctionLike]]:
        if fullname == f"{SIGNAL_INSTANCE}.__getitem__":
            return _getitem_signature_hook
        if fullname == f"{SIGNAL_INSTANCE}.emit":
            return _emit_signature_hook
        for method in ("connect", "disconnect"):
            if fullname == f"{SIGNAL_INSTANCE}.{method}":
                return functools.partial(_connect_signature_hook, method=method)
        return None

    def get_method_hook(
        self, fullname: str
    ) -> Optional[Callable[[MethodContext], Type]]:
        if fullname == f"{SIGNAL_INSTANCE}.__getitem__":
            return _getitem_hook
        return None


def plugin(version: str) -> type[Plugin]:
    return TypesPySide6Plugin
