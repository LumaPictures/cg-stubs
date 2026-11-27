import _apex
import apex
import hou
import typing
from apex.apexutils import BijectiveMap as BijectiveMap
from apex.stateparmutils import _AnimateState as _StateParmUtilsState
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from typing import Concatenate, Literal, Protocol
from typing_extensions import TypedDict

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_T = TypeVar('_T')
class _AnimateState(_StateParmUtilsState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    def getControlSelectors(self, set_visibility: bool = ...) -> None: ...
    def getControlsByRig(self, control_paths: Iterable[str] | None = ...) -> dict[str, list[str]]: ...

class _GalleryComponentKwargs(TypedDict, total=False):
    initialize: bool
    label: str
    version: str
    core: str
    namespace: str
    icon: str
    categories: str | None
    savesource: bool

SELECT_JOINTTAG_TOOL: str
LOCATE_JOINTTAG_TOOL: str
SELECT_JOINTS_TOOL: str
SELECT_JOINT_TOOL: str
SELECT_CONTROLS_TOOL: str
MAP_JOINTS_TOOL: str
MAP_COMPONENT_TOOL: str
TAG_COMPONENT_TOOL: str
COMPONENT_TOOL: str
ADD_TAG_TOOL: str
MODIFY_TAG_TOOL: str
MODIFY_MAPPING_TOOL: str
ADD_MAPPING_TOOL: str
ANIMATION_PARM: str
VIEWPORT_PARM: str
GUIDES_STASH_PARM: str
RIG_STASH_PARM: str
RIGPARM_STASH_PARM: str
SHAPESPARM_STASH_PARM: str
CACHE_PARM_WHITE_LIST: list[str]
DELAYED_PARM_LIST: list[str]
CACHE_PARMS: list[str]
RIG_SHOW_PARM: str
GUIDES_SHOW_PARM: str
SHAPES_SHOW_PARM: str
APPLY_SHAPES_PARM: str
RIG_NAME_PARM: str
SKEL_NAME_PARM: str
SHAPE_NAME_PARM: str
BUILDRIG_PARM: str
PRIMARY_AXIS: str
SECONDARY_AXIS: str
LEFT_PARM: str
RIGHT_PARM: str
GUIDES_NODE: str
RIG_NODE: str
SHAPES_NODE: str
GUIDE_RIG_NODE: str
PROCESSED_RIG_NODE: str
CONFIG_FUNCTION: str
GUIDES_NODE_CONFIG: str
RIG_NODE_CONFIG: str
SHP_NODE_CONFIG: str
ANIM_NODE_CONFIG: str
AUTORIG_PARMS: list[str]
TWEAK_MODE: str
RIG_MODE: str
INPUT_SKELETON: str
INPUT_TEMPLATE_NODE: str
INPUT_TEMPLATE: str
INPUT_SKELETON_FIT: str
REST_GUIDES_SKEL: str
INPUT_GUIDES_SKEL: str
GUIDES_CHAR: str
GUIDES_RIG: str
RIG_CHAR: str
RIG_RIG: str
SHAPES_CHAR: str
GUIDE_MODE: str
GUIDE_TAG_MODE: str
RIG_TAG_MODE: str
DUAL_TAG_MODE: str
SEGMENT_PARM: str
ROOT_COMPONENT: str
GALLERY_SOURCE_IDENTIFIER: str
GALLERY_SOURCE_FILENAME: str
DEFAULT_ICON_PATH: str
INPUT_ICON_PATH: str
RIGGING_BUTTON_PREFIX: str
GUIDES_KEY: Literal['guides']
GUIDE_TYPE_KEY: Literal['guide_type_data']
DEFAULT_NAMES_KEY: str
NUMELEMENTS_KEY: str
DEFAULT_LENGTH_KEY: str
DEFAULT_DIRECTION_KEY: str
REMOVE_UNMAPPED_KEY: str
initialized: bool

def initGallerySource(path: str | None = None, force: bool = True, clear: bool = False) -> None: ...
def hasAssetGallerySource() -> bool:
    """checks if a given component asset catalog already exists"""
def saveGallerySource(path: str | None = None) -> None:
    """saves the assetbrowser data source """
def clearGallerySource(path: str | None = None) -> None:
    """clears all entries from the assetbrowser"""
def saveComponentToGallery(kwargs: _GalleryComponentKwargs) -> None:
    """adds a given component to the assetbrowser data source or updates the component accordingly"""
def nodeIsRigable(node: hou.OpNode) -> bool:
    """
    only returns true if the given node has all the given parm to 
    interact with it with the autorig state, we on purpose rather check
    for the parms and not for node types to stay node agnostic 
    """
def characterElementPath(character_name: str, element_name: str, extension: str | None = None) -> str:
    """
    quick way to assemble the path to our state specific rig elements. based on the 
    character and element name 
    """
def recreateRig(state: _AnimateState, rig_path: str, packed_folder: hou.Geometry, update_geo: bool = False, update_selection_sets: bool = False) -> apex.SceneGraph | None:
    """reloads a single rig entry of the current scene animate scene"""
def addCharacter(state: _AnimateState, rig_path: str, packed_folder: hou.Geometry, exclude: bool = True, exclude_paths: Iterable[str] | None = None) -> None:
    """adds a new character to the rig state. This is necessary if the rig state is active we are starting
    without a skeleton input. In that case the guide and animation test rig both do not exist and need to be initialized

    :param state: _description_
    :param rig_path: _description_
    :param packed_folder: _description_
    :param exclude: _description_, defaults to True
    :param exclude_paths: _description_, defaults to None
    """
def checkSkeletonScaleReflection(left_pts: Sequence[hou.Point], right_pts: Sequence[hou.Point]) -> Literal[0, 1, 2]:
    """checks if a given skeleton uses reflected scaling
    returns 0 if no reflected scales exist, returns 1 if right is reflected and 2 if left is reflected"""
def checkRootScale(skel: hou.Geometry) -> bool:
    """Returns True if the skeleton has non-default scaling on any root control."""
def checkSkeletonNames(skel: hou.Geometry, group: str, name_pattern: str = '') -> bool:
    """checks if the names of all joints in a dedicated joint group match a given name pattern
    returns True if all match and false if some joints do not Match"""
def checkSkeleton(skel: hou.Geometry, left_pattern: str, right_pattern: str, scale: bool = True, names: bool = True, patterns: bool = True) -> tuple[str | None, hou.EnumValue[hou.severityType] | None]:
    """a wrapper that checks a given skeleton based on various criteria: Returns true if the given skeleton is valid
    returns otherwise an error message specific to the found issues."""
def settingsFromSkeleton(node: hou.SopNode, skel: hou.Geometry, use_confirm_dialog: bool = True, force: bool = True) -> bool:
    """collect info about body side indicators and the primary axis

    :param skel: the skel to analyze
    :return: _description_
    """
def selectionToPattern(state: _AnimateState) -> str: ...
def patternToControls(state: _AnimateState, rig_path: str, pattern: str) -> list[str]:
    """
    converts an apex path pattern to a list of valid control paths for a given rig
    :param state: the animate state, 
    :param rig_path: the path to the rig that we want to check the apex pattern for
    :param pattern: the apex pattern to use to filter out the controls from the given rig
    """
def rgb2hex(r: float, g: float, b: float) -> str: ...
def setNewColorFromPalette(node: hou.SopNode, num_parms: int, idx: int) -> hou.Vector4:
    """
    Look at the previous entries in the multiparm, remove them from the
    palette, then sample the palette for a new color not used recently,
    then write the index in the palette into the multiparm and write the
    actual color as well.

    :param node: The autorig builder SOP node.
    :param num_parms: The number of multiparms including the new one
                      just added.
    :param idx: The index into the multiparm of the instance just added.
    """
def getMappingFromAttrib(ref_skel: hou.Geometry, attribname: str = 'mapping', guides_geo: hou.Geometry | None = None) -> BijectiveMap[str, str]:
    """Build a BijectiveMap mapping point names to values from a dict-typed point attribute.

    :param ref_skel: Reference skeleton geometry holding the mapping attribute.
    :param attribname: Name of the dict-typed point attribute to read.
    :param guides_geo: Optional guides geometry. When provided, a mapping is
        only kept if its guide-side name actually exists on the guides skeleton
        (mirrors getMappingFromNames). Without it no existence check is done.
    """
def getMappingFromNames(ref_skel: hou.Geometry, guides_geo: hou.Geometry) -> BijectiveMap[str, str]:
    """Build a BijectiveMap from direct name-to-name matches between ref and guides skel.

    Same key direction as getMappingFromAttrib: result[guide_name] = ref_name
    (so result.inverse[ref_name] = guide_name). For name-mode the two are equal.
    """

class VariadicPairInfo:
    """Info about a variadic pair span in a reference skeleton.

    Represents a contiguous chain of joints between a variadic start and
    variadic end joint, where the in-between joints should be removed on
    match and replaced with numbered variadic entries.
    """
    pair_name: str
    start: str
    end: str
    between: list[str]
    def __init__(self, pair_name: str, start: str, end: str, between: list[str]) -> None: ...

def scanVariadicPairs(ref_skel: hou.Geometry | None) -> dict[str, VariadicPairInfo]:
    """Scan a reference skeleton for variadic pair markers.

    Looks for joints with a point dict attribute 'properties' containing
    a 'variadic' key. Joints sharing the same variadic pair name are paired,
    with the ancestor as start and descendant as end.

    :param ref_skel: Reference skeleton geometry
    :return: Dict mapping pair_name to VariadicPairInfo
    """
def _collectTrailingShifts(ref_skel: hou.Geometry, info: VariadicPairInfo, delta: int) -> dict[str, tuple[int, str]]:
    """Find ref-side joints past info.end matching end_base_NN with NN > end's
    number, return {old_name: new_name} shifted upward by delta.

    Used when the guide chain extends the variadic span past info.end so the
    trailing numbered joints don't collide with the variadic intermediates.
    """
def getMappingWithVariadic(ref_skel: hou.Geometry, guides_geo: hou.Geometry, attribname: str = 'mapping') -> tuple[BijectiveMap[str, str], dict[str, list[tuple[str, str]]], dict[str, str]]:
    """Build a BijectiveMap that includes variadic pair mappings.

    Extends getMappingFromAttrib by scanning for variadic pairs on the
    reference skeleton. For each pair, inbetween joints on the guides
    geometry are mapped using the end joint name with a zero-padded index
    (e.g. 'spine_end_00', 'spine_end_01', ...).

    When the guide chain is longer than the reference variadic span and the
    reference has trailing numbered joints past info.end (e.g. spine_04,
    spine_05 past a spine_03 end marker), those trailing joints are shifted
    upward in the BijectiveMap by the chain delta so the variadic
    intermediates can occupy spine_01..spine_(N+1) without clobbering the
    trailing attrib-driven mappings. The returned ref_renames dict captures
    those shifts so downstream code can redirect references to the original
    names.

    Also returns a variadic_input dict keyed by pair_name, where each value
    is an ordered list of (guide_joint, default_name) tuples:
      - ('guide_start', 'start')
      - ('guide_between_0', 'start_0'), ('guide_between_1', 'start_1'), ...
      - ('guide_end', 'end')

    :param ref_skel: Reference skeleton geometry
    :param guides_geo: Guides input geometry
    :param attribname: Name of the mapping attribute on ref_skel. The special
        value 'name' selects a direct name-to-name match between ref_skel and
        guides_geo instead of reading a dict-typed mapping attribute.
    :return: (BijectiveMap, variadic_input dict, ref_renames dict)
    """
def parmTemplatesCachePath() -> str: ...
def writeParmTemplatesCache() -> None: ...
def ensureParmTemplatesCache() -> None:
    """Guarantee the parmtemplates .bgeo exists on disk. Cheap when it does."""
def loadParmTemplatesGeo() -> hou.Geometry: ...
def reloadComponents() -> None: ...

class ComponentData:
    name: str
    label: str
    deprecated: int
    deprecatedmsg: str
    hidden: int
    def __init__(self, name: str = '', label: str = '', deprecated: bool = False, deprecatedmsg: str = '', hidden: bool = False) -> None: ...
    def basename(self) -> str: ...
    def version(self) -> str: ...
    @staticmethod
    def splitNameAndVersion(full_name: str) -> tuple[str, str]: ...
    @staticmethod
    def fromGeo(geo: hou.Geometry) -> ComponentData: ...

class GuideComponentData(ComponentData):
    """manages the guide component data. 
    """
    guides: hou._OptionDict | Literal[False] | None
    reference_skeleton: hou.Geometry | None
    reference_left: str
    template_data: hou._OptionDict | None
    reference: str | None
    guide_type: str | None
    guide_type_data: dict[str, _apex._PlainValue | None]
    interface: hou._OptionDict
    configurecontrols: hou._OptionDict
    def __init__(self, name: str = '', label: str = '', deprecated: bool = False, deprecatedmsg: str = '', hidden: bool = False) -> None: ...
    @staticmethod
    def fromGeo(geo: hou.Geometry, path: str | None = None, subgraph_reg: apex.Registry | None = None, include_interface: bool = False) -> GuideComponentData: ...
    def getComponentToolName(self, reselect: bool = False) -> str: ...

class GuideComponentCache:
    """query information about the current components data"""
    registry: apex.Registry
    standard_registry: apex.Registry
    component_map: dict[str, GuideComponentData]
    invalid_components: list[str]
    def __init__(self) -> None: ...
    def getSkeleton(self, component_name: str) -> hou.Geometry | None: ...
    def getTemplate(self, component_name: str) -> hou._OptionDict | None: ...
    def getConfigureControls(self, component_name: str) -> hou._OptionDict | None: ...
    def setData(self, component_name: str) -> bool: ...
    @typing.overload
    def getData(self, component_name: str, attrib_name: None = ...) -> GuideComponentData | None: ...
    @typing.overload
    def getData(self, component_name: str, attrib_name: Literal['name', 'label', 'deprecatedmsg', 'reference_left']) -> str | None: ...
    @typing.overload
    def getData(self, component_name: str, attrib_name: Literal['deprecated', 'hidden']) -> int | None: ...
    @typing.overload
    def getData(self, component_name: str, attrib_name: Literal['reference', 'guide_type']) -> str | None: ...
    @typing.overload
    def getData(self, component_name: str, attrib_name: Literal['guides']) -> hou._OptionDict | Literal[False] | None: ...
    @typing.overload
    def getData(self, component_name: str, attrib_name: Literal['template_data', 'interface', 'configurecontrols']) -> hou._OptionDict | None: ...
    @typing.overload
    def getData(self, component_name: str, attrib_name: Literal['reference_skeleton']) -> hou.Geometry | None: ...
    @typing.overload
    def getData(self, component_name: str, attrib_name: Literal['guide_type_data']) -> dict[str, _apex._PlainValue | None] | None: ...
    def clear(self) -> None: ...
    def reloadAssetGalleryEntries(self, force: bool = True) -> None: ...

class AutoRigNodeManager:
    """
    manages the update behavior of an APEX Autorig SOP node or a node using that system inside
    The updating can be specifically controled when used in the viewport. 
    We do want to pypass any temporary stashed when the state is not aktive. This allows us 
    to be fully procedural on sop level but more performant based on caching when in the viewport
    if a given node does not pass the requirements for the full interactive state behavior, the allow_non_interative flag 
    allows to the manager to be used on nodes that do not match the full requirements and any functions requiring stashing
    will just be silently ignored. 
    """
    node: hou.SopNode | None
    node_config: dict[str, str]
    is_valid: bool
    rig_mode: str
    allow_non_interactive: bool
    parm_CB: None
    rig_geo: hou.Geometry
    shp_geo: hou.Geometry
    guide_geo: hou.Geometry
    guide_rig_geo: hou.Geometry
    def __init__(self, node: hou.SopNode | None, allow_non_interative: bool = True) -> None: ...
    @staticmethod
    def exceptionHandler(func: Callable[Concatenate['AutoRigNodeManager', _P], _R]) -> Callable[Concatenate['AutoRigNodeManager', _P], _R | None]:
        """
        only executes the function if the node manager has a valid modifyable node. otherwise an error will be raised
        the error can be bypassed with the self.allow_non_interactve instance vars
        """
    def setNode(self, node: hou.SopNode | None) -> None:
        """sets the hou node that is to be treated as an autorig node 

        :param node: _description_
        """
    def guideRigPath(self) -> str: ...
    def shapeRigPath(self) -> str: ...
    def animRigPath(self) -> str: ...
    def animCharPath(self) -> str: ...
    def guideCharPath(self) -> str: ...
    def guideSkelName(self) -> str: ...
    def clear(self) -> None: ...
    def nodeIsRigable(self) -> bool:
        """
        only returns true if the given node has all the given parms to 
        interact with it with the autorig state, we on purpose rather check
        for the parms and not for node types to stay node agnostic. We also allow that all the given parm names 
        can be overriden by the config
        """
    def getConfig(self) -> dict[str, str]:
        """
        get the state config dict of the current node's python script module. We can use this to allow the 
        user to overwrite some of the nodes that we look for in an implementation
        and we can use this to use the animate state within other hdas
        """
    @typing.overload
    def getConfigValue(self, key: str | None, default: None = ...) -> str | None: ...
    @typing.overload
    def getConfigValue(self, key: str | None, default: _T) -> str | _T: ...
    def getParm(self, name: str) -> hou.Parm | None:
        """get the node paramater of your current node base on the parm name and use the config override for the 
        parm name if one exist. 
        NOTE: we currently to not raise any errors if the given parm does not exist since we already check for the 
        existance of all parms when we set the current node
        :param name: the name of the parm to be fetched
        :return: hou.Parm
        """
    def getPrimaryAxis(self, default: hou.Vector3 = ...) -> hou.Vector3: ...
    def getSecondaryAxis(self, default: hou.Vector3 = ...) -> hou.Vector3: ...
    @exceptionHandler
    def getNodeGeometry(self, node_name: str, config_key: str | None = None, force: bool = False) -> hou.Geometry:
        """
        recooks and then fetches the current geometry of a given stage in the rigging process from a node inside our
        current hda.

        :param node_name: the name of the node inside our hda that we want to fetch the geo from
        :param config_key: allows us to fetch a user defined name for that node from the config, defaults to None
        :return: _description_
        """
    @exceptionHandler
    def getNodeInputGeometry(self, idx: int = 0, element_name: str | None = None) -> hou.Geometry:
        """
        fetches the given input geometry or a given input geometyr element of the current node

        :param node_name: the name of the node inside our hda that we want to fetch the geo from
        :param config_key: allows us to fetch a user defined name for that node from the config, defaults to None
        :return: _description_
        """
    @exceptionHandler
    def showRig(self, on: bool = True) -> None:
        """
        add or removes the final rig of the character in the viewport 
        :param on: defines if the final rig character is to be added or removed from the viewport, defaults to True
        """
    def rigVisible(self) -> int | None: ...
    @exceptionHandler
    def toggleShape(self, on: bool = True) -> None:
        """toggles if we see the current rig result of the control shape rig"""
    @exceptionHandler
    def showGuides(self, on: bool = True) -> None:
        """shows or hides the guide rig"""
    @exceptionHandler
    def updateGuides(self, force: bool = False, set_cache: bool = True) -> hou.Geometry | None:
        """updates the guides caches to the latest parms and setting from the viewport interaction"""
    @exceptionHandler
    def updateRig(self, update_guides: bool = False, force: bool = True, set_cache: bool = True, use_shape: bool = False) -> hou.Geometry | None:
        """updates cache of the rig generated by the guides to the latest guide settings"""
    @exceptionHandler
    def updateGuideRig(self, update_guides: bool = False, force: bool = True) -> hou.Geometry | None:
        """updates cache of the rig generated by the guides to the latest guide settings"""
    def updateShape(self, force: bool = True) -> None: ...
    @exceptionHandler
    def setRigMode(self, state: _AnimateState, mode: str | None = None, force: bool = False, ui_update: bool = True) -> None: ...
    def clearCaches(self) -> None:
        """
        clears all intermittent geo caches that we store on the node in order to improve performance while we are 
        interacting with the node. We always want to clear all caches as soon as we exit the node. 
        """
    def loadCaches(self, state: _AnimateState, set_mode: bool = False) -> bool: ...
    def reload(self, state: _AnimateState, update_rig: bool = True, force: bool = False, reload_scene: bool = False) -> None:
        """reloads the guide rig and optionally the animation test rig of the rig state
        this is a surgical update. We avoid a full scene reload in order to reduce the refresh time
        for the characters. 

        :param state: the animation viewer state
        :param update_rig: defines if the test animation rig is to be reloaded, defaults to True
        :param force: defines if the geometry for the rigs needs to be recooked, defaults to False
        :param reload_scene: saves the animation before doing a full reload of the guide and test animation rig, defaults to False
        """
    @exceptionHandler
    def reloadRig(self, state: _AnimateState, force: bool = False, update_geo: bool = True, forc_update: bool = False) -> None: ...
    @exceptionHandler
    def reloadGuideRig(self, state: _AnimateState, force: bool = False, update_geo: bool = True, forc_update: bool = False) -> None: ...
    @exceptionHandler
    def reloadShapeRig(self, state: _AnimateState, force: bool = False, update_geo: bool = True, forc_update: bool = False) -> None: ...
    @exceptionHandler
    def showChar(self, state: _AnimateState, path: str, on: bool = True) -> None: ...
    @exceptionHandler
    def setInteractive(self, on: bool = True, state: _AnimateState | None = None) -> bool: ...
    def getReferenceShape(self) -> hou.Geometry | None:
        """
        gets the input reference shape before any deformation. 
        we use this as the ground zeroe reference shape to know where to place joints
        """
    def getGuidesByPattern(self, scene: apex.Scene, map_filter: str) -> list[str]:
        """
        we need to define the guide controls that we actually want to map. 
        All other guide joints need to be unselectable. this step only applies for guides
        that already have been added
        """
    def getInputTemplateDict(self) -> hou._OptionDict | None:
        """returns the input template dict """
    def getInputTemplateSkeleton(self, offset: hou.Vector3 | None = None) -> hou.Geometry: ...
    @exceptionHandler
    def setNewSegmentColor(self, idx: int | None = None) -> hou.Vector4:
        """apply a new random color for the new segment to be added"""
    def getSegmentNames(self) -> list[str]: ...
    @exceptionHandler
    def isUniqueSegmentName(self, name: str, warn: bool = True) -> bool: ...
    @exceptionHandler
    def getUniqueSegmentName(self, name: str) -> str:
        """create a unique name entry for the new segment"""
    @exceptionHandler
    def resetControls(self, state: _AnimateState, segment: str) -> None:
        """
        resets the controls associated with e given segment
        of both the guide and the anim test rig back to the default values 
        :param segmet: the name of the segment to be reset
        """
    def matchGuides(self, state: _AnimateState, segment: str, reference_mapping: apex.Dict, mapping: Mapping[str, str]) -> None:
        """match the guide controls to the matching reference skeleton transforms. This is being used to 
        make sure that new joints are b

        :param state: _description_
        :param segment: the current segment where we want to update the guide positions
        :param reference_mapping: _description_
        :param mapping: _description_
        """
    def validateGuides(self, skel: hou.Geometry | None = None) -> Literal[0, 1, 2] | None:
        """checks if the given skeleton uses uses rotational mirroring. Returns false if the mirror is based on 
        flipped scales
        :param skel: the skeleton to be validated, defaults to None
        :return: True if the skeleton has rotational mirroring or no mirroring, False if negative skaling can be found
        """
    @exceptionHandler
    def settingsFromGuides(self, use_confirm_dialog: bool = True) -> bool:
        """collect info about body side indicators and the primary axis

        :param skel: the skel to analyze
        :return: _description_
        """
    @exceptionHandler
    def getInputGuides(self) -> hou.Geometry | None:
        """get guides skel before processing
        """
    @exceptionHandler
    def renameSegment(self, segment_name: str, new_segment_name: str) -> tuple[str, str] | tuple[None, None]:
        """renames a component and updates all the guide positions

        :param segment_name: _description_
        :param new_segment_name: _description_
        :return: _description_
        """
    @exceptionHandler
    def renameBodySides(self, left: str | None = None, right: str | None = None) -> tuple[str, str] | tuple[None, None]:
        """renames a component and updates all the guide positions

        :param segment_name: _description_
        :param new_segment_name: _description_
        :return: _description_
        """
    def getSegmentIndex(self, multiparm: hou.Parm, segment_name: str, numInstances: int | None = None) -> int:
        """return the multiparm index of a segment based on its segment name"""
    @exceptionHandler
    def insertSegment(self, segment_name: str, component_name: str, mapping: Mapping[str, str] | None = None, sorted_keys: Sequence[str] | None = None, root: str | None = None, removed: str | None = None, tags: str | None = None, t: hou.Vector3 | None = None, r: hou.Vector3 | None = None, s: hou.Vector3 | None = None, mirror: bool | None = None, numelements: int | None = None, multiparm_idx: int | None = None) -> tuple[int, hou.Vector4]:
        """Insert a new segment into the multiparm and set all its parameters.

        Pure node operation — no callbacks, undo groups, gadgets, or reload.

        :return: Tuple of (1-based multiparm index, color hou.Vector4)
        """
    @exceptionHandler
    def updateSegmentParms(self, segment_name: str, component_name: str | None = None, parent: str | None = None, mapping: Mapping[str, str] | None = None, removed: str | None = None, tags: str | None = None, mirror: bool | None = None, numelements: int | None = None, t: hou.Vector3 | None = None, r: hou.Vector3 | None = None, s: hou.Vector3 | None = None, segment_index: int | None = None) -> bool:
        """Compare and update only changed parameters on an existing segment.

        Pure node operation.

        :param segment_index: Optional 0-based index if already known, skips internal lookup.
        :return: True if any parameter was changed
        """
    @exceptionHandler
    def reorderSegments(self, desired_order: Iterable[str], current_names: list[str] | None = None) -> bool:
        """Reorder multiparm instances to match desired_order.

        Enforces skeleton fit at index 0 and root component right after,
        matching the insertion logic in addSegment.

        :param desired_order: Full list of segment names in desired order
        :param current_names: Optional pre-built names list to skip internal lookup.
        :return: True if reordering was performed
        """
    @exceptionHandler
    def saveSegmentNames(self) -> None:
        """saves all the relevant """

class OrientationManager:
    """manages orientation updates of selected controls based on a matching transformed skeleton"""
    skeleton: hou.Geometry | None
    secondary_axis: hou.Vector3
    primary_axis: hou.Vector3
    rig_path: str
    compute_local: hou.SopVerb
    def __init__(self, rig_path: str, primary_axis: hou.Vector3 = ..., secondary_axis: hou.Vector3 = ...) -> None: ...
    def setSkeleton(self, skeleton: hou.Geometry) -> None:
        """sets and sorts the skeleton to be checked for for the orientation"""
    def orientJoint(self, pt: hou.Point, child: hou.Point | None = None, refsecondary: hou.Vector3 | None = None, up: hou.Vector3 | None = None) -> hou.Matrix4:
        """orients a single joint to a specified child"""
    def orientJoints(self, group: str, ignore_multi_parents: bool = True, rig_path: str | None = None) -> dict[str, hou.Matrix4]:
        """orients a group of joints to its given parent
        the updated xforms get collected in a joint -> xform dictionary which is returned
        by this method"""
    def orientControls(self, state: _AnimateState, controls: Sequence[str] | None = None) -> None:
        """
        orients a selection of joints based controls with the given set primary and secondary
        axis defined by the orientation manager.
        We use the given current skeleton as the helper to calculate the orientation
        so it is important to use the setSkeleton function to provide a skeleton with a matching hierarchy
        and transformation that matches the current controls
        """
    def aimControls(self, state: _AnimateState, controls: Sequence[str] | None = None) -> None:
        """aims a given control to the primary control. This action requires 2 controls
        to be selected"""
