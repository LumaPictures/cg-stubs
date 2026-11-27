import curveutils as cu
import hou
import resourceutils as ru
import typing
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from curvestate import constants as constants
from curvestate.baseoperation import BaseSubTool as BaseSubTool
from typing import Literal, Protocol

from typing import TypeAlias
from typing import TypeVar
from typing import TypeVar
_K = TypeVar('_K')
_DK = TypeVar('_DK', default=int)
_DV = TypeVar('_DV', default=float)
_PointAttribValue: TypeAlias = hou.AttribReturnType | hou._OptionDict | tuple[hou._OptionDict, ...]
PointMoveData: TypeAlias = tuple[int, hou.Vector3]
class _CurveState(Protocol):
    @property
    def node(self) -> hou.SopNode | None: ...
    @property
    def scene_viewer(self) -> hou.SceneViewer: ...
    @property
    def color_options(self) -> ru.ColorOptions: ...
    def getNodeReferenceCurveGeometry(self) -> hou.Geometry | None: ...
    def getNodeInputGeometry(self) -> hou.Geometry | None: ...
    def activeOperation(self) -> BaseSubTool: ...
    def getSelectionPtNums(self) -> list[int]: ...
    def getSelectionString(self) -> str: ...
    def clearCachedPtnums(self) -> None: ...
ActiveHandleTuple = tuple[int | None, int | None, int | None]
PRIMIDX_ATTRIB: str
PTPRIMIDX_ATTRIB: str
PTIDX_INPRIM_ATTRIB: str
PRE_PTNUM_ATTRIB: str
PRIM_LASTIDX_ATTRIB: str
CURVEUPOS_ATTRIB: str
CURVENUM_ATTRIB: str
CURVETANGENT_ATTRIB: str
CURVEUP_ATTRIB: str
CURVEORIENT_ATTRIB: str
ANCHORPTS_ATTRIB: str
ANCHORPTS_GROUP: str
BROKENPTS_GROUP: str
SMOOTHPTS_GROUP: str
AUTOPTS_GROUP: str
ROUNDCORNERPTS_GROUP: str
SELECTEDPTS_GROUP: str
ACTIVEPRIM_GROUP: str
POLYPRIMS_GROUP: str
POLYPTS_GROUP: str
NURBSPRIMS_GROUP: str
NURBSPTS_GROUP: str
BEZIERPRIMS_GROUP: str
BEZIERPTS_GROUP: str

def colorToVector4(col: hou.Color) -> hou.Vector4: ...
def getSelectColor(color_options: ru.ColorOptions) -> hou.Color: ...
def getPointColor(color_options: ru.ColorOptions) -> hou.Color: ...
def getAnchorLocateColor(color_options: ru.ColorOptions) -> hou.Color: ...
def getHandleLocateColor(color_options: ru.ColorOptions) -> hou.Color: ...
def getHandleColor(color_options: ru.ColorOptions) -> hou.Color: ...
def getInactiveHandleColor(color_options: ru.ColorOptions) -> hou.Color: ...
def getBranchColor(color_options: ru.ColorOptions) -> hou.Color: ...
def getEndColor(color_options: ru.ColorOptions) -> hou.Color: ...
def getBranchEndColor(color_options: ru.ColorOptions) -> hou.Color: ...
def getAutoPointRingColor(color_options: ru.ColorOptions) -> hou.Color: ...
def getLocateCurveColor(color_options: ru.ColorOptions) -> hou.Color: ...

class UpdateBlock:
    """
    Used in the ReferenceCurve class to disable updates while
    updating to prevent infinite recursion.
    """
    def __init__(self, holder: ReferenceCurve) -> None: ...
    def __enter__(self) -> None:
        """ Called when a with block is entered. """
    def __exit__(self, *args: object) -> None:
        """ Called when a with block is exited. """

def pointInternalPtnum(point: hou.Point) -> int:
    """
    Return the real point number that the point is derived from.
    Many of the internal geometry representations are only subsets
    of the full geometry. This is used to map the points in these
    geometries back to the full geometry.

    :point: The point to look up the internal point number on.
    """
def pointsInternalPtnums(points: Iterable[hou.Point]) -> list[int]:
    """
    From the list of points, return the respective list of point
    numbers in the full detail.

    :points: The list of points.
    """
def getInternalPtnums(geo: hou.Geometry | None, ptnums: Iterable[int]) -> list[int]:
    """
    Given a list of point numbers in a sub detail and a detail,
    return the list of point numbers in the full detail.

    :geo: The sub geometry to lookup point numbers in.
    :ptnums: The source list of point numbers in geo.
    """
def getFullGeoPoint(point: hou.Point, full_geo: hou.Geometry | None) -> hou.Point | None:
    """
    Given a point, possibly in a subgeo, return the corresponding
    point in the full geometry.

    See pointInternalPtnum.

    :point: The point to look up.
    """
def getFullGeoPrim(prim: hou.Prim, full_geo: hou.Geometry | None) -> hou.Prim | None:
    """
    Get the prim in the source detail.

    :prim: A primitive in another geometry, such as if the prim has
           been resampled, but the prim numbers still match up.
    """
def isPointBroken(ptnum: int, geo: hou.Geometry | None = None) -> bool:
    """
    Whether the point is considered a corner.

    :ptnum: The point number to check.
    :geo: The geometry to check on.
    """
def isPointSmooth(ptnum: int, geo: hou.Geometry | None) -> bool:
    """
    Whether the point is considered smooth.

    :ptnum: The point number to check.
    :geo: The geometry to check on.
    """
def isPointAuto(ptnum: int, geo: hou.Geometry | None) -> bool:
    """
    Whether the point is considered an auto point.

    :ptnum: The point number to check.
    :geo: The geometry to check on.
    """
def isPointAnchor(ptnum: int, geo: hou.Geometry | None) -> bool:
    """
    Whether the point is considered an anchor point.

    :ptnum: The point number to check.
    :geo: The geometry to check on.
    """
