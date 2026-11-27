from collections.abc import Callable, Container, Iterable, Mapping, Sequence
from typing import NotRequired, Protocol, TypeAlias, TypedDict

import curveutils as cu
from apex import xformgadget as xg
import hou
from houtypes import ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateKwargs
import resourceutils as ru
import viewerstate.utils as su
from curvestate.curve3.controller import Curve3Controller
from curvestate.curve3.referencegeo import Curve3ReferenceGeo, _PseudoHandle
from curvestate.curve3.tool_base import Curve3ToolBase

_Color: TypeAlias = hou.Color | hou.Vector4 | Sequence[float]
_DrawableSelection: TypeAlias = Mapping[str, Mapping[str, list[int]]]
_ParmStringProvider: TypeAlias = Callable[[str], str | None]
# A drawable's summary for the debug.get.drawables command; the counts are there when it has geometry.
class _DrawableInfo(TypedDict):
    name: str
    class_index: int
    drawable_index: int
    type: str
    exists: bool
    pointcount: NotRequired[int]
    primitivecount: NotRequired[int]

class _ClearHoverPickFn(Protocol):
    def __call__(self, *, log_label: str) -> object: ...

class _SetLocateFromDrawableSelectionFn(Protocol):
    def __call__(
        self,
        drawable_selection: _DrawableSelection,
        /,
        source_drawables: Sequence[hou.GeometryDrawable] | None = ...,
    ) -> object: ...

