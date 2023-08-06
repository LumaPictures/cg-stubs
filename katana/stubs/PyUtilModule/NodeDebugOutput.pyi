# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyUtilModule.EnvUtils as EnvUtils
import Utils.EventModule as EventModule
import PyFnGeolib as FnGeolib
import GeoAPI as GeoAPI
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import PyUtilModule.RenderManager as RenderManager
import RenderingAPI as RenderingAPI
import Utils as Utils
from _typeshed import Incomplete
from typing import Set, Tuple

def CanPrintDebugOutput() -> bool: ...
def WriteRenderDebug(node: NodegraphAPI.Node, renderer, filename: Incomplete | None = ..., expandProcedural: bool = ..., openInEditor: bool = ..., customEditor: Incomplete | None = ..., log: Incomplete | None = ...): ...
def WriteRenderOutput(node: NodegraphAPI.Node, renderer, filename: Incomplete | None = ..., expandProcedural: bool = ..., openInEditor: bool = ..., customEditor: Incomplete | None = ..., log: Incomplete | None = ...): ...
def WriteRenderOutputForRenderMethod(renderMethodName, node: NodegraphAPI.Node, renderer, filename: Incomplete | None = ..., expandProcedural: bool = ..., log: Incomplete | None = ..., openInEditor: bool = ..., customEditor: Incomplete | None = ..., sceneGraphPath: Incomplete | None = ..., printToConsole: bool = ...): ...
def WriteSerializedOpTreeToDisk(node: NodegraphAPI.Node, applyRenderResolvers, log: Incomplete | None = ...): ...