def isBranchedPoint(ptnum: int, geo: hou.Geometry | None) -> bool:
    """
    Whether the point is considered a branch point.

    :ptnum: The point number to check.
    :geo: The geometry to check on.
    """
def isEndPoint(ptnum: int, geo: hou.Geometry | None) -> bool:
    """ Whether the point is an open end of a curve. """
def isPointRoundCorner(ptnum: int, geo: hou.Geometry | None) -> bool:
    """
    Returns true iff the point is the leading point in a rounded
    corner. This differs from isRoundedCornerAnchor in that that
    function will return true for both anchors in a rounded corner.
    The two functions can be used together to tell if a point is the
    leading point or the end point in a rounded corner.

    :ptnum: The point number to check.
    :geo: The geometry to check on.
    """
def computeGroupGeometry(input_geo: hou.Geometry, group_string: str, negate: bool = False, points: bool = True) -> hou.Geometry:
    """
    Compute the geometry containing only the points in group_string
    NOTE: if all but one point in a primitive are deleted, the primitive
           is also deleted, so the resulting geometry CAN have unconnected
           points For this reason, it is not good to rely on the
           primitives in the resultant geometry.

    :input_geo: The geomety to filter elements on.
    :group_string: The group string used to filter.
    :negate: Whether to negate the result.
    :points: Whether the group is computed on points, or primitives.
    """
def resampleByPrimType(input_geo: hou.Geometry) -> hou.Geometry:
    """
    This is how the preview curve is created.
    We need to resample in special ways for each curve
    to format it correctly so that we can pick on the curve.

    :input_geo: The geometry to resample.
    """
def createBackboneGeo(base_geo: hou.Geometry, ptnums_arrays: Iterable[Iterable[int]]) -> hou.Geometry:
    """
    Create the backbone geometry connecting intermediate
    points in beziers of order > 4 and nurbs curves.

    :base_geo: The geometry to compute the backbone from.
    :ptnums: The point numbers to create as part of the backbone.
    """
def primIntrinsicType(prim: hou.Prim) -> str | None:
    """
    Get the intrinsic primitive type.

    :prim: The primitive.
    """
def convertIntrinsicType(typename: str | None) -> hou.EnumValue[hou.primType]:
    """
    Return the python enum value corresponding to the given
    typename string.

    :typename: The typename string.
    """
def getPrimDisplayType(prim: hou.Prim) -> str:
    """
    Get the primitive display type.

    :prim: The primitive.
    """
def isPrimBezier(prim: hou.Prim) -> bool:
    """
    Whether the primitive is a bezier curve.

    :prim: The prim to check the type of.
    """
def isPrimNurbs(prim: hou.Prim) -> bool:
    """
    Whether the primitive is a nurbs curve.

    :prim: The prim to check the type of.
    """
def isPrimPoly(prim: hou.Prim) -> bool:
    """
    Whether the primitive is a polygon curve.

    :prim: The prim to check the type of.
    """
def getPrimOrder(prim: hou.Prim) -> int:
    """
    Get the primitive order.

    :prim: The prim to check.
    """
def getPrimSegmentSize(prim: hou.Prim) -> int:
    """ Get the segment size for the prim. """
def removeBranchedPoints(ptnums: list[int], geo: hou.Geometry | None) -> list[int]:
    """
    Remove points that have multiple vertices.

    :ptnums: The list of point numbers.
    :geo: The geometry to check the points on.
    """
def setRoundCornerCenters(round_corners_geo: hou.Geometry, full_geo: hou.Geometry | None, tolerance: float = 1e-06) -> hou.Geometry:
    """
    Given a geometry containing only the points that are used for
    rounded corners use the context of these points to find the
    center of the rounded corner and place the point there. This
    is used to create the geometry for the rounded corner widgets

    :round_corners_geo: Geometry containing only the rounded corner points.
    :full_geo: The full geometry.
    :tolerance: A tolerance for whether two positions are considered the same.
    """
def needsBezierCase(geo: hou.Geometry | None) -> bool:
    """
    Whether we need to consider bezier special cases.

    :geo: The geometry to check on.
    """
def updateShowBezierOps(node: hou.SopNode | None, geo: hou.Geometry | None) -> None:
    """ Update a flag for whether bezier operations are enabled. """
def computeActiveGroupString(input_geo: hou.Geometry, input_group_str: str) -> str: ...
def getHandleInfo(ptnum: int, geo: hou.Geometry | None) -> list[list[hou.Point | None]]:
    """
    Given a point number of an anchor point, return a list of 3 points
    the lower, middle, and upper part of the handle centered at the
    given point. Any of the returned points can be None signifying that
    the point does not exist.

    :ptnum: The point number to check.
    :geo: The geometry to check on.
    """
def computeHandlesFromPtnums(input_geo: hou.Geometry, ptnums: Iterable[int]) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry]:
    """
    Compute handle geometries from the point numbers.

    :input_geo: The input geo to compute handles on.
    :pts: THe list of point numbers to create handles for.
    """
def computeHandlesFromPositions(input_geo: hou.Geometry | None, pts: Iterable[int | cu.PseudoHandleTuple]) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry] | tuple[None, None, None]:
    '''
    This function gathers the data from the active operation to know
    where to place "pseudo" handles. Pseudo handles look like
    interactible bezier handles but are not actually interactible.
    The reason to create pseudo handles is so that operations can show
    as many handles as they would like without needing to worry about
    setting up the parameters and managing several real bezier handles.

    3 Geometries:
       1. Smooth Lines
       2. Broken Lines
       3. End Points

    :input_geo: The geometry to comput handles on.
    :pts: The list of pseudo handle points, or tuples specifying the handles.
    '''
def pointPrims(ptnum: int, geo: hou.Geometry | None) -> list[hou.Prim]:
    """
    Get the prims on the point.

    :ptnum: The point number.
    :geo: The geometry to use.
    """
def pointPrim(ptnum: int, geo: hou.Geometry | None) -> hou.Prim | None:
    """
    Get the first prim on the point.

    :ptnum: The point number.
    :geo: The geometry to use.
    """
