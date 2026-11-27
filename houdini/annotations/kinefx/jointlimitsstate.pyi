from collections.abc import Callable, Mapping
from typing import Literal, Never, NotRequired, Protocol, TypeAlias, TypedDict, overload, type_check_only

import apex.rotationlimitsgadget as rlg
import apex.translationlimitsgadget as tlg
import hou
import statehud.utils as shu
import statehud.window as shud
from apex.rotationlimitsgadget import RotationLimitsHandle
from apex.translationlimitsgadget import TranslationLimitsHandle
from houtypes import (
    ViewerStateCommandKwargs,
    ViewerStateDrawKwargs,
    ViewerStateEnterKwargs,
    ViewerStateEventKwargs,
    ViewerStateKwargs,
    ViewerStateMenuActionKwargs,
    ViewerStateMenuPreOpenKwargs,
    ViewerStateNodeChangeKwargs,
    ViewerStateParmChangeKwargs,
    ViewerStatePlaybackChangeKwargs,
    ViewerStateSelectionKwargs,
    ViewerStateVolatileClientKwargs,
)
import kinefx.stateutils as ksu
from kinefx.stateutils import StashParmsCollection, ViewerStateDisplayOptions
from kinefx.ui.rigvisualisers import KinefxRigVisualiser
from statehud.parmutils import _HUDParmValue

# A joint's limits, as initializeLimits() makes them (rotations in degrees); addEntry() adds the
# rest of a stash parms entry.
_JointLimits = TypedDict(
    "_JointLimits",
    {
        "rOrd#": int,
        "rxrange#": tuple[float, float],
        "ryrange#": tuple[float, float],
        "rzrange#": tuple[float, float],
        "txrange#": tuple[float, float],
        "tyrange#": tuple[float, float],
        "tzrange#": tuple[float, float],
        "group#": NotRequired[str],
        "enablerlimits#": NotRequired[int],
        "enabletlimits#": NotRequired[int],
    },
)

# A stash parms entry (one per joint with limits), as the stash parms collection reads it back:
# the ranges as Vector2s.
_JointLimitsEntry = TypedDict(
    "_JointLimitsEntry",
    {
        "group#": str,
        "rOrd#": int,
        "enablerlimits#": int,
        "rxrange#": hou.Vector2,
        "ryrange#": hou.Vector2,
        "rzrange#": hou.Vector2,
        "enabletlimits#": int,
        "txrange#": hou.Vector2,
        "tyrange#": hou.Vector2,
        "tzrange#": hou.Vector2,
    },
)

# A copied stash parms entry: one without its group.
_CopiedJointLimits = TypedDict(
    "_CopiedJointLimits",
    {
        "rOrd#": int,
        "enablerlimits#": int,
        "rxrange#": hou.Vector2,
        "ryrange#": hou.Vector2,
        "rzrange#": hou.Vector2,
        "enabletlimits#": int,
        "txrange#": hou.Vector2,
        "tyrange#": hou.Vector2,
        "tzrange#": hou.Vector2,
    },
)

# What the HUD widgets need of their state.
class _HUDWidgetState(Protocol):
    @property
    def scene_viewer(self) -> hou.SceneViewer: ...
    def onHUDWindowValuesChange(self, slider_name: str, v: _HUDParmValue) -> None: ...

_RangeSliderName: TypeAlias = Literal[
    "rxrangemin", "rxrangemax", "ryrangemin", "ryrangemax", "rzrangemin", "rzrangemax",
    "txrangemin", "txrangemax", "tyrangemin", "tyrangemax", "tzrangemin", "tzrangemax",
]

mirror_axis_menu: list[tuple[str, str]]
mirror_planenormal: dict[str, hou.Vector3]
rOrd_str: list[ksu._RotateOrder]
rotation_order_menu_items: tuple[tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str]]

class ConfigureJointLimitValuesHUDWidget:
    rotation_limit_hud_handles: tuple[str, ...]
    translation_limit_hud_handles: tuple[str, ...]
    combo_boxes: tuple[str, ...]
    buttons: tuple[str, ...]
    state: _HUDWidgetState
    hud_handle: shud.WidgetBundleWindow
    visible_parms: tuple[str, ...]
    def __init__(self, state: _HUDWidgetState, pin_manager: shu.PinManager | None = ...) -> None: ...
    @property
    def widgethotkey(self) -> str | None: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str | None) -> None: ...
    def onHUDWindowValueChangeCallback(self, slider_name: str) -> Callable[[_HUDParmValue], None]: ...
    def onHUDWindowButtonPressCallback(self, slider_name: str) -> Callable[[], None]: ...
    def onHUDWindowValueChange(self, slider_name: str, v: _HUDParmValue) -> None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def isVisible(self) -> bool: ...
    # The rotation order combo box's index (None without one), or a slider's value.
    @overload
    def getSliderValue(self, name: Literal["rOrd"]) -> int | None: ...
    @overload
    def getSliderValue(self, name: _RangeSliderName) -> float: ...
    @overload
    def getSliderValue(self, name: str) -> int | float | None: ...
    @overload
    def updateSlider(self, name: Literal["rOrd"], val: int) -> None: ...
    @overload
    def updateSlider(self, name: str, val: float) -> None: ...
    def updateSliderVisibility(self, rotation_limits: bool | int = ..., translation_limits: bool | int = ...) -> None: ...

