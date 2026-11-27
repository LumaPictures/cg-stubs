import hou
import resourceutils as ru
import typing
from collections.abc import Iterable, Mapping, Sequence
from houtypes import RadialMenuKwargs, ViewerStateEventKwargs, ViewerStateKwargs
from typing import Any, Callable, Generic, Literal, NotRequired, Protocol, TypeAlias, TypedDict


from typing import TypeAlias
from typing import TypeVar
from typing import TypeVar
BasisTuple: TypeAlias = tuple[hou.Vector3, hou.Vector3, hou.Vector3]
PlaneOrigAndNormal: TypeAlias = tuple[hou.Vector3, hou.Vector3]
KwargsDict: TypeAlias = dict[str, Any]
PtnumFrameList: TypeAlias = list[tuple[int, hou.Vector3, hou.Vector3]]
CircleBaseInfo: TypeAlias = tuple[float, hou.Vector3]
CircleExtendedInfo: TypeAlias = tuple[float, hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3, bool, float]
SingleArcPoints: TypeAlias = tuple[hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3]
SplitArcPoints: TypeAlias = tuple[hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3]
PseudoHandleTuple: TypeAlias = tuple[hou.Vector3 | None, hou.Vector3 | None, hou.Vector3 | None, bool]
PickPointResultType: TypeAlias = hou.Point
PickHandleLineResultType: TypeAlias = tuple[hou.Point, hou.Point, float, hou.Vector3]
PickCurveResultType: TypeAlias = tuple[hou.Prim, float, hou.Vector3]
PickRoundCornerResultType: TypeAlias = tuple[hou.Point, hou.Vector3]
PickFaceResultType: TypeAlias = tuple[hou.Prim, hou.Vector3, hou.Vector3] | tuple[hou.Prim, None, None]
PickResultType: TypeAlias = hou.Point | PickHandleLineResultType | PickCurveResultType | PickRoundCornerResultType | PickFaceResultType
_PickCallback: TypeAlias = Callable[[ViewerStateEventKwargs, dict[str, PickResultType]], bool]
_KeyCallback: TypeAlias = Callable[[int | None, list[str]], bool]
_GadgetStateT_co = TypeVar('_GadgetStateT_co', bound=_GadgetState, covariant=True, default=_GadgetState)
_StateT_co = TypeVar('_StateT_co', covariant=True, default=object)
class _GadgetState(Protocol):
    @property
    def state_gadgets(self) -> Mapping[str, hou.GadgetDrawable]: ...
    @property
    def state_context(self) -> hou.ViewerStateContext: ...

class _RadialItem(TypedDict):
    type: int
    loc: hou.EnumValue[hou.radialItemLocation]
    label: str
    icon: str
    parm: NotRequired[str]
    value: NotRequired[int | float | str | dict[str, str]]
    script: NotRequired[str]
PointNumberMap = dict[int, int]
PtnumToVtxnumMap = dict[int, int]
PointNumberSet = set[int]
PointNumberList = list[int]
PtnumSetAndMaybeMap = PointNumberSet | tuple[PointNumberSet, PointNumberMap]
PrimNumList = list[int]
PrimNumSet = set[int]
PtnumRadiusList = list[tuple[int, float]]
IDENTITY_BASIS: list[hou.Vector3]

def findCurveNode(node: hou.OpNode) -> hou.SopNode | None:
    """ Find a curve::2.0 node, first check node, otherwise find a child. """
def extractMatrix3(m: hou.Matrix4) -> hou.Matrix3:
    """ Extract the matrix3 part of m. """
def getViewportHandleScaling(scene_viewer: hou.SceneViewer) -> tuple[float, hou.Matrix4]:
    """
    Get some information to help scale handles based on
    their distance from the view camera.

    returns a pair (scale, m_inverted) that are meant
    to be used with the getViewportHandlePScale function
    for returning the amount to scale a point based on its
    position in the viewport.

    :scene_viewer: The scene viewer to use to extract the transforms from.
    """
def getViewportHandlePScale(pos: hou.Vector3, scale: float, m_inverted: hou.Matrix4) -> float:
    """
    Returns a float representing the base amount needed to scale
    a point based on the distance to the viewport camera. The 
    returned scale ensures that the geometry that this is used
    to scale stays the same size regardless of how far it is
    from the viewport camera.

    Pos is the position of the point in space, scale and m_inverted
    are returned by getViewportHandleScaling and are computed
    from the viewport.

    :pos: The position of the handle in the space.
    :scale: The scale as returned by getViewportHandleScaling.
    :m_inverted: The matrix as returned by getViewportHandleScaling.
    """
def snapDir45Degrees(direction: hou.Vector3, basis_rot: hou.Quaternion | None = None) -> hou.Vector3:
    """
    Get the closest direction that is a multiple of 45 degrees
    to the given direction vector.

    :direction: Source direction vector to snap.
    :basis_rot: rotation of basis frame.
    """
def snapDirRelative45Degrees(direction: hou.Vector3, from_direction: hou.Vector3) -> hou.Vector3:
    """
    Gets the closest direction to the 'direction' that is a multiple
    of 45 degrees from the 'from_direction' in the plane formed by
    'direction' and 'from_direction'.

    :direction: The source direction to snap.
    :from_direction: The output direction is some vector in which the angle
        with the 'from_direction' is a multiple of 45 degrees, and lies in the
        same place as the 'from_direction' and the 'direction'.
    """
def getAxisOrthogonalPriority(direction: hou.Vector3, axes: list[hou.Vector3] | None = None) -> list[hou.Vector3]:
    """
    Sorts the axes by how orthogonal they are to the given direction.
    Computes the dot product between the supplied direction and
    each of the axes (or the principal axes if axes=None), returns
    the axes sorted by the dot product in increasing order.

    :direction: The source direction vector.
    :axes: A tuple of the basis vectors.
    """
def getMostOrthogonalAxisPlane(direction: hou.Vector3, plane_orig: hou.Vector3 | None = None) -> tuple[hou.Vector3, hou.Vector3]:
    """
    Returns the plane that is the most orthogonal to the given direction.
    Computes the dot product of the supplied direction to the principal
    axes, finds the axis that has the smallest angle to the direction,
    and uses this axis as the plane normal. Returns a 2-tuple of the
    plane_orig or (0,0,0) if plane_orig=None, and the determined direction.

    :direction: The source direction vector.
    :plane_orig: The plane origin, if None uses (0,0,0).
    """
def getConstructionPlane(scene_viewer: hou.SceneViewer, plane_orig: hou.Vector3 | None = None) -> tuple[hou.Vector3, hou.Vector3] | None:
    """
    Return a 2-tuple of the construction plane origin (or plane_orig
    if plane_orig is not None) and the construction plane normal,
    OR return None if the construction plane is not visible.

    :scene_viewer: The scene viewer.
    :plane_orig: The origin of the plane, uses (0,0,0) if None.
    """
def intersectConstructionPlane(scene_viewer: hou.SceneViewer, orig: hou.Vector3, direction: hou.Vector3, plane_orig: hou.Vector3 | None = None) -> hou.Vector3 | None:
    """
    Return the intersection of the ray defined by (orig, direction)
    with the construction plane (optionally centered at plane_orig if
    not None), OR return None if the construction plane is not visible.

    :scene_viewer: The scene viewer.
    :orig: The origin of the ray to intersect.
    :direction: The direction of the ray to intersect.
    :plane_orig: The origin of the construction plane to intersect with. If None,
        uses the construction plane's defined origin.
    """
def getSnappingNode(snapping_dict: hou._SnappingRay) -> hou.Node | None:
    """
    Return the node of the geometry that was snapped to.

    :snapping_dict: The snapping dict as returned by hou.ViewerEvent.snappingRay()
    """
def getSnappingGeo(snapping_dict: hou._SnappingRay) -> hou.Geometry | None:
    """
    Return the geometry that was snapped to.

    :snapping_dict: The snapping dict as returned by hou.ViewerEvent.snappingRay()
    """
def warnSnapToCurrentNode(scene_viewer: hou.SceneViewer) -> None: ...

class SnapHelper:
    ignore_pts: list[int]
    def __init__(self) -> None: ...
    def addIgnorePoint(self, ptnum: int) -> None: ...
    def clearIgnorePoints(self) -> None: ...
    def isPointAllowed(self, pt: hou.Point) -> bool: ...
    def isPrimAllowed(self, prim: hou.Prim) -> bool: ...
    def isEdgeAllowed(self, p0: hou.Point, p1: hou.Point) -> bool: ...
    def isMidpointAllowed(self, p0: hou.Point, p1: hou.Point) -> bool: ...
    def isBreakpointAllowed(self, vtx: hou.Vertex) -> bool: ...

def getSnappedPos(ui_event: hou.ViewerEvent, scene_viewer: hou.SceneViewer, ref_pos: hou.Vector3 | None = None, snap_helper: SnapHelper | None = None) -> hou.Vector3 | None:
    """
    Check if the ui_event should be snapped, and determines the snapped
    position using the supported snapping options.

    Currently supports snapping to points, primitives, grid edges,
    and grid points.

    :ui_event: The viewer event given to the python state. I.e. kwargs['ui_event'].
    :scene_viewer: The scene viewer.
    :ref_pos: A reference position to use, such as the last position that was picked.
    """
def adjustPosWorldTransform(scene_viewer: hou.SceneViewer, pos: hou.Vector3) -> hou.Vector3:
    """
    Transform a position given in world space into geometry space.

    :scene_viewer: The scene viewer.
    :pos: The position to map.
    """
def adjustVectorWorldTransform(scene_viewer: hou.SceneViewer, vec: hou.Vector3) -> hou.Vector3:
    """
    Transform a vector given in world space into geometry space.

    :scene_viewer: The scene viewer.
    :vec: The vector to map.
    """
def adjustNormalWorldTransform(scene_viewer: hou.SceneViewer, vec: hou.Vector3) -> hou.Vector3:
    """
    Transform a noraml vector given in world space into geometry space.

    NOTE: The difference with this and adjustPosWorldTransform is that this
    multiplies by the inverse transpose of the model to geometry transform.

    :scene_viewer: The scene viewer.
    :vec: The vector to map.
    """