def pointPrimsInternalTypes(ptnum: int, geo: hou.Geometry | None) -> list[hou.EnumValue[hou.primType]]:
    """
    Get a list of the internal types on the point.

    :ptnum: The point number.
    :geo: The geometry to use.
    """
def isPointBezier(ptnum: int, geo: hou.Geometry | None) -> bool:
    """
    Whether the point has a bezier curve on it.

    :ptnum: The point number.
    :geo: The geometry to use.
    """
def isPointNurbs(ptnum: int, geo: hou.Geometry | None) -> bool:
    """
    Whether the point has a nurbs curve on it.

    :ptnum: The point number.
    :geo: The geometry to use.
    """
def isPointPoly(ptnum: int, geo: hou.Geometry | None = None) -> bool:
    """
    Whether the point has a polygon curve on it.

    :ptnum: The point number.
    :geo: The geometry to use.
    """
def pointVisualType(ptnum: int, geo: hou.Geometry | None) -> hou.EnumValue[hou.primType]: ...
def isPrimBezierHigherOrder(prim: hou.Prim) -> bool:
    """
    Whether the primitive is a bezier curve and the order > 4.

    :prim: The primitive to check.
    """
def isPointBezierHigherOrder(ptnum: int, geo: hou.Geometry | None) -> bool:
    """
    Whether any prim around the point is a bezier higher order
    prim.

    :ptnum: The point number.
    :geo: The geometry to use.
    """
def getOrderFromPoint(ptnum: int, geo: hou.Geometry | None) -> int:
    """
    Get order from primitive on point.

    This only works correctly if the point has a single prim.

    :ptnum: The point number to lookup.
    :geo: The geomerty to use.
    """
def getMaxOrderFromPoint(ptnum: int, geo: hou.Geometry | None) -> int:
    """
    Get the maximal order of the prims around the point.

    :ptnum: The point number to lookup.
    :geo: The geomerty to use.
    """
def getBrokenPointsGroup(node: hou.SopNode) -> str:
    """ Get the corner points group string. """
def getSmoothPointsGroup(node: hou.SopNode) -> str:
    """ Get the smooth points group string. """
def getAutoPointsGroup(node: hou.SopNode) -> str:
    """ Get the auto points group string. """
def isBezier(node: hou.SopNode | None) -> bool:
    """ Whether the output type is set to bezier. """
def isNurbs(node: hou.SopNode | None) -> bool:
    """ Whether the output type is set to NURBs. """
def isPoly(node: hou.SopNode | None) -> bool:
    """ Whether the output type is set to polygons. """
def getOrder(node: hou.SopNode | None) -> int:
    """ Get the order specified in the parameter pane. """
def getDefaultPrimType(node: hou.SopNode | None) -> hou.EnumValue[hou.primType]:
    """ Get the primitive type. """
def getRoundedCornersString(node: hou.SopNode | None) -> str:
    """ Get the rounded corner parm string. """
def showRoundedCorners(node: hou.SopNode | None, geo: hou.Geometry | None) -> bool:
    """ Get whether to show rounded corners. """
def outputOrientAttrib(node: hou.SopNode | None) -> bool | None:
    """ Get whether to output an orient attrib. """
def forceAlignToTangent(node: hou.SopNode | None) -> bool | None:
    """ Get the align tangent parm value. """
def softTransformEnabled(node: hou.SopNode | None) -> bool | None:
    """ Get whether soft transform is enabled. """
def getCacheGeometry(cache_geo: hou.Geometry, node: hou.SopNode | None) -> hou.Geometry:
    '''
    Prep the cached geometry. Use the base geoemetry
    and add any necessary attributes to it.
    These attributes are for any preprocessing needed so
    that the cached geometry matches the result from
    iteratively doing the operations.
    Since auto points and rounded corners actively update,
    they are evaluated after the operations. We need to "undo"
    These operations so there is no disparity between cached and not.
    Adding attributes for rounded corner points and auto points lets us
    do this computation. Auto points are already stored in a group that
    is used.

    :cache_geo: The geometry to use to start creating the cache geo.
    '''
def findHigherOrderCagePoints(geo: hou.Geometry, ptnum: int) -> tuple[list[int], list[list[int]], bool]: ...
def createUpCirclesGeometry(node: hou.SopNode | None, circle_geo: hou.Geometry, geo: hou.Geometry, scene_viewer: hou.SceneViewer) -> tuple[hou.Geometry, hou.Geometry]:
    """
    Create the circles geometry for rotating up vectors.
    Set up N and pscale attributes to copy the circles to the
    points properly. Then copy the circles to the points.
    """
def createOrientGuideGeometry(node: hou.SopNode | None, curve_geo: hou.Geometry | None, density_scale: float = 1.0, scale: float = 1.0) -> hou.Geometry:
    """
    Create the spine geometry for showing the up attribute.
    1. Convert the curve to polygon.
    2. Use the bbox of the curve to size the gnomon.
    3. Copy the gnomon geometry to the resampled curve.

    :enable: Whether to enable the orient guide geometry.
    :density_scale: How dense to make the guides along the curve. A higher number
                    will place more guides along the curve.
    :scale: The side of the individual guide gnomons.
    """
def createAnchorGeometries(geo: hou.Geometry, sel_string: str, color_options: ru.ColorOptions) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry, hou.Geometry]:
    """
    Update the geometry for anchor points, updates the other geometries
    that are rooted at the anchor geometries as well. This is separated
    out so that this can be called to just update the anchor point
    geometry without recreating the full internal geometry.
    """
def createActivePrimGroupGeometry(input_geo: hou.Geometry, active_prim_group: str) -> hou.Geometry: ...
def createReferenceCurveGeometry(node: hou.SopNode, geo: hou.Geometry) -> hou.Geometry:
    """ Add attributes and groups to the geometry so we can further analyze it. """
def getImplicitCurveTangent(ptnum: int, geo: hou.Geometry | None) -> hou.Vector3 | None:
    """
    Get the implicit curve tangent defined by the curve at the point.

    :ptnum: The point number.
    :geo: The geometry to use.
    """
