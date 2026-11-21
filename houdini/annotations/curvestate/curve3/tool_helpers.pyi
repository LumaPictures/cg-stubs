from collections.abc import Callable, Iterable, Sequence
from typing import TypedDict, overload

import hou
from curvestate.curve3.controller import Curve3Controller


class _HandlePointDragContext(TypedDict):
    anchor: hou.Point | None
    is_anchor_drag: bool
    drag_selection: list[int]
    visual_override: list[int]
    active_handles: list[int]


class _HandleLineDragContext(TypedDict):
    drag_selection: list[int]
    visual_override: list[int]
    active_handles: list[int]
    is_anchor_drag: bool


def should_commit_draw_event(reason: hou.EnumValue[hou.uiEventReason], drag_active: bool) -> bool: ...
def node_handle_is_alive(node: hou.Node | None, expected_path: str | None = ...) -> bool: ...
def format_pos3_string(pos: hou.Vector3) -> str: ...
def format_pos3_list_string(points: Iterable[hou.Vector3]) -> str: ...
def point_group_string(ptnums: Iterable[int]) -> str: ...
def is_curve_prim(prim: hou.Prim | None) -> bool: ...
def draw_points_required(
    primtype_token: str,
    newpointtype_token: str,
    continuing_from_curve: bool,
    nurbs_order: int,
    bezier_order: int,
) -> int: ...
def is_anchor_point(point: hou.Point | None) -> bool: ...
def anchor_point_for(point: hou.Point | None) -> hou.Point | None: ...
@overload
def remap_retracted_tangent_to_anchor(point: hou.Point, *, epsilon: float = ...) -> hou.Point: ...
@overload
def remap_retracted_tangent_to_anchor(point: None, *, epsilon: float = ...) -> None: ...
def remap_retracted_tangent_to_anchor(
    point: hou.Point | None,
    *,
    epsilon: float = ...,
) -> hou.Point | None: ...
@overload
def point_internal_ptnum(point: hou.Point) -> int: ...
@overload
def point_internal_ptnum(point: None) -> None: ...
def point_internal_ptnum(point: hou.Point | None) -> int | None: ...
def preferred_start_ref_ptnum(
    selected_ptnums: Iterable[int], picked_ptnums: Iterable[int]
) -> int | None: ...
def resolve_anchor_handle_from_line(
    p0: hou.Point, p1: hou.Point
) -> tuple[hou.Point | None, hou.Point | None]: ...
def build_handle_point_drag_context(
    *,
    dragged_point: hou.Point,
    selected_ptnums: Sequence[int] | None,
    anchor_ptnums_from_ptnums_fn: Callable[[list[int]], Iterable[int]],
    include_selected_anchor_drag: bool = ...,
) -> _HandlePointDragContext: ...
def build_handle_line_drag_context(
    *,
    anchor: hou.Point | None,
    handle: hou.Point | None,
    selected_ptnums: Sequence[int] | None,
    anchor_ptnums_from_ptnums_fn: Callable[[list[int]], Iterable[int]],
) -> _HandleLineDragContext: ...
def anchor_ptnums_from_ptnums(controller: Curve3Controller, ptnums: Iterable[int]) -> list[int]: ...
