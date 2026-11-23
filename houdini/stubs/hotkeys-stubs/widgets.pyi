import hou
from collections.abc import Callable as Callable, Iterable, Mapping
from dbg import DbgPrinter
from hutil.PySide import QtCore, QtGui, QtWidgets
from typing import Any, Literal

dbg: DbgPrinter
the_scaled_icon_size: int
the_icon_size: int
the_new_ui_skin: bool | None
ShiftKeyBit: int
AltKeyBit: int
ControlKeyBit: int
CommandKeyBit: int
ConflictBit: int
ConflictAncestorBit: int
ConflictDescendantBit: int
keysequence_display_separator: str

def get_linenumber() -> str: ...
def hom_color_to_hex(hom_color: hou.Color) -> str: ...
def is_key_sequence_prefix(key_substring: str, key_sequence: str) -> bool:
    """
    `substring` must not be the same as `sequence`
    """

class LinkLabel(QtWidgets.QLabel):
    openExternalLinks: bool
    def __init__(self, text: str, callback: Callable[[str], object] | None = None, **kwargs: Any) -> None: ...
    def mousePressEvent(self, other: QtGui.QMouseEvent) -> None: ...

class ConflictWarning(QtWidgets.QWidget):
    context: str
    action: str
    label: str
    key: str
    location: Literal['above', 'below'] | None
    callback: Callable[[str], object]
    all_keys: tuple[str, ...]
    def __init__(self, context: str, action: str, label: str, key: str, location: Literal['above', 'below'] | None, callback: Callable[[str], object], *args: Any, **kwargs: Any) -> None: ...

class AssignmentInfo(QtWidgets.QWidget):
    context: str
    action: str
    label: str
    key: str
    location: Literal['self', 'above', 'below'] | None
    callback: Callable[[str], object]
    def __init__(self, context: str, action: str, label: str, key: str, location: Literal['self', 'above', 'below'] | None, callback: Callable[[str], object], *args: Any, **kwargs: Any) -> None: ...

class NoAssignmentInfo(QtWidgets.QWidget):
    context: str
    action: str | None
    label: str
    key: str
    callback: Callable[[str], object]
    def __init__(self, context: str, action: str | None, label: str, key: str, callback: Callable[[str], object], *args: Any, **kwargs: Any) -> None: ...

def make_conflict_list(rows: Iterable[QtWidgets.QWidget]) -> QtWidgets.QScrollArea: ...

class RawKeyCapture(QtWidgets.QLineEdit):
    accept: QtCore.Signal
    cancel: QtCore.Signal
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def isRecordKeySequence(self) -> bool: ...
    def startRecordKeySequence(self) -> None: ...
    def stopRecordKeySequence(self) -> None: ...
    def pressKey(self, keystring: str) -> None: ...

class KeyCaptureWidget(QtWidgets.QFrame):
    capturekey: RawKeyCapture
    specialsbutton: QtWidgets.QToolButton
    specialsmenu: QtWidgets.QMenu
    accept: QtCore.Signal
    changed: QtCore.Signal
    cancel: QtCore.Signal
    special_items: list[str]
    def __init__(self, allow_sequence: bool = True, parent: QtWidgets.QWidget | None = None) -> None: ...
    def pressKey(self, keystring: str) -> None: ...
    def setText(self, text: str) -> None: ...
    def text(self) -> str: ...
    def recordKeySequence(self) -> None: ...
    def stopRecordKeySequence(self) -> None: ...

keyalias: dict[str, str]

class VirtualKeyBoardFrame(QtWidgets.QFrame):
    prop_lavoutSpacing: int | str
    prop_lavoutMargins: int | str
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def readLayoutSpacing(self) -> int | str: ...
    def readLayoutMargins(self) -> int | str: ...
    def setLayoutSpacing(self, val: int | str) -> None: ...
    def setLayoutMargins(self, val: int | str) -> None: ...
    def setLayout(self, layout: QtWidgets.QLayout) -> None: ...
    layoutSpacing: QtCore.Property
    layoutMargins: QtCore.Property

class VirtualKeyCapWidget(QtWidgets.QPushButton):
    """A virtual-keyboard keycap.

    The classic skin is styled entirely by base.qss and uses the default
    QPushButton painting. The new (Pluto) skin does not load base.qss, so it
    reproduces the keycap look (and the sizing/font the stylesheet provided) by
    painting itself. The new-skin behaviour is gated behind _newUI() in the
    blocks marked below; when the classic skin and its base.qss block are
    eventually removed, drop those guards and make their bodies unconditional.
    """
    label: str
    label_shift: str
    prop_conflictItemFormat: str
    smalltype: bool
    def __init__(self, keyname: str, parent: QtWidgets.QWidget | None = None) -> None: ...
    def readConflictItemFormat(self) -> str: ...
    def setConflictItemFormat(self, new_format: str) -> None: ...
    conflictItemFormat: QtCore.Property
    def getLabel(self, keyname: str) -> str: ...
    def getLabels(self, keyname: str) -> tuple[str, str]: ...
    def setProperties(self, properties: Mapping[str, object]) -> bool: ...
    def setModifiers(self, modifiers: int) -> None: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...

def toKeyDisplayString(keystr: str) -> str: ...
def fromKeyDisplayString(keystr: str) -> str: ...
