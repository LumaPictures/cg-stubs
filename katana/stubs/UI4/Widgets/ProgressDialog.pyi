# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
from _typeshed import Incomplete
from typing import Set, Tuple

class ProgressDialog(PyQt5.QtWidgets.QProgressDialog):
    def __init__(self, parent, titleText: Incomplete | None = ..., labelText: Incomplete | None = ..., minimumValue: int = ..., maximumValue: int = ..., interval: int = ..., minimumDuration: int = ...) -> None: ...
    def showEvent(self, event): ...
    def update(self, value: int) -> bool: ...
