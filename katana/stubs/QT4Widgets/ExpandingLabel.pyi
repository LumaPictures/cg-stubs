# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from _typeshed import Incomplete
from typing import Set, Tuple

class ExpandingLabel(PyQt5.QtWidgets.QTextEdit):
    def __init__(self, *args) -> None: ...
    def _rightAlign(self): ...
    def minimumSizeHint(self): ...
    def resizeEvent(self, resizeEvent): ...
    def setText(self, qstring, color: Incomplete | None = ...): ...
    def sizeHint(self): ...
    def sizePolicy(self): ...
