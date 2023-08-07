# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodeGraphView as NodeGraphView
import NodegraphAPI as NodegraphAPI
import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from UI4.KatanaPrefs.KatanaPrefsObject import KatanaPrefs as KatanaPrefs
from typing import Set, Tuple

class NodeGraphViewDrawingLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def idleUpdate(self): ...
    def paintGL(self): ...
    def setLayerStack(self, v): ...
