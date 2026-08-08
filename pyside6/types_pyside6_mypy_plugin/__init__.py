"""Optional mypy plugin that improves type checking of PySide6 signals.

The plugin provides two features that cannot be expressed in the stubs alone:

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

Unsubscripted ``connect``/``emit`` on a multi-signature signal use only the
default (first) signature at runtime -- PySide does not dispatch across
signatures by argument types -- and the stubs already check them against the
first signature, so the plugin leaves them alone.

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
import os
from typing import Any, Callable, Optional

from mypy import errorcodes
from mypy.nodes import ARG_POS
from mypy.options import Options
from mypy.plugin import (
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

# Type arguments to Signal(...) that idiomatically mean "anything".
_ANY_CLASSES = frozenset({"builtins.object", "typing.Any"})

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
            item = proper_element.items[0] if isinstance(proper_element, Overloaded) else proper_element
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
        return None

    def get_method_hook(
        self, fullname: str
    ) -> Optional[Callable[[MethodContext], Type]]:
        if fullname == f"{SIGNAL_INSTANCE}.__getitem__":
            return _getitem_hook
        return None


def plugin(version: str) -> type[Plugin]:
    return TypesPySide6Plugin