def getViewDirection(scene_viewer: hou.SceneViewer) -> hou.Vector3:
    """
    Get a vector pointing in the view direction.

    :scene_viewer: The scene viewer to use the view matrices from.
    """
def getViewDirectionInGeometrySpace(scene_viewer: hou.SceneViewer) -> hou.Vector3:
    """Return the viewport view direction in the current node's geometry space."""
def getViewBasis(scene_viewer: hou.SceneViewer) -> list[hou.Vector3]:
    """
    Get a basis for the view. This defines the view plane and the view
    plane normal.
    """
def getImagePlaneBasis(layer_xform: hou.Matrix4) -> list[hou.Vector3]: ...
def getConstructionPlaneBasis(scene_viewer: hou.SceneViewer) -> list[hou.Vector3]:
    """
    Get a basis for the construction plane. This defines the construction
    plane axes and its normal.
    """
def getViewOrigin(scene_viewer: hou.SceneViewer) -> hou.Vector3:
    """
    Get a vector representing the view pivot.

    :scene_viewer: The scene viewer to pull the view matrices from.
    """
def getViewOrient(scene_viewer: hou.SceneViewer) -> hou.Quaternion:
    """
    Get a quaternion giving the rotations of the view.

    :scene_viewer: The scene viewer to pull the view matrices from.
    """
def checkPriorityRayIntersect(scene_viewer: hou.SceneViewer, orig: hou.Vector3, direction: hou.Vector3, plane_orig: hou.Vector3 | None = None, ui_event: hou.ViewerEvent | None = None, last_pos: hou.Vector3 | None = None, snap_helper: SnapHelper | None = None) -> hou.Vector3 | None:
    """
    Return the snapped ray position if applicable, otherwise
    return the intersection of the ray defined by (orig, direction)
    with the construction plane with origin at plane_orig or (0,0,0) if
    plane_orig=None.

    If the construction plane is not enabled, and the ray does not snap,
    return None.

    :scene_viewer: The scene viewer.
    :orig: The ray origin.
    :direction: The ray direction.
    :plane_orig: The plane origin, uses (0,0,0) if None.
    :ui_event: The hou.ViewerEvent as returned by kwargs['ui_event'].
    :last_pos: The last pick position, can be used by some snapping options
        such as depth snapping.
    """
def getRayIntersectAxis(scene_viewer: hou.SceneViewer, orig: hou.Vector3, direction: hou.Vector3, plane_orig: hou.Vector3 | None = None, ui_event: hou.ViewerEvent | None = None, last_pos: hou.Vector3 | None = None, snap_helper: SnapHelper | None = None) -> hou.Vector3:
    """
    Intersects the supplied ray with the highest priority feature.

    First checks to see if the ray was snapped to anything, return
    the snapped position if applicable.

    Next checks intersection with the construction plane, return the
    intersection with the construction plane if enabled. The origin of
    the construction plane can be overridden through the plane_orig
    parameter.

    Finally, return the intersection of the ray with the plane with
    normal specified by the principle axes that is most orthogonal
    to the view direction.

    :scene_viewer: The scene viewer.
    :orig: The ray origin.
    :direction: The ray direction.
    :plane_orig: The plane origin, uses (0,0,0) if None.
    :ui_event: The hou.ViewerEvent as returned by kwargs['ui_event'].
    :last_pos: The last pick position, can be used by some snapping options
        such as depth snapping.
    """
def getGuidePlane(scene_viewer: hou.SceneViewer, plane_orig: hou.Vector3 | None = None, ui_event: hou.ViewerEvent | None = None) -> tuple[hou.Vector3, hou.Vector3] | None:
    """
    If the ui_event is snapping, return None.

    Otherwise, if the construction plane is enabled return the
    construction plane (optionally centered at plane_orig if not None)

    Finally, if the construction plane is not enabled, return the
    plane with normal specified by a principle axis that is most
    orthogonal to the view direction.

    :scene_viewer: The scene viewer.
    :plane_orig: The plane origin, uses (0,0,0) if None.
    :ui_event: The hou.ViewerEvent as returned by kwargs['ui_event'].
    """
def getRayIntersectPlane(scene_viewer: hou.SceneViewer, orig: hou.Vector3, direction: hou.Vector3, plane_orig: hou.Vector3 | None = None, plane_normal: hou.Vector3 | None = None, ui_event: hou.ViewerEvent | None = None, last_pos: hou.Vector3 | None = None, snap_helper: SnapHelper | None = None) -> hou.Vector3:
    """
    Intersects the supplied ray with the highest priority feature.

    First checks to see if the ray was snapped to anything, return
    the snapped position if applicable.

    Next checks intersection with the construction plane, return the
    intersection with the construction plane if enabled. The origin of
    the construction plane can be overridden through the plane_orig
    parameter.

    Finally, return the intersection of the ray with the plane with
    normal specified by the view direction and origin specified by
    plane_orig, or (0,0,0) if plane_orig=None.

    :scene_viewer: The scene viewer.
    :orig: The ray origin.
    :direction: The ray direction.
    :plane_orig: The plane origin, uses (0,0,0) if None.
    :ui_event: The hou.ViewerEvent as returned by kwargs['ui_event'].
    :last_pos: The last pick position, can be used by some snapping options
        such as depth snapping.
    """
def getRayIntersectViewPlane(scene_viewer: hou.SceneViewer, orig: hou.Vector3, direction: hou.Vector3, plane_orig: hou.Vector3 | None = None, ui_event: hou.ViewerEvent | None = None, last_pos: hou.Vector3 | None = None, snap_helper: SnapHelper | None = None) -> hou.Vector3:
    """
    Intersects the supplied ray with the highest priority feature.

    First checks to see if the ray was snapped to anything, return
    the snapped position if applicable.

    Next checks intersection with the construction plane, return the
    intersection with the construction plane if enabled. The origin of
    the construction plane can be overridden through the plane_orig
    parameter.

    Finally, return the intersection of the ray with the plane with
    normal specified by the view direction and origin specified by
    plane_orig, or (0,0,0) if plane_orig=None.

    :scene_viewer: The scene viewer.
    :orig: The ray origin.
    :direction: The ray direction.
    :plane_orig: The plane origin, uses (0,0,0) if None.
    :ui_event: The hou.ViewerEvent as returned by kwargs['ui_event'].
    :last_pos: The last pick position, can be used by some snapping options
        such as depth snapping.
    """
def layerXformToImagePlane(layer_xform: hou.Matrix4) -> tuple[hou.Vector3, hou.Vector3]: ...
def getRayIntersectImagePlane(scene_viewer: hou.SceneViewer, orig: hou.Vector3, direction: hou.Vector3, layer_xform: hou.Matrix4, plane_orig: hou.Vector3 | None = None, ui_event: hou.ViewerEvent | None = None, last_pos: hou.Vector3 | None = None, snap_helper: SnapHelper | None = None) -> hou.Vector3: ...
def getRayIntersectDepth(scene_viewer: hou.SceneViewer, orig: hou.Vector3, direction: hou.Vector3, depth: float | None = None, ui_event: hou.ViewerEvent | None = None, last_pos: hou.Vector3 | None = None, snap_helper: SnapHelper | None = None) -> hou.Vector3:
    """
    Intersects the supplied ray with the highest priority feature.

    First checks to see if the ray was snapped to anything, return
    the snapped position if applicable.

    Next checks intersection with the construction plane, return the
    intersection with the construction plane if enabled. The origin of
    the construction plane can be overridden through the plane_orig
    parameter.

    Finally, return the intersection of the ray with the plane with
    normal specified by the view direction and origin that is depth
    away from the view position, or (0,0,0) if depth is None.

    :scene_viewer: The scene viewer.
    :orig: The ray origin.
    :direction: The ray direction.
    :depth: The depth to sample the ray at from the view position.
    :ui_event: The hou.ViewerEvent as returned by kwargs['ui_event'].
    :last_pos: The last pick position, can be used by some snapping options
        such as depth snapping.
    """

class curve3DPicker:
    mode: int
    last_depth: float | None
    last_pos: hou.Vector3 | None
    snap_helper: SnapHelper
    image_layer_xform: hou.Matrix4 | None
    MODE_AXIS_ALIGNED: int
    MODE_CAMERA_ALIGNED: int
    MODE_VIEWPLANE: int
    MODE_IMAGEPLANE: int
    def __init__(self, initial_mode: int = ...) -> None: ...
    def setImagePlane(self, layer_xform: hou.Matrix4) -> None: ...
    def hasImagePlane(self) -> bool: ...
    def setIgnorePoint(self, pt_num: int) -> None: ...
    def addIgnorePoint(self, pt_num: int) -> None: ...
    def clearIgnorePoints(self) -> None: ...
    def reset(self) -> None:
        """ Reset the stored last depth and position info. """
    def setPickMode(self, mode: int) -> None:
        """
        Change the pick mode, if it differs reset the picker.

        :mode: One of MODE_AXIS_ALIGNED, MODE_CAMERA_ALIGNED, MODE_VIEWPLANE.
        """
    def isPlanar(self) -> bool: ...
    def planarBasis(self, scene_viewer: hou.SceneViewer) -> list[hou.Vector3]:
        """
        Return U,V,N where U,V are the basis vectors of the plane
        and N is the normal.
        """
    def planeNormal(self, scene_viewer: hou.SceneViewer) -> hou.Vector3: ...
    def intersect(self, scene_viewer: hou.SceneViewer, rorig: hou.Vector3, rdir: hou.Vector3, ui_event: hou.ViewerEvent | None = None, last_depth: float | None = None, plane_orig: hou.Vector3 | None = None, align_last_pos: bool = True) -> hou.Vector3:
        """
        Intersect using one of the three modes.

        :scene_viewer:
        :rorig:
        :rdir:
        :ui_event: The ui event from the mouse event, used for snapping
                  and construction planes.
        :last_depth: The depth to use in MOVE_CAMERA_ALIGNED. If none,
                    uses the value from the previous intersect call
                    or 0 if reset.
        :plane_orig: The origin of the plane to intersect with in
                    MODE_AXIS_ALIGNED or MODE_VIEWPLANE, if left None
                    uses the previous pick position as the plane_orig,
                    or (0,0,0) if reset.
        :align_last_pos: In MODE_AXIS_ALIGNED or MODE_VIEWPLANE, whether
                        to use the previous pick position as the plane
                        origin and save the position for the next intersect.
        """

