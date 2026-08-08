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

2. ``emit()`` is checked against every declared signature.

   The stubs can only check ``emit`` (and ``__call__``: signals passed as
   callables dispatch like ``emit``) against a signal's default (first)
   signature, so emits through a non-default signature of a multi-signature
   signal are not properly checked.  The plugin replaces the signature of
   ``SignalInstance.emit`` with one overload per declared signature, so an
   emit matching any declared signature is accepted, and an emit matching
   none of them is an error.

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

from mypy.nodes import ARG_POS
from mypy.options import Options
from mypy.plugin import (
    FunctionContext,
    MethodSigContext,
    Plugin,
    ReportConfigContext,
)
from mypy.types import (
    AnyType,
    FunctionLike,
    Instance,
    Overloaded,
    TupleType,
    Type,
    TypeOfAny,
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


def _emit_signature_hook(ctx: MethodSigContext) -> FunctionLike:
    """Check ``emit``/``__call__`` against every declared signature.

    The stub signature can only check against the default (first) signature;
    this replaces it with one overload per signature of the receiver, e.g. for
    ``SignalInstance[tuple[int], tuple[str]]`` an emit matching either
    ``(int)`` or ``(str)`` is accepted.
    """
    receiver = get_proper_type(ctx.type)
    if not isinstance(receiver, Instance) or receiver.type.fullname != SIGNAL_INSTANCE:
        return ctx.default_signature
    items = []
    for sig in receiver.args:
        proper_sig = get_proper_type(sig)
        if not isinstance(proper_sig, TupleType):
            # unparametrized or irregular SignalInstance: leave the (fully
            # permissive) stub signature alone
            return ctx.default_signature
        items.append(
            ctx.default_signature.copy_modified(
                arg_types=list(proper_sig.items),
                arg_kinds=[ARG_POS] * len(proper_sig.items),
                arg_names=[None] * len(proper_sig.items),
            )
        )
    if not items:
        return ctx.default_signature
    if len(items) == 1:
        return items[0]
    return Overloaded(items)


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
        if fullname in (f"{SIGNAL_INSTANCE}.emit", f"{SIGNAL_INSTANCE}.__call__"):
            return _emit_signature_hook
        return None


def plugin(version: str) -> type[Plugin]:
    return TypesPySide6Plugin
