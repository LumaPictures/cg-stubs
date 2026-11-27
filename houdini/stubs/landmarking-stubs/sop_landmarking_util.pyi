import hou
import logging
import resourceutils
import viewerstate.utils as su
from collections import OrderedDict as OrderedDict
from enum import Enum as Enum
from houtypes import ViewerStateDrawKwargs, ViewerStateEventKwargs
from typing import Protocol, Self

from typing import TypeAlias
from typing import TypeVar
from collections.abc import Mapping
from houtypes import ViewerParmProperties
from typing import Literal
from typing import TypeAlias
from typing import TypeVar
_StateParms: TypeAlias = Mapping[str, ViewerParmProperties]
_Intersection: TypeAlias = tuple[Literal[True], int, int] | tuple[Literal[False], None, None]
_LandmarkLists: TypeAlias = tuple[list['Landmark'], list['Landmark | None'], list['Landmark'], list['Landmark']]
_StateT = TypeVar('_StateT', bound=_LandmarkState)
class _LandmarkState(Protocol):
    scene_viewer: hou.SceneViewer
    state_name: str
    state_type: int
    multiparam_idx: int
    uimode: UIMODE
    groups: dict[int, LandmarkGroup]
    logger: logging.Logger
    translate_handle: hou.Handle | None
    source_guide: hou.SimpleDrawable | None
    target_guide: hou.SimpleDrawable | None
    source_gi: su.GeometryIntersector | None
    target_gi: su.GeometryIntersector | None
    single_drawable: hou.GeometryDrawable

class _LandmarkGeoState(_LandmarkState, Protocol):
    source_que: hou.Geometry | None
    target_que: hou.Geometry | None
    def sync(self, node: hou.SopNode, /) -> None: ...
    def addLandmarkGroup(self, node: hou.SopNode, /) -> None: ...

class _LandmarkGroupState(_LandmarkState, Protocol):
    def addLandmarkGroup(self, node: hou.SopNode, group_id: int, /) -> None: ...

class _LandmarkDrawState(_LandmarkState, Protocol):
    xray: hou.GeometryDrawable

class _LandmarkMouseState(_LandmarkState, Protocol):
    MOUSE_ACTIVE_TRIGGERED: bool
    def onMouseClick(self, kwargs: ViewerStateEventKwargs, /) -> None: ...
    def sync(self, node: hou.SopNode, /) -> None: ...

tt_pixel_eps: int
tt_src_cd: tuple[float, float, float]
tt_tgt_cd: tuple[float, float, float]
tt_blue: hou.Vector4
tt_cyan: hou.Vector4
tt_green: hou.Vector4
tt_yellow: hou.Vector4
tt_orange: hou.Vector4
tt_purple: hou.Vector4
tt_xray: hou.Vector4

class STYLE_GUIDE:
    line_params: hou._DrawableParams
    xray_params: hou._DrawableParams
    src_point_params: hou._DrawableParams
    tgt_point_params: hou._DrawableParams
    selection_circle_params: hou._DrawableParams
    selection_point_params: hou._DrawableParams
    match_point_params: hou._DrawableParams
    match_line_params: hou._DrawableParams
    highlight_params: hou._DrawableParams

class PointParser:
    """
    Parse point coordinates string into hou.Vector3 array
    """
    string: str
    def __init__(self, string: str) -> None: ...
    def parse(self) -> list[hou.Vector3] | None:
        '''
        Parses the given string and returns and array of hou.Vecotr3
        Assumes that the string has the following format
        "x1,y1,z1 x2,y2,z2 x3,y3,z3..."
        '''

class IndexParser:
    """
    Parse point indices string into an array
    """
    geo: hou.Geometry
    string: str
    def __init__(self, geo: hou.Geometry, string: str) -> None: ...
    def parse(self) -> list[hou.Point | None] | None:
        '''
        Parses the given string and returns and array of indices
        Assumes that the string has the following format
        "i1 i2 i3..."
        '''

class EditMode(Enum):
    Edit = 0
    Match = 1
    Unmatch = 2

class LabelMode(Enum):
    Off = 0
    On = 1
    Index = 2

class ViewMode(Enum):
    All = 0
    Selectable = 1

