# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.HintUtils as HintUtils
import QT4FormWidgets.PolicyMimeData as PolicyMimeData
import QtCore
import QtWidgets
import Utils.WeakMethod as WeakMethod
import re
from _typeshed import Incomplete
from typing import ClassVar

class AbstractValuePolicy:
    SUBSCRIPT_EXPR: ClassVar[re.Pattern] = ...
    _QueuedChanged: ClassVar[dict] = ...
    def __init__(self, parent): ...
    def _AbstractValuePolicy__parentNameChanged(self, parentName): ...
    def _HandleQueuedChanges(self): ...
    def _appendToContextMenu(self, menu: QtWidgets.QMenu): ...
    def _appendToStateMenu(self, menu: QtWidgets.QMenu) -> bool: ...
    def _appendToWrenchMenu(self, menu): ...
    def _childStateChange(self): ...
    def _childStateReset(self): ...
    def _closeButtonClicked(self): ...
    def _customizeWrenchButton(self, wrenchButton: QtWidgets.QPushButton): ...
    def _freeze(self): ...
    def _handleValuePolicyChange(self, event: ValuePolicyEvent): ...
    def _potentialFreezeChange(self, anyHandlers: Incomplete | None = ..., active: Incomplete | None = ..., frozenTop: Incomplete | None = ...): ...
    def _propagateNameChange(self, policy: ValuePolicy): ...
    def _propagateStateChange(self, visitedParents: set = ...): ...
    def _thaw(self): ...
    def addCallback(self, callback): ...
    def addWeakCallback(self, callback): ...
    def bakeCurve(self, keys): ...
    def canHaveCurve(self): ...
    def canHaveExpression(self): ...
    def checkMimeData(self, mimeData): ...
    def delCallback(self, callback): ...
    def delWeakCallback(self, callback): ...
    def findRelativePolicy(self, pathList, index: int = ...): ...
    def getArrayChild(self, index): ...
    def getArrayChildren(self): ...
    def getArraySize(self): ...
    def getAvailableStates(self): ...
    def getChildByName(self, name): ...
    def getChildren(self): ...
    def getCurve(self): ...
    def getCurveAutoKey(self): ...
    def getCurveKey(self): ...
    def getCurveXml(self): ...
    def getExpression(self): ...
    def getExpressionError(self): ...
    def getExpressionNamespace(self): ...
    def getExpressionReference(self): ...
    def getFullName(self): ...
    def getMimeData(self) -> QtCore.QMimeData: ...
    def getName(self): ...
    def getNumChildren(self): ...
    def getOpenStateKey(self): ...
    def getParent(self): ...
    def getSceneGraphLocationPath(self) -> str | None: ...
    def getStateAppearance(self, state): ...
    def getTooltip(self) -> str: ...
    def getType(self): ...
    def getValue(self): ...
    def getValueAsString(self): ...
    def getValueState(self): ...
    def getWidgetHints(self): ...
    def hasFloatingCurve(self): ...
    def isCloseButtonEnabled(self) -> bool: ...
    def isCurveEnabled(self): ...
    def isCurveViewed(self): ...
    def isExpressionEnabled(self): ...
    def isFrozen(self): ...
    def isGroupParameterBeingEdited(self): ...
    def isLocked(self): ...
    def isValid(self) -> bool: ...
    def loadCurveFromFile(self, path): ...
    def removeArrayChild(self, index): ...
    def reorderArrayChild(self, oldIndex, newIndex): ...
    def setArraySize(self, size): ...
    def setCurve(self, curve): ...
    def setCurveAutoKey(self, autoKey): ...
    def setCurveEnabled(self, state): ...
    def setCurveKey(self, state): ...
    def setCurveViewed(self, state): ...
    def setCurveXml(self, xml): ...
    def setExpression(self, expr): ...
    def setExpressionEnabled(self, flag): ...
    def setMimeData(self, mimeData, dropAction): ...
    def setParent(self, parent: AbstractValuePolicy | None): ...
    def setValue(self, value, final: bool = ...): ...
    def setValueFromString(self, value, final: bool = ...): ...
    def setValueState(self, state): ...
    def shouldDisplayClose(self) -> bool: ...
    def shouldDisplayState(self): ...
    def shouldDisplayWrench(self): ...
    def toggleValueState(self): ...
    def valueChanged(self, value: bool = ..., final: bool = ..., stateChanged: bool = ..., topologyChanged: bool = ..., nameChanged: bool = ...): ...
    def waitForReady(self): ...
    def writeCurveToFile(self, path): ...

class ValuePolicyEvent:
    def __init__(self, policy, value, final, stateChanged, topologyChanged, nameChanged): ...
    def _updateChanges(self, value, final, stateChanged, topologyChanged, nameChanged): ...
    def getPolicy(self): ...
    def hasNameChanged(self): ...
    def hasStateChanged(self): ...
    def hasTopologyChanged(self): ...
    def hasValueChanged(self): ...
    def isFinal(self): ...

class ValuePolicyProxy:
    def __init__(self, policy): ...
    def _ValuePolicyProxy__valueChangedEvent(self, event): ...
    def addCallback(self, callback): ...
    def addWeakCallback(self, callback): ...
    def delCallback(self, callback): ...
    def delWeakCallback(self, callback): ...
    def findRelativePolicy(self, pathList, index: int = ...): ...
    def getChildByName(self, name): ...
    def getChildren(self): ...
    def getFullName(self): ...
    def getMimeData(self): ...
    def getName(self): ...
    def getPolicy(self): ...
    def getTooltip(self) -> str: ...
    def getWidgetHints(self): ...
    def setName(self, overrideName): ...
    def setPolicy(self, policy): ...
    def setWidgetHints(self, overrideHints): ...
    def __getattr__(self, name): ...