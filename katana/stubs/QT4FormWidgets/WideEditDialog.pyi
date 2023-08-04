# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class WideEditDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, policy, factory) -> None: ...
    def showEvent(self, event: PyQt5.QtGui.QShowEvent): ...
    def sizeHint(self): ...
