# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class CustomMenu(PyQt5.QtWidgets.QMenu):
    def __init__(self, parent) -> None: ...
    def actionEvent(self, event: PyQt5.QtGui.QActionEvent): ...
    def sizeHint(self) -> PyQt5.QtCore.QSize: ...
