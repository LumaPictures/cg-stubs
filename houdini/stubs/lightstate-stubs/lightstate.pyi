import hou
from collections.abc import Mapping, MutableMapping, Sequence
from houtypes import NodeEventKwargs, ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateHandleToStateKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs, ViewerStateParmChangeKwargs, ViewerStateStateToHandleKwargs
from lightstate.lightdata import LightStateData as LightStateData
from typing import Literal, Unpack

from typing import TypeAlias
from houtypes import ViewerParmProperties
from typing import TypeAlias
_StateParms: TypeAlias = Mapping[str, ViewerParmProperties]
HKTOKEN_MODE_DEFAULT: str
HKTOKEN_MODE_SPECULAR: str
HKTOKEN_MODE_DIFFUSE: str
HKTOKEN_MODE_SHADOW: str
HKTOKEN_TOGGLE_LOOKAT: str
HKTOKEN_RESIZE: str
HKTOKEN_TOGGLE_BARNDOOR: str
HKTOKEN_TOGGLE_RESIZE_HANDLES: str
MODE_DEFAULT: str
MODE_SPECULAR: str
MODE_DIFFUSE: str
MODE_SHADOW: str
DISTANCE_KEY: str
BRIGHTNESS_KEY: str
TARGET_KEY: str
SPHERE_LIGHTTYPE: str
DISK_LIGHTTYPE: str
RECT_LIGHTTYPE: str
CYL_LIGHTTYPE: str
PORTAL_LIGHTTYPE: str
LIGHT_TYPES_NO_RESIZE: tuple[str, str, str, str]
LIGHT_TYPES_UNIFORM_RESIZE: tuple[str, str]
BBOX_LIGHT_TYPES: list[str]
BRECT_LIGHT_TYPES: list[str]
NO_SPOTLIGHT_LIGHT_TYPES: list[str]
DISTANCE_TEXT: str
INTENSITY_TEXT: str
EXPOSURE_TEXT: str
RADIUS_TEXT: str
WIDTH_TEXT: str
HEIGHT_TEXT: str
LENGTH_TEXT: str

class LightStateHandle:
    """
    Encapsulation of state handles to reduce clutter in the State object.
    """
    barndoor_enabled: bool
    lightxformparmset: set[str]
    lightShapingParmSet: set[str]
    def __init__(self, data: LightStateData, scene_viewer: hou.SceneViewer) -> None: ...
    @staticmethod
    def bindHandles(template: hou.ViewerStateTemplate) -> hou.ViewerStateTemplate: ...
    @property
    def bbox(self) -> hou.Handle: ...
    @property
    def brect(self) -> hou.Handle: ...
    def update(self) -> None: ...
    def setLightXform(self, xform: hou.Matrix4) -> None: ...
    def show(self, show: bool) -> None: ...
    def showBarndoor(self, show: bool) -> None: ...
    def showLight(self, show: bool) -> None: ...
    def toggleBarndoor(self) -> None: ...
    def handleChange(self, kwargs: ViewerStateHandleToStateKwargs) -> None: ...
    def parmChange(self, kwargs: ViewerStateStateToHandleKwargs) -> None: ...
    def updateLightValues(self, kwargs: ViewerStateHandleToStateKwargs) -> None: ...
    def updateLightHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None: ...
    def updateBBoxValues(self, handle_parms: Mapping[str, float]) -> None: ...
    def updateBBoxHandle(self, handle_parms: MutableMapping[str, float]) -> None: ...
    def updateBRectValues(self, handle_parms: Mapping[str, float]) -> None: ...
    def updateBRectHandle(self, handle_parms: MutableMapping[str, float]) -> None: ...
    def updateBarndoorValues(self, handle_parms: Mapping[str, float]) -> None: ...
    def updateBarndoorHandle(self, handle_parms: MutableMapping[str, float]) -> None: ...

def computeLightPos(cameraPos: hou.Vector3, distanceToMaintain: float, hitPos: hou.Vector3, normal: hou.Vector3) -> hou.Vector3:
    """
    Computes the reflected light position
     cameraPos - world space camera position.
     oldLightPos - world space light position, the distance from the
    old position to the clicked point on the surface is maintained as
    the distance from the clicked point to the new light position.
     hitPos - the surface point that we clicked on.
     normal - the surface normal that
    """

