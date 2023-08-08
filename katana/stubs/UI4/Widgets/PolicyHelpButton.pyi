# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
from ResourceFiles.IconManager import ResourceManager as ResourceManager
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from typing import ClassVar, Set, Tuple

class PolicyHelpButton(ToolbarButton):
    _ErrorPixmap: ClassVar[None] = ...
    _ErrorRolloverPixmap: ClassVar[None] = ...
    _NormalPixmap: ClassVar[None] = ...
    _RolloverPixmap: ClassVar[None] = ...
    _WarningPixmap: ClassVar[None] = ...
    _WarningRolloverPixmap: ClassVar[None] = ...
    aboutToShow: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent: PyQt5.QtWidgets.QWidget) -> None: ...
    def _PolicyHelpButton__on_mousePressEvent(self, event): ...
    def getHelpText(self): ...
    def getHelpTitle(self): ...
    def getHelpType(self): ...
    def getHelpURL(self): ...
    def isHelpAvailable(self): ...