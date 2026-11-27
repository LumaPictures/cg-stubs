import _apex
import hou
from apex import apexriggraphutils as aru, stateutils_2 as asu
from collections.abc import Callable as Callable, Collection, Iterable, Mapping, Sequence
from houtypes import ViewerStateEventKwargs
from hutil.PySide.QtCore import QTimer
from typing import Protocol

class _AnimateState(asu._AnimateState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    def _groupPrimaryToGroup(self, control_path: str) -> str | None: ...
    def _refreshControlData(self) -> None: ...
    def getChildOrdering(self, control_path: str) -> list[str]: ...
    def getPickWalkData(self, sel_controls: Sequence[str] | None = ...) -> tuple[dict[str, 'PickWalkRig'], dict[str, list[str]]]: ...

CHILD_PRIORITY_PATTERNS_PROPERTY: str
PICK_WALK_PARENT_PROPERTY: str
DEFAULT_FINGER_ORDERING: _apex.StringArray
DEFAULT_BODYSIDE_ORDERING: _apex.StringArray
DEFAULT_ROOT_ORDERING: _apex.StringArray
DEFAULT_CHEST_ORDERING: _apex.StringArray
DEFAULT_FOOT_ORDERING: _apex.StringArray
VISIBLE_TIME: int
HOTKEY_KEYNAME_MAPPINGS: dict[str, str]

class PickWalkRig:
    """
    Wrapper around the pick walk data for a rig or character. Can be used
    with either a rig graph or a skeleton.
    """
    rig_path: str
    graph_or_skel: hou.Geometry | _apex.Graph
    skel: hou.Geometry | None
    graph: _apex.Graph | None
    control_to_joint: Callable[[str], str] | None
    joint_to_control: Callable[[str], str] | None
    position_cb: Callable[[str, str], hou.Vector3 | None] | None
    parent_lookup_cb: Callable[[str, str], str | None] | None
    def __init__(self, rig_path: str, graph_or_skel: hou.Geometry | _apex.Graph, control_to_joint: Callable[[str], str] | None = None, joint_to_control: Callable[[str], str] | None = None, position_cb: Callable[[str, str], hou.Vector3 | None] | None = None, parent_lookup_cb: Callable[[str, str], str | None] | None = None) -> None: ...
    def isGraph(self) -> bool:
        """ Whether it is using the graph. """
    def isSkel(self) -> bool:
        """ Whether it is using the skeleton. """
    def controlToJoint(self, ctrl_path: str) -> str:
        """ The control to joint function. """
    def jointToControl(self, joint_name: str) -> str:
        """ The joint to control function. """
    def skelWrapper(self) -> aru.SkelWrapper:
        """ Get a skeleton wrapper object. """
    def getPosition(self, control_path: str) -> hou.Vector3 | None: ...
    def _parentLookup(self, control_name: str) -> str | None: ...

class PickWalkerCache:
    """ Cache to hold onto parent and child maps. """
    parent_maps: dict[str, dict[str, str]]
    child_maps: dict[str, dict[str, list[str]]]
    def __init__(self) -> None: ...
    def clear(self) -> None:
        """ Clear all cached maps. """
    def getDepthMap(self, pick_walk_rig: PickWalkRig, node_name_filter: set[str], roots: Iterable[str] | None = None) -> dict[str, int]: ...
    def getHeightMap(self, pick_walk_rig: PickWalkRig, node_name_filter: set[str], roots: Collection[str] | None = None, leaves: Iterable[str] | None = None) -> dict[str, int]: ...
    def getParentMap(self, pick_walk_rig: PickWalkRig, node_name_filter: set[str]) -> dict[str, str]:
        """
        Get the parent map given the pick walk rig.

        :pick_walk_rig: The wrapper around the skeleton or rig graph.
        :node_name_filter: The set of names to include in the parent map.
        """
    def getChildMap(self, pick_walk_rig: PickWalkRig, node_name_filter: set[str]) -> dict[str, list[str]]:
        '''"
        Get the child map given the pick walk rig.

        :pick_walk_rig: The wrapper around the skeleton or rig graph.
        :node_name_filter: The set of names to include in the child map.
        '''
    def getParent(self, pick_walk_rig: PickWalkRig, control_name: str, node_name_filter: set[str]) -> str | None:
        """
        Get the parent.

        :pick_walk_rig: The wrapper around the skeleton or rig graph.
        :control_name: The control name.
        :node_name_filter: The set of valid control names.
        """
    def getParentWrapper(self, pick_walk_rig: PickWalkRig, control_name: str, node_name_filter: set[str], child_orderer: aru.ChildOrderer | None = None) -> str | None:
        """
        Wrapper around getParent to have the same signature as others that
        require the child_orderer input.
        """
    def getFirstChild(self, pick_walk_rig: PickWalkRig, control_name: str, node_name_filter: set[str], child_orderer: aru.ChildOrderer | None = None) -> str | None:
        """
        Get the first child.

        :pick_walk_rig: The wrapper around the skeleton or rig graph.
        :control_name: The control name.
        :node_name_filter: The set of valid control names.
        """
    def getChildren(self, pick_walk_rig: PickWalkRig, control_name: str, node_name_filter: set[str], child_orderer: aru.ChildOrderer | None = None) -> list[str]:
        """
        Get the child controls.

        :pick_walk_rig: The wrapper around the skeleton or rig graph.
        :control_name: The control name.
        :node_name_filter: The set of valid control names.
        """
    def getDescendants(self, pick_walk_rig: PickWalkRig, control_names: Collection[str], node_name_filter: set[str], first_branch_only: bool = False, child_orderer: aru.ChildOrderer | None = None) -> list[str]:
        """
        Get the list of all descendants.

        :pick_walk_rig: The wrapper around the skeleton or rig graph.
        :control_names: The control names to get the descendants of.
        :node_name_filter: The set of valid control names.
        :first_branch_only: Defines if the descendants should only be traced up the next branch.
        """
    def getDescendantPath(self, pick_walk_rig: PickWalkRig, control_name: str, descendant_name: str, node_name_filter: set[str]) -> list[str]:
        """
        Get the controls in a hierarchical order that lead from a given control name to a given descendant control

        :pick_walk_rig: The wrapper around the skeleton or rig graph.
        :control_name: The given start control to start the path traversal from
        :descendant_name: The name of the specific decendant control to find the hierarchy control path for
        :node_name_filter: The set of valid control names.
        """
    def getNextSibling(self, pick_walk_rig: PickWalkRig, control_name: str, node_name_filter: set[str], child_orderer: aru.ChildOrderer | None = None) -> str | None:
        """
        Get the next sibling.

        :pick_walk_rig: The wrapper around the skeleton or rig graph.
        :control_name: The control name.
        :node_name_filter: The set of valid control names.
        """
    def getPrevSibling(self, pick_walk_rig: PickWalkRig, control_name: str, node_name_filter: set[str], child_orderer: aru.ChildOrderer | None = None) -> str | None:
        """
        Get the previous sibling.

        :pick_walk_rig: The wrapper around the skeleton or rig graph.
        :control_name: The control name.
        :node_name_filter: The set of valid control names.
        """
    def buildLocalHierarchy(self, pick_walk_rig: PickWalkRig, control_name: str, node_name_filter: set[str], child_orderer: aru.ChildOrderer | None = None) -> tuple[hou.Geometry, hou.Geometry, dict[int, hou.Vector3]]: ...

TEXT_FONT_SIZE: float

class PickWalkGuide:
    """
    Encapsulate the pick walking local hierarchy guide.
    """
    scene_viewer: hou.SceneViewer
    local_guide_drawable: hou.SimpleDrawable
    local_guide_points_drawable: hou.GeometryDrawable
    primary_pt_circle_drawable: hou.GeometryDrawable
    key_map: dict[int, str]
    text_drawables: dict[int, hou.TextDrawable]
    next_key_posns: dict[int, hou.Vector3]
    timer: QTimer
    def __init__(self, scene_viewer: hou.SceneViewer, hotkeys: asu.Hotkeys) -> None: ...
    def draw(self, draw_handle: int) -> None:
        """ Draw the guides. """
    def unloadDrawables(self) -> None:
        """ Unload simple drawables when exiting the state. """
    def setGeometry(self, local_guide_skel: hou.Geometry, p0_geo: hou.Geometry, next_key_posns: dict[int, hou.Vector3]) -> None:
        """ Set the local hierarchy geometry and the primary point geometry. """
    def show(self, val: bool, auto_hide: bool = True) -> None:
        """
        Show or hide the pick walk guide, optionally also can specify
        whether to auto hide after a short duration.
        """
    def hide(self) -> None:
        """ Hide the pick walk guide. """

class PickWalker:
    """
    Used to perform pick walking/growing/shrinking on the rig or skeleton
    using hotkeys.
    """
    pick_walk_cache: PickWalkerCache
    pick_walk_guide: PickWalkGuide
    hotkeys: asu.Hotkeys
    def __init__(self, state: _AnimateState) -> None: ...
    @property
    def state(self) -> _AnimateState | None: ...
    def draw(self, draw_handle: int) -> None:
        """ Draw the guides. """
    def unloadDrawables(self) -> None:
        """ Unload drawables. """
    def hideGuideSkel(self) -> None:
        """ Hide the local hierarchy guide. """
    def showGuideSkel(self, local_guide_skel: hou.Geometry, p0_geo: hou.Geometry, next_key_posns: dict[int, hou.Vector3], auto_hide: bool = True) -> None:
        """ Update and show the local hierarchy guide. """
    def matchRigs(self, ctrl_A: str, ctrl_B: str, rig_to_all_controls: Mapping[str, Iterable[str]] | None = None, names_only: bool = False, child_ordering_fn: Callable[[str], list[str]] | None = None, branch_only: bool = False) -> list[tuple[str, str]]: ...
    def selectDescendants(self, controls_list: Sequence[str] | None = None) -> None:
        """ Given a list of controls, select the descendant controls. """
    def getDescendants(self, controls_list: Sequence[str], rig_to_all_controls: Mapping[str, Iterable[str]] | None = None, first_branch_only: bool = False) -> list[str]:
        """ Given a list of controls, select the descendant controls. """
    def getChildren(self, controls_list: Sequence[str], rig_to_all_controls: Mapping[str, Iterable[str]] | None = None, exclude_parents: bool = True) -> list[str]:
        """ Given a list of controls, select the children controls. """
    def getParentMap(self, controls_list: Sequence[str], rig_to_all_controls: Mapping[str, Iterable[str]] | None = None, exclude_selected: bool = True) -> dict[str, str]:
        """ Given a list of controls, create a map of the selected control to its parent
        
            selected control -> parent control
        
        param exclude_selected: gives the option to exclude all mapping entries where the parent is also part of the 
        current control list. This is for example helpful for some pose constraints where only the controls that 
        are not part of the current selection need extra constraints
        """
    def getDescendantPath(self, ctrl_A: str, ctrl_B: str, rig_to_all_controls: Mapping[str, Iterable[str]] | None = None) -> list[str]:
        """ Given a list of controls, select the descendant controls. """
    def _walk(self, next_controls_fn: Callable[[PickWalkRig, str, set[str], aru.ChildOrderer], str | list[str] | None], pick_modifier: hou.EnumValue[hou.pickModifier] | None, need_ordering: bool = True) -> None:
        """
        Call to perform the walk.

        :next_controls_fn: The function to apply to do one step of one control.
        :pick_modifier: Whether to do a replace, add, or remove.
        """
    def walkUp(self, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None) -> None:
        """ Call to walk/grow/shrink up. """
    def walkDown(self, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None) -> None:
        """ Call to walk/grow/shrink down. """
    def walkLeft(self, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None) -> None:
        """ Call to walk/grow/shrink to the left. """
    def walkRight(self, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None) -> None:
        """ Call to walk/grow/shrink to the right. """
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Respond to the key event. Sent from the animate state. """
