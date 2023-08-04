# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Callbacks as Callbacks
import CatalogAPI as CatalogAPI
import ConfigurationAPI_cmodule as Configuration
import Utils.EventModule as EventModule
import FnAttribute as FnAttribute
import FnGeolib as FnGeolib
import FnGeolib.GeolibRuntime
import PyFnGeolibServices as FnGeolibServices
import GeoAPI as GeoAPI
import PyUtilModule.LiveRenderAPI as LiveRenderAPI
import RerenderEventMapper.LiveRenderPortOpObserver as LiveRenderPortOpObserver
import Nodes3DAPI.Node3D_geolib3 as Node3D_geolib3
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Nodes3DAPI as Nodes3DAPI
import PyQt5.QtCore as QtCore
import PyUtilModule.RenderManager.RenderCore as RenderCore
import PyUtilModule.RenderManager.RenderGlobals as RenderGlobals
import PyUtilModule.RenderManager as RenderManager
import RenderingAPI as RenderingAPI
import PyUtilModule.RenderingCommon as RenderingCommon
import Nodes3DAPI.UpdateModes as UpdateModes
import Utils as Utils
import collections
from PyUtilModule.WorkingSet import WorkingSet as WorkingSet, __renderWorkingSet as __renderWorkingSet, __workingSet as __workingSet
from PyUtilModule.WorkingSetClient import WorkingSetClient as WorkingSetClient
from PyUtilModule.WorkingSetManager import WorkingSetManager as WorkingSetManager
from _typeshed import Incomplete
from typing import Any, Set, Tuple

ForesightPlusEnabled: bool
__allowFollowRenderWorkingSet: bool
__areEventHandlersRegistered: bool
__areIRFsOpsDirty: bool
__cachedViewerMatrixArgs: None
__client: None
__cookedInitialLocations: set
__deferredLocationEvents: dict
__hadManualUpdateEvent: bool
__initialStateClient: None
__initialStateRuntime: None
__inputOpToLiveRenderOpChain: None
__interactiveRenderFiltersPorts: list
__irfPort: None
__liveAttributeWorker: None
__liveRenderDeferredRemovalTerminalOps: list
__liveRenderTerminalOps: dict
__locAttrHashCache: collections.defaultdict
__locationTypeCache: collections.defaultdict
__oldLightList: None
__pruneOpChain: None
__queuedUpdates: collections.deque
__renderOp: None
__renderPort: None
__runtime: None
__sendFullUpdateForNewLocation: bool
__terminalOpDelegatesRootOp: None
__terminalOps: list
__terminalOpsRootOp: None
__viewedGraphStateHash: None
__virtualCameraSSCOp: None
kVirtualCameraSceneGraphLocation: str

class LiveAttributeWorker:
    def __init__(self, runtime, client: Incomplete | None = ...) -> None: ...
    def applyQueuedAttributeChanges(self): ...
    def canApplyUpdate(self) -> bool: ...
    def getLiveAttributeOp(self) -> FnGeolib.GeolibRuntime.Op: ...
    def queueLiveAttribute(self, locationPath, attrValue, attrPath: str = ...): ...
    def setClient(self, client: FnGeolib.GeolibRuntime.client): ...
    def setLiveAttributeOp(self, liveAttrOp: FnGeolib.GeolibRuntime.Op): ...

