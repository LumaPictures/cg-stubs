import apex
import apex.autorigutils as ar
import apex.stateutils_2 as asu
import hou
from apex.apexutils import BijectiveMap as BijectiveMap
from apex.pickwalker import DEFAULT_FINGER_ORDERING as DEFAULT_FINGER_ORDERING, PickWalkRig as PickWalkRig, PickWalker as PickWalker
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from houtypes import ViewerStateDrawKwargs, ViewerStateEventKwargs
from resourceutils import CursorIcon
from typing import Literal, Protocol, TypeAlias

from typing import TypeAlias
VariadicPairInfo: TypeAlias = ar.VariadicPairInfo
class _ModifierKeys(Protocol):
    def isShiftKey(self) -> bool: ...
    def isCtrlKey(self) -> bool: ...

class _AnimateState(asu._AnimateState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    @property
    def cursor_font_size(self) -> float: ...

class _JointPatternFunc(Protocol):
    def __call__(self, joints: list[str], exclude: bool = ..., /) -> str: ...
PARENT_MAP: str
CHAIN_MAP: str
NEW_PARENT_MAP: str
HIERARCHY_MAP: str
RAY_GRAPH: str
REFERENCE_GRAPH: str
REFERENCE_RIG_PATH: str
SKEL_RIG_PATH: str
SKELETON_KWARGS: str
SKEL_GRAPH_PARM: str
TEMP_ROOT_NAME: str
SINGLE_MATCH: str
HIERARCHY_MATCH: str
PARENT_MATCH: str
DELETE_MATCH: str
DRAG_MATCH: str
DEFAULT_RADIUS: float
REFERENCE_RADIUS: float
NEARPOINT_RADIUS: float
SNAP_DISTANCE: float
DRAG_SNAP_DISTANCE: float
REF_SNAP_MULTIPLIER: float
DEFAULT_LINE_WIDTH: float
MAP_LINE_WIDTH: float
DARK_PREVIEW_FACTOR: float
OVERLAP_OFFSET: float
OVERLAP_GRAY_VALUE: float
LIGHT_DEFAULT_COLOR: hou.Vector4
DARK_DEFAULT_COLOR: hou.Vector4

class ColorScheme:
    """Manages all visualization colors for the joint mapper.

    Centralizes color management including default colors, preview colors,
    highlight colors, and theme-specific colors (light/dark).
    """
    default: hou.Vector4
    default_v3: hou.Vector3
    light_default: hou.Vector4
    dark_default: hou.Vector4
    preview: hou.Vector4
    dark_preview: hou.Vector4
    highlight: hou.Vector4
    def_highlight: hou.Vector4
    parent: hou.Vector4
    remove: hou.Vector4
    reference: hou.Vector4
    nearpoint: hou.Vector4
    preview_v3: hou.Vector3
    highlight_v3: hou.Vector3
    reference_v3: hou.Vector3
    parent_v3: hou.Vector3
    remove_v3: hou.Vector3
    def __init__(self, scene_viewer: hou.SceneViewer) -> None:
        """Initialize color scheme from scene viewer settings.

        :param scene_viewer: The Houdini scene viewer to extract colors from
        :type scene_viewer: hou.SceneViewer
        """
    def setDefaultColor(self, color: hou.Vector4) -> None:
        """Update the default color.

        :param color: hou.Vector4 color to set as default
        :type color: hou.Vector4
        """

class DrawableSet:
    """Manages all drawable objects for joint visualization.

    Handles creation, configuration, and visibility of all drawable elements
    including point markers, lines, and reference skeleton visualizations.
    """
    scene_viewer: hou.SceneViewer
    colors: ColorScheme
    default: hou.GeometryDrawable | None
    default_line: hou.GeometryDrawable | None
    preview: hou.GeometryDrawable | None
    refskel: hou.GeometryDrawable | None
    refskel_line: hou.GeometryDrawable | None
    map_line: hou.GeometryDrawable | None
    nearpoint: hou.GeometryDrawable | None
    reference_drawables: list[hou.GeometryDrawable]
    map_line_geo: hou.Geometry | None
    preview_guide_match_points: list[int]
    variadic_guide_match_points: list[int]
    is_visible: bool
    reference_match_pattern: str
    full_match_pattern: str
    def __init__(self, scene_viewer: hou.SceneViewer, colors: ColorScheme) -> None:
        """Initialize drawable set.

        :param scene_viewer: The Houdini scene viewer for drawables
        :type scene_viewer: hou.SceneViewer
        :param colors: ColorScheme instance for color management
        :type colors: ColorScheme
        """
    def createMapLineGeo(self) -> None:
        """Create geometry for the preview line that shows mapping target.

        Creates a two-point line geometry used to visualize the connection
        between a source joint and its mapping target.
        """
    def updateLineGeo(self, start_pos: hou.Vector3, end_pos: hou.Vector3) -> None:
        """Update the positions of the map line endpoints.

        :param start_pos: Starting position (source joint)
        :type start_pos: hou.Vector3
        :param end_pos: Ending position (target joint)
        :type end_pos: hou.Vector3
        """
    def show(self, visible: bool) -> None:
        """Show or hide all drawables.

        :param visible: True to show, False to hide
        :type visible: bool
        """
    def isVisible(self) -> bool:
        """Check if drawables are visible.

        :return: True if visible, False otherwise
        :rtype: bool
        """
    def clear(self, clear_drawables: bool = False) -> None:
        """Clear drawable state and optionally release drawable references.

        :param clear_drawables: If True, set all drawable references to None
        :type clear_drawables: bool
        """

class SkeletonData:
    """Manages guide skeleton geometry and related data.

    Handles skeleton setup, joint overlap resolution, and skeleton state management
    including original positions for reset functionality.
    """
    colors: ColorScheme
    skeleton: hou.Geometry | None
    orig_skeleton: hou.Geometry | None
    default_points: list[int]
    cached_points: list[int]
    is_reset: bool
    exclude_pattern: str
    def __init__(self, colors: ColorScheme) -> None:
        """Initialize skeleton data.

        :param colors: ColorScheme instance for color management
        :type colors: ColorScheme
        """
    def setSkeleton(self, skeleton: hou.Geometry, excluded_joints: list[str] | None = None, grp_pattern_func: _JointPatternFunc | None = None) -> tuple[hou.Geometry, hou.Geometry]:
        """Set and initialize the guide skeleton.

        :param skeleton: hou.Geometry containing the guide skeleton
        :type skeleton: hou.Geometry
        :param excluded_joints: Optional list of joint names to exclude
        :type excluded_joints: list[str] or None
        :param grp_pattern_func: Function to generate group patterns from joint lists
        :type grp_pattern_func: callable or None
        :return: Tuple of (skeleton, default_skel) geometries
        :rtype: tuple[hou.Geometry, hou.Geometry]
        """
    def resolveJointOverlap(self, near_point_name: str) -> None:
        """Offset overlapping joints for better visualization.

        Joints sharing the same position are given subtle offsets to make
        them individually selectable.

        :param near_point_name: Name of the point to check for overlaps
        :type near_point_name: str
        """
    def reset(self) -> None:
        """Reset skeleton to original positions and colors.

        Undoes any offsets applied by resolveJointOverlap.
        """
    def updateColor(self, color_3d: hou.Vector3) -> None:
        """Update the color of all skeleton points.

        :param color_3d: hou.Vector3 color to apply to all points
        :type color_3d: hou.Vector3
        """
    def clear(self) -> None:
        """Clear all skeleton data and reset to initial state."""

class ReferenceData:
    """Manages reference skeleton data and transforms.

    Handles reference skeleton setup, transform management, and provides
    utilities for working with reference joints and hierarchies.
    """
    skeleton: hou.Geometry | None
    rest: hou.Geometry | None
    transforms: apex.Dict
    start_transforms: apex.Dict
    rest_transforms: apex.Dict
    xform: hou.Matrix4 | None
    current_xform: hou.Matrix4 | None
    xform_offset: hou.Matrix4
    variadic_pairs: dict[str, VariadicPairInfo]
    joint_name: str
    def __init__(self) -> None:
        """Initialize reference data."""
    def setSkeleton(self, skeleton: hou.Geometry, joint_path_func: Callable[[str], str] | None = None) -> list[str]:
        """Set and initialize the reference skeleton.

        :param skeleton: hou.Geometry containing the reference skeleton
        :type skeleton: hou.Geometry
        :param joint_path_func: Function to generate joint paths
        :type joint_path_func: callable or None
        :return: List of joint paths for the reference skeleton
        :rtype: list[str]
        """
    @property
    def has_variadic_pairs(self) -> bool:
        """Whether the reference skeleton has any variadic pair markers."""
    def setJoint(self, name: str, xform: hou.Matrix4 | None = None, joint_path_func: Callable[[str], str] | None = None) -> None:
        """Set the current selected reference joint.

        :param name: Joint name
        :type name: str
        :param xform: Optional transform matrix
        :type xform: hou.Matrix4 or None
        :param joint_path_func: Function to generate joint path
        :type joint_path_func: callable or None
        """
    def findRoots(self) -> list[str]:
        """Find root joint names of the reference skeleton.

        Uses cached value when available for O(1) repeated access.

        :return: List of root joint names
        :rtype: list[str]
        """
    def findXform(self, jointname: str | None = None) -> hou.Matrix4 | None:
        """Find transform for a reference joint.

        :param jointname: Optional joint name, uses reference_joint_name if None
        :type jointname: str or None
        :return: hou.Matrix4 transform or None
        :rtype: hou.Matrix4 or None
        """
    def findRestXform(self, jointname: str | None = None) -> hou.Matrix4 | None:
        """Find rest transform for a reference joint.

        :param jointname: Optional joint name, uses reference_joint_name if None
        :type jointname: str or None
        :return: hou.Matrix4 rest transform or None
        :rtype: hou.Matrix4 or None
        """
    def getJointNameOnly(self) -> str:
        """Extract joint name from full path.

        :return: Joint name without path prefix
        :rtype: str
        """
    def setOffset(self, offset: hou.Vector3) -> None:
        """Set the transform offset for reference skeleton.

        :param offset: hou.Vector3 offset to apply
        :type offset: hou.Vector3
        """
    def updateTransform(self, name: str, xform: hou.Matrix4) -> None:
        """Update a reference joint's transform.

        :param name: Joint name
        :type name: str
        :param xform: New transform matrix
        :type xform: hou.Matrix4
        """
    def clear(self) -> None:
        """Clear all reference data and reset to initial state."""

class MappingState:
    """Manages bijective joint mapping state.

    Tracks the mapping between guide skeleton joints and reference joints,
    including matched pairs, removed joints, and mapping operations.
    """
    map: BijectiveMap[str, str]
    matched: list[tuple[str, str]]
    removed: list[str]
    removed_joints: list[str]
    variadic_matched: dict[str, list[tuple[str, str]]]
    match_mode: str | None
    src_left: str | None
    src_right: str | None
    tgt_left: str | None
    tgt_right: str | None
    root_xf: hou.Matrix4
    is_variadic: bool
    root_grp: str
    root_name: str
    dragging: bool
    def __init__(self) -> None:
        """Initialize mapping state."""
    def clear(self) -> None:
        """Clear all mapping data and reset to initial state."""
    def init(self, map_dict: Mapping[str, str] | None = None, multiparm: Sequence[Mapping[str, str]] | None = None) -> None:
        """Load initial map from dict or multiparm list.

        :param map_dict: Dictionary to load map from
        :param multiparm: List of multiparm entries with 'default#' and 'existing#' keys
        """
    def update(self, matched: list[tuple[str, str]], removed: list[str], clear: bool = False) -> None:
        """Update map with matched/removed pairs, with body side mirroring.

        :param matched: List of (skeleton_joint, reference_joint) tuples
        :param removed: List of reference joint names to remove
        :param clear: Whether to clear existing map first
        """
    def isMapped(self) -> bool:
        """Check if any mappings exist.

        :return: True if there are mappings, False otherwise
        :rtype: bool
        """
    def keys(self) -> list[str]:
        """Get all map keys.

        :return: List of map keys
        :rtype: list
        """
    def values(self) -> list[str]:
        """Get all map values.

        :return: List of map values
        :rtype: list
        """
    def rootPatternMatch(self, bodyside_pattern: str | None = None) -> bool:
        """Check if mapping matches given body side pattern.

        :param bodyside_pattern: Pattern to match (defaults to skeleton_left)
        :return: True if pattern matches, False otherwise
        """
    @staticmethod
    def generatePointPattern(names: list[str], exclude: bool = False) -> str:
        """Generate Houdini group pattern from joint names.

        :param names: List of joint names
        :type names: list[str]
        :param exclude: If True, generate exclusion pattern
        :type exclude: bool
        :return: Space-separated pattern string
        :rtype: str
        """
    def updateRemoved(self, jnt: str, toggle: bool = True, add: bool = True, clear: bool = False) -> None:
        """Update the removed joints list.

        :param jnt: Joint name to update
        :type jnt: str
        :param toggle: If True, toggle joint in/out of list
        :type toggle: bool
        :param add: If True and not toggle, add joint; if False, remove
        :type add: bool
        :param clear: If True, clear the list first
        :type clear: bool
        """
    def autoRemove(self, rest: hou.Geometry) -> None:
        """Auto-generate list of unmapped joints to remove.

        :param rest: Reference rest skeleton geometry
        :type rest: hou.Geometry
        """
    def removedPattern(self) -> str:
        """Generate group pattern for removed joints.

        :return: Space-separated group pattern string
        :rtype: str
        """

class NullCursorIcon:
    """Null object pattern for cursor icon when state doesn't have one.

    All methods are no-ops, allowing code to call cursor_icon methods
    without checking for existence.
    """
    def setText(self, *args: object, **kwargs: object) -> None: ...
    def setTextPos(self, *args: object, **kwargs: object) -> None: ...
    def showIcon(self, *args: object, **kwargs: object) -> None: ...
    def showText(self, *args: object, **kwargs: object) -> None: ...
    def onMouseEvent(self, *args: object, **kwargs: object) -> None: ...

class NullPickWalker:
    """Null object pattern for pick walker when state doesn't have one.

    Returns empty results for all methods.
    """
    def getDescendants(self, *args: object, **kwargs: object) -> list[str]: ...
    def getDescendantPath(self, *args: object, **kwargs: object) -> list[str]: ...
    def matchRigs(self, *args: object, **kwargs: object) -> list[tuple[str, str]]: ...

class PatternBuilder:
    """Builds group patterns for Houdini geometry selection.

    Centralizes all @name= pattern generation logic for consistency
    and easier maintenance.
    """
    @staticmethod
    def fromNames(names: Iterable[str], exclude: bool = False) -> str:
        """Build @name pattern from joint names.

        :param names: List or iterable of joint names
        :param exclude: If True, prefix with ^ for exclusion
        :type exclude: bool
        :return: Space-separated pattern string
        :rtype: str
        """
    @staticmethod
    def fromRoots(roots: list[str]) -> str:
        """Build pattern for reference root joints.

        :param roots: List of root joint names
        :type roots: list[str]
        :return: Space-separated pattern string
        :rtype: str
        """

class MatchingHelpers:
    """Static utility methods for joint matching operations.

    Provides helper functions for sorting map keys by hierarchy,
    finding body side mappings, and other matching-related utilities.
    """
    @staticmethod
    def refPath(joint: str) -> str:
        """Generate full path for reference joint.

        :param joint: Joint name
        :type joint: str
        :return: Full joint path string
        :rtype: str
        """
    @staticmethod
    def skelPath(joint: str) -> str:
        """Generate full path for skeleton joint.

        :param joint: Joint name
        :type joint: str
        :return: Full joint path string
        :rtype: str
        """
    @staticmethod
    def jointPattern(joints: list[str] | None = None, exclude: bool = True) -> str:
        """Generate group pattern from joint names.

        :param joints: List of joint names
        :type joints: list[str] or None
        :param exclude: If True, generate exclusion pattern
        :type exclude: bool
        :return: Space-separated pattern string
        :rtype: str
        """
    @staticmethod
    def sortByHierarchy(mapping: BijectiveMap[str, str], reference_skeleton: hou.Geometry, pick_walker: PickWalker | NullPickWalker, joint_paths: Mapping[str, Iterable[str]], reference_path_func: Callable[[str], str], is_variadic: bool = False) -> list[str]:
        """Sort mapping keys by hierarchical order of reference rig.

        :param mapping: BijectiveMap to sort
        :type mapping: utils.BijectiveMap
        :param reference_skeleton: Reference skeleton geometry
        :type reference_skeleton: hou.Geometry
        :param pick_walker: PickWalker instance for hierarchy traversal
        :type pick_walker: PickWalkRig
        :param joint_paths: Dict of joint paths by rig path
        :type joint_paths: dict
        :param reference_path_func: Function to generate reference joint paths
        :type reference_path_func: callable
        :param is_variadic: Whether to include variadic joints (_1, _2, etc.)
        :type is_variadic: bool
        :return: List of sorted map keys
        :rtype: list
        """
    @staticmethod
    def findBodyside(skeleton: hou.Geometry | None, reference_transforms: apex.Dict, reference_roots: list[str], is_mapped: bool, root_pattern_match_func: Callable[[str], bool] | None = None, tolerance: float = 0.3) -> int:
        """Determine if mapping is on left, right, or center body side.

        :param skeleton: Guide skeleton geometry
        :type skeleton: hou.Geometry
        :param reference_transforms: Dict of reference transforms
        :type reference_transforms: apex.Dict
        :param reference_roots: List of reference root joint names
        :type reference_roots: list[str]
        :param is_mapped: Whether mapping exists
        :type is_mapped: bool
        :param root_pattern_match_func: Optional function to check root pattern match
        :type root_pattern_match_func: callable or None
        :param tolerance: Relative tolerance for body side detection
        :type tolerance: float
        :return: 0 for left, 1 for right, 2 for center
        :rtype: int
        """
    @staticmethod
    def jointName(joint_path: str) -> str:
        """Extract joint name from full joint path.

        :param joint_path: Full path string (e.g., '/rig/joint')
        :type joint_path: str
        :return: Joint name (e.g., 'joint')
        :rtype: str
        """
    @staticmethod
    def matchByName(source_names: list[str], target_names: list[str], case_sensitive: bool = True) -> dict[str, str]:
        """Find matching joints by name between source and target lists.

        :param source_names: List of source joint names
        :type source_names: list[str]
        :param target_names: List of target joint names
        :type target_names: list[str]
        :param case_sensitive: Whether matching should be case sensitive
        :type case_sensitive: bool
        :return: Dict mapping source names to target names
        :rtype: dict[str, str]
        """

class ComponentJointMapper:
    """we wanta a generic visualizer to map component or component parts to an existing skeleton
    All existing joints get a visualizer that is non selectable. The closest root point will be 
    indicated with a ring and all joints that are to be mapped with be indicated with a slightly 
    different point icon and a different color. The visualizer will be used as a preview before
    changes to the tool are applied"""
    scene_viewer: hou.SceneViewer
    colors: ColorScheme
    drawables: DrawableSet
    skel: SkeletonData
    ref: ReferenceData
    mapping: MappingState
    near_pt: int | None
    near_name: str | None
    orig_name: str | None
    orig_pt: int | None
    root_xf: hou.Matrix4
    snap_dist: float
    drag_snap_dist: float
    paths: dict[str, list[str]]
    rename_pattern: None
    ui_parms: apex.Dict
    ray_graph: apex.Graph
    reference_graph: apex.Graph
    parent_matched: list[tuple[str, str]]
    removing: bool
    delete_removed: bool
    drag_mode: bool
    dragging: bool
    tag: str
    parent_drag: bool
    def __init__(self, scene_viewer: hou.SceneViewer, state: _AnimateState, **kwargs: object) -> None: ...
    @property
    def state(self) -> _AnimateState | None: ...
    @property
    def cursor_icon(self) -> CursorIcon | NullCursorIcon:
        """Get cursor icon from state, or null object if unavailable."""
    @property
    def pick_walker(self) -> PickWalker | NullPickWalker:
        """Get pick walker from state, or null object if unavailable."""
    @property
    def cursor_font_size(self) -> float:
        """Get cursor font size from state, or default if unavailable."""
    def setCursorDescription(self, description: str) -> None:
        """Set cursor description on state if available."""
    def updateLineGeo(self, a: hou.Matrix4, b: hou.Matrix4) -> None:
        """Update map line positions from transform matrices."""
    def jointPattern(self, joints: list[str] | None = None, exclude: bool = True) -> str:
        """Generate group pattern via MatchingHelpers."""
    def setSkeleton(self, skeleton: hou.Geometry | None = None, excluded_joints: list[str] | None = None) -> None:
        """updates the skeleton that we want to map our new skeleton elements to"""
    def setColor(self, color: hou.Vector4) -> None:
        """store teh current colors for the base skeleton. defaults to black"""
    def setLightMode(self, on: bool) -> None:
        """applies the light colors for the color mapping mode. to match the skeleton colors better"""
    def genRefJointChain(self, default_joints: Sequence[str], height: float, direction: hou.Vector3 = ...) -> hou.Geometry:
        """automatically generates a reference skeleton joint chain. this can be helpful for components with varying
        amounts fo joints like spines
        """
    def setRefSkeleton(self, skeleton: hou.Geometry, root: str | None = None, offset: hou.Vector3 | None = None) -> None:
        """updates the template skeleton that we want to map to our current main skeleton
        with the given drag interaction

        :param skeleton: _description_
        :param pattern: _description_, defaults to None
        """
    def setJoint(self, name: str | None = None, xform: hou.Matrix4 | None = None) -> None:
        """sets the current selected reference joint that we use as the root for any mapping operation

        :param name: _description_, defaults to None
        :param xform: _description_, defaults to None
        """
    def getMappingWithVariadic(self) -> tuple[BijectiveMap[str, str], dict[str, list[tuple[str, str]]], dict[str, str]]:
        """Build a BijectiveMap extended with variadic pair mappings.

        Mirrors the format of ar.getMappingWithVariadic() using the gadget's
        existing mapping state and variadic match data.

        :return: (BijectiveMap, variadic_input dict, ref_renames dict)
        """
    def sortMapKeys(self) -> list[str]:
        """sort the mapping entry based on hierarchical order of the reference rig"""
    def getSkelRoot(self, default_parent: bool = True) -> str | None:
        """find the root joint of a currently given reference skeleton, the given root is used to attach the 
        mapping root to"""
    def setExcludePattern(self, excluded_joints: list[str] | None = None) -> None:
        """defines which joinst are to be excluded from the default visualizer"""
    def nearestSkelPt(self, distance: float | None = None, set_nearpoint: bool = True) -> str:
        """
        project the skeleton to the current view plane and find the point closest 
        to the rayed mouse position
        """
    def nearestRefPt(self) -> str:
        """
        find the closest reference joint to the current mouse position. we can use this to show the name of the closest
        reference joint
        """
    def updateRefSkel(self) -> None:
        """
        project the skeleton to the current view plane and find the point closest
        to the rayed mouse position
        """
    def setPreviewJoints(self, names: list[str] | None, reference_names: list[str] | None, descendants: list[str] | None = None) -> None:
        """sets the joint group patterns for the highlighting of the reference skeleton and generates the pt num 
        lists that are used to isolated the same groups for the geometry drawalbes

        :param names: _description_
        :param orig_names: _description_
        :param descendants: _description_, defaults to None
        """
    def setOffset(self, update: bool = False, offset: hou.Vector3 | None = None, current_xform: hou.Matrix4 | None = None) -> None:
        """the reference xform offset is being used to """
    def translateRefJoints(self, joints: list[str], xform: hou.Matrix4 | None = None, start_xform: hou.Matrix4 | None = None, xforms: apex.Dict | None = None, exclude_mapped: bool = True) -> None:
        """applies an xform offset to the reference joints. this is important for template mappings
        otherwise the template might be placed per default exactly on top of the existing guide skeleton. we also
        need it to place the gadget at a dedicated location when we position fully unmapped elements"""
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDraw(self, handle: int) -> None: ...
    def show(self, on: bool) -> None:
        """show or hide the overall gadget. Setting the gadget to invisible also suppresses all interactions"""
    def resolveOverlap(self) -> None:
        """handles joints that are share the same position and gives them a subtle offset
        for better mapping selection opionts"""
    def reset(self) -> None:
        """resets the skeleton positions back to the default postions we need this since we might modify the skel
        positions to show overlapping joints better. overlapping joints only get resolves for the closest joints"""
    def isVisible(self) -> bool: ...
    def onPreLocateEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """we do need to fully block the mouse event of the animation state based on
        the pre locate event"""
    def applyDrag(self, reason: hou.EnumValue[hou.uiEventReason], device: _ModifierKeys) -> None:
        """applies the given mapping for the drag action on mouse drag and up. We need a seperate function
        Since the mouse up event for the assetbrowser drag handling is not being handles via the mouse event"""
    def updateRemoved(self, jnt: str, toggle: bool = True, add: bool = True, clear: bool = False) -> None:
        """Update the removed joints list via MappingState."""
    def autoRemove(self) -> None:
        """Auto-generate removed joints list via MappingState."""
    def removedPattern(self) -> str:
        """Get removed joints group pattern via MappingState."""
    def setNonDragMode(self, device: _ModifierKeys) -> None: ...
    def setDragMode(self, device: _ModifierKeys) -> None:
        """we do have special shift activation when we use drag matching to dynamicly switch to parent mode"""
    def setMode(self, mode: str | None = None, update: bool = True) -> None:
        """defines how how much of the hierarchy is to be mapped. valid option are:
        single: only mapps the current reference joint to the nearest joint
        branch: maps the chain up to the next branch from the reference joint based on the nearest joints
        hierarchy: maps the full hierarchy of the current join to the nearies joint

        if the mode is none than matchin is disabled
        """
    def onParentMatch(self, reason: hou.EnumValue[hou.uiEventReason], device: _ModifierKeys, move: bool = False) -> None:
        """handles the operations where we want to set the parent of the overall new skeleton
        

        :param reason: _description_
        :param device: _description_
        :param move: _description_, defaults to False
        """
    def setRoot(self) -> None: ...
    def findRoots(self) -> list[str]:
        """finds the root joint names of the reference skelton that we want to map to the existing skeleton"""
    def firstRefRoot(self) -> str:
        """Get first reference root joint name safely.

        :return: First root name, or empty string if none
        :rtype: str
        """
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def getPickWalkData(self, rig_path: str) -> PickWalkRig | Literal[False]:
        """ Get the pick walk data for the given rig path. """
    def onHierarchyMatch(self, reason: hou.EnumValue[hou.uiEventReason], device: _ModifierKeys, single_mode: bool | None = None) -> None: ...
    def snapMatched(self) -> None:
        """adjusts the positions of the reference skeleton joints, based on the 
        """
    def refPath(self, joint: str) -> str:
        """Generate reference joint path via MatchingHelpers."""
    def skelPath(self, joint: str) -> str:
        """Generate skeleton joint path via MatchingHelpers."""
    def clear(self, clear_drawables: bool = False) -> None:
        """Clears all the stored data of the current instance and resets all the drawables."""
    def findBodyside(self, tolerance: float = 0.3) -> int:
        """Check if current mapping is on left, right, or center body side.

        :param tolerance: Relative tolerance for body side detection
        :return: 0 if left, 1 if right, 2 if centered
        """
    def findXform(self, jointname: str | None = None) -> hou.Matrix4:
        """returns the xform position of a currently applied reference skeleton joint. 
        If no jointname is given the xform position of the root will be returned
        :param jointname: the name of the joint to be used, defaults to None, which implies that 
        the roots xform will be returned
        """
    def findRefRestXf(self, jointname: str | None = None) -> hou.Matrix4:
        """returns the rest xform position of a currently applied reference skeleton joint. 
        If no jointname is given the rest xform position of the root will be returned. Teh rest xform can be used to 
        apply the current xform as a local
        :param jointname: the name of the joint to be used, defaults to None, which implies that 
        the roots rest xform will be returned
        """
