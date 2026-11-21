from collections.abc import Callable, Iterable, Mapping
from typing import Any, ClassVar

import hou
from PySide6 import QtCore, QtGui, QtWidgets

the_scaled_icon_size: int
the_icon_size: int
ShiftKeyBit: int
AltKeyBit: int
ControlKeyBit: int
CommandKeyBit: int
ConflictBit: int
ConflictAncestorBit: int
ConflictDescendantBit: int

def get_linenumber() -> str: ...
def hom_color_to_hex(hom_color: hou.Color) -> str: ...

class LinkLabel(QtWidgets.QLabel):
    def __init__(self, text: str, callback: Callable[[str], object] | None = ..., **kwargs: Any) -> None: ...
    def mousePressEvent(self, other: QtGui.QMouseEvent) -> None: ...

class ConflictWarning(QtWidgets.QWidget):
    context: str
    action: str
    label: str
    key: str
    dir: str | None
    callback: Callable[[str], object]
    def __init__(
        self,
        context: str,
        action: str,
        label: str,
        key: str,
        dir: str | None,
        callback: Callable[[str], object],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...

class AssignmentInfo(QtWidgets.QWidget):
    context: str
    action: str
    label: str
    key: str
    dir: str | None
    callback: Callable[[str], object]
    def __init__(
        self,
        context: str,
        action: str,
        label: str,
        key: str,
        dir: str | None,
        callback: Callable[[str], object],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...

class NoAssignmentInfo(QtWidgets.QWidget):
    context: str
    action: str
    label: str
    key: str
    callback: Callable[[str], object]
    def __init__(
        self,
        context: str,
        action: str,
        label: str,
        key: str,
        callback: Callable[[str], object],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...

def make_conflict_list(rows: Iterable[QtWidgets.QWidget]) -> QtWidgets.QScrollArea: ...

class RawKeyCapture(QtWidgets.QLineEdit):
    cancel: ClassVar[QtCore.Signal]
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...

class KeyCaptureWidget(QtWidgets.QFrame):
    accept: ClassVar[QtCore.Signal]
    changed: ClassVar[QtCore.Signal]
    cancel: ClassVar[QtCore.Signal]
    special_items: list[str]
    capturekey: RawKeyCapture
    specialsbutton: QtWidgets.QToolButton
    specialsmenu: QtWidgets.QMenu
    def setText(self, text: str) -> None: ...
    def text(self) -> str: ...
    def __init__(self, accept_label: str, parent: QtWidgets.QWidget | None = ...) -> None: ...

keyalias: dict[str, str]

class VirtualKeyBoardFrame(QtWidgets.QFrame):
    prop_lavoutSpacing: int | str
    prop_lavoutMargins: int | str
    layoutSpacing: ClassVar[QtCore.Property]
    layoutMargins: ClassVar[QtCore.Property]
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def readLayoutSpacing(self) -> int | str: ...
    def readLayoutMargins(self) -> int | str: ...
    def setLayoutSpacing(self, val: int | str) -> None: ...
    def setLayoutMargins(self, val: int | str) -> None: ...

class VirtualKeyCapWidget(QtWidgets.QPushButton):
    label: str
    label_shift: str
    prop_conflictItemFormat: str
    conflictItemFormat: ClassVar[QtCore.Property]
    def __init__(self, keyname: str, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def readConflictItemFormat(self) -> str: ...
    def setConflictItemFormat(self, format: str) -> None: ...
    def getLabel(self, keyname: str) -> str: ...
    def getLabels(self, keyname: str) -> tuple[str, str]: ...
    def setProperties(self, properties: Mapping[str, object]) -> bool: ...
    def setModifiers(self, modifiers: int) -> None: ...

def toKeyDisplayString(keystr: str) -> str: ...
def fromKeyDisplayString(keystr: str) -> str: ...
