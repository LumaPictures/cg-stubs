import pxr.Gf as Gf
import PySide6.QtCore
import pxr.Sdf as Sdf
from pxr.Usdviewq.customAttributes import BoundingBoxAttribute as BoundingBoxAttribute, ComputedPropertyFactory as ComputedPropertyFactory, ComputedPropertyNames as ComputedPropertyNames, LocalToWorldXformAttribute as LocalToWorldXformAttribute
from typing import Any, Callable, ClassVar

class Blocker:
    __init__: ClassVar[Callable] = ...
    blocked: ClassVar[Callable] = ...
    __enter__: ClassVar[Callable] = ...
    __exit__: ClassVar[Callable] = ...

class SelectionDataModel(PySide6.QtCore.QObject):
    __init__: ClassVar[Callable] = ...
    _buildPropPath: ClassVar[Callable] = ...
    _computedPropSelectionChanged: ClassVar[Callable] = ...
    _ensureValidPrimPath: ClassVar[Callable] = ...
    _ensureValidPropPath: ClassVar[Callable] = ...
    _ensureValidTargetPath: ClassVar[Callable] = ...
    _getComputedPropFromPath: ClassVar[Callable] = ...
    _getPropFromPath: ClassVar[Callable] = ...
    _getTargetFromPath: ClassVar[Callable] = ...
    _primSelectionChanged: ClassVar[Callable] = ...
    _propSelectionChanged: ClassVar[Callable] = ...
    _requireNotBatchingComputedProps: ClassVar[Callable] = ...
    _requireNotBatchingPrims: ClassVar[Callable] = ...
    _requireNotBatchingProps: ClassVar[Callable] = ...
    _switchProps: ClassVar[Callable] = ...
    _validateComputedPropName: ClassVar[Callable] = ...
    _validateInstanceIndexParameter: ClassVar[Callable] = ...
    addComputedProp: ClassVar[Callable] = ...
    addComputedPropPath: ClassVar[Callable] = ...
    addPrim: ClassVar[Callable] = ...
    addPrimPath: ClassVar[Callable] = ...
    addProp: ClassVar[Callable] = ...
    addPropPath: ClassVar[Callable] = ...
    addPropTarget: ClassVar[Callable] = ...
    addPropTargetPath: ClassVar[Callable] = ...
    clear: ClassVar[Callable] = ...
    clearComputedProps: ClassVar[Callable] = ...
    clearPoint: ClassVar[Callable] = ...
    clearPrims: ClassVar[Callable] = ...
    clearProps: ClassVar[Callable] = ...
    getComputedPropPaths: ClassVar[Callable] = ...
    getComputedProps: ClassVar[Callable] = ...
    getFocusComputedProp: ClassVar[Callable] = ...
    getFocusComputedPropPath: ClassVar[Callable] = ...
    getFocusPrim: ClassVar[Callable] = ...
    getFocusPrimPath: ClassVar[Callable] = ...
    getFocusProp: ClassVar[Callable] = ...
    getFocusPropPath: ClassVar[Callable] = ...
    getLCDPaths: ClassVar[Callable] = ...
    getLCDPrims: ClassVar[Callable] = ...
    getPoint: ClassVar[Callable] = ...
    getPrimInstances: ClassVar[Callable] = ...
    getPrimPathInstances: ClassVar[Callable] = ...
    getPrimPaths: ClassVar[Callable] = ...
    getPrims: ClassVar[Callable] = ...
    getPropPaths: ClassVar[Callable] = ...
    getPropTargetPaths: ClassVar[Callable] = ...
    getPropTargets: ClassVar[Callable] = ...
    getProps: ClassVar[Callable] = ...
    removeAbstractPrims: ClassVar[Callable] = ...
    removeComputedProp: ClassVar[Callable] = ...
    removeComputedPropPath: ClassVar[Callable] = ...
    removeInactivePrims: ClassVar[Callable] = ...
    removePrim: ClassVar[Callable] = ...
    removePrimPath: ClassVar[Callable] = ...
    removeProp: ClassVar[Callable] = ...
    removePropPath: ClassVar[Callable] = ...
    removePropTarget: ClassVar[Callable] = ...
    removePropTargetPath: ClassVar[Callable] = ...
    removePrototypePrims: ClassVar[Callable] = ...
    removeUndefinedPrims: ClassVar[Callable] = ...
    removeUnpopulatedPrims: ClassVar[Callable] = ...
    setComputedProp: ClassVar[Callable] = ...
    setComputedPropPath: ClassVar[Callable] = ...
    setPoint: ClassVar[Callable] = ...
    setPrim: ClassVar[Callable] = ...
    setPrimPath: ClassVar[Callable] = ...
    setProp: ClassVar[Callable] = ...
    setPropPath: ClassVar[Callable] = ...
    setPropTarget: ClassVar[Callable] = ...
    setPropTargetPath: ClassVar[Callable] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    switchToPrim: ClassVar[Callable] = ...
    switchToPrimPath: ClassVar[Callable] = ...
    togglePrim: ClassVar[Callable] = ...
    togglePrimPath: ClassVar[Callable] = ...
    def signalComputedPropSelectionChanged(self, *args, **kwargs) -> Any: ...
    def signalPrimSelectionChanged(self, *args, **kwargs) -> Any: ...
    def signalPropSelectionChanged(self, *args, **kwargs) -> Any: ...

class _PrimSelection:
    __init__: ClassVar[Callable] = ...
    _allInstancesSelected: ClassVar[Callable] = ...
    _clearPrimPath: ClassVar[Callable] = ...
    _discardInstance: ClassVar[Callable] = ...
    _noInstancesSelected: ClassVar[Callable] = ...
    addPrimPath: ClassVar[Callable] = ...
    clear: ClassVar[Callable] = ...
    getDiff: ClassVar[Callable] = ...
    getPrimPathInstances: ClassVar[Callable] = ...
    getPrimPaths: ClassVar[Callable] = ...
    removeMatchingPaths: ClassVar[Callable] = ...
    removePrimPath: ClassVar[Callable] = ...
    togglePrimPath: ClassVar[Callable] = ...

class _PropSelection:
    __init__: ClassVar[Callable] = ...
    addPropPath: ClassVar[Callable] = ...
    addTarget: ClassVar[Callable] = ...
    clear: ClassVar[Callable] = ...
    getPropPaths: ClassVar[Callable] = ...
    getTargets: ClassVar[Callable] = ...
    removePropPath: ClassVar[Callable] = ...
    removeTarget: ClassVar[Callable] = ...