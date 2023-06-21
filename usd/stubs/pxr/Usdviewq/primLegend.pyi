import PySide6.QtWidgets
from pxr.Usdviewq.common import BoldenLabelText as BoldenLabelText, ColorizeLabelText as ColorizeLabelText, ItalicizeLabelText as ItalicizeLabelText, UIPrimTypeColors as UIPrimTypeColors
from pxr.Usdviewq.primLegendUI import Ui_PrimLegend as Ui_PrimLegend
from typing import Callable, ClassVar

class PrimLegend(PySide6.QtWidgets.QWidget):
    __init__: ClassVar[Callable] = ...
    GetHeight: ClassVar[Callable] = ...
    GetResetHeight: ClassVar[Callable] = ...
    IsMinimized: ClassVar[Callable] = ...
    ToggleMinimized: ClassVar[Callable] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...