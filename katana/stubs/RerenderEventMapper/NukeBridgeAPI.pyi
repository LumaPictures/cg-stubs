# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI as CatalogAPI
import ConfigurationAPI_cmodule as Configuration
import NodegraphAPI as NodegraphAPI
import RerenderEventMapper.NukeSessionMonitor as NukeSessionMonitor
import RenderingAPI as RenderingAPI
import Utils as Utils
from PyUtilModule.VirtualKatana import RenderManager as RenderManager
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

RENDER_NODE_NAME: str
g_nukeConfigurationError: None
g_nukeConfigured: None
g_nukeConfiguredVersion: None
g_nukeRenderNode: None

class CompTypes:
    INTERACTIVE_COMP: ClassVar[str] = ...
    LIVE_COMP: ClassVar[str] = ...
    PREVIEW_COMP: ClassVar[str] = ...

def GetCatalogItemLabel(catalogItem: CatalogAPI.CatalogItem) -> str: ...
def GetCurrentKatanaReaderNodesMapping() -> dict[str, str]: ...
def GetCurrentKatanaWriterNodeName() -> str: ...
def GetKatanaReaderNodeNames() -> list[str]: ...
def GetKatanaWriterNodeNames() -> list[str]: ...
def GetLastNukeScriptPath() -> str: ...
def GetNukeBridgeConfigurationError() -> str | None: ...
def GetNukeBridgeConfiguredVersion() -> str | None: ...
def GetNukeBridgeRenderNode() -> NodegraphAPI.Node: ...
def GetRootNukeMappingParam(): ...
def GetRootNukeOutputParam(): ...
def GetRootNukeParam(): ...
def GetRootNukeScriptParam(): ...
def GetRootNukeSessionParam(): ...
def GetSupportedNukeVersions() -> tuple[str, ...]: ...
def InitializeNukeBridge() -> bool: ...
def IsNukeBridgeConfigured() -> bool: ...
def IsNukeBridgeSession(catalogItem: CatalogAPI.CatalogItem) -> bool: ...
def LoadNukeScript(nukeScriptPath: str, inProgressHandler: Incomplete | None = ..., onErrorCallback: Incomplete | None = ...) -> bool: ...
def ParseCatalogItemLabel(label: str) -> str: ...
def SetCurrentKatanaReaderNodesMapping(mapping: dict[str, str]): ...
def SetCurrentKatanaWriterNodeName(nodeName: str): ...
def StartComp(compType: str, renderFarmName: Incomplete | None = ...): ...
def _BuildNukeBridgeNodeNetwork() -> NodegraphAPI.Node: ...
def _ConfigureNukeBridge(): ...
def _ResetKatanaNodeNames(katanaNodes: dict): ...
def _RunCommand(commandArguments: list[str], inProgressHandler: Incomplete | None = ...): ...
def _WriteOrGetTempGetKatanaNodesScriptPath() -> str: ...
