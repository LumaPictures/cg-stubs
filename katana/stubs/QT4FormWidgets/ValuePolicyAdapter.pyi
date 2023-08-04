# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.ValuePolicy
import QT4FormWidgets.ValuePolicy as ValuePolicy
from _typeshed import Incomplete
from typing import Set, Tuple

class ValuePolicyAdapter(QT4FormWidgets.ValuePolicy.AbstractValuePolicy):
    def __init__(self, alias, policyMap, parent: Incomplete | None = ...) -> None: ...
    def getArrayChild(self, index): ...
    def getArraySize(self): ...
    def getChildByName(self, name): ...
    def getChildren(self): ...
    def getName(self): ...
    def getNumChildren(self): ...
    def getType(self): ...
    def getValueState(self): ...
    def getWidgetHints(self): ...
    def isLocked(self): ...
    def removeArrayChild(self, index): ...
    def reorderArrayChild(self, oldIndex, newIndex): ...
    def setWidgetHints(self, hints): ...

class ValuePolicyAlias(QT4FormWidgets.ValuePolicy.AbstractValuePolicy):
    def __init__(self, alias, valuePolicy, parent: Incomplete | None = ...) -> None: ...
    def _AbstractValuePolicy__parentNameChanged(self, *args, **kwargs): ...
    def _appendToContextMenu(self, *args, **kwargs): ...
    def _appendToStateMenu(self, *args, **kwargs): ...
    def _appendToWrenchMenu(self, *args, **kwargs): ...
    def _childStateChange(self, *args, **kwargs): ...
    def _childStateReset(self, *args, **kwargs): ...
    def _closeButtonClicked(self, *args, **kwargs): ...
    def _customizeWrenchButton(self, *args, **kwargs): ...
    def _freeze(self, *args, **kwargs): ...
    def _handleValuePolicyChange(self, *args, **kwargs): ...
    def _potentialFreezeChange(self, *args, **kwargs): ...
    def _propagateNameChange(self, *args, **kwargs): ...
    def _propagateStateChange(self, visitedParents: set = ...): ...
    def _thaw(self, *args, **kwargs): ...
    def addCallback(self, *args, **kwargs): ...
    def addWeakCallback(self, *args, **kwargs): ...
    def bakeCurve(self, *args, **kwargs): ...
    def canHaveCurve(self, *args, **kwargs): ...
    def canHaveExpression(self, *args, **kwargs): ...
    def checkMimeData(self, *args, **kwargs): ...
    def delCallback(self, *args, **kwargs): ...
    def delWeakCallback(self, *args, **kwargs): ...
    def findRelativePolicy(self, *args, **kwargs): ...
    def getArrayChild(self, *args, **kwargs): ...
    def getArrayChildren(self, *args, **kwargs): ...
    def getArraySize(self, *args, **kwargs): ...
    def getAvailableStates(self, *args, **kwargs): ...
    def getChildByName(self, *args, **kwargs): ...
    def getChildren(self, *args, **kwargs): ...
    def getCurve(self, *args, **kwargs): ...
    def getCurveAutoKey(self, *args, **kwargs): ...
    def getCurveKey(self, *args, **kwargs): ...
    def getCurveXml(self, *args, **kwargs): ...
    def getExpression(self, *args, **kwargs): ...
    def getExpressionError(self, *args, **kwargs): ...
    def getExpressionNamespace(self, *args, **kwargs): ...
    def getExpressionReference(self, *args, **kwargs): ...
    def getFullName(self, *args, **kwargs): ...
    def getMimeData(self, *args, **kwargs): ...
    def getName(self): ...
    def getNumChildren(self, *args, **kwargs): ...
    def getOpenStateKey(self, *args, **kwargs): ...
    def getParent(self): ...
    def getSceneGraphLocationPath(self, *args, **kwargs): ...
    def getStateAppearance(self, *args, **kwargs): ...
    def getTooltip(self, *args, **kwargs): ...
    def getType(self, *args, **kwargs): ...
    def getValue(self, *args, **kwargs): ...
    def getValueAsString(self, *args, **kwargs): ...
    def getValueState(self, *args, **kwargs): ...
    def getWidgetHints(self): ...
    def hasFloatingCurve(self, *args, **kwargs): ...
    def isCloseButtonEnabled(self, *args, **kwargs): ...
    def isCurveEnabled(self, *args, **kwargs): ...
    def isCurveViewed(self, *args, **kwargs): ...
    def isExpressionEnabled(self, *args, **kwargs): ...
    def isFrozen(self, *args, **kwargs): ...
    def isGroupParameterBeingEdited(self, *args, **kwargs): ...
    def isLocked(self, *args, **kwargs): ...
    def isValid(self, *args, **kwargs): ...
    def loadCurveFromFile(self, *args, **kwargs): ...
    def removeArrayChild(self, *args, **kwargs): ...
    def reorderArrayChild(self, *args, **kwargs): ...
    def setArraySize(self, *args, **kwargs): ...
    def setCurve(self, *args, **kwargs): ...
    def setCurveAutoKey(self, *args, **kwargs): ...
    def setCurveEnabled(self, *args, **kwargs): ...
    def setCurveKey(self, *args, **kwargs): ...
    def setCurveViewed(self, *args, **kwargs): ...
    def setCurveXml(self, *args, **kwargs): ...
    def setExpression(self, *args, **kwargs): ...
    def setExpressionEnabled(self, *args, **kwargs): ...
    def setMimeData(self, *args, **kwargs): ...
    def setParent(self, *args, **kwargs): ...
    def setValue(self, *args, **kwargs): ...
    def setValueFromString(self, *args, **kwargs): ...
    def setValueState(self, *args, **kwargs): ...
    def setWidgetHints(self, hints): ...
    def shouldDisplayClose(self, *args, **kwargs): ...
    def shouldDisplayState(self, *args, **kwargs): ...
    def shouldDisplayWrench(self, *args, **kwargs): ...
    def toggleValueState(self, *args, **kwargs): ...
    def valueChanged(self, *args, **kwargs): ...
    def waitForReady(self, *args, **kwargs): ...
    def writeCurveToFile(self, *args, **kwargs): ...
    def __getattr__(self, name): ...

def CreateValuePolicyAdapter(sourcePolicy, mapping, alias: str = ..., parent: Incomplete | None = ...): ...
def CreateValuePolicyAdapterMap(sourcePolicy, mapping): ...
def FlattenValuePolicyAdapterMap(mapping, visited: set = ...): ...
