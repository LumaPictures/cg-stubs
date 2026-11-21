# Houdini stubs generated from Houdini 22.0.466

import _cop as COP
import dbg as DBG
import enum as ENUM
import hou as HOU
import staterecordutils as SRU
import typing as TY
from . import core as CORE
from collections.abc import Callable as Callable, Sequence
from dataclasses import dataclass as DATACLASS
from houtypes import NodeEventKwargs, ViewerStateCommandKwargs, ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs
from typing import Any, Protocol, TypeAlias, Unpack

from typing import TypeAlias
_CopOutput: TypeAlias = HOU.ImageLayer | HOU.NanoVDB | HOU.DetachedAttrib | HOU.Geometry
_ActionKwargs: TypeAlias = ViewerStateMenuActionKwargs | ViewerStateEventKwargs
RVS: TypeAlias = SRU.RecordableViewerState
class _NodeEventCallback(Protocol):
    def __call__(self, **kwargs: Unpack[NodeEventKwargs]) -> object: ...
ITY = CORE.InvokeType
HUER: type[HOU.uiEventReason]
SHOULD_DEBUG: bool

def debug_print(*args: object) -> None: ...

class GeoDrawableParmNames(ENUM.StrEnum):
    COLOUR_1 = 'color1'
    FADE_FACTOR = 'fade_factor'
    LINE_WIDTH = 'line_width'

class ViewerStateArgNames(ENUM.StrEnum):
    COMMAND = 'command'
    COMMAND_ARGS = 'command_args'
    DRAW_HANDLE = 'draw_handle'
    MENU_ITEM = 'menu_item'
    MENU_ITEM_STATES = 'menu_item_states'
    NODE = 'node'
    PARM_NAME = 'parm_name'
    PARM_TUPLE = 'parm_tuple'
    SCENE_VIEWER = 'scene_viewer'
    TYPE = 'type'
    UI_EVENT = 'ui_event'
    VALUE = 'value'

class Names(ENUM.StrEnum):
    FULL_VIS = 'FULL_VIS'
    LAYERS = 'layers'
    STASH = 'stash'
    UV_GEO = 'UV_GEO'

ICON_NAME: str
TOOL_LABEL: str
MENU_LABEL: str
MAIN_MENU_ID: str
VIEWERSTATE_TYPE_NAME: str
DEFAULT_CURSOR_PROMPT: str
HUD_TITLE: str
RADIAL_MENU_NAME: str
SPACE_COUNT: int
RESIZE_STROKE_BASE_MULT: float
RESIZE_WHEEL_BASE_MULT: float
EMPTY_GEO: HOU.Geometry
STROKE_REASONS: tuple[HOU.EnumValue[HOU.uiEventReason], ...]
START_STROKE_REASONS: tuple[HOU.EnumValue[HOU.uiEventReason], ...]
END_STROKE_REASONS: tuple[HOU.EnumValue[HOU.uiEventReason], ...]
HK_CTX: str
BRUSH_INVALIDATING_PARM_NAMES: tuple[str, ...]
SOP_VERB: Callable[[str], HOU.OpVerb | None]

class ColourIdxs(ENUM.IntEnum):
    FG = 0
    BG = 1

PALETTE_IDX_LABELS: tuple[str, str]
PALETTE_PARM_NAMES: list[tuple[str, ...]]

@DATACLASS
class Brush:
    start_stroke: Callable[[_CopOutput, _CopOutput], list[_CopOutput]]
    apply_stamps: Callable[[_CopOutput, _CopOutput, _CopOutput, _CopOutput, _CopOutput], list[_CopOutput]]
    finish_stroke: Callable[[_CopOutput, _CopOutput, _CopOutput], list[_CopOutput]]

USE_ADVANCED_DRAWABLES: bool
CURSOR_COLOUR: HOU.Vector3
CURSOR_COLOUR_VEC: HOU.Vector3
LM_CIRCLE_COLOUR: HOU.Vector3
LM_UNSTRETCHED_COLOUR: HOU.Vector3
LM_STRETCHED_COLOUR: HOU.Vector3
circle_verb: HOU.OpVerb | None
circle_geo: HOU.Geometry
CURSOR_GEO: HOU.Geometry
LM_CIRCLE_GEO: HOU.Geometry
LM_ARC_GEO: HOU.Geometry
line_verb: HOU.OpVerb | None
LM_CXN_GEO: HOU.Geometry
stash: HOU.Node | None

@DATACLASS
class CursorScreenPose:
    ndc: HOU.Vector2

