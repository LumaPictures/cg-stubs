# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from typing import ClassVar, Set, Tuple

class TimelineWidget(PyQt5.QtWidgets.QWidget):
    _TimelineWidget__ACTION_NONE: ClassVar[int] = ...
    _TimelineWidget__ACTION_PAN: ClassVar[int] = ...
    _TimelineWidget__ACTION_SELECT: ClassVar[int] = ...
    _TimelineWidget__ACTION_SET_TIME: ClassVar[int] = ...
    _TimelineWidget__ACTION_SLIDER_L: ClassVar[int] = ...
    _TimelineWidget__ACTION_SLIDER_PAN: ClassVar[int] = ...
    _TimelineWidget__ACTION_SLIDER_R: ClassVar[int] = ...
    _TimelineWidget__ACTION_ZOOM: ClassVar[int] = ...
    _TimelineWidget__HIT_NONE: ClassVar[int] = ...
    _TimelineWidget__HIT_SLIDER_CENTER: ClassVar[int] = ...
    _TimelineWidget__HIT_SLIDER_L: ClassVar[int] = ...
    _TimelineWidget__HIT_SLIDER_R: ClassVar[int] = ...
    _TimelineWidget__HIT_TIMELINE: ClassVar[int] = ...
    _TimelineWidget__HOVER_NONE: ClassVar[int] = ...
    _TimelineWidget__HOVER_SLIDER_CENTER: ClassVar[int] = ...
    _TimelineWidget__HOVER_SLIDER_L: ClassVar[int] = ...
    _TimelineWidget__HOVER_SLIDER_R: ClassVar[int] = ...
    currentTimeChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    fullRangeChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    keySetChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    selectionChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    timeRangeChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, *args) -> None: ...
    @staticmethod
    def CalculateTicks(rangeMin, rangeMax, posFn, invPosFn, widthFn, margin: int = ..., forceBoundLabels: bool = ...): ...
    @staticmethod
    def RoundRange(range): ...
    def _TimelineWidget__cleanRange(self, range, intify: bool = ...): ...
    def _TimelineWidget__emitCurrentTimeChanged(self, time, final): ...
    def _TimelineWidget__getSliderDivisionRects(self, sliderRect): ...
    def _TimelineWidget__getSliderExtent(self): ...
    def _TimelineWidget__getSliderTimeFromLocalPoint(self, x): ...
    def _TimelineWidget__getTickArea(self, time): ...
    def _TimelineWidget__getTickAreaExtent(self): ...
    def _TimelineWidget__getTimelineExtent(self): ...
    def _TimelineWidget__hitTestLocalPoint(self, point): ...
    def _TimelineWidget__paintArrows(self, painter): ...
    def _TimelineWidget__paintBackground(self, painter): ...
    def _TimelineWidget__paintCurrentTime(self, painter): ...
    def _TimelineWidget__paintHoverTime(self, painter): ...
    def _TimelineWidget__paintKeys(self, painter): ...
    def _TimelineWidget__paintSelection(self, painter): ...
    def _TimelineWidget__paintSlider(self, painter): ...
    def _TimelineWidget__paintTicksAndLabels(self, painter): ...
    def _TimelineWidget__setFloatTimeRange(self, floatTimeRange, update: bool = ..., final: bool = ...): ...
    def _TimelineWidget__zoomTimeRange(self, factor, center, final: bool = ...): ...
    def addKey(self, time): ...
    def allowSelection(self): ...
    def clearKeys(self): ...
    def currentTime(self): ...
    def fitTimeRangeToKeys(self): ...
    def floatHoverTime(self): ...
    def fullRange(self): ...
    def getTimeFromLocalX(self, x, floatValue: bool = ...): ...
    def hoverTime(self): ...
    def isFullRangeFinal(self): ...
    def isTimeRangeFinal(self): ...
    def keyPressEvent(self, keyEvent): ...
    def keySet(self): ...
    def leaveEvent(self, event): ...
    def mouseMoveEvent(self, mouseEvent): ...
    def mousePressEvent(self, mouseEvent): ...
    def mouseReleaseEvent(self, mouseEvent): ...
    def paintEvent(self, paintEvent): ...
    def removeKey(self, time): ...
    def resetTimeRange(self): ...
    def selectedTimeRange(self): ...
    def setAllowSelection(self, flag): ...
    def setCurrentTime(self, t): ...
    def setFullRange(self, range, final: bool = ...): ...
    def setKeys(self, keySet): ...
    def setSelectedTimeRange(self, timeRange): ...
    def setTimeRange(self, timeRange, final: bool = ...): ...
    def timeRange(self): ...
    def wheelEvent(self, wheelEvent): ...
