import _apex
import hou
import typing
from _apexscene import Scene as Scene, SceneGraph as SceneGraph
from collections.abc import Callable as Callable, Collection, Iterable, Mapping
from typing import Literal

def getInverseRig(rig: SceneGraph, pattern: str) -> _apex.Graph:
    """
    Set up inverse rig graph using pattern.

    :param rig: rig to be inverted
    :type rig: ApexRig
    :param pattern: pattern for inversion
    :type pattern: str
    :return: the inverse rig
    :rtype: _apex.Graph
    """
def createControlToJointMap(rig_graph: _apex.Graph) -> dict[str, list[str]]:
    """
    Create a map of controls to their corresponding points on the skeleton.

    :param rig_graph: rig graph of controls
    :type rig_graph: _apex.Graph
    :return: a map of control name to point name
    :rtype: Dict{str:List[str]}
    .. note::
        Certain controls (i.e. ik controllers) can map to multiple points
    """

NODE_PORT_LINKS: dict[str, list[tuple[str, str]]]
IK_NODE_PORT_LINKS: dict[str, dict[str, list[str]]]
TWIST_TAG: str
PICK_WALK_EXCLUDE_TAG: str
SKIP_TAGS: set[str]

def findIKNextPort(rig_graph: _apex.Graph, nodeid: int, wire_in: tuple[int, int], reverse: bool) -> list[int]:
    """
    Try nodeid as an IK node with a special pattern to find the next ports.

    :rig_graph: The apex graph for the rig.
    :nodeid: The current node
    :wire_in: The wire into the current node.
    :reverse: Whether to search in the opposite direction.
    """
def getNodeParents(rig_graph: _apex.Graph, nodeid: int, node_name_filter: set[str], max_n: int = 0) -> list[tuple[int, int]]:
    """
    Get the parent nodes.

    :rig_graph: The apex graph to use for the rig.
    :nodeid: The current node to get parents of.
    :node_name_filter: 
    """
def getControlParents(rig_graph: _apex.Graph, control_name: str, node_name_filter: set[str]) -> list[str]:
    """
    Get the control parents given a rig graph.

    :rig_graph: The apex Graph used for the rig of the character.
    :control_name: The control name.
    :node_name_filter: A set of control names to include in the parent map.
    """
def buildParentMap(rig_graph: _apex.Graph, node_name_filter: set[str], parent_lookup_cb: Callable[[str], str | None] | None = None) -> dict[str, str]:
    """
    Build the parent map for a rig graph.

    :rig_graph: The apex Graph used for the rig of the character.
    :node_name_filter: A set of control names to include in the parent map.
    """

class SkelWrapper:
    """
    A wrapper around the skeleton that also comes with functors
    for converting between control names and joints on the skeleton.
    """
    skel: hou.Geometry
    control_to_joint: Callable[[str], str]
    joint_to_control: Callable[[str], str]
    def __init__(self, skel: hou.Geometry, control_to_joint: Callable[[str], str], joint_to_control: Callable[[str], str]) -> None: ...

def skelJointParent(skel: hou.Geometry, joint_name: str) -> str | None:
    """ Given a skeleton geometry, and a joint name, find the parent joint name. """
def getSkelControlParents(skel: SkelWrapper, control_name: str, node_name_filter: set[str]) -> list[str]:
    """
    Get the parents of the control given the skel.

    :skel: A wrapper around the skeleton that also comes with functors
           for converting between control names and joints on the skeleton.
    :control_name: The control name.
    :node_name_filter: A set of control names to include in the parent map.
    """
def buildSkelParentMap(skel: SkelWrapper, node_name_filter: set[str], parent_lookup_cb: Callable[[str], str | None] | None = None) -> dict[str, str]:
    """
    Build the parent map from the skeleton.

    :skel: A wrapper around the skeleton that also comes with functors
           for converting between control names and joints on the skeleton.
    :node_name_filter: A set of control names to include in the parent map.
    """
def buildChildMap(parent_map: Mapping[str, str]) -> dict[str, list[str]]:
    """ Given the parent map, invert it to find the child map. """
def getFirstParent(parent_map: Mapping[str, str], control_name: str) -> str | None:
    """
    Get the parent of the control.

    :parent_map: The map of parent control from each control.
    :control_name: The control name.
    """
def getRoots(parent_map: Mapping[str, str], child_map: Mapping[str, list[str]]) -> list[str]: ...
def buildDepthMap(parent_map: Mapping[str, str], child_map: Mapping[str, list[str]], roots: Iterable[str] | None = None) -> dict[str, int]: ...
def getLeaves(parent_map: Mapping[str, str], child_map: Mapping[str, list[str]]) -> list[str]: ...
def buildHeightMap(parent_map: Mapping[str, str], child_map: Mapping[str, list[str]], roots: Collection[str] | None = None, leaves: Iterable[str] | None = None) -> dict[str, int]:
    """
    Build map of control_name -> maximal height w.r.t. one of the leaves
    under control_name.
    """

class ChildOrderer:
    rig_path: str
    ordering_fn: Callable[[str], list[str]] | None
    height_map: Mapping[str, int] | None
    def __init__(self, rig_path: str, ordering_fn: Callable[[str], list[str]] | None, height_map: Mapping[str, int] | None = None) -> None: ...
    def getOrdering(self, parent: str) -> list[str]: ...
    def reorder(self, parent: str, children: list[str]) -> list[str]: ...

