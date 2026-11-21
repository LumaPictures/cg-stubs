import hou
from enum import Enum
from houtypes import ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateHandleToStateKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs, ViewerStateNodeChangeKwargs, ViewerStateStateToHandleKwargs
from typing import TypedDict

class _HUDRow(TypedDict, total=False):
    id: str
    type: str
    visible: bool
    label: str
    value: str | float | int
    key: str
    wide: bool
    count: int
    rows: list['_HUDRow']
    current: int | str | None

class _HUDTemplate(TypedDict, total=False):
    title: str
    icon: str
    desc: str
    rows: list['_HUDRow']

PHYSICAL_LENS_NO_DISTORTION: dict[str, str | int]
RENDER_STYLE_DISABLED: int
RENDER_STYLE_GLOW: int
RENDER_STYLE_GLOW_MINUS_MATTE: int
ALLOW_PICK_FLOOR: bool

def queryLopWorldPos(scene_node: hou.OpNode, scene_viewer: hou.SceneViewer, ui_event: hou.ViewerEvent) -> tuple[hou.Vector3, bool]: ...
def querySopWorldPos(scene_node: hou.OpNode, scene_viewer: hou.SceneViewer, ui_event: hou.ViewerEvent) -> tuple[hou.Vector3, bool]: ...
def queryCopWorldPos(scene_node: hou.OpNode, scene_viewer: hou.SceneViewer, ui_event: hou.ViewerEvent) -> tuple[hou.Vector3, bool]: ...
def queryWorldPos(node: hou.OpNode, scene_viewer: hou.SceneViewer, state_cat: hou.OpNodeTypeCategory, ui_event: hou.ViewerEvent) -> tuple[hou.Vector3, bool]: ...

class Mode(Enum):
    TILT = (0,)
    FSTOP = (1,)
    EXPOSURE = (2,)
    FOCAL_LENGTH = 3

class BaseState:
    state_name: str
    state_cat: hou.OpNodeTypeCategory
    scene_viewer: hou.SceneViewer
    xform_parm_set: set[str]
    parm_tuple_map: dict[str, str]
    handle_parm_map: dict[str, str]
    available_modes: set[str]
    HK_CTXT: str
    HK_LOOKAT_HOTKEY: str
    HK_FOCUS_HOTKEY: str
    HK_FSTOP_HOTKEY: str
    HK_EXPOSURE_HOTKEY: str
    HK_FOCAL_LENGTH_HOTKEY: str
    HK_TILT_HOTKEY: str
    HK_CLEAR_HOTKEY: str
    HUD_TEMPLATE: _HUDTemplate
    node: hou.OpNode
    def __init__(self, state_name: str, scene_viewer: hou.SceneViewer, state_cat: hou.OpNodeTypeCategory | None = None, state_icon: str = 'LOP_camera', state_label: str = 'Camera') -> None: ...
    def setupMappings(self) -> None: ...
    def onGenerate(self, kwargs: ViewerStateKwargs) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """
        Process mouse events
        """
    def onHandleToState(self, kwargs: ViewerStateHandleToStateKwargs) -> None: ...
    def onStateToHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None: ...
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> None:
        """
            Callback implementing the actions of a bound menu. Called 
            when a menu item has been selected. 
        """
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> None:
        """ Implement this callback to update the menu content before 
        it is drawn. 
        """
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def handleMousePick(self, kwargs: ViewerStateEventKwargs) -> None:
        """
            Handles mouse picks, shift click places focus distance/points.
        """
    def handleMouseDrag(self, kwargs: ViewerStateEventKwargs) -> None:
        """
            Handles mouse drags, LMB drags focus points.
        """
    def handleMouseLocated(self, kwargs: ViewerStateEventKwargs) -> None:
        """
            Handles mouse movements, used for hover effects
        """
    def onNodeChangeEvent(self, kwargs: ViewerStateNodeChangeKwargs) -> None:
        """
            Callback for when a node parameter changes.
        """
    def getLensShader(self) -> None: ...
    def placeLookAt(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def setLookAtPosition(self, worldPos: hou.Vector3) -> None: ...
    def primstr(self) -> str | None: ...
    def updateFocusGeo(self) -> None: ...
    def renderFocusPlane(self, handle: hou.Handle) -> None: ...
    def renderPlanePoints(self, handle: hou.Handle) -> None: ...
    def updateTilt(self) -> None: ...
    def placeFocus(self, kwargs: ViewerStateEventKwargs) -> None:
        """
            On a click event, this function computes the focus distance such that
            the point clicked is in focus.
        """
    def updateHUD(self) -> None: ...
    def getCameraXform(self, pre: bool = False, geo: hou.Geometry | None = None) -> hou.Matrix4:
        """
            Called to get light xform, if pre is True then return pre xform.
        """
    def getClipWidthHeight(self) -> tuple[float, float]:
        """
            Get width and height of frustum at focus distance.
        """
    def setMaxDistToCentroid(self) -> None: ...
    def getPlaneScale(self) -> tuple[float, float]: ...
    def buildLookAt(self, to: hou.Vector3, fro: hou.Vector3, up: hou.Vector3) -> hou.Matrix4: ...
    def setSelectedPlanePoint(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def verifyPointCentroid(self) -> None: ...

def setupViewerStateTemplate(template: hou.ViewerStateTemplate, state_typename: str, state_cat: hou.OpNodeTypeCategory) -> None: ...
