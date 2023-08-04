# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from _typeshed import Incomplete
from typing import Set, Tuple

class FixableBoxLayout(PyQt5.QtWidgets.QBoxLayout):
    def __init__(self, orient: PyQt5.QtWidgets.QBoxLayout.Direction = ..., parent: Incomplete | None = ...) -> None: ...
    def setFixedWidth(self, fixedWidth): ...
    def sizeHint(self): ...
