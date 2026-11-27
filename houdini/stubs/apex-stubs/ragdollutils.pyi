import _apex
import apex
import hou
import typing
from _apexscene import Control as Control, ControlManager as ControlManager
from apex import mapping_2 as mapping
from apex.bake import BakeSourceParmsBase as BakeSourceParmsBase, BakeSourceXformBase as BakeSourceXformBase
from apex.ragdollbase import RagdollStateBase as RagdollStateBase
from apex.scene_2 import Scene as Scene, getGeometryInputCallbacksDefaults as getGeometryInputCallbacksDefaults
from apex.ui.animationhudwidgets import RESET_MODIFIER as RESET_MODIFIER
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from enum import StrEnum
from houtypes import ViewerStateEventKwargs
from spriteutils import SpriteGadget
from typing import Callable as Callable, Literal, Sequence

from typing import TypeAlias
from typing import TypeVar
from collections.abc import Hashable
from collections.abc import Sized
from typing import TypeAlias
from typing import TypeVar
_K = TypeVar('_K')
_S = TypeVar('_S', bound=Sized)
_H = TypeVar('_H', bound=Hashable)
_T = TypeVar('_T')
_ShapeSelection: TypeAlias = dict[hou.SimpleDrawable, Sequence[hou.Prim]]
RAGDOLL_SOLVERPARMS: _apex.Dict

def defaultTimestep() -> float:
    """The default timestep which should be used for the solver."""

DEFAULT_GRAVITY: hou.Vector3
RAGDOLLPOSE_SOLVERPARMS: _apex.Dict
VISUALISER_VEX_SNIPPET: str
SLIDER_MOUSE_RESET_MODIFIER: dict[tuple[int, int], str]
MATCH_LOCAL_SHAPES_COLOR: hou.Vector3
MATCH_WORLD_SHAPES_COLOR: hou.Vector3
INACTIVE_SHAPES_COLOR: hou.Vector3
JOINTS_OUTSIDE_LIMITS_DEBUG_DRAWABLE_OUTLINE_COLOR: hou.Color

class RagdollProperties(StrEnum):
    VISUALISER_OFFSET = 'visualiser_offset'
    VISUALISER_OFFSET_HANDLE_PIVOT = 'visualiser_offset_handle_pivot'
    VISUALISER_OFFSET_HANDLE_VISIBILITY = 'visualiser_offset_handle_visibility'
    CONSTRAINTS_VISIBILITY = 'constraints_visibility'
    MATCH_WORLD_VISIBILITY = 'matchworld_visibility'
    BAKE_TO_NEW_LAYER = 'bake_to_new_layer'
    BAKE_START_FRAME = 'bakestartframe'
    BAKE_END_FRAME = 'bakeendframe'
    BAKE_INCREMENT = 'bakeinc'
    BAKE_ONLY_EXISTING = 'onlykeyexisting'
    DEBUG_INTERSECT = 'showshapeintersections'
    DEBUG_LIMITS = 'showshapesoutsidelimits'
    DISPLAY_MODE = 'display_mode'
    STASH_RIG = 'writerigtoscenegraph'
    GRAVITY = 'gravity'
    GROUND_POS = 'groundpos'
    GROUND_ROT = 'groundrot'
    GROUND_BOUNCE = 'groundbounce'
    GROUND_DISPLAY = 'grounddisplay'
    GROUND_ENABLE = 'groundenable'
    GROUND_FRICTION = 'groundfriction'
    ANGULAR_LIMIT_STIFFNESS = 'angularlimitstiffness'
    ANGULAR_LIMIT_DAMPING_RATIO = 'angularlimitdampingratio'
    CONSTRAINTS = 'constraints'
    CONSTRAINTS_CHANNELPRIMS = 'constraintschannels'
    FORCES = 'forces'
    TIMESTEP = 'timestep'
    STACK_CHANNELGEO = 'stack_channelgeo'
    STACK_LAYERDATA = 'stack_layerdata'
    STACK_LAYERNAMES = 'stack_layernames'
    STACK_ACTIVELAYER = 'stack_activelayer'

class RagdollParms(StrEnum):
    FORCERESETSIM = 'forceresetsim'
    NORESIMFRAME = 'disableresimframe'
    TIME = 'time'

SOLVER_NAME: str
OUTPUT_GEO_CHAR_NAME_ATTRIB_NAME: str
RAGDOLL_CHARACTER_CONFIGURATIONS_PROPERTY_KEY: str
UNDO_TAG: str
UNDO_SELECTION_TAG: str

def loadGeoFromFile(filepath: str) -> hou.Geometry: ...

