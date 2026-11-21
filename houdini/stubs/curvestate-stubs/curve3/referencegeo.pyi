import curveutils as cu
import hou
import resourceutils as ru
from .controller_backend import scene_node_geometry as scene_node_geometry
from .debug import debug_print as debug_print
from .tool_helpers import point_group_string as point_group_string
from collections.abc import Callable as Callable, Iterable, Mapping
from enum import Enum
from typing import Final, Literal, Protocol

class _AmbiguousNodeEndpoint(Enum):
    AMBIGUOUS_NODE_ENDPOINT = 0

class _GroupPointsGeoFn(Protocol):
    def __call__(self, input_geo: hou.Geometry, group_string: str, /, negate: bool = ...) -> hou.Geometry: ...

AMBIGUOUS_NODE_ENDPOINT: Final[Literal[_AmbiguousNodeEndpoint.AMBIGUOUS_NODE_ENDPOINT]]

def _handle_build_attribvop_verb(style: str, cache: dict[str, hou.SopVerb]) -> hou.SopVerb | None:
    """
    Return a cached Attribute VOP verb for generating Bezier handle geometry.

    Supports the reference-geometry construction pipeline. Uses the supplied inputs and
    cached geometry state to perform this focused step.
    """
def _anchor_class_groups_attribvop_verb(cache: dict[str, hou.SopVerb]) -> hou.SopVerb | None:
    """
    Return a cached Attribute VOP verb that classifies anchor points as ends or branches.

    Runs on anchor geometry and reads source topology from input 1 using `__internal_ptnum`
    as the stable point id. This avoids classifying source geometry, collecting ids in
    Python, and projecting the groups back onto anchor geometry with groupcreate verbs.
    """
def add_internal_ptnum_geo_if_needed(base_geo: hou.Geometry) -> hou.Geometry:
    """
    Ensure every source point has a stable internal point id.

    Downstream drawable, pick, and selection geometries may be filtered or rebuilt, so local
    ptnums cannot be used as durable identity. Returns the input unchanged when the
    attribute already exists; otherwise runs the Enumerate SOP verb over points to create
    `__internal_ptnum`.

    Takes base_geo, the source geometry to normalize. Returns geometry with
    `__internal_ptnum`, or an empty geometry for empty input.
    """
def add_internal_primnum_geo_if_needed(base_geo: hou.Geometry) -> hou.Geometry:
    """
    Ensure every source primitive has a stable internal primitive id.

    Preview and drawable primitives are converted/resampled, but picking must still map back
    to the original curve primitive. Returns the input unchanged when the primitive
    attribute exists; otherwise runs the Enumerate SOP verb over primitives to create
    `__internal_primnum`.

    Takes base_geo, the source geometry to normalize. Returns geometry with
    `__internal_primnum`, or an empty geometry for empty input.
    """
def anchor_source_ptnums_from_group(source_geo: hou.Geometry, prepared_geo: hou.Geometry, group_name: str) -> list[int] | None:
    '''
    Return source-domain anchor ptnums from a group on source geometry.

    The committed verb/source geometry does not own `__internal_ptnum`; its
    output group is already in source point-number space and may include Bezier
    tangents/control vertices. This maps those source point numbers through
    `__internal_ptnum` on prepared curve geometry, intersects them with
    `__anchor_points`, then returns source-domain anchor ptnums. Returns None
    when the source group is not present, so callers can distinguish "no output
    group" from "output group existed but contained no anchors".
    '''
def build_curve_drawable_hull_geo(prepared_geo: hou.Geometry) -> hou.Geometry:
    """
    Build the curve hull geometry used by drawable consumers.

    Makes this derived drawable/reference geometry reusable outside the viewer state. copies
    or filters the input geometry, applies the required SOP verbs/groups, and returns
    derived geometry data.
    """
def force_cd_color_typeinfo(geo: hou.Geometry) -> None:
    """
    Force the `Cd` attribute to carry Houdini color type information.

    keep drawable color authoring consistent across anchor/reference outputs. resolves
    color/group inputs and writes Cd or color-related verb parameters.
    """

