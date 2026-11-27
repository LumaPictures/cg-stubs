import hou
import resourceutils as ru
import typing
from houtypes import ViewerStateEventKwargs
from typing import TypeAlias, TypedDict, Unpack

from typing import TypeAlias
LineSegmentDrawable: TypeAlias = ru.LineSegmentDrawable
DragGuide: TypeAlias = ru.DragGuide
class _StateDraggerKwargs(TypedDict, total=False):
    name: str
    xform: hou.Matrix4
    inv_xform: hou.Matrix4

class _HandleDraggerKwargs(TypedDict, total=False):
    name: str
BASE_TEST_DIST: int
SLOW_FACTOR: float
MIN_SCALE: float
TOLERANCE: float
HANDLE_PREF_REG: str
HANDLE_SCALE_PREF: str
HANDLE_SHOW_PLANES_PREF: str
HANDLE_SHOW_HIDDEN_PLANES_PREF: str
HANDLE_SHOW_TUMBLE_PREF: str
HANDLE_SHOW_VIEW_RING_PREF: str
HANDLE_INDIRECT_DRAG_PREF: str
HANDLE_INDIRECT_TRANSLATE_PREF: str
HANDLE_HIDE_RINGS_VIEW_DIR_PREF: str
HANDLE_SHOW_NEGATIVE_AXES_PREF: str
HANDLE_PREFER_PLANES_OVER_BACKFACING_AXES_PREF: str
HANDLE_DEFAULT_GIMBAL_PREF: str
APEXHANDLE_PREF_REG: str
APEXHANDLE_CLIP_DIST_PREF: str
APEXHANDLE_SHOW_PLANES_PREF: str
APEXHANDLE_CENTER_VIEW_ALIGN_PREF: str
APEXHANDLE_AXES_OUTSIDE_PREF: str
APEXHANDLE_PLANES_OUTSIDE_PREF: str
APEXHANDLE_LINE_WIDTH_PREF: str
APEXHANDLE_BRIGHTNESS_PREF: str
APEXHANDLE_VIEW_RING_SCALE_PREF: str
APEXHANDLE_TUMBLE_SPHERE_SCALE_PREF: str
APEXHANDLE_ALL_VIEWPORTS_PREF: str
APEXHANDLE_ALT_ROTATE_PREF: str
APEXHANDLE_GLOBAL_SCALE_PREF: str
APEXHANDLE_ARROW_TIP_SCALE_PREF: str
APEXHANDLE_CENTER_BOX_SCALE_PREF: str
APEXHANDLE_AXIS_LENGTH_SCALE_PREF: str
APEXHANDLE_ROT_SPHERE_SCALE_PREF: str
APEXHANDLE_PLANE_SCALE_PREF: str
APEXHANDLE_SHOW_LABELS_PREF: str
APEXHANDLE_SHOW_ROT_SPHERES_PREF: str
APEXHANDLE_AXIS_OFFSET_PREF: str
APEXHANDLE_OUTSIDE_AXIS_OFFSET_PREF: str
APEXHANDLE_OUTSIDE_AXIS_SCALE_PREF: str
APEXHANDLE_USE_LADDER_PREF: str
APEXHANDLE_TUMBLE_COMBINED_PREF: str
APEXHANDLE_TUMBLE_BORDER_PREF: str
APEXHANDLE_SEPARATE_ALIGNS_PREF: str
APEXHANDLE_T_ALIGNMENT_PREF: str
APEXHANDLE_R_ALIGNMENT_PREF: str
APEXHANDLE_S_ALIGNMENT_PREF: str
APEXHANDLE_SELECT_INDIRECT_PREF: str
APEXHANDLE_CHANGE_MODE_AUTO_PREF: str
LEGACY_PREF_MAP: dict[str, str]
SCALE_INHERITANCE_LIST: list[hou.EnumValue[hou.scaleInheritanceMode]]
AXES: tuple[str, str, str]

def axisNameToIndex(axis_name: str) -> int: ...
def moveLegacyPrefs() -> list[str]:
    """ Find any legacy preferences, set the new pref values and delete the old pref. """
def isSingular(m: hou.Matrix4) -> bool:
    """ Whether the matrix m is singular (i.e. has 0 determinant). """
def getWorldOrigin(scene_viewer: hou.SceneViewer) -> hou.Vector3:
    """ Just returns (0,0,0)."""