class _HandleLocateSingleSelectionFn(Protocol):
    def __call__(
        self,
        *,
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

class _HandleSingleSelectionPickFn(Protocol):
    def __call__(
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

def _merge_drawable_geometry(output_geo: hou.Geometry, drawable: hou.GeometryDrawable) -> None: ...

class GenericDrawableSelector(ru.DrawableSelector):
    owner: DrawableSelectorComponent
    def __init__(self, scene_viewer: hou.SceneViewer, owner: DrawableSelectorComponent) -> None: ...
    def onLocateSingleSelection(self, kwargs: ViewerStateEventKwargs, result: ru.SingleSelectResult) -> bool: ...
    def onSingleSelection(self, kwargs: ViewerStateEventKwargs, result: ru.SingleSelectResult) -> bool: ...
    def onBoxSelection(self, kwargs: ViewerStateEventKwargs, result: ru.BoxSelectResult) -> bool: ...
    def onLocateBoxSelection(self, kwargs: ViewerStateEventKwargs, result: ru.BoxSelectResult) -> bool: ...
    def canStartBoxSelection(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def getDragLocate(self, kwargs: ViewerStateEventKwargs) -> bool: ...

class GenericDrawableSelectorColors(su.DrawableSelectorColors):
    drawable_selector: ru.DrawableSelector
    def __init__(self, scene_viewer: hou.SceneViewer, drawable_selector: ru.DrawableSelector) -> None: ...
    def _modifierColorKey(self, drawable_typename: str) -> str: ...

class DrawableSelectorComponent:
    scene_viewer: hou.SceneViewer
    drawable_classes_provider: Callable[[], list[list[hou.GeometryDrawable]]]
    on_locate_single_selection: Callable[[ViewerStateEventKwargs, ru.SingleSelectResult], bool]
    on_single_selection: Callable[[ViewerStateEventKwargs, ru.SingleSelectResult], bool]
    on_box_selection: Callable[[ViewerStateEventKwargs, ru.BoxSelectResult], bool]
    on_locate_box_selection: Callable[[ViewerStateEventKwargs, ru.BoxSelectResult], bool]
    can_start_box_selection_fn: Callable[[ViewerStateEventKwargs, Callable[[ViewerStateEventKwargs], bool]], bool] | None
    drag_locate_fn: Callable[[ViewerStateEventKwargs], bool] | None
    selector: GenericDrawableSelector
    selector_colors: GenericDrawableSelectorColors
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        *,
        drawable_classes_provider: Callable[[], list[list[hou.GeometryDrawable]]],
        on_locate_single_selection: Callable[[ViewerStateEventKwargs, ru.SingleSelectResult], bool],
        on_single_selection: Callable[[ViewerStateEventKwargs, ru.SingleSelectResult], bool],
        on_box_selection: Callable[[ViewerStateEventKwargs, ru.BoxSelectResult], bool],
        on_locate_box_selection: Callable[[ViewerStateEventKwargs, ru.BoxSelectResult], bool],
        can_start_box_selection_fn: Callable[[ViewerStateEventKwargs, Callable[[ViewerStateEventKwargs], bool]], bool] | None = ...,
        drag_locate_fn: Callable[[ViewerStateEventKwargs], bool] | None = ...,
    ) -> None: ...
    def refresh_drawable_classes(self) -> None: ...
    def set_use_handle_pick_radius(self, on: bool) -> None: ...

def internal_ptnums_from_drawable_selection(
    drawable_selection: _DrawableSelection,
    source_drawables: Iterable[hou.GeometryDrawable],
) -> list[int]: ...
def indices_from_internal_ptnums(
    source_drawable: hou.GeometryDrawable,
    ptnums: Container[int],
) -> list[int]: ...
def set_index_locate_drawable(
    locate_drawable: hou.GeometryDrawable,
    source_geo: hou.Geometry,
    indices: Sequence[int],
) -> None: ...
def set_locate_from_drawable_selection(
    *,
    drawable_selection: _DrawableSelection,
    locate_specs: Iterable[tuple[hou.GeometryDrawable, hou.GeometryDrawable]],
    clear_locate_drawables_fn: Callable[[], object],
    update_locate_color_fn: Callable[[], object],
    source_drawables: Iterable[hou.GeometryDrawable] | None = ...,
    log_label: str | None = ...,
) -> tuple[bool, list[str]]: ...
def ptnums_from_single_selection_result(
    selector: ru.DrawableSelector,
    result: ru.SingleSelectResult,
    source_drawables: Iterable[hou.GeometryDrawable],
) -> list[int]: ...
def ptnums_from_box_selection_result(
    selector: ru.DrawableSelector,
    result: ru.BoxSelectResult,
    source_drawables: Iterable[hou.GeometryDrawable],
) -> list[int]: ...
def handle_locate_single_selection(
    *,
    selector: ru.DrawableSelector,
    kwargs: ViewerStateEventKwargs,
    result: ru.SingleSelectResult,
    get_drawable_fn: Callable[[int, int], hou.SimpleDrawable | hou.AdvancedDrawable],
    clear_hover_pick_fn: _ClearHoverPickFn,
    clear_locate_drawables_fn: Callable[[], object],
    handle_locate_single_selection_fn: _HandleLocateSingleSelectionFn,
    anchor_drawables: tuple[hou.GeometryDrawable, ...],
    handle_point_drawables: tuple[hou.GeometryDrawable, ...],
    handle_line_drawables: tuple[hou.GeometryDrawable, ...],
    curve_drawable: hou.GeometryDrawable,
    set_locate_from_drawable_selection_fn: _SetLocateFromDrawableSelectionFn,
    set_locate_line_from_result_fn: Callable[[hou.GeometryDrawable, ru.SinglePickTuple], object],
    set_locate_curve_from_pick_fn: Callable[[cu.PickCurveResultType | None], object],
    curve_u_attrib_fn: Callable[[hou.Vertex], float],
) -> bool: ...
def handle_single_selection(
    *,
    selector: ru.DrawableSelector,
    kwargs: ViewerStateEventKwargs,
    result: ru.SingleSelectResult,
    tool_policy: Curve3ToolBase,
    log_label: str,
    current_group_string: str,
    current_optype_string: str,
    get_drawable_fn: Callable[[int, int], hou.SimpleDrawable | hou.AdvancedDrawable],
    ptnums_from_single_fn: Callable[[ru.SingleSelectResult], list[int]],
    apply_selection_fn: Callable[[list[int], hou.EnumValue[hou.pickModifier]], object],
    handle_single_selection_pick_fn: _HandleSingleSelectionPickFn,
    anchor_drawables: tuple[hou.GeometryDrawable, ...],
    handle_point_drawables: tuple[hou.GeometryDrawable, ...],
    handle_line_drawables: tuple[hou.GeometryDrawable, ...],
    curve_drawable: hou.GeometryDrawable,
    curve_u_attrib_fn: Callable[[hou.Vertex], float],
    set_last_single_pick_ptnums_fn: Callable[[list[int]], object],
) -> bool: ...
def handle_locate_box_selection(
    *,
    selector: ru.DrawableSelector,
    result: ru.BoxSelectResult,
    clear_locate_drawables_fn: Callable[[], object],
    set_locate_from_drawable_selection_fn: _SetLocateFromDrawableSelectionFn,
    source_drawables: Sequence[hou.GeometryDrawable],
) -> bool: ...
def handle_box_selection(
    *,
    selector: ru.DrawableSelector,
    kwargs: ViewerStateEventKwargs,
    result: ru.BoxSelectResult,
    tool_policy: Curve3ToolBase,
    ptnums_from_box_fn: Callable[[ru.BoxSelectResult], list[int]],
    apply_selection_fn: Callable[[list[int], hou.EnumValue[hou.pickModifier]], object],
) -> bool: ...

class Curve3DrawableGeometrySource:
    color_options: ru.ColorOptions
    reference_geo: Curve3ReferenceGeo
    def __init__(
        self,
        *,
        color_options: ru.ColorOptions,
        reference_geo: Curve3ReferenceGeo | None = ...,
    ) -> None: ...
    def bind_live_providers(
        self,
        geometry_provider: Callable[[], hou.Geometry | None],
        parm_string_provider: _ParmStringProvider,
    ) -> None: ...
    def set_curve_geometry(
        self,
        source_geo: hou.Geometry,
        *,
        parm_string_provider: _ParmStringProvider | None = ...,
    ) -> None: ...
    def configure_orient_guide(
        self,
        *,
        build: bool,
        show_x: bool = ...,
        show_y: bool = ...,
        show_z: bool = ...,
        guide_scale: float = ...,
    ) -> None: ...

def _build_component_processed_source(
    *,
    scene_viewer: hou.SceneViewer,
    color_options: ru.ColorOptions,
    source_geo: hou.Geometry | None,
    parm_string_provider: _ParmStringProvider | None = ...,
    configure_source_fn: Callable[[Curve3DrawableGeometrySource], object] | None = ...,
) -> Curve3DrawableGeometrySource: ...
def _set_locate_point_drawable_params(
    drawable: hou.GeometryDrawable,
    *,
    color: _Color,
    radius: float,
    style: hou.EnumValue[hou.drawableGeometryPointStyle],
) -> None: ...

class Curve3AnchorPointDrawables:
    scene_viewer: hou.SceneViewer
    color_options: ru.ColorOptions
    point_broken_drawable: hou.GeometryDrawable
    point_smooth_drawable: hou.GeometryDrawable
    point_balanced_drawable: hou.GeometryDrawable
    point_auto_drawable: hou.GeometryDrawable
    point_auto_ring_drawable: hou.GeometryDrawable
    point_ends_broken_drawable: hou.GeometryDrawable
    point_ends_smooth_drawable: hou.GeometryDrawable
    point_ends_balanced_drawable: hou.GeometryDrawable
    point_ends_auto_drawable: hou.GeometryDrawable
    point_ends_auto_ring_drawable: hou.GeometryDrawable
    locate_broken_point_drawable: hou.GeometryDrawable
    locate_smooth_point_drawable: hou.GeometryDrawable
    locate_balanced_point_drawable: hou.GeometryDrawable
    locate_auto_point_drawable: hou.GeometryDrawable
    locate_ends_broken_point_drawable: hou.GeometryDrawable
    locate_ends_smooth_point_drawable: hou.GeometryDrawable
    locate_ends_balanced_point_drawable: hou.GeometryDrawable
    locate_ends_auto_point_drawable: hou.GeometryDrawable
    def __init__(self, scene_viewer: hou.SceneViewer, color_options: ru.ColorOptions) -> None: ...
    def set_locate_color(self, color: _Color) -> None: ...
    def clear_locate_drawables(self) -> None: ...
    def draw_locate_drawables(self, draw_handle: int) -> None: ...
    def show(self, on: bool) -> None: ...
    def draw(self, draw_handle: int) -> None: ...
    def savePlaybackOutputGeometry(self, geo: hou.Geometry) -> None: ...
    def update_from_processed_source(
        self,
        processed_source: Curve3DrawableGeometrySource | Curve3ReferenceGeo,
    ) -> None: ...
    def update_from_curve_geometry(
        self,
        source_geo: hou.Geometry,
        *,
        processed_source: Curve3DrawableGeometrySource | None = ...,
        parm_string_provider: _ParmStringProvider | None = ...,
    ) -> Curve3DrawableGeometrySource: ...

class Curve3TangentLineDrawables:
    scene_viewer: hou.SceneViewer
    color_options: ru.ColorOptions
    handle_lines_tied_drawable: hou.GeometryDrawable
    handle_lines_broken_drawable: hou.GeometryDrawable
    handle_lines_auto_drawable: hou.GeometryDrawable
    def __init__(self, scene_viewer: hou.SceneViewer, color_options: ru.ColorOptions) -> None: ...
    def set_interactive(self, enabled: bool) -> None: ...
    def show(self, on: bool) -> None: ...
    def draw(self, draw_handle: int) -> None: ...
    def savePlaybackOutputGeometry(self, geo: hou.Geometry) -> None: ...
    def update_from_processed_source(
        self,
        processed_source: Curve3DrawableGeometrySource | Curve3ReferenceGeo,
    ) -> None: ...
    def update_from_curve_geometry(
        self,
        source_geo: hou.Geometry,
        *,
        processed_source: Curve3DrawableGeometrySource | None = ...,
        parm_string_provider: _ParmStringProvider | None = ...,
    ) -> Curve3DrawableGeometrySource: ...

class Curve3TangentPointDrawables:
    scene_viewer: hou.SceneViewer
    color_options: ru.ColorOptions
    handle_points_tied_drawable: hou.GeometryDrawable
    handle_points_broken_drawable: hou.GeometryDrawable
    handle_points_auto_drawable: hou.GeometryDrawable
    locate_handle_points_tied_drawable: hou.GeometryDrawable
    locate_handle_points_broken_drawable: hou.GeometryDrawable
    locate_handle_points_auto_drawable: hou.GeometryDrawable
    def __init__(self, scene_viewer: hou.SceneViewer, color_options: ru.ColorOptions) -> None: ...
    def set_interactive(self, enabled: bool) -> None: ...
    def set_locate_color(self, color: _Color) -> None: ...
    def clear_locate_drawables(self) -> None: ...
    def draw_locate_drawables(self, draw_handle: int) -> None: ...
    def show(self, on: bool) -> None: ...
    def draw(self, draw_handle: int) -> None: ...
    def savePlaybackOutputGeometry(self, geo: hou.Geometry) -> None: ...
    def update_from_processed_source(
        self,
        processed_source: Curve3DrawableGeometrySource | Curve3ReferenceGeo,
    ) -> None: ...
    def update_from_curve_geometry(
        self,
        source_geo: hou.Geometry,
        *,
        processed_source: Curve3DrawableGeometrySource | None = ...,
        parm_string_provider: _ParmStringProvider | None = ...,
    ) -> Curve3DrawableGeometrySource: ...

class Curve3PreviewCurveDrawable:
    scene_viewer: hou.SceneViewer
    color_options: ru.ColorOptions
    drawable: hou.GeometryDrawable
    def __init__(self, scene_viewer: hou.SceneViewer, color_options: ru.ColorOptions, *, name: str = ...) -> None: ...
    def show(self, on: bool) -> None: ...
    def draw(self, draw_handle: int) -> None: ...
    def drawables_info(self, *, class_index: int) -> list[_DrawableInfo]: ...
    def savePlaybackOutputGeometry(self, geo: hou.Geometry) -> None: ...
    def update_from_processed_source(
        self,
        processed_source: Curve3DrawableGeometrySource | Curve3ReferenceGeo,
    ) -> None: ...
    def update_from_curve_geometry(
        self,
        source_geo: hou.Geometry,
        *,
        processed_source: Curve3DrawableGeometrySource | None = ...,
        parm_string_provider: _ParmStringProvider | None = ...,
    ) -> Curve3DrawableGeometrySource: ...

class Curve3SinglePointPreviewDrawable:
    scene_viewer: hou.SceneViewer
    drawable: hou.GeometryDrawable
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        *,
        name: str,
        color: _Color,
        radius: float,
        style: hou.EnumValue[hou.drawableGeometryPointStyle] = ...,
    ) -> None: ...
    def set_points(self, points: Sequence[hou.Vector3]) -> None: ...
    def set_position(self, pos: hou.Vector3) -> None: ...
    def set_style(self, style: hou.EnumValue[hou.drawableGeometryPointStyle]) -> None: ...
    def clear(self) -> None: ...
    def draw(self, draw_handle: int) -> None: ...
    def savePlaybackOutputGeometry(self, geo: hou.Geometry) -> None: ...

class Curve3InsertPreviewDrawable(Curve3SinglePointPreviewDrawable):
    color_options: ru.ColorOptions
    def __init__(self, scene_viewer: hou.SceneViewer, color_options: ru.ColorOptions) -> None: ...

class Curve3OrientGuideDrawable:
    scene_viewer: hou.SceneViewer
    color_options: ru.ColorOptions
    drawable: hou.GeometryDrawable
    def __init__(self, scene_viewer: hou.SceneViewer, color_options: ru.ColorOptions, *, name: str = ...) -> None: ...
    def show(self, on: bool) -> None: ...
    def draw(self, draw_handle: int) -> None: ...
    def savePlaybackOutputGeometry(self, geo: hou.Geometry) -> None: ...
    def configure_processed_source(
        self,
        processed_source: Curve3DrawableGeometrySource,
        *,
        build: bool,
        show_x: bool = ...,
        show_y: bool = ...,
        show_z: bool = ...,
        guide_scale: float = ...,
    ) -> None: ...
    def update_from_processed_source(
        self,
        processed_source: Curve3DrawableGeometrySource | Curve3ReferenceGeo,
    ) -> None: ...
    def update_from_curve_geometry(
        self,
        source_geo: hou.Geometry,
        *,
        processed_source: Curve3DrawableGeometrySource | None = ...,
        parm_string_provider: _ParmStringProvider | None = ...,
        build: bool = ...,
        show_x: bool = ...,
        show_y: bool = ...,
        show_z: bool = ...,
        guide_scale: float = ...,
    ) -> Curve3DrawableGeometrySource: ...

class Curve3AnchorTangentDrawables:
    anchors: Curve3AnchorPointDrawables
    tangent_lines: Curve3TangentLineDrawables
    tangent_points: Curve3TangentPointDrawables
    def show(self, on: bool) -> None: ...
    def set_tangents_interactive(self, enabled: bool) -> None: ...
    def draw_tangents(self, draw_handle: int) -> None: ...
    def draw_tangent_locate_drawables(self, draw_handle: int) -> None: ...
    def draw_points(self, draw_handle: int) -> None: ...
    def draw_point_locate_drawables(self, draw_handle: int) -> None: ...
    def draw(self, draw_handle: int) -> None: ...
    def clear_locate_drawables(self) -> None: ...
    def set_locate_color(self, color: _Color) -> None: ...
    def draw_locate_drawables(self, draw_handle: int) -> None: ...
    def savePlaybackOutputGeometry(self, geo: hou.Geometry) -> None: ...
    def anchor_ptnums_from_drawable_selection(self, drawable_selection: _DrawableSelection) -> list[int]: ...
    def drawables_info(
        self,
        *,
        tangents_interactive: bool,
        point_class_index: int,
        line_class_index: int,
    ) -> list[_DrawableInfo]: ...
    def update_from_processed_source(
        self,
        processed_source: Curve3DrawableGeometrySource | Curve3ReferenceGeo,
    ) -> None: ...
    def update_from_curve_geometry(
        self,
        source_geo: hou.Geometry,
        *,
        processed_source: Curve3DrawableGeometrySource | None = ...,
        parm_string_provider: _ParmStringProvider | None = ...,
    ) -> Curve3DrawableGeometrySource: ...

class Curve3DrawableManager:
    DRAWABLE_CLASS_POINTS: int
    DRAWABLE_CLASS_CURVES: int
    scene_viewer: hou.SceneViewer
    controller: Curve3Controller
    color_options: ru.ColorOptions
    reference_geo: Curve3ReferenceGeo
    processed_geometry_source: Curve3DrawableGeometrySource
    anchor_point_drawables: Curve3AnchorPointDrawables
    tangent_line_drawables: Curve3TangentLineDrawables
    tangent_point_drawables: Curve3TangentPointDrawables
    anchor_tangent_drawables: Curve3AnchorTangentDrawables
    selectable_curve_component: Curve3PreviewCurveDrawable
    orient_guide_component: Curve3OrientGuideDrawable
    insert_preview_component: Curve3InsertPreviewDrawable
    locate_line_drawable: hou.GeometryDrawable
    highlight_curve_section: cu.HighlightCurveSection
    drawable_selector_component: DrawableSelectorComponent
    drawable_selector: GenericDrawableSelector
    drawable_selector_colors: GenericDrawableSelectorColors
    def __init__(self, scene_viewer: hou.SceneViewer, controller: Curve3Controller) -> None: ...
    def _tool_policy(self) -> Curve3ToolBase: ...
    def _selector_can_start_box_selection(self, kwargs: ViewerStateEventKwargs, default_fn: Callable[[ViewerStateEventKwargs], bool]) -> bool: ...
    def _selector_get_drag_locate(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def drawableSelectorClasses(self) -> list[list[hou.GeometryDrawable]]: ...
    def refresh_tangent_drawable_colors(self) -> None: ...
    def set_node(self, node: hou.OpNode | None) -> None: ...
    def set_pseudo_handle_points(self, pts: Iterable[int | _PseudoHandle] | None) -> None: ...
    def clear_pseudo_handle_points_for_rebuild(self) -> None: ...
    def set_active_handle_points(self, pts: Iterable[int] | None) -> None: ...
    def set_visual_selection_override(self, ptnums: Iterable[int] | None) -> None: ...
    def on_enter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def on_exit(self, kwargs: ViewerStateKwargs) -> None: ...
    def enable(self, on: bool) -> None: ...
    def show(self, on: bool) -> None: ...
    def on_draw_opaque(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def on_draw_drawableselector(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def on_draw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def set_insert_preview_position(self, pos: hou.Vector3) -> None: ...
    def clear_insert_preview(self) -> None: ...
    def draw_insert_preview(self, draw_handle: int) -> None: ...
    def clear_draw_preview_curve(self) -> None: ...
    def set_draw_preview_curve_geo(self, geo: hou.Geometry | None) -> None: ...
    def on_mouse_event(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def begin_interactive_drag(self) -> None: ...
    def end_interactive_drag(self) -> None: ...
    def update_from_prefs(self) -> None: ...
    def on_pref_changed(self, pref_name: str) -> None: ...
    def update_geometry(self, force: bool = ...) -> None: ...
    def external_pick(self, kwargs: ViewerStateEventKwargs) -> xg._ExternalPick | None: ...
    def get_last_curve_pick(self) -> cu.PickCurveResultType | None: ...
    def clear_last_curve_pick(self, reason: str = ...) -> None: ...
    def get_drawables_info(self) -> list[_DrawableInfo]: ...
    def savePlaybackOutputGeometry(self, geo: hou.Geometry) -> None: ...
    def _apply_selection(self, ptnums: Iterable[int], modifier: hou.EnumValue[hou.pickModifier]) -> None: ...
    def apply_selection(self, ptnums: Iterable[int], modifier: hou.EnumValue[hou.pickModifier]) -> None: ...
    def onLocateSingleSelection(self, kwargs: ViewerStateEventKwargs, result: ru.SingleSelectResult) -> bool: ...
    def onSingleSelection(self, kwargs: ViewerStateEventKwargs, result: ru.SingleSelectResult) -> bool: ...
    def onStartBoxSelection(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onLocateBoxSelection(self, kwargs: ViewerStateEventKwargs, result: ru.BoxSelectResult) -> bool: ...
    def _clear_locate_drawables(self) -> None: ...
    def _update_locate_color(self) -> None: ...
    def _set_locate_from_drawable_selection(
        self,
        drawable_selection: _DrawableSelection,
        source_drawables: Sequence[hou.GeometryDrawable] | None = ...,
    ) -> None: ...
    def _set_locate_line_from_result(self, drawable: hou.GeometryDrawable, elem_tuple: ru.SinglePickTuple) -> None: ...
    def _set_locate_curve_from_pick(self, pick: cu.PickCurveResultType | None) -> bool: ...
    def onBoxSelection(self, kwargs: ViewerStateEventKwargs, result: ru.BoxSelectResult) -> bool: ...
