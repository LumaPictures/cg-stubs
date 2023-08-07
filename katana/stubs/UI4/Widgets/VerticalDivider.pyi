# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import Set, Tuple

class VerticalDivider(PyQt5.QtWidgets.QFrame):
    def __init__(self, *args) -> None: ...
    def paintEvent(self, event): ...