def getWorldOrientation(scene_viewer: hou.SceneViewer) -> hou.Matrix3:
    """ Just returns the identity matrix."""
def getCPlaneXform(scene_viewer: hou.SceneViewer) -> hou.Matrix4:
    """ Get the construction plane transform."""
def getCPlaneOrigin(scene_viewer: hou.SceneViewer) -> hou.Vector3:
    """ Get the construction plane origin."""
def getCPlaneOrientation(scene_viewer: hou.SceneViewer) -> hou.Matrix3:
    """ Get the construction plane orientation matrix3."""
def getViewOrientation(scene_viewer: hou.SceneViewer) -> hou.Matrix3:
    """ Get the view transform orientation matrix3. """
def projectToPlane(pos: hou.Vector3, nml: hou.Vector3, orig: hou.Vector3) -> hou.Vector3:
    """
    Project pos onto the plane defined by the normal nml
    and going through the point orig.
    """
def getCPlaneProjection(scene_viewer: hou.SceneViewer, pos: hou.Vector3) -> hou.Vector3:
    """ Get the projection of 'pos' onto the construction plane. """
def redrawViewports(scene_viewer: hou.SceneViewer, only_current: bool = False) -> None:
    """ Redraw the viewports. """
def avoidZeroScale(scale_amt: float) -> float:
    """ Returns the minimum scale if the scale is 0.0. """
def avoidZeroScaleVec(scale_vec: hou.Vector3) -> hou.Vector3:
    """ Calls avoidZeroScale for each component independently. """
def isSlowMouseEvent(kwargs: ViewerStateEventKwargs) -> bool:
    """ Check if the key combination is pressed to do slow movements. """
def isSteppedMouseEvent(kwargs: ViewerStateEventKwargs) -> bool:
    """ Check if the key combination is pressed to do a stepped movement. """
def isAxisSnapMouseEvent(kwargs: ViewerStateEventKwargs) -> bool:
    """ Check if we should enable axis snapping. """
def isGlobalModeModifierMouseEvent(kwargs: ViewerStateEventKwargs) -> bool:
    """ Check if we should enable axis snapping. """
def roundToStep(value: float, step: float) -> float:
    """ Round the value to the closest multiple of 'step'. """
def roundVecLengthToStep(v: hou.Vector3, step: float) -> hou.Vector3:
    """ Round the vector length to the closest multiple of 'step'. """
def roundRotateMatxStep(rot_matx: hou.Matrix3, step: float) -> hou.Matrix3:
    """
    Round the rotation matrix 'rot_matx' to the closest multiple of 'step'.

    This is done by assuming rot_matx describes only a rotation and treating
    it as a quaternion, then decomposing that to an angle and axis,
    and rounding the angle to a multiple of step, then rebuilding the
    matrix and returning the result.
    """
@typing.overload
def adjustSlow(val: float) -> float: ...
@typing.overload
def adjustSlow(val: hou.Vector3) -> hou.Vector3: ...
def adjustRotMatxSlow(rot: hou.Matrix3) -> hou.Matrix3:
    """
    Adjust the rotation matrix by the slow factor.

    This decomposes the 'rot' matrix into an angle and
    axis, multiplies the angle by the slow factor, and
    returns the modified matrix.
    """
def multVecMat4(v: hou.Vector3, m: hou.Matrix4) -> hou.Vector3:
    """
    Multiply the vector3 'v' by the matrix4 'm' while ignoring
    the translation components of 'm'.
    """
def getRotationMatrix4(xform: hou.Matrix4) -> hou.Matrix4: ...
def getRotationMatrix3(xform: hou.Matrix4) -> hou.Matrix3: ...
def snapZeroFloat(val: float) -> float:
    """ Snap the float value 'val' to 0.0 if within the tolerance. """
def snapZeroVec(val: hou.Vector3) -> hou.Vector3:
    """ Snap the values in the hou.Vector3 to 0.0 if within the tolerance. """
@typing.overload
def snapZero(val: float) -> float: ...
@typing.overload
def snapZero(val: hou.Vector3) -> hou.Vector3: ...
def getColorVec(col: hou.Color) -> tuple[float, float, float, float]:
    """ Get a color tuple from the colour object. """