class CurveColors:
    color_options: ru.ColorOptions | None
    point_color_v4: hou.Vector4
    channel_color_v4: hou.Vector4
    select_color_v4: hou.Vector4
    branched_color_v4: hou.Vector4
    ends_color_v4: hou.Vector4
    branched_ends_color_v4: hou.Vector4
    def __init__(self, color_options: ru.ColorOptions | None) -> None:
        """
        Initialize this helper object.

        Centralizes the state needed by later geometry-builder calls. stores constructor
        arguments on the instance without producing geometry.
        """
    def set_color_options(self, color_options: ru.ColorOptions | None) -> None:
        """
        Set the color options used by later reference-geometry rebuilds.

        Lets the owner configure reference-geometry generation without reaching into internals.
        Normalizes and stores the supplied value for use by the next update/build.
        """
    def update(self) -> None:
        """
        Refresh the adapter state from its current inputs.

        Supports the reference-geometry construction pipeline. Uses the supplied inputs and
        cached geometry state to perform this focused step.
        """

class _CurveAnchorGeoBuildAdapter:
    color_cache: CurveColors
    _cached_attribvop_verbs: dict[str, hou.SopVerb]
    def __init__(self, *, source_geo: hou.Geometry, color_cache: CurveColors, selected_visual_ptnums_override: Iterable[int] | None = None, attribvop_cache: dict[str, hou.SopVerb] | None = None) -> None:
        """
        Initialize this helper object.

        Centralizes the state needed by later geometry-builder calls. stores constructor
        arguments on the instance without producing geometry.
        """
    def force_cd_color_typeinfo(self, geo: hou.Geometry) -> None:
        """
        Force the `Cd` attribute to carry Houdini color type information.

        keep drawable color authoring consistent across anchor/reference outputs. resolves
        color/group inputs and writes Cd or color-related verb parameters.
        """
    def anchor_selected_group_expr(self, anchor_geo: hou.Geometry) -> str:
        """
        Return the group expression used to color selected anchors.

        Centralizes group expression/materialization rules used by drawable builders. queries,
        creates, combines, or filters groups with HOM/SOP verbs.
        """
    def ensure_anchor_class_groups(self, anchor_geo: hou.Geometry) -> None:
        """
        Ensure anchor class groups exist on anchor geometry.

        Classifies anchor points directly from source topology in one Attribute VOP pass.
        Mutates `anchor_geo` to contain `__end_pts`, `__branched_pts`, and
        `__branched_end_pts`, preserving the anchor geometry's existing point attributes
        and groups.
        """
    def anchor_class_group_expr(self, anchor_geo: hou.Geometry, class_group: str) -> str:
        """
        Return a usable expression for an anchor class group.

        Centralizes group expression/materialization rules used by drawable builders. queries,
        creates, combines, or filters groups with HOM/SOP verbs.
        """
    def apply_anchor_colors(self, anchor_geo: hou.Geometry, source_geo: hou.Geometry) -> None:
        """
        Apply anchor colors.

        Keeps mutation/color/group logic in one place. Runs the relevant verb or attribute edits
        on supplied geometry using the provided group/color inputs.
        """

def build_curve_anchor_geo(reference_geo: hou.Geometry, *, source_geo: hou.Geometry | None, color_cache: CurveColors, selected_visual_ptnums_override: Iterable[int] | None = None, fallback_anchor_ptnums_fn: Callable[[hou.Geometry], list[int]] | None = None, attribvop_cache: dict[str, hou.SopVerb] | None = None) -> hou.Geometry:
    """
    Build the anchor-point geometry used by point drawables.

    Makes this derived drawable/reference geometry reusable outside the viewer state. copies
    or filters the input geometry, applies the required SOP verbs/groups, and returns
    derived geometry data.
    """
