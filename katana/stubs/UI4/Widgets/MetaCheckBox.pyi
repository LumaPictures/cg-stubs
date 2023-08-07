# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
from typing import ClassVar, Set, Tuple

class MetaCheckBox(PyQt5.QtWidgets.QCheckBox):
    toggled: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, displayName, meta, parent) -> None: ...
    def _MetaCheckBox__toggled(self, on): ...
    def getMeta(self): ...
    def mouseMoveEvent(self, ev): ...
    def mousePressEvent(self, ev): ...
    def mouseReleaseEvent(self, ev): ...