def checkPrimClosed(prim: hou.Prim | None) -> bool:
    """
    Shortcut to check if a primitive is closed.

    :prim:
    """
def getCurveOrder(prim: hou.Prim | None) -> int:
    '''
    Shortcut to getting the order of a primitive.
    Will throw a hou.OperationFailed error if the primitive
    does not have an "order" intrinsic attribute.

    :prim:
    '''
def isVertexOpenEndPoint(vtx: hou.Vertex) -> bool:
    """
    Check if the point supplied is an end point of the curve
    primitive that it is a part of, and that this curve is not closed.

    :vtx: The point to check.
    """
def isPointOpenEndpoint(point: hou.Point, allow_branch_points: bool = False) -> bool:
    """
    Check if the point supplied is an end point of the curve
    primitive that it is a part of, and that this curve is not closed.

    :point: The point to check.
    """
def getVertexUOnCurve(vtx: hou.Vertex) -> float:
    """
    Return the U position of a point along a curve.

    :vtx: The point to check.
    """
def getPointUOnCurve(point: hou.Point) -> float:
    """
    Return the U position of a point along a curve.

    :point: The point to check.
    """
def getCurveNumSegments(prim: hou.Prim) -> int:
    """
    Given a curve primitive, return the number of segments in the curve.

    :prim: The primitive in question.
    """
def getFullU(upos: float, prim: hou.Prim) -> float:
    """
    Given a upos in [0,1] on a curve primitive with N segments
    will return upos * N to give a new version of the u position
    in the range [0, N].

    :upos: The source u position.
    :prim: The primitive that upos is valid for.
    """
def getIntersegmentUPos(upos: float, prim: hou.Prim) -> float:
    """
    Given a upos in [0,1] on the curve prim, will return
    a value in the range [0,1] representing the position of
    the upos within the individual segment on the curve that
    the position lies in.

    For example, given a curve with 4 segments (or 5 points) with
    u positions at [0, 0.25, 0.5, 0.75, 1], and a upos=0.4, this
    function will identify that the upos lies in the segment [0.25, 0.5],
    and return the value 0.6=(0.4-0.25)/(0.5-0.25).

    :upos: The source u position.
    :prim: The primitive that upos is valid for.
    """
def getSegmentNum(upos: float, prim: hou.Prim) -> int:
    """
    Given a upos in [0,1] on the curve prim, will return
    the segment number (0 indexed) that the upos lies within
    along the curve.

    :upos: The source u position.
    :prim: The primitive that upos is valid for.
    """
def getCurveAdjacentVertices(upos: float, prim: hou.Prim) -> tuple[hou.Vertex, hou.Vertex] | tuple[None, None]:
    """
    Given a upos in [0,1] on the curve prim, will determine
    the segment that the upos lies within on the curve, and
    return the two vertices (as hou.Vertex objects) at the ends
    of the segment.

    :upos: The source u position.
    :prim: The primitive that upos is valid for.
    """
def getCurveAdjacentPoints(upos: float, prim: hou.Prim) -> tuple[hou.Point, hou.Point] | tuple[None, None]:
    """
    Given a upos in [0,1] on the curve prim, will determine
    the segment that the upos lies within on the curve, and
    return the two points (as hou.Point objects) at the ends
    of the segment.

    :upos: The source u position.
    :prim: The primitive that upos is valid for.
    """
def getCurveSection(upos: float, prim: hou.Prim, ref_geo: hou.Geometry | None = None) -> list[hou.Point]:
    """
    Given a upos in [0,1] on the curve prim,
    return the points forming the section of the
    curve that upos is within.

    Optionally, a ref_geo hou.Geometry can be supplied
    allowing prim to be a polygon primitive even if the
    real primitive is of another type. If ref_geo is given
    then the prim number is looked up in ref_geo and the
    type and order information is taken from there instead.

    :upos: The source u position.
    :prim: The primitive that upos is valid for.
    :ref_geo: Optional reference geometry to pull the type and order from.
    """
def adjacentPointsToVertices(p0: hou.Point, p1: hou.Point) -> tuple[hou.Vertex, hou.Vertex] | tuple[None, None]:
    """
    Return the vertices on the first prim encountered
    for which p0 and p1 are adjacent vertices on the primitive.

    Primitives are visited in the order of the vertices around p0.

    :p0: The first point.
    :p1: The second point.
    """
@typing.overload
def wrapPtsWithMap(pts: set[int], mapping: dict[int, int], with_map: Literal[True]) -> tuple[set[int], dict[int, int]]: ...
@typing.overload
def wrapPtsWithMap(pts: set[int], mapping: dict[int, int], with_map: Literal[False]) -> set[int]: ...
@typing.overload
def wrapPtsWithMap(pts: set[int], mapping: dict[int, int], with_map: bool) -> set[int] | tuple[set[int], dict[int, int]]: ...
@typing.overload
def wrapPtsWithIdentityMap(pts: set[int], with_map: Literal[True]) -> tuple[set[int], dict[int, int]]: ...
@typing.overload
def wrapPtsWithIdentityMap(pts: set[int], with_map: Literal[False]) -> set[int]: ...
@typing.overload
def wrapPtsWithIdentityMap(pts: set[int], with_map: bool) -> set[int] | tuple[set[int], dict[int, int]]: ...
@typing.overload
def updatePtnumsOnPointsDelete(ptnums: Iterable[int], delete_points: Iterable[int], with_map: Literal[False] = ...) -> set[int]: ...
@typing.overload
def updatePtnumsOnPointsDelete(ptnums: Iterable[int], delete_points: Iterable[int], with_map: Literal[True]) -> tuple[set[int], dict[int, int]]: ...
@typing.overload
def updatePtnumsOnPointsDelete(ptnums: Iterable[int], delete_points: Iterable[int], with_map: bool = ...) -> set[int] | tuple[set[int], dict[int, int]]: ...
def getRelativeSegmentVertices(start_arc_vtx: hou.Vertex, offsets: Sequence[int]) -> list[hou.Vertex | None]:
    """
    Get the vertices on the curve relative to the start_arc_vtx.
    Offsets is a list of integers, which can be positive or negative.
    Returns the vertices on the curve that are offset from start_arc_vtx
    by the values in offsets.
    The returned list is in the same order as offsets, and any points
    that are not defined, are still included but will be None.

    :start_arc_vtx: The vertex at the start of the arc.
    :offsets: A list of integer offsets for which vertices on the curve
        relative to the start_arc_vtx to return.
    """
def getRelativeSegmentPoints(start_arc_pt: hou.Point | None, offsets: Sequence[int]) -> list[hou.Point | None]:
    """
    Get the points on the curve relative to the start_arc_pt.
    Offsets is a list of integers, which can be positive or negative.
    Returns the points on the curve that are offset from start_arc_pt
    by the values in offsets.
    The returned list is in the same order as offsets, and any points
    that are not defined, are still included but will be None.

    :start_arc_pt: The point at the start of the arc.
    :offsets: A list of integer offsets for which points on the curve
        relative to the start_arc_pt to return.
    """
def getCutBranchData(geo: hou.Geometry, cut_points: Iterable[int]) -> dict[int, list[tuple[hou.Vertex, int]]]:
    """
    Given a geometry and a list of point numbers for branch points that
    are to be split, get a map of
    point -> [(vertex, new point number) for vertex around point]

    :geo: The geometry.
    :cut_points: The point numbers that are about to the split.
    """
def getBezierAnchorVertex(vtx: hou.Vertex, order: int) -> hou.Vertex:
    """
    Given a vertex on a bezier curve, return the Anchor
    point that this point is linked to.

    :vtx: The hou.Vertex object.
    :order: The order to treat the curve as.
    """
def getBezierAnchorPoint(point: hou.Point, order: int) -> hou.Point:
    """
    Given a point on a bezier curve, return the Anchor
    point that this point is linked to.

    :vtx: The hou.Vertex object.
    :order: The order to treat the curve as.
    """
def isPointBezierAnchor(point: hou.Point, order: int) -> bool:
    """
    Given a point on a bezier curve, return whether the
    point is an anchor point.

    :point: The point in question.
    :order: The order of the bezier curve.
    """
def isPointBezierHandle(point: hou.Point, order: int) -> bool:
    """
    Given a point on a bezier curve, return whether the
    point is a bezier handle point connected to an anchor.

    :point: The point in question.
    :order: The order of the bezier curve.
    """
def isVertexBezierHigherOrderIntermediate(vtx: hou.Vertex, order: int) -> bool:
    """
    Given a vertex on a bezier curve, return whether the
    vertex is an intermediate point on a higher order
    bezier curve.

    :vtx: The vertex in question.
    :order: The order of the bezier curve.
    """
def isPointBezierHigherOrderIntermediate(point: hou.Point, order: int) -> bool:
    """
    Given a point on a bezier curve, return whether the
    point is an intermediate point on a higher order
    bezier curve.

    :point: The point in question.
    :order: The order of the bezier curve.
    """
def evalAutoBezierClosed(anchors: Sequence[hou.Vector3]) -> tuple[list[hou.Vector3], list[hou.Vector3]]:
    """
    Given a list of anchor points on a closed bezier curve.
    Evaluates the C2 continuous bezier curve interpolating
    these anchor points.

    Returns two lists, p1, p2, containing the positions of the
    first and last intermediate control points within each segment
    of the curve.

    :anchors: The list of anchor point positions.
    """
