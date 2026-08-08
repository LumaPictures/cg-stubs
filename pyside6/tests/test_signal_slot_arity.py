"""Check which slot signatures `SignalInstance.connect` accepts.

Qt lets a slot take *fewer* arguments than the signal emits, and a slot whose
extra parameters all have defaults is callable with fewer arguments too.  Both
must be accepted.  A slot with extra *required* parameters can never be called
by the signal and must be rejected.

The `# type: ignore[...]` comments double as assertions: `warn_unused_ignores`
is enabled, so an ignore on a line that does *not* error is itself an error.
"""

from PySide6 import QtCore


class Emitter(QtCore.QObject):
    no_args = QtCore.Signal()
    one_arg = QtCore.Signal(str)
    two_args = QtCore.Signal(str, int)
    # `object` payloads carry no useful type, so they must be annotated to be
    # checked.  QtCore.Signal is not subscriptable at runtime, hence the quotes.
    payload: "QtCore.Signal[tuple[list[str]]]" = QtCore.Signal(object)


def slot_none() -> None: ...
def slot_str(a: str) -> None: ...
def slot_str_int(a: str, b: int) -> None: ...


# extra parameters, all defaulted -> callable with fewer args
def slot_str_default(a: str, rewind: bool = True) -> None: ...
def slot_str_two_defaults(a: str, b: int = 0, c: str = "") -> None: ...
def slot_all_defaults(a: str = "", b: int = 0) -> None: ...


# extra parameters that are required -> never callable by the signal
def slot_str_required(a: str, rewind: bool) -> None: ...


# keyword-only parameters are never passed positionally by a signal
def slot_str_kwonly_default(a: str, *, rewind: bool = True) -> None: ...
def slot_str_kwonly_required(a: str, *, rewind: bool) -> None: ...


def test_slot_arity() -> None:
    e = Emitter()

    # --- exact arity ------------------------------------------------------
    e.no_args.connect(slot_none)
    e.one_arg.connect(slot_str)
    e.two_args.connect(slot_str_int)

    # --- fewer arguments than the signal emits (allowed by Qt) ------------
    e.one_arg.connect(slot_none)
    e.two_args.connect(slot_none)
    e.two_args.connect(slot_str)

    # --- extra arguments, all defaulted (the `set_sequence` case) ---------
    e.one_arg.connect(slot_str_default)
    e.one_arg.connect(slot_str_two_defaults)
    e.one_arg.connect(slot_all_defaults)
    e.no_args.connect(slot_all_defaults)
    e.payload.connect(slot_payload_default)

    # --- extra *required* arguments: rejected -----------------------------
    e.one_arg.connect(slot_str_required)  # type: ignore[call-overload]
    # `connect` on a no-argument signal is not overloaded, so this reports
    # `arg-type` rather than `call-overload`.
    e.no_args.connect(slot_str)  # type: ignore[arg-type]

    # --- keyword-only parameters ------------------------------------------
    # A defaulted keyword-only parameter is fine: the signal simply never
    # passes it.  A required one can never be supplied, so it must be rejected.
    e.one_arg.connect(slot_str_kwonly_default)
    e.one_arg.connect(slot_str_kwonly_required)  # type: ignore[call-overload]

    # --- wrong argument type is still caught ------------------------------
    e.one_arg.connect(slot_wrong_type)  # type: ignore[call-overload]


def slot_payload_default(seq: list[str], rewind: bool = True) -> None: ...
def slot_wrong_type(a: int) -> None: ...


def test_bound_method_slot_with_defaults() -> None:
    """The same rules apply to bound methods, which is how slots are usually written."""

    class Receiver(QtCore.QObject):
        def exact(self, a: str) -> None: ...
        def defaulted(self, a: str, rewind: bool = True) -> None: ...
        def required(self, a: str, rewind: bool) -> None: ...

    e = Emitter()
    r = Receiver()

    e.one_arg.connect(r.exact)
    e.one_arg.connect(r.defaulted)
    e.one_arg.connect(r.required)  # type: ignore[call-overload]


def test_lambda_slot() -> None:
    e = Emitter()

    e.one_arg.connect(lambda a: None)
    e.one_arg.connect(lambda: None)
    e.one_arg.connect(lambda a, b=1: None)
    e.one_arg.connect(lambda a, b: None)  # type: ignore[call-overload]
