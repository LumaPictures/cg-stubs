# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Callbacks as Callbacks
import ConfigurationAPI_cmodule as Configuration
import Utils.EventModule as EventModule
import FnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import FnGeolibProducers as FnGeolibProducers
import Nodes3DAPI.Node3DEventTypes as Node3DEventTypes
import Nodes3DAPI.Node3D_geolib3 as Node3D_geolib3
import NodegraphAPI as NodegraphAPI
import NodegraphAPI_cmodule
import Nodes2DAPI as Nodes2DAPI
import Nodes3DAPI.Node3D_geolib3
import PyFnAttribute
import PyFnGeolib
import RenderingAPI as RenderingAPI
import Utils as Utils
from Nodes3DAPI.IncomingSceneOpDelegates import IncomingSceneOpDelegate as IncomingSceneOpDelegate, OutgoingAttributesDelegate as OutgoingAttributesDelegate, RegisterIncomingSceneOpDelegate as RegisterIncomingSceneOpDelegate, RegisterOutgoingAttributesDelegate as RegisterOutgoingAttributesDelegate
from Nodes3DAPI.Node3D_geolib3 import ActivatePort as ActivatePort, CommitChanges as CommitChanges, DeactivatePort as DeactivatePort, GetDefaultSourceOp as GetDefaultSourceOp, GetRuntime as GetRuntime, IsProcessing as IsProcessing, ManualUpdate as ManualUpdate, MarkPortOpClientDirty as MarkPortOpClientDirty, RegisterCommitIdCallback as RegisterCommitIdCallback, RegisterPortOpClient as RegisterPortOpClient, UnregisterPortOpClient as UnregisterPortOpClient, UpdatePortOpClients as UpdatePortOpClients
from Nodes3DAPI.NodeTypeBuilder import NodeTypeBuilder as NodeTypeBuilder
from Nodes3DAPI.OpCacheManager import OpCacheManager as OpCacheManager, g_opCacheManager as g_opCacheManager
from Nodes3DAPI.ScenegraphMask import GetScenegraphMaskEnabled as GetScenegraphMaskEnabled, GetScenegraphMaskLocationsAndRoot as GetScenegraphMaskLocationsAndRoot, GetVisibilityFollowsWorkingSet as GetVisibilityFollowsWorkingSet
from Nodes3DAPI.TerminalOpDelegates.TerminalOpDelegate import TerminalOpDelegate
from PyUtilModule.WorkingSetManager import WorkingSetManager as WorkingSetManager
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ImplicitResolverStage:
    AfterLookFileResolvePostprocessResolver: ClassVar[int] = ...
    AfterPostprocessResolvers: ClassVar[int] = ...
    AfterStandardResolvers: ClassVar[int] = ...
    AfterViewerResolvers: ClassVar[int] = ...
    BeforeLookFileResolvePostprocessResolver: ClassVar[int] = ...
    BeforePreprocessResolvers: ClassVar[int] = ...
    BeforeStandardResolvers: ClassVar[int] = ...
    BeforeViewerResolvers: ClassVar[int] = ...

class Node3D(NodegraphAPI_cmodule.PythonNode, Nodes3DAPI.Node3D_geolib3.NodeGeolib3):
    def __init__(self) -> None: ...
    def _getInvalidConnectionsErrorMessage(self, errorMessages): ...
    def getAll3DInputs(self, graphState): ...
    def getPortsWithInvalidConnections(self, errorMessages: Incomplete | None = ...): ...
    def require3DInput(self, portName, graphState): ...
    def validateConnection(self, otherOutPort, myInPort, errorMessages: Incomplete | None = ...): ...

def ApplyImplicitResolverOps(txn, op, node, graphState: Incomplete | None = ..., extraOpArgsByOpType: Incomplete | None = ...): ...
def ApplyOp(txn, inputOp, opType, opArgs: Incomplete | None = ...): ...
def ApplyRenderSettingsToGraphState(renderSettingsAttr: FnAttribute.GroupAttribute, graphState: NodegraphAPI.GraphState, renderUUID: Incomplete | None = ...) -> NodegraphAPI.GraphState: ...
def CreateClient(node, graphState: Incomplete | None = ..., portIndex: int = ...): ...
def Get3DPortFromNode(node, graphState: Incomplete | None = ..., portIndex: int = ...): ...
def Get3DSourceFromNodeInput(node: NodegraphAPI.Node, inputPortName: str, graphState: NodegraphAPI.GraphState) -> NodegraphAPI.Port | None: ...
def GetExtraParameterValueSourceNodePorts(node: NodegraphAPI.Node) -> list[NodegraphAPI.Port]: ...
def GetExtraParameterValueSourceNodes(node: NodegraphAPI.Node) -> list[NodegraphAPI.Node]: ...
def GetGeometryProducer(node: Incomplete | None = ..., graphState: Incomplete | None = ..., portIndex: int = ...) -> FnGeolibProducers.GeometryProducer | None: ...
def GetOp(txn, node: NodegraphAPI.Node, graphState: Incomplete | None = ..., portIndex: int = ..., applyTerminalOpDelegates: bool = ...): ...
def GetOpChain(txn, node, graphState: Incomplete | None = ..., portIndex: int = ...): ...
def GetRegisteredImplicitResolvers(stage): ...
def GetRegisteredTerminalOpDelegate(name: str) -> TerminalOpDelegate: ...
def GetRegisteredTerminalOpDelegateNames() -> list[str]: ...
def GetRenderOp(txn, node, graphState: Incomplete | None = ..., portIndex: int = ..., useMaxSamples: bool = ..., applyRenderSelectedMask: bool = ..., update3DNodes: bool = ..., visitedState: Incomplete | None = ..., runtime: Incomplete | None = ..., renderUUID: Incomplete | None = ...): ...
def GetRenderProducer(node: Incomplete | None = ..., graphState: Incomplete | None = ..., useMaxSamples: bool = ..., portIndex: int = ..., applyRenderSelectedMask: bool = ...) -> FnGeolibProducers.GeometryProducer | None: ...
def GetRenderTerminalOpSpecs(rendererName: str, renderMethodType: str, graphState: NodegraphAPI.GraphState) -> list[tuple[str, PyFnAttribute.GroupAttribute]]: ...
def GetRenderTerminalOps(txn: PyFnGeolib.GeolibRuntimeTransaction, rendererName: str, renderMethodType: str, graphState: Incomplete | None = ...) -> list[PyFnGeolib.GeolibRuntimeOp]: ...
def GetRenderThreads(): ...
def RegisterImplicitResolver(stage, opType, opArgs, addSystemArgs: bool = ...): ...
def RegisterTerminalOpDelegate(name: str, terminalOpDelegate: TerminalOpDelegate): ...
def SetExtraParameterValueSourceNodes(node: NodegraphAPI.Node, sourceNodes: list[NodegraphAPI.Node]): ...
def SetRenderThreads(numThreads): ...
def UnregisterTerminalOpDelegate(name: str): ...
