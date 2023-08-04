# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import ClassVar, Set, Tuple

class PopupMenuOption(PyQt5.QtWidgets.QFrame):
    class DialogRequestButton(PyQt5.QtWidgets.QLabel):
        dialogRequest: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
        def __init__(self, *args) -> None: ...
        def _DialogRequestButton__emit(self): ...
        def enterEvent(self, ev): ...
        def leaveEvent(self, ev): ...
        def mousePressEvent(self, ev): ...
        def mouseReleaseEvent(self, ev): ...

    class MenuLabel(PyQt5.QtWidgets.QLabel):
        activated: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
        def __init__(self, *args) -> None: ...
        def _MenuLabel__emit(self): ...
        def enterEvent(self, ev): ...
        def leaveEvent(self, ev): ...
        def mousePressEvent(self, ev): ...
        def mouseReleaseEvent(self, ev): ...
    def __init__(self, text, *args) -> None: ...
    def closePopupMenu(self): ...
    def enterEvent(self, ev): ...
    def leaveEvent(self, ev): ...
