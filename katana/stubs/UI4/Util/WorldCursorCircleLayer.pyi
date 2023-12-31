# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Util.GLDrawingRoutines as GLDrawingRoutines
import NodegraphAPI
import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import UI4 as UI4
from UI4.FormMaster.Editors.Layers.LayerWithTransform import LayerWithTransform as LayerWithTransform
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class WorldCursorCircleLayer(LayerWithTransform, QT4GLLayerStack.LayerStack.Layer):
    _CROSSHAIR_SIZE: ClassVar[int] = ...
    _CROSSHAIR_START: ClassVar[int] = ...
    _CROSSHAIR_THRESHOLD: ClassVar[int] = ...
    def __init__(self, node: NodegraphAPI.Node, radius: Incomplete | None = ..., **kwargs) -> None: ...
    def _drawCursor(self, cursorPos, radius, color): ...
    def getCursorPos(self): ...
    def getRadius(self): ...
    def paintGL(self): ...
    def setCursorPos(self, newCursorPos): ...
    def setRadius(self, r): ...
    def setVisible(self, visible): ...
