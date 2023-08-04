# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import PyFnAttribute as FnAttribute
import GeolibRuntime
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Nodes3DAPI as Nodes3DAPI
import PyUtilModule.ProjectSnapshot as ProjectSnapshot
import PyUtilModule.RenderManager.RenderGlobals as RenderGlobals
import RenderingAPI as RenderingAPI
from PyUtilModule.RenderManager.Constants import RenderModes as RenderModes
from PyUtilModule.RenderManager.Exceptions import UnsupportedRenderMethodNameException as UnsupportedRenderMethodNameException
from typing import ClassVar, Set, Tuple

class RenderingSettings:
    kOpTreeExportPass: ClassVar[int] = ...
    kOpTreeRenderPass: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def setDefaults(self): ...

def CheckGlobalSettings(settings): ...
def GetRendererAndSettings(settings: RenderingSettings, renderMethodName: str, renderOpNode: NodegraphAPI.Node, runtime: GeolibRuntime, txn: GeolibRuntimeTransaction, client: GeolibRuntime.Client) -> tuple[str, str, GeolibRuntimeOp]: ...
