# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import LiveRenderPortOpObserver
import Nodes3DAPI.Node3DEventTypes as Node3DEventTypes
import Nodes3DAPI.Node3D_geolib3 as Node3D_geolib3
import NodegraphAPI
import PyUtilModule.RenderManager.NodegraphUtils as NodegraphUtils
import Nodes3DAPI as Nodes3DAPI
import PyFnAttribute as PyFnAttribute
import PyFnGeolib as PyFnGeolib
import PyFnGeolibServices as PyFnGeolibServices
import PyUtilModule.RenderManager.RenderGlobals as RenderGlobals
import PyUtilModule.RenderManager as RenderManager
import RenderSettingsExtractor
import PyUtilModule.RenderingCommon as RenderingCommon
import PyUtilModule.RenderManager.ScenegraphUtils as ScenegraphUtils
import Utils as Utils
import abc
from Nodes3DAPI.OpCacheManager import OpCacheManager as OpCacheManager
from PyUtilModule.WorkingSet import WorkingSet as WorkingSet
from PyUtilModule.WorkingSetManager import WorkingSetManager as WorkingSetManager
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class AOVOpChain(_OpChain):
    def __init__(self, mainSequenceID: int) -> None: ...
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp) -> PyFnGeolib.GeolibRuntimeOp: ...

class CameraOverrideOpChain(_OpChain):
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp, renderCameraPath: str) -> PyFnGeolib.GeolibRuntimeOp: ...
    def applyOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, inputOp: PyFnGeolib.GeolibRuntimeOp, renderCameraType: int, renderCameraPath: str) -> PyFnGeolib.GeolibRuntimeOp: ...

class ImplicitResolversOpChain(_OpChain):
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState) -> PyFnGeolib.GeolibRuntimeOp: ...

class IsolateOpChain(_OpArgsOpChain):
    def __init__(self) -> None: ...
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp, opArgs: PyFnAttribute.GroupAttribute) -> PyFnGeolib.GeolibRuntimeOp: ...
    def applyOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, inputOp: PyFnGeolib.GeolibRuntimeOp, cameraName: str) -> PyFnGeolib.GeolibRuntimeOp: ...

class LiveAttributeQueue:
    _kAttrEditorPattern: ClassVar[str] = ...
    _kAttrPathPattern: ClassVar[str] = ...
    _kAttrRootPattern: ClassVar[str] = ...
    _kLocationPathPattern: ClassVar[str] = ...
    def __init__(self) -> None: ...
    def flush(self, txn: LiveRenderPortOpObserver._TransactionProxy): ...
    def insert(self, locationPath: str, attrPath: str, attrValue: str, attrEditor: PyFnAttribute.GroupAttribute | None): ...
    def setOp(self, op: PyFnGeolib.GeolibRuntimeOp): ...

class LiveRenderOpChain:
    _opCacheManager: ClassVar[OpCacheManager] = ...
    def __init__(self, renderUUID: str, mainSequenceID: int, renderSettingsExtractor: RenderSettingsExtractor, initialImplicitResolversOpChain: ImplicitResolversOpChain, initialDefaultRenderSettingsOpChain: RenderSettingsDefaultsOpChain, implicitResolversOpChain: ImplicitResolversOpChain, defaultRenderSettingsOpChain: RenderSettingsDefaultsOpChain, isolateOpChain: IsolateOpChain, renderWorkingSetOpChain: RenderWorkingSetOpChain, renderSettingsOpChain: RenderSettingsOpChain, renderOutputsOpChain: RenderOutputsOpChain, virtualCameraOpChain: VirtualCameraOpChain, cameraOverrideOpChain: CameraOverrideOpChain, aovOpChain: AOVOpChain, roiOpChain: ROIOpChain, renderInfoPluginOpChain: RenderInfoPluginOpChain, liveRenderUpdatesOpChain: LiveRenderUpdatesOpChain) -> None: ...
    @classmethod
    def _getCachedOp(cls, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState, visitedState, txn): ...
    def getOp(self, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState, visitedState: set, txnProxy: LiveRenderPortOpObserver._TransactionProxy) -> PyFnGeolib.GeolibRuntimeOp: ...

class LiveRenderUpdatesOpChain(_OpArgsOpChain):
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp, workingSetOpArgs: PyFnAttribute.GroupAttribute) -> PyFnGeolib.GeolibRuntimeOp: ...
    def applyOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, inputOp: PyFnGeolib.GeolibRuntimeOp) -> PyFnGeolib.GeolibRuntimeOp: ...

class ROIOpChain(_OpChain):
    def __init__(self) -> None: ...
    def _checkAndUpdateDirtyState(self, roi) -> bool: ...
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp, roi) -> PyFnGeolib.GeolibRuntimeOp: ...
    def applyOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, inputOp: PyFnGeolib.GeolibRuntimeOp) -> PyFnGeolib.GeolibRuntimeOp: ...

