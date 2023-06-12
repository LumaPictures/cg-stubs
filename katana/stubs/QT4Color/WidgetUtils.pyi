# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
from typing import ClassVar

class MiniLabelButton(PyQt5.QtWidgets.QLabel):
    clicked: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, text, parent): ...
    def mousePressEvent(self, _ev): ...
    def paintEvent(self, ev): ...

class StripedFrame(PyQt5.QtWidgets.QFrame):
    def paintEvent(self, ev): ...

def SetCompactWidgetWidth(w, padding: int = ...): ...