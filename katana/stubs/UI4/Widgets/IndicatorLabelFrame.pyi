# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import KatanaResources as KatanaResources
import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import Utils as Utils
from UI4.Widgets.IconLabelFrame import IconLabelFrame as IconLabelFrame
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class IndicatorLabelFrame(IconLabelFrame):
    _IndicatorLabelFrame__pixmaps: ClassVar[dict] = ...
    def __init__(self, activeIconName: Incomplete | None = ..., inactiveIconName: Incomplete | None = ..., autoHide: bool = ..., parent: Incomplete | None = ..., flags: PyQt5.QtCore.Qt.WindowType = ...) -> None: ...
    def _IndicatorLabelFrame__getPixmap(self, iconName: str) -> PyQt5.QtGui.QPixmap: ...
    def _IndicatorLabelFrame__linkClicked(self, link: str): ...
    def setAutoHide(self, autoHide: bool): ...
    def updateDisplay(self, active: bool, message: str = ..., nodeNames: Incomplete | None = ...): ...
