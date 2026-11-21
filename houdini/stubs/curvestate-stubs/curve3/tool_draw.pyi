import hou
from . import referencegeo as referencegeo
from .debug import debug_print as debug_print
from .drawables import Curve3SinglePointPreviewDrawable as Curve3SinglePointPreviewDrawable
from .move_points import PointMoveSession as PointMoveSession
from .pick import pick_on_plane as pick_on_plane
from .tool_base import Curve3ToolBase as Curve3ToolBase
from .tool_helpers import anchor_ptnums_from_ptnums as anchor_ptnums_from_ptnums, build_handle_point_drag_context as build_handle_point_drag_context, draw_points_required as draw_points_required, format_pos3_list_string as format_pos3_list_string, is_curve_prim as is_curve_prim, remap_retracted_tangent_to_anchor as remap_retracted_tangent_to_anchor, should_commit_draw_event as should_commit_draw_event
from .undo_helpers import execute_with_undo as execute_with_undo
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from curvestate.curve3.controller import Curve3Controller as Curve3Controller
from curvestate.curve3.pick_controller import _CurvePickEvent, _HandlePointPickEvent
from curvestate.curve3.referencegeo import _AmbiguousNodeEndpoint
from dataclasses import dataclass, field
from houtypes import ViewerMenuItemState, ViewerStateDrawKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateVolatileClientKwargs
from typing import Literal, TypeAlias


from typing import TypeAlias
_PseudoHandle: TypeAlias = tuple[hou.Vector3 | None, hou.Vector3, hou.Vector3, bool, int] | tuple[hou.Vector3 | None, hou.Vector3, hou.Vector3, bool, None, str]
ContinuationPick: TypeAlias = tuple[hou.Prim, float | int, hou.Vector3 | None, int]
class _DrawModeBase:
    """Base mode class for draw-tool state machine."""
    name: str
    def on_mouse_event(self, tool: Curve3DrawTool, kwargs: ViewerStateEventKwargs, drawable_handled: bool) -> bool:
        """Return the default handled state for a draw-mode mouse event."""

class _ChooseLocationMode(_DrawModeBase):
    """Curve2-style choose-location mode before segment placement starts."""
    name: str
    def on_mouse_event(self, tool: Curve3DrawTool, kwargs: ViewerStateEventKwargs, drawable_handled: bool) -> bool:
        """Route mouse input while choosing the first or next draw location."""

class _SegmentAddMode(_DrawModeBase):
    """Curve2-style segment-add mode while placing points on an active segment."""
    name: str
    def on_mouse_event(self, tool: Curve3DrawTool, kwargs: ViewerStateEventKwargs, drawable_handled: bool) -> bool:
        """Route mouse input while adding points to the active segment."""

class _AutoSegmentAddMode(_SegmentAddMode):
    """
    Reserved mode for auto-draw parity.
    Behavior currently routes through segment-add semantics.
    """
    name: str

@dataclass
class DrawSessionState:
    """Transient draw-session state storage."""
    last_draw_pos: hou.Vector3 | None = ...
    last_hover_pos: hou.Vector3 | None = ...
    drag_start_pos: hou.Vector3 | None = ...
    drag_active: bool = ...
    drawing_active: bool = ...
    segment_points: list[hou.Vector3] = field(default_factory=list)
    continue_pick: ContinuationPick | None = ...
    continue_prepend: bool = ...
    continue_from_curve: bool = ...
    pending_endpoint_pick: ContinuationPick | None = ...
    pending_anchor_point: hou.Point | None = ...
    preview_live: bool = ...
    suppress_next_segment_pick: bool = ...
    pseudo_preview_key: tuple[float | bool | None, ...] | None = ...
    continue_ref_internal_ptnum: int | None = ...
    continue_target_internal_ptnum: int | None = ...
    continue_ref_pos: hou.Vector3 | None = ...
    pending_start_branch_target_ptnum: int | None = ...
    segment_drawsymmetric: bool = ...
    tangent_break_frozen_pos: hou.Vector3 | None = ...
    pending_outgoing_tangent_pos: hou.Vector3 | None = ...
    next_outgoing_tangent_pos: hou.Vector3 | None = ...
    segment_force_corner: bool = ...
    draw_arc_active: bool = ...
    topology_resume_drawing: bool = ...
    topology_resume_prepend: bool = ...
    suppress_topology_cleanup: bool = ...