@DATACLASS
class CursorWorldPose:
    pos: HOU.Vector3
    nml: HOU.Vector3
CursorPose = CursorScreenPose | CursorWorldPose

class MouseButton(ENUM.IntEnum):
    LEFT = 0
    MIDDLE = 1

MOUSE_BUTTONS: tuple[MouseButton, ...]
MOUSE_BUTTON_NAMES: tuple[str, str]

@DATACLASS
class MouseModProps:
    name: str
    lmb_brush: CORE.Tool

class MouseMod(ENUM.IntEnum):
    NONE = 0
    SHIFT = 1
    CTRL = 2
    COUNT = 3
    def props(self: TY.Self) -> MouseModProps: ...

MOUSE_MODS: tuple[MouseMod, ...]
MOUSE_MOD_PROPS: tuple[MouseModProps, MouseModProps, MouseModProps]

def opnode_dev_get_brush_tool(opnode: HOU.OpNode, dev: HOU.UIEventDevice, mouse_button: MouseButton) -> CORE.Tool | None: ...

@DATACLASS
class Mousebind:
    button: MouseButton
    mod: MouseMod

BRUSH_TOOL_BINDINGS: tuple[tuple[CORE.Tool | None, ...], ...]
STATIC_MOUSEBINDS: tuple[Mousebind, ...]

class HudRowNames:
    BRUSH_RADIUS: str
    BRUSH_RADIUS_G: str
    LM_RADIUS: str
    LM_RADIUS_G: str
    BRUSH_OPACITY: str
    BRUSH_OPACITY_G: str
    BRUSH_FLOW: str
    BRUSH_FLOW_G: str
    LMB: str
    TOOL: str
    TOOL_G: str

ON_OFF_STRS: tuple[str, str]

def device_event_is_key(dev: HOU.UIEventDevice) -> bool: ...
def opnode_get_layer(opnode: HOU.OpNode, path: str) -> HOU.ImageLayer | None: ...
def opnode_get_geo(opnode: HOU.OpNode, path: str) -> HOU.Geometry | None: ...
def opnode_get_uv_geo(opnode: HOU.OpNode) -> HOU.Geometry | None: ...
def opnode_get_lm_radius(opnode: HOU.OpNode) -> float: ...
def opnode_get_refl_sym(opnode: HOU.OpNode) -> COP.ReflectionSymmetry | None: ...
def opnode_get_radius_parm(opnode: HOU.OpNode, tool: CORE.Tool, space: int) -> HOU.Parm | None: ...
def opnode_get_radius(opnode: HOU.OpNode, tool: CORE.Tool, align: int) -> float | None: ...
def opnode_get_brush(opnode: HOU.OpNode, tool: CORE.Tool) -> Brush | None: ...
def opnode_get_sampling_layer(paint_node: HOU.OpNode, should_sample_result_parm_name: str) -> HOU.ImageLayer | None: ...
def vec3_get_ortho(v: HOU.Vector3) -> HOU.Vector3: ...
def viewport_get_cam_pos(vp: HOU.GeometryViewport) -> HOU.Vector3: ...

@DATACLASS
class WriteMaskCacheEntry:
    orig: HOU.ImageLayer
    reflected: HOU.ImageLayer | None

@DATACLASS
class WriteMaskTable:
    value: dict[HOU.Vector3, WriteMaskCacheEntry]

@DATACLASS
class UniformWriteMask:
    value: HOU.ImageLayer
WriteMaskCache = UniformWriteMask | WriteMaskTable

