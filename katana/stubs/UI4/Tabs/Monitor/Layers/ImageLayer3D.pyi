# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import UI4 as UI4
from UI4.Tabs.Monitor.Layers.ImageLayerBase import ImageLayerBase as ImageLayerBase
from typing import Set, Tuple

class ImageLayer3D(QT4GLLayerStack.LayerStack.Layer, ImageLayerBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def getViewIndexFromWindowPos(self, qpos): ...
    def paintDropArea(self, dropColor): ...
    def paintGL(self): ...
    def processEvent(self, event): ...