@dataclass(frozen=True)
class DrawTarget:
    """Resolved target for one draw commit."""
    kind: str
    point: hou.Point | None = ...
    endpoint_pick: ContinuationPick | None = ...
    @property
    def ptnum(self) -> int | None:
        """Return the target point number in reference-geometry space."""

class ContinuationResolver:
    """Shared continuation identity + endpoint mapping logic for draw tool."""
    tool: Curve3DrawTool
    def __init__(self, tool: Curve3DrawTool) -> None:
        """Bind continuation resolution helpers to a draw tool instance."""
    def internal_from_preview_curve_endpoint(self, prim: hou.Prim | None, endpoint_code: int) -> int:
        """Resolve a preview-curve endpoint to its internal point number."""
    def endpoint_pick_from_point(self, point: hou.Point | None) -> ContinuationPick | None:
        """Convert an endpoint point into a normalized endpoint pick."""
    def endpoint_pick_from_internal_ptnum(self, internal_ptnum: int) -> ContinuationPick | None:
        """Resolve an internal endpoint point number to a node endpoint pick."""
    def normalize_pending_endpoint_pick(self, pick: ContinuationPick | None, context: str) -> tuple[ContinuationPick | None, bool]:
        """Normalize a pending endpoint pick to current node-geometry identity."""
    def resolve_continue_pick(self) -> tuple[ContinuationPick | None, bool]:
        """Consume and normalize the pending endpoint used to continue a curve."""
    def peek_continue_pick(self) -> tuple[ContinuationPick | None, bool]:
        """Return the current continuation endpoint without consuming it."""
    def set_continuation_pick(self, pick: ContinuationPick | None, prepend: bool) -> None:
        """Store the active continuation endpoint and reference identity."""
    def capture_reference_from_pick(self, pick: ContinuationPick | None, prepend: bool) -> None:
        """Capture stable endpoint identity for continuation rebinding."""
    def rebind_continue_pick_from_reference(self, prepend: bool) -> ContinuationPick | None:
        """Refresh continuation endpoint state after topology changes."""
    def current_curve_end_pick(self, prepend: bool = False, force_last: bool = False) -> ContinuationPick | None:
        """Return an endpoint pick for the active curve end in reference geometry."""
    def internal_from_node_curve_endpoint(self, node_geo: hou.Geometry, node_prim: hou.Prim, endpoint_code: int) -> int | None:
        """Delegate node endpoint to internal-point mapping to reference geometry."""
    def map_internal_to_node_endpoint(self, internal_ptnum: int) -> tuple[hou.Prim, int, hou.Vector3, int] | Literal[_AmbiguousNodeEndpoint.AMBIGUOUS_NODE_ENDPOINT] | None:
        """Delegate internal-point to node endpoint mapping to reference geometry."""

class DrawPreviewPipeline:
    """Hover preview + pseudo tangent preview orchestration."""
    tool: Curve3DrawTool
    def __init__(self, tool: Curve3DrawTool) -> None:
        """Bind preview orchestration to a draw tool instance."""
    def update_hover_preview(self, kwargs: ViewerStateEventKwargs, ui_event: hou.ViewerEvent) -> None:
        """Update hover preview geometry and pseudo handles for the cursor."""
    def update_drag_pseudo_handles(self, hover_pos: hou.Vector3, preview_geo: hou.Geometry | None = None, ui_event: hou.ViewerEvent | None = None) -> None:
        """Refresh pseudo tangent handles shown during draw hover/drag preview."""
    def build_drag_pseudo_handles(self, hover_pos: hou.Vector3, preview_geo: hou.Geometry | None = None, ui_event: hou.ViewerEvent | None = None) -> list[_PseudoHandle]:
        """Build pseudo tangent handle payloads for active Bezier draw preview."""
    def continuation_endpoint_pseudo_handle(self) -> _PseudoHandle | None:
        """Build a pseudo handle for the existing endpoint being continued."""
    def continuation_endpoint_preview_pseudo_handle(self, preview_geo: hou.Geometry | None) -> _PseudoHandle | None:
        """Build a pseudo handle from preview geometry for the continued endpoint."""
    def join_target_preview_pseudo_handle(self, preview_geo: hou.Geometry | None, target_ptnum: int) -> _PseudoHandle | None:
        """Build a pseudo handle for a previewed join target point."""
    def set_pseudo_handle_preview(self, handles: Sequence[_PseudoHandle]) -> None:
        """Publish pseudo handle preview points when the payload changes."""
    def clear_pseudo_handle_preview(self) -> None:
        """Clear active pseudo tangent handle preview points."""
    def preview_points_for_hover(self, hover_pos: hou.Vector3, ui_event: hou.ViewerEvent | None = None) -> list[hou.Vector3]:
        """Return preview curve points implied by current draw state and hover."""
    def update_preview_curve_drawable(self, preview_points: Iterable[hou.Vector3], preview_pick: ContinuationPick | None, preview_prepend: bool, *, draw_symmetric: bool = True, force_corner: bool = False, force_balanced: bool = False) -> hou.Geometry | None:
        """Build and display preview curve geometry for the current draw segment."""

