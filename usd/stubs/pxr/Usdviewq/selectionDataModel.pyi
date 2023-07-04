# mypy: disable_error_code = misc
import pxr.Gf as Gf
import PySide6.QtCore
import pxr.Sdf as Sdf
import typing
from _typeshed import Incomplete
from pxr.Usdviewq.customAttributes import BoundingBoxAttribute as BoundingBoxAttribute, ComputedPropertyFactory as ComputedPropertyFactory, ComputedPropertyNames as ComputedPropertyNames, LocalToWorldXformAttribute as LocalToWorldXformAttribute
from typing import Callable, ClassVar

ALL_INSTANCES: int

class Blocker:
    def __init__(self, exitCallback: Callable = ...): ...
    def blocked(self): ...
    def __enter__(self): ...
    def __exit__(self, *args): ...

class SelectionDataModel(PySide6.QtCore.QObject):
    signalComputedPropSelectionChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalPrimSelectionChanged: ClassVar[PySide6.QtCore.Signal] = ...
    signalPropSelectionChanged: ClassVar[PySide6.QtCore.Signal] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, rootDataModel, _computedPropFactory: Incomplete | None = ...): ...
    def _buildPropPath(self, primPath, propName): ...
    def _computedPropSelectionChanged(self): ...
    def _ensureValidPrimPath(self, path): ...
    def _ensureValidPropPath(self, prop): ...
    def _ensureValidTargetPath(self, targetPath): ...
    def _getComputedPropFromPath(self, primPath, propName): ...
    def _getPropFromPath(self, path): ...
    def _getTargetFromPath(self, path): ...
    def _primSelectionChanged(self, emitSelChangedSignal: bool = ...): ...
    def _propSelectionChanged(self): ...
    def _requireNotBatchingComputedProps(self): ...
    def _requireNotBatchingPrims(self): ...
    def _requireNotBatchingProps(self): ...
    def _switchProps(self, fromPrimPath, toPrimPath): ...
    def _validateComputedPropName(self, propName): ...
    def _validateInstanceIndexParameter(self, instance): ...
    def addComputedProp(self, prop): ...
    def addComputedPropPath(self, primPath, propName): ...
    def addPrim(self, prim, instance: int = ...): ...
    def addPrimPath(self, path, instance: int = ...): ...
    def addProp(self, prop): ...
    def addPropPath(self, path): ...
    def addPropTarget(self, prop, target): ...
    def addPropTargetPath(self, path, targetPath): ...
    def clear(self): ...
    def clearComputedProps(self): ...
    def clearPoint(self): ...
    def clearPrims(self): ...
    def clearProps(self): ...
    def getComputedPropPaths(self): ...
    def getComputedProps(self): ...
    def getFocusComputedProp(self): ...
    def getFocusComputedPropPath(self): ...
    def getFocusPrim(self): ...
    def getFocusPrimPath(self): ...
    def getFocusProp(self): ...
    def getFocusPropPath(self): ...
    def getLCDPaths(self): ...
    def getLCDPrims(self): ...
    def getPoint(self): ...
    def getPrimInstances(self): ...
    def getPrimPathInstances(self): ...
    def getPrimPaths(self): ...
    def getPrims(self): ...
    def getPropPaths(self): ...
    def getPropTargetPaths(self): ...
    def getPropTargets(self): ...
    def getProps(self): ...
    def removeAbstractPrims(self): ...
    def removeComputedProp(self, prop): ...
    def removeComputedPropPath(self, primPath, propName): ...
    def removeInactivePrims(self): ...
    def removePrim(self, prim, instance: int = ...): ...
    def removePrimPath(self, path, instance: int = ...): ...
    def removeProp(self, prop): ...
    def removePropPath(self, path): ...
    def removePropTarget(self, prop, target): ...
    def removePropTargetPath(self, path, targetPath): ...
    def removePrototypePrims(self): ...
    def removeUndefinedPrims(self): ...
    def removeUnpopulatedPrims(self): ...
    def setComputedProp(self, prop): ...
    def setComputedPropPath(self, primPath, propName): ...
    def setPoint(self, point): ...
    def setPrim(self, prim, instance: int = ...): ...
    def setPrimPath(self, path, instance: int = ...): ...
    def setProp(self, prop): ...
    def setPropPath(self, path): ...
    def setPropTarget(self, prop, target): ...
    def setPropTargetPath(self, path, targetPath): ...
    def switchToPrim(self, prim, instance: int = ...): ...
    def switchToPrimPath(self, path, instance: int = ...): ...
    def togglePrim(self, prim, instance: int = ...): ...
    def togglePrimPath(self, path, instance: int = ...): ...

class _PrimSelection:
    def __init__(self): ...
    def _allInstancesSelected(self, path): ...
    def _clearPrimPath(self, path): ...
    def _discardInstance(self, path, instance): ...
    def _noInstancesSelected(self, path): ...
    def addPrimPath(self, path, instance: int = ...): ...
    def clear(self): ...
    def getDiff(self) -> typing.Any: ...
    def getPrimPathInstances(self): ...
    def getPrimPaths(self): ...
    def removeMatchingPaths(self, matches): ...
    def removePrimPath(self, path, instance: int = ...): ...
    def togglePrimPath(self, path, instance: int = ...): ...

class _PropSelection:
    def __init__(self): ...
    def addPropPath(self, primPath, propName): ...
    def addTarget(self, primPath, propName, target): ...
    def clear(self): ...
    def getPropPaths(self): ...
    def getTargets(self): ...
    def removePropPath(self, primPath, propName): ...
    def removeTarget(self, primPath, propName, target): ...