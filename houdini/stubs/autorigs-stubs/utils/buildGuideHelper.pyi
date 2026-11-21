import collections
import hou
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from past.utils import old_div as old_div
from typing import Any

from typing import TypeAlias
from typing import TypeAlias
_NodesData: TypeAlias = Mapping[str, Sequence[Any] | dict[str, Any]]
_GuideNames: TypeAlias = collections.OrderedDict[str, 'str | _GuideNames']
def setPosition(node: hou.OpNode, xyztuple: Sequence[float]) -> None: ...
def setRotation(node: hou.OpNode, xyztuple: Sequence[float]) -> None: ...
def setModuleParmTuple(module: hou.OpNode, parm: str, xyztuple: Sequence[float]) -> None: ...
def makeReferenceCopy(node: hou.OpNode, copyname: str, display: bool = False, parent: hou.OpNode | None = None) -> hou.ObjNode: ...
def mirrorNodes(src_list: Iterable[hou.OpNode], dest_list: Sequence[hou.ObjNode]) -> None:
    """Mirror all the src nodes in a list"""
def mirrorNode(src: hou.OpNode, dest: hou.ObjNode, display: bool = False) -> None:
    """Mirror the src node on to the dest node
        src: source node
        dest: mirrored node
        display: whether to display the mirrored node
    """
def createAndMirrorNode(node: hou.OpNode, copyname: str, display: bool = False, parent: hou.OpNode | None = None) -> hou.ObjNode:
    """Copy and mirror the given node"""
def makeTransformParamReferences(node: hou.OpNode, newnode: hou.OpNode) -> None:
    """Set mirrored transform references for the newnode"""
def mirrorParamReferences(node: hou.OpNode, newnode: hou.OpNode, params: Iterable[str]) -> None:
    """Set mirrored param references for the newnode"""
def clearReferences(node: hou.OpNode) -> None: ...
def createNull(parent_node: hou.OpNode, name: str, parent: hou.OpNode | None = None, keeppos: bool = False, size: float = 0.05, fxn: Callable[[hou.ObjNode], object] | None = None) -> hou.ObjNode:
    """Create a basic null node(control)"""
def setTRSPNodeParms(src: hou.OpNode, dst: hou.OpNode) -> None: ...
def copyAllParms(src: hou.OpNode, dst: hou.OpNode) -> None:
    """Copies all the values of the parameters from the src 
    node to the dst node. """
def displayGuides(nodesdata: _NodesData, display: bool) -> None: ...
def lockGuides(nodesdata: _NodesData, lock: bool) -> None: ...
def lockGuideData(guidedata: hou.OpNode, lock: bool) -> None: ...
def deleteGuides(nodesdata: _NodesData) -> None: ...
def lockGuide(guide: hou.OpNode, lock: bool) -> None: ...
def updateMirror(nodesdata: _NodesData, value: bool) -> None: ...
def updateSide(nodesdata: _NodesData, mirrornodesdata: _NodesData, value: int) -> None: ...
def renameGuides(nodesdata: Mapping[str, Sequence[Any]], guidenames: Mapping[str, str]) -> None: ...
def toJSON(nodesdata: _NodesData) -> _GuideNames: ...
def createSimpleParentCHOP(node: hou.OpNode, parent: hou.OpNode, maskvalue: int | None = None, blendvalue: float = 1, keeppos: bool = False, blendparm: hou.Parm | None = None) -> hou.OpNode:
    """Creates a simple parent blend constraint.
    node: the node to be parented,
    parent: the parent node,
    maskvalue: the mask value to apply on the blend,
    keeppos: whether to keep position
    """
def addAngleParameter(guide: hou.OpNode, r_parm: str, r_range: Sequence[float], offset: float = 0, negative: bool = True) -> None:
    '''
    Adds an angle parameter to the given guide, and drive the expression for r_parm.
    The expression is "offset (+ or -) angle"
    guide: the guide node to add the parameter,
    r_parm: the rotate parm_name to be driven by the angle,
    r_range: the hard range for the angle (min, max),
    offset: offset for the expression,
    negative: + or -
    '''
def addPoseScope(node: hou.ObjNode, parm: str, input_sop: hou.SopNode | None = None) -> hou.SopNode:
    """
    Adds posescope to the geo node and point it to parm.
    node: the node to create the pose scope,
    parm: the parm name to map the pose scope to,
    input_sop: a specific input within the node to connect the nodes to
    """
def createGuideLines(parent: hou.OpNode, name: str, src: hou.OpNode, dests: Iterable[hou.OpNode], color: Sequence[float] = (0, 0, 0), resample: bool = False, segment_multiplier: float = 100) -> hou.ObjNode:
    """
    Creates a line point from src to each of the destination nodes.
    parent: the parent node to create the geometry,
    name: name of the node,
    src: the src node,
    dests: the list of nodes for which to create lines,
    color: the color of the lines, default is black,
    resample: whether to resample and make the line dashes,
    segment_multiplier: the multiplier for segmentation of resampling
    """
def createArrowPicker(node: hou.ObjNode) -> hou.SopNode:
    """
    Creates an arrow picker sop.
    node: (objNode) the sop node to create the arrow
    """
def makeNonRenderable(geo_node: hou.ObjNode) -> None:
    """Make the geo node not renderable"""
def snapGuideToGeometry(guide: hou.ObjNode, node: hou.ObjNode, geo: hou.Geometry, primgrp: str | None = None) -> None:
    """Snap the guide to the center of the geometry
    guide: the guide to snap
    node: the obj node of the geometry
    geometry: the geometry data (hou.Geometry)
    primgrp: the primitive group for bounding box
    """