class DrawCommitPipeline:
    """Segment accumulation -> SOP commit orchestration."""
    tool: Curve3DrawTool
    def __init__(self, tool: Curve3DrawTool) -> None:
        """Bind commit orchestration to a draw tool instance."""
    def commit_if_ready(self) -> bool:
        """Commit the current segment once enough points have been accumulated."""

class Curve3DrawTool(Curve3ToolBase):
    tool_name: str
    tool_label: str
    default_optype: str | None
    hud_hints: list[dict[str, str]]
    prompt_message: str
    draw_on_view_plane: bool
    def __init__(self, controller: Curve3Controller) -> None:
        """Create draw-mode state, preview drawables, and drag sessions."""
    @property
    def last_draw_pos(self) -> hou.Vector3 | None:
        """Return the last committed or previewed draw position."""
    @last_draw_pos.setter
    def last_draw_pos(self, value: hou.Vector3 | None) -> None:
        """Store the last committed or previewed draw position."""
    def _fresh_curve_start_position(self, kwargs: ViewerStateEventKwargs, ui_event: hou.ViewerEvent) -> hou.Vector3 | None:
        """Resolve the start position for a new curve-start gesture."""
    def _commit_position(self, kwargs: ViewerStateEventKwargs, ui_event: hou.ViewerEvent, pending_anchor: hou.Point | None, *, use_drag_release: bool) -> hou.Vector3 | None:
        """Resolve the point position to commit for a completed draw gesture."""
    def on_activate(self) -> None:
        """Prepare a neutral draw state when the tool becomes active."""
    def on_deactivate(self) -> None:
        """Stop draw interactions and clear transient draw state."""
    def on_interrupt(self, kwargs: ViewerStateKwargs) -> None:
        """Cancel active dragging without discarding continuation context."""
    def on_undo_or_redo(self) -> None:
        """End active gestures while preserving active draw continuation for rebuild."""
    def before_geometry_dependents_refresh(self) -> None:
        """Drop topology-derived draw previews before geometry is rebuilt."""
    def after_geometry_dependents_refresh(self) -> None:
        """Re-arm drawing from the current curve endpoint after topology changes."""
    def on_exit(self, kwargs: ViewerStateKwargs) -> None:
        """Stop draw interactions when leaving the viewer state."""
    def on_draw(self, kwargs: ViewerStateDrawKwargs) -> None:
        """Draw draw-mode-only overlays."""
    def on_pick_curve(self, kwargs: ViewerStateEventKwargs, handle_event: _CurvePickEvent) -> bool:
        """Handle curve picks for draw-mode insert and continuation workflows."""
    def on_pick_handle_point(self, kwargs: ViewerStateEventKwargs, handle_event: _HandlePointPickEvent) -> bool:
        """Handle point picks for tangent moves, endpoint continuation, and anchors."""
    def on_mouse_event(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Process draw-tool mouse events after drawable pick dispatch."""
    def handle_controller_command(self, command: str, args: object = None) -> bool:
        """Handle draw-specific finish commands."""
    def on_key_transit_event(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Use the shared A hotkey as a volatile draw-arc modifier in draw mode."""
    def on_volatile_client_event(self, kwargs: ViewerStateVolatileClientKwargs) -> bool:
        """Disable draw-arc mode when the A volatile client is released."""
    def hotkey_accept_command(self) -> str | None:
        """Finish the active draw curve for the shared accept hotkey."""
    def hotkey_delete_mode_action_command(self) -> str | None:
        """Delete selected points for the shared delete-mode hotkey."""
    def hud_tool_hints(self, *, hint_fn: Callable[[str, str], dict[str, str]], selection_hints: list[dict[str, str]], hotkey_refs: Mapping[str, str]) -> list[dict[str, str]]:
        """Return draw HUD hints in the established order."""
    def update_menu_item_states(self, menu_item_states: dict[str, ViewerMenuItemState], *, active: bool, set_visible_fn: Callable[[dict[str, ViewerMenuItemState], str, bool], object]) -> None:
        """Show draw-only context-menu actions only while draw mode is active."""
    def requires_neutral_preview_for_parm_change(self) -> bool:
        """Drawing sessions recook parm changes through NOP to avoid stale append previews."""
    def on_edit_plane_mode_changed(self, use_view_plane: bool) -> None:
        """Use controller view-plane mode for draw placement."""
    def drawable_should_select_single_result(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Allow draw-mode drawable selection only for MMB point-move setup."""
    def drawable_should_preselect_single_result(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Draw MMB needs selection before draw-mode move/finish routing sees it."""
    def drawable_should_clear_selection_on_empty_single(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Never clear draw selection from empty drawable hits."""
    def commit_active_drag_for_command(self, command: str, sync_fn: Callable[[], object] | None = None) -> bool:
        """Commit the draw point/tangent drag before a command."""
    def active_tangent_drag_for_command(self) -> bool:
        """Return whether a draw command is interrupting a tangent/control drag."""
    def drawable_should_handle_box_selection(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Draw mode owns box-like gestures itself; drawable box selection is disabled."""
    def drawable_should_start_box_selection(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Draw mode does not start generic drawable box selection."""
    def drawable_get_drag_locate(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Draw-mode MMB move setup uses drag-locate through the drawable selector."""
    def drawable_overlay_geo(self, *, processed_geo: hou.Geometry, preview_geo: hou.Geometry) -> hou.Geometry:
        """Use live draw preview geometry as overlay source while it exists."""
    def drawable_overlay_visible(self, *, interactive_drag_active: bool, processed_geo: hou.Geometry, preview_geo: hou.Geometry) -> bool:
        """Show draw overlay for live draw preview or active point movement."""
    def drawable_overlay_uses_raw_source(self, *, source_geo: hou.Geometry, preview_geo: hou.Geometry) -> bool:
        """Draw preview overlay is already cooked preview output; do not refilter it."""
    def build_draw_preview_geo(self, data: str, pick: ContinuationPick | None, prepend: bool, *, draw_symmetric: bool = True, force_corner: bool = False, force_balanced: bool = False) -> hou.Geometry | None:
        """Cook curve3core preview geometry for the pending append/prepend segment."""
    def build_draw_join_preview_geo(self, group: str, *, straighten: bool = False) -> hou.Geometry | None:
        """Cook preview geometry for the pending joinsegment action."""
    def _on_mouse_event_choose(self, kwargs: ViewerStateEventKwargs, drawable_handled: bool) -> bool:
        """Handle mouse flow while choosing where drawing should start."""
    def _on_mouse_event_segment(self, kwargs: ViewerStateEventKwargs, drawable_handled: bool) -> bool:
        """Handle mouse flow after a draw segment has been started."""
    def _pick_position(self, kwargs: ViewerStateEventKwargs, ui_event: hou.ViewerEvent) -> hou.Vector3 | None:
        """Pick the current cursor position on the active draw plane."""
    def _draw_drag_position(self, kwargs: ViewerStateEventKwargs, ui_event: hou.ViewerEvent) -> hou.Vector3 | None:
        """Return the active draw-drag position, preserving hovered targets for straight segments."""
    def finish_drawing(self, and_close: bool = False) -> bool:
        """
        Finalize draw-mode session.

        For finish+close we intentionally resolve the close target from draw-session
        continuation state (internal endpoint id), not `activeprim`, because
        `activeprim` can legitimately be -1 while still having a valid continuation
        endpoint armed in draw mode.
        """
    def _update_hover_preview(self, kwargs: ViewerStateEventKwargs, ui_event: hou.ViewerEvent) -> bool:
        """Delegate hover preview refresh to the preview pipeline."""
    def _update_choose_cursor(self, kwargs: ViewerStateEventKwargs, ui_event: hou.ViewerEvent) -> None:
        """Update the red choose cursor shown at the next anchor position."""
    def _anchor_preview_pos(self, kwargs: ViewerStateEventKwargs, ui_event: hou.ViewerEvent) -> hou.Vector3 | None:
        """Return the anchor position to visualize under the draw cursor."""
    def _hover_preview_position(self, kwargs: ViewerStateEventKwargs, ui_event: hou.ViewerEvent, label: str) -> hou.Vector3 | None:
        """Return a hover anchor position from pick-controller state."""
    def get_prompt_message(self, kwargs: ViewerStateEventKwargs | None = None) -> str: ...
    def _use_view_plane(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Return whether draw picking should use the view plane."""
    def mmb_use_view_plane(self) -> bool:
        """Return whether MMB point moves should use the view plane."""
