# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import QT4FormWidgets as QT4FormWidgets
from typing import ClassVar

class ColorTextValidator(PyQt5.QtGui.QValidator):
    def __init__(self, *args): ...
    def parseColor(self, text): ...
    def validate(self, inStr, qPos): ...

class ColorTextWidget(QT4FormWidgets.InputWidgets.InputLineEdit):
    valueChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent): ...
    def _ColorTextWidget__updateText(self): ...
    def _ColorTextWidget__valueChangedCB(self): ...
    def getColorText(self, color): ...
    def keyPressEvent(self, event): ...
    def setColor(self, color): ...

def ColorFromText(text): ...
def ColorToText(color, roundDigits: int = ...): ...