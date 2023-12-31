# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import PySide6.QtWidgets
from pxr.Usdviewq.common import BoldenLabelText as BoldenLabelText, ColorizeLabelText as ColorizeLabelText, ItalicizeLabelText as ItalicizeLabelText, UIPrimTypeColors as UIPrimTypeColors
from pxr.Usdviewq.primLegendUI import Ui_PrimLegend as Ui_PrimLegend
from typing import ClassVar

class PrimLegend(PySide6.QtWidgets.QWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent) -> None: ...
    def GetHeight(self): ...
    def GetResetHeight(self): ...
    def IsMinimized(self): ...
    def ToggleMinimized(self): ...
