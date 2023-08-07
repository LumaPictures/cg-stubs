# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import NodegraphAPI as NodegraphAPI
import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import PyQt5.QtCore as QtCore
import Utils as Utils
from UI4.Tabs.NodeGraphTab.Layers.LinkConnectionLayer import LinkConnectionLayer as LinkConnectionLayer
from typing import Set, Tuple

class PortInteractionLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def _PortInteractionLayer__node_delete_cb(self, eventType, eventID, node: NodegraphAPI.Node, *args, **kwargs): ...
    def _PortInteractionLayer__removeNodeCallback(self, eventType, eventID, node: NodegraphAPI.Node, **kwargs): ...
    def paintGL(self): ...
    def processEvent(self, event): ...
