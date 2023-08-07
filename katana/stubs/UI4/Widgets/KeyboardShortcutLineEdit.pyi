# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class KeyboardShortcutLineEdit(PyQt5.QtWidgets.QLineEdit):
    def keyPressEvent(self, keyEvent: PyQt5.QtGui.QKeyEvent): ...
