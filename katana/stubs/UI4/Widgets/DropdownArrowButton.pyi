# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class DropdownArrowButton(PyQt5.QtWidgets.QPushButton):
    def __init__(self, height) -> None: ...
    def enterEvent(self, event: PyQt5.QtCore.QEvent): ...
    def leaveEvent(self, event: PyQt5.QtCore.QEvent): ...
    def paintEvent(self, event: PyQt5.QtGui.QPaintEvent): ...
    def setDropdownEnabled(self, enabled: bool): ...
    def setRectangularFixedSize(self, height: int | None): ...