class _STATETYPE:
    MULTIPARM: int
    NODE: int
    NODE_NEW_GROUP: int
    NODE_EDIT_GROUP: int
    INVALID_INPUTS: int

STATETYPE: _STATETYPE

class _STATEPARM:
    SOLVE: str
    RESET: str
    ACCEPT: str
    CANCEL: str
    INPUT: str
    LND_NAME: str
    GRP_NAME: str
    NEW_GRP: str
    EDIT_GRP: str
    CENTER_CAMERA: str
    XRAY_SRC: str
    GEO_COLOR: str
    SEP1: str
    SNAP_MODE: str
    EDIT_MODE: str
    VIEW_MODE: str

STATEPARM: _STATEPARM

class _PARM_INFO:
    ENABLE_GRP: str
    NUM_GRPS: str
    COLOR: str
    NAME: str
    SRC_GRP: str
    USE_SRC_POS: str
    SRC_POS: str
    SRC_UNPAIRED: str
    TRGT_GRP: str
    USE_TRGT_POS: str
    TRGT_POS: str
    TRGT_UNPAIRED: str
    PREFIX_LABEL: str
    ATTRIB_LABEL: str
    SRC_STASH: str
    TGT_STASH: str
    STASH_SRC: str
    STASH_TGT: str

PARM_INFO: _PARM_INFO

class _QUE_ATTR:
    EVENT: str
    INPUT: str
    OUTPUT: str
    LABEL: str
    ATTR: str
    INIT: str

QUE_ATTR: type[_QUE_ATTR]

class _QUE_EVENTS:
    CREATE: str
    REMOVE: str
    RELOCATE: str
    RELABEL: str
    UNINIT: str

QUE_EVENTS: type[_QUE_EVENTS]

class UIMODE:
    SHOW_TARGET: bool | int
    IS_DRAGGING: bool
    MOUSE_ACTIVE_TRIGGERED: bool
    MOUSE_ACTIVE_CALLED: bool
    DRAG_IDS: tuple[int, int] | None
    HOVER_OVER_IDS: tuple[int, int] | None
    LAST_MOUSE_POS: hou.Vector3 | None
    HIGHLIGHTER_POS: hou.Vector3 | None
    HIGHLIGHTER_SRC_ID: int | None
    HIGHLIGHTER_TGT_ID: int | None
    HIGHLIGHTER_SRC_IDS: list[int]
    HIGHLIGHTER_TGT_IDS: list[int]
    HIGHLIGHTER_PAIRS: dict[int, int]
    LAST_SRC_BALL_POS: hou.Vector3 | None
    LAST_TARGET_BALL_POS: hou.Vector3 | None
    LAST_SNAP_POS: hou.Vector3 | None
    GUIDE_TRANS: hou.Matrix4 | None
    GUIDE_CENTER: hou.Vector3 | None
    LND_NAME: str
    SHOW_XRAY_SRC: bool
    SHOW_GEO_COLOR: bool
    EDIT_MODE: str
    VIEW_MODE: str

def globalCreateLandmarksLine(scene_viewer: hou.SceneViewer, src_landmark: hou.Vector3, target_landmark: hou.Vector3) -> tuple[hou.Geometry, hou.GeometryDrawable]: ...

class Landmark:
    position: hou.Vector3
    point_number: int
    visible: bool | int
    list_index: int | None
    active: bool
    def __init__(self, position: hou.Vector3, point_number: int) -> None: ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    @classmethod
    def fromPoint(cls, point: hou.Point) -> Self: ...
    @classmethod
    def fromPointTransform(cls, point: hou.Point, transform: hou.Matrix4, number: int | None = None) -> Self: ...
    @classmethod
    def fromPos(cls, pos: hou.Vector3) -> Self: ...
    @classmethod
    def fromPosNum(cls, pos: hou.Vector3, num: int) -> Self: ...
    @classmethod
    def fromPosTransform(cls, pos: hou.Vector3, transform: hou.Matrix4, number: int | None = None) -> Self: ...
    def translate(self, t: hou.Vector3) -> None: ...

