import hou
import typing
from collections.abc import Sequence

RORD_LOOKUP: dict[str, tuple[int, int, int]]
AXIS_COLORS: list[str]
TOLERANCE: float
DOTTED_LINE_LENGTH: float
AXES: list[hou.Vector3]
SOFT_LIMIT_LERP_COLS: list[hou.Vector3]
BASE_SIZE_SCALE: float
BASE_OUTER_PLANE_SCALE: float
BASE_INNER_PLANE_SCALE: float

def rotOrderStringToInts(rord: str) -> tuple[int, int, int]:
    """
    Convert a rotation order from a string of the form
    'xyz' to a tuple of integers such that

    rot[order[0]] gives the first euler angle.
    rot[order[1]] gives the second euler angle.
    rot[order[2]] gives the third euler angle.
    """
@typing.overload
def applyLimits(v: hou.Vector3, min_v: hou.Vector3 | None, max_v: hou.Vector3 | None) -> hou.Vector3: ...
@typing.overload
def applyLimits(v: int, min_v: int | None, max_v: int | None) -> int: ...
@typing.overload
def applyLimits(v: float, min_v: float | None, max_v: float | None) -> float: ...
@typing.overload
def applyLimits(v: hou.Vector3 | float, min_v: hou.Vector3 | float | None, max_v: hou.Vector3 | float | None) -> hou.Vector3 | float: ...
def maxComponents(u: hou.Vector3, v: hou.Vector3) -> hou.Vector3:
    """
    Return a vector in which each component is the min of the
    respective components in u and v.
    """
def minComponents(u: hou.Vector3, v: hou.Vector3) -> hou.Vector3:
    """
    Return a vector in which each component is the min of the
    respective components in u and v.
    """
def chooseLimitMin(limit_min: hou.Vector3 | None, guide_limit_min: hou.Vector3 | None, enforce_guide_limit: bool) -> hou.Vector3 | None:
    """
    Choose the lower limit given the lock limit, the guide limit and
    whether we are enforcing the guide limits.
    """
def chooseLimitMax(limit_max: hou.Vector3 | None, guide_limit_max: hou.Vector3 | None, enforce_guide_limit: bool) -> hou.Vector3 | None:
    """
    Choose the upper limit given the lock limit, the guide limit and
    whether we are enforcing the guide limits.
    """
def minLimitHit(pos: hou.Vector3, lim: hou.Vector3 | None, i: int) -> bool:
    """ Whether pos exceeds the given min limit. """
def maxLimitHit(pos: hou.Vector3, lim: hou.Vector3 | None, i: int) -> bool:
    """ Whether pos exceeds the given max limit. """
def anyLimitHit(pos: hou.Vector3, min_lim: hou.Vector3 | None, max_lim: hou.Vector3 | None) -> bool:
    """ Whether pos hits or exceeds any limit. """
def lerpVector(v0: hou.Vector3, v1: hou.Vector3, weight: float) -> hou.Vector3:
    """ Linearly interpolate between two vectors. """
def outsideLimits(pos: hou.Vector3, min_lim: hou.Vector3 | None, max_lim: hou.Vector3 | None) -> bool:
    """ Return whether pos is outside the given limits within a tolerance. """
def strictlyInsideLimits(pos: hou.Vector3, min_lim: hou.Vector3 | None, max_lim: hou.Vector3 | None) -> bool:
    """ Return whether pos is inside the given limits within a tolerance. """
def closestLimitPos(pos: hou.Vector3, min_lim: hou.Vector3 | None, max_lim: hou.Vector3 | None) -> hou.Vector3:
    """
    Return the closest position to pos that is inside the given limits.
    If pos itself is within the limits, it will be returned.
    """
def closestOneSidedLimitPosToLine(origin: hou.Vector3, direction: hou.Vector3, min_lim: hou.Vector3 | None, max_lim: hou.Vector3 | None) -> tuple[hou.Vector3, hou.Vector3]: ...
def closestLimitPosToLine(origin: hou.Vector3, direction: hou.Vector3, min_lim: hou.Vector3 | None, max_lim: hou.Vector3 | None) -> tuple[hou.Vector3, hou.Vector3]:
    """
    Find the closest point on the line defined by origin and directin to the
    limit planes defined by min_lim and max_lim.

    NOTE: This currently assumes direction is not parallel to any of the
    planes and will only check against the edges of the box.
    """
def getLimitIntersection(ray_orig: hou.Vector3, ray_dir: hou.Vector3, limit_min: hou.Vector3 | None, limit_max: hou.Vector3 | None, allow_reverse: bool = False) -> list[hou.Vector3]:
    """
    Find the intersections between the line defined by ray_orig and ray_dir
    and the limit planes defined by limit_min and limit_max.
    If allow_reverse is true, it will also include intersections in the
    negative direction.
    """
def getOutlineGeometry(faces_geo: hou.Geometry) -> hou.Geometry:
    """ Return a geometry containing only unshared edges in faces_geo. """
def makeLineSegment(geo: hou.Geometry, start_pos: hou.Vector3 | Sequence[float], end_pos: hou.Vector3 | Sequence[float]) -> hou.Polygon:
    """ Create a line segment in geo between start_pos and end_pos. """

