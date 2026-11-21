# Houdini stubs generated from Houdini 22.0.466

import hou
from .pick import pick_on_plane as pick_on_plane
from .tool_helpers import point_group_string as point_group_string
from .undo_helpers import execute_with_undo as execute_with_undo
from collections.abc import Callable as Callable, Sequence
from curvestate.curve3.adapters import ViewerAdapter as ViewerAdapter
from curvestate.curve3.controller import Curve3Controller as Curve3Controller
from typing import Protocol

class _DraggerFlagFn(Protocol):
    def __call__(self, ui_event: hou.ViewerEvent, /, is_anchor: bool) -> int | None: ...

def apply_drag_display_context(controller: Curve3Controller, *, group: str, optype: str, active_handle_ptnums: Sequence[int] | None = None, visual_selection_override: Sequence[int] | None = None) -> None:
    """Shared drag display/context setup used by point and handle drags."""
def restore_drag_display_context(controller: Curve3Controller, *, restore_group: str | None, restore_active_handle_ptnums: Sequence[int] | None = None) -> None:
    """Shared drag display/context restore for point and handle drags."""

class PointMoveSession:
    """
    Shared middle-mouse move flow for selected points.

    This class owns drag preview + grouped commit behavior so tools can reuse
    identical move semantics without duplicating drag state logic.
    """
    controller: Curve3Controller
    adapter: ViewerAdapter
    undo_label: str
    def __init__(self, controller: Curve3Controller, adapter: ViewerAdapter, dragger_name: str, undo_label: str, dragger_flag_fn: _DraggerFlagFn) -> None: ...
    @property
    def active(self) -> bool: ...
    @property
    def is_anchor_drag(self) -> bool: ...
    def active_tangent_drag(self) -> bool:
        """Return True when an active drag is moving tangent/control points."""
    def get_active_handle_ptnums(self) -> list[int]: ...
    def begin(self, ui_event: hou.ViewerEvent, selected_ptnums: Sequence[int], restore_group: str, start_ref_ptnum: int | None = None, *, active_handle_ptnums: Sequence[int] | None = None, visual_selection_override: Sequence[int] | None = None, undo_label: str | None = None, drag_center_pos: hou.Vector3 | None = None, lock_length: bool = False, guide_mode: str = 'point', anchor_pos: hou.Vector3 | None = None, start_pos_override: hou.Vector3 | None = None, is_anchor_drag: bool = False, use_view_plane: bool = False) -> None: ...
    def on_mouse_event(self, ui_event: hou.ViewerEvent) -> bool: ...
    def commit_for_command(self, sync_fn: Callable[[], object] | None = None) -> bool:
        """Commit the active drag before a command and resume on the next mouse event."""
    def resume_pending_restart(self, ui_event: hou.ViewerEvent) -> bool:
        """Start the pending command-interrupted drag using the next mouse event."""
    def end(self, *, clear_pending_restart: bool = True) -> None: ...
    def _start_position_from_selection(self, selected_ptnums: Sequence[int], preferred_ptnum: int | None = None) -> hou.Vector3 | None: ...
