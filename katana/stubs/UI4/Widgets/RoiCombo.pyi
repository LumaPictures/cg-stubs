# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import PyUtilModule.RenderManager as RenderManager
import Utils as Utils
from QT4Widgets.PopdownLabel import PopdownLabel as PopdownLabel
from typing import ClassVar, Set, Tuple

class RoiCombo(PopdownLabel):
    roiVisibilityChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent) -> None: ...
    def _RoiCombo__renderManager_roiChanged_callback(self, *args, **kwargs): ...
    def buildMenu(self, menu: PyQt5.QtWidgets.QMenu): ...
    def getRoiVisible(self): ...
    def setRoiVisible(self, isVisible): ...
    def updateState(self): ...
