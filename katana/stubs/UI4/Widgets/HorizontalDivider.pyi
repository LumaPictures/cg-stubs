# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from _typeshed import Incomplete
from typing import Set, Tuple

class HorizontalDivider(PyQt5.QtWidgets.QFrame):
    def __init__(self, parent: Incomplete | None = ..., flags: int = ...) -> None: ...
