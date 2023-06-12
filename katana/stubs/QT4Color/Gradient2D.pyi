# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4Color.ColorTransforms as ColorTransforms
import QT4Color.Degenerate as Degenerate
import QT4Color.Globals as Globals
import PyOpenColorIO as OCIO
import PyQt5.QtWidgets
from typing import ClassVar

OCIO_ERROR: None
cursor_circle_data: bytes

class Gradient2DWidget(PyQt5.QtWidgets.QFrame):
    valueChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, color, uMode, vMode, parent, enableFilmlook: bool = ..., enableNoFilmlookColorSpace: bool = ...): ...
    def _Gradient2DWidget__gradientDestroyedCB(self): ...
    def _Gradient2DWidget__updateGradient(self): ...
    def _Gradient2DWidget__wheelEventCB(self, delta): ...
    def setColor(self, color): ...
    def setFilmlookEnabled(self, enabled): ...
    def setMode(self, uMode, vMode): ...
    def setNoFilmlookColorSpaceEnabled(self, enabled): ...
    def setReadOnly(self, value): ...
    def sizeHint(self): ...
    def sizePolicy(self): ...

class GradientDrawable(PyQt5.QtWidgets.QOpenGLWidget):
    CURSOR_CIRCLE: ClassVar[None] = ...
    valueChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    wheelEventSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, *args): ...
    def _GradientDrawable__drawGradient(self): ...
    def _GradientDrawable__drawMark(self): ...
    def _GradientDrawable__posToRgb(self, position): ...
    def _GradientDrawable__sendValueChangedFromMouse(self, ev, final: bool = ...): ...
    def _GradientDrawable__windowPosToUV(self, pos): ...
    def getPickingColorspace(self): ...
    def mouseMoveEvent(self, ev): ...
    def mousePressEvent(self, ev): ...
    def mouseReleaseEvent(self, ev): ...
    def paintGL(self): ...
    def resizeGL(self, width, height): ...
    def setColorAndModes(self, rgb, uMode, vMode): ...
    def setFilmlookEnabled(self, enabled): ...
    def setNoFilmlookColorSpaceEnabled(self, enabled): ...
    def setReadOnly(self, value): ...
    def wheelEvent(self, ev): ...