def evalAutoBezier(anchors: Sequence[hou.Vector3], start_p1: hou.Vector3 | None = None, end_p2: hou.Vector3 | None = None) -> tuple[list[hou.Vector3], list[hou.Vector3]]:
    """
    Given a list of anchor points, computes the bezier
    curve that would be created from the auto-draw mode
    on the Curve-2.0 SOP.

    Start_p1 and End_p2 are optional inputs. When left as None,
    the curve will be computed such that there is zero curvature
    at the first and last anchor points. If start_p1 is defined,
    the curve will be computed to go smoothly into the tangent
    defined at the first point by the first anchor and start_p1.
    Similarly, if start_p2 is defined, the curve will be computed
    to go smoothly into the tangent defined at the last point by
    the last anchor and end_p2.

    Return two lists, p1, p2, containing the positions of the
    first and last intermediate control points within each segment
    of the curve.

    The curve is created to be an open bezier curve with C2 continuity
    and with the second derivate equal to 0 at the end points.

    :anchors: List of anchor point positions.
    :start_p1: Optional first tangent position of the first segment.
    :end_p2: Optional last tangent position of final segment.
    """
@typing.overload
def fitCircleStartDir(first_pt: hou.Vector3, second_pt: hou.Vector3, start_tangent_dir: hou.Vector3, output_extra_info: Literal[False] = ...) -> tuple[float, hou.Vector3] | None: ...
@typing.overload
def fitCircleStartDir(first_pt: hou.Vector3, second_pt: hou.Vector3, start_tangent_dir: hou.Vector3, output_extra_info: Literal[True]) -> tuple[float, hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3, bool, float] | None: ...
@typing.overload
def fitCircleStartDir(first_pt: hou.Vector3, second_pt: hou.Vector3, start_tangent_dir: hou.Vector3, output_extra_info: bool = ...) -> tuple[float, hou.Vector3] | tuple[float, hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3, bool, float] | None: ...
@typing.overload
def fitCircleBezier(p0: hou.Vector3, p3: hou.Vector3, start_tangent: hou.Vector3, split_reflex: Literal[False]) -> tuple[hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3] | None: ...
@typing.overload
def fitCircleBezier(p0: hou.Vector3, p3: hou.Vector3, start_tangent: hou.Vector3, split_reflex: bool = ...) -> tuple[hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3] | tuple[hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3, hou.Vector3] | None: ...
def raiseBezierOrder(points: Sequence[hou.Vector3]) -> list[hou.Vector3]:
    """
    Given a bezier segment defined by points, return the points
    defining the an equivalent segment but in a bezier curve with
    one order higher.

    :points: The list of point positions on the bezier curve to raise.
    """
def closestPointsBetweenLines(p1: hou.Vector3, v1: hou.Vector3, p2: hou.Vector3, v2: hou.Vector3) -> tuple[hou.Vector3, float, hou.Vector3, float]:
    """
    Given two lines defined as l1 = p1 + s * v1 and
    l2 = p2 + t * v2, computes the two points on l1 and l2
    that are as close as possible to one another.

    Return a 4-tuple of (x,t,y,s) where x,y are the respective closest
    points on l2 and l1, and t,s are the values such that
    x = p2 + t * v2 and y = p1 + s * v1.

    If v1 and v2 are colinear, return (p1, 0.0, p2, 0.0).

    :p1: A point on the first line.
    :v1: The direction of the first line.
    :p2: A point on the second line.
    :v2: The direction of the second line.
    """
def isHandleBroken(prev_pos: hou.Vector3, center_pos: hou.Vector3, next_pos: hou.Vector3, tolerance: float = 1e-05) -> bool:
    """
    Check if the bezier handle specified by prev_pos, center_pos, and
    next_pos is broken based on whether the lower arm of the handle
    (specified by prev_pos-center_pos) and the upper arm of the handle
    (specified by next_pos-center_pos) are colinear.

    Uses the dot product between the two arms, and returns True if the
    dot product is within tolerance of 1.

    :prev_pos: Initial point position of the handle.
    :center_pos: Center position of the handle.
    :next_pos: Last point position of the handle.
    :tolerance: Floating point tolerance for whether to consider it broken.
    """
def isHandleSmooth(prev_pos: hou.Vector3, center_pos: hou.Vector3, next_pos: hou.Vector3, tolerance: float = 1e-05) -> bool:
    """
    Check if the bezier handle specified by prev_pos, center_pos, and
    next_pos is smooth (not balanced) based on whether the lower arm
    of the handle (specified by prev_pos-center_pos) and the upper arm
    of the handle (specified by next_pos-center_pos) are not balanced.

    Return True if the expected position of next_pos if the handle were
    balanced is more than a distance of tolerance away from the actual
    position of next_pos.

    :prev_pos: Initial point position of the handle.
    :center_pos: Center position of the handle.
    :next_pos: Last point position of the handle.
    :tolerance: Floating point tolerance for whether to consider it smooth.
    """
def symmetricTangent(center_pos: hou.Vector3, opposite_pos: hou.Vector3) -> hou.Vector3:
    """
    Return the tangent position symmetric to opposite_pos about center_pos.

    Informal verification:
    - Symmetry about center requires center be the midpoint of (opposite, result).
    - Midpoint equation: center = (opposite + result) / 2.
    - Solving gives result = 2*center - opposite, implemented below.
    """
def isTangentRetracted(epos: hou.Vector3, cpos: hou.Vector3, tolerance: float = 1e-05) -> bool:
    """ Whether the tangent length is less than some cutoff. """
def isHandleCorner(prev_pos: hou.Vector3 | None, center_pos: hou.Vector3 | None, next_pos: hou.Vector3 | None, tolerance: float = 1e-05) -> bool:
    """
    Check if the handle specified by prev_pos, center_pos, and next_pos
    is a corner (with retracted tangents).

    Return True if the length of at least one side of the handle is
    at most tolerance.

    :prev_pos: Initial point position of the handle.
    :center_pos: Center position of the handle.
    :next_pos: Last point position of the handle.
    :tolerance: Floating point tolerance for whether to consider it a
                retracted corner.
    """
def createBezierHandlesGeometry(handle_pts: Iterable[tuple[hou.Vector3 | None, hou.Vector3 | None, hou.Vector3 | None, bool]]) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry]:
    """
    Given a sequence handle_pts of 4-tuples of (hou.Vector3,hou.Vector3,
    hou.Vector3,boolean) where the first three hou.Vector3 objects
    represent the positions of the points in a handle, where the first
    if the lower arm of the handle, the second if the center position,
    and the third is the upper arm of the handle, and finally the boolean
    in the fourth spot specifies whether the handle is broken or not.

    Return a 3-tuple of three geometries, the first of which
    contiaining the handle lines for the broken handles,
    the second containing the handle lines for the smooth
    handles, and the third containing the end points for all
    of the handles.

    :handle_pts: A list of PseudoHandleTuples.
    """
def computeRoundCornerCenterFromRad(prev_pos: hou.Vector3, p0: hou.Vector3, next_pos: hou.Vector3, radius: float) -> hou.Vector3:
    """
    Compute the center of a rounded corner given the
    previous anchor point position, the next anchor point
    position, the middle anchor point position, and the
    radius of the rounded corner.

    Return the position of the center of the rounded corner.

    :prev_pos: Previous anchor position.
    :p0: Middle anchor position. This is the position of the round corner behind the scenes.
    :next_pos: The next anchor position.
    :radius: The radius of the arc.
    """
def computeRoundCornerCenter(p0: hou.Vector3, p1: hou.Vector3, p2: hou.Vector3, p3: hou.Vector3) -> hou.Vector3:
    """
    Compute the center of a rounded corner given
    the four points defining the shape of the current
    rounded corner bezier segment, p0,p1,p2,p3.

    Return the center of the rounded corner.

    :p0: The first anchor point.
    :p1: The first tangent point.
    :p2: The second tangent point.
    :p3: The second anchor point.
    """
def radiusFromAnchorsAndCenter(previous_anchor: hou.Vector3, arc_start_anchor: hou.Vector3, arc_end_anchor: hou.Vector3, next_anchor: hou.Vector3, desired_center_position: hou.Vector3) -> float:
    """
    Used to compute the changed radius when dragging the rounded corner
    widgets in Curve::2.0. 

    Given four anchor points defining the rounded corner arc and the
    anchor points before and after, along with the position that
    the center widget has been dragged to, keeps the rounded corner
    origin constant, and computes a new radius and center from
    the projected position of desired_center_position to the line
    connecting the rounded corner origin to the previous center position.

    Returns the computed radius.

    :previous_anchor: The previous anchor position.
    :arc_start_anchor: The arc start anchor position.
    :arc_end_anchor: The arc end anchor position.
    :next_anchor: The next anchor position.
    :desired_center_position: The approximate, new center positon.
        I.e. This is to be used while dragging the center to compute the
        new radius.
    """
def findConnectedPoints(sel_str: str, input_geo: hou.Geometry) -> list[int] | None: ...