def build_curve_anchor_split_geos(anchor_geo: hou.Geometry, *, compute_group_points_geo_fn: _GroupPointsGeoFn, force_cd_color_typeinfo_fn: Callable[[hou.Geometry], object]) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry]:
    """
    Split anchor geometry into the style/end-point geometries used by drawables.

    Makes this derived drawable/reference geometry reusable outside the viewer state. copies
    or filters the input geometry, applies the required SOP verbs/groups, and returns
    derived geometry data.
    """

class _CurveHandleGeoBuildAdapter:
    _handle_build_verb_cache: dict[str, hou.SopVerb]
    def __init__(self, *, source_geo: hou.Geometry | None, reference_geo: hou.Geometry | None, handle_build_verb_cache: dict[str, hou.SopVerb] | None = None) -> None:
        """
        Initialize this helper object.

        Centralizes the state needed by later geometry-builder calls. stores constructor
        arguments on the instance without producing geometry.
        """
    def get_verb_cache(self) -> dict[str, hou.SopVerb]: ...
    def ensure_internal_ptnum(self, geo: hou.Geometry, allow_add: bool = False) -> None:
        """
        Ensure geometry points carry `__internal_ptnum`.

        Supports the reference-geometry construction pipeline. Uses the supplied inputs and
        cached geometry state to perform this focused step.
        """
    def compute_handles_from_ptnums(self, input_geo: hou.Geometry, ptnums: list[int]) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry]:
        """
        Compute handle geometries from selected or active ptnums.

        Derives selection or topology data needed by later builders. Evaluates the provided
        geometry/groups with SOP verbs or HOM iteration.
        """
    def compute_pseudo_handle_geos(self, pts: list[cu.PseudoHandleTuple]) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry] | None:
        """
        Compute pseudo-handle geometries from ad hoc pseudo-handle inputs.

        Derives selection or topology data needed by later builders. Evaluates the provided
        geometry/groups with SOP verbs or HOM iteration.
        """

def build_curve_pseudo_handle_geos(pseudo_handle_pts: list[int | cu.PseudoHandleTuple], *, source_geo: hou.Geometry | None, reference_geo: hou.Geometry | None) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry] | None:
    """
    Build pseudo-handle line and endpoint geometries.

    Makes this derived drawable/reference geometry reusable outside the viewer state. copies
    or filters the input geometry, applies the required SOP verbs/groups, and returns
    derived geometry data.
    """
def build_curve_pseudo_handle_only_geos(pseudo_handle_pts: list[int | cu.PseudoHandleTuple], *, source_geo: hou.Geometry | None, reference_geo: hou.Geometry | None) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry]:
    """
    Build only pseudo-handle geometries for empty or preview-only states.

    Makes this derived drawable/reference geometry reusable outside the viewer state. copies
    or filters the input geometry, applies the required SOP verbs/groups, and returns
    derived geometry data.
    """
def build_curve_handle_geos(work_geo: hou.Geometry, *, source_geo: hou.Geometry | None, reference_geo: hou.Geometry | None, handle_build_verb_cache: dict[str, hou.SopVerb] | None, active_handle_pts: list[int], pseudo_handle_pts: list[int | cu.PseudoHandleTuple]) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry]:
    """
    Build tangent line and tangent endpoint geometries for Bezier anchors.

    Makes this derived drawable/reference geometry reusable outside the viewer state. copies
    or filters the input geometry, applies the required SOP verbs/groups, and returns
    derived geometry data.
    """
def build_curve_orient_guide_geo(prepared_geo: hou.Geometry, *, up_attrib_name: str = ..., scale_attrib_name: str = ..., show_x: bool = True, show_y: bool = True, show_z: bool = True, guide_scale: float = 0.1) -> hou.Geometry:
    """
    Build the orient/scale guide geometry displayed along curves.

    Makes this derived drawable/reference geometry reusable outside the viewer state. copies
    or filters the input geometry, applies the required SOP verbs/groups, and returns
    derived geometry data.
    """
