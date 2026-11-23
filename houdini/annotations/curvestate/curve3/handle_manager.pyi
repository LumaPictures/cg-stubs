from collections.abc import Callable
from typing import TypedDict

import hou
from apex import xformgadget as xg
from houtypes import (
    ViewerStateCommandKwargs,
    ViewerStateDrawKwargs,
    ViewerStateEnterKwargs,
    ViewerStateEventKwargs,
    ViewerStateKwargs,
    ViewerStateMenuActionKwargs,
    ViewerStateMenuPreOpenKwargs,
    ViewerStateParmChangeKwargs,
    ViewerStateVolatileClientKwargs,
)
from curvestate.curve3.controller import Curve3Controller
from curvestate.curve3.state import CurveState

def _mark_command_ret(command_args: object, handled: bool = ...) -> None: ...

# The context Curve3HandleManager._context() passes to the provider hooks.
class _HandleContext(TypedDict):
    controller: Curve3Controller
    geometry: hou.Geometry | None
    handle_manager: Curve3HandleManager

# A configure_instance() context also says whether the Apex instance was just added.
class _HandleInstanceContext(_HandleContext):
    new_instance: bool

# HandleTarget.metadata, as the providers in tool_edit fill it.
class _HandleTargetMetadata(TypedDict, total=False):
    position: hou.Vector3
    visual_override: tuple[int, ...]
    active_handles: tuple[int, ...]
    command_source_ptnums: tuple[int, ...]

# The handle manager's drag state; the orient/scale provider adds its own keys while dragging.
class _HandleDragState(TypedDict, total=False):
    target_key: str
    selected: tuple[int, ...]
    start_pos: hou.Vector3
    restore_group: str
    index: int
    restore_active_handles: list[int]
    start_xform_parms: dict[str, hou.Vector3]
    start_world_xform: hou.Matrix4
    start_world_center: hou.Vector3
    start_pivot_space_xform: hou.Matrix4
    active_handles: tuple[int, ...]
    visual_override: tuple[int, ...]
    command_source_ptnums: tuple[int, ...]
    orient_start_up: hou.Vector3
    orient_tangent: hou.Vector3
    change_relative: bool
    change_group: str
    current_value: float | hou.Vector3
    scale_start_value: float

# The events apex.xformgadget.ApexXformHandle sends its handle callbacks (its
# _processHandle*() methods); `event_kwargs` is the viewer state event that caused it, if any.
class _XformHandleEventBase(TypedDict):
    index: int
    event_kwargs: ViewerStateKwargs | None

class _XformHandleCustomActionEvent(_XformHandleEventBase):
    menu_item: str

class _XformHandleUpdateEvent(_XformHandleEventBase):
    name: str
    parms: dict[str, hou.Vector3] | None
    in_undo: bool
    interactive: bool

class _XformHandleStartEvent(_XformHandleUpdateEvent):
    component: str
    pivot_mode: bool

# An xformgadget handle instance's settings (apex.xformgadget._defaultHandleSettings()); the
# toggles are ints, and updateSetting() can add other keys.
class _XformHandleSettings(TypedDict):
    rOrd: int
    xOrd: int
    pre_rOrd: int
    pre_xOrd: int
    xform_mode: str
    t_alignment: str
    r_alignment: str
    s_alignment: str
    separate_align: int
    name: str
    label: str
    gimbal_mode: int
    pivot_mode: int
    enabled_components: dict[str, int]
    visible: int
    enabled_modes: dict[str, bool]
    reflection_hint: hou.Vector3
    has_reflection_hint: bool

class _XformHandleSettingsEvent(_XformHandleEventBase):
    name: str
    settings: _XformHandleSettings | None
    in_undo: bool

class HandleTarget:
    metadata: _HandleTargetMetadata