RAGDOLL_CONFIGURATION_VISUALISERS_COMPILED_GRAPH_FILEPATH: str
RAGDOLL_COLLISION_SHAPE_INTERSECTIONS_COMPILED_GRAPH_FILEPATH: str
CONFIGURE_LIMITS_JOINTS_OUTSIDE_LIMITS_COMPILED_GRAPH_FILEPATH: str
collisionshape_intersections_compiled_graph_geo: hou.Geometry
joints_outside_limits_compiled_graph_geo: hou.Geometry
the_t_r_default: hou.Vector3
the_s_default: hou.Vector3

class RagdollGraphBase:
    """
    A set of static methods for performing various operations 
    on ragdoll and ragdoll pose graphs.
    NOTE: Most likely too late, 
    but this should be converted to an APEX Component
    """
    @staticmethod
    def buildGraph(solverParms: _apex.Dict, isPosingGraph: bool = False) -> _apex.Graph: ...
    @staticmethod
    def addCharacter(graph: _apex.Graph, source_char_name: str, isPosingGraph: bool = False) -> None: ...

def createChannelPrimGeo() -> hou.Geometry:
    """
    Create a new channelprims geometry that can get fed into the ragdoll solver callback.
    """
def findOrCreateChannel(channel_prims_geo: hou.Geometry, channel_name: str) -> hou.ChannelPrim:
    """
    Given a channel_prims_geo, return a channel prim by name or
    create a new one if it doesn't exist.
    """
def setChannelDefault(channel: hou.ChannelPrim, val: float) -> None: ...
def getChannelValue(channel_prims_geo: hou.Geometry, channel_name: str, frame: float = ...) -> float | None:
    """
    Given a channel_prims_geo, evaluate a particular channel, looked up by name, 
    at a frame and return its value. Returns None if the channel does not exist.
    """
def getChannelDataIds(geo: hou.Geometry) -> list[hou.AttribDataId]:
    """
    Returns a list of data ids which can be used to check for changes
    to the provided channel primitive geometry.
    """
def buildMotionClip(scene: Scene, rest_skel_path: str, output_skel_path: str, startframe: int, endframe: int, fps: float) -> hou.Geometry:
    '''
    Returns a new motionclip geometry.

    The rest_skel_path is a scene path pointing at the rest skeleton.
    The output_skel_path is an APEX graph output path. If the rest_skel_path is
    the graph\'s input, output_skel_path should be the output.

    The output_skel_path has the following format:
    "mychar.char/myrig.rig/myrig_graph_outputnode/Base.skel"
    '''
def _removeEmptyDictArrayEntry(d: dict[_K, _S]) -> dict[_K, _S]:
    """
    Remove all keys in the passed in dictionary that have an empty
    array as value.
    """
def selectionDictsCombine(d1: Mapping[hou.SimpleDrawable, Sequence[hou.Prim]], d2: Mapping[hou.SimpleDrawable, Sequence[hou.Prim]], pick_mod: hou.EnumValue[hou.pickModifier]) -> _ShapeSelection:
    """
    Combine two dictionaries based on a pick_mod.
    """
@typing.overload
def partitionSourceControlsByRig(source_controls: Iterable[Control], as_names: Literal[False] = ...) -> dict[str, list[Control]]: ...
@typing.overload
def partitionSourceControlsByRig(source_controls: Iterable[Control], as_names: Literal[True]) -> dict[str, list[str]]: ...
@typing.overload
def partitionSourceControlsByRig(source_controls: Iterable[Control], as_names: bool = ...) -> dict[str, list[Control]] | dict[str, list[str]]: ...
@typing.overload
def filterMappedSourceControls(source_controls: Iterable[Control], mapping_dict: Mapping[str, mapping.MappingCollection], as_names: Literal[False] = ..., unmapped: bool = ...) -> list[Control]: ...
@typing.overload
def filterMappedSourceControls(source_controls: Iterable[Control], mapping_dict: Mapping[str, mapping.MappingCollection], as_names: Literal[True], unmapped: bool = ...) -> list[str]: ...
@typing.overload
def filterMappedSourceControls(source_controls: Iterable[Control], mapping_dict: Mapping[str, mapping.MappingCollection], as_names: bool = ..., unmapped: bool = ...) -> list[Control] | list[str]: ...
@typing.overload
def findMappedDescendantControls(scene: Scene, source_ctrls: Iterable[Control], mapping_dict: Mapping[str, mapping.MappingCollection], as_names: Literal[False] = ...) -> list[Control]: ...
@typing.overload
def findMappedDescendantControls(scene: Scene, source_ctrls: Iterable[Control], mapping_dict: Mapping[str, mapping.MappingCollection], as_names: Literal[True]) -> list[str]: ...
@typing.overload
def findMappedDescendantControls(scene: Scene, source_ctrls: Iterable[Control], mapping_dict: Mapping[str, mapping.MappingCollection], as_names: bool = ...) -> list[Control] | list[str]: ...
def getControlRestTransforms(scene: Scene, rig_path: str) -> _apex.Dict:
    '''
    Evaluate the rig under the scene path "rig_path" with default
    parameters and return the output for all controls.
    '''
