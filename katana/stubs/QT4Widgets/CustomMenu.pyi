# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QtCore as QtCore
import QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class CustomMenu(PyQt5.QtWidgets.QMenu):
    def __init__(self, parent): ...
    def actionEvent(self, event: QtGui.QActionEvent): ...
    def sizeHint(self) -> QtCore.QSize: ...
