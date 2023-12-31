# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import PyQt5.QtGui
import QT4GLLayerStack as QT4GLLayerStack
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import UI4 as UI4
from QT4GLLayerStack.LayerStack import LayerStack
from UI4.Tabs.DopeSheet.KeyDrawingLayer import KeyDrawingLayer as KeyDrawingLayer
from UI4.Tabs.DopeSheet.KeyInteractionLayer import KeyInteractionLayer as KeyInteractionLayer
from UI4.Tabs.DopeSheet.PanAndScrollLayer import PanAndScrollLayer as PanAndScrollLayer
from UI4.Util.Events import ClickFilter as ClickFilter
from typing import ClassVar, Set, Tuple

class KeyLayerStack(LayerStack):
    _GL_UPDATE_THROTTLE_INTERVAL: ClassVar[int] = ...
    _MAX_SCALE_X: ClassVar[int] = ...
    def __init__(self, parent, treeWidget) -> None: ...
    def _KeyLayerStack__directUpdateGL(self): ...
    def _KeyLayerStack__getKeysSelected(self, item, keyList, includeParents: bool = ...): ...
    def _KeyLayerStack__getTreeOffsetAndHeight(self): ...
    def clearKeysPotential(self): ...
    def clearSelection(self, update: bool = ...): ...
    def contextMenuEvent(self, event): ...
    def event(self, rawEvent): ...
    def fontChange(self, oldFont: PyQt5.QtGui.QFont): ...
    def frameInOut(self): ...
    def frameKeysAll(self): ...
    def frameKeysSelected(self): ...
    def frameTimeRange(self, inTime, outTime): ...
    def frameWorkingInOut(self): ...
    def getKeysSelected(self, includeParents: bool = ...): ...
    def hitTestBox(self, worldBox): ...
    def hitTestPoint(self, worldPt): ...
    def hitTestPointForItem(self, worldPt): ...
    def resizeGL(self, w, h): ...
    def selectAll(self, update: bool = ...): ...
    def setGhostTime(self, t): ...
    def setKeysPotential(self, potentials, conflict: bool = ...): ...
    def setKeysSelected(self, keyList, selected, update: bool = ...): ...
    def setKeysSelectedExclusive(self, keyList, update: bool = ...): ...
    def toggleKeysSelected(self, keyList, update: bool = ...): ...
    def translateEyePoint(self, dx, dy): ...
    def updateGL(self): ...
    def updateScroll(self): ...