class Dragger:
    """
    Encapsulates the specialized dragging behaviour used
    in the curve::2.0 state.
    """
    name: str
    scene_viewer: hou.SceneViewer
    end_pos: hou.Vector3
    center_pos: hou.Vector3
    lock_length: float | None
    prev_pos: hou.Vector3
    pos: hou.Vector3 | None
    intersector: curve3DPicker
    plane_orig: hou.Vector3
    is_handle: bool
    use_viewer_state_dragger: bool
    viewer_state_dragger: hou.ViewerHandleDragger | hou.ViewerStateDragger
    last_flag: int | None
    is_dragging: bool
    LOCK_DIR: int
    SNAP_DIR: int
    C_PLANE_HEIGHT: int
    IGNORE: int
    def __init__(self, scene_viewer: hou.SceneViewer, name: str | None = None, is_handle: bool = False) -> None: ...
    def getIntersector(self) -> curve3DPicker:
        """ Get the intersector used to pick points in 3D. """
    def toWorldSpace(self, pos: hou.Vector3) -> hou.Vector3: ...
    def toGeoSpace(self, pos: hou.Vector3) -> hou.Vector3: ...
    def setTransform(self, space_xform: hou.Matrix4) -> None: ...
    def syncModelToGeoTransform(self) -> None: ...
    def startDrag(self, ui_event: hou.ViewerEvent, epos: hou.Vector3, cpos: hou.Vector3 | None = None, plane_orig: hou.Vector3 | None = None, lock_length: float | None = None) -> None:
        """
        Start a regular drag given an end position
        and plane center position.

        :epos: End Pos of handle, and the position being dragged.
        :cpos: Center pos of handle.
        :plane_orig: Intersection plane origin.
        """
    def resetDragRefPositions(self, epos: hou.Vector3, cpos: hou.Vector3 | None) -> None:
        """ End the current drag, start a new one using the same plane origin and lock length. """
    def startDragLockLength(self, ui_event: hou.ViewerEvent, epos: hou.Vector3, cpos: hou.Vector3, plane_orig: hou.Vector3 | None = None) -> None:
        """
        Start a drag with a locked distance between the drag position
        and the center position. The locked distance is taken
        to be ||cpos-epos||.

        :epos: End pos of handle, and position being dragged.
        :cpos: Center pos of handle.
        :plane_orig: Intersection plane origin.
        """
    def curPos(self) -> hou.Vector3 | None:
        """
        Return the current position after the most recent drag
        or None if drag has not been called.
        """
    def curDelta(self) -> hou.Vector3:
        """
        Return the change in position from the most recent call to drag
        and the call prior to it.
        """
    def startEndPos(self) -> hou.Vector3:
        """ Return the end_pos that was initially provided when starting a drag. """
    def startCenterPos(self) -> hou.Vector3:
        """ Return the center_pos that was initially provided when starting a drag. """
    def planeOrigin(self) -> hou.Vector3:
        """
        Return the plane origin that was initially provided when starting
        a drag, or the center position if no plane origin was provided.
        """
    def planeNormal(self) -> hou.Vector3: ...
    def adjustPickedPosition(self, scene_viewer: hou.SceneViewer, flag: int | None = None) -> hou.Vector3:
        """
        Adjusts the picked position in self.pos according to the flag
        sets and returns self.pos.

        :scene_viewer: The scene viewer.
        :flag: How to restrict the drag.
            Dragger.SNAP_DIR -> Snap to 45 degree angles.
            Dragger.LOCK_DIR -> Lock the direction while dragging to only change length.
            Dragger.C_PLANE_HEIGHT -> Only move normal to the construction plane.
        """
    def getIntersectPos(self, scene_viewer: hou.SceneViewer, ui_event: hou.ViewerEvent, flag: int | None = None) -> hou.Vector3:
        """
        Depending on the flag, picks a position in the world using the
        mouse position and any other snapping information.

        Return the picked position.

        :scene_viewer: The scene viewer.
        :ui_event: The viewer event given to the mouse event.
        :flag: How to restrict the drag.
        """
    def drag(self, scene_viewer: hou.SceneViewer, ui_event: hou.ViewerEvent, flag: int | None = None) -> hou.Vector3:
        """
        Update the current position with the new drag event, return
        the updated position.

        If flag=Dragger.SNAP_DIR, will snap the direction of the drag
        to increments of 45 degrees.

        If flag=Dragger.LOCK_DIR, will keep the direction of the drag constant.

        If flag=Dragger.C_PLANE_HEIGHT, will set the drag direction to be
        perpendicular to the construction plane.

        :scene_viewer: The scene viewer.
        :ui_event: The viewer event given to the mouse event.
        :flag: How to restrict the drag.
        """
    def endDrag(self) -> None: ...
    def active(self) -> bool: ...

class KeyManager:
    """ Encapsulates the key management behaviour in curve::2.0. """
    keyReleaseCallback: _KeyCallback | None
    keyPressCallback: _KeyCallback | None
    active_keys: set[int]
    active_modifiers: set[str]
    KEY_A: int
    KEY_SHIFT: str
    KEY_CTRL: str
    def __init__(self) -> None: ...
    def setKeyPressCallback(self, cb: _KeyCallback | None) -> None:
        """ Sets a callback to be called when keys are pressed.
        """
    def setKeyReleaseCallback(self, cb: _KeyCallback | None) -> None:
        """ Sets a callback to be called when keys are released.
        """
    def keysActive(self, keys: Iterable[int] = ..., modifiers: Iterable[str] = ...) -> bool:
        """ Check whether the keys pressed and modifiers pressed
            matches the specified keys and modifiers provided.
        """
    def clearActiveKeys(self) -> None:
        """ Clear all pressed keys and modifiers.
        """
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Called when a key is pressed down or lifted up.
            Return True iff the appropriate callback exists and
            the callback returns true on the event.
        """

class ScreenMapper:
    """
    Class for mapping stuff to the screen
    Often need to map many points, so it makes sense to initialize
    it once, and use multiple times.
    """
    vp: hou.GeometryViewport
    geo_to_world_matx: hou.Matrix4 | None
    def __init__(self, scene_viewer: hou.SceneViewer) -> None: ...
    def mapToScreen(self, pos: hou.Vector3) -> hou.Vector2:
        """ Maps from geometry space to the screen. """

def mapPosScreen(scene_viewer: hou.SceneViewer, pos: hou.Vector3) -> hou.Vector2:
    """
    Map a single position from geometry space to the screen.

    Return the mapped position.

    :scene_viewer: The scene viewer.
    :pos: The source position to map to the screen.
    """

class HighlightPoint:
    """
    A class to help creating a drawable with one or more points
    that can be manually moved and set easily.

    Used for the cursor point in Curve::2.0 when inserting or
    adding new points.
    """
    scene_viewer: hou.SceneViewer
    def __init__(self, scene_viewer: hou.SceneViewer, name: str) -> None: ...
    def buildGeometry(self, npts: int) -> None:
        """
        Build the geometry for these points.

        :npts: Number of points to create in the drawable.
        """
    def rebuildGeometry(self, npts: int) -> None:
        """
        Check if the number of points has changed, and possibly re-build
        the geometry if needed.

        :npts: Number of points to create in the drawable.
        """
    def pointSize(self) -> int:
        """ The point size of the drawable points. """
    def setParams(self, params: hou._DrawableParams) -> None:
        """
        Call to set the parameters for the drawable points.

        :params: The params dict to give to the drawable.
        """
    def show(self, val: bool) -> None:
        """ Call to show or hide the drawable points. """
    def setPosition(self, pos: hou.Vector3) -> None:
        """
        Call with a single hou.Vector3 position to set the
        drawable to be a single point with this position.

        :pos: The position to set for the 0'th point.
        """
    def setPositions(self, posns: Sequence[hou.Vector3]) -> None:
        """
        Call with a list of hou.Vector3 positions to set the
        drawable to have one point for each of these positions.

        :posns: The positions to set for the first len(posns) points.
        """
    def draw(self, draw_handle: int) -> None:
        """ Draw the points. """

class HighlightCurveSection:
    """
    Helper class to encapsulate creating a short curve segment
    that can be used to highlight a single curve segment.
    """
    scene_viewer: hou.SceneViewer
    name: str
    def __init__(self, scene_viewer: hou.SceneViewer, name: str) -> None: ...
    def setBezierSamples(self, n: int) -> None:
        """
        Set the number of resamples used in the segment when
        creating a bezier segment.

        :n: Number of samples.
        """
    def setParams(self, params: hou._DrawableParams) -> None:
        """
        Set the parameters of the curve drawable.

        :params: The params dict for the drawable.
        """
    def show(self, val: bool) -> None:
        """ Show or hide the curve drawable. """
    def recreateGeometry(self, n_pts: int) -> None:
        """
        Re-create the geometry with a new number of points.

        :n_pts: The number of points.
        """
    def setCurveGeometry(self, geo: hou.Geometry, ref_geo: hou.Geometry | None = None) -> None:
        """
        Sets the curve point positions of the segment to use the
        specified segment from geo.

        Optionally a ref_geo can be passed in with a different primitive type
        to geo if geo was possibly converted to a different type.

        :geo: The geometry to use to sample positions.
        :ref_geo: A reference geo incase the type of geo was 'casted', i.e. geo
            was a bezier curve, now is a polyline of the cage polygon for the bezier
            with all of the control vertices, but the type name is no longer bezier.
        """
    def setSection(self, upos: float, prim_num: int) -> None:
        """
        Set the prim number and u position of the segment to create.

        :upos: The u position on the curve that is picked.
        :prim_num: The prim number of the prim that is picked.
        """
    def primNum(self) -> int:
        """Return the cached source primitive number for this section."""
    def draw(self, draw_handle: int) -> None:
        """ Draw the curve drawable. """

class BoxSelector:
    """ Class to encapsulate box selecting in Curve::2.0 state. """
    name: str
    scene_viewer: hou.SceneViewer
    is_selecting: bool
    start_pos: hou.Vector2
    end_pos: hou.Vector2
    start_selection: list[int]
    vp_offset: hou.Vector2
    plane_normal: hou.Vector3
    screen_mapper: ScreenMapper
    def __init__(self, name: str, scene_viewer: hou.SceneViewer) -> None: ...
    def show(self, val: bool) -> None:
        """ Show or hide the box drawable.
        """
    def onEnter(self, kwargs: ViewerStateKwargs) -> None:
        """ Called from onEnter in the state.
        """
    def updateBoxGeo(self, ui_event: hou.ViewerEvent) -> None:
        """ Update the box geometry.
        """
    def draw(self, handle: int) -> None:
        """ Draw the box drawable.
        """
    def clear(self) -> None:
        """ Clear the active box information.
        """
    def startBoxSelect(self, pos: hou.Vector2) -> None:
        """ Start a box selection from the given position.
        """
    def updateBoxSelect(self, pos: hou.Vector2) -> None:
        """ Update the box selection with the end pos at the given position.
        """
    def endBoxSelect(self, pos: hou.Vector2) -> None:
        """ End the box selection with the end pos at the given position.
        """
    def isSelecting(self) -> bool:
        """ Return whether the box is actively selecting.
        """
    def isWorldPosInBox(self, pos: hou.Vector3) -> bool:
        """ Check if a position in geometry space is inside
            the box.
        """
    def mergeExisting(self, pts: list[int], MEkwargs: ViewerStateEventKwargs | None) -> list[int]:
        """ Handle modifier keys and merging the selection with the
            existing selection.

            Return the new selection.
        """
    def getPoints(self, MEkwargs: ViewerStateEventKwargs | None) -> list[int]:
        """ Get the selected points.
        """
    def updateOnMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Call on mouse event, returns true if should consume the mouse event.
            Used to update the box selection once already started.
        """
    def startOnMouseEvent(self, kwargs: ViewerStateEventKwargs) -> None:
        """ Call to start box selecting.
        """
    def getPointNumber(self, point_object: hou.Point) -> int:
        """ Override to provide a method to retrieve the point number
            given the point_object.

            Can be overriden to allow interfacing with objects other than hou.Point
            objects.
        """
    def getPointPosition(self, point_object: hou.Point) -> hou.Vector3:
        """ Override to provide a method to retrieve the point position
            given the point_object.

            Can be overriden to allow interfacing with objects other than hou.Point
            objects.
        """
    def resetSelection(self) -> None:
        """ Override to provide a method to reset the selected
            points.
        """
    def setPointsSelection(self, pts: Sequence[int]) -> None:
        """ Override to provide a method to set the point selection.
        """
    def onSelectionUpdate(self) -> None:
        """ Override to provide a method that is called on a selection
            update.
        """
    def getExistingSelectionPtnums(self) -> list[int]:
        """ Override to provide a method to return the existing
            selection point numbers.
        """
    def addToExisting(self, MEkwargs: ViewerStateEventKwargs | None = None) -> bool:
        """ Exists for backward compatibility."""
    def toggleWithExisting(self, MEkwargs: ViewerStateEventKwargs | None = None) -> bool:
        """ Exists for backward compatibility."""
    def getGeometryPoints(self) -> list[hou.Point]:
        """ Override to provide a method for returning all of the points
            in the target geometry.
        """