def prepare_curve_drawable_source(base_geo: hou.Geometry, parm_string_provider: Callable[[str], str | None] | None) -> hou.Geometry:
    """
    Prepare the reusable curve source consumed by drawable builders.

    Anchors, handles, preview curves, hulls, and guide geometry all need the same stable ids
    and family/type groups; doing this once avoids repeated verb work and keeps every
    downstream builder on the same contract. Ensures point/primitive identity attributes,
    filters to curve primitives, creates poly/nurbs/bezier family groups, seeds Bezier
    point-type groups from parms, and creates the anchor admission group.

    Contract:
    - point ids are available in `__internal_ptnum`
    - primitive ids are available in `__internal_primnum`
    - curve-family prim/point groups exist for poly/nurbs/bezier
    - point-type groups exist for corner/smooth/auto
    - anchor admission group exists in `__anchor_points`
    """
def build_curve_reference_geo(prepared_geo: hou.Geometry, *, selected_group: str = ...) -> hou.Geometry:
    """
    Build reference geometry from a prepared curve source.

    Makes this derived drawable/reference geometry reusable outside the viewer state. copies
    or filters the input geometry, applies the required SOP verbs/groups, and returns
    derived geometry data.
    """
def build_curve_preview_geo(prepared_geo: hou.Geometry) -> hou.Geometry:
    """
    Build the preview curve geometry used for curve drawing and picking.

    the viewer needs a consistent polyline-like representation for hover, segment picking,
    and display across polygon, NURBS, and Bezier curves. Uses the prepared family groups to
    resample/convert curves, promotes the primitive and curve-position attributes needed by
    picking, and returns the resulting drawable curve geometry.
    """