class RenderInfoPluginOpChain(_OpChain):
    def __init__(self, liveAttributeQueue) -> None: ...
    @staticmethod
    def _RenderInfoPluginOpChain__createOp(txnProxy, opType, opArgs): ...
    def _checkAndUpdateDirtyState(self, graphState: NodegraphAPI.GraphState, renderer: str) -> bool: ...
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp, graphState: NodegraphAPI.GraphState, renderer: str) -> PyFnGeolib.GeolibRuntimeOp: ...

class RenderOutputsOpChain(_OpChain):
    def __init__(self) -> None: ...
    def _checkAndUpdateDirtyState(self, renderOutputs: list[str]) -> bool: ...
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp, renderOutputs: list[str]) -> PyFnGeolib.GeolibRuntimeOp: ...

class RenderSettingsDefaultsOpChain(_OpChain):
    def __init__(self) -> None: ...
    def _checkAndUpdateDirtyState(self, opSystemArgs: PyFnAttribute.GroupAttribute) -> bool: ...
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp, opSystemArgs: PyFnAttribute.GroupAttribute) -> PyFnGeolib.GeolibRuntimeOp: ...

class RenderSettingsExtractor:
    class Settings(tuple):
        _field_defaults: ClassVar[dict] = ...
        _fields: ClassVar[tuple] = ...
        _fields_defaults: ClassVar[dict] = ...
        def __init__(self, _cls, renderSettingsAttr, renderer, renderCameraPath, renderCameraType, interactiveOutputs) -> None: ...
        def _asdict(self): ...
        @classmethod
        def _make(cls, iterable): ...
        def _replace(self, _self, **kwds): ...
        def __getnewargs__(self): ...
        @property
        def interactiveOutputs(self): ...
        @property
        def renderCameraPath(self): ...
        @property
        def renderCameraType(self): ...
        @property
        def renderSettingsAttr(self): ...
        @property
        def renderer(self): ...
    def __init__(self, runtime: PyFnGeolib.GeolibRuntime) -> None: ...
    def extract(self, txn: PyFnGeolib.GeolibRuntimeTransaction, terminalOp: PyFnGeolib.GeolibRuntimeOp) -> RenderSettingsExtractor.Settings: ...
    def getCachedRootAttrs(self): ...

class RenderSettingsOpChain(_OpChain):
    def __init__(self) -> None: ...
    def _checkAndUpdateDirtyState(self, graphState: NodegraphAPI.GraphState, renderSettings: PyFnAttribute.GroupAttribute) -> bool: ...
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp, graphState: NodegraphAPI.GraphState, renderSettings: PyFnAttribute.GroupAttribute) -> PyFnGeolib.GeolibRuntimeOp: ...

class RenderWorkingSetOpChain(_OpArgsOpChain):
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp, opArgs: PyFnAttribute.GroupAttribute) -> PyFnGeolib.GeolibRuntimeOp: ...
    def applyOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, inputOp: PyFnGeolib.GeolibRuntimeOp, cameraName: str) -> PyFnGeolib.GeolibRuntimeOp: ...

class VirtualCameraOpChain(_OpChain):
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp) -> PyFnGeolib.GeolibRuntimeOp: ...
    def applyOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, inputOp: PyFnGeolib.GeolibRuntimeOp, renderCameraPath: str) -> PyFnGeolib.GeolibRuntimeOp: ...

class _OpArgsOpChain(_OpChain):
    def __init__(self) -> None: ...
    def _checkAndUpdateDirtyState(self, opArgs: PyFnAttribute.GroupAttribute) -> bool: ...

class _OpChain(_OpPool):
    __metaclass__: ClassVar[type[abc.ABCMeta]] = ...
    def __init__(self, rootOp: Incomplete | None = ..., terminalOp: Incomplete | None = ...) -> None: ...
    def _OpChain__reset(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, *args, **kwargs): ...
    @staticmethod
    def _applyOp(txnProxy: LiveRenderPortOpObserver._TransactionProxy, inputOp: PyFnGeolib.GeolibRuntimeOp, opType: str, opArgs: PyFnAttribute.GroupAttribute = ...) -> PyFnGeolib.GeolibRuntimeOp: ...
    def _checkAndUpdateDirtyState(self, args: tuple, kwargs: dict) -> bool: ...
    def _createOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, rootOp: PyFnGeolib.GeolibRuntimeOp, *args, **kwargs) -> PyFnGeolib.GeolibRuntimeOp: ...
    def applyOpChain(self, txnProxy: LiveRenderPortOpObserver._TransactionProxy, inputOp: PyFnGeolib.GeolibRuntimeOp, *args, **kwargs) -> PyFnGeolib.GeolibRuntimeOp: ...

class _OpPool:
    def __init__(self) -> None: ...
    def _release(self): ...

def _pairwise(iterable): ...
