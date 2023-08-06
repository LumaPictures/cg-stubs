# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI as CatalogAPI
import ConfigurationAPI_cmodule as Configuration
import PyFnGeolib as FnGeolib
import PyFnGeolibProducers as FnGeolibProducers
import PyUtilModule.RenderManager.InteractiveRenderDelegateManager as InteractiveRenderDelegateManager
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Nodes3DAPI as Nodes3DAPI
import PyUtilModule.ProjectSnapshot as ProjectSnapshot
import PyUtilModule.RenderManager.RenderGlobals as RenderGlobals
import RenderingAPI as RenderingAPI
import PyUtilModule.RenderingCommon as RenderingCommon
import Utils as Utils
import typing
from PyUtilModule.RenderManager.Constants import RenderModes as RenderModes
from PyUtilModule.RenderManager.Exceptions import RenderingException as RenderingException, UnsupportedRenderMethodNameException as UnsupportedRenderMethodNameException
from PyUtilModule.RenderManager.NodegraphUtils import ApplyInteractiveRenderDelegates as ApplyInteractiveRenderDelegates, BuildRenderPortsAndGraphStatesList as BuildRenderPortsAndGraphStatesList, CollapseNodesAndPorts as CollapseNodesAndPorts, CreateRenderNodeParameters as CreateRenderNodeParameters, DisableKatanaNodeGraphEventProcessing as DisableKatanaNodeGraphEventProcessing, GetSourcePortsAndNamesFromLists as GetSourcePortsAndNamesFromLists, IsScriptRender as IsScriptRender, NotifyIfInteractiveRerender as NotifyIfInteractiveRerender
from PyUtilModule.RenderManager.RenderSettings import CheckGlobalSettings as CheckGlobalSettings, GetRendererAndSettings as GetRendererAndSettings, RenderingSettings as RenderingSettings
from PyUtilModule.RenderManager.ResolutionTableUtils import GetTempResolutionTablePath as GetTempResolutionTablePath, SaveResolutionTables as SaveResolutionTables
from PyUtilModule.RenderManager.ScenegraphUtils import AddCameraOverrideToRecipe as AddCameraOverrideToRecipe, AddRenderOutputsToRecipe as AddRenderOutputsToRecipe, AddRenderSettingsToRecipe as AddRenderSettingsToRecipe, AddVirtualCameraToRecipe as AddVirtualCameraToRecipe, BakeAOVs as BakeAOVs, GetInteractiveOutputs as GetInteractiveOutputs
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import Set, Tuple

class RenderComponents:
    def __init__(self) -> None: ...

def CancelRender(stallOnCompletion: bool = ..., mainSequenceID: int = ..., **kwargs): ...
def CancelRendersByType(renderType: int, stallOnCompletion: bool = ..., predicate: Incomplete | None = ...): ...
def StartRender(renderMethodName: str, node: typing.Optional[NodegraphAPI.Node] = ..., port: typing.Optional[NodegraphAPI.Port] = ..., nodeList: Incomplete | None = ..., portList: Incomplete | None = ..., serialDiskRenderNodeList: Incomplete | None = ..., views: Incomplete | None = ..., settings: Incomplete | None = ..., **kwargs) -> list[dict]: ...
def StartRenderLegacy(node: typing.Optional[NodegraphAPI.Node] = ..., port: typing.Optional[NodegraphAPI.Port] = ..., nodeList: Incomplete | None = ..., portList: Incomplete | None = ..., serialHotrenderNodeList: Incomplete | None = ..., views: Incomplete | None = ..., saveRenderXML: bool = ..., hotRender: bool = ..., ROI: Incomplete | None = ..., ignoreROI: bool = ..., overscanPadding: Incomplete | None = ..., sampleRate: Incomplete | None = ..., frame: Incomplete | None = ..., interactive: bool = ..., useID: Incomplete | None = ..., interactiveOutputs: Incomplete | None = ..., emitTileRenderOrdering: bool = ..., diskCachingAllowed: Incomplete | None = ..., tilePrioritizer: Incomplete | None = ..., buffer2DAutoLock: Incomplete | None = ..., interactiveRenderMask: Incomplete | None = ..., createCatalogItem: Incomplete | None = ..., asynch: bool = ..., asynch_renderMessageCB: Incomplete | None = ..., asynch_renderProgressCB: Incomplete | None = ..., serialHotrender_progressCB: Incomplete | None = ..., render_completionCB: Incomplete | None = ..., renderMethodName: Incomplete | None = ...): ...
