# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import NodeGraphView as NodeGraphView
import NodegraphAPI as NodegraphAPI
import UI4.KatanaPrefs.PrefNames as PrefNames
import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import UI4 as UI4
from UI4.KatanaPrefs.KatanaPrefsObject import KatanaPrefs as KatanaPrefs
from UI4.Tabs.NodeGraphTab.Layers.NodeOverlayLayer import DrawNodeNameOverlay as DrawNodeNameOverlay
from typing import Set, Tuple

class OffscreenFlagDisplayLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def _OffscreenFlagDisplayLayer__drawArrowToNode(self, node: NodegraphAPI.Node, wsize, p1, p2, cx, cy, color, mousePos): ...
    def _OffscreenFlagDisplayLayer__hitTestArrow(self, pos, angle, clickPoint): ...
    def paintGL(self): ...
    def processEvent(self, event): ...

def _IsNodeHidden(node: NodegraphAPI.Node): ...
