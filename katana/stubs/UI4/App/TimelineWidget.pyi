# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import KatanaResources as KatanaResources
import NodegraphAPI as NodegraphAPI
import UI4.FormMaster.ParameterKeyMimeData as ParameterKeyMimeData
import PyQt5.QtCore
import QT4Widgets as QT4Widgets
import QT4Widgets.Timebar
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import UI4.FormMaster.ParameterCurveEditSet
import Utils as Utils
from UI4.FormMaster.ParameterCurveEditSet import ParameterCurveEditWatcher as ParameterCurveEditWatcher
from UI4.Util.UndoGrouping import UndoContextGuard as UndoContextGuard
from typing import ClassVar, Set, Tuple

class TimelineWidget(QT4Widgets.Timebar.TimebarWidget, UI4.FormMaster.ParameterCurveEditSet.ParameterCurveEditWatcher):
    keysChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent) -> None: ...
    def _TimelineWidget__contextMenu(self, localPos): ...
    def _TimelineWidget__currentTime_changed(self, time, final): ...
    def _TimelineWidget__fullRange_changed(self, inTime, outTime): ...
    def _TimelineWidget__getNameForParameters(self, parameters): ...
    def _TimelineWidget__increment_changed(self, increment): ...
    def _TimelineWidget__nodegraph_loadEnd_callback(self, eventType, eventID, **kwargs): ...
    def _TimelineWidget__nodegraph_setCurrentTime_callback(self, eventType, eventID, **kwargs): ...
    def _TimelineWidget__nodegraph_setTimeIncrement_callback(self, eventType, eventID, **kwargs): ...
    def _TimelineWidget__nodegraph_setTimeRange_callback(self, eventType, eventID, **kwargs): ...
    def _TimelineWidget__nodegraph_setWorkingTimeRange_callback(self, eventType, eventID, **kwargs): ...
    def _TimelineWidget__on_keysChanged(self): ...
    def _TimelineWidget__selection_changed(self): ...
    def _TimelineWidget__showDopeSheet(self): ...
    def _TimelineWidget__timeRange_changed(self, inTime, outTime): ...
    def _TimelineWidget__updateKeys(self): ...
    def _initializeSet(self, curveEditSetCopy): ...
    def _keysActiveChanged(self, paramFullName, active): ...
    def _keysChanged(self, paramFullName): ...
    def _nameChanged(self, oldParamFullName, newParamFullName, newParamLocalName): ...
    def _nodeNameChanged(self, oldNodeName, newNodeName): ...
    def _showKeys(self, paramFullName, show): ...
