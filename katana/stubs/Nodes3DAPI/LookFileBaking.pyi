# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Callbacks as Callbacks
import ConfigurationAPI_cmodule as Configuration
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import FnGeolibProducers
import GeoAPI.Util.LookFileUtil as LegacyLookFileUtil
import LookFileBakeAPI as LookFileBakeAPI
import LookFileBakeAPI.LookFileBaker
import Nodes3DAPI.Node3D as Node3D
import NodegraphAPI as NodegraphAPI
import PyFnGeolib
import typing
from _typeshed import Incomplete
from typing import Set, Tuple

class PostLookFileBakeHandler(_PrePostLookFileBakeCallbackForwarder):
    def __init__(self, node: Incomplete | None = ...) -> None: ...

class PreLookFileBakeHandler(_PrePostLookFileBakeCallbackForwarder):
    def __init__(self, node: Incomplete | None = ...) -> None: ...

class _PrePostLookFileBakeCallbackForwarder(LookFileBakeAPI.LookFileBaker.BakePrePostHandlerBase):
    callback: Incomplete
    node: Incomplete
    def __init__(self, node: Incomplete | None = ...) -> None: ...
    def notify(self, assetId: str, rootLocationProducers: dict[str, FnGeolibProducers.GeometryProducer], progressCallback: typing.Callable | None, abortCallback: typing.Callable | None): ...

def BakingContext(): ...
def GetBakeState() -> bool: ...
def GetGlobalBakeState() -> bool: ...
def GetLocationIntervalEvictor(node: Incomplete | None = ..., intervalParameterName: str = ..., configVarName: str = ...) -> LocationIntervalEvictor | None: ...
def GetLookFileBakeOp(node: NodegraphAPI.Node, inputPortName: str, graphState: typing.Optional[Nodegraph], txn: PyFnGeolib.GeolibRuntime.Transaction | None) -> PyFnGeolib.GeolibRuntime.Op | None: ...
def GetLookFileBakeOps(node: NodegraphAPI.Node, inputPortNames: Sequence[str], graphState: typing.Optional[Nodegraph], txn: Incomplete | None = ...) -> list[PyFnGeolib.GeolibRuntime.Op | None]: ...
def PostLookFileBake(node: NodegraphAPI.Node | None, assetId: str, rootLocationProducers: dict[str, FnGeolibProducers.GeometryProducer], progressCallback: typing.Callable | None, abortCallback: typing.Callable | None): ...
def PreLookFileBake(node: NodegraphAPI.Node | None, assetId: str, rootLocationProducers: dict[str, FnGeolibProducers.GeometryProducer], progressCallback: typing.Callable | None, abortCallback: typing.Callable | None): ...
def ValidateGraphState(graphStateOrTime: typing.Optional[Nodegraph]) -> NodegraphAPI.GraphState: ...