class TransformLimitGuide:
    """
    Encapsulate the creation and visualization of transform limits guide
    geometry drawables.

    Creates a spherical patch, and a pie-like guide for the rotation limits.
    """
    scene_viewer: hou.SceneViewer
    axis_colors: list[hou.Vector3]
    face_drawable: hou.GeometryDrawable
    line_drawable: hou.GeometryDrawable
    face_line_drawable: hou.GeometryDrawable
    dotted_line_drawable: hou.GeometryDrawable
    point_drawable: hou.GeometryDrawable
    faces_geometry: hou.Geometry
    faces_lines_geometry: hou.Geometry
    lines_geometry: hou.Geometry
    dotted_line_geometry: hou.Geometry
    points_geometry: hou.Geometry
    parent_xform: hou.Matrix4
    scale_factor: float
    scale_xform: hou.Matrix4
    inv_scale_xform: hou.Matrix4
    rot_limit_min: hou.Vector3 | None
    rot_limit_max: hou.Vector3 | None
    rot_guide_limit_min: hou.Vector3 | None
    rot_guide_limit_max: hou.Vector3 | None
    trans_limit_min: hou.Vector3 | None
    trans_limit_max: hou.Vector3 | None
    trans_guide_limit_min: hou.Vector3 | None
    trans_guide_limit_max: hou.Vector3 | None
    cur_rotates: hou.Vector3
    cur_scales: hou.Vector3
    cur_translates: hou.Vector3
    start_translates: hou.Vector3
    ANGLE_INC: int
    plane_base_scaling: float
    rot_order: str
    enforce_guide_limits: bool
    show_axes: bool
    show_rot_guides: bool
    show_trans_guides: bool
    enabled: bool
    def __init__(self, scene_viewer: hou.SceneViewer, name: str) -> None: ...
    def enable(self, val: bool) -> None: ...
    def setOpacity(self, weight: float = 1.0, min_opacity: float = 0.05, max_opacity: float = 0.3, max_line_opacity: float = 0.5) -> None:
        """
        Set opacity of guides using a weight between 0 and 1,
        the actual alpha of the face guides is lerped using this weight
        between 0.05 and 0.3 and the alpha of line guides is lerped between
        0.05 and 0.5.
        """
    def showRotateGuides(self, on: bool) -> None:
        """ Set whether rotate guides are visible. """
    def showTranslateGuides(self, on: bool) -> None:
        """ Set whether translate guides are visible. """
    def showAll(self, on: bool = True) -> None:
        """ Set whether to show both the rotate and translate guides. """
    def hasRotationLimits(self) -> bool:
        """
        Whether there are any rotation limits set, even if they
        are just guide limits.

        NOTE: If there are only guide limits we still want to draw
              geometry to show these limits.
        """
    def hasTranslationLimits(self) -> bool:
        """
        Whether there are any translation limits set,
        even if they are just guide limits.

        NOTE: If there are only guide limits we still want to draw
              geometry to show these limits.
        """
    def setRotOrder(self, rot_order: str | None = None) -> None:
        """ Set the rotation order. """
    def setRotLimits(self, limit_min: hou.Vector3 | None = None, limit_max: hou.Vector3 | None = None) -> None:
        """ Set the rotation limits. """
    def setGuideRotLimits(self, guide_limit_min: hou.Vector3 | None = None, guide_limit_max: hou.Vector3 | None = None) -> None:
        """
        Set the rotation guide limits. These are not enforced, but just
        show a guide line to the limit from the current position when
        given.
        """
    def getRotLimitMin(self) -> hou.Vector3 | None:
        """ Get the enforced min rotate limit. """
    def getRotLimitMax(self) -> hou.Vector3 | None:
        """ Get the enforced min rotate limit. """
    def setTranslateLimits(self, limit_min: hou.Vector3 | None = None, limit_max: hou.Vector3 | None = None) -> None:
        """ Set the translate limits. """
    def setGuideTranslateLimits(self, guide_limit_min: hou.Vector3 | None = None, guide_limit_max: hou.Vector3 | None = None) -> None:
        """
        Set the translation guide limits. These are not enforced, but just
        show a guide line to the limit from the current position when
        given.
        """
    def getTranslateLimitMin(self) -> hou.Vector3 | None:
        """ Get the enforced min translate limits. """
    def getTranslateLimitMax(self) -> hou.Vector3 | None:
        """ Get the enforced max translate limits. """
    def setEnforceGuideLimits(self, enforce: bool) -> None:
        """ Set whether the guide limits are enforced. """
    def clearLimits(self) -> None:
        """ Clear the rotation and translation limits. """
    def setParentTransform(self, xform: hou.Matrix4) -> None:
        """ Set the local space parent transform. """
    def setHandlePivotTransform(self, xform: hou.Matrix4 | None) -> None:
        """
        Set the handle's pivot transform. This is only used to see
        if the parent xform is equal to the handle's pivot xform.

        If set to None, always show the axes. Otherwise,

        If they are not equal, we add geometry to represent the
        control's local axes that are constrained within the visualized
        rotation limits.

        If they are equal, this is not necessary as these axes are the
        handle's axes.
        """
    def setGuideScale(self, scale: float) -> None:
        """ Set the scale for the guides. """
    def setStartLocalTranslates(self, translates: hou.Vector3) -> None:
        """ Set the start translates in local space. """
    def setLocalTranslates(self, translates: hou.Vector3) -> None:
        """ Set the current translates in local space. """
    def setLocalRotates(self, rots: hou.Vector3) -> None:
        """ Set the current rotates in local space. """
    def setLocalScales(self, scales: hou.Vector3) -> None:
        """ Set the current scales in local space. """
    def update(self) -> None:
        """ Update the geometry. """
    def show(self, val: bool) -> None:
        """ Show or hide the drawables. """
    def showIfHasLimits(self) -> None:
        """ Show the guide is there are limits set. """
    def draw(self, draw_handle: int) -> None:
        """ Draw the drawables. """
