from collections.abc import Callable, Mapping, Sequence
from typing import Any, Protocol, TypeAlias, TypedDict

import curveutils as cu
import hou
from houtypes import ViewerStateEventKwargs
import resourceutils as ru
from curvestate.curve3.controller import Curve3Controller

_CurvePick: TypeAlias = cu.PickCurveResultType | tuple[hou.Prim, float, hou.Vector3 | None, int]
_DrawableSelection: TypeAlias = Mapping[str, Mapping[str, list[int]]]

# The handle_event dicts dispatch_pick_event() passes to a tool's on_pick_* method.
class _HandlePointPickEvent(TypedDict):
    result: hou.Point
    internal_ptnum: int | None

class _HandleLinePickEvent(TypedDict):
    result: cu.PickHandleLineResultType

class _CurvePickEvent(TypedDict):
    result: cu.PickCurveResultType

_PickEvent: TypeAlias = _HandlePointPickEvent | _HandleLinePickEvent | _CurvePickEvent

class _SetLocateFromDrawableSelectionFn(Protocol):
    def __call__(
        self,
        drawable_selection: _DrawableSelection,
        /,
        source_drawables: Sequence[hou.GeometryDrawable] | None = ...,
    ) -> object: ...

class PickController:
    controller: Curve3Controller
    def __init__(self, controller: Curve3Controller) -> None: ...
    def peek_hover_pick(self) -> cu.PickCurveResultType | None: ...
    def get_hover_pick(self, *, log_label: str | None = ...) -> cu.PickCurveResultType | None: ...
    def set_hover_pick(self, pick: cu.PickCurveResultType | None, *, log_label: str | None = ...) -> None: ...
    def clear_hover_pick(self, *, log_label: str | None = ...) -> None: ...
    def peek_hover_point(self) -> hou.Point | None: ...
    def peek_hover_point_kind(self) -> str | None: ...
    def set_hover_point(self, point: hou.Point | None, *, kind: str | None = ...) -> None: ...
    def clear_hover_point(self) -> None: ...
    def resolve_curve_pick(
        self,
        *,
        elem_tuple: int,
        ray_orig: hou.Vector3,
        ray_dir: hou.Vector3,
        drawable: hou.GeometryDrawable,
        curve_u_attrib_fn: Callable[[hou.Vertex], float],
        log_label: str,
    ) -> cu.PickCurveResultType | None: ...
    def resolve_handle_point_pick(
        self,
        *,
        drawable: hou.GeometryDrawable,
        elem_tuple: ru.SinglePickTuple,
        context: str = ...,
    ) -> tuple[hou.Point, int | None] | None: ...
    def resolve_handle_line_pick(
        self,
        *,
        drawable: hou.GeometryDrawable,
        elem_tuple: ru.SinglePickTuple,
        ray_orig: hou.Vector3,
        ray_dir: hou.Vector3,
    ) -> cu.PickHandleLineResultType | None: ...
    def resolve_handle_pick_event(
        self,
        *,
        drawable: hou.GeometryDrawable,
        elem_tuple: ru.SinglePickTuple,
        ui_event: hou.ViewerEvent,
        point_drawables: Sequence[hou.GeometryDrawable],
        line_drawables: Sequence[hou.GeometryDrawable],
    ) -> tuple[str, _HandlePointPickEvent | _HandleLinePickEvent] | None: ...
    def external_pick_payload(
        self,
        *,
        drawable: hou.GeometryDrawable,
        elem_tuple: ru.SinglePickTuple,
        ui_event: hou.ViewerEvent,
        point_drawables: Sequence[hou.GeometryDrawable],
        line_drawables: Sequence[hou.GeometryDrawable],
    ) -> dict[str, hou.Vector3 | str] | None: ...
    def update_locate_line_from_result(
        self,
        *,
        drawable: hou.GeometryDrawable,
        elem_tuple: ru.SinglePickTuple,
        clear_locate_drawables: Callable[[], object],
        locate_line_drawable: hou.GeometryDrawable,
    ) -> bool: ...
    def dispatch_pick_event(self, method_name: str, kwargs: ViewerStateEventKwargs, handle_event: _PickEvent) -> bool | None: ...
    def handle_single_handle_pick(
        self,
        *,
        kwargs: ViewerStateEventKwargs,
        drawable: hou.GeometryDrawable,
        elem_tuple: ru.SinglePickTuple,
        ui_event: hou.ViewerEvent,
        point_drawables: Sequence[hou.GeometryDrawable],
        line_drawables: Sequence[hou.GeometryDrawable],
    ) -> bool: ...
    def handle_single_selection_pick(
        self,
        *,
        kwargs: ViewerStateEventKwargs,
        drawable: hou.GeometryDrawable,
        elem_tuple: ru.SinglePickTuple,
        ui_event: hou.ViewerEvent,
        modifier: hou.EnumValue[hou.pickModifier],
        anchor_drawables: tuple[hou.GeometryDrawable, ...],
        handle_point_drawables: tuple[hou.GeometryDrawable, ...],
        handle_line_drawables: tuple[hou.GeometryDrawable, ...],
        curve_drawable: hou.GeometryDrawable,
        curve_u_attrib_fn: Callable[[hou.Vertex], float],
    ) -> bool: ...
    def handle_locate_single_selection(
        self,
        *,
        kwargs: ViewerStateEventKwargs,
        result: ru.SingleSelectResult,
        drawable: hou.GeometryDrawable,
        drawable_selection: _DrawableSelection,
        anchor_drawables: tuple[hou.GeometryDrawable, ...],
        handle_point_drawables: tuple[hou.GeometryDrawable, ...],
        handle_line_drawables: tuple[hou.GeometryDrawable, ...],
        curve_drawable: hou.GeometryDrawable,
        set_locate_from_drawable_selection: _SetLocateFromDrawableSelectionFn,
        set_locate_line_from_result: Callable[[hou.GeometryDrawable, ru.SinglePickTuple], object],
        set_locate_curve_from_pick: Callable[[cu.PickCurveResultType | None], object],
        clear_locate_drawables: Callable[[], object],
        curve_u_attrib_fn: Callable[[hou.Vertex], float],
    ) -> bool: ...
    def is_stale_pick(self, pick: _CurvePick | None) -> bool: ...
    def resolve_segment_anchor_ptnums(self, pick: _CurvePick | None) -> list[int]: ...
    def resolve_curve_point_ptnums(self, pick: _CurvePick | None) -> list[int]: ...
    def resolve_append_parms(self, pick: _CurvePick | None) -> dict[str, int]: ...
    def resolve_insert_parms(self, pick: _CurvePick | None) -> dict[str, int | float]: ...
