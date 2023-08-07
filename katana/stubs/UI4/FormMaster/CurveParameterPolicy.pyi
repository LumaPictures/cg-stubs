# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import UI4.FormMaster.ParameterCurveEditSet as ParameterCurveEditSet
import PyFCurve as PyFCurve
import PyQt5.QtCore
import PyXmlIO as PyXmlIO
import PyQt5.QtCore as QtCore
import UI4.FormMaster.States as States
import Utils as Utils
from UI4.FormMaster.BaseParameterPolicy import BaseParameterPolicy as BaseParameterPolicy
from typing import Set, Tuple

class CurveParameterPolicy(BaseParameterPolicy):
    def __init__(self, param, parent) -> None: ...
    def _CurveParameterPolicy__isValidFCurveElementInMimeData(self, mimeData): ...
    def canHaveCurve(self): ...
    def checkMimeData(self, mimeData): ...
    def getCurveAutoKey(self): ...
    def getCurveKey(self): ...
    def getMimeData(self) -> PyQt5.QtCore.QMimeData: ...
    def getValue(self): ...
    def getValueState(self): ...
    def isCurveEnabled(self): ...
    def isCurveViewed(self): ...
    def setCurveAutoKey(self, autoKey): ...
    def setCurveEnabled(self, state): ...
    def setCurveKey(self, state): ...
    def setCurveViewed(self, state): ...
    def setMimeData(self, mimeData, dropAction): ...
    def setValue(self, value, final: bool = ...): ...
    def setValueState(self, state): ...
