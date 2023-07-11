# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class WideEditDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, policy, factory): ...
    def showEvent(self, event: QtGui.QShowEvent): ...
    def sizeHint(self): ...
