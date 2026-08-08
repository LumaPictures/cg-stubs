"""Type-checking assertions for the pyside6_stubs_mypy_plugin mypy plugin.

Like test_generic_signals.py, this file exists to be type-checked, not
executed: a bare statement asserts that mypy reports no error, and a
``# type: ignore[code]`` comment asserts that mypy reports exactly that error
(the config enables strict mode, so a stale ignore also fails).

Unlike test_generic_signals.py, this file is NOT checked by the project's
plain mypy configuration (see the exclude in pyproject.toml): it is checked by
tests/test_signal_object_plugin.py using tests/mypy-plugin.ini, which enables
the plugin.  The plugin rewrites `object` (and `typing.Any`) arguments in
``Signal(...)`` declarations to mean ``typing.Any``, so the "no error"
assertions below hold only when the plugin is active.
"""

from __future__ import absolute_import, print_function

import typing

from PySide6 import QtCore


class CustomData:
    """Stand-in for a complex type emitted through a Signal(object) signal."""


class ObjectSignals(QtCore.QObject):
    # Signal(object) is the idiomatic way to declare a signal that emits an
    # arbitrary value (Qt registers it as PyObject), so the plugin makes it
    # infer as Signal[tuple[Any]] instead of Signal[tuple[object]].
    signal_obj = QtCore.Signal(object)
    # Only the `object` argument becomes Any: Signal[tuple[int, Any]].
    signal_int_obj = QtCore.Signal(int, object)
    # `typing.Any` is a real, instantiable class at runtime since Python 3.11
    # and PySide6 likewise registers it as PyObject, so it is treated the same
    # way.  (Without the plugin, mypy treats the *value* `Any` as the nominal
    # class `typing.Any`, which no slot argument type is compatible with.)
    signal_any = QtCore.Signal(typing.Any)
    # `object` is rewritten in every signature of a multi-signature signal.
    signal_multi = QtCore.Signal((object,), (int,))
    # Control: signals without `object` are untouched by the plugin and remain
    # strictly checked.
    signal_int = QtCore.Signal(int)

    def _connect_signals(self) -> None:
        # An object-declared signal behaves as Any: slots with any argument
        # type are accepted, as are slots that take fewer arguments.
        self.signal_obj.connect(self.slot_none)
        self.signal_obj.connect(self.slot_data)
        self.signal_obj.connect(self.slot_int)
        self.signal_obj.disconnect(self.slot_data)
        self.signal_any.connect(self.slot_data)
        self.signal_multi.connect(self.slot_data)

        # Only signal_int_obj's `object` argument becomes Any; its `int`
        # argument is still strictly checked.
        self.signal_int_obj.connect(self.slot_int_data)
        self.signal_int_obj.connect(self.slot_str_data)  # type: ignore[call-overload]

        # The plugin does not affect other signals: connecting a slot with a
        # wrong argument type is still an error.
        self.signal_int.connect(self.slot_int)
        self.signal_int.connect(self.slot_data)  # type: ignore[call-overload]

    def _emit_signals(self) -> None:
        # object-declared arguments accept any value on emit
        self.signal_obj.emit(CustomData())
        self.signal_obj.emit(1)
        self.signal_any.emit(CustomData())
        self.signal_int_obj.emit(1, CustomData())
        self.signal_int_obj.emit("one", CustomData())  # type: ignore[arg-type]
        self.signal_int.emit(1)
        self.signal_int.emit(CustomData())  # type: ignore[arg-type]

    def slot_none(self) -> None:
        pass

    def slot_data(self, arg1: CustomData) -> None:
        pass

    def slot_int(self, arg1: int) -> None:
        pass

    def slot_int_data(self, arg1: int, arg2: CustomData) -> None:
        pass

    def slot_str_data(self, arg1: str, arg2: CustomData) -> None:
        pass
