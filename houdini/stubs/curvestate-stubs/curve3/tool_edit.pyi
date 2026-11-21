import hou
from .handle_manager import Curve3HandleProviderBase as Curve3HandleProviderBase, HandleTarget as HandleTarget
from .move_points import PointMoveSession as PointMoveSession, apply_drag_display_context as apply_drag_display_context, restore_drag_display_context as restore_drag_display_context
from .tool_base import Curve3ToolBase as Curve3ToolBase
from .tool_helpers import anchor_point_for as anchor_point_for, anchor_ptnums_from_ptnums as anchor_ptnums_from_ptnums, build_handle_line_drag_context as build_handle_line_drag_context, build_handle_point_drag_context as build_handle_point_drag_context, is_anchor_point as is_anchor_point, is_curve_prim as is_curve_prim, point_group_string as point_group_string, preferred_start_ref_ptnum as preferred_start_ref_ptnum, remap_retracted_tangent_to_anchor as remap_retracted_tangent_to_anchor, resolve_anchor_handle_from_line as resolve_anchor_handle_from_line
from .undo_helpers import execute_with_undo as execute_with_undo
from collections.abc import Callable as Callable, Iterable, Mapping
from curvestate.curve3.controller import Curve3Controller as Curve3Controller
from curvestate.curve3.handle_manager import Curve3HandleManager as Curve3HandleManager, _HandleContext, _HandleInstanceContext
from curvestate.curve3.pick_controller import _CurvePickEvent, _HandleLinePickEvent, _HandlePointPickEvent
from houtypes import ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateKwargs

class EditHandleProvider(Curve3HandleProviderBase):
    """Edit-mode handle provider."""
    tool: Curve3EditTool
    def __init__(self, tool: Curve3EditTool) -> None:
        """Store the edit tool that supplies selection and focus state."""
    def provider_name(self) -> str:
        """Return the stable provider id used by the handle manager."""
    def is_enabled(self) -> bool:
        """Return True when the edit tool is the active Curve3 tool."""
    def build_targets(self, context: _HandleContext) -> list[HandleTarget]:
        """
        Build xform handle targets for the current edit selection.

        Returns one focused tangent target when a tangent is focused, one
        centroid target for selected anchors, or an empty list when there is
        nothing editable.
        """
    def configure_instance(self, manager: Curve3HandleManager, instance_index: int, target: HandleTarget, context: _HandleInstanceContext) -> None:
        """
        Configure one xform gadget instance for an edit target.

        The method positions the gadget at the target metadata position and
        initializes its runtime parms. It returns None and raises on invalid
        target or missing gadget state.
        """

class Curve3EditTool(Curve3ToolBase):
    drag_on_view_plane: bool
    tool_name: str
    tool_label: str
    default_optype: str | None
    hud_hints: list[dict[str, str]]
    prompt_message: str
    def __init__(self, controller: Curve3Controller) -> None:
        """Create edit-mode state, insert preview, handle provider, and drag sessions."""
    def handle_provider(self) -> EditHandleProvider:
        """Return the edit xform-handle provider for the handle manager."""
    def get_prompt_message(self, kwargs: ViewerStateEventKwargs | None = None) -> str:
        """
        Return the edit prompt for the current hover context.

        The base prompt is augmented when hovering anchors or curves. The
        return value is the full prompt string shown by the viewer state.
        """
    def on_enter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """Reset transient edit state when the tool/state becomes active."""
    def on_exit(self, kwargs: ViewerStateKwargs) -> None:
        """Clear transient edit UI state when leaving edit mode or the state."""
    def on_draw(self, kwargs: ViewerStateDrawKwargs) -> None:
        """Edit-mode draw hook; shared drawables are drawn by the manager."""
    def drawable_tangents_interactive(self) -> bool:
        """Edit mode allows direct tangent point and tangent line picking."""
    def on_edit_plane_mode_changed(self, use_view_plane: bool) -> None:
        """Use controller view-plane mode for edit drags."""
    def drawable_overlay_visible(self, *, interactive_drag_active: bool, processed_geo: hou.Geometry, preview_geo: hou.Geometry) -> bool:
        """Show the edit overlay according to the node-owned preview-curve policy."""
    def hotkey_delete_mode_action_command(self) -> str | None:
        """Delete selected points for the shared delete-mode hotkey."""
    def commit_active_drag_for_command(self, command: str, sync_fn: Callable[[], object] | None = None) -> bool:
        """Commit the edit point/tangent drag before a command."""
    def active_tangent_drag_for_command(self) -> bool:
        """Return whether an edit command is interrupting a tangent/control drag."""
    def active_tangent_drag_group_for_command(self) -> str:
        """Return anchor plus the single actively dragged tangent side."""
    def tangent_command_source_ptnums(self, tangent_ptnum: int, active_handle_ptnums: Iterable[int]) -> tuple[int, ...]:
        """Return the point-type command source for an active tangent-side drag."""
    def hud_tool_hints(self, *, hint_fn: Callable[[str, str], dict[str, str]], selection_hints: list[dict[str, str]], hotkey_refs: Mapping[str, str]) -> list[dict[str, str]]:
        """Return edit HUD hints in the established order."""
    def on_mouse_event(self, kwargs: ViewerStateEventKwargs) -> bool:
        """
        Route edit-mode mouse events through active drags, picking, and moves.

        Returns True when the event was consumed by edit behavior; False lets
        the framework continue with other handlers.
        """
    def on_pick_handle_point(self, kwargs: ViewerStateEventKwargs, handle_event: _HandlePointPickEvent) -> bool:
        """
        Handle anchor and tangent-point picks from the drawable selector.

        Returns True when the pick starts or completes edit behavior. Returning
        False allows generic point selection to continue for anchor clicks.
        """
    def on_pick_handle_line(self, kwargs: ViewerStateEventKwargs, handle_event: _HandleLinePickEvent) -> bool:
        """
        Start a tangent drag from a picked tangent line segment.

        Returns True when the line resolves to an anchor/handle pair and a drag
        session starts; otherwise returns False.
        """
    def on_pick_curve(self, kwargs: ViewerStateEventKwargs, handle_event: _CurvePickEvent) -> bool:
        """
        Handle edit-mode curve primitive picks.

        Depending on modifiers, this selects curve points, inserts points, or
        starts curve pull. Returns True when an action handled the pick.
        """
    def mmb_use_view_plane(self) -> bool:
        """Return whether middle-mouse moves should use the view plane."""
    def handle_focus_point_number(self) -> int | None:
        """Return the focused tangent point number, or None when not focused."""
    def focus_visual_anchor_ptnums(self) -> list[int]:
        """
        Return anchors to highlight while a tangent focus handle is active.

        Uses the last stable anchor selection when available, otherwise the
        current drawable selection.
        """
