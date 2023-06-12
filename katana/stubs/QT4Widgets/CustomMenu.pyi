# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QtCore
import QtGui

class CustomMenu(PyQt5.QtWidgets.QMenu):
    def __init__(self, parent): ...
    def actionEvent(self, event: QtGui.QActionEvent): ...
    def sizeHint(self) -> QtCore.QSize: ...