class RadialItemType:
    """ Supported types for the addRadialItems function. """
    BUTTON: int
    SETPARM: int
    SCRIPT: int

def runRadialNodeButton(kwargs: RadialMenuKwargs, button: str) -> None:
    """
    Given the kwargs available to a radial menu script, press
    the specified button on the current node.

    If the current node is None or the parameter does not exist
    on the node, this will silently fail.

    :kwargs: The kwargs dict given to the radial menu script.
    :button: The button name on the curve sop node to run.
    """
def runRadialNodeSetParm(kwargs: RadialMenuKwargs, parm: str, val: int | float | str | dict[str, str] | hou.Parm | hou.Ramp | hou.Geometry) -> None:
    """
    Given the kwargs available to a radial menu script, set the
    value of the specified parameter on the current node to
    the provided value.

    If the current node is None or the parameter does not exist
    on the node, this will silently fail.

    :kwargs: The kwargs dict given to the radial menu.
    :parm: The parm on the sop node to set.
    :val: The value to set the parm to.
    """
def addRadialItems(menu: hou.RadialMenu, items: Iterable[_RadialItem]) -> None:
    '''
    Populate a python radial menu with items.

    Each item has a "type" keyword argument which can be
    one of RadialItemType.BUTTON, RadialItemType.SETPARM,
    or RadialItemType.SCRIPT.

    Each item also has an argument for the location in the radial menu, "loc",
    an argument for the label, "label", and an argument for the icon, "icon".

    BUTTON items have an argument for "parm", which is the button on the
    node to press when this radial item is activated.

    SETPARM items have an argument "parm" for the parameter and "value" for the value
    to set the parameter when the radial item is activated.

    SCRIPT items have an argument "script" which is a string of python code to be
    evaluated when the radial item is activated. The script is provided with a
    kwargs dictionary containing the node.

    :menu: The radial menu to add items to.
    :items: A dictionary of item definitions as described above.
    '''
def constructRotationRingGeometry(scale: float = 1.125, gap: float = 0.05) -> hou.Geometry:
    """
    Create the geometry for the rotation rings used in the curve orient mode.

    Creates two arcs with arrows on the ends.

    :scale: The scale of the geometry.
    :gap:  Defines a gap between the arcs.
    """
PickPointEventDict = dict[str, PickPointResultType]
PickHandleLineEventDict = dict[str, PickHandleLineResultType]
PickCurveEventDict = dict[str, PickCurveResultType]
PickRoundCornerEventDict = dict[str, PickRoundCornerResultType]
PickFaceEventDict = dict[str, PickFaceResultType]

class BaseHandleWrapper(Generic[_GadgetStateT_co]):
    """ A base class for many of the interactive widgets in the Curve::2.0 state. """
    gadget_name: str
    scene_viewer: hou.SceneViewer
    main_state: _GadgetStateT_co
    node: hou.SopNode | None
    color_options: ru.ColorOptions
    def __init__(self, gadget_name: str, scene_viewer: hou.SceneViewer, main_state: _GadgetStateT_co, drawable_type: hou.EnumValue[hou.drawableGeometryType]) -> None: ...
    def drawables(self, include_inactive: bool = True) -> list[hou.SimpleDrawable | hou.AdvancedDrawable]:
        """ Get the drawables included in this wrapper. """
    def activeDrawables(self) -> list[hou.SimpleDrawable | hou.AdvancedDrawable]:
        """ Get only the interactive drawables. """
    def setNeedsRay(self, val: bool) -> None:
        """
        Set to true if the gadget need to send a ray when
        picking the position.

        :val: Whether self.checkHoverHandle requires a ray to function.
        """
    def setCallback(self, cb: _PickCallback) -> None:
        """ Set a callback that will be called when the widget is picked. """
    def setDoubleClickCallback(self, cb: _PickCallback) -> None:
        """ Set a callback to be used on double click events. """
    def pointSize(self) -> int:
        """ The point size of drawable points. """
    def lineWidth(self) -> int:
        """ The line width of drawable lines. """
    def setNode(self, node: hou.SopNode) -> None:
        """ Set the active node. """
    def name(self) -> str:
        """ Return the gadget name. """
    def initialize(self) -> None:
        """ Call after creating the object. """
    def show(self, val: bool) -> None:
        """ Show or hide the drawables. """
    def setEnableInteraction(self, val: bool) -> None:
        """ Set whether the widget can be interacted with or not. """
    def setParams(self, active_params: hou._DrawableParams, inactive_params: hou._DrawableParams) -> None:
        """
        Set the parameters for the active and inactive drawables.

        :active_params: The params dict to pass to the active drawable.
        :inactive_params: The params dict to pass to the inactive drawable.
        """
    def isActiveGadget(self) -> bool:
        """ Return whether this gadget is currently being picked. """
    def draw(self, draw_handle: int) -> None:
        """ Draw this object. Uses the provided getGeometry() function. """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Called on mouse events, checks whether this object is hovered. """
    def onMouseDoubleClickEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Called when this object is double clicked. """
    def getGeometry(self) -> hou.Geometry | None:
        """ Override to provide the geometry for this object. """
    def checkHoverHandle(self, ray_orig: hou.Vector3 | None = None, ray_dir: hou.Vector3 | None = None) -> hou.Point | tuple[hou.Point, hou.Point, float, hou.Vector3] | tuple[hou.Prim, float, hou.Vector3] | tuple[hou.Point, hou.Vector3] | tuple[hou.Prim, hou.Vector3, hou.Vector3] | tuple[hou.Prim, None, None] | None:
        """
        Override to provide a method for checking if the object is
        being hovered over.

        :ray_orig: The origin of the ray. Can be None for some types if its not needed.
        :ray_dir: The direction of the ray. Can be None for some types if its not needed.
        """

def findNURBSStart(prim: hou.Prim, u: float, start: int = -1) -> int:
    """
    Find the start knot index being used in the
    evaluation of the position u on the curve.

    :prim: The NURBs prim.
    :u: The u position we are evaluating.
    :start: The start position, if -1 uses order-1.
    """
def findNURBSValidStart(prim: hou.Prim, u: float, off: int = -1) -> int:
    """
    Given a u position on the curve, return the
    start knot index being used.

    :prim: The NURBs prim.
    :u: The u position we are evaluating.
    :off: The value of findNURBSStart(prim, u).
    """
def getCVRangeOfDomain(prim: hou.Prim, u: float, wrap_cv: bool = True) -> tuple[int, int]:
    """
    Given a NURBs curve and u position, find the start
    and end control vertices (indexes into the curve)
    that influence this u position.

    :prim: The NURBS Prim.
    :u: The u position we are interested in finding the range of control vertices
        that affect this position of the curve.
    :wrap_cv: Whether to wrap the control vertex indices around when they go past nvtx.
    """
def pickPointDrawable(c1: int, drawable: hou.GeometryDrawable, point_lookup: Callable[[hou.Point], hou.Point | None]) -> hou.Point | None:
    """
    Given a pick index on the point drawable, and a lookup
    function mapping points on the drawable to points in some
    other full geometry, return the picked point in the full
    geometry.

    :c1: The point number in the drawable's geometry.
    :drawable: The drawable.
    :point_lookup: The function mapping points from drawable.geometry() to some
        other geometry.
    """
def rayToLine(p0: hou.Vector3, p1: hou.Vector3, ray_orig: hou.Vector3, ray_dir: hou.Vector3) -> tuple[float, hou.Vector3]:
    """
    Given two points defining a line segment, and a ray, return (t,x), representing
    the closest point on the line segment to the ray. Where t in [0,1] is the
    fraction along the line segment, with p0 at t=0 and p1 at t=1,
    and x is the hou.Vector3 giving the actual position between p0 and p1.

    :p0: The first point on the line segment.
    :p1: The second point on the line segment.
    :ray_orig: The origin of the ray.
    :ray_dir: The direction of the ray.
    """
def edgeEndFromStart(p0: hou.Point | None) -> hou.Point | None:
    """
    Given a point at the start of an edge (where the points have only
    a single vertex), return the point at the end of the edge.
    """