class LandmarkPair:
    pair_id: int
    src_landmark: Landmark
    target_landmark: Landmark
    is_new: bool
    line_geo: resourceutils.Line
    text_drawable: hou.TextDrawable
    active: bool
    def __init__(self, scene_viewer: hou.SceneViewer, pair_id: int, src_landmark: Landmark, target_landmark: Landmark, is_new: bool) -> None: ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def isActive(self) -> bool: ...
    @classmethod
    def fromSrcLandmark(cls, scene_viewer: hou.SceneViewer, pair_id: int, src_landmark: Landmark) -> Self: ...
    def updateLineGeometry(self) -> None: ...
    def deleteTargetLandmark(self) -> None: ...
    def setTargetLandmarkPoint(self, point_number: int, pos: hou.Vector3) -> None: ...
    def setTargetLandmarkPos(self, pos: hou.Vector3) -> None: ...
    def translate(self, t: hou.Vector3) -> None: ...
    def show(self, show: bool | int) -> None: ...

class LandmarkGroup:
    """
    Landmark group that contains landmark pairs.
    Corresponds to the landmark multiparm instance
    """
    group_id: int
    name: str
    color: hou.Vector4
    enabled: bool | int
    landmark_pairs: list[LandmarkPair]
    landmark_sources: list[Landmark]
    landmark_targets: list[Landmark]
    use_target_pos: bool | int
    use_src_pos: bool | int
    def __init__(self, group_id: int, name: str, color: hou.Vector4, enabled: bool | int, use_src_pos: bool | int, use_target_pos: bool | int) -> None: ...
    def containsSrcLandmark(self, point_number: int) -> bool:
        """
        Does the group contain a pair whose source landmark has the point number
        """
    def removeLandmarkPair(self, pair_id: int) -> None:
        """
        Remove landmark pair with the given id.
        """
    def addPair(self, scene_viewer: hou.SceneViewer, node: hou.SopNode | None, src_landmark: Landmark, target_landmark: Landmark | None, id: int = -1) -> int:
        """Add a new landmark pair to the group.

        Parameters:
            scene_viewer (hou.SceneViewer):
            node (hou.Node):
            src_landmark (Landmark): source landmark
            target_landmark (Landmark): corresponding target landmark for the
                                        src_landmark. Is None if target landmark
                                        has not been set by the user yet.
        """
    def addSource(self, src_landmark: Landmark) -> None:
        """Add a single, unpaired source landmark to the group.

        Parameters:
            src_landmark (Landmark): source landmark
        """
    def addTarget(self, tgt_landmark: Landmark) -> None:
        """Add a single, unpaired target landmark to the group.

        Parameters:
            tgt_landmark (Landmark): target landmark
        """
    def findIntersection(self, scene_viewer: hou.SceneViewer, ray_origin: hou.Vector3, ray_direction: hou.Vector3, src: bool = True, depthSort: bool = True, mode: str = ...) -> _Intersection: ...
    def getPairString(self, transform: hou.Matrix4) -> tuple[str, str]:
        """ Create tuple of strings that would be used to set source AND target
            point group node parameters
        """
    def getSourceString(self, transform: hou.Matrix4) -> str:
        """ Create a strings that would be used to set unmatched source
            node parameter
        """
    def getTargetString(self, transform: hou.Matrix4) -> str:
        """ Create tuple of strings that would be used to set unmatched target
            node parameter
        """
    def translate(self, t: hou.Vector3) -> None:
        """ Translate the whole landmark group by hou.Vector3 """
    def isEmpty(self) -> bool: ...
    def numPairs(self) -> int: ...
    def numSources(self) -> int: ...
    def numTargets(self) -> int: ...
    def deleteSource(self, id: int) -> None: ...
    def deleteTarget(self, id: int) -> None: ...
    def findNewPairIndex(self) -> int: ...
    def findNewSourceIndex(self) -> int: ...
    def findNewTargetIndex(self) -> int: ...
    def findSource(self, pid: int) -> int | None: ...
    def findTarget(self, pid: int) -> int | None: ...
    def getPair(self, pid: int) -> LandmarkPair: ...
    def getSource(self, pid: int) -> Landmark: ...
    def getTarget(self, pid: int) -> Landmark: ...
    def setSource(self, pid: int, pos: hou.Vector3) -> None: ...
    def setTarget(self, pid: int, pos: hou.Vector3) -> None: ...
    def nextPairIdWithoutTarget(self) -> int | None:
        '''"
        Find the next pair that does not have its target point number or
        position set.
        Return None if no such pair exists
        '''
    def syncWithNode(self, node: hou.SopNode, guide_trans: hou.Matrix4, undolabel: str = 'Landmarks', multi_mode: bool = True) -> None: ...

