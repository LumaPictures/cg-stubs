from __future__ import absolute_import, print_function

from typing import Any

from PySide6 import QtCore, QtWidgets


class MainDialog(QtWidgets.QDialog):
    # The types of signals 1-3 are inferred based on type arguments
    signal1 = QtCore.Signal()
    signal2 = QtCore.Signal(int)
    signal3 = QtCore.Signal(int, str)
    # Signals support multiple signatures when passed as tuples, but this can't be described
    # using type annotations.
    # For simple cases where both signatures have a single arg, we can simply use a union for the type.
    # WARNING: QtCore.Signal is not subscriptable at runtime, so you must create a forward reference
    # (e.g. wrap it in quotes)
    signal4: "QtCore.Signal[int | str]" = QtCore.Signal((int,), (str,))
    # For more complicated multi-signals, we can ignore the error which effectively disables checking for this signal.
    # To regain type safety, use indexing when accessing the signal (see examples below).
    signal5 = QtCore.Signal((int, int), (str, str))  # type: ignore[var-annotated]
    signal6 = QtCore.Signal((int,), (int, int))  # type: ignore[var-annotated]

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
        self.signal1.connect(self.slot1)
        # All remaining slots require an argument
        self.signal1.connect(self.slot2a)  # type: ignore[arg-type]
        self.signal1.connect(self.slot2b)  # type: ignore[arg-type]
        self.signal1.connect(self.slot2c)  # type: ignore[arg-type]
        self.signal1.connect(self.slot3)  # type: ignore[arg-type]
        self.signal1.connect(self.slot4)  # type: ignore[arg-type]

        self.signal2.connect(self.slot1)  # type: ignore[arg-type]
        self.signal2.connect(self.slot2a)
        # Argument has the wrong type,
        # but Qt happens to be able to coerce an int to str.
        self.signal2.connect(self.slot2b)  # type: ignore[arg-type]
        self.signal2.connect(self.slot2c)
        # Is missing a required argument
        self.signal2.connect(self.slot3)  # type: ignore[arg-type]
        self.signal2.connect(self.slot4)

        self.signal3.connect(self.slot1)  # type: ignore[arg-type]
        self.signal3.connect(self.slot2a)  # type: ignore[arg-type]
        self.signal3.connect(self.slot2b)  # type: ignore[arg-type]
        self.signal3.connect(self.slot2c)  # type: ignore[arg-type]
        self.signal3.connect(self.slot3)
        self.signal3.connect(self.slot4)

        self.signal4.connect(self.slot1)  # type: ignore[arg-type]
        self.signal4.connect(self.slot2a)  # type: ignore[arg-type]
        # Argument 1 has the wrong type,
        # but Qt happens to be able to coerce an int to str.
        self.signal4.connect(self.slot2b)  # type: ignore[arg-type]
        self.signal4.connect(self.slot2c)
        # Is missing a required argument
        self.signal4.connect(self.slot3)  # type: ignore[arg-type]
        self.signal4.connect(self.slot4)

        # signal5 does not do any type checking because it represents multiple signatures
        self.signal5.connect(self.slot1)
        # Argument 1 might have the wrong type
        # depending on the Signal signature.
        self.signal5.connect(self.slot2a)
        # Argument 1 might have the wrong type
        # depending on the Signal signature.
        self.signal5.connect(self.slot2b)
        self.signal5.connect(self.slot2c)
        self.signal5.connect(self.slot3)
        self.signal5.connect(self.slot4)

        # we can use indexing to check a particular signature
        self.signal5[int, int].connect(self.slot1)  # type: ignore[arg-type]
        # Argument 1 might have the wrong type
        # depending on the Signal signature.
        self.signal5[int, int].connect(self.slot2a)  # type: ignore[arg-type]
        # Argument 1 might have the wrong type
        # depending on the Signal signature.
        self.signal5[int, int].connect(self.slot2b)  # type: ignore[arg-type]
        self.signal5[int, int].connect(self.slot2c)  # type: ignore[arg-type]
        self.signal5[int, int].connect(self.slot3)
        self.signal5[int, int].connect(self.slot4)

        self.signal5[str, str].connect(self.slot1)  # type: ignore[arg-type]
        # Argument 1 might have the wrong type
        # depending on the Signal signature.
        self.signal5[str, str].connect(self.slot2a)  # type: ignore[arg-type]
        # Argument 1 might have the wrong type
        # depending on the Signal signature.
        self.signal5[str, str].connect(self.slot2b)  # type: ignore[arg-type]
        self.signal5[str, str].connect(self.slot2c)  # type: ignore[arg-type]
        self.signal5[str, str].connect(self.slot3)
        self.signal5[str, str].connect(self.slot4)

        # type checking is disabled for signal6
        self.signal6.connect(self.slot1)
        self.signal6.connect(self.slot2a)
        # Argument 1 has the wrong type,
        # but Qt happens to be able to coerce an int to str.
        self.signal6.connect(self.slot2b)
        self.signal6.connect(self.slot2c)
        self.signal6.connect(self.slot3)
        self.signal6.connect(self.slot4)

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
        self.signal5.emit(1, 2)
        self.signal5.emit("bad")  # not checked, because Signal/SignalInstance can't represent multiple signatures
        self.signal5[int, int].emit(3, 4)
        self.signal5[int, int].emit("one", "two")  # type: ignore[arg-type]
        self.signal5[str, str].emit("one", "two")

    @QtCore.Slot()
    def _emitSignal6(self) -> None:
        self._text_edit.clear()
        self.signal6.emit(1)
        self.signal6[int].emit(2)
        self.signal6[int, int].emit(3, 4)

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