def filterMappingForControls(mapping_dict: Mapping[str, mapping.MappingCollection], source_ctrls: Iterable[Control]) -> dict[str, mapping.MappingCollection]:
    """
    Given a mapping dictionary(as set up in _readMapping under ragdolltool_2.py) and a list
    of source controls, it returns a sub-section of the mapping_dict that maps only those
    source_ctrls. It essentially discards any mapping entry that attempts to map a control that
    is not found under source_ctrls. 
    """
def similar(a: Sequence[_H], b: Sequence[_H]) -> float: ...
def combineListsUsingPickModifier(a: Iterable[_H], b: list[_H], pickmod: hou.EnumValue[hou.pickModifier]) -> list[_H]: ...

@dataclass
class RagdollConfig:
    character_name: str
    skel_path: str
    shapes_path: str
    skel_output_path: str
    mapping_name: str
    config_attrib: str

def parseRagdollConfig(ragdoll_config: apex.Dict, scene: Scene, rig_path: str) -> RagdollConfig:
    """
    Loads the ragdoll settings from the character config property (i.e. from
    the APEX Configure Character SOP).
    """
def findSkinPath(scene: Scene, skel_path: str) -> str | None:
    """
    Given a scene path to a rest skeleton of an APEX character, perform a heurustic
    to find the corresponding captured skin.
    """
def addControlsToActiveLayer(scene: Scene, source_ctrls: Iterable[Control]) -> None:
    """
    Add the passed in source_ctrls list to the active layer.
    """
def computeMatrixFromTransformAndP(transform: hou.Matrix3, pos: hou.Vector3) -> hou.Matrix4:
    """
    Given a joint's transform and position
    compute a matrix4 combining the two    
    """

class BaseSkelXform(BakeSourceXformBase):
    def __init__(self, components: str, xform: hou.Matrix4) -> None: ...
    def xform(self, frame: float, ctrl_mgr: ControlManager) -> hou.Matrix4: ...

class RagdollBakeCopyParms(BakeSourceParmsBase):
    def __init__(self, parms: apex.Dict) -> None: ...
    def parms(self, frame: float, scene: Scene, ctrl_mgr: ControlManager) -> _apex.Dict: ...

def createConstraintMappingCollection(channels: hou.Geometry, mappingcollection: mapping.MappingCollection) -> mapping.MappingCollection:
    """
    Creates a mapping collection based on match world transforms
    channel prims that evaluate to >.5 or if mwt * stiffness > threshold   
    This creates a list of joint names. It then iterates through the mapping
    looking for these names and adds an entry to the mapping collection for 
    every hit.
    """
def setMappingGadgetAttributes(gadget: mapping.MappingGadget) -> None:
    """
    Sets attributes on mapping gadget
    should these be exposed to user ?    
    """
def startRagdollPosingMode(ragdolltool: RagdollStateBase) -> None:
    """
    Launches Ragdoll Posing Mode    
    """
def startRagdollMode(ragdolltool: RagdollStateBase, includeGraph: bool) -> None:
    """
    Starts the Ragdoll tool
    includeGraph lets you reuse the graph. This is used when launching from
    Edit Mode as it reuses the graph but posing uses a different graph    
    """

class RagdollSpriteGadget:
    gadget: SpriteGadget
    visible: bool
    DEFAULT_SIZE: float
    FIXED_SIZE: float
    def __init__(self, scene_viewer: hou.SceneViewer, pos: hou.Vector3, forces: Sequence[str], callback: Callable[[str, int, hou.EnumValue[hou.pickModifier]], object]) -> None: ...
    def show(self, on: bool) -> None: ...
    def onDraw(self, handle: int) -> None: ...
    def onDrawInterrupt(self, handle: int) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool | None: ...
    def updateLook(self, bbox: hou.BoundingBox) -> None:
        """
        updates  the position of the gadget along 
        with the size and offset of the buttons   
        """
    def updatePosition(self, position: hou.Vector3) -> None: ...
    def updateSizeAndOffset(self, size: float) -> None: ...
    def updateOffset(self, size: float) -> None: ...
    def _update(self, fun: Callable[[str, _T], object], funp: _T) -> None: ...
