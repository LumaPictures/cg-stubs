# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QT4Widgets.Timeline as Timeline
from typing import ClassVar

class FrameButtonWidget(PyQt5.QtWidgets.QToolButton):
    def __init__(self, text, parent): ...

class FrameEditWidget(PyQt5.QtWidgets.QLineEdit):
    def __init__(self, parent, callback): ...
    def changeEvent(self, event): ...

class FramesPopup(PyQt5.QtWidgets.QFrame):
    closed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent): ...
    def addRow(self): ...
    def addWidget(self, text, widget): ...
    def closeEvent(self, event): ...
    def popup(self, pos): ...

class TimebarWidget(PyQt5.QtWidgets.QFrame):
    currentTimeChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    fullRangeChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    incrementChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    selectionChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    timeRangeChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, *args): ...
    def _TimebarWidget__addLabeledEdit(self, labelText, callback, layout): ...
    def _TimebarWidget__backButton_clicked_callback(self): ...
    def _TimebarWidget__backKeyButton_clicked_callback(self): ...
    def _TimebarWidget__buildChildren(self): ...
    def _TimebarWidget__doEditCurrent(self): ...
    def _TimebarWidget__doEditEnd(self): ...
    def _TimebarWidget__doEditIncrement(self): ...
    def _TimebarWidget__doEditStart(self): ...
    def _TimebarWidget__emitCurrentTimeChanged(self, time, final): ...
    def _TimebarWidget__forwardButton_clicked_callback(self): ...
    def _TimebarWidget__forwardKeyButton_clicked_callback(self): ...
    def _TimebarWidget__resetButton_clicked_callback(self): ...
    def _TimebarWidget__timeline_currentTimeChanged_CB(self, time, final): ...
    def _TimebarWidget__timeline_fullRangeChanged(self, inTime, outTime): ...
    def _TimebarWidget__timeline_selectionChanged(self): ...
    def _TimebarWidget__timeline_timeRangeChanged(self, inTime, outTime): ...
    def addKey(self, time): ...
    def backButton(self): ...
    def backKey(self): ...
    def backKeyButton(self): ...
    def backStep(self): ...
    def clearKeys(self): ...
    def currentTime(self): ...
    def currentTimeEdit(self): ...
    def endTimeEdit(self): ...
    def forwardButton(self): ...
    def forwardKey(self): ...
    def forwardKeyButton(self): ...
    def forwardStep(self): ...
    def fullRange(self): ...
    def increment(self): ...
    def incrementEdit(self): ...
    def isFullRangeFinal(self): ...
    def isTimeRangeFinal(self): ...
    def keySet(self): ...
    def removeKey(self, time): ...
    def resetButton(self): ...
    def selectedTimeRange(self): ...
    def setCurrentTime(self, time): ...
    def setFullRange(self, range): ...
    def setIncrement(self, i): ...
    def setKeys(self, keys): ...
    def setSelectedTimeRange(self, range): ...
    def setTimeRange(self, range): ...
    def startTimeEdit(self): ...
    def timeRange(self): ...
    def timeline(self): ...