def AddSettingsToRerenderRecipe(): ...
def ApplyTerminalOpDelegates(inputOp: FnGeolib.GeolibRuntime.Op, txn: transaction): ...
def CheckLiveRenderSettings(attributes: FnAttribute.GroupAttribute): ...
def CheckOutputsRenderSettings(attributes: FnAttribute.GroupAttribute, mainSequenceID: Incomplete | None = ...): ...
def GetAppliedTerminalOps() -> list[tuple[Any, str, FnAttribute.GroupAttribute]]: ...
def GetChangedAttributes(locationPath: str, locationAttrs: FnAttribute, locationType: str, sendFullUpdate: bool = ...): ...
def GetDefaultTerminalOps(txn: transaction, opInput) -> list[FnGeolib.GeolibRuntime.Op]: ...
def GetDeletedLocationsUpdate(deletedLocations: list[str]) -> FnAttribute.GroupAttribute: ...
def GetInteractiveRenderFiltersOps(opInput: FnGeolib.GeolibRuntime.Op, activatePorts: bool = ...) -> list[FnGeolib.GeolibRuntime.Op]: ...
def GetLightListChanges(location: str, locationAttrs): ...
def GetLiveRenderNodeAndPort() -> Tuple[Node3D, port]: ...
def GetRenderCameraChanges(location: str, locationAttrs: FnAttribute.GroupAttribute): ...
def GetWatchedAttributeGroups(liveRenderAttrs: FnAttribute.GroupAttribute) -> dict: ...
def GetWatchedAttributes(attrToWatch: FnAttribute.GroupAttribute, prefix: str = ...) -> list: ...
def HasHashChanged(locationPath, attrName: str, newAttr: FnAttribute) -> bool: ...
def InitializeGeolib3Client(): ...
def OnCancelled(): ...
def OnCompleted(): ...
def OnErrored(): ...
def OnIdle(): ...
def OnLiveRenderClearAllTerminalOps(eventType, eventID): ...
def OnLiveRenderInsertTerminalOp(eventType: str, eventID: object, opKey: Incomplete | None = ..., opType: str = ..., opArgs: Incomplete | None = ..., insertIndex: Incomplete | None = ...): ...
def OnLiveRenderRemoveTerminalOp(eventType: str, eventID: object, opKey: Incomplete | None = ..., deferred: bool = ...): ...
def OnLiveRenderRestoreDefaultTerminalOps(eventType, eventID): ...
def OnManualUpdate(eventType: str, eventID: object, updateMode: Incomplete | None = ...): ...
def OnNodeDeleted(eventType: str, eventID: object, node: NodegraphAPI.Node, oldName: str): ...
def OnNodeRenamed(eventType: str, eventID: object, node: NodegraphAPI.Node, oldName: str, newName: str): ...
def OnNodeSetBypassed(eventType, eventID, node, **kwargs): ...
def OnParameterFinalize(eventType, eventID, param, **kwargs): ...
def OnRerenderCameraChanged(eventType: str, eventID: object, cameraType: Incomplete | None = ..., cameraPath: Incomplete | None = ...): ...
def OnRoiChanged(): ...
def OnSendCommand(): ...
def OnSendData(): ...
def OnSetCurrentTime(eventType: str, eventID: object): ...
def OnStarted(): ...
def OnStop(): ...
def OnStopped(sequenceIDs): ...
def OnUpdate(): ...
def OnUpdateModeChanged(eventType: str, eventID: object, updateMode: Incomplete | None = ...): ...
def OnViewMatrixChanged(): ...
def OnViewerLiveAttributeChanged(eventType: str, eventID: object, locationPath: str, attrPath: str, attrValue: FnAttribute.Attribute): ...
def OnVisibilityFollowsWorkingSetChanged(eventType, eventID, visibilityFollowsWorkingSet): ...
def QueueRenderSettingsSequenceIDMapAttributeUpdate(mainSequenceIDs: list[int]): ...
def SetLiveAttribute(locationPath: str, attrPath: str, attrValue: FnAttribute.Attribute, attrEditor: Incomplete | None = ...): ...
def SetVirtualCameraAttributes(attributes: FnAttribute.Attribute): ...
def StartGeolib3Listening(): ...
def StopGeolib3Listening(): ...
def StopRerender(): ...
def UnregisterEventHandlers(): ...
def _GetGeolibServiceHostAndPort(mainSequenceID): ...
def _SendForesightCommand(mainSequenceID, command): ...
def _UpdateVirtualCameraSSCOpArgs(txn): ...
def __RemoveDeferredTerminalOps(): ...
def __RemoveTerminalOp(opKey: object): ...
def __createPruneOpChain(txn): ...
def __createRenderWorkingSetResolveOp(txn): ...
def __createRenderWorkingSetSetupOp(txn): ...
def __deferUntilOriginalLocationCooked(location: str) -> bool: ...
def __emitCachedViewMatrixChanged(): ...
def __getIRFsOpAndPorts(sourceGraphState: Incomplete | None = ...): ...
def __interactiveRenderFilterOpCallback(port, graphState, op, transaction): ...
def __interactiveRenderFiltersGetOpFunction(sourceNode, sourcePort, sourceGraphState, visitedState, txn): ...
def __processInitialStateEvents() -> list[LocationEvent]: ...
def __registerEventHandlers(rerenderNodeName): ...
def __setPruneOpChainInputOpArgs(): ...
def __terminalOpCallback(port, graphState, op, transaction): ...
def __unregisterEventHandlers(): ...
def changeVisibilityFollowsWorkingSet(visibilityFollowsWorkingSet): ...
def getImplicitTerminalOps(txn: transaction, opInput: FnGeolib.GeolibRuntime.Op, renderNode: NodegraphAPI.Node) -> list[FnGeolib.GeolibRuntime.Op]: ...
def liveRenderWorkingSetClearedCallback(workingSet): ...