def formatDictStringParm(kvmap: Mapping[_K, object], key_set: Iterable[_K] | None = None) -> str:
    """
    Format a dictionary into a string that lists the entries
    separated by spaces and with a : between the keys and values.
    Used by rounded corners.

    :kvmap: The map of values to package.
    :key_set: The set of keys to use, if none uses all.
    """
@typing.overload
def splitDictStringParm(parmstr: str, geo: hou.Geometry | None, key_fn: Callable[[str], _DK] | None = ..., val_fn: Callable[[str], _DV] | None = ..., attrib_name: None = ..., attrib_keep_fn: Callable[[_PointAttribValue], bool] | None = ...) -> dict[_DK | int, _DV | float]: ...
@typing.overload
def splitDictStringParm(parmstr: str, geo: hou.Geometry | None, key_fn: Callable[[str], _DK] | None, val_fn: Callable[[str], _DV] | None, attrib_name: str, attrib_keep_fn: Callable[[_PointAttribValue], bool] | None = ...) -> dict[_DK | int, _DV | float | _PointAttribValue]: ...
@typing.overload
def splitDictStringParm(parmstr: str, geo: hou.Geometry | None, key_fn: Callable[[str], _DK] | None = ..., val_fn: Callable[[str], _DV] | None = ..., *, attrib_name: str, attrib_keep_fn: Callable[[_PointAttribValue], bool] | None = ...) -> dict[_DK | int, _DV | float | _PointAttribValue]: ...
def getOrientAttribValue(ptnum: int, geo: hou.Geometry | None, node: hou.SopNode | None) -> hou.Quaternion | None:
    """
    Get the orient attribute value at a point.

    :ptnum: The point number.
    :geo: The geometry to use.
    """
def getTargetVectorByIndex(node: hou.SopNode | None, index: int, parm_name: str | None = None) -> hou.Vector3 | None:
    """
    Get the vector parm by index into the multiparm.

    :index: The index into the multiparm.
    :parm_name: The parameter name. This specifies which vector in the
        given multiparm instance to grab.
    """
@typing.overload
def getTargetOrientPoints(node: hou.SopNode | None, exclude_disabled: bool = ..., tuple_with_vectors: Literal[False] = ...) -> list[int]: ...
@typing.overload
def getTargetOrientPoints(node: hou.SopNode | None, exclude_disabled: bool, tuple_with_vectors: Literal[True]) -> list[tuple[int, hou.Vector3 | None, hou.Vector3 | None]]: ...
@typing.overload
def getTargetOrientPoints(node: hou.SopNode | None, exclude_disabled: bool = ..., *, tuple_with_vectors: Literal[True]) -> list[tuple[int, hou.Vector3 | None, hou.Vector3 | None]]: ...
@typing.overload
def getTargetOrientPoints(node: hou.SopNode | None, exclude_disabled: bool = ..., tuple_with_vectors: bool = ...) -> list[int] | list[tuple[int, hou.Vector3 | None, hou.Vector3 | None]]: ...
def getTargetOrientPointsMap(node: hou.SopNode | None, exclude_disabled: bool = True) -> dict[int, tuple[hou.Vector3 | None, hou.Vector3 | None]]:
    """
    Get a map of ptnum -> (up vector, tangent vector) for each point
    that has a orient key frame on it.

    :exclude_disabled: Whether to exclude disabled key points.
    """
def setPointPos(geo: hou.Geometry | None, ptnum: int, pos: hou.Vector3) -> None:
    """
    Manually set some points position in the reference geometry.
    This is useful to adjust just a single point position without
    needing to recompute the full reference geometry from the nodes
    cooked geometry which is quite expensive.

    :geo: The geometry to set the position on.
    :ptnum: The point number in geo.
    :pos: The updated position.
    """
def updatePointFromMap(ptnum: int, pos: hou.Vector3, the_map: Mapping[int, int] | None, geo: hou.Geometry | None) -> None:
    """
    Update a point position for the sub geometry. See setPointPos.

    :ptnum: The point number in the full geometry.
    :pos: The updated position.
    :the_map: The map mapping full geometry ptnums to sub geo ptnums relevant
        for geo.
    :geo: The sub geo.
    """

class PointGeoWrapper:
    my_geo: hou.Geometry | None
    mapping: dict[int, int] | None
    def __init__(self) -> None: ...
    @property
    def geo(self) -> hou.Geometry | None: ...
    @geo.setter
    def geo(self, geometry: hou.Geometry | None) -> None: ...
    def buildMap(self) -> None: ...

