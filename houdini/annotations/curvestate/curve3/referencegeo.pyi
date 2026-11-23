from collections.abc import Callable, Iterable, Mapping
from enum import Enum
from typing import Any, Final, Literal, Protocol

import curveutils as cu
import hou
import resourceutils as ru

# A bare object() sentinel at runtime; an enum member lets `is` checks narrow it away.
class _AmbiguousNodeEndpoint(Enum):
    AMBIGUOUS_NODE_ENDPOINT = 0

AMBIGUOUS_NODE_ENDPOINT: Final[Literal[_AmbiguousNodeEndpoint.AMBIGUOUS_NODE_ENDPOINT]]

class _GroupPointsGeoFn(Protocol):
    def __call__(self, input_geo: hou.Geometry, group_string: str, /, negate: bool = ...) -> hou.Geometry: ...

def force_cd_color_typeinfo(geo: hou.Geometry) -> None: ...

class CurveColors:
    color_options: ru.ColorOptions | None
    point_color_v4: hou.Vector4
    channel_color_v4: hou.Vector4
    select_color_v4: hou.Vector4
    branched_color_v4: hou.Vector4
    ends_color_v4: hou.Vector4
    branched_ends_color_v4: hou.Vector4
    def __init__(self, color_options: ru.ColorOptions | None) -> None: ...
    def set_color_options(self, color_options: ru.ColorOptions | None) -> None: ...
    def update(self) -> None: ...

def _handle_build_attribvop_verb(style: str, cache: dict[str, hou.SopVerb]) -> hou.SopVerb | None: ...
def _anchor_class_groups_attribvop_verb(cache: dict[str, hou.SopVerb]) -> hou.SopVerb | None: ...

class _CurveAnchorGeoBuildAdapter:
    color_cache: CurveColors
    _cached_attribvop_verbs: dict[str, hou.SopVerb]
    def __init__(
        self,
        *,
        source_geo: hou.Geometry,
        color_cache: CurveColors,
        selected_visual_ptnums_override: Iterable[int] | None = ...,
        attribvop_cache: dict[str, hou.SopVerb] | None = ...,
    ) -> None: ...
    def force_cd_color_typeinfo(self, geo: hou.Geometry) -> None: ...
    def ensure_anchor_class_groups(self, anchor_geo: hou.Geometry) -> None: ...
    def apply_anchor_colors(self, anchor_geo: hou.Geometry, source_geo: hou.Geometry) -> None: ...

def build_curve_anchor_geo(
    reference_geo: hou.Geometry,
    *,
    source_geo: hou.Geometry | None,
    color_cache: CurveColors,
    selected_visual_ptnums_override: Iterable[int] | None = ...,
    fallback_anchor_ptnums_fn: Callable[[hou.Geometry], list[int]] | None = ...,
    attribvop_cache: dict[str, hou.SopVerb] | None = ...,
) -> hou.Geometry: ...
def build_curve_anchor_split_geos(
    anchor_geo: hou.Geometry,
    *,
    compute_group_points_geo_fn: _GroupPointsGeoFn,
    force_cd_color_typeinfo_fn: Callable[[hou.Geometry], object],
) -> tuple[
    hou.Geometry,
    hou.Geometry,
    hou.Geometry,
    hou.Geometry,
    hou.Geometry,
    hou.Geometry,
    hou.Geometry,
    hou.Geometry,
]: ...

class _CurveHandleGeoBuildAdapter:
    _handle_build_verb_cache: dict[str, hou.SopVerb]
    def __init__(
        self,
        *,
        source_geo: hou.Geometry | None,
        reference_geo: hou.Geometry | None,
        handle_build_verb_cache: dict[str, hou.SopVerb] | None = ...,
    ) -> None: ...
    def get_verb_cache(self) -> dict[str, hou.SopVerb]: ...
    def ensure_internal_ptnum(self, geo: hou.Geometry, allow_add: bool = ...) -> None: ...

def build_curve_handle_geos(
    work_geo: hou.Geometry,
    *,
    source_geo: hou.Geometry | None,
    reference_geo: hou.Geometry | None,
    handle_build_verb_cache: dict[str, hou.SopVerb] | None,
    active_handle_pts: list[int],
    pseudo_handle_pts: list[int | cu.PseudoHandleTuple],
) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry]: ...
def prepare_curve_drawable_source(
    base_geo: hou.Geometry,
    parm_string_provider: Callable[[str], str | None] | None,
) -> hou.Geometry: ...

class Curve3ReferenceGeo:
    _cached_attribvop_verbs: dict[str, hou.SopVerb]
    color_cache: CurveColors
    def set_node(self, node: hou.Node | None) -> None: ...
    def set_geometry_provider(self, provider: Callable[[], hou.Geometry | None]) -> None: ...
    def ensure_geometry_provider(self, provider: Callable[[], hou.Geometry | None]) -> None: ...
    def set_parm_string_provider(self, provider: Callable[[str], str | None]) -> None: ...
    def ensure_parm_string_provider(self, provider: Callable[[str], str | None]) -> None: ...
    def set_color_options(self, color_options: ru.ColorOptions | None) -> None: ...
    def set_build_orient_guide(self, on: bool) -> None: ...
    def set_orient_guide_axis_visibility(self, *, x: bool, y: bool, z: bool) -> None: ...
    def set_orient_guide_scale(self, scale: float) -> None: ...
    def execute_curve3core_preview_verb(
        self,
        node: hou.Node,
        *,
        base_parms: Mapping[str, object] | None = ...,
        override_parms: Mapping[str, object] | None = ...,
        input_geo: hou.Geometry | None = ...,
        prune_prim_typenames: Iterable[str] = ...,
        log_label: str = ...,
    ) -> hou.Geometry | None: ...
    def invalidate(self) -> None: ...
    def set_pseudo_handle_pts(self, pts: Iterable[int | cu.PseudoHandleTuple]) -> None: ...
    def set_active_handle_pts(self, pts: Iterable[int]) -> None: ...
    def set_selected_visual_ptnums_override(self, ptnums: Iterable[int] | None) -> None: ...
    def internal_from_node_curve_endpoint(
        self, node_geo: hou.Geometry, node_prim: hou.Prim, endpoint_code: int
    ) -> int | None: ...
    def map_internal_to_node_endpoint(
        self, internal_ptnum: int, node_geo: hou.Geometry | None = ...
    ) -> tuple[hou.Prim, int, hou.Vector3, int] | Literal[_AmbiguousNodeEndpoint.AMBIGUOUS_NODE_ENDPOINT] | None: ...