def getHandleScalePref() -> float:
    """ Get the handle scale preference value. """
def getHandleShowTumblePref() -> bool:
    """ Get the handle show tumble sphere pref. """
def getHandleShowPlanesPref() -> bool:
    """ Get the handle show planes preference value. """
def getHandleShowViewRingPref() -> bool:
    """ Get the handle show planes preference value. """
def getHandleIndirectDragPref() -> bool:
    """ Get the handle allow indirect drag preference value. """
def getHandleIndirectTranslatePref() -> bool:
    """ Get the handle allow indirect drag preference value. """
def getHandleHideRingsViewDirPref() -> bool:
    """ Get the handle hide rotate rings parallel to the view direction pref. """
def getHandleShowHiddenPlanesPref() -> bool:
    """ Get the handle allow planar dragging between axes pref. """
def getHandleShowNegativeAxesPref() -> bool:
    """ Get the handle show negative axes pref. """
def getHandlePreferPlanesOverBackfacingAxesPref() -> bool:
    """ Get the handle show negative axes pref. """
def getHandleDefaultGimbalPref() -> bool:
    """ Get the handle show negative axes pref. """
def getHandleClipDistPref() -> float:
    """ Get the clip distance pref. """
def getHandleCenterViewAlignedPref() -> bool:
    """ Get the center view aligned square pref. """
def getHandleAxesOutsidePref() -> bool:
    """ Get the axes outside pref. """
def getHandlePlanesOutsidePref() -> bool:
    """ Get the planes outside pref. """
def getHandleAllViewportsPref() -> bool:
    """ Get the all viewports pref. """
def getHandleAltRotatePref() -> bool:
    """ Get the alt rotate pref. """
def getHandleLineWidthPref() -> float:
    """ Get the line width pref. """
def getHandleBrightnessPref() -> float:
    """ Get the brightness pref. """
def getHandleViewRingScalePref() -> float:
    """ Get the view ring scale pref. """
def getHandleTumbleSphereScalePref() -> float:
    """ Get the tumble sphere scale pref. """
def getHandleGlobalScalePref() -> float:
    """ Get the global handle scale pref. """
def getHandleArrowTipScalePref() -> float: ...
def getHandleCenterBoxScalePref() -> float: ...
def getHandleAxisLengthScalePref() -> float: ...
def getHandleRotateSphereScalePref() -> float: ...
def getHandlePlaneScalePref() -> float: ...
def getHandleShowLabelsPref() -> bool: ...
def getHandleShowRotSpheresPref() -> bool: ...
def getHandleAxisOffsetPref() -> float: ...
def getHandleOutsideAxisScalePref() -> float: ...
def getHandleOutsideAxisOffsetPref() -> float: ...
def getHandleUseLadderPref() -> bool: ...
def getHandleSeparateAlignsPref() -> bool: ...
def getHandleTumbleCombinedPref() -> bool: ...
def getHandleTumbleBorderPref() -> bool: ...
def getHandleDefaultTAlignmentPref() -> int: ...
def getHandleDefaultRAlignmentPref() -> int: ...
def getHandleDefaultSAlignmentPref() -> int: ...
def getHandleSelectIndirectPref() -> bool: ...
def getHandleChangeModeAutoPref() -> bool: ...
def getHandleScaling(scene_viewer: hou.SceneViewer, pos: hou.Vector3, scale_factor: float = 1.0) -> float:
    """
    Compute a handle scaling factor given the scene viewer, the position
    in the scene and an optional scale factor to multiply into it.
    """
def projectToSphere(vec: hou.Vector3, z_axis: hou.Vector3, radius: float, direction: float | None = None) -> hou.Vector3:
    """
    Project the vector 'vec' to a sphere of radius 'radius'.
    The projection is done in a way that the component of 'vec'
    perpendicular to the 'z_axis' does not change, and only
    the parallel component to 'z_axis' is modified so that the
    vector's tip sits on the surface of the sphere.

    If the perpendicular component has length greater than 'radius',
    the vector cannot be projected exactly to the surface. In this
    case, the vector is projected to the plane with normal 'z_axis',
    going through the origin, and the length is modified to be 'radius'.
    """
def intersectGeometry(geo: hou.Geometry, ui_event: hou.ViewerEvent) -> tuple[int, hou.Vector3]:
    """
    Take the ray from the ui_event and use it to intersect with the
    geometry. Return a tuple of the primnum sampled and the position.
    If no intersection found, the primnum is returned as -1.
    """