def pickLineDrawable(c1: int, c2: int | None, ray_orig: hou.Vector3, ray_dir: hou.Vector3, drawable: hou.GeometryDrawable, point_lookup: Callable[[hou.Point], hou.Point | None]) -> tuple[hou.Point, hou.Point, float, hou.Vector3] | None:
    """
    Given pick indices, a ray, a line drawable and a function mapping points
    on the drawable to points in some superset geometry, return a 4-tuple
    (p0,p1,t,x) where p0,p1 are the points on the line segment that is picked,
    and (t,x) define where on the line segment is closest to the cursor.

    :c1: The first pick index.
    :c2: The second pick index, or None.
    :ray_orig: The origin of the ray.
    :ray_dir: The direction of the ray.
    :drawable: The line drawable.
    :point_lookup: A function mapping points on the drawables geometry to
        points in some superset geometry.
    """
def pickFaceDrawable(c1: int, ray_orig: hou.Vector3, ray_dir: hou.Vector3, drawable: hou.GeometryDrawable, prim_lookup: Callable[[hou.Prim], hou.Prim]) -> tuple[hou.Prim, hou.Vector3, hou.Vector3] | tuple[hou.Prim, None, None] | None:
    """
    Given a pick index on a face drawable, a ray, the face drawable, and
    function mapping primitives on the drawable to prims in some superset
    geometry, return a 3-tuple of (prim, uwv, pos) of the prim being picked,
    the uvw pos on the prim, and the hou.Vector3 pos.

    :c1: The index of the prim in drawable.
    :ray_orig: The origin of the ray.
    :ray_dir: The direction of the ray.
    :drawable: The drawable.
    :prim_lookup: The lookup function mapping prims on the drawable to prims
        in some superset geometry.
    """
def pickCurveDrawable(c1: int, c2: int | None, ray_orig: hou.Vector3, ray_dir: hou.Vector3, drawable: hou.GeometryDrawable, prim_lookup: Callable[[hou.Prim], hou.Prim | None], vtx_upos_lookup: Callable[[hou.Vertex], float]) -> tuple[hou.Prim, float, hou.Vector3] | None:
    """
    Given pick indices c1,c2 on the line drawable, a ray and functions mapping
    prims in the drawable geometry to prims in a superset geometry, and a
    function to lookup accurate u-positions of vertices on the curve,
    return a 3-tuple of (prim, upos, pos) giving the pick position on the
    curve.

    :c1: The index of the first point on the segment being picked.
    :c2: The index of the second point on the segment being picked, or None.
    :ray_orig: The origin of the ray.
    :ray_dir: The direction of the ray.
    :drawable: The line drawable for the curves.
    :prim_lookup: A function mapping prims in the drawable geometry to
        prims in some superset geometry.
    :vtx_upos_lookup: A function mapping vertices in the drawable geometry
        to u positions.
    """

class BasePointHandle(BaseHandleWrapper[_GadgetStateT_co]):
    """ Base class for interactive point widgets in the Curve::2.0 state. """
    def __init__(self, gadget_name: str, scene_viewer: hou.SceneViewer, main_state: _GadgetStateT_co) -> None: ...
    def setParams(self, active_params: hou._DrawableParams, inactive_params: hou._DrawableParams) -> None:
        """ Set the parameters for the active and inactive drawables. """
    def checkHoverHandle(self, ray_orig: hou.Vector3 | None = None, ray_dir: hou.Vector3 | None = None) -> hou.Point | None:
        """
        Determine if the points in this widget are being picked.

        If not being picked or there is an error, return None.

        Otherwise, return the point (as a hou.Point object)
        that is being picked.
        """
    def getFullGeoPoint(self, handle_geo_point: hou.Point) -> hou.Point | None:
        """
        Override to provide a method for looking up the
        point in the full geometry.

        This is necessary because usually the drawable's geometry
        is a subset of the full geometry.

        :handle_geo_point: The point object in the drawable geometry.
        """

class BezierHandleLines(BaseHandleWrapper[_GadgetStateT_co]):
    """
    Class to encapsulate the creation of Bezier Handle Line widgets.

    This is a non-python handle version of interactible bezier handle lines.

    This is also used to create the pseudo handles in Curve::2.0 that show bezier
    handles but have the interactibility turned off.
    """
    def __init__(self, gadget_name: str, scene_viewer: hou.SceneViewer, main_state: _GadgetStateT_co) -> None: ...
    def initialize(self) -> None:
        """ Called after constructing the object. """
    def checkHoverHandle(self, ray_orig: hou.Vector3 | None = None, ray_dir: hou.Vector3 | None = None) -> tuple[hou.Point, hou.Point, float, hou.Vector3] | None:
        """
        Determine the handle line (defined by the end points),
        and the position along the handle that was picked.

        Returns a 4-tuple, (p1, p2, t, x), where p1, p2 are the two
        points defining the line, t is a value [0,1] giving how
        far the picked position was from p1 to p2, and x is the picked
        position.

        Return None if not picked.
        """
    def getFullGeoPoint(self, handle_geo_point: hou.Point) -> hou.Point | None:
        """ Override to provide a mapping between points in the geometry
            used for these lines, and the full geometry.

            Such a mapping is often necessary because the geometry is likely
            a subset of the full geometry.
        """

class BezierHandlePoints(BasePointHandle[_GadgetStateT_co]):
    """
    Class to encapsulate creation of the widget for the end
    points of bezier handles.
    """
    def initialize(self) -> None:
        """ Called after the construction of the object. """

class RoundedCornerWidgetPoints(BasePointHandle[_GadgetStateT_co]):
    """ Class to encapsulate the rounded corner widgets. """
    def initialize(self) -> None:
        """ Called after construction of the object. """
    def checkHoverHandle(self, ray_orig: hou.Vector3 | None = None, ray_dir: hou.Vector3 | None = None) -> tuple[hou.Point, hou.Vector3] | None:
        """ Return the rounded corner point that is being interacted with. """

class BaseFaceHandle(BaseHandleWrapper[_GadgetStateT_co]):
    """
    Encapsulates the creation of interactible face widgets using face
    gadget drawables.
    """
    def __init__(self, gadget_name: str, scene_viewer: hou.SceneViewer, main_state: _GadgetStateT_co) -> None: ...
    def checkHoverHandle(self, ray_orig: hou.Vector3 | None = None, ray_dir: hou.Vector3 | None = None) -> tuple[hou.Prim, hou.Vector3, hou.Vector3] | tuple[hou.Prim, None, None] | None:
        """ Return the prim, the uvw pos on the prim and the pick position if valid. """
    def getRealGeoPrim(self, prim: hou.Prim) -> hou.Prim:
        """
        Override to provide a method of converting the internal gadget
        geometry primitive to a primitive in your reference geometry.

        This is used when picking parts of the geometry to map the selected
        geometry back to something more useful.
        """

class BackboneCurveHandle(BaseHandleWrapper[_GadgetStateT_co]):
    """ Encapsulate the creation of the interactible curve drawable in curve::2.0. """
    def __init__(self, gadget_name: str, scene_viewer: hou.SceneViewer, main_state: _GadgetStateT_co) -> None: ...
    def initialize(self) -> None:
        """ Called after constructing the object. """
    def checkHoverHandle(self, ray_orig: hou.Vector3 | None = None, ray_dir: hou.Vector3 | None = None) -> tuple[hou.Prim, float, hou.Vector3] | None:
        """
        If picked, return a 3-tuple (prim, upos, x) containing the picked primitive,
        the U position on the primitive and the position in geometry space
        that was picked.

        Otherwise, return None if not picked.
        """
    def getRealGeoPrim(self, handle_geo_prim: hou.Prim) -> hou.Prim:
        """
        Override to provide a method for returning the real geometry's primitive
        given a primitive. This is necessary because often the geometry used for the
        drawable is a resampled version of the real geometry. To get the real
        points in the geometry, it needs to map the primitives back to the non-resampled
        versions.
        """
    def getPointUpos(self, point: hou.Point) -> float:
        """
        Override to provide a method for getting the u position of a point
        along the curve.

        :point: The point to get the upos of.
        """
    def getVertexUpos(self, vertex: hou.Vertex) -> float:
        """
        Override to provide a method for getting the u position of a vertex
        along the curve.

        :vertex: The vertex to get the upos of.
        """

class CurveControlPointHandle(BasePointHandle[_GadgetStateT_co]):
    """ Encapsulate the creation of the widgets for control points on the curve. """
    def initialize(self) -> None:
        """ Called after constructing the object. """