class ConfigureJointLimitEnablerHUDWidget:
    state: _HUDWidgetState
    hud_handle: shud.WidgetBundleWindow
    def __init__(self, state: _HUDWidgetState, pin_manager: shu.PinManager | None = ...) -> None: ...
    @property
    def widgethotkey(self) -> str | None: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str | None) -> None: ...
    def onHUDWindowValueChangeCallback(self, slider_name: str) -> Callable[[_HUDParmValue], None]: ...
    def onHUDWindowValueChange(self, slider_name: str, v: _HUDParmValue) -> None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def isVisible(self) -> bool: ...
    def getSliderValue(self, name: str) -> bool: ...
    def updateSlider(self, name: str, val: bool) -> None: ...

class State:
    HK_CTXT: str
    HK_VOL: str
    HK_DEL: str
    HK_SHOW_VALUES_HUD_HANDLE: str
    HK_SHOW_LIMITENABLER_HUD_HANDLE: str
    HK_COPY: str
    HK_PASTE: str
    HK_PASTE_MIRRORED: str
    INPUT_NODE_EVENTS: tuple[hou.EnumValue[hou.nodeEventType], ...]
    state_name: str
    scene_viewer: hou.SceneViewer
    node: hou.SopNode | None
    error_msg: str | None
    enter_kwargs: ViewerStateEnterKwargs | dict[str, Never]
    geo: hou.Geometry | None
    # Never read: the state uses rest_geo, which onEnter() sets.
    geo_rest: hou.Geometry
    rest_geo: hou.Geometry | None
    display_options: ViewerStateDisplayOptions
    stash_parms: StashParmsCollection[_JointLimitsEntry] | None
    symmetry_lookup: list[int]
    symmetry_success: bool
    found_symmetrical_pts: bool
    symmetrical_pts: list[hou.Point | None]
    mirror_axis: str
    rOrd: int
    runcallback: bool
    rotation_limits_gadget: RotationLimitsHandle
    translation_limits_gadget: TranslationLimitsHandle
    main_drawable: KinefxRigVisualiser
    ghosted_drawable: KinefxRigVisualiser
    selection: hou.Selection
    pre_selection: hou.Selection
    cur_selection: hou.Selection
    enablerlimits: int
    enabletlimits: int
    showallhandles: int
    rlimitdisplay: int
    tlimitdisplay: int
    pick_mod: ksu._PickModifier
    # The copied entry, without its group ({} until something is copied).
    copied_values: _CopiedJointLimits | dict[str, Never]
    hud_pin_mgr: shu.PinManager
    hud_values_handle: ConfigureJointLimitValuesHUDWidget
    hud_enabler_handle: ConfigureJointLimitEnablerHUDWidget
    # Houdini sets both on a python state that binds gadgets (the limits handles use them).
    @type_check_only
    @property
    def state_gadgets(self) -> Mapping[str, hou.GadgetDrawable]: ...
    @type_check_only
    @property
    def state_context(self) -> hou.ViewerStateContext: ...
    def __init__(self, state_name: str, scene_viewer: hou.SceneViewer) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onHUDWindowValuesChange(self, slider_name: str, v: _HUDParmValue) -> None: ...
    def onRotationLimitsHandleStartUpdate(self, kwargs: rlg._HandleUpdateKwargs) -> None: ...
    def onRotationLimitsHandleUpdate(self, kwargs: rlg._HandleUpdateKwargs) -> None: ...
    def onRotationLimitsHandleEndUpdate(self, kwargs: rlg._HandleUpdateKwargs) -> None: ...
    def onTranslationLimitsHandleStartUpdate(self, kwargs: tlg._HandleUpdateKwargs) -> None: ...
    def onTranslationLimitsHandleUpdate(self, kwargs: tlg._HandleUpdateKwargs) -> None: ...
    def onTranslationLimitsHandleEndUpdate(self, kwargs: tlg._HandleUpdateKwargs) -> None: ...
    def onSelection(self, kwargs: ViewerStateSelectionKwargs) -> bool | None: ...
    def onStartSelection(self, kwargs: ViewerStateSelectionKwargs) -> None: ...
    def onLocatedSelection(self, kwargs: ViewerStateSelectionKwargs) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool | None: ...
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool | None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool | None: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool | None: ...
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool | None: ...
    def initializeLimits(self, pt_name: str) -> _JointLimits: ...
    def addEntry(self, sel: hou.Selection) -> None: ...
    def getSymmetricPoints(self, sel: hou.Selection) -> None: ...
    # The state's own calls also pass inithandles: bool.
    def mySelectionHandler(self, kwargs: ksu._SelectionArgs) -> bool | None: ...
    def onNodeChangeEvent(self, kwargs: ViewerStateNodeChangeKwargs) -> None: ...
    def onPlaybackChangeEvent(self, kwargs: ViewerStatePlaybackChangeKwargs) -> None: ...
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None: ...
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> None: ...
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> None: ...

def createViewerStateTemplate() -> hou.ViewerStateTemplate: ...
