# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI as CatalogAPI
import CatalogAPI.Catalog
import LiveRenderOpChain as LiveRenderOpChain
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import PyFnAttribute
import PyFnGeolib
import RenderManager.RenderSettings
import Utils as Utils
from Callbacks.Callbacks import Callbacks as Callbacks
from Nodes3DAPI.PortOpClient import GraphStateSpec as GraphStateSpec, PortOpClient as PortOpClient
from PyUtilModule.RenderManager.Constants import RenderModes as RenderModes
from PyUtilModule.WorkingSetManager import WorkingSetManager as WorkingSetManager
from typing import Any, ClassVar

class LiveRenderPortOpObserver(PortOpClient):
    _abc_impl: ClassVar[_abc_data] = ...
    _kDynamicGSV: ClassVar[str] = ...
    _kRenderCancelledEvent: ClassVar[str] = ...
    _kRenderFinalizedEvent: ClassVar[str] = ...
    _kStaticGSV: ClassVar[str] = ...
    _kTerminalOpDirtyEvents: ClassVar[tuple] = ...
    _kUnregisterEventName: ClassVar[str] = ...
    _kVirtualCameraMoveEvent: ClassVar[str] = ...
    _observers: ClassVar[dict] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    def __init__(self, runtime: PyFnGeolib.GeolibRuntime, node: NodegraphAPI.Node, graphState: NodegraphAPI.GraphState, mainSequenceID: int, opChain: LiveRenderOpChain, liveAttributeQueue: LiveRenderOpChain.LiveAttributeQueue, renderingSettings: RenderManager.RenderSettings.RenderingSettings, projectSnapshot: ProjectSnapshot | None): ...
    def _LiveRenderPortOpObserver__commitGSVToGraphStateSpec(self, gsvID: str): ...
    def _LiveRenderPortOpObserver__copyGraphStateEntry(self, sourceGraphState: NodegraphAPI.GraphState, targetGraphStateBuilder: NodegraphAPI.GraphStateBuilder, variableName: str): ...
    def _LiveRenderPortOpObserver__encodeGSVNames(self, graphState: NodegraphAPI.GraphState) -> set[str]: ...
    @classmethod
    def _LiveRenderPortOpObserver__getGeolibServiceHostAndPort(cls, mainSequenceID): ...
    @classmethod
    def _LiveRenderPortOpObserver__onCatalogGSVPinned(cls, objectHash: object, catalogItem: CatalogAPI.Catalog.CatalogItem, gsvID: str, isPinned: bool): ...
    @classmethod
    def _LiveRenderPortOpObserver__onDirtyEvent(cls, args: tuple, kwargs: dict): ...
    def _LiveRenderPortOpObserver__onNodeDelete(self, eventType: str, eventID: int, **kwargs): ...
    @classmethod
    def _LiveRenderPortOpObserver__onRenderCancelled(cls, eventType: str, mainSequenceIDs: tuple[int, ...]): ...
    @classmethod
    def _LiveRenderPortOpObserver__onRenderFinalized(cls, eventType: str, eventID: int, renderMethod: str, runtime: PyFnGeolib.GeolibRuntime, node: NodegraphAPI.Node, graphState: NodegraphAPI.GraphState, renderUUID: str, renderer: str, renderingSettings: RenderManager.RenderSettings.RenderingSettings, projectSnapshot: ProjectSnapshot | None): ...
    @classmethod
    def _LiveRenderPortOpObserver__onUnregister(cls, eventType: str, eventID: int): ...
    @classmethod
    def _LiveRenderPortOpObserver__onVirtualCameraMoved(cls, eventType: str, eventID: object, attrName: str, attrValue: PyFnAttribute.Attribute, isFinal: bool): ...
    def _LiveRenderPortOpObserver__tryRegisterEventHandler(self, eventType, fn): ...
    def _LiveRenderPortOpObserver__tryUnregisterEventHandler(self, eventType, fn): ...
    def _LiveRenderPortOpObserver__unregister(self): ...
    def _LiveRenderPortOpObserver__updateCatalogItem(self, graphState: NodegraphAPI.GraphState): ...
    def addImmutableGraphStateVariable(self, variableName: str): ...
    def getImmutableGraphStateVariables(self) -> set[str]: ...
    def getOp(self, node: NodegraphAPI.Node, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState, visitedState: set, txn: PyFnGeolib.GeolibRuntimeTransaction) -> PyFnGeolib.GeolibRuntimeOp: ...
    def getTxnQueue(self) -> OpTreeCommandRequestQueue: ...
    def modifyInitialGraphState(self, graphState: NodegraphAPI.GraphState) -> NodegraphAPI.GraphState: ...
    def opChanged(self, op: PyFnGeolib.GeolibRuntimeOp, graphState: NodegraphAPI.GraphState, txn: PyFnGeolib.GeolibRuntimeTransaction): ...
    @classmethod
    def queueLiveAttribute(cls, locationPath: str, attrPath: str, attrValue: str, attrEditor: PyFnAttribute.GroupAttribute | None): ...
    @classmethod
    def registerEvents(cls): ...
    @classmethod
    def registerLiveRender(cls, runtime: PyFnGeolib.GeolibRuntime, node: NodegraphAPI.Node, graphState: NodegraphAPI.GraphState, mainSequenceID: int, renderUUID: str, renderingSettings: RenderManager.RenderSettings.RenderingSettings, projectSnapshot: ProjectSnapshot | None) -> LiveRenderPortOpObserver: ...
    def removeImmutableGraphStateVariable(self, variableName: str): ...
    @classmethod
    def unregisterEvents(cls): ...
    @classmethod
    def unregisterLiveRender(cls, mainSequenceID: int): ...
    @property
    def mainSequenceID(self) -> Any: ...

class _RemoteGeolibUnavailableError(Exception): ...

class _RemoteRenderSpoolingError(Exception): ...

class _TransactionProxy:
    def __init__(self, txn: PyFnGeolib.GeolibRuntimeTransaction, txnAdaptor: OpTreeCommandRequestTransactionAdaptor): ...
    def createOp(self) -> PyFnGeolib.GeolibRuntimeOp: ...
    def localOnly(self) -> None: ...
    def setClientOp(self, client: PyFnGeolib.GeolibRuntimeClient, op: PyFnGeolib.GeolibRuntimeOp): ...
    def setNodeName(self, op: PyFnGeolib.GeolibRuntimeOp, name: str): ...
    def setNodeType(self, op: PyFnGeolib.GeolibRuntimeOp, nodeType: str): ...
    def setOpArgs(self, op: PyFnGeolib.GeolibRuntimeOp, opType: str, args: PyFnAttribute.GroupAttribute): ...
    def setOpInputs(self, op: PyFnGeolib.GeolibRuntimeOp, inputOps: list[PyFnGeolib.GeolibRuntimeOp]): ...
    def setTag(self, op: PyFnGeolib.GeolibRuntimeOp, tag: str): ...
    def useOpPool(self, opPool: LiveRenderOpChain._OpPool) -> None: ...
    def __getattr__(self, item: str) -> Any: ...
    @property
    def localTransaction(self) -> Any: ...
    @property
    def remoteTransaction(self) -> Any: ...