def pickIntersectDrawable(drawable: hou.AdvancedDrawable, ui_event: hou.ViewerEvent) -> tuple[str | None, int, hou.Vector3]:
    """
    Take the ray from the ui_event and use it to intersect with the
    geometry in the drawable.

    If unsuccessful, return a tuple of (None, -1, (0,0,0))
    If successful, return a tuple of (component name, handle index, intersect pos).
    """

class PickHelper:
    """ Encapsulate checking for picking points and edges, and highlighting
        the located edge or point.
    """
    scene_viewer: hou.SceneViewer
    color_options: ru.ColorOptions
    guide_color: hou.Color
    guide_line: ru.LineSegmentDrawable
    pick_point_geo: hou.Geometry
    pick_point_p: hou.Attrib
    guide_point_drawable: hou.GeometryDrawable
    pick_test_dist: float
    def __init__(self, scene_viewer: hou.SceneViewer, name: str) -> None: ...
    def checkPick(self, ui_event: hou.ViewerEvent) -> tuple[()] | tuple[hou.Vector3] | tuple[hou.Vector3, hou.Vector3]:
        """ Check for a point or edge pick given the ui_event. """
    def show(self, val: bool) -> None:
        """ Show the guides. """
    def setPickPoint(self, pos: hou.Vector3) -> None:
        """ Set the point at 'pos' to be highlighted. """
    def setPickEdge(self, pos0: hou.Vector3, pos1: hou.Vector3) -> None:
        """ Set the edge between pos0 and pos1 to be highlighted. """
    def draw(self, draw_handle: int) -> None:
        """ Draw the pick guides. """

def circleTangentDir(center_pos: hou.Vector3, ring_pos: hou.Vector3, nml: hou.Vector3) -> hou.Vector3:
    """ Get the circles tangent direction (normalized) given the
        center_pos, nml, and the ring_pos position on the circle
        which is where the tangent is evaluated at.
    """

class SpoolDraggerImpl:
    """ Encapsulate the internal logic for the spool dragger
        to be shared between the python state and python handle
        variants derived from hou.ViewerStateDragger and
        hou.ViewerHandleDragger respectively.
    """
    owner: SpoolDragger | SpoolHandleDragger
    def __init__(self, owner: SpoolDragger | SpoolHandleDragger) -> None: ...
    def getDottedLineStart(self) -> hou.Vector3:
        """ Start position of dotted line when dragging. """
    def getDottedLineEnd(self) -> hou.Vector3:
        """ End position of dotted line when dragging. """
    def getRedLineStart(self) -> hou.Vector3:
        """ Start position of red line when dragging. """
    def getRedLineEnd(self) -> hou.Vector3:
        """ End position of red line when dragging. """
    def startSpoolDrag(self, ui_event: hou.ViewerEvent, center_pos: hou.Vector3, radius: float, rotate_axis: hou.Vector3, use_alt_mode: bool, tolerance: float = 0.1) -> None:
        """ Start a spool drag. """
    def updateSpoolDrag(self, ui_event: hou.ViewerEvent) -> float:
        """ Update the spool drag. """
    def pullActive(self) -> bool:
        """ Get whether the pull spool behaviour is active. """
    def center(self) -> hou.Vector3:
        """ Get the center position used in the spool drag. """
    def startPos(self) -> hou.Vector3:
        """ Get the start pick position for the spool drag. """
    def startDir(self) -> hou.Vector3:
        """ Get the start direction for the spool drag. """
    def pos(self) -> hou.Vector3:
        """ Return the last mouse position for the spool drag. """
    def angle(self) -> float:
        """ Return angle in degrees. """
    def quaternion(self) -> hou.Quaternion:
        """ Return the quaternion for the angle from the spool drag. """
    def matrix3(self) -> hou.Matrix3:
        """ Return the rotation matrix3 for the angle from the spool drag. """

