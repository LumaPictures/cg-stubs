# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI_cmodule
import Nodes2DAPI_cmodule
from typing import Any, overload
from typing import List

NodeDehilightingModeConnected: int
NodeDehilightingModeContributing: int

def GetFontFile() -> str: ...
def angleVector2D(arg0: float, arg1: float, arg2: float, arg3: float) -> float: ...
def boundBoxBox(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> tuple: ...
def insideVector2DBox(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> bool: ...
def intersectBoxBox(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> tuple: ...
def intersectLineBox(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> tuple: ...
def intersectLines(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float) -> Any: ...
def lengthVector2D(arg0: float, arg1: float) -> float: ...
def nodeShape_clearAllHiddenPortLinks() -> None: ...
def nodeShape_setPortLinkHidden(srcPort: NodegraphAPI_cmodule.Port, dstPort: NodegraphAPI_cmodule.Port, hidden: bool = ...) -> None: ...
def nodeWorld_addNode(node: NodegraphAPI_cmodule.Node, p: List[tuple[float, float]]) -> None: ...
def nodeWorld_draw(viewRoot: NodegraphAPI_cmodule.GroupNode, x: float, y: float) -> None: ...
def nodeWorld_drawFloatingLink(viewRoot: NodegraphAPI_cmodule.GroupNode, port: NodegraphAPI_cmodule.Port, x: float, y: float, viewScale: float) -> None: ...
def nodeWorld_drawPreselect(viewRoot: NodegraphAPI_cmodule.GroupNode, x: float, y: float, l: float, b: float, r: float, t: float, viewScale: float) -> None: ...
def nodeWorld_drawSelectedLink(viewRoot: NodegraphAPI_cmodule.GroupNode, portA: NodegraphAPI_cmodule.Port, portB: NodegraphAPI_cmodule.Port, viewScale: float, dimHead: bool = ..., dimTail: bool = ...) -> None: ...
def nodeWorld_drawSelectedPort(viewRoot: NodegraphAPI_cmodule.GroupNode, port: NodegraphAPI_cmodule.Port, viewScale: float) -> None: ...
def nodeWorld_drawShadow(l: float, b: float, r: float, t: float, w: float, o: float) -> None: ...
def nodeWorld_drawText(text: str) -> None: ...
def nodeWorld_findGroupNodeOfClick(viewRoot: NodegraphAPI_cmodule.Node, x: float, y: float, viewScale: float) -> Any: ...
def nodeWorld_flowText(text: str, lineWidth: float) -> List[str]: ...
def nodeWorld_getBounds(node: NodegraphAPI_cmodule.Node, useBasicDisplay: bool = ..., includeThumbnail: bool = ..., addPadding: bool = ...) -> tuple: ...
def nodeWorld_getBoundsOfListOfNodes(nodes: List[NodegraphAPI_cmodule.Node], useBasicDisplay: bool = ..., addPadding: bool = ...) -> tuple: ...
def nodeWorld_getChildBounds(viewRoot: NodegraphAPI_cmodule.GroupNode) -> tuple: ...
def nodeWorld_getFloatingOffset() -> tuple: ...
def nodeWorld_getGroupNodeRelativeAndAbsoluteChildScales(viewRoot: NodegraphAPI_cmodule.GroupNode, group: NodegraphAPI_cmodule.GroupNode, viewScale: float, x: float, y: float) -> tuple: ...
def nodeWorld_getLinkEndPoints(viewRoot: NodegraphAPI_cmodule.GroupNode, portA: NodegraphAPI_cmodule.Port, portB: NodegraphAPI_cmodule.Port, viewScale: float) -> tuple: ...
def nodeWorld_getNodeDehilitingMode() -> int: ...
def nodeWorld_getPortPosition(port: NodegraphAPI_cmodule.Port, viewScale: float) -> tuple: ...
def nodeWorld_getShapeAttrAsNumber(node: NodegraphAPI_cmodule.Node, attr: str) -> Any: ...
def nodeWorld_getShapeAttrAsString(node: NodegraphAPI_cmodule.Node, attr: str) -> Any: ...
def nodeWorld_hitTestBox(viewRoot: NodegraphAPI_cmodule.GroupNode, l: float, b: float, r: float, t: float, viewScale: float) -> list: ...
def nodeWorld_hitTestInset(group: NodegraphAPI_cmodule.GroupNode, x: float, y: float, viewScale: float) -> Any: ...
def nodeWorld_hitTestNode(viewRoot: NodegraphAPI_cmodule.GroupNode, node: NodegraphAPI_cmodule.Node, x: float, y: float, viewScale: float) -> Any: ...
def nodeWorld_hitTestPoint(viewRoot: NodegraphAPI_cmodule.GroupNode, x: float, y: float, viewScale: float) -> list: ...
def nodeWorld_isLargePortAreaEnabled() -> bool: ...
def nodeWorld_loadSceneIntoNodegraphSvgManager(id: str, path: str, opacity: float = ...) -> None: ...
def nodeWorld_mapFromWorldPositionToCurrentGroupWorldPosition(viewRoot: NodegraphAPI_cmodule.GroupNode, node: NodegraphAPI_cmodule.Node, x: float, y: float, viewScale: float) -> list: ...
def nodeWorld_measureText(text: str) -> tuple: ...
def nodeWorld_moveNode(node: NodegraphAPI_cmodule.Node, p: List[tuple[float, float]]) -> None: ...
def nodeWorld_refreshAllViewMaskLinkColors() -> None: ...
def nodeWorld_refreshAllViewMasks() -> None: ...
def nodeWorld_refreshNodeViewMaskFlags(node: NodegraphAPI_cmodule.Node) -> None: ...
def nodeWorld_removeNode(node: NodegraphAPI_cmodule.Node) -> None: ...
def nodeWorld_sceneIsLoadedIntoNodegraphSvgManager(id: str) -> bool: ...
def nodeWorld_setExpressionLinksEnabled(arg0: bool) -> None: ...
def nodeWorld_setFloatingOffset(groupNode: NodegraphAPI_cmodule.GroupNode, node: NodegraphAPI_cmodule.Node, x: float, y: float, viewScale: float) -> None: ...
def nodeWorld_setLargePortAreaEnabled(enabled: bool) -> None: ...
def nodeWorld_setLargePortAreaIncludeTypes(includeInput: bool, includeOutput: bool) -> None: ...
def nodeWorld_setLowContrastLookEnabled(arg0: bool) -> None: ...
def nodeWorld_setNodeActive(node: NodegraphAPI_cmodule.Node) -> None: ...
def nodeWorld_setNodeDehilitingEnabled(arg0: bool) -> None: ...
def nodeWorld_setNodeDehilitingMode(arg0: int) -> None: ...
def nodeWorld_setNodeState(node: NodegraphAPI_cmodule.Node, viewed: bool, edited: bool, selected: bool, floating: bool) -> None: ...
def nodeWorld_setNodeThumbnail(node: NodegraphAPI_cmodule.Node, thumbnail: Nodes2DAPI_cmodule.IntImage) -> None: ...
def nodeWorld_setNodeThumbnailEnabled(node: NodegraphAPI_cmodule.Node, enabled: bool) -> None: ...
def nodeWorld_setParent(node: NodegraphAPI_cmodule.Node, oldParent: NodegraphAPI_cmodule.GroupNode) -> None: ...
@overload
def nodeWorld_setShapeAttr(node: NodegraphAPI_cmodule.Node, attr: str, value: str) -> None: ...
@overload
def nodeWorld_setShapeAttr(node: NodegraphAPI_cmodule.Node, attr: str, value: float) -> None: ...
def nodeWorld_setShowNodeIcons(show: bool) -> None: ...
def nodeWorld_setViewMasksEnabled(enabled: bool) -> None: ...
def nodeWorld_shouldLargePortAreaIncludeInputPorts() -> bool: ...
def nodeWorld_shouldLargePortAreaIncludeOutputPorts() -> bool: ...
def nodeWorld_tranformPointToChildSpace(group: NodegraphAPI_cmodule.GroupNode, x: float, y: float, viewScale: float) -> tuple: ...
def nodeWorld_updateNodeHiliteTableWithIncomingNodes(node: NodegraphAPI_cmodule.Node) -> None: ...
def normalizeVector2D(arg0: float, arg1: float) -> tuple: ...
def scaleBoxVector2D(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> tuple: ...
def translateBoxVector2D(arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float) -> tuple: ...