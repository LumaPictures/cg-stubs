import hou
import typing
from .tool_helpers import is_curve_prim as is_curve_prim, point_group_string as point_group_string
from .undo_helpers import execute_with_undo as execute_with_undo
from collections.abc import Callable as Callable, Iterable, Mapping
from curvestate.curve3.adapters import SceneViewerAdapter as SceneViewerAdapter
from curvestate.curve3.controller import Curve3Controller as Curve3Controller, _DebugCommandResult
from curvestate.curve3.handle_manager import Curve3HandleProviderBase as Curve3HandleProviderBase
from curvestate.curve3.move_points import PointMoveSession as PointMoveSession
from curvestate.curve3.pick_controller import _CurvePickEvent, _HandlePointPickEvent
from curveutils import PickCurveResultType as PickCurveResultType
from houtypes import ViewerMenuItemState, ViewerStateCommandKwargs, ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateVolatileClientKwargs
from typing import Generic, Literal, TypeGuard

from typing import TypeVar
from typing import TypeVar
_OverrideT_co = TypeVar('_OverrideT_co', covariant=True, default=object)
class Curve3ToolBase(Generic[_OverrideT_co]):
    controller: Curve3Controller
    adapter: SceneViewerAdapter
    tool_name: str
    tool_label: str
    hud_hints: list[dict[str, str]]
    default_optype: str | None
    prompt_message: str
    def __init__(self, controller: Curve3Controller) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    def on_enter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def on_exit(self, kwargs: ViewerStateKwargs) -> None: ...
    def on_resume(self, kwargs: ViewerStateKwargs) -> None: ...
    def on_interrupt(self, kwargs: ViewerStateKwargs) -> None: ...
    def on_undo_or_redo(self) -> None: ...
    def on_draw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def on_mouse_event(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def on_key_event(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def on_key_transit_event(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def on_volatile_client_event(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def label(self) -> str:
        """Return the label expected by the framework HUD API."""
    def category(self) -> str:
        """Return the framework HUD category for all Curve3 tools."""
    def icon(self) -> str:
        """Return the icon used by the framework HUD for Curve3 tools."""
    def hudTemplate(self) -> list[dict[str, str]]:
        """Return this tool's HUD rows through the owning CurveState."""
    def onActivate(self, kwargs: Mapping[str, object] | None = None) -> None:
        """Framework activation entrypoint; sync the controller to this tool."""
    def onDeactivate(self) -> None:
        """Framework deactivation entrypoint; controller owns actual tool teardown."""
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Framework mouse entrypoint routed through controller-level handling."""
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> bool:
        """Framework draw entrypoint routed through controller-level drawing."""
    def onResume(self, kwargs: ViewerStateKwargs) -> None:
        """Framework resume entrypoint routed through controller-level handling."""
    def onInterrupt(self, kwargs: ViewerStateKwargs) -> None:
        """Framework interrupt entrypoint routed through controller-level handling."""
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Framework key entrypoint routed through controller-level handling."""
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Framework key-transit entrypoint routed through controller-level handling."""
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool:
        """Framework volatile-client entrypoint routed through controller handling."""
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool | _DebugCommandResult | None: ...
    def hotkey_create_mode_point_command(self) -> str | None:
        """Return the command for the shared create-mode-point hotkey."""
    def hotkey_delete_mode_action_command(self) -> str | None:
        """Return the command for the shared delete-mode-action hotkey."""
    def hotkey_accept_command(self) -> str | None:
        """Return the command for the shared accept hotkey."""
    def hud_tool_hints(self, *, hint_fn: Callable[[str, str], dict[str, str]], selection_hints: list[dict[str, str]], hotkey_refs: Mapping[str, str]) -> list[dict[str, str]]:
        """Return this tool's HUD hints in the exact tool-specific order."""
    def update_menu_item_states(self, menu_item_states: dict[str, ViewerMenuItemState], *, active: bool, set_visible_fn: Callable[[dict[str, ViewerMenuItemState], str, bool], object]) -> None:
        """Update context-menu state for items owned by this tool."""
    def handle_controller_command(self, command: str, args: object = None) -> bool:
        """Handle tool-owned controller commands before generic command routing."""
    def before_geometry_dependents_refresh(self) -> None:
        """Prepare tool-owned transient state before geometry-dependent rebuilds."""
    def after_geometry_dependents_refresh(self) -> None:
        """Restore tool-owned transient state after geometry-dependent rebuilds."""
    def operation_override_parms(self, optype: str) -> dict[str, _OverrideT_co]:
        """Return extra parms for a generic curve3core operation commit."""
    def commit_active_drag_for_command(self, command: str, sync_fn: Callable[[], object] | None = None) -> bool:
        """Commit any active tool-owned drag before running a command."""
    def active_tangent_drag_for_command(self) -> bool:
        """Return whether a command should preserve the single dragged tangent side."""
    def active_tangent_drag_group_for_command(self) -> str:
        """Return an existing active tangent-drag command group when available."""
    def requires_neutral_preview_for_parm_change(self) -> bool:
        """Return whether controller parm changes should preview through NOP."""
    def force_handle_visible(self) -> bool:
        """Return whether this tool requires the xform handle to stay visible."""
    def on_edit_plane_mode_changed(self, use_view_plane: bool) -> None:
        """Receive controller edit-plane mode changes relevant to this tool."""
    def drawable_should_select_single_result(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Return whether a valid single drawable hit should update selection."""
    def drawable_should_preselect_single_result(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Return whether selection should happen before pick-specific handling."""
    def drawable_should_clear_selection_on_empty_single(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Return whether an empty single-select click should clear selection."""
    def drawable_should_handle_box_selection(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Return whether drawable box selection should modify selection."""
    def drawable_should_start_box_selection(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Return whether this mouse event may start drawable box selection."""
    def drawable_get_drag_locate(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Return whether drawable selector should use drag-locate for this event."""
    def drawable_tangents_interactive(self) -> bool:
        """Return whether tangent point/line drawables should be pickable."""
    def drawable_allows_intool_orient_guide(self) -> bool:
        """Return whether frame-guide 'in tool' mode should build in this tool."""
    def drawable_overlay_geo(self, *, processed_geo: hou.Geometry, preview_geo: hou.Geometry) -> hou.Geometry:
        """Return the source geometry used for the transient overlay drawable."""
    def drawable_overlay_visible(self, *, interactive_drag_active: bool, processed_geo: hou.Geometry, preview_geo: hou.Geometry) -> bool:
        """Return whether the transient overlay drawable should be visible."""
    def drawable_overlay_uses_raw_source(self, *, source_geo: hou.Geometry, preview_geo: hou.Geometry) -> bool:
        """Return whether overlay source should bypass prepared curve filtering."""
    def get_prompt_message(self, kwargs: ViewerStateEventKwargs | None = None) -> str: ...
    def set_prompt_message(self, message: str) -> None: ...
    def refresh_prompt_message(self, kwargs: ViewerStateEventKwargs | None = None) -> None: ...
    def apply_curve_pick_full_curve_selection(self, pick_result: PickCurveResultType, modifier: hou.EnumValue[hou.pickModifier]) -> bool: ...
    def apply_curve_pick_segment_selection(self, pick_result: PickCurveResultType) -> bool: ...
    def handle_curve_pick_selection(self, kwargs: ViewerStateEventKwargs, handle_event: _CurvePickEvent) -> bool: ...
    def finish_drawing(self, and_close: bool = False) -> bool: ...
    def handle_provider(self) -> Curve3HandleProviderBase | None: ...
    @typing.overload
    def pick_internal_ptnum_from_handle_event(self, handle_event: _HandlePointPickEvent, *, required: Literal[True]) -> int: ...
    @typing.overload
    def pick_internal_ptnum_from_handle_event(self, handle_event: _HandlePointPickEvent, *, required: bool = ...) -> int | None: ...
    def begin_mmb_selected_point_move(self, ui_event: hou.ViewerEvent, move_session: PointMoveSession, *, selected_for_move: Iterable[int] | None = None, picked_ptnums: Iterable[int] | None = None) -> bool:
        """
        Shared MMB selected-point move bootstrap used by draw/edit tools.
        Assumes drawables were already fed the current mouse event so cached
        picked/selected points are current for this event.
        """
    def mmb_use_view_plane(self) -> bool: ...
    def draw_insert_preview(self, draw_handle: hou.Handle) -> None: ...
    def clear_insert_preview(self) -> None: ...
    def is_valid_insert_pick(self, pick: PickCurveResultType | None) -> TypeGuard[PickCurveResultType]: ...
    def update_insert_preview_from_hover(self, kwargs: ViewerStateEventKwargs, *, enabled: bool) -> PickCurveResultType | None: ...
    def commit_insert_from_pick(self, pick: PickCurveResultType | None, *, undo_label: str) -> bool: ...