class Dragger:
    """
    Draggable widget data object, this is used to power the brightness/distance
    draggers.
    TODO: PolyBevel3.0 has a much nicer dragging handle but it intercepts mouse
    events directly so I could not find a way to have separate dragging handles
    for distance/brightness.
    """
    ticks: Sequence[float]
    tick: int
    mult: float
    def __init__(self, ticks: Sequence[float]) -> None: ...
    def increaseTick(self) -> None: ...
    def decreaseTick(self) -> None: ...
    def value(self) -> float: ...

class LightState:
    state_name: str
    scene_viewer: hou.SceneViewer
    mode: str
    drag_text: str
    mouse_down_position: hou.Vector3 | None
    last_mouse_position: hou.Vector3 | None
    intensity_dragger: Dragger | None
    distance_dragger: Dragger | None
    resize_dragger: Dragger | None
    initialPos: hou.Vector3 | None
    place_target: bool
    distance_drag: bool
    brightness_drag: bool
    resize_drag: bool | int
    light_size_modifier: int
    hk_mode_default: str
    hk_mode_specular: str
    hk_mode_diffuse: str
    hk_mode_shadow: str
    hk_toggle_lookat: str
    hk_resize: str
    hk_toggle_barndoor: str
    hk_toggle_resize_handles: str
    data: LightStateData
    node: hou.LopNode
    text_cursor: hou.TextDrawable
    state_parms: _StateParms
    _light_handle: LightStateHandle
    @staticmethod
    def registerHotkeys(hotkey_definitions: hou.PluginHotkeyDefinitions, state_name: str, state_cat: hou.OpNodeTypeCategory) -> None: ...
    @staticmethod
    def bindMenu(template: hou.ViewerStateTemplate) -> None: ...
    @staticmethod
    def bindParameters(template: hou.ViewerStateTemplate) -> None: ...
    def __init__(self, state_name: str, scene_viewer: hou.SceneViewer) -> None:
        """
        Initialize member variables
        """
    def onEnter(self, kwargs: ViewerStateEnterKwargs, data: LightStateData) -> None:
        """
        Executed when state is entered.
        """
    def onResume(self, kwargs: ViewerStateKwargs) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """
        Process mouse events
        """
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """
            Process keyboard transit events
        """
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None:
        """
        React to state parameter changes.
        """
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> None: ...
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> None: ...
    def onHandleToState(self, kwargs: ViewerStateHandleToStateKwargs) -> None: ...
    def onStateToHandle(self, kwargs: ViewerStateStateToHandleKwargs) -> None: ...
    def bindHandles(self, template: hou.ViewerStateTemplate) -> None: ...
    def handleMousePick(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def handleMouseDrag(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def handleModeChange(self, kwargs: ViewerStateKwargs, newMode: str) -> None: ...
    def _updateHUD(self) -> None: ...
    def renderLine(self, handle: int) -> None: ...
    def renderPivotAndTarget(self, handle: int) -> None: ...
    def updateNodeParmCB(self, **kwargs: Unpack[NodeEventKwargs]) -> None:
        """
            Callback for when node parm/parm_tuple gets modified.
        """
    def adapt_brightness(self, curIntensity: float, curExposure: float, oldDist: float, newDist: float) -> None: ...
    def getFocusPoint(self) -> hou.Vector3: ...
    def placeLight(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def placeLookAt(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def setLightPos(self, kwargs: ViewerStateEventKwargs, viewport: hou.GeometryViewport, mousePosX: float, mousePosY: float) -> tuple[hou.Vector3, Literal[True], hou.Vector3] | tuple[None, Literal[False], None]:
        """
        Given the kwargs for some node, we compute the light position when clicking
        on a piece of geometry.
        viewport - Geometry viewport that we want to check for intersection.
        mousePosX/Y - Screen space mouse position that we clicked.
        diffuse - True if we want to set the light to have a diffuse highlight
        at the surface we clicked on. False if we want specular.
        """
    def setLookAtPosition(self, worldPos: hou.Vector3) -> None: ...
    def updateShadowPivotAndTarget(self) -> None: ...
    def updateRailGeometry(self) -> None:
        """
            Instead of messing around with xforms we just create a new open
            polygon with 2 points (yea we just make a line).
        """
    def updateGuideGeo(self) -> None: ...