class Curve3ReferenceGeo:
    """Minimal reference-geo wrapper for Curve 3 (expand as needed)."""
    color_cache: CurveColors
    _cached_attribvop_verbs: dict[str, hou.SopVerb]
    def __init__(self, node: hou.Node | None = None) -> None:
        """
        Initialize this helper object.

        Centralizes the state needed by later geometry-builder calls. stores constructor
        arguments on the instance without producing geometry.
        """
    def set_node(self, node: hou.Node | None) -> None:
        """
        Set the node used by later reference-geometry rebuilds.

        Lets the owner configure reference-geometry generation without reaching into internals.
        Normalizes and stores the supplied value for use by the next update/build.
        """
    def set_geometry_provider(self, provider: Callable[[], hou.Geometry | None]) -> None:
        """
        Set the geometry provider used by later reference-geometry rebuilds.

        Lets the owner configure reference-geometry generation without reaching into internals.
        Normalizes and stores the supplied value for use by the next update/build.
        """
    def ensure_geometry_provider(self, provider: Callable[[], hou.Geometry | None]) -> None:
        """ Set geometry provider if None. """
    def set_parm_string_provider(self, provider: Callable[[str], str | None]) -> None:
        """
        Set the parm string provider used by later reference-geometry rebuilds.

        Lets the owner configure reference-geometry generation without reaching into internals.
        Normalizes and stores the supplied value for use by the next update/build.
        """
    def ensure_parm_string_provider(self, provider: Callable[[str], str | None]) -> None:
        """ Set parm string provider if None. """
    def set_color_options(self, color_options: ru.ColorOptions | None) -> None:
        """
        Set the color options used by later reference-geometry rebuilds.

        Lets the owner configure reference-geometry generation without reaching into internals.
        Normalizes and stores the supplied value for use by the next update/build.
        """
    def set_build_orient_guide(self, on: bool) -> None:
        """
        Set the build orient guide used by later reference-geometry rebuilds.

        Lets the owner configure reference-geometry generation without reaching into internals.
        Normalizes and stores the supplied value for use by the next update/build.
        """
    def set_orient_guide_axis_visibility(self, *, x: bool, y: bool, z: bool) -> None:
        """
        Set the orient guide axis visibility used by later reference-geometry rebuilds.

        Lets the owner configure reference-geometry generation without reaching into internals.
        Normalizes and stores the supplied value for use by the next update/build.
        """
    def set_orient_guide_scale(self, scale: float) -> None:
        """
        Set the orient guide scale used by later reference-geometry rebuilds.

        Lets the owner configure reference-geometry generation without reaching into internals.
        Normalizes and stores the supplied value for use by the next update/build.
        """
    def update(self) -> bool:
        """
        Refresh all cached reference and drawable geometries.

        source geometry, selection, visual overrides, pseudo handles, and guide settings can
        change independently; this method keeps the derived geometry cache coherent. computes a
        cache signature from geometry ids and state, skips work when unchanged, otherwise
        rebuilds prepared source, reference geo, anchors, split anchor geos, preview curves,
        orient guides, and handles.
        """
    def get_base_geo(self) -> hou.Geometry:
        """
        Return the cached base geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_anchor_geo(self) -> hou.Geometry:
        """
        Return the cached anchor geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_reference_geo(self) -> hou.Geometry:
        """
        Return the cached reference geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def has_selected_bezier_points(self) -> bool:
        """
        Test whether selected bezier points.

        let callers branch on topology/selection state without duplicating geometry queries.
        Checks the relevant cached geometry, groups, or primitive identity and returns a
        boolean.
        """
    def has_selected_closed_curve_points(self) -> bool:
        """
        Test whether selected closed curve points.

        let callers branch on topology/selection state without duplicating geometry queries.
        Checks the relevant cached geometry, groups, or primitive identity and returns a
        boolean.
        """
    def get_anchor_broken_geo(self) -> hou.Geometry:
        """
        Return the cached anchor broken geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_anchor_smooth_geo(self) -> hou.Geometry:
        """
        Return the cached anchor smooth geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_anchor_balanced_geo(self) -> hou.Geometry:
        """
        Return the cached anchor balanced geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_anchor_auto_geo(self) -> hou.Geometry:
        """
        Return the cached anchor auto geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_anchor_ends_broken_geo(self) -> hou.Geometry:
        """
        Return the cached anchor ends broken geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_anchor_ends_smooth_geo(self) -> hou.Geometry:
        """
        Return the cached anchor ends smooth geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_anchor_ends_balanced_geo(self) -> hou.Geometry:
        """
        Return the cached anchor ends balanced geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_anchor_ends_auto_geo(self) -> hou.Geometry:
        """
        Return the cached anchor ends auto geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_drawable_hull_geo(self) -> hou.Geometry:
        """
        Return the cached drawable hull geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_curve_base_geo(self) -> hou.Geometry:
        """
        Return the cached curve base geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_preview_curve_geo(self) -> hou.Geometry:
        """
        Return the cached preview curve geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_orient_guide_geo(self) -> hou.Geometry:
        """
        Return the cached orient guide geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def execute_curve3core_preview_verb(self, node: hou.Node, *, base_parms: Mapping[str, object] | None = None, override_parms: Mapping[str, object] | None = None, input_geo: hou.Geometry | None = None, prune_prim_typenames: Iterable[str] = ('PackedGeometry', 'Channel'), log_label: str = 'preview verb') -> hou.Geometry | None:
        """
        Execute curve3core as a non-destructive preview verb.

        tools need live preview output without mutating node parms or committing stateful
        operations. merges base parms with caller overrides, optionally prunes helper primitive
        types from the input, executes the curve3core verb, and returns its output geometry.
        """
    def get_handle_smooth_lines_geo(self) -> hou.Geometry:
        """
        Return the cached handle smooth lines geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_handle_broken_lines_geo(self) -> hou.Geometry:
        """
        Return the cached handle broken lines geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_handle_auto_lines_geo(self) -> hou.Geometry:
        """
        Return the cached handle auto lines geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_handle_end_points_tied_geo(self) -> hou.Geometry:
        """
        Return the cached handle end points tied geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_handle_end_points_broken_geo(self) -> hou.Geometry:
        """
        Return the cached handle end points broken geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_handle_end_points_auto_geo(self) -> hou.Geometry:
        """
        Return the cached handle end points auto geo.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def get_handle_end_points_geo(self) -> hou.Geometry:
        """
        Return the cached handle end points geo.

        some older tests/callers expect a single endpoint geometry instead of separate
        tied/broken/auto endpoint drawables. Creates a new geometry and merges the cached
        endpoint geometries for every handle style that currently exists.
        """
    def invalidate(self) -> None:
        """
        reset invalidate.

        Clears stale derived geometry after source geometry changes. Replaces cached
        geometries/state with empty defaults.
        """
    def set_pseudo_handle_pts(self, pts: Iterable[int | cu.PseudoHandleTuple]) -> None:
        """
        Set the pseudo handle pts used by later reference-geometry rebuilds.

        Lets the owner configure reference-geometry generation without reaching into internals.
        Normalizes and stores the supplied value for use by the next update/build.
        """
    def get_pseudo_handle_pts(self) -> list[int | cu.PseudoHandleTuple]:
        """
        Return the cached pseudo handle pts.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def set_active_handle_pts(self, pts: Iterable[int]) -> None:
        """
        Set the active handle pts used by later reference-geometry rebuilds.

        Lets the owner configure reference-geometry generation without reaching into internals.
        Normalizes and stores the supplied value for use by the next update/build.
        """
    def get_active_handle_pts(self) -> list[int]:
        """
        Return the cached active handle pts.

        provide a stable read API for drawable and picker code. Reads the current cached member
        and returns it directly.
        """
    def set_selected_visual_ptnums_override(self, ptnums: Iterable[int] | None) -> None:
        """
        Set the selected visual ptnums override used by later reference-geometry rebuilds.

        Lets the owner configure reference-geometry generation without reaching into internals.
        Normalizes and stores the supplied value for use by the next update/build.
        """
    def get_full_geo_point(self, point: hou.Point) -> hou.Point | None:
        """
        Return the cached full geo point.

        picker and drawable callbacks operate on split geometries but tool operations must act
        on the source/reference point identity. Reads `__internal_ptnum` from the point and
        looks that point up in cached base geometry, with a strict compatibility fallback for
        base-geo points missing the attribute.

        Takes point, a point from a derived or base geometry. Returns matching base-geo point,
        or None when unavailable.
        """
    def get_full_geo_prim(self, prim: hou.Prim) -> hou.Prim | None:
        """
        Return the cached full geo prim.

        curve picking produces primitives from preview geometry, while operations need the
        original source primitive identity. Reads strict `__internal_primnum`, looks up that
        primitive on the cached base geo, and validates that the result is still a curve.

        Takes prim, a primitive carrying `__internal_primnum`. Returns matching base-geo
        primitive; raises if identity is invalid.
        """
    def get_internal_primnum(self, prim: hou.Prim) -> int:
        """
        Return the cached internal primnum.

        Primitive number remapping is common during conversion/resampling, so callers need a
        strict source identity attribute. Reads `__internal_primnum`, validates that it exists
        and is non-negative, and raises a bug-level error otherwise.

        Takes prim, a primitive expected to carry `__internal_primnum`. Returns non-negative
        internal Primitive number.
        """
    def internal_from_node_curve_endpoint(self, node_geo: hou.Geometry, node_prim: hou.Prim, endpoint_code: int) -> int | None:
        """
        Resolve internal from node curve endpoint mapping.

        Preserves stable identity between source, reference, and drawable geometries. uses
        internal point/primitive attributes and endpoint topology to translate between numbering
        domains.
        """
    def map_internal_to_node_endpoint(self, internal_ptnum: int, node_geo: hou.Geometry | None = None) -> tuple[hou.Prim, int, hou.Vector3, int] | Literal[_AmbiguousNodeEndpoint.AMBIGUOUS_NODE_ENDPOINT] | None:
        """
        Resolve map internal to node endpoint mapping.

        Preserves stable identity between source, reference, and drawable geometries. uses
        internal point/primitive attributes and endpoint topology to translate between numbering
        domains.
        """
    def can_join_selected_endpoints(self, group_string: str) -> bool:
        """
        Test whether join selected endpoints.

        let callers branch on topology/selection state without duplicating geometry queries.
        Checks the relevant cached geometry, groups, or primitive identity and returns a
        boolean.
        """
