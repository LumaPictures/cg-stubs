from collections.abc import Callable, Sequence
from typing import Protocol

import hou
from curvestate.curve3.adapters import ViewerAdapter
from curvestate.curve3.controller import Curve3Controller

class _DraggerFlagFn(Protocol):
    def __call__(self, ui_event: hou.ViewerEvent, /, is_anchor: bool) -> int | None: ...

def apply_drag_display_context(
    controller: Curve3Controller,
    *,
    group: str,
    optype: str,
    active_handle_ptnums: Sequence[int] | None = ...,
    visual_selection_override: Sequence[int] | None = ...,
) -> None: ...
def restore_drag_display_context(
    controller: Curve3Controller,
    *,
    restore_group: str | None,
    restore_active_handle_ptnums: Sequence[int] | None = ...,
) -> None: ...

class PointMoveSession:
    controller: Curve3Controller
    adapter: ViewerAdapter
    undo_label: str
    def __init__(
        self,
        controller: Curve3Controller,
        adapter: ViewerAdapter,
        dragger_name: str,
        undo_label: str,
        dragger_flag_fn: _DraggerFlagFn,
    ) -> None: ...
    @property
    def active(self) -> bool: ...
    @property
    def is_anchor_drag(self) -> bool: ...
    def active_tangent_drag(self) -> bool: ...
    def get_active_handle_ptnums(self) -> list[int]: ...
    def begin(
        self,
        ui_event: hou.ViewerEvent,
        selected_ptnums: Sequence[int],
        restore_group: str,
        start_ref_ptnum: int | None = ...,
        *,
        active_handle_ptnums: Sequence[int] | None = ...,
        visual_selection_override: Sequence[int] | None = ...,
        undo_label: str | None = ...,
        drag_center_pos: hou.Vector3 | None = ...,
        lock_length: bool = ...,
        guide_mode: str = ...,
        anchor_pos: hou.Vector3 | None = ...,
        start_pos_override: hou.Vector3 | None = ...,
        is_anchor_drag: bool = ...,
        use_view_plane: bool = ...,
    ) -> None: ...
    def on_mouse_event(self, ui_event: hou.ViewerEvent) -> bool: ...
    def commit_for_command(self, sync_fn: Callable[[], object] | None = ...) -> bool: ...
    def resume_pending_restart(self, ui_event: hou.ViewerEvent) -> bool: ...
    def end(self, *, clear_pending_restart: bool = ...) -> None: ...
    def _start_position_from_selection(
        self, selected_ptnums: Sequence[int], preferred_ptnum: int | None = ...
    ) -> hou.Vector3 | None: ...
