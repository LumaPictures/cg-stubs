"""Optional mypy plugin that makes ``QtCore.Signal(object)`` behave as ``typing.Any``.

``Signal(object)`` is a common PySide idiom for declaring a signal that emits an
arbitrary/complex value (Qt registers it as ``PyObject``), so its idiomatic
meaning is ``typing.Any`` rather than ``builtins.object``.  The distinction
matters to a type checker: a slot annotated with a specific type is not
compatible with an ``object`` argument (callables are contravariant in their
arguments), so without this plugin ``Signal(object).connect(slot)`` is an error
for any slot more specific than ``object``.

This cannot be expressed in the stubs alone: any ``Signal.__init__`` overload
that accepts ``type[object]`` also accepts every other ``type[X]``, and mypy
matches ``SignalInstance[tuple[X]]`` covariantly against
``SignalInstance[tuple[object]]``, so a stub-level special case would erase the
type checking of every other signal.  A plugin can instead rewrite the type at
the declaration site, which is precise: only arguments declared as ``object``
become ``Any``; all other arguments of the same signal remain strictly checked.

Usage (mypy configuration)::

    [tool.mypy]
    plugins = ["pyside6_stubs_mypy_plugin"]

The plugin also rewrites arguments declared as ``typing.Any`` (which is a real,
instantiable class at runtime since Python 3.11, and which PySide6 likewise
registers as ``PyObject``), since mypy otherwise treats the *value* ``Any``
nominally.
"""

from __future__ import annotations

from typing import Callable, Optional

from mypy.plugin import FunctionContext, Plugin
from mypy.types import (
    AnyType,
    Instance,
    TupleType,
    Type,
    TypeOfAny,
    get_proper_type,
)

SIGNAL = "PySide6.QtCore.Signal"

# Type arguments to Signal(...) that idiomatically mean "anything".
_ANY_CLASSES = frozenset({"builtins.object", "typing.Any"})


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


class PySide6StubsPlugin(Plugin):
    def get_function_hook(
        self, fullname: str
    ) -> Optional[Callable[[FunctionContext], Type]]:
        if fullname == SIGNAL:
            return _signal_hook
        return None


def plugin(version: str) -> type[Plugin]:
    return PySide6StubsPlugin