class SpoolDragger(hou.ViewerStateDragger):
    """ Encapsulate some of the helper code for setting up a
        rotation drag, with the option for pulling away along
        the tangent from where the ring was originally
        pressed.

        The dragger will compute two angles, one based on
        going around the ring, and another based on the
        projection of the vector connecting the initial press
        position and the current mouse position onto the
        ring's tangent at the initial press point.

        It will choose the pull-out angle only if this gives
        a larger angle, matches the direction, and the round
        about rotate angle is less than one full turn.

        This version of the SpoolDragger will work in python states.
    """
    def __init__(self, *args: str | hou.Matrix4, **kwargs: Unpack[_StateDraggerKwargs]) -> None: ...
    def getDottedLineStart(self) -> hou.Vector3:
        """ Start position of dotted line when dragging. """
    def getDottedLineEnd(self) -> hou.Vector3:
        """ End position of dotted line when dragging. """
    def getRedLineStart(self) -> hou.Vector3:
        """ Start position of red line when dragging. """
    def getRedLineEnd(self) -> hou.Vector3:
        """ End position of red line when dragging. """
    def startSpoolDrag(self, ui_event: hou.ViewerEvent, center_pos: hou.Vector3, radius: float, rotate_axis: hou.Vector3, use_alt_mode: bool, tolerance: float = 0.1) -> None:
        """ Start a spool drag. """
    def updateSpoolDrag(self, ui_event: hou.ViewerEvent) -> float:
        """ Update the spool drag. """
    def pullActive(self) -> bool:
        """ Get whether the pull spool behaviour is active. """
    def center(self) -> hou.Vector3:
        """ Get the center position used in the spool drag. """
    def startPos(self) -> hou.Vector3:
        """ Get the start pick position for the spool drag. """
    def startDir(self) -> hou.Vector3:
        """ Get the start direction for the spool drag. """
    def pos(self) -> hou.Vector3:
        """ Return the last mouse position for the spool drag. """
    def angle(self) -> float:
        """ Return angle in degrees. """
    def quaternion(self) -> hou.Quaternion:
        """ Return the quaternion for the angle from the spool drag. """
    def matrix3(self) -> hou.Matrix3:
        """ Return the rotation matrix3 for the angle from the spool drag. """

class SpoolHandleDragger(hou.ViewerHandleDragger):
    """ Encapsulate some of the helper code for setting up a
        rotation drag, with the option for pulling away along
        the tangent from where the ring was originally
        pressed.

        The dragger will compute two angles, one based on
        going around the ring, and another based on the
        projection of the vector connecting the initial press
        position and the current mouse position onto the
        ring's tangent at the initial press point.

        It will choose the pull-out angle only if this gives
        a larger angle, matches the direction, and the round
        about rotate angle is less than one full turn.

        This version of the SpoolDragger will work in python states.
    """
    def __init__(self, *args: str, **kwargs: Unpack[_HandleDraggerKwargs]) -> None: ...
    def transform(self) -> hou.Matrix4: ...
    def inverseTransform(self) -> hou.Matrix4: ...
    def getDottedLineStart(self) -> hou.Vector3:
        """ Start position of dotted line when dragging. """
    def getDottedLineEnd(self) -> hou.Vector3:
        """ End position of dotted line when dragging. """
    def getRedLineStart(self) -> hou.Vector3:
        """ Start position of red line when dragging. """
    def getRedLineEnd(self) -> hou.Vector3:
        """ End position of red line when dragging. """
    def startSpoolDrag(self, ui_event: hou.ViewerEvent, center_pos: hou.Vector3, radius: float, rotate_axis: hou.Vector3, use_alt_mode: bool, tolerance: float = 0.1) -> None:
        """ Start a spool drag. """
    def updateSpoolDrag(self, ui_event: hou.ViewerEvent) -> float:
        """ Update the spool drag. """
    def pullActive(self) -> bool:
        """ Get whether the pull spool behaviour is active. """
    def center(self) -> hou.Vector3:
        """ Get the center position used in the spool drag. """
    def startPos(self) -> hou.Vector3:
        """ Get the start pick position for the spool drag. """
    def startDir(self) -> hou.Vector3:
        """ Get the start direction for the spool drag. """
    def pos(self) -> hou.Vector3:
        """ Return the last mouse position for the spool drag. """
    def angle(self) -> float:
        """ Return angle in degrees. """
    def quaternion(self) -> hou.Quaternion:
        """ Return the quaternion for the angle from the spool drag. """
    def matrix3(self) -> hou.Matrix3:
        """ Return the rotation matrix3 for the angle from the spool drag. """
