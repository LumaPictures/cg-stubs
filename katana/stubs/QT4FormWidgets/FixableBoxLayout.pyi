# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtWidgets.QBoxLayout
from _typeshed import Incomplete

class FixableBoxLayout(PyQt5.QtWidgets.QBoxLayout):
    def __init__(self, orient: PyQt5.QtWidgets.QBoxLayout.Direction = ..., parent: Incomplete | None = ...): ...
    def setFixedWidth(self, fixedWidth): ...
    def sizeHint(self): ...