def getChildren(child_map: Mapping[str, list[str]], control_name: str, child_orderer: ChildOrderer | None = None) -> list[str]:
    """
    Get the child controls.

    :child_map: The map of child controls from each control.
    :control_name: The control name.
    """
def getFirstChild(child_map: Mapping[str, list[str]], control_name: str, child_orderer: ChildOrderer | None = None) -> str | None:
    """
    Get the first child of the control. 

    :child_map: The map of child controls from each control.
    :control_name: The control name.
    """
@typing.overload
def getSiblings(parent_map: Mapping[str, str], child_map: Mapping[str, list[str]], control_name: str, child_orderer: ChildOrderer | None = ..., return_parent: Literal[False] = ...) -> list[str]: ...
@typing.overload
def getSiblings(parent_map: Mapping[str, str], child_map: Mapping[str, list[str]], control_name: str, child_orderer: ChildOrderer | None, return_parent: Literal[True]) -> tuple[list[str], list[str]]: ...
def getNextSibling(parent_map: Mapping[str, str], child_map: Mapping[str, list[str]], control_name: str, child_orderer: ChildOrderer | None = None) -> str | None:
    """
    Get the next sibling of the control. 

    :parent_map: The map of parent control from each control.
    :child_map: The map of child controls from each control.
    :control_name: The control name.
    """
def getPrevSibling(parent_map: Mapping[str, str], child_map: Mapping[str, list[str]], control_name: str, child_orderer: ChildOrderer | None = None) -> str | None:
    """
    Get the previous sibling of the control. 

    :parent_map: The map of parent control from each control.
    :child_map: The map of child controls from each control.
    :control_name: The control name.
    """
def getDescendantPath(parent_name: str, descendant_name: str, parent_map: Mapping[str, str]) -> list[str]:
    """
    Get the hierarchy path leading from a given start control to a specific descendant control. 
    If the given descendant control is not a descendant of the given start control the returned hierarchy path list is 
    empty

    :parent_name: The control name of the start control to find the path to a given descendant control for.
    :parent_name: The control name of the descandant control to find the hierarchy path from a given start control from
    :child_map: The map of child controls from each control.
    """
def getDescendants(controls: Collection[str], child_map: Mapping[str, list[str]], first_branch_only: bool = False, child_orderer: ChildOrderer | None = None) -> list[str]:
    """
    Get the list of descendant controls.

    :controls: The control names.
    :child_map: The map of child controls from each control.
    :first_branch_only: Defines if the descendants should only be traced up the next branch.
    """

PARENT_KEY: int
CHILD_KEY: int
NEXT_SIBLING_KEY: int
PREV_SIBLING_KEY: int

def buildLocalHierarchy(control_name: str, rig_path: str, parent_map: Mapping[str, str], child_map: Mapping[str, list[str]], position_cb: Callable[[str], hou.Vector3 | None], child_orderer: ChildOrderer | None = None) -> tuple[hou.Geometry, hou.Geometry, dict[int, hou.Vector3]]:
    """ Build the local hierarchy around the given control. """
def getSkel(scene: Scene, rig_path: str) -> hou.Geometry | None:
    """
    Evaluate a rig graph's skeleton from the scene, defined as the first
    output port whose name ends with the suffix .skel.

    :param scene: The apex scene to evaluate the skeleton from
    :type scene: apex.Scene
    :param rig_path: The path of the rig graph to evaluate
    :type rig_path: str
    :return: skeleton of rig_graph
    :rtype: hou.Geometry
    .. note::
        Returns None if no skeleton is found.
    """
def getLocalTransformsFromWorld(inverse_rig_graph: _apex.Graph, xforms: _apex.Dict) -> _apex.Dict:
    """
    Evaluate the inverse_rig_graph to get the local transforms of xforms as
    separate component parameter values.

    :param inverse_rig_graph: inverse rig to be evaluated
    :type inverse_rig_graph: _apex.Graph
    :param xforms: transforms in world space to be converted to local space
    :type xforms: Dict{str, hou.Matrix4}
    :return: dictionary of the control transform label and its value 
    :rtype: Dict{str:hou.Vector3}
    """
def getRigGraphAtRest(scene: Scene, rig_path: str) -> _apex.Graph: ...
def getMirrorFlipAxesFromControls(scene: Scene, rig_path: str, mirrored_ctrls: Mapping[str, str], mirror_axis: hou.Vector3) -> dict[str, int]:
    """
    Determine what axes are flipped when ctrl is flipped along the mirror axis compared to mirrored_ctrl. 

    :param scene: The scene with the controls to mirror
    :type scene: apex.Scene
    :param rig_path: The path to the rig in the scene that the controls belong to
    :type rig_path: str
    :param mirrored_ctrls: A dictionary from controls to their mirrored control
    :type mirrored_ctrls: dict from str to str
    :param mirror_axis: normal of the plane along which the mirror should occur
    :type mirror_axis: hou.Vector3
    :return: flipaxes as a bitfield. 1 for the x axis, 2 for the y axis, 4 for the z axis
    :rtype: int
    """
