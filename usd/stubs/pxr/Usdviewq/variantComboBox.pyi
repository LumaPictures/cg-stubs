# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import PySide6.QtWidgets
from pxr.Usdviewq.common import Timer as Timer
from typing import ClassVar

class VariantComboBox(PySide6.QtWidgets.QComboBox):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent, prim, variantSetName, mainWindow): ...
    def updateVariantSelection(self, index, timer): ...
