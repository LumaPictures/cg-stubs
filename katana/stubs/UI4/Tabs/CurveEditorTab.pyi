# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import PyFCurve as PyFCurve
import PyFCurveGraphWidget
import QT4Widgets as QT4Widgets
import QTFCurve as QTFCurve
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import Utils as Utils
from PyUtilModule.VirtualKatana import FormMaster as FormMaster
from UI4.Tabs.BaseTab import BaseTab as BaseTab
from _typeshed import Incomplete
from typing import Set, Tuple

PluginRegistry: list
TEMPORAL_QUANTIZATION_STEPS: int
TEMPORAL_QUANTIZATION_STEPS_INVERSE: float
global_paramExpressionCache: dict
global_paramExpressionCurves: dict
global_paramsShowingKeys: set

class CurveEditorPanel(BaseTab):
    class _LocalDomainSelectionObserver(PyFCurveGraphWidget.DomainSliderObserver):
        def __init__(self, domainSlider) -> None: ...
        def valueChanged(self, domainSlider: Incomplete | None = ...): ...
    def __init__(self, parent) -> None: ...
    def _CurveEditorPanel__actionBegin_callback(self, name): ...
    def _CurveEditorPanel__actionEnd_callback(self): ...
    def _CurveEditorPanel__finalizeValue_self_callback(self, eventType, eventID, **kwargs): ...
    def _CurveEditorPanel__nodegraph_setCurrentTime_callback(self, eventType, eventID, **kwargs): ...
    def _CurveEditorPanel__parameter_showKeys_callback(self, eventType, eventID, paramFullName, show): ...
    def _CurveEditorPanel__processUnfocusedKeyEvent(self, unfocusedEvent): ...
    def _CurveEditorPanel__unloadCurve(self, fcurve): ...
    def _CurveEditorPanel__updateDomainSlider(self): ...
    def _CurveEditorPanel__updateKeys(self): ...
    def _CurveEditorPanel__update_self_callback(self, eventType, eventID, **kwargs): ...
    def closeEvent(self, event): ...
    def event(self, event): ...

def __eval_node_param(name, frame): ...
def global_parameter_showKeys_callback(eventType, eventID, paramFullName, show): ...