class Curve3HandleProviderBase:
    def build_targets(self, context: _HandleContext) -> list[HandleTarget]: ...
    def configure_instance(self, manager: Curve3HandleManager, instance_index: int, target: HandleTarget, context: _HandleInstanceContext) -> None: ...
    def on_handle_start(self, event: _XformHandleStartEvent, target: HandleTarget, context: _HandleContext) -> None: ...
    def on_handle_update(self, event: _XformHandleUpdateEvent, target: HandleTarget, context: _HandleContext) -> None: ...
    def on_handle_end(self, event: _XformHandleUpdateEvent, target: HandleTarget, context: _HandleContext) -> None: ...
    def on_settings_update(self, event: _XformHandleSettingsEvent, target: HandleTarget, context: _HandleContext) -> None: ...
    def on_custom_action(self, event: _XformHandleCustomActionEvent, target: HandleTarget, context: _HandleContext) -> None: ...

class Curve3HandleManager:
    controller: Curve3Controller
    _drag_state: _HandleDragState | None
    def __init__(self, controller: Curve3Controller) -> None: ...
    def get_xform_gadget(self) -> xg.ApexXformHandle | None: ...
    def reset_gadget_instance_xform_parms(self, index: int) -> None: ...
    def _reset_gadget_instance_scale_parm(self, index: int) -> None: ...
    def set_provider(self, provider: Curve3HandleProviderBase | None) -> None: ...
    def set_state_owner(self, state_owner: CurveState | None) -> None: ...
    def set_hotkey_context(self, hotkey_context: str) -> None: ...
    def initialize(self) -> None: ...
    def set_visible(self, visible: bool) -> None: ...
    def on_enter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def on_exit(self, kwargs: ViewerStateKwargs) -> None: ...
    def on_resume(self, kwargs: ViewerStateKwargs) -> None: ...
    def on_interrupt(self, kwargs: ViewerStateKwargs) -> None: ...
    def on_draw_setup(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def on_draw_opaque(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def on_draw_transparent(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def on_draw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def on_draw_interrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def on_mouse_event(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def on_key_event(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def on_key_transit_event(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def on_parm_change_event(self, kwargs: ViewerStateParmChangeKwargs) -> None: ...
    def on_volatile_client_event(self, kwargs: ViewerStateVolatileClientKwargs) -> None: ...
    def on_command(self, kwargs: ViewerStateCommandKwargs) -> bool: ...
    def _prepare_edit_handle_switch(self, kwargs: ViewerStateCommandKwargs) -> None: ...
    def _ensure_edit_handle_visible(self, kwargs: ViewerStateCommandKwargs) -> None: ...
    def on_menu_pre_open(self, kwargs: ViewerStateMenuPreOpenKwargs) -> bool: ...
    def on_menu_action(self, kwargs: ViewerStateMenuActionKwargs) -> bool: ...
    def _external_pick(self, kwargs: ViewerStateEventKwargs) -> dict[str, hou.Vector3 | str] | None: ...
    def commit_active_drag_for_command(self, command: str, sync_fn: Callable[[], object] | None = ...) -> bool: ...
    def refresh_instances(self, force: bool = ...) -> None: ...
    def _context(self) -> _HandleContext: ...
    def event_xform_parms(self, event: _XformHandleEventBase) -> dict[str, hou.Vector3]: ...
    def _target_from_event(self, event: _XformHandleEventBase) -> HandleTarget: ...
    def _event_position(self, event: _XformHandleEventBase) -> hou.Vector3: ...
    def _on_handle_start(self, event: _XformHandleStartEvent) -> None: ...
    def _on_handle_update(self, event: _XformHandleUpdateEvent) -> None: ...
    def _on_handle_end(self, event: _XformHandleUpdateEvent) -> None: ...
    def _on_handle_settings_update(self, event: _XformHandleSettingsEvent) -> None: ...
    def _on_handle_custom_action(self, event: _XformHandleCustomActionEvent) -> None: ...
    def drag_state(self) -> _HandleDragState | None: ...
    def _sync_instances(
        self,
        targets: list[HandleTarget],
        context: _HandleContext,
        *,
        preserved_xform_state_by_key: dict[str, dict[str, object]] | None = ...,
    ) -> None: ...
