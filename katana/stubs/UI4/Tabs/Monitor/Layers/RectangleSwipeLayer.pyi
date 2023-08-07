# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack as QT4GLLayerStack
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from QT4GLLayerStack.RectangleLayer import RectangleLayer
from UI4.Tabs.Monitor.Layers.ImageLayerBase import ImageLayerBase as ImageLayerBase
from UI4.Util.GLDrawingRoutines import drawEllipse as drawEllipse, drawSmoothArrow as drawSmoothArrow, drawSmoothCross as drawSmoothCross, drawSmoothCrosshairs as drawSmoothCrosshairs, drawSmoothEllipse as drawSmoothEllipse, drawSmoothHandle as drawSmoothHandle, drawSmoothPoly as drawSmoothPoly, drawSmoothText as drawSmoothText
from typing import Set, Tuple

class RectangleSwipeLayer(RectangleLayer, ImageLayerBase):
    def __init__(self, *args, **kwargs) -> None: ...
    def getViewIndexFromWindowPos(self, qpos): ...
    def paintGL(self): ...
    def processEvent(self, event): ...
