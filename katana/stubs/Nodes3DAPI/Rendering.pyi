# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import Callbacks as Callbacks
import ConfigurationAPI_cmodule as Configuration
import PyFnAttribute as FnAttribute
import Nodes3DAPI.Node3D as Node3D
import Nodes2DAPI as Nodes2DAPI
import PyFnGeolibProducers
import RenderingAPI as RenderingAPI
import Nodes3DAPI.RenderingUtil as RenderingUtil
import Utils as Utils
from _typeshed import Incomplete
from typing import Set, Tuple

def CancelAllRenders(waitOnCompletion: bool = ..., predicate: Incomplete | None = ...): ...
def CancelRender(mainSequenceID: int, waitOnCompletion: bool = ..., predicate: Incomplete | None = ...): ...
def GetRenderCommandLine(renderer: str, renderMethodType: str, renderMethodName: str, renderTime: float, geolib3OpTreeFilename: str, frameRanges: str, useID: bool, mainSequenceID: Incomplete | None = ..., debugOutputFilename: Incomplete | None = ..., expandProcedural: bool = ..., renderSettings: Incomplete | None = ..., enableRuntimeProfiling: bool = ..., **kwargs) -> str: ...
def RenderNode3D(producer: PyFnGeolibProducers.GeometryProducer, sampleRate: tuple[float, ...], regionOfInterest, renderNodeName: str, renderTime: float, mainSequenceID: int, useID: bool, geolib3OpTreeFilename: str, frameRanges: str, renderMethodType: Incomplete | None = ..., renderMethodName: Incomplete | None = ..., registerRender: bool = ..., reportRenderMessages: bool = ..., debugOutputFilename: Incomplete | None = ..., expandProcedural: bool = ..., rendererOverride: Incomplete | None = ..., enableRuntimeProfiling: bool = ..., remoteRender: bool = ..., renderFarm: Incomplete | None = ...) -> None: ...
def SignalRender(mainSequenceID, signal): ...
