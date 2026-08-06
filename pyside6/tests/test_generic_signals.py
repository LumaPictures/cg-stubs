from __future__ import absolute_import, print_function

from PySide6 import QtCore, QtWidgets


class MainDialog(QtWidgets.QDialog):
    # The types of these signals are inferred from the constructor arguments, so
    # no explicit annotations are required.  Signal and SignalInstance are
    # parametrized by one or more signatures, where each signature is a tuple of
    # argument types.
    signal1 = QtCore.Signal()
    signal2 = QtCore.Signal(int)
    signal3 = QtCore.Signal(int, str)
    # Signals support multiple signatures when passed as tuples.  Inference is
    # supported for up to two signatures with up to two arguments each; other
    # configurations must be annotated manually, e.g.
    #   signal7: "QtCore.Signal[tuple[int, int, int], tuple[str]]" = QtCore.Signal(
    #       (int, int, int), (str,)
    #   )
    # WARNING: QtCore.Signal is not subscriptable at runtime, so manual
    # annotations must be forward references (wrapped in quotes).
    signal4 = QtCore.Signal((int,), (str,))
    signal5 = QtCore.Signal((int, int), (str, str))
    signal6 = QtCore.Signal((int,), (int, int))

    def __init__(self) -> None:
        super().__init__()

        self._connect_signals()

        main_layout = QtWidgets.QVBoxLayout()

        layout = QtWidgets.QGridLayout()
        button = QtWidgets.QPushButton("()")
        button.pressed.connect(self._emitSignal1)
        layout.addWidget(button, 0, 0)

        button = QtWidgets.QPushButton("(int)")
        button.clicked.connect(self._emitSignal2)
        layout.addWidget(button, 0, 1)

        button = QtWidgets.QPushButton("(int, str)")
        button.clicked.connect(self._emitSignal3)
        layout.addWidget(button, 0, 2)

        button = QtWidgets.QPushButton("((int,), (str,))")
        button.clicked.connect(self._emitSignal4)
        layout.addWidget(button, 1, 0)

        button = QtWidgets.QPushButton("((int, int), (str, str))")
        button.clicked.connect(self._emitSignal5)
        layout.addWidget(button, 1, 1)

        button = QtWidgets.QPushButton("((int,), (int, int))")
        button.clicked.connect(self._emitSignal6)
        layout.addWidget(button, 1, 2)
        main_layout.addLayout(layout)

        self._text_edit = QtWidgets.QPlainTextEdit()
        main_layout.addWidget(self._text_edit)

        button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.StandardButton.Ok
            | QtWidgets.QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        main_layout.addWidget(button_box)

        self.setLayout(main_layout)

    def _connect_signals(self) -> None:
        # Qt allows connecting slots that accept fewer arguments than the signal
        # emits, and the stubs support that pattern for up to the first three
        # arguments.  Signals with multiple signatures are checked against their
        # default (first) signature.
        self.signal1.connect(self.slot1)
        # All remaining slots require an argument
        self.signal1.connect(self.slot2a)  # type: ignore[arg-type]
        self.signal1.connect(self.slot2b)  # type: ignore[arg-type]
        self.signal1.connect(self.slot2c)  # type: ignore[arg-type]
        self.signal1.connect(self.slot3)  # type: ignore[arg-type]
        self.signal1.connect(self.slot4)  # type: ignore[arg-type]

        self.signal2.connect(self.slot1)
        self.signal2.connect(self.slot2a)
        # Argument has the wrong type.
        # Qt happens to be able to coerce an int to str, but we want users to be explicit.
        self.signal2.connect(self.slot2b)  # type: ignore[call-overload]
        self.signal2.connect(self.slot2c)
        # Is missing a required argument
        self.signal2.connect(self.slot3)  # type: ignore[call-overload]
        self.signal2.connect(self.slot4)

        self.signal3.connect(self.slot1)
        self.signal3.connect(self.slot2a)
        # Argument 1 has the wrong type.
        # Qt happens to be able to coerce an int to str, but we want users to be explicit.
        self.signal3.connect(self.slot2b)  # type: ignore[call-overload]
        self.signal3.connect(self.slot2c)
        self.signal3.connect(self.slot3)
        self.signal3.connect(self.slot4)

        self.signal4.connect(self.slot1)
        self.signal4.connect(self.slot2a)
        # Argument 1 has the wrong type.
        # Qt happens to be able to coerce an int to str, but we want users to be explicit.
        self.signal4.connect(self.slot2b)  # type: ignore[call-overload]
        self.signal4.connect(self.slot2c)
        # Is missing a required argument
        self.signal4.connect(self.slot3)  # type: ignore[call-overload]
        self.signal4.connect(self.slot4)

        self.signal5.connect(self.slot1)
        # Argument 1 has the correct type in the default Signal signature.
        self.signal5.connect(self.slot2a)
        # Argument 1 has the wrong type in the default Signal signature.
        self.signal5.connect(self.slot2b)  # type: ignore[call-overload]
        self.signal5.connect(self.slot2c)
        self.signal5.connect(self.slot3)
        self.signal5.connect(self.slot4)

        # We can use indexing to check against a specific signature instead of
        # the default one.
        self.signal5[int, int].connect(self.slot1)
        self.signal5[int, int].connect(self.slot2a)
        # Argument 1 has the wrong type.
        self.signal5[int, int].connect(self.slot2b)  # type: ignore[call-overload]
        self.signal5[int, int].connect(self.slot2c)
        self.signal5[int, int].connect(self.slot3)
        self.signal5[int, int].connect(self.slot4)

        self.signal5[str, str].connect(self.slot1)
        # Argument 1 has the wrong type.
        self.signal5[str, str].connect(self.slot2a)  # type: ignore[call-overload]
        self.signal5[str, str].connect(self.slot2b)
        self.signal5[str, str].connect(self.slot2c)
        self.signal5[str, str].connect(self.slot3)
        self.signal5[str, str].connect(self.slot4)

        self.signal6.connect(self.slot1)
        self.signal6.connect(self.slot2a)
        # Argument 1 has the wrong type.
        # Qt happens to be able to coerce an int to str, but we want users to be explicit.
        self.signal6.connect(self.slot2b)  # type: ignore[call-overload]
        self.signal6.connect(self.slot2c)
        # The default Signal signature is missing an argument.
        self.signal6.connect(self.slot3)  # type: ignore[call-overload]
        self.signal6.connect(self.slot4)

        # Signals can be connected to other signals: emitting the first signal
        # emits the connected signal with the same arguments, so the connected
        # signal's arguments are checked like a slot's.
        self.signal2.connect(self.signal1)  # receiving signal takes fewer args
        self.signal3.connect(self.signal2)  # prefix of the emitted args
        self.signal5[str, str].connect(self.signal4[str])
        # The receiving signal requires more arguments than are emitted.
        self.signal1.connect(self.signal2)  # type: ignore[arg-type]
        self.signal2.connect(self.signal3)  # type: ignore[arg-type]

    @QtCore.Slot()
    def _emitSignal1(self) -> None:
        self._text_edit.clear()
        self.signal1.emit()

    @QtCore.Slot()
    def _emitSignal2(self) -> None:
        self._text_edit.clear()
        self.signal2.emit(1)

    @QtCore.Slot()
    def _emitSignal3(self) -> None:
        self._text_edit.clear()
        self.signal3.emit(1, "one")

    @QtCore.Slot()
    def _emitSignal4(self) -> None:
        self._text_edit.clear()
        self.signal4.emit(1)
        self.signal4[int].emit(2)
        self.signal4[str].emit("one")

    @QtCore.Slot()
    def _emitSignal5(self) -> None:
        self._text_edit.clear()
        # emit is checked against the default (first) signature
        self.signal5.emit(1, 2)
        # This matches neither of signal5's signatures.  It is flagged because
        # emit is checked against the default signature; a bad emit that
        # matches a non-default signature in argument count would not be.
        self.signal5.emit("bad")  # type: ignore[arg-type, call-arg]
        self.signal5[int, int].emit(3, 4)
        self.signal5[int, int].emit("one", "two")  # type: ignore[arg-type]
        self.signal5[str, str].emit("one", "two")

    @QtCore.Slot()
    def _emitSignal6(self) -> None:
        self._text_edit.clear()
        self.signal6.emit(1)
        self.signal6[int].emit(2)
        self.signal6[int, int].emit(3, 4)

    def _invalid(self) -> None:
        # Incorrect usage of __getitem__ is flagged when the index can be
        # validated against the signal's first or last signature.
        # signal1 has no arguments
        self.signal1[int]  # type: ignore[index]
        self.signal1[str]  # type: ignore[index]
        # Unable to get mypy to flag this as an issue: indexes with multiple
        # types that match no signature fall through to an unchecked catchall.
        self.signal1[int, str]
        # signal2 has an `int` type
        self.signal2[str]  # type: ignore[index]
        # signal3 has 2 arguments
        self.signal3[int]  # type: ignore[call-overload]
        # signal4 accepts int or str
        self.signal4[float].emit(4.0)  # type: ignore[arg-type, index]
        self.signal5[int]  # type: ignore[call-overload]
        self.signal5[str]  # type: ignore[call-overload]
        # Unable to get mypy to flag this as an issue (see signal1 above).
        self.signal5[int, str]

    @QtCore.Slot()
    def slot1(self) -> None:
        self._text_edit.insertPlainText("slot1: ()\n")

    @QtCore.Slot()
    def slot2a(self, arg1: int) -> None:
        self._text_edit.insertPlainText(f"slot2a: ({arg1!r})\n")

    @QtCore.Slot()
    def slot2b(self, arg1: str) -> None:
        self._text_edit.insertPlainText(f"slot2b: ({arg1!r})\n")

    @QtCore.Slot(int)
    @QtCore.Slot(str)
    def slot2c(self, arg1: int | str) -> None:
        self._text_edit.insertPlainText(f"slot2c: ({arg1!r})\n")

    @QtCore.Slot()
    def slot3(self, arg1: int | str, arg2: int | str) -> None:
        self._text_edit.insertPlainText(f"slot3: ({arg1!r}, {arg2!r})\n")

    @QtCore.Slot()
    def slot4(self, arg1: int | str, arg2: int | str | None = None) -> None:
        self._text_edit.insertPlainText(f"slot4: ({arg1!r}, {arg2!r})\n")
