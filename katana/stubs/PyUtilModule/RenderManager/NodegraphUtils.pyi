# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyUtilModule.RenderManager.InteractiveRenderDelegateManager as InteractiveRenderDelegateManager
import NodegraphAPI as NodegraphAPI
import PyUtilModule.RenderManager.RenderGlobals as RenderGlobals
import Utils as Utils
from PyUtilModule.RenderManager.Constants import RenderModes as RenderModes
from PyUtilModule.RenderManager.Exceptions import RenderingException as RenderingException

def ApplyInteractiveRenderDelegates(renderPort: NodegraphAPI.Port): ...
def BuildRenderPortsAndGraphStatesList(settings: RenderingSettings, sourcePorts: list[int | str], sourceNodes: NodegraphAPI.Node) -> list[NodegraphAPI.Port]: ...
def CollapseNodesAndPorts(node, port, nodeList, portList): ...
def CreateRenderNodeParameters(node: NodegraphAPI.Node, settings: RenderingSettings, renderComponents: RenderComponents) -> list[NodegraphAPI.Parameter]: ...
def DisableKatanaNodeGraphEventProcessing(): ...
def DisconnectInteractiveRenderDelegates(renderPort: NodegraphAPI.Port, blindData: dict): ...
def GetSourcePortsAndNamesFromLists(nodeList: list[NodegraphAPI.Node | str], portList: list[str], renderMethodType: str) -> list[None]: ...
def InteractiveRenderDelegatesApplied(renderPort: NodegraphAPI.Port) -> NodegraphAPI.Port: ...
def IsScriptRender(renderPortsAndGraphStates: list[NodegraphAPI.Port]) -> bool: ...
def NotifyIfInteractiveRerender(renderAction, nodeList): ...
def _FilterAllNodeGraphEvents(eventType, eventID, *args, **kwargs): ...