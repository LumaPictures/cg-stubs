# Houdini stubs generated from Houdini 22.0.466

import curveutils as cu
import hou
import resourceutils as ru
import viewerstate.utils as su
from collections.abc import Sequence
from curvestate import constants as constants, referencegeo as referencegeo
from curvestate.baseoperation import BaseOperation as BaseOperation, _CurveState
from houtypes import ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateParmChangeKwargs
from resourceutils import DragGuide
from typing import Any, Unpack

from typing import TypeAlias
from collections.abc import Mapping
_DrawableSelection: TypeAlias = Mapping[str, Mapping[str, list[int]]]
def getEnableDragGuidesPref() -> bool:
    """ Get the value of the enable drag guides preference. """

class DrawableInteractionManager(BaseOperation):
    """
    Class for wrapping all guide geometry for the handles
    and backbone curve
    """
    is_visible: bool
    scene_viewer: hou.SceneViewer
    main_state: _CurveState
    name: str
    viewport_labels: hou.TextDrawable
    curve_simple_drawable: hou.SimpleDrawable | None
    cursor_label: ru.CursorLabel
    drag_guide: DragGuide
    SMOOTH_ANCHOR_GADGET: str
    BROKEN_ANCHOR_GADGET: str
    AUTO_ANCHOR_GADGET: str
    BALANCED_ANCHOR_GADGET: str
    ENDS_SMOOTH_ANCHOR_GADGET: str
    ENDS_BROKEN_ANCHOR_GADGET: str
    ENDS_AUTO_ANCHOR_GADGET: str
    ENDS_BALANCED_ANCHOR_GADGET: str
    HIDDEN_ANCHOR_GADGET: str
    BEZIER_LINES_GADGET: str
    BEZIER_BROKEN_LINES_GADGET: str
    BEZIER_PTS_GADGET: str
    CURVE_GADGET: str
    BEZIER_HIGHER_ORDER_GADGET: str
    ROUNDED_CORNER_GADGET: str
    ORIENT_CIRCLES_LINES_GADGET: str
    ORIENT_CIRCLES_FACES_GADGET: str
    HANDLE_POINT_DRAWABLE: str
    HIGHER_ORDER_POINT_DRAWABLE: str
    LOCATE_SMOOTH_DRAWABLE: str
    LOCATE_BROKEN_DRAWABLE: str
    LOCATE_AUTO_DRAWABLE: str
    LOCATE_BALANCED_DRAWABLE: str
    LOCATE_ENDS_SMOOTH_DRAWABLE: str
    LOCATE_ENDS_BROKEN_DRAWABLE: str
    LOCATE_ENDS_AUTO_DRAWABLE: str
    LOCATE_ENDS_BALANCED_DRAWABLE: str
    DRAWABLE_CLASS_POINTS: int
    DRAWABLE_CLASS_PRIMS: int
    class DrawableSelector(ru.DrawableSelector):
        """ Override to delegate to owner class. """
        parent: DrawableInteractionManager
        def __init__(self, scene_viewer: hou.SceneViewer, parent: DrawableInteractionManager) -> None: ...
        def onLocateSingleSelection(self, kwargs: ViewerStateEventKwargs, result: ru.SingleSelectResult) -> bool: ...
        def onSingleSelection(self, kwargs: ViewerStateEventKwargs, result: ru.SingleSelectResult) -> bool: ...
        def onBoxSelection(self, kwargs: ViewerStateEventKwargs, result: ru.BoxSelectResult) -> bool: ...
        def onLocateBoxSelection(self, kwargs: ViewerStateEventKwargs, result: ru.BoxSelectResult) -> bool: ...
        def onStartBoxSelection(self, kwargs: ViewerStateEventKwargs) -> bool: ...
        def getDragLocate(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    class DrawableSelectorColors(su.DrawableSelectorColors):
        """ Override to access activePickModifier from our drawable selector. """
        drawable_selector: DrawableInteractionManager.DrawableSelector
        def __init__(self, scene_viewer: hou.SceneViewer, drawable_selector: DrawableInteractionManager.DrawableSelector) -> None: ...
    class BezierHandleLines(cu.LineHandleBundle[_CurveState]):
        """ Wrap the bezier handle line drawables. """
        def getSmoothLineGeometry(self) -> hou.Geometry | None:
            """ Get the geometry for smooth handles. """
        def getBrokenLineGeometry(self) -> hou.Geometry | None:
            """ Get the geometry for broken handles. """
        def getGeometry(self, handle_name: str) -> hou.Geometry | None:
            """
            Get the geometry for a given drawable.

            :handle_name: The name of the drawable.
            """
        def getFullGeoPoint(self, handle_geo_point: hou.Point) -> hou.Point | None:
            """
            Get point in the full geometry.

            :handle_geo_point: The point in the handle's sub geometry.
            """
        def initialize(self) -> None:
            """ Called after creating the object. """
    class HiddenControlPointHandle(cu.BasePointHandle[_CurveState]):
        """
        Anchor points.
        Overridden to tell it to use special geometry.
        """
        def getFullGeoPoint(self, handle_geo_point: hou.Point) -> hou.Point | None:
            """
            Get point in the full geometry.

            :handle_geo_point: The point in the handle's sub geometry.
            """
        def initialize(self) -> None:
            """ Called after creating the object. """
        def setPointSize(self, size: int) -> None:
            """
            Set the size of points in the drawables.

            :size: The radius.
            """
    class AnchorPointHiddenHandle(HiddenControlPointHandle):
        """ Hidden drawable for anchor points. """
        def getGeometry(self) -> hou.Geometry | None: ...
    class BezierHigherOrderPoints(HiddenControlPointHandle):
        """ Drawable for bezier higher order points. """
        def getGeometry(self) -> hou.Geometry | None: ...
    class BezierHandlePoints(HiddenControlPointHandle):
        """ Drawable for bezier handle points. """
        def getGeometry(self) -> hou.Geometry | None: ...
    class BackboneCurveHandle(cu.BackboneCurveHandle[_CurveState]):
        """
        For preview curve, also used as a gadget to handle operations
        that need to mouse over the curve, e.g. inserting or dragging curve.
        Overridden to tell it to use special geometry
        """
        def getShownParams(self) -> tuple[cu._DrawableParams, cu._DrawableParams]:
            """ Get the params for the active drawable and the inactive drawable. """
        def getHiddenParams(self) -> tuple[cu._DrawableParams, cu._DrawableParams]:
            """ Get params for active and inactive hidden drawables. """
        def updateParams(self, show_preview_curve: bool) -> None:
            """
            Update params for active and inactive drawables.

            :show_preview_curve: Whether the preview curve is visible.
                This decides whether we pull the params from
                self.getShownParams() or self.getHiddenParams()
            """
        def getGeometry(self) -> hou.Geometry | None:
            """ Get the geometry for the preview curve."""
        def getRealGeoPrim(self, handle_geo_prim: hou.Prim) -> hou.Prim | None:
            """
            Get the prim in the full geometry.

            :handle_geo_prim: The prim object in the drawable subset geo.
            """
        def getPointUpos(self, point: hou.Point) -> float:
            """ Get point u position from the attribute. """
        def getVertexUpos(self, vertex: hou.Vertex) -> float:
            """
            Get the vertex u position from the point.

            NOTE: We are assuming the preview curve that was computed
                  has no branch points here, which is valid if all the curves
                  have been passed through a resample.

            :vertex: The vertex in the curve on the resampled geo.
            """
    class BasePointVisualizer(cu.PointSelectorBundle[_CurveState]):
        """ Wrap drawables for selected points. """
        def __init__(self, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
        def getDrawableList(self) -> list[str]: ...
        def getGeometry(self, name: str) -> hou.Geometry | None: ...
    class BezierPointVisualizer(BasePointVisualizer):
        """ Wrapper for visualizing all types of bezier points. """
        include_handles: bool
        def __init__(self, scene_viewer: hou.SceneViewer, main_state: _CurveState, include_handles: bool = False) -> None: ...
        def getDrawableList(self) -> list[str]:
            """ Get the list of drawables to show. """
        def getGeometry(self, name: str) -> hou.Geometry | None:
            """ Get geometry for a given drawable by name. """
        def initialize(self) -> None:
            """ Called after construction. """
        def endsPointSize(self) -> float: ...
        def getHandleColor(self) -> hou.Color:
            """ Color for handle axes. """
        def getColor(self) -> hou.Color:
            """ Color for points. """
        def getBrokenDrawable(self) -> str:
            """ Drawable name of broken anchors. """
        def getSmoothDrawable(self) -> str:
            """ Drawable name of smooth anchors. """
        def getBalancedDrawable(self) -> str:
            """ Drawable name of balanced anchors. """
        def getAutoDrawable(self) -> str:
            """ Drawable name of auto anchors. """
        def getEndsBrokenDrawable(self) -> str: ...
        def getEndsSmoothDrawable(self) -> str: ...
        def getEndsBalancedDrawable(self) -> str: ...
        def getEndsAutoDrawable(self) -> str: ...
        def getHandlePointDrawable(self) -> str:
            """ Drawable name of handle points. """
        def getHigherOrderPointDrawable(self) -> str:
            """ Drawable name of higher order intermediate points. """
        def getBrokenGeometry(self) -> hou.Geometry | None:
            """ Broken anchor geometry. """
        def getSmoothGeometry(self) -> hou.Geometry | None:
            """ Smooth anchor geometry. """
        def getBalancedGeometry(self) -> hou.Geometry | None:
            """ Balanced anchor geometry. """
        def getAutoGeometry(self) -> hou.Geometry | None:
            """ Auto anchor geometry. """
        def getEndsBrokenGeometry(self) -> hou.Geometry | None: ...
        def getEndsSmoothGeometry(self) -> hou.Geometry | None: ...
        def getEndsBalancedGeometry(self) -> hou.Geometry | None: ...
        def getEndsAutoGeometry(self) -> hou.Geometry | None: ...
        def getHandlePointGeometry(self) -> hou.Geometry | None:
            """ Handle end point geometry. """
        def getHigherOrderGeometry(self) -> hou.Geometry | None:
            """ Higher order indermediate geometry. """
    class BezierPointLocator(BezierPointVisualizer):
        """ Drawables for when locating points. """
        shown_drawables: list[str]
        def __init__(self, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
        def getAnchorGeometry(self) -> hou.Geometry | None:
            """ Bezier anchor geometry. """
        def getBrokenGeometry(self) -> hou.Geometry | None:
            """ Full anchor geometry. """
        def getSmoothGeometry(self) -> hou.Geometry | None:
            """ Full anchor geometry. """
        def getBalancedGeometry(self) -> hou.Geometry | None:
            """ Full anchor geometry. """
        def getAutoGeometry(self) -> hou.Geometry | None:
            """ Full anchor geometry. """
        def getEndsBrokenGeometry(self) -> hou.Geometry | None: ...
        def getEndsSmoothGeometry(self) -> hou.Geometry | None: ...
        def getEndsBalancedGeometry(self) -> hou.Geometry | None: ...
        def getEndsAutoGeometry(self) -> hou.Geometry | None: ...
        def getBrokenDrawable(self) -> str:
            """ Drawable name for located broken points. """
        def getSmoothDrawable(self) -> str:
            """ Drawable name for located smooth points. """
        def getBalancedDrawable(self) -> str:
            """ Drawable name for located balanced points. """
        def getAutoDrawable(self) -> str:
            """ Drawable name for located auto points. """
        def getEndsBrokenDrawable(self) -> str: ...
        def getEndsSmoothDrawable(self) -> str: ...
        def getEndsBalancedDrawable(self) -> str: ...
        def getEndsAutoDrawable(self) -> str: ...
        def show(self, val: bool) -> None:
            """ Show/hide all of these drawables. """
        def updateDrawableSelection(self, drawable_selection: _DrawableSelection, color: hou.Color | Sequence[float]) -> None:
            """ Update the located points from the drawable selection. """
        def draw(self, draw_handle: hou.Handle) -> None:
            """ Draw the located points. """
    class RoundedCornerWidgetPoints(cu.RoundedCornerWidgetPoints[_CurveState]):
        """ Round corner widgets. """
        def getGeometry(self) -> hou.Geometry | None:
            """ Get the round corner widget geometry. """
        def getFullGeoPoint(self, handle_geo_point: hou.Point) -> hou.Point | None:
            """ Get the point the widget corresponds to. """
    class BaseGeoDrawer:
        """ Base class to make some drawables that are always non-interactive. """
        scene_viewer: hou.SceneViewer
        main_state: _CurveState
        color_options: ru.ColorOptions
        point_drawable: hou.GeometryDrawable
        node: hou.SopNode | None
        def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
        def setNode(self, node: hou.SopNode | None) -> None: ...
        def setParams(self, params: cu._DrawableParams) -> None: ...
        def initialize(self) -> None: ...
        def show(self, val: bool) -> None: ...
        def draw(self, draw_handle: hou.Handle) -> None: ...
        def updateConfig(self, kwargs: ViewerStateDrawKwargs) -> None: ...
        def createDrawable(self, name: str) -> hou.GeometryDrawable: ...
        def getParams(self) -> cu._DrawableParams: ...
        def getGeometry(self) -> hou.Geometry | None: ...
    class BaseGeoLineDrawer(BaseGeoDrawer):
        """ Base class for line drawables. """
        def createDrawable(self, name: str) -> hou.GeometryDrawable: ...
    class BezierPseudoEndPoints(BaseGeoDrawer):
        """ Drawable for bezier inactive handle end points. """
        def getParams(self) -> cu._DrawableParams: ...
        def getGeometry(self) -> hou.Geometry | None: ...
    class BezierLocateEndPoints(BaseGeoDrawer):
        """ Drawable for located end points. """
        geometry: hou.Geometry
        def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
        def setLocatePoint(self, ptnum: int) -> None:
            """ Set the given point number to be located. """
        def clearLocatePoint(self) -> None: ...
        def getParams(self, is_anchor: bool = False, is_broken: bool = False) -> cu._DrawableParams:
            """
            Get the params to draw the point.

            :is_anchor: Whether we draw the point as an anchor point.
            :is_broken: If the point is an anchor point, whether we draw
                a square or a circle.
            """
        def getGeometry(self) -> hou.Geometry: ...
    class BezierPseudoSmoothLines(BaseGeoLineDrawer):
        """ Drawable wrapper for inactive handles for smooth lines. """
        def getParams(self) -> cu._DrawableParams: ...
        def getGeometry(self) -> hou.Geometry | None: ...
    class BezierPseudoBrokenLines(BaseGeoLineDrawer):
        """ Drawable wrapper for inactive handles for broken lines. """
        def getParams(self) -> cu._DrawableParams: ...
        def getGeometry(self) -> hou.Geometry | None: ...
    class SelectRoundedCornerWidgetPoints(BaseGeoDrawer):
        """ Show selected rounded corners. """
        def getParams(self) -> cu._DrawableParams: ...
        def getGeometry(self) -> hou.Geometry | None:
            """ Get geometry for selected rounded corner widgets. """
    class LocateRoundedCornerWidgetPoints(BaseGeoDrawer):
        """ Show selected rounded corners. """
        show_located: bool
        visible: bool
        def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
        def getParams(self) -> cu._DrawableParams: ...
        def getGeometry(self) -> hou.Geometry | None:
            """ Get geometry for rounded corner widgets. """
        def show(self, val: bool) -> None: ...
        def updateLocateIndices(self, point_indices: Sequence[int]) -> None: ...
        def updateDrawableSelection(self, drawable_selection: _DrawableSelection, color: hou.Color | Sequence[float]) -> None:
            """ Update from the drawable selection dictionary. """
    class CurveBackbone(BaseGeoLineDrawer):
        """ Used for the cage curve on nurbs and higher order bezier. """
        def getParams(self) -> cu._DrawableParams: ...
        def getGeometry(self) -> hou.Geometry | None:
            """ Get backbone geo. """
    class AutoPoints(BaseGeoDrawer):
        """ Draw rings around auto points. """
        def pointSize(self) -> int: ...
        def getColor(self) -> hou.Color: ...
        def getParams(self) -> cu._DrawableParams: ...
        def getGeometry(self) -> hou.Geometry | None:
            """ Get geometry for auto points. """
    class EndAutoPoints(AutoPoints):
        """ Draw rings around end auto points. """
        def pointSize(self) -> int: ...
        def getGeometry(self) -> hou.Geometry | None:
            """ Get geometry for auto points. """
    class OrientGuide(BaseGeoDrawer):
        """ Drawable for gnomons along curves. """
        density_scale: float
        scale: float
        enable: bool
        def __init__(self, *args: Unpack[tuple[str, hou.SceneViewer, _CurveState]]) -> None: ...
        def createDrawable(self, name: str) -> hou.GeometryDrawable: ...
        def getParams(self) -> cu._DrawableParams: ...
        def getGeometry(self) -> hou.Geometry | None:
            """ Get geometry for orient guides along the curve. """
        def updateConfig(self, kwargs: ViewerStateDrawKwargs) -> None:
            """ Update the configuration using using the state parms. """
    class OrientCirclesLines(cu.BackboneCurveHandle[_CurveState]):
        """ Drawable for the orient circle lines. """
        def initialize(self) -> None:
            """ Called after constructing the object to set params. """
        def getGeometry(self) -> hou.Geometry | None:
            """ Get the orient circle lines geometry. """
    class OrientCirclesFaces(cu.BaseFaceHandle[_CurveState]):
        """ Drawable for orient circle faces. """
        def initialize(self) -> None:
            """ Called after constructing the object to set params. """
        def getGeometry(self) -> hou.Geometry | None:
            """ Get the orient face geometry. """
    bezier_handle_lines: DrawableInteractionManager.BezierHandleLines
    bezier_handle_points: DrawableInteractionManager.BezierHandlePoints
    bezier_higher_order_points: DrawableInteractionManager.BezierHigherOrderPoints
    bezier_control_point_handle: DrawableInteractionManager.AnchorPointHiddenHandle
    pseudo_bezier_smooth_lines: DrawableInteractionManager.BezierPseudoSmoothLines
    pseudo_bezier_broken_lines: DrawableInteractionManager.BezierPseudoBrokenLines
    pseudo_bezier_end_points: DrawableInteractionManager.BezierPseudoEndPoints
    backbone_curve_handle: DrawableInteractionManager.BackboneCurveHandle
    rounded_corner_handle: DrawableInteractionManager.RoundedCornerWidgetPoints
    select_round_corner_widgets: DrawableInteractionManager.SelectRoundedCornerWidgetPoints
    locate_round_corner_widgets: DrawableInteractionManager.LocateRoundedCornerWidgetPoints
    bezier_point_locator: DrawableInteractionManager.BezierPointLocator
    bezier_point_visualizer: DrawableInteractionManager.BezierPointVisualizer
    bezier_handle_locator: DrawableInteractionManager.BezierLocateEndPoints
    higher_order_backbone_handle: DrawableInteractionManager.CurveBackbone
    auto_points: DrawableInteractionManager.AutoPoints
    auto_end_points: DrawableInteractionManager.EndAutoPoints
    orient_guide: DrawableInteractionManager.OrientGuide
    orient_circles_lines: DrawableInteractionManager.OrientCirclesLines
    orient_circles_faces: DrawableInteractionManager.OrientCirclesFaces
    drawable_selector: DrawableInteractionManager.DrawableSelector
    drawable_selector_colors: DrawableInteractionManager.DrawableSelectorColors
    def __init__(self, name: str, scene_viewer: hou.SceneViewer, main_state: _CurveState) -> None: ...
    def getDrawableSelector(self) -> DrawableInteractionManager.DrawableSelector:
        """ Return the drawable selector instance. """
    def getPointNumbers(self, drawable_name: str, drawable_indices: Sequence[int]) -> list[int]:
        """ Get the point numbers given the drawable name and indices. """
    def setLocateIndices(self, drawable_selection: _DrawableSelection) -> None:
        """ Set located points from a drawable selection. """
    def setLocateSinglePoint(self, ptnum: int) -> None:
        """ Set a point to be located. """
    def clearLocateSinglePoint(self) -> None:
        """ Clear located point. """
    def setCursorLabel(self, label: str | None) -> None:
        """ Set the label for the cursor. """
    def _setCursorParms(self, kwargs: ViewerStateEventKwargs) -> None:
        """ Set params for cursor label. """
    def setPickingCurve(self, val: bool) -> None:
        """ Set whether we want to enable picking on curves. """
    def setPickingAnchors(self, val: bool) -> None:
        """ Set whether we want to enable picking on anchor points. """
    def setPickingHandles(self, val: bool) -> None:
        """ Set whether we want to enable picking on handles. """
    def reactNodeParmsUpdate(self, event_type: hou.EnumValue[hou.nodeEventType], node: hou.SopNode, **kwargs: Any) -> None:
        """ React to a node parameter change. """
    def updateNode(self) -> None:
        """ Update the node references. """
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """ Called when entering the state. """
    def updateFromPrefs(self) -> None:
        """ Called to update from ALL relevant preferences. """
    def onPrefChanged(self, pref_name: str) -> None:
        """ Called when a single preference changes. """
    def getBezierHandleLines(self) -> DrawableInteractionManager.BezierHandleLines: ...
    def getBezierHandlePoints(self) -> DrawableInteractionManager.BezierHandlePoints: ...
    def getBackboneCurveHandle(self) -> DrawableInteractionManager.BackboneCurveHandle: ...
    def getBezierControlPointHandle(self) -> DrawableInteractionManager.AnchorPointHiddenHandle: ...
    def getHighlightCurveHandle(self) -> cu.HighlightCurveSection: ...
    def getRoundedCornerHandle(self) -> DrawableInteractionManager.RoundedCornerWidgetPoints: ...
    def getBezierHigherOrderPointHandle(self) -> DrawableInteractionManager.BezierHigherOrderPoints: ...
    def getOrientCirclesLinesHandle(self) -> DrawableInteractionManager.OrientCirclesLines: ...
    def getOrientCirclesFacesHandle(self) -> DrawableInteractionManager.OrientCirclesFaces: ...
    def show(self, val: bool) -> None:
        """ Show or hide all the drawables. """
    def drawRoundedCornerWidgets(self, draw_handle: hou.Handle) -> None:
        """ Draw the rounded corner widgets. """
    def inOrientMode(self) -> bool:
        """ Whether we are in orient mode. """
    def drawOrientGuideGeometry(self, kwargs: ViewerStateDrawKwargs) -> None:
        """ Draw the orient guide geometry. """
    def drawHighlightCurveSection(self, draw_handle: hou.Handle) -> None:
        """ Draw a single section of the curve. """
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None:
        """ Draw the main set of drawables for the state. """
    def drawableSelectorClasses(self) -> list[list[hou.SimpleDrawable | hou.AdvancedDrawable]]:
        """
        Generate the lists of drawables to pick against.

        First pick against points drawables, then pick against handles,
        and then finally pick against curves.

        This defines the picking priorities.
        """
    def enableDrawableSelector(self, on: bool) -> None:
        """ Enable or disable the drawable selector. """
    def enableDrawableBoxSelector(self, on: bool) -> None:
        """ Enable or disable box selecting with the drawable selector. """
    def onLocateSingleSelection(self, kwargs: ViewerStateEventKwargs, result: ru.SingleSelectResult) -> bool:
        """ Called when locating a single pick from the drawable selector. """
    def checkPickHandlePts(self, kwargs: ViewerStateEventKwargs, elem_tuple: ru.SinglePickTuple, drawable: hou.GeometryDrawable) -> bool: ...
    def checkPickHandleLines(self, kwargs: ViewerStateEventKwargs, elem_tuple: ru.SinglePickTuple, drawable: hou.GeometryDrawable, ray_orig: hou.Vector3, ray_dir: hou.Vector3) -> bool: ...
    def checkPickAnchorPts(self, kwargs: ViewerStateEventKwargs, elem_tuple: ru.SinglePickTuple, drawable: hou.GeometryDrawable) -> bool: ...
    def checkPickRoundedCorners(self, kwargs: ViewerStateEventKwargs, elem_tuple: ru.SinglePickTuple, drawable: hou.GeometryDrawable) -> bool: ...
    def checkPickCurve(self, kwargs: ViewerStateEventKwargs, elem_tuple: ru.SinglePickTuple, drawable: hou.GeometryDrawable, ray_orig: hou.Vector3, ray_dir: hou.Vector3) -> bool: ...
    def checkPickOrientCirclesLines(self, kwargs: ViewerStateEventKwargs, elem_tuple: ru.SinglePickTuple, drawable: hou.GeometryDrawable, ray_orig: hou.Vector3, ray_dir: hou.Vector3) -> bool: ...
    def checkPickOrientCirclesFaces(self, kwargs: ViewerStateEventKwargs, elem_tuple: ru.SinglePickTuple, drawable: hou.GeometryDrawable, ray_orig: hou.Vector3, ray_dir: hou.Vector3) -> bool: ...
    def checkSinglePickDrawables(self, kwargs: ViewerStateEventKwargs, elem_tuple: ru.SinglePickTuple, drawable: hou.GeometryDrawable) -> bool:
        """
        Check single picks for each of the drawables.

        :kwargs: The kwargs dict given to onMouseEvent.
        :elem_tuple: The element numbers picked.
        :drawable: The drawable to reference.
        """
    def onSingleSelection(self, kwargs: ViewerStateEventKwargs, result: ru.SingleSelectResult) -> bool:
        """ Called after doing a single selection with the drawable selector. """
    def onStartBoxSelection(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Called after starting a box selection by the drawable selector. """
    def onBoxSelection(self, kwargs: ViewerStateEventKwargs, result: ru.BoxSelectResult) -> bool:
        """ Called on finishing a box selection by the drawable selector. """
    def onLocateBoxSelection(self, kwargs: ViewerStateEventKwargs, result: ru.BoxSelectResult) -> bool:
        """ Called on locating a box selection by the drawable selector. """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, snap_pt: hou.Point | None = None, snap_prim: hou.Prim | None = None, snap_upos: float | None = None, snap_pos: hou.Vector3 | None = None) -> bool:
        """
        Send the mouse event to each of the gadgets, which may call a
        registered callback.
        """
    def getDragGuide(self) -> DragGuide:
        """ Get the drag guide. """
    def enableDragGuide(self, val: bool) -> None:
        """ Enable or disable the drag guides. """
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None: ...