def accept(state: _LandmarkState, state_parms: _StateParms, node: hou.SopNode) -> None: ...
def areGeosValid(state: _LandmarkState, node: hou.SopNode) -> bool: ...
def areInputsValid(state: _LandmarkState, state_parms: _StateParms, node: hou.SopNode) -> bool:
    """
    Check that source and target meshes are valid.
    """
def cancel(state: _LandmarkGroupState, state_parms: _StateParms, node: hou.SopNode) -> None: ...
def createEvent(gq: hou.Geometry, pos: hou.Vector3, node: hou.SopNode, init: int = 1) -> None: ...
def deleteColorData(state: _LandmarkState, geo: hou.Geometry) -> bool:
    """
    Delete any type of shading information users might not want to see.
    """
def doesIntersectLandmarks(state: _LandmarkState, ray_origin: hou.Vector3, ray_direction: hou.Vector3, isSrc: bool, edit_mode: str = ...) -> tuple[int, int]: ...
def drawGuides(state: _LandmarkDrawState, kwargs: ViewerStateDrawKwargs, guide: STYLE_GUIDE) -> None: ...
def getGroup(state: _LandmarkState, gid: int) -> LandmarkGroup: ...
def getPair(state: _LandmarkState, gid: int, pid: int) -> LandmarkPair: ...
def hasColorData(state: _LandmarkState, geo: hou.Geometry) -> bool:
    """
    Look for any type of custom shading information users might want to see
    instead of a simple shaded drawable.
    """
def initGeoQue(node: hou.SopNode, search_parm: str | None = None) -> hou.Geometry: ...
def localToGuideSpace(state: _LandmarkState, node: hou.SopNode, pos: hou.Vector3) -> hou.Vector3: ...
def localToGuideSpaceTransform(state: _LandmarkState, node: hou.SopNode) -> hou.Matrix4: ...
def onMouseLocated(state: _LandmarkState, node: hou.SopNode, ui_event: hou.ViewerEvent) -> None: ...
def onMouseStartDrag(state: _LandmarkMouseState, node: hou.SopNode, ui_event: hou.ViewerEvent) -> None: ...
def onMouseDrag(state: _LandmarkMouseState, ui_event: hou.ViewerEvent) -> None: ...
def onMouseDragEnd(state: _LandmarkMouseState, kwargs: ViewerStateEventKwargs, gq: hou.Geometry | None = None) -> None: ...
def initLandmarkGeoData(state: _LandmarkGeoState, node: hou.SopNode, geo1: hou.Geometry, geo2: hou.Geometry | None = None) -> _LandmarkLists: ...
def parseLandmarkData(state: _LandmarkState, node: hou.SopNode) -> _LandmarkLists: ...
def isEmpty(node: hou.SopNode) -> bool: ...
def relabelEvent(gq: hou.Geometry, input_id: int = -1, output_id: int = -1, label: str = '') -> None: ...
def relocateEvent(gq: hou.Geometry, pos: hou.Vector3, id: int) -> None: ...
def uninitializeEvent(gq: hou.Geometry, pos: hou.Vector3, id: int) -> None: ...
def removeEvent(gq: hou.Geometry, input_id: int = -1, output_id: int = -1) -> None: ...
def reset(state: _LandmarkGeoState, node: hou.SopNode) -> None: ...
def singleSolve(node: hou.SopNode) -> None: ...
def toggleSourceTarget(state: _LandmarkState, state_parms: _StateParms, node: hou.SopNode) -> bool: ...
def updateDrawablesVisibility(state: _StateT, node: hou.SopNode) -> _StateT: ...
def undoGuideTransform(state: _LandmarkState, point: hou.Vector3) -> hou.Vector3: ...
def updateIntersectionCache(state: _LandmarkState, node: hou.SopNode) -> None:
    """
    Creates/updates the source and target intersection cache for
    detecting screen cursor intersections.
    """
def updateLandmarkingGeos(state: _LandmarkDrawState, node: hou.SopNode, offset: bool = True) -> None:
    """
    Create the source and target reference drawable along with any
    available shading information if requested.
    """