class ControlPointHandleBundle(BaseHandleWrapper[_GadgetStateT_co]):
    """
    Encapsulates a bundle of control point handles. Wraps any number
    of control point handles together to allow them to act as one unit.
    """
    scene_viewer: hou.SceneViewer
    color_options: ru.ColorOptions
    main_state: _GadgetStateT_co
    node: hou.SopNode | None
    class BezierSubHandle(CurveControlPointHandle[_GadgetState]):
        parent_handle: ControlPointHandleBundle[_GadgetState]
        def __init__(self, gadget_name: str, scene_viewer: hou.SceneViewer, main_state: _GadgetState, parent_handle: ControlPointHandleBundle[_GadgetState]) -> None: ...
        def getGeometry(self) -> hou.Geometry | None:
            """ Get the geometry for this sub handle. """
        def getFullGeoPoint(self, handle_geo_point: hou.Point) -> hou.Point | None:
            """ Get the full geometry point corresponding to this point. """
    registered_handles: dict[str, ControlPointHandleBundle.BezierSubHandle]
    def __init__(self, scene_viewer: hou.SceneViewer, main_state: _GadgetStateT_co, handle_names: Iterable[str]) -> None: ...
    def drawables(self, include_inactive: bool = True) -> list[hou.SimpleDrawable | hou.AdvancedDrawable]:
        """ Get the drawables included in this wrapper. """
    def activeDrawables(self) -> list[hou.SimpleDrawable | hou.AdvancedDrawable]:
        """ Get only the interactive drawables. """
    def setCallback(self, cb: _PickCallback) -> None:
        """ Set the regular callback to use. """
    def setDoubleClickCallback(self, cb: _PickCallback) -> None:
        """ Specify the double click callback to use. """
    def setNode(self, node: hou.SopNode) -> None:
        """ Set the sop node. """
    def setParams(self, handle_name: str, active_params: hou._DrawableParams, inactive_params: hou._DrawableParams) -> None:  # type: ignore[override]
        """
        Set the active and inactive params on the drawables for the given sub handle.

        :handle_name: The name of the sub handle.
        :active_params: The dict of active drawable params.
        :inactive_params: The dict of inactive drawable params.
        """
    def initialize(self) -> None:
        """ Called after constructing the object. """
    def show(self, val: bool) -> None:
        """ Show or hide the drawables. """
    def setEnableInteraction(self, val: bool) -> None:
        """ Set whether to allow interacting with these widgets. """
    def isActiveGadget(self) -> bool:
        """ Return true if either of the widgets is being picked. """
    def draw(self, draw_handle: int) -> None:
        """ Draw the point drawables. """
    def getSubGeometry(self, h: BezierSubHandle) -> hou.Geometry | None:
        """
        Return the sub geometry based on the name of the interacted gadget.

        :h: The sub-handle to get the geometry from.
        """
    def checkHoverHandle(self, ray_orig: hou.Vector3 | None = None, ray_dir: hou.Vector3 | None = None) -> hou.Point | None:
        """
        Determine if the points in this widget are being picked.

        If not being picked or there is an error, return None.

        Otherwise, return the point (as a hou.Point object)
        that is being picked.
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Called on mouse events, checks whether this object is hovered. """
    def onMouseDoubleClickEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Called when this object is double clicked. """
    def getGeometry(self, handle_name: str) -> hou.Geometry | None:
        """
        Override to provide a method for retrieving the geometry
        for a given registered point type.
        """
    def getFullGeoPoint(self, handle_geo_point: hou.Point) -> hou.Point | None:
        """
        Override to provide a method for looking up the
        point in the full geometry.

        This is necessary because usually the drawable's geometry
        is a subset of the full geometry.
        """

class BezierControlPointHandle(ControlPointHandleBundle[_GadgetStateT_co]):
    """
    Encapsulate the special behaviour of the bezier control points.
    Wraps two widgets into one, one for the broken control points,
    and one for the smooth control points.

    Exists for backwards compatibility.
    """
    broken_pt_handle: ControlPointHandleBundle.BezierSubHandle
    smooth_pt_handle: ControlPointHandleBundle.BezierSubHandle
    def __init__(self, smooth_handle_name: str, broken_handle_name: str, scene_viewer: hou.SceneViewer, main_state: _GadgetStateT_co) -> None: ...
    def getGeometry(self, handle_name: str) -> hou.Geometry | None:
        """ Get geometry for the given sub handle. """
    def getSmoothGeometry(self) -> hou.Geometry | None:
        """
        Override to provide a method for retrieving the smooth
        control points geometry.
        """
    def getBrokenGeometry(self) -> hou.Geometry | None:
        """
        Override to provide a method for retrieving the broken
        control points geometry.
        """

class LineHandleBundle(BaseHandleWrapper[_GadgetStateT_co]):
    """
    Encapsulates a bundle of handle lines. Wraps any number of line widgets
    into one interactible bundle.
    """
    scene_viewer: hou.SceneViewer
    color_options: ru.ColorOptions
    main_state: _GadgetStateT_co
    node: hou.SopNode | None
    class SubBezierLine(BezierHandleLines[_GadgetState]):
        parent_handle: LineHandleBundle[_GadgetState]
        def __init__(self, gadget_name: str, scene_viewer: hou.SceneViewer, main_state: _GadgetState, parent_handle: LineHandleBundle[_GadgetState]) -> None: ...
        def getFullGeoPoint(self, handle_geo_point: hou.Point) -> hou.Point | None: ...
        def getGeometry(self) -> hou.Geometry | None: ...
    registered_handles: dict[str, LineHandleBundle.SubBezierLine]
    def __init__(self, scene_viewer: hou.SceneViewer, main_state: _GadgetStateT_co, handle_names: Iterable[str]) -> None: ...
    def drawables(self, include_inactive: bool = True) -> list[hou.SimpleDrawable | hou.AdvancedDrawable]:
        """ Get the drawables included in this wrapper. """
    def activeDrawables(self) -> list[hou.SimpleDrawable | hou.AdvancedDrawable]:
        """ Get only the interactive drawables. """
    def setCallback(self, cb: _PickCallback) -> None:
        """ Set the callback that is called on a mouse event. """
    def setDoubleClickCallback(self, cb: _PickCallback) -> None:
        """ Set the callback that is called on a double click event. """
    def setNode(self, node: hou.SopNode) -> None:
        """ Set the sop node. """
    def setParams(self, handle_name: str, active_params: hou._DrawableParams, inactive_params: hou._DrawableParams) -> None:  # type: ignore[override]
        """
        Set the active and inactive drawable params for this sub handle.

        :handle_name: The name of the sub handle.
        :active_params: The active parameters dict.
        :inactive_params: The inactive parameters dict.
        """
    def initialize(self) -> None:
        """ Called after constructing the object. """
    def show(self, val: bool) -> None:
        """ Show or hide the drawables. """
    def setEnableInteraction(self, val: bool) -> None:
        """ Set whether to allow interacting with these widgets. """
    def isActiveGadget(self) -> bool:
        """ Return true if either of the widgets is being picked. """
    def draw(self, draw_handle: int) -> None:
        """ Draw the line drawables. """
    def getSubGeometry(self, h: SubBezierLine) -> hou.Geometry | None:
        """
        Return the sub geometry based on the name
        of the interacted gadget.

        :h: The sub-handle object.
        """
    def checkHoverHandle(self, ray_orig: hou.Vector3 | None = None, ray_dir: hou.Vector3 | None = None) -> tuple[hou.Point, hou.Point, float, hou.Vector3] | None:
        """
        Determine the handle line (defined by the end points),
        and the position along the handle that was picked.

        Returns a 4-tuple, (p1, p2, t, x), where p1, p2 are the two
        points defining the line, t is a value [0,1] giving how
        far the picked position was from p1 to p2, and x is the picked
        position.

        Return None if not picked.
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Called on mouse events, checks whether this object is hovered. """
    def onMouseDoubleClickEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Called when this object is double clicked. """
    def getGeometry(self, handle_name: str) -> hou.Geometry | None:
        """
        Override to provide a method for retrieving the handle geometry
        by the handle_name.
        """
    def getFullGeoPoint(self, handle_geo_point: hou.Point) -> hou.Point | None:
        """
        Override to provide a mapping between points in the geometry
        used for these lines, and the full geometry.

        Such a mapping is often necessary because the geometry is likely
        a subset of the full geometry.
        """

class BezierLineWrapper(LineHandleBundle[_GadgetStateT_co]):
    """
    Encapsulate the specialized behaviour of bezier handle lines.
    Wraps two widgets into one, one for the broken handle lines, and
    one for the smooth handle lines.

    Exists for backwards compatibility.
    """
    smooth_line_handle: LineHandleBundle.SubBezierLine
    broken_line_handle: LineHandleBundle.SubBezierLine
    def __init__(self, smooth_handle_name: str, broken_handle_name: str, scene_viewer: hou.SceneViewer, main_state: _GadgetStateT_co) -> None: ...
    def getGeometry(self, handle_name: str) -> hou.Geometry | None:
        """ Get the geometry for the given sub-handle. """
    def getSmoothLineGeometry(self) -> hou.Geometry | None:
        """
        Override to provide a method for retrieving the smooth
        control points geometry.
        """
    def getBrokenLineGeometry(self) -> hou.Geometry | None:
        """
        Override to provide a method for retrieving the broken
        control points geometry.
        """

class PointSelectorBundle(Generic[_StateT_co]):
    """ Encapsulate the selected point visualization. """
    scene_viewer: hou.SceneViewer
    main_state: _StateT_co
    color_options: ru.ColorOptions
    registered_drawables: dict[str, hou.GeometryDrawable]
    node: hou.SopNode | None
    def __init__(self, scene_viewer: hou.SceneViewer, main_state: _StateT_co, names: Iterable[str]) -> None: ...
    def setNode(self, node: hou.SopNode) -> None:
        """ Set the sop node. """
    def pointSize(self) -> int:
        """ Get point size for the drawable. """
    def setParams(self, name: str, params: hou._DrawableParams) -> None:
        """
        Set params for the drawable with the given name.

        :name: The name of the drawable.
        :params: The params to set for this drawable.
        """
    def initialize(self) -> None:
        """ Called after constructing the object. """
    def show(self, val: bool) -> None:
        """ Show or hide the drawables. """
    def draw(self, draw_handle: int) -> None:
        """ Draw the selected points. """
    def getGeometry(self, drawable_name: str) -> hou.Geometry | None:
        """
        Override to provide a method for retrieving the geometry for
        each of the drawables by name.

        :drawable_name: The drawable name to lookup the geometry for.
        """

class BezierPointSelector(PointSelectorBundle[_StateT_co]):
    """
    Encapsulate the selected point visualization.

    This exists for backwards compatibility.
    """
    broken_name: str
    smooth_name: str
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _StateT_co) -> None: ...
    def setSmoothParams(self, params: hou._DrawableParams) -> None:
        """ Set params for the smooth points drawable. """
    def setBrokenParams(self, params: hou._DrawableParams) -> None:
        """ Set params for the broken points drawable. """
    def getGeometry(self, drawable_name: str) -> hou.Geometry | None:
        """
        Get the geometry for the given drawable.

        :drawable_name: The name of the drawable to grab the geo for.
        """
    def getBrokenSelectGeometry(self) -> hou.Geometry | None:
        """ Get the geometry for the selected broken points. """
    def getSmoothSelectGeometry(self) -> hou.Geometry | None:
        """ Get the geometry for the selected smooth points. """
