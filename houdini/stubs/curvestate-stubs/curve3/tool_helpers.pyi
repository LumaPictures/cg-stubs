import hou
import typing
from collections.abc import Callable as Callable, Iterable, Sequence
from curvestate.curve3.controller import Curve3Controller as Curve3Controller
from typing import TypedDict

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

def should_commit_draw_event(reason: hou.EnumValue[hou.uiEventReason], drag_active: bool) -> bool:
    """Return True when a draw gesture should commit to the SOP."""
def node_handle_is_alive(node: hou.Node | None, expected_path: str | None = None) -> bool:
    """Return whether a Houdini node handle still resolves to a live node."""
def format_pos3_string(pos: hou.Vector3) -> str:
    """Format a position for the SOP `data` parm."""
def format_pos3_list_string(points: Iterable[hou.Vector3]) -> str:
    """Format positions for the SOP `data` parm as space-separated pos tuples."""
def point_group_string(ptnums: Iterable[int]) -> str:
    """Return a stable sorted Houdini point-group string for point numbers."""
def is_curve_prim(prim: hou.Prim | None) -> bool:
    """Return True if the primitive is a supported curve primitive type."""
def draw_points_required(primtype_token: str, newpointtype_token: str, continuing_from_curve: bool, nurbs_order: int, bezier_order: int) -> int:
    """
    Return how many draw points are needed before committing one segment.

    This matches the intended Curve 2-style flow: no commit until a segment
    definition is complete, with bezier thresholds dependent on new anchor type.
    """
def is_anchor_point(point: hou.Point | None) -> bool:
    """Return True if the point is an anchor (non-handle) bezier point."""
def anchor_point_for(point: hou.Point | None) -> hou.Point | None:
    """Return owning bezier anchor for a point, or None if not available."""
@typing.overload
def remap_retracted_tangent_to_anchor(point: hou.Point, *, epsilon: float = ...) -> hou.Point: ...
@typing.overload
def remap_retracted_tangent_to_anchor(point: None, *, epsilon: float = ...) -> None: ...
@typing.overload
def point_internal_ptnum(point: hou.Point) -> int: ...
@typing.overload
def point_internal_ptnum(point: None) -> None: ...
def preferred_start_ref_ptnum(selected_ptnums: Iterable[int], picked_ptnums: Iterable[int]) -> int | None:
    """Pick the first picked point that is in the current selection."""
def resolve_anchor_handle_from_line(p0: hou.Point, p1: hou.Point) -> tuple[hou.Point | None, hou.Point | None]:
    """Resolve (anchor, handle) from a picked tangent segment endpoints."""
def build_handle_point_drag_context(*, dragged_point: hou.Point, selected_ptnums: Sequence[int] | None, anchor_ptnums_from_ptnums_fn: Callable[[list[int]], Iterable[int]], include_selected_anchor_drag: bool = True) -> _HandlePointDragContext:
    '''
    Build shared drag context for handle-point drags.

    Returns:
      {
        "anchor": hou.Point|None,
        "is_anchor_drag": bool,
        "drag_selection": list[int],
        "visual_override": list[int],
        "active_handles": list[int],
      }
    '''
def build_handle_line_drag_context(*, anchor: hou.Point | None, handle: hou.Point | None, selected_ptnums: Sequence[int] | None, anchor_ptnums_from_ptnums_fn: Callable[[list[int]], Iterable[int]]) -> _HandleLineDragContext:
    """Build shared drag context for handle-line drags."""
def anchor_ptnums_from_ptnums(controller: Curve3Controller, ptnums: Iterable[int]) -> list[int]:
    """Resolve anchor point numbers for arbitrary selected points."""