class ReferenceCurve:
    """
    Class to encapsulate creation and management of internal geometry for
    things like guide drawables, gadgets, selection points, preview curves, etc.
    """
    main_state: _CurveState
    base_geo: hou.Geometry | None
    base_geo_id: tuple[int, ...] | None
    input_geo_id: tuple[int, ...] | None
    active_prim_group: str
    geo: hou.Geometry
    active_prim_group_geo: hou.Geometry | None
    full_select_geo: hou.Geometry | None
    round_point_geo: hou.Geometry | None
    select_round_point_geo: hou.Geometry | None
    orient_guide_geo: hou.Geometry | None
    orient_circles_lines_geo: hou.Geometry | None
    orient_circles_faces_geo: hou.Geometry | None
    orient_circle_base_geo: hou.Geometry | None
    preview_curve_geo: hou.Geometry | None
    pre_operation_geo: hou.Geometry | None
    pseudo_handle_geos: Sequence[hou.Geometry | None]
    active_handle_geos: tuple[hou.Geometry | None, hou.Geometry | None, hou.Geometry | None]
    pseudo_handle_pts: list[int | cu.PseudoHandleTuple]
    active_handle_pts: list[int]
    round_corner_anchors: set[int]
    pts_near_round_corners: set[int]
    round_corner_radii: dict[int, float]
    auto_update: bool
    anchor_points: PointGeoWrapper
    broken_points: PointGeoWrapper
    smooth_points: PointGeoWrapper
    balanced_points: PointGeoWrapper
    auto_points: PointGeoWrapper
    broken_end_points: PointGeoWrapper
    smooth_end_points: PointGeoWrapper
    balanced_end_points: PointGeoWrapper
    auto_end_points: PointGeoWrapper
    higher_order_points: PointGeoWrapper
    higher_order_backbone: PointGeoWrapper
    anchor_point_collections: list[PointGeoWrapper]
    handle_point_collections: list[PointGeoWrapper]
    point_collections: list[PointGeoWrapper]
    in_update: bool
    PRIMIDX_ATTRIB: str
    PTPRIMIDX_ATTRIB: str
    PTIDX_INPRIM_ATTRIB: str
    PRE_PTNUM_ATTRIB: str
    PRIM_LASTIDX_ATTRIB: str
    CURVEUPOS_ATTRIB: str
    CURVENUM_ATTRIB: str
    CURVETANGENT_ATTRIB: str
    CURVEUP_ATTRIB: str
    CURVEORIENT_ATTRIB: str
    ANCHORPTS_ATTRIB: str
    ANCHORPTS_GROUP: str
    BROKENPTS_GROUP: str
    SMOOTHPTS_GROUP: str
    AUTOPTS_GROUP: str
    ROUNDCORNERPTS_GROUP: str
    SELECTEDPTS_GROUP: str
    ACTIVEPRIM_GROUP: str
    POLYPRIMS_GROUP: str
    POLYPTS_GROUP: str
    NURBSPRIMS_GROUP: str
    NURBSPTS_GROUP: str
    BEZIERPRIMS_GROUP: str
    BEZIERPTS_GROUP: str
    def __init__(self, main_state: _CurveState) -> None: ...
    def setAutoUpdate(self, val: bool) -> None:
        """
        Used for optimizing certain operations.
        When auto update is enabled on any change to the
        node parms, it will need to recreate the full
        geometries from the node geometry. This can be slow
        as many of these geometries require O(n) operations.
        In some cases when dragging individual points, auto
        updating can be disabled, and you can pass information
        to manually update the parts of the geometry, turning
        a update operation that would be O(n) into an O(1) operation.

        :val: Whether to auto update.
        """
    def getAutoUpdate(self) -> bool:
        """ See setAutoUpdate. """
    def setPreviewCurve(self, geo: hou.Geometry | None) -> None:
        """
        Set the preview curve to the given geometry.
        The preview curve cannot be automatically updated,
        as many operations update the preview curve in different
        ways and at different times. E.g. button operations update
        on doing an operation, dragging points updates the preview
        curve on finishing a drag, and in draw modes, the preview
        curve is updated on any mouse move to show how the curve
        will look once the action is taken.

        :geo: The new preview curve geometry.
        """
    def getPreviewCurve(self) -> hou.Geometry | None:
        """ See setPreviewCurve. """
    def setPseudoHandlePts(self, pts: list[int | cu.PseudoHandleTuple]) -> None:
        """ Set point nums for which non-interactive handles are drawn on. """
    def getPseudoHandlePts(self) -> list[int | cu.PseudoHandleTuple]:
        """ Get point nums for which non-interactive handles are drawn. """
    def setActiveHandlePts(self, pts: list[int]) -> None:
        """ Set point nums for which active handles are made on. """
    def getActiveHandlePts(self) -> list[int]:
        """ Get point nums for which active handles are made on. """
    def updatePreOperationGeo(self) -> None:
        """
        Set the pre operation geo to the current geometry.
        This is used to keep track of two versions of the geometry,
        before and after an operation. This is used when updating the
        string group parameters as some operations need to know either
        the geometry before or after the operation or both.
        """
    def getPreOperationGeo(self) -> hou.Geometry | None:
        """ See updatePreOperationGeo """
    def checkNodeGeoChange(self, force_update: bool = False) -> bool:
        """
        Reset node geometry if auto update is on
        if the vexAttribDataId has changed, it will
        recompute the internal geometry

        :force_update: Whether to force an update of the geometry.
        """
    def setGeometry(self, geo: hou.Geometry) -> bool:
        """
        Set the base geometry that the internal geometry
        is created from. Updates the internal geometry if
        the base geo is different from the previous base geo.

        :geo: The geometry to freeze and use as the base geometry.
        """
    def getActivePrimGroup(self) -> str:
        """
        Get the group of primitives not being modified by the node
        Internally in the node, it only works with the active geometry
        so we need to remove the inactive primitives to make the internal
        state geometry consistent.
        """
    def isRoundCornerAnchor(self, ptnum: int) -> bool:
        """
        Whether a point is an anchor that is in a rounded corner.

        :ptnum: The point number in question.
        """
    def isNearRoundCorner(self, ptnum: int) -> bool:
        """
        Whether a point is an anchor next to a rounded corner
        or in a rounded corner. Some operations do not work properly
        if next to a rounded corner.

        :ptnum: The point number in question.
        """
    def removeRoundCornerAnchors(self, ptnums: list[int]) -> list[int]:
        """
        Return ptnums with all ptnum with isRoundCornerAnchor being true removed.

        :ptnums: A list of point numbers.
        """
    def removeAnchorsNearRoundCorners(self, ptnums: list[int]) -> list[int]:
        """
        Return ptnums with all ptnum with isNearRoundCorner being true removed.

        :ptnums: A list of point numbers.
        """
    def removeBranchedPoints(self, ptnums: list[int], geo: hou.Geometry | None = None) -> list[int]:
        """
        Remove points that have multiple vertices.

        :ptnums: The list of point numbers.
        :geo: The geometry to check the points on. If None, uses self.geo.
        """
    def resampleByPrimType(self, input_geo: hou.Geometry | None = None) -> hou.Geometry:
        """
        This is how the preview curve is created.
        We need to resample in special ways for each curve
        to format it correctly so that we can pick on the curve.

        :input_geo: The geometry to resample. If None, uses self.getGeometry().
        """
    def computeHandlesFromPtnums(self, input_geo: hou.Geometry, pts: Iterable[int | cu.PseudoHandleTuple]) -> tuple[hou.Geometry, hou.Geometry, hou.Geometry]:
        """
        Compute handle geometries from the point numbers.

        :input_geo: The input geo to compute handles on.
        :pts: THe list of point numbers to create handles for.
        """
    def updatePseudoHandlesEmpty(self) -> None:
        """ Update pseudo handles to be empty. """
    def updatePseudoHandles(self) -> None:
        """
        Update the pseudo handle geometry.
        These are non-interactive guides showing the handles on the
        pseudo handle points.
        """
    def createBackboneGeo(self, base_geo: hou.Geometry, ptnums_arrays: Iterable[Iterable[int]]) -> hou.Geometry | None:
        """
        Create the backbone geometry connecting intermediate
        points in beziers of order > 4 and nurbs curves.

        :base_geo: The geometry to compute the backbone from.
        :ptnums: The point numbers to create as part of the backbone.
        """
    def updateHigherOrderGeos(self) -> None:
        """
        Update the geometry for higher order points geometry.
        Creates the interactive intermediate points on beziers of order > 4
        and the backbone curve used in high order bezier and nurbs.
        """
    def updateRoundCornerGeometry(self) -> None:
        """
        Compute the rounded corner centers geometry.
        Also fills out the dictionaries that keep track of which anchors
        are rounded corners and are near rounded corners.
        """
    def getOrientCircleBaseGeometry(self) -> hou.Geometry:
        """ Create and store the twist circle geometry. """
    def updateUpCirclesGeometry(self) -> None:
        """
        Create the circles geometry for rotating up vectors.
        Set up N and pscale attributes to copy the circles to the
        points properly. Then copy the circles to the points.
        """
    def updateOrientGuideGeometry(self, enable: bool = True, density_scale: float = 1.0, scale: float = 1.0) -> None:
        """
        Create the spine geometry for showing the up attribute.
        1. Convert the curve to polygon.
        2. Use the bbox of the curve to size the gnomon.
        3. Copy the gnomon geometry to the resampled curve.

        :enable: Whether to enable the orient guide geometry.
        :density_scale: How dense to make the guides along the curve. A higher number
                        will place more guides along the curve.
        :scale: The side of the individual guide gnomons.
        """
    def updateAnchorGeometries(self) -> None:
        """
        Update the geometry for anchor points, updates the other geometries
        that are rooted at the anchor geometries as well. This is separated
        out so that this can be called to just update the anchor point
        geometry without recreating the full internal geometry.
        """
    def setEmptyGeo(self) -> None:
        """ Reset all geometries. """
    def needsBezierCase(self, geo: hou.Geometry | None = None) -> bool:
        """
        Whether we need to consider bezier special cases.

        :geo: The geometry to check on, defaults to self.geo is None.
        """
    def updateShowBezierOps(self) -> None:
        """ Update a flag for whether bezier operations are enabled. """
    def update(self) -> None:
        """ Update the state's reference geometry. """
    def buildSubgeoMaps(self) -> None:
        """
        Build some maps that help with optimizing updates to geometries
        by mapping real point numbers to the point numbers in the internal
        geometries. This is used to allow some operations to update in O(1)
        rather than O(n).
        """
    def updateHandlePointPosition(self, ptnum: int, pos: hou.Vector3) -> None:
        """
        See updatePointPositions and setPointPos.

        :ptnum: The point number of the handle point to move.
        :pos: The updated position.
        """
    def updateAnchorPointPosition(self, ptnum: int, pos: hou.Vector3) -> None:
        """
        See updatePointPositions and setPointPos.

        :ptnum: The anchor point number in the full geometry to move.
        :pos: The updated position.
        """
    def canOptimizePointMove(self, ptnum: int) -> bool:
        """
        Whether we can optimize the point move.
        See updatePointPositions and setPointPos.
        We cannot optimize round corner moves, or branched points.

        :ptnum: The point number to query.
        """
    def canOptimizePointUpdate(self, anchor_data: Iterable[tuple[int, hou.Vector3]], handle_data: Iterable[tuple[int, hou.Vector3]]) -> bool:
        """
        See updatePointPositions.

        :anchor_data: List of data for moving anchor points.
        :handle_data: List of data for moving handle points.
        """
    def updatePointPositions(self, anchor_data: Iterable[tuple[int, hou.Vector3]], handle_data: Iterable[tuple[int, hou.Vector3]]) -> None:
        """
        Used to update curve point positions in all of the internal geometry
        representations in an O(1) way to avoid an O(n) update that requires
        evaluating several node verbs.

        In some cases, the optimization must be disabled, this is the case
        if there is anything that is changing that is hard to predict or if
        predicting the changes is just as slow as a full update. This is the
        case when the orient attribute is enabled as it needs to update the full
        guide geometry. This is also the case with rounded corners and auto points,
        where a single point move can affect many points, or even a full curve.

        :anchor_data: List of data for moving anchor points.
        :handle_data: List of data for moving handle points.
        """
    def getFullGeoPoint(self, point: hou.Point) -> hou.Point | None:
        """
        Given a point, possibly in a subgeo, return the corresponding
        point in the full geometry.

        See pointInternalPtnum.

        :point: The point to look up.
        """
    def getFullGeoPrim(self, prim: hou.Prim) -> hou.Prim | None:
        """
        Get the prim in the source detail.

        :prim: A primitive in another geometry, such as if the prim has
               been resampled, but the prim numbers still match up.
        """
    def isPointBroken(self, ptnum: int, geo: hou.Geometry | None = None) -> bool:
        """
        Whether the point is considered a corner.

        :ptnum: The point number to check.
        :geo: The geometry to check on, uses self.getGeometry() if None.
        """
    def isPointSmooth(self, ptnum: int, geo: hou.Geometry | None = None) -> bool:
        """
        Whether the point is considered smooth.

        :ptnum: The point number to check.
        :geo: The geometry to check on, uses self.getGeometry() if None.
        """
    def isPointAuto(self, ptnum: int, geo: hou.Geometry | None = None) -> bool:
        """
        Whether the point is considered an auto point.

        :ptnum: The point number to check.
        :geo: The geometry to check on, uses self.getGeometry() if None.
        """
    def isPointAnchor(self, ptnum: int, geo: hou.Geometry | None = None) -> bool:
        """
        Whether the point is considered an anchor point.
    
        :ptnum: The point number to check.
        :geo: The geometry to check on, uses self.getGeometry() if None.
        """
    def isBranchedPoint(self, ptnum: int, geo: hou.Geometry | None = None) -> bool:
        """
        Whether the point is considered a branch point.

        :ptnum: The point number to check.
        :geo: The geometry to check on, uses self.getGeometry() if None.
        """
    def isEndPoint(self, ptnum: int, geo: hou.Geometry | None = None) -> bool:
        """ Whether the point is an open end of a curve. """
    def isPointRoundCorner(self, ptnum: int, geo: hou.Geometry | None = None) -> bool:
        """
        Returns true iff the point is the leading point in a rounded
        corner. This differs from isRoundedCornerAnchor in that that
        function will return true for both anchors in a rounded corner.
        The two functions can be used together to tell if a point is the
        leading point or the end point in a rounded corner.

        :ptnum: The point number to check.
        :geo: The geometry to check on, uses self.getGeometry() if None.
        """
    def pointHasTangents(self, ptnum: int) -> bool:
        """
        Whether a point has controllable tangents. We only draw
        tangents on bezier curves, and on anchors that are not rounded
        corners or auto points.

        :ptnum: The point number in question.
        """
    def vertexHasTangents(self, vtx: hou.Vertex) -> bool:
        """
        Whether a vertex has controllable tangents. We only draw
        tangents on bezier curves, and on anchors that are not rounded
        corners or auto points.

        :vtx: The vertex in question.
        """
    def getBrokenPointsGroup(self) -> str:
        """ Get the corner points group string. """
    def getSmoothPointsGroup(self) -> str:
        """ Get the smooth points group string. """
    def getAutoPointsGroup(self) -> str:
        """ Get the auto points group string. """
    def isBezier(self) -> bool:
        """ Whether the output type is set to bezier. """
    def isNurbs(self) -> bool:
        """ Whether the output type is set to NURBs. """
    def isPoly(self) -> bool:
        """ Whether the output type is set to polygons. """
    def getOrder(self) -> int:
        """ Get the order specified in the parameter pane. """
    def getDefaultPrimType(self) -> hou.EnumValue[hou.primType]:
        """ Get the primitive type. """
    def pointPrim(self, ptnum: int, geo: hou.Geometry | None = None) -> hou.Prim | None:
        """
        Get the first prim on the point.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        """
    def pointPrims(self, ptnum: int, geo: hou.Geometry | None = None) -> list[hou.Prim]:
        """
        Get the prims on the point.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        """
    def pointPrimsInternalTypes(self, ptnum: int, geo: hou.Geometry | None = None) -> list[hou.EnumValue[hou.primType]]:
        """
        Get a list of the internal types on the point.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        """
    def isPointBezier(self, ptnum: int, geo: hou.Geometry | None = None) -> bool:
        """
        Whether the point has a bezier curve on it.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        """
    def isPointNurbs(self, ptnum: int, geo: hou.Geometry | None = None) -> bool:
        """
        Whether the point has a nurbs curve on it.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        """
    def isPointPoly(self, ptnum: int, geo: hou.Geometry | None = None) -> bool:
        """
        Whether the point has a polygon curve on it.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        """
    def pointVisualType(self, ptnum: int, geo: hou.Geometry | None = None) -> hou.EnumValue[hou.primType]: ...
    def isPointBezierHigherOrder(self, ptnum: int, geo: hou.Geometry | None = None) -> bool:
        """
        Whether any prim around the point is a bezier higher order
        prim.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        """
    def getOrderFromPoint(self, ptnum: int, geo: hou.Geometry | None = None) -> int:
        """
        Get order from primitive on point.

        This only works correctly if the point has a single prim.

        :ptnum: The point number to lookup.
        :geo: The geomerty to use. Defaults to self.getGeometry() if None.
        """
    def getMaxOrderFromPoint(self, ptnum: int, geo: hou.Geometry | None = None) -> int:
        """
        Get the maximal order of the prims around the point.

        :ptnum: The point number to lookup.
        :geo: The geomerty to use. Defaults to self.getGeometry() if None.
        """
    def getRoundedCornersString(self) -> str:
        """ Get the rounded corner parm string. """
    def showRoundedCorners(self) -> bool:
        """ Get whether to show rounded corners. """
    def outputOrientAttrib(self) -> bool | None:
        """ Get whether to output an orient attrib. """
    def forceAlignToTangent(self) -> bool | None:
        """ Get the align tangent parm value. """
    def softTransformEnabled(self) -> bool | None:
        """ Get whether soft transform is enabled. """
    @typing.overload
    def splitDictStringParm(self, parmstr: str | None = ..., key_fn: Callable[[str], _DK] | None = ..., val_fn: Callable[[str], _DV] | None = ..., override_geo: hou.Geometry | None = ..., attrib_name: None = ..., attrib_keep_fn: Callable[[_PointAttribValue], bool] | None = ...) -> dict[_DK | int, _DV | float]: ...
    @typing.overload
    def splitDictStringParm(self, parmstr: str | None, key_fn: Callable[[str], _DK] | None, val_fn: Callable[[str], _DV] | None, override_geo: hou.Geometry | None, attrib_name: str, attrib_keep_fn: Callable[[_PointAttribValue], bool] | None = ...) -> dict[_DK | int, _DV | float | _PointAttribValue]: ...
    @typing.overload
    def splitDictStringParm(self, parmstr: str | None = ..., key_fn: Callable[[str], _DK] | None = ..., val_fn: Callable[[str], _DV] | None = ..., override_geo: hou.Geometry | None = ..., *, attrib_name: str, attrib_keep_fn: Callable[[_PointAttribValue], bool] | None = ...) -> dict[_DK | int, _DV | float | _PointAttribValue]: ...
    def getTargetVectorByIndex(self, index: int, parm_name: str | None = None) -> hou.Vector3 | None:
        """
        Get the vector parm by index into the multiparm.

        :index: The index into the multiparm.
        :parm_name: The parameter name. This specifies which vector in the
            given multiparm instance to grab.
        """
    @typing.overload
    def getTargetOrientPoints(self, exclude_disabled: bool = ..., tuple_with_vectors: Literal[False] = ...) -> list[int]: ...
    @typing.overload
    def getTargetOrientPoints(self, exclude_disabled: bool, tuple_with_vectors: Literal[True]) -> list[tuple[int, hou.Vector3 | None, hou.Vector3 | None]]: ...
    @typing.overload
    def getTargetOrientPoints(self, exclude_disabled: bool = ..., *, tuple_with_vectors: Literal[True]) -> list[tuple[int, hou.Vector3 | None, hou.Vector3 | None]]: ...
    @typing.overload
    def getTargetOrientPoints(self, exclude_disabled: bool = ..., tuple_with_vectors: bool = ...) -> list[int] | list[tuple[int, hou.Vector3 | None, hou.Vector3 | None]]: ...
    def getTargetOrientPointsMap(self, exclude_disabled: bool = True) -> dict[int, tuple[hou.Vector3 | None, hou.Vector3 | None]]:
        """
        Get a map of ptnum -> (up vector, tangent vector) for each point
        that has a orient key frame on it.

        :exclude_disabled: Whether to exclude disabled key points.
        """
    def getOrientAttribValue(self, ptnum: int, geo: hou.Geometry | None = None) -> hou.Quaternion | None:
        """
        Get the orient attribute value at a point.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        """
    def getOrientAxisAttribValue(self, ptnum: int, geo: hou.Geometry | None = None, axis: hou.Vector3 | None = None) -> hou.Vector3 | None:
        """
        Get an axis rotated by the orient attribute at a point.
        Basically, take some axis vector and return the vector in the points frame.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        :axis: The axis to transform, if None uses +Z axis.
        """
    def getOrientUpAttribValue(self, ptnum: int, geo: hou.Geometry | None = None) -> hou.Vector3 | None:
        """
        Get the up axis in the points frame.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        """
    def getOrientTangentAttribValue(self, ptnum: int, geo: hou.Geometry | None = None) -> hou.Vector3 | None:
        """
        Get the tangent axis in the points frame.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        """
    def getImplicitCurveTangent(self, ptnum: int, geo: hou.Geometry | None = None) -> hou.Vector3 | None:
        """
        Get the implicit curve tangent defined by the curve at the point.

        :ptnum: The point number.
        :geo: The geometry to use. Defaults to self.getGeometry() if None.
        """
    def getGeometry(self) -> hou.Geometry:
        """ Get the base goemetry. """
    def getCacheGeometry(self, cache_geo: hou.Geometry | None = None) -> hou.Geometry:
        '''
        Prep the cached geometry. Use the base geoemetry
        and add any necessary attributes to it.
        These attributes are for any preprocessing needed so
        that the cached geometry matches the result from
        iteratively doing the operations.
        Since auto points and rounded corners actively update,
        they are evaluated after the operations. We need to "undo"
        These operations so there is no disparity between cached and not.
        Adding attributes for rounded corner points and auto points lets us
        do this computation. Auto points are already stored in a group that
        is used.

        :cache_geo: The geometry to use to start creating the cache geo.
        '''
    def getRoundPointGeometry(self) -> hou.Geometry | None:
        """ Get the rounded corner points geometry. """
    def getSelectRoundPointGeometry(self) -> hou.Geometry | None:
        """ Get the selected round corner points geometry. """
    def getAnchorGeometry(self) -> hou.Geometry | None: ...
    def getBrokenPointGeometry(self) -> hou.Geometry | None: ...
    def getSmoothPointGeometry(self) -> hou.Geometry | None: ...
    def getBalancedPointGeometry(self) -> hou.Geometry | None: ...
    def getAutoPointGeometry(self) -> hou.Geometry | None: ...
    def getBrokenEndPointGeometry(self) -> hou.Geometry | None: ...
    def getSmoothEndPointGeometry(self) -> hou.Geometry | None: ...
    def getBalancedEndPointGeometry(self) -> hou.Geometry | None: ...
    def getAutoEndPointGeometry(self) -> hou.Geometry | None: ...
    def getHigherOrderBezierGeometry(self) -> hou.Geometry | None: ...
    def getHigherOrderBackboneGeometry(self) -> hou.Geometry | None: ...
    def getPseudoHandleBrokenLineGeometry(self) -> hou.Geometry | None: ...
    def getPseudoHandleSmoothLineGeometry(self) -> hou.Geometry | None: ...
    def getPseudoHandleEndsGeometry(self) -> hou.Geometry | None: ...
    def getActiveHandleBrokenLineGeometry(self) -> hou.Geometry | None: ...
    def getActiveHandleSmoothLineGeometry(self) -> hou.Geometry | None: ...
    def getActiveHandleEndsGeometry(self) -> hou.Geometry | None: ...
    def getOrientGuideGeometry(self, enable: bool = True, density_scale: float = 1.0, scale: float = 1.0) -> hou.Geometry | None:
        """
        Return the spine geometry for showing the up attribute.

        :enable: Whether to enable the orient guide geometry.
        :density_scale: How dense to make the guides along the curve. A higher number
                        will place more guides along the curve.
        :scale: The side of the individual guide gnomons.
        """
    def getOrientCirclesLinesGeometry(self) -> hou.Geometry | None: ...
    def getOrientCirclesFacesGeometry(self) -> hou.Geometry | None: ...
    def getHandleInfo(self, ptnum: int, geo: hou.Geometry | None = None) -> list[list[hou.Point | None]]:
        """
        Given a point number of an anchor point, return a list of 3 points
        the lower, middle, and upper part of the handle centered at the
        given point. Any of the returned points can be None signifying that
        the point does not exist.

        :ptnum: The point number to check.
        :geo: The geometry to check on, uses self.getGeometry() if None.
        """
