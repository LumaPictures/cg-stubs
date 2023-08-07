# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
from typing import ClassVar, Set, Tuple

class DoubleClickSizeGrip(PyQt5.QtWidgets.QSizeGrip):
    applyDefaultSize: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent) -> None: ...
    def mouseDoubleClickEvent(self, e): ...