class ViewerState(RVS):
    scene_viewer: HOU.SceneViewer
    raycache: HOU.GeometryRayCache
    opnode_to_on_geo_changed: dict[HOU.OpNode, _NodeEventCallback]
    stroke_reg: COP.StrokeRegulator
    group_mask: HOU.ImageLayer | None
    vis_cam_pos: None
    lm_cxn_geo_colour: HOU.Vector3 | tuple[float, ...]
    cursor: HOU.GeometryDrawable
    lm_cursor: HOU.GeometryDrawable
    lm_cxn: HOU.GeometryDrawable
    prev_radial_menu: str
    brushes: list[Brush | None]
    drag_start_mouse_sum: float | None
    drag_start_radius: float
    lm_resized: bool
    press_time: float
    sd_raw_stroke: HOU.Geometry | None
    sd_stroke_state: _CopOutput | None
    sd_writing_colour: HOU.ImageLayer | None
    sd_writing_alpha: _CopOutput | None
    pos_map: HOU.ImageLayer | None
    normal_map: HOU.ImageLayer | None
    cursor_pose: COP.CursorPose | None
    cursor_ndc: HOU.Vector2 | None
    def __init__(self: TY.Self, scene_viewer: HOU.SceneViewer, **kwargs: Any) -> None: ...
    write_masks: WriteMaskCache | None
    def reset_write_masks(self: TY.Self) -> None: ...
    def cached_write_mask(self: TY.Self, vp_cam_pos: HOU.Vector3) -> WriteMaskCacheEntry | None: ...
    def make_geo_drawable(self: TY.Self, label: str, colour: Sequence[float] | None) -> HOU.GeometryDrawable: ...
    curr_tool: CORE.Tool | None
    lm_resize_is_held: bool
    is_in_stroke: bool
    brush_is_valid: bool
    def onEnter(self: TY.Self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def onExit(self: TY.Self, kwargs: ViewerStateKwargs) -> None: ...
    @RVS.recordableEvent
    def onResume(self: TY.Self, kwargs: ViewerStateKwargs) -> bool: ...
    @RVS.recordableEvent
    def onInterrupt(self: TY.Self, kwargs: ViewerStateKwargs) -> bool: ...
    @RVS.recordableEvent
    def onMouseWheelEvent(self: TY.Self, kwargs: ViewerStateEventKwargs) -> bool: ...
    @RVS.recordableEvent
    def onMouseEvent(self: TY.Self, kwargs: ViewerStateEventKwargs) -> bool: ...
    @RVS.recordableEvent
    def onKeyEvent(self: TY.Self, kwargs: ViewerStateEventKwargs) -> bool | None: ...
    @RVS.recordableEvent
    def onKeyTransitEvent(self: TY.Self, kwargs: ViewerStateEventKwargs) -> bool | None: ...
    @RVS.recordableEvent
    def onMenuAction(self: TY.Self, kwargs: ViewerStateMenuActionKwargs) -> bool: ...
    def onMenuPreOpen(self: TY.Self, kwargs: ViewerStateMenuPreOpenKwargs) -> None: ...
    @RVS.recordableEvent
    def onCommand(self: TY.Self, kwargs: ViewerStateCommandKwargs) -> bool: ...
    def on_parm_changed(self: TY.Self, **kwargs: Any) -> None: ...
    def store_all_brushes(self: TY.Self, opnode: HOU.OpNode) -> None: ...
    def store_brush(self: TY.Self, opnode: HOU.OpNode, tool: CORE.Tool) -> None: ...
    def update_brush_radius_hud_rows(self: TY.Self, opnode: HOU.OpNode) -> None: ...
    def update_lm_activity_hud_row(self: TY.Self, opnode: HOU.OpNode) -> None: ...
    def update_lm_radius_hud_rows(self: TY.Self, opnode: HOU.OpNode) -> None: ...
    def update_brush_opacity_hud_rows(self: TY.Self, opnode: HOU.OpNode) -> None: ...
    def update_brush_flow_hud_rows(self: TY.Self, opnode: HOU.OpNode) -> None: ...
    def update_lmb_hud_rows(self: TY.Self, opnode: HOU.OpNode) -> None: ...
    def update_align_hud_row(self: TY.Self, opnode: HOU.OpNode) -> None: ...
    def update_paint_2d_hud_row(self: TY.Self, opnode: HOU.OpNode) -> None: ...
    def update_mask_vis_hud_row(self: TY.Self, opnode: HOU.OpNode) -> None: ...
    def flash_msg(self: TY.Self, msg: str) -> None: ...
    def is_composite_view(self: TY.Self) -> bool: ...
    def show_error(self: TY.Self, text: str) -> None: ...
    def show_bad_brush_error(self: TY.Self) -> None: ...
    def get_adjusted_parm(self: TY.Self, opnode: HOU.OpNode, hint: CORE.Tool | None) -> HOU.Parm | None: ...
    @DBG.ZoneScopedDecorator
    def on_mouse_event_impl(self: TY.Self, kwargs: ViewerStateEventKwargs) -> None: ...
    def cam(self: TY.Self) -> COP.StrokeRegulatorCamera: ...
    @DBG.ZoneScopedDecorator
    def update_cursor(self: TY.Self, opnode: HOU.OpNode, mouse_ndc: HOU.Vector2 | None) -> None: ...
    def finish_stroke(self: TY.Self, opnode: HOU.OpNode) -> None: ...
    def shoot_ray(self: TY.Self, opnode: HOU.OpNode, cam: COP.StrokeRegulatorCamera, ndc: HOU.Vector2) -> tuple[float, float] | None: ...
    def handle_sample_stroke(self: TY.Self, opnode: HOU.OpNode, cam: COP.StrokeRegulatorCamera, ndc: HOU.Vector2) -> None: ...
    def handle_fill(self: TY.Self, opnode: HOU.OpNode, cam: COP.StrokeRegulatorCamera, ndc: HOU.Vector2) -> None: ...
    def handle_adjust_stroke(self: TY.Self, opnode: HOU.OpNode, ev: HOU.ViewerEvent, is_start_of_stroke: bool) -> None: ...
    def finish_resize_stroke(self: TY.Self) -> None: ...
    @DBG.ZoneScopedDecorator
    def handle_brush_stroke(self: TY.Self, opnode: HOU.OpNode, ev: HOU.ViewerEvent, tool: CORE.Tool, stamp_xforms: COP.StampXforms) -> None: ...
    def finish_brush_stroke(self: TY.Self) -> None: ...
    def get_on_geo_changed(self: TY.Self, opnode: HOU.OpNode) -> _NodeEventCallback: ...
    def on_key_event_impl(self: TY.Self, kwargs: ViewerStateEventKwargs, is_transit: bool) -> bool | None: ...
    def swap_colours(self: TY.Self, kwargs: _ActionKwargs) -> None: ...
    def reset_all(self: TY.Self, kwargs: _ActionKwargs, opnode: HOU.OpNode) -> None: ...
    def end_undo(self: TY.Self) -> None: ...
    def defensively_end_undo(self: TY.Self) -> None: ...
    def begin_undo(self: TY.Self, label: str) -> None: ...
    def lm_resize(self: TY.Self, kwargs: _ActionKwargs) -> None: ...
    def clear_curr_layer(self: TY.Self, opnode: HOU.OpNode, mask_val: float) -> None: ...
    def clear_colour_mask_black(self: TY.Self, kwargs: _ActionKwargs) -> None: ...
    def clear_colour_mask_white(self: TY.Self, kwargs: _ActionKwargs) -> None: ...
    def toggle_align(self: TY.Self, kwargs: _ActionKwargs) -> None: ...
    def toggle_mask_vis(self: TY.Self, kwargs: _ActionKwargs) -> None: ...
    def toggle_paint_2d(self: TY.Self, kwargs: _ActionKwargs) -> None: ...
    def viewport_is_uv(self: TY.Self) -> bool: ...
    @DBG.ZoneScopedDecorator
    def compute_pos_map(self: TY.Self, opnode: HOU.OpNode) -> bool: ...
    @DBG.ZoneScopedDecorator
    def compute_pos_and_write_masks(self: TY.Self, opnode: HOU.OpNode) -> bool: ...
    def effective_stroke_align(self: TY.Self, opnode: HOU.OpNode) -> int: ...
    def onDraw(self: TY.Self, kwargs: ViewerStateDrawKwargs) -> None: ...

def make_switch_to_tool(tool: CORE.Tool) -> Callable[[ViewerState, _ActionKwargs], None]: ...

@DATACLASS
class ActionProps:
    label: str
    default_key: str
    handler_is_transit: bool
    proc: Callable[[ViewerState, _ActionKwargs], None]
    def hk_id(self: TY.Self) -> str: ...
    def hk_ref(self: TY.Self) -> str: ...

class Action(ENUM.IntEnum):
    PAINT = 0
    ERASE = 1
    SMOOTH = 2
    SAMPLE = 3
    FILL = 4
    CLEAR_COLOUR_MASK_WHITE = 5
    CLEAR_COLOUR_MASK_BLACK = 6
    TOGGLE_ALIGN = 7
    SWAP_COLOURS = 8
    TOGGLE_PAINT_2D = 9
    TOGGLE_MASK_VIS = 10
    LAZY_MOUSE = 11
    def props(self: TY.Self) -> ActionProps: ...

ACTIONS: tuple[Action, ...]
ACTION_PROPS: tuple[ActionProps, ...]
SWITCH_TOOL_ACTIONS: tuple[Action, ...]

@DATACLASS
class ToggleAction:
    action: Action
    parm_name: str

TOGGLE_ACTIONS: tuple[ToggleAction, ToggleAction, ToggleAction]
AXN_MENU_ID_PREFIX: str

def action_is_bound(axn: Action) -> bool: ...
def action_to_name_str(axn: Action) -> str: ...

action_to_hud_row_name: Callable[[Action], str]
axn_to_menu_id: Callable[[Action], str]

def menu_id_to_axn(menu_id: str) -> Action: ...
def createViewerStateTemplate() -> HOU.ViewerStateTemplate: ...
