import hou
import typing
from collections.abc import Collection, Container, Iterable, Iterator, Sequence
from houtypes import ViewerStateSelectionKwargs
from kinefx import attribwatcher as attribwatcher, rigapi as rigapi
from kinefx.attribwatcher import AttributeWatcher as AttributeWatcher
from kinefx.stateutils import KinefxPackedHighlighter as KinefxPackedHighlighter, ViewerStateDisplayOptions as ViewerStateDisplayOptions, _LocatedSelection, _MouseSelectionArgs, _PickModifier, _PreSelection
from viewerstate.utils import GeometryIntersector

from typing import TypeAlias
from typing import Literal
from typing import TypeAlias
_PointState: TypeAlias = Literal['enabled', 'disabled']
_GeoMod: TypeAlias = Sequence[int]
def addInvalidBounds(geo: hou.Geometry) -> None:
    """
    
    """
def getGeoHiddenPts(geo: hou.Geometry | None) -> set[hou.Point]:
    """
    Get all the points in **geo** that have a dictionary attribute 'rig_display', with rig_display['joint']['visible'] key 
    set to False.
    Used to determine which points to hide in the state.

    :param geo: geometry to get the hidden points from
    :type geo: hou.Geometry
    :return: hidden points
    :rtype: set of int
    """

class DrawableConstants:
    """
    UI Size constants for drawables.
    """
    joint_scale: float
    axis_scale: float
    joint_pixel_size: float
    ring_pixel_size: float
    text_margin: float
    popup_left: float
    popup_width: float
    joint_falloff_size: float
    glow_falloff_size: float
    @staticmethod
    def glow_size(v: float) -> int:
        """
        Set the glow width of the visualisers and keep them in pixel space.
        Clamp the minimum value to 1.
        """
    glow_pixel_size: int
    text_glow_pixel_size: int
    glow_link_size: int
    font_size: float
    @classmethod
    def setAxisScale(cls, s: float) -> None:
        """
        Clamp the scale value of the axes visualisers to 0.1 and 10.

        :param s: scale value
        :type s: float
        """
    @classmethod
    def setJointScale(cls, s: float) -> None:
        """
        Clamp the scale value of the point visualisers to 0.1 and 4.
        Handle the scaling of all of the elements associated with the point visualiser: popup, locating ring, glow.

        :param s: scale value
        :type s: float
        """
    @classmethod
    def updateScales(cls, dist: float, update_jointscale: bool = False, update_axesscale: bool = False) -> bool:
        """
        Update the scales of the point, axes visualisers, by **dist**.

        :param dist: value to add to the current scales(scroll value from onMouseWheelEvent for example)
        :type dist: float
        :param update_jointscale: whether to update the scale of the point visualsier or not
        :type update_jointscale: bool
        :param update_axesscale: whether to update the scale of the axes visualsier or not
        :type update_axesscale: bool
        :return: whether any scales have been updated
        :rtype: bool
        """
    @classmethod
    def getJointScale(cls) -> float:
        """
        Get the point visualiser scale value.

        :return: point visualiser scale value
        :rtype: float
        """
    @classmethod
    def getAxisScale(cls) -> float:
        """
        Get the axes visualiser scale value.

        :return: axes visualiser scale value
        :rtype: float
        """

class KinefxPointDrawable:
    """
    Build the KineFX point visualiser and provide support methods for interacting with it.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param geo: geometry to build the visualiser for
    :type geo: hou.Geometry
    """
    scene_viewer: hou.SceneViewer
    geo: hou.Geometry
    attribwatcher: AttributeWatcher
    drawable: hou.GeometryDrawable
    target_point_params: hou._DrawableParams
    highlight_color: tuple[float, float, float, float]
    highlight_params: hou._DrawableParams
    highlight_drawable: hou.GeometryDrawable
    prehighlight_drawable: hou.GeometryDrawable
    _prehighlight_draw: bool
    hidden_points: set[hou.Point]
    temp_hidden_points: set[hou.Point]
    visible_points: set[hou.Point]
    hide_all: bool
    def __init__(self, scene_viewer: hou.SceneViewer, geo: hou.Geometry | None, name: str | None = None) -> None:
        """
        Constructor method.
        """
    def updateDrawableScales(self) -> None:
        """
        Update the visualiser scale from the `DrawableConstants` scene variables.
        """
    def setMainDrawableParams(self, params: hou._DrawableParams) -> None:
        """
        Set the main visualiser parameters.

        :param params: parameters to set
        :type params: dict
        """
    def setGeometry(self, geo: hou.Geometry | None) -> None:
        """
        Set the geometry of the visualiser.

        :param geo: geometry to set
        :type geo: hou.Geometry
        """
    def highlight(self, pts: Iterable[hou.Point] | None, clear: bool = False) -> None:
        """
        Mark the visualisers belonging to **pts** for highlighting in `onDraw`.

        :param pts: points to highlight
        :type pts: list or tuple of hou.Point
        :param clear: whether to replace the current highlight or merge with it
        :type clear: bool
        """
    def prehighlight(self, pts: Iterable[hou.Point] | None, clear: bool = False) -> None:
        """
        Mark the visualisers belonging to **pts** for prehighlighting in `onDraw`.

        :param pts: points to prehighlight
        :type pts: list or tuple of hou.Point
        :param clear: whether to replace the current prehighlight or merge with it
        :type clear: bool
        """
    def hidePoints(self, pts: Iterable[hou.Point], clear: bool = True) -> None:
        """
        Mark the visualisers belonging to **pts** for being hidden in `onDraw`.

        :param pts: points to hide
        :type pts: list or tuple of hou.Point
        :param clear: whether to replace the current hidden points or merge with them
        :type clear: bool
        """
    def showPoints(self, pts: Iterable[hou.Point], clear: bool = True) -> None:
        """
        Mark the visualisers belonging to **pts** for being shown(if they had been hidden) in `onDraw`.

        :param pts: points to show
        :type pts: list or tuple of hou.Point
        :param clear: whether to show only **pts** from the whole geometry(True) or to remove **pts** from the current hidden points(False)
        :type clear: bool
        """
    def show(self, on: bool) -> None:
        """
        Show or hide the visualiser.

        :param on: whether to show or hide the visualiser
        :type on: bool
        """
    def draw(self, draw_handle: int, color: hou._DrawableColor | None = None) -> None:
        """
        Draw the point visualiser.
        Handle hiding and showing, prehighlighting and highlighting points.

        :param draw_handle: handle for performing the render operation
        :type draw_handle: int
        :param color: color of the point visualiser
        :type color: hou.Vector4
        """
    def getPointsFromIndices(self, indices: Collection[int]) -> list[hou.Point]:
        """
        Takes a list of indices of points on the rig visualiser's geometry
        and returns the corresponding list of points without duplicates.

        :param indices: A list of indices of points on the rig visualiser's
                        geometry
        :type indices: Tuple of Int
        :return: The corresponding set of points.
        :rtype: Tuple of Point
        """
    def onSelection(self, kwargs: ViewerStateSelectionKwargs) -> list[hou.Point]:
        """
        A handler for the viewer state's onSelection handler which is called
        when selections on drawables are identified.

        :param kwargs: The dictionary for the onSelection handler.
        :type kwargs: dict
        :return: A list of points selected on the rig visualiser's geometry.
        :rtype: Tuple of hou.Point
        """
    def drawableMask(self) -> list[str]:
        """
        Returns a list of the names of drawables that can be located by the
        onLocatedSelection callback.

        :return: A list of the names of the drawables owned by this
                 KinfexPointDrawable that can be located by the
                 onLocatedSelection callback.
        :rtype: Tuple of Strings
        """
    def onLocatedSelection(self, kwargs: ViewerStateSelectionKwargs) -> list[hou.Point]:
        """
        A handler for the viewer state's onLocatedSelection handler which is
        called when selections on drawables are identified.

        :param kwargs: The dictionary for the onLocatedSelection handler.
        :type kwargs: dict
        """
    def setPreHighlightColor(self, pick_mod: _PickModifier) -> None:
        """
        Sets the color of the pre-highlighted points based upon the requested
        pick modifier.

        :param pick_mod: The pick modifier.
        :type pick_mod: hou.pickModifier
        """
    def intersect(self, ui_event: hou.UIEvent) -> tuple[hou.Point, float] | tuple[None, float] | tuple[None, None]:
        """
        Get the intersected point visualiser.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        :return: intersected edge and the geometry intersection world position 
        :rtype: point snapped to and distance from the mouse cursor to that point
        .. note::
            If geometry is invalid, returns None, None.
        """

class KinefxLinkDrawable:
    """
    Build the KineFX bone link visualiser - wireframe and solid - and provide support methods for interacting with it.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param geo: geometry to build the visualiser for
    :type geo: hou.Geometry
    """
    scene_viewer: hou.SceneViewer
    geo: hou.Geometry
    geo_mod: _GeoMod
    line_width: int
    attribwatcher: AttributeWatcher
    show_solid: bool
    global_scale: float
    line_drawable: hou.GeometryDrawable
    def_color: hou.Vector4
    solid_drawable: hou.GeometryDrawable
    highlight_drawable: hou.GeometryDrawable
    prehighlight_drawable: hou.GeometryDrawable
    copyverb: hou.SopVerb
    visible_points: set[hou.Point]
    hidden_points: set[hou.Point]
    temp_hidden_points: set[hou.Point]
    def __init__(self, scene_viewer: hou.SceneViewer, geo: hou.Geometry | None, name: str | None = None) -> None:
        """
        Constructor method.
        """
    def setGeometry(self, geo: hou.Geometry | None) -> None:
        """
        Set the visualiser geometry.

        :param geo: new geometry to set
        :type geo: hou.Geometry
        """
    def highlight(self, edges: Iterable[hou.Edge] | None, clear: bool = False) -> None:
        """
        Mark the visualisers belonging to **edges** for highlighting in `onDraw`.

        :param edges: edges to highlight
        :type edges: list or tuple of hou.Edge
        :param clear: whether to replace the current highlight or merge with it
        :type clear: bool
        """
    def prehighlight(self, edges: Iterable[hou.Edge] | None, clear: bool = False) -> None:
        """
        Mark the visualisers belonging to **edges** for prehighlighting in `onDraw`.

        :param edges: edges to prehighlight
        :type edges: list or tuple of hou.Edge
        :param clear: whether to replace the current prehighlight or merge with it
        :type clear: bool
        """
    def show(self, on: bool) -> None:
        """
        Show or hide the visualiser.

        :param on: whether to show or hide the visualiser
        :type on: bool
        """
    def hidePoints(self, pts: Iterable[hou.Point], clear: bool = True, setdirty: bool = True) -> None:
        """
        Mark the visualisers belonging to **pts** for being hidden in `onDraw`.

        :param pts: points to hide
        :type pts: list or tuple of hou.Point
        :param clear: whether to replace the current hidden points or merge with them
        :type clear: bool
        :param setdirty: flag to mark the visualiser geometry for update on next draw
        :type setdirty: bool
        """
    def showPoints(self, pts: Iterable[hou.Point], clear: bool = True) -> None:
        """
        Mark the visualisers belonging to **pts** for being shown(if they had been hidden) in `onDraw`.

        :param pts: points to show
        :type pts: list or tuple of hou.Point
        :param clear: whether to show only **pts** from the whole geometry(True) or to remove **pts** from the current hidden points(False)
        :type clear: bool
        """
    def draw(self, draw_handle: int, color: hou._DrawableColor | None = None) -> None:
        """
        Draw the bone link visualiser.
        Handle hiding and showing points, prehighlighting and highlighting edges.

        :param draw_handle: handle for performing the render operation
        :type draw_handle: int
        :param color: color of the bone link visualiser
        :type color: hou.Vector4
        """
    def getEdgesFromPrimIndices(self, indices: Collection[int]) -> list[hou.Edge]:
        """
        Takes a tuple of indices of edges on the bone geometry and returns
        the corresponding list of edges.

        :param indices: A list of indices of edges on the bone geometry.
        :type indices: Tuple of Int
        :return: The edges on the rig visualiser's geometry which corresponds
                 to the bones.
        :rtype: Tuple of Edge
        """
    def getEdgesFromPointIndices(self, indices: Sequence[int]) -> list[hou.Edge]: ...
    def onSelection(self, kwargs: ViewerStateSelectionKwargs) -> list[hou.Edge]:
        """
        A handler for the viewer state's onSelection handler which is called
        when selections on drawables are identified.

        :param kwargs: The dictionary for the onSelection handler.
        :type kwargs: dict
        :return: A list of edges selected on the rig visualiser's geometry.
        :rtype: Tuple of hou.Edge
        """
    def drawableMask(self) -> list[str]:
        """
        Returns a list of the names of drawables that can be located by the
        onLocatedSelection callback.

        :return: A list of the names of the drawables owned by this
                 KinfexLinkDrawable that can be located by the
                 onLocatedSelection callback.
        :rtype: Tuple of Strings
        """
    def onLocatedSelection(self, kwargs: ViewerStateSelectionKwargs) -> list[hou.Edge]:
        """
        A handler for the viewer state's onLocatedSelection handler which is
        called when selections on drawables are identified.

        :param kwargs: The dictionary for the onLocatedSelection handler.
        :type kwargs: dict
        """
    def setPreHighlightColor(self, pick_mod: _PickModifier) -> None:
        """
        Sets the color of the pre-highlighted edges based upon the requested
        pick modifier.

        :param pick_mod: The pick modifier
        :type pick_mod: hou.pickModifier
        """
    def intersect(self, ui_event: hou.ViewerEvent) -> tuple[hou.Edge | None, hou.Vector3] | tuple[None, None]:
        """
        Get the intersected bone link visualiser.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        :return: intersected edge and the geometry intersection world position 
        :rtype: hou.Edge, hou.Vector3
        .. note::
            If geometry is invalid, returns None, None.
        """

class KinefxAxisDrawable:
    """
    Build the KineFX point axes visualiser and provide support methods for interacting with it.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param template_geo: geometry to build the visualiser for
    :type template_geo: hou.Geometry
    :param instance_geo: visualiser geometry to instanciate on each point
    :type instance_geo: hou.Geometry
    """
    axis_size: int
    line_width: int
    scene_viewer: hou.SceneViewer
    geo: hou.Geometry
    geo_mod: _GeoMod
    template_normalize_transforms: bool
    attribwatcher: AttributeWatcher
    drawable: hou.GeometryDrawable
    copyverb: hou.SopVerb
    visible_points: set[hou.Point]
    hidden_points: set[hou.Point]
    temp_hidden_points: set[hou.Point]
    def __init__(self, scene_viewer: hou.SceneViewer, template_geo: hou.Geometry, instance_geo: hou.Geometry, name: str | None = None) -> None:
        """
        Constructor method.
        """
    def setGeometry(self, geo: hou.Geometry) -> None:
        """
        Set the geometry of the visualiser.

        :param geo: geometry to set
        :type geo: hou.Geometry
        """
    def show(self, on: bool) -> None:
        """
        Show or hide the visualiser.

        :param on: whether to show or hide the visualiser
        :type on: bool
        """
    def hidePoints(self, pts: Iterable[hou.Point], clear: bool = True) -> None:
        """
        Mark the visualisers belonging to **pts** for being hidden in `onDraw`.

        :param pts: points to hide
        :type pts: list or tuple of hou.Point
        :param clear: whether to replace the current hidden points or merge with them
        :type clear: bool
        """
    def showPoints(self, pts: Iterable[hou.Point], clear: bool = True) -> None:
        """
        Mark the visualisers belonging to **pts** for being shown(if they had been hidden) in `onDraw`.

        :param pts: points to show
        :type pts: list or tuple of hou.Point
        :param clear: whether to show only **pts** from the whole geometry(True) or to remove **pts** from the current hidden points(False)
        :type clear: bool
        """
    def draw(self, draw_handle: int, color: hou._DrawableColor | None = None) -> None:
        """
        Draw the point axes visualiser.
        Handle hiding and showing points.

        :param draw_handle: handle for performing the render operation
        :type draw_handle: int
        :param color: color of the point axes visualiser
        :type color: hou.Vector4
        """

class KinefxFaceGeoDrawable:
    """
    -NON-POLYGONAL GEOMETRY NOT SUPPORTED ATM FOR ADVANCED DRAWABLES SO THIS METHOD IS NOT CURRENTLY IN USE-
    Build the KineFX control geometry visualiser and provide support methods for interacting with it.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param template_geo: geometry to build the visualiser for
    :type template_geo: hou.Geometry
    """
    scene_viewer: hou.SceneViewer
    geo: hou.Geometry
    geo_mod: _GeoMod
    attribwatcher: AttributeWatcher
    drawable: hou.GeometryDrawable
    highlight_drawable: hou.GeometryDrawable
    copyverb: hou.SopVerb
    transform: hou.Matrix4
    point_states: list[_PointState]
    def __init__(self, scene_viewer: hou.SceneViewer, template_geo: hou.Geometry) -> None:
        """
        Builder method.
        """
    def setPointGeo(self, state: _PointState, geo: hou.Geometry) -> None: ...
    def setScale(self, scale: float) -> None: ...
    def setRigid(self, on: bool) -> None: ...
    def setRemoveNegativeScales(self, on: bool) -> None: ...
    def highlight(self, pts: Iterable[hou.Point] | None, clear: bool = False) -> None: ...
    def disable(self, pts: Iterable[hou.Point] | None, clear: bool = False) -> None: ...
    def enable(self, pts: Iterable[hou.Point]) -> None: ...
    def hidepoints(self, pts: Iterable[hou.Point] | None, clear: bool = False) -> None: ...
    def show(self, on: bool) -> None: ...
    def draw(self, draw_handle: int, color: hou._DrawableColor | None = None) -> None: ...
    def intersect(self, ui_event: hou.ViewerEvent, overlapdist: float = 1.0) -> tuple[list[hou.Point] | tuple[()], hou.Vector3] | None: ...

class KinefxRigVisualiser:
    """
    Build the KineFX-specific visualisers and provide support methods for interacting with them.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param geo: geometry to build the visualisers for
    :type geo: hou.Geometry
    :param viewer_state: viewer state to build the visualisers for
    :type viewer_state: hou.ViewerStateTemplate
    :param output_idx: in cases where the **geo** is coming from an input node with multiple outputs, 
    store the output index where the **geo** is coming from so that we can reference it later
    :type output_idx: int
    :param name: name of the visualiser
    :type name: string
    :param edge_select_parent_only: If true, we an edge is pre-highlighted or when the getPointSelection selection is used, only the parent of the edge will be selected for the joint popup or inclusion in the group.
    :type edge_select_parent_only: bool
    :param single_box_selection: If true, when box selecting (using onLocatedSelection or onSelection), a maximum of one point or edge will be selectable.
    :type single_box_selection: bool
    """
    scene_viewer: hou.SceneViewer
    output_idx: int
    name: str
    label: str
    geo: hou.Geometry
    attribwatcher: AttributeWatcher
    joint_scale_adjust: int
    override_color: hou._DrawableColor | None
    viewer_state: object
    control_drawable: hou.SimpleDrawable | None
    display_options: ViewerStateDisplayOptions
    axis: hou.Geometry
    axis_drawable: KinefxAxisDrawable | None
    joint_drawable: KinefxPointDrawable | None
    link_drawable: KinefxLinkDrawable | None
    single_box_selection: bool
    edge_select_parent_only: bool
    event_pos: hou.Vector3 | None
    packedhighlight: KinefxPackedHighlighter
    scene_gi: GeometryIntersector
    def __init__(self, scene_viewer: hou.SceneViewer, geo: hou.Geometry | None, viewer_state: object = None, output_idx: int = 0, name: str = '', label: str = '', edge_select_parent_only: bool = False, single_box_selection: bool = False, freeze_geometry: bool = False) -> None:
        """
        Constructor method.
        """
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def show_joints(self) -> bool:
        """
        Get the `show_joints` flag from the current `stateutils.ViewerStateDisplayOptions` instance.

        :return: `show_joints` flag
        :rtype: bool
        """
    @property
    def show_links(self) -> bool:
        """
        Get the `show_links` flag from the current `stateutils.ViewerStateDisplayOptions` instance.

        :return: `show_links` flag
        :rtype: bool
        """
    @property
    def show_axes(self) -> bool:
        """
        Get the `show_axes` flag from the current `stateutils.ViewerStateDisplayOptions` instance.

        :return: `show_axes` flag
        :rtype: bool
        """
    @property
    def show_scene_geo(self) -> bool:
        """
        Get the `show_scene_geo` flag from the current `stateutils.ViewerStateDisplayOptions` instance.

        :return: `show_scene_geo` flag
        :rtype: bool
        """
    def onDisplayUpdate(self) -> None:
        """
        Update the control geometry and solid bone link visualier visibility whenever `updateDisplayOptions` is called.

        These need to be handled separate from the rest because the `control_drawable` is a hou.SimpleDrawable, which means
        that it can't be explicitly drawn so we have to toggle its visibility somewhere else, and the `link_drawable` handles
        the solid visualiser's visibility in its own draw method so setting the `show_solid` flag is enough.
        """
    def sopNode(self) -> hou.SopNode | None:
        """Return the SOP Node that this object's geometry belongs to, if any.

        :return: node
        :rtype: hou.SopNode
        """
    def isGeoValid(self) -> bool:
        """
        Check if the visualiser geometry is valid or not.

        :return: valid flag
        :rtype: bool
        """
    def visible(self) -> bool:
        """
        Check if the visualiser is hidden or not.

        :return: visibility flag
        :rtype: bool
        """
    def setOffsetTransform(self, xform: hou.Matrix4) -> None:
        """
        Offset the transformation of the control geometry visualiser.

        :param xform: transformation matrix to offset the `control_drawable` by
        :type xform: hou.Matrix4
        """
    def getPointsFromEdges(self, edges: Iterable[hou.Edge], parents_only: bool | None = None) -> list[hou.Point]:
        """
        Returns the list of points which correspond to the list of edges for
        this rig's geometry.

        :param edges: A list of edges on the geometry
        :type edges: Tuple of hou.Edge
        :param parents_only: Whether to select only the parent points of the
                             edges or to select all points on the edge.
                             If None, self.edge_select_parent_only is used.
        :type parents_only: bool or None
        :return: A list of the points that correspond to the list of edges.
        :rtype: Tuple of hou.Point
        """
    @typing.overload
    def getPointSelection(self, sel: hou.Selection, parents_only: bool | None = ...) -> hou.Selection: ...
    @typing.overload
    def getPointSelection(self, sel: None, parents_only: bool | None = ...) -> None: ...
    def configureBoxSelection(self, single_box_selection: bool) -> None: ...
    def preHighlightPoints(self, pts: Sequence[hou.Point], offset: hou.Vector2 = ...) -> None:
        """
        Mark the **pts** visualisers for prehighlighting in `onDraw`.
        Only prehighlight if the point popups are not persistent - a.k.a the user has not clicked on overlapping points.

        :param pts: points to pre-highlight
        :type pts: tuple of hou.Point
        :param offset: offset the joint popup visualiser in screen space
        :type offset: hou.Vector2
        """
    def preHighlightEdges(self, edges: hou.Edge | Collection[hou.Edge], offset: hou.Vector2 = ...) -> None:
        """
        Mark the **edges** visualisers for prehighlighting in `onDraw`.
        Only prehighlight if the point popups are not persistent - a.k.a the user has not clicked on overlapping points.

        :param edge: edge to pre-highlight
        :type edge: hou.Edge
        :param offset: offset the joint popup visualiser in screen space
        :type offset: hou.Vector2
        """
    def clearPointPreHighlight(self) -> None: ...
    def clearEdgePreHighlight(self) -> None: ...
    def clearPreHighlight(self) -> None:
        """
        Clear all prehighlights.
        Only clear the prehighlight if the point popups are not persistent - a.k.a the user has not clicked on overlapping points.
        """
    def highlightSelection(self, selection: hou.Selection) -> None:
        """
        Mark the selected point or edge visualisers for highlighting in `onDraw`.

        :param selection: custom state selection object to use for highlighting visualisers
        :type selection: hou.Selection
        """
    def getHighlightPts(self) -> set[hou.Point]:
        """
        Get the current highlighted points.
        
        :return: highlighted points
        :rtype: set of hou.Point
        """
    def getPreHighlightPts(self) -> set[hou.Point]:
        """
        Get the current prehighlighted points.
        
        :return: pre-highlighted points
        :rtype: set of hou.Point
        """
    def getPreHighlightEdges(self) -> set[hou.Edge]:
        """
        Get the current prehighlighted edges.
        
        :return: pre-highlighted edges
        :rtype: set of hou.Edge
        """
    def getHighlightEdges(self) -> set[hou.Edge]:
        """
        Get the current highlighted edges.
        
        :return: highlighted edges
        :rtype: set of hou.Edge
        """
    def getHighlightPackedPrims(self) -> list[hou.PackedGeometry]:
        """
        Get the current highlighted packed primitives(control geometry) that
        are not also pre highlighted.

        :return: highlighted control geometry packed primitives
        :rtype: list of hou.PackedGeometry
        """
    def getPreHighlightPackedPrims(self) -> list[hou.PackedGeometry]:
        """
        Get the current prehighlighted packed primitives(control geometry).

        :return: prehighlighted control geometry packed primitives
        :rtype: list of hou.PackedGeometry
        """
    def setGeometry(self, geo: hou.Geometry | None) -> None:
        """
        Set the geometry of the visualisers.

        :param geo: geometry to set
        :type geo: hou.Geometry
        """
    def resetModCountCache(self) -> None:
        """
        Mark the link and axes visualiser geometries for update on next draw.
        """
    def updateDisplayOptions(self, display_options: ViewerStateDisplayOptions | None = None) -> None:
        """
        Update the display options(KineFX-specific python state menu entries and parameters).

        :param display_options: python state display options to update the visualisers from
        :type display_options: stateutils.ViewerStateDisplayOptions
        """
    @property
    def joint_popup(self) -> KinefxJointPopup | None:
        """
        Get the joint popup visualiser.

        :return: joint popup visualiser object
        :rtype: rigvisualisers.KinefxJointPopup
        .. note::
            If no joint popup is active, returns None.
        """
    def showPopup(self, pts: Sequence[hou.Point], persistent: bool = False, offset: hou.Vector2 = ...) -> None:
        """
        Create joint popup visualiser for **pts** and set it as persistent or not.

        :param pts: points to create popup visualisers for
        :type pts: list of hou.Point
        :param persistent: whether the popup visualisers should be persistent(does not disappear on next draw) or not
        :type persistent: bool
        :param offset: offset the popup visualiser in screen space
        :type offset: hou.Vector2
        """
    def freezePopup(self) -> None:
        """
        Set joint popup visualiser as persistent(does not disappear on next draw).
        """
    def unfreezePopup(self) -> None:
        """
        Set joint popup visualiser as non-persistent(disappear on next draw).
        """
    def isPopupFrozen(self) -> bool | None:
        """
        Get whether the joint popup visualiser is persistent(does not disappear on next draw) or not.

        :return: whether the joint popup visualiser is persistent or not
        :rtype: bool
        """
    def clearPopup(self) -> None:
        """
        Clear the current joint popup visualiser.
        """
    def show(self, on: bool) -> None:
        """
        Show or hide the visualisers.

        :param on: whether to show or hide the visualisers
        :type on: bool
        """
    def clear(self) -> None:
        """
        Disable and hide the visualiser.
        """
    def acceptsSelection(self) -> bool:
        """
        Get whether the visualisers accept being selected or not.

        :return: whether the visualisers accept being selected or not
        :rtype: bool
        """
    def setAcceptsSelection(self, on: bool, ghost: bool = True) -> None:
        """
        Set the visualisers whether to accept being selected or not and toggle the ghosting.

        :param on: whether the visualisers accept being selected or not
        :type on: bool
        :param ghost: whether the ghost the visualisers or not(if they do not accept being selected)
        :type ghost: bool
        """
    def isGhosted(self) -> bool:
        """
        Get whether the visualisers are ghosted(color them grey) or not.

        :return: whether the visualisers are ghosted or not
        :rtype: bool
        """
    def hidePoints(self, pts: Collection[hou.Point], clear: bool = False, skip_axes: bool = False) -> None:
        """
        Mark the visualisers belonging to **pts** for being hidden in `onDraw`.

        :param pts: points to hide
        :type pts: list or tuple of hou.Point
        :param clear: whether to replace the current hidden points or merge with them
        :type clear: bool
        :param skip_axes: If true, the visibility for the axes of the points will not
                          be changed.
        :type skip_axes: bool
        """
    def showPoints(self, pts: Collection[hou.Point], clear: bool = True, skip_axes: bool = False) -> None:
        """
        Mark the visualisers belonging to **pts** for being shown(if they had been hidden) in `onDraw`.

        :param pts: points to show
        :type pts: list or tuple of hou.Point
        :param clear: whether to show only **pts** from the whole geometry(True) or to remove **pts** from the current hidden points(False)
        :type clear: bool
        :param skip_axes: If true, the visibility for the axes of the points will not
                          be changed.
        :type skip_axes: bool
        """
    def draw(self, handle: int) -> None:
        """
        Draw the visualisers.
        Handle prehighlighting and highlighting of points and bone links as well as showing, hiding of 
        popup visualisers.

        :param draw_handle: handle for performing the render operation
        :type draw_handle: int
        """
    def drawableMask(self) -> list[str]:
        """
        Returns a list of the names of drawables that can be located by the
        onLocatedSelection callback.

        :return: A list of the names of the drawables owned by this
                 KinfexRigVisualiser that can be located by the
                 onLocatedSelection callback.
        :rtype: Tuple of String
        """
    def getLocatedSelection(self) -> _LocatedSelection:
        """
        Returns the result of the last located selection.

        :return: The result of the last call to onLocatedSelection.
        :rtype: Dict
        """
    def clearLocatedSelection(self) -> None:
        """
        Clears the recorded result of the last call to onLocatedSelection.
        """
    def onSelection(self, kwargs: ViewerStateSelectionKwargs) -> _LocatedSelection:
        """
        A handler for the viewer state's onSelection handler which is called
        when selections on drawables are identified.

        :param kwargs: The dictionary for the onSelection handler.
        :type kwargs: dict
        :return: A dictionary containing the following keys:
                 'visualiser': this KinefxRigVisualiser.
                 'joint_selection': a point selection of the selected joints.
                 'link_selection': an edge selection of the selected links.
        :rtype: dict
        """
    def onLocatedSelection(self, kwargs: ViewerStateSelectionKwargs, highlight_all: bool = False, do_highlight: bool = True) -> _LocatedSelection:
        """
        A handler for the viewer state's onLocatedSelection handler which is
        called when selections on drawables are identified.

        :param kwargs: The dictionary for the onLocatedSelection handler.
        :type kwargs: dict
        :param highlight_all: If enabled, all located points and links will be
                              highlighted. Otherwise, links will only be
                              highlighted when not points are located.
        :type highlight_all: bool
        :param do_highlight: Whether the located points and edges will be
                             pre-highlighted. This is set to false by the
                             onSelection function.
        :type do_highlight: bool
        :return: A dictionary containing the following keys:
                 'visualiser': this KinefxRigVisualiser.
                 'joint_selection': a point selection of the located joints.
                 'link_selection': an edge selection of the located links.
        :rtype: dict
        """
    def setPreHighlightColor(self, pick_mod: _PickModifier) -> None:
        """
        Sets the color of the pre-highlighted points and edges of the
        visualiser based upon the requested pick modifier.

        :param pick_mod: The pick modifier
        :type pick_mod: hou.pickModifier
        """
    @staticmethod
    def getPointFromControl(the_geo: hou.Geometry | None, the_prim: hou.Prim | None) -> hou.Point | None: ...
    def intersect(self, ui_event: hou.ViewerEvent) -> tuple[hou.Selection, float] | tuple[None, None]:
        """
        Intersect the current visualiser and return the intersected component as a selection.
        Handle prehighlighting of the intersected components.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        :return: intersected visualiser as a selection and distance from the mouse cursor to the intersected point
        :rtype: hou.Selection, float
        .. note::
            When intersecting bone links or persistent popups, returned distance is equal to 0.0
        """
    def buildSelectionDictionary(self, ui_event: hou.ViewerEvent) -> tuple[_MouseSelectionArgs | None, _PreSelection | None]:
        """
        Handle visualiser interactions: locating and selecting. 
        Display popup text visualiser for overlapping joints.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        :param dragger: state dragger object
        :type dragger: hou.ViewerStateDragger
        :return: selection and pre-selection dictionaries containing the following keys:
        `selection`: hou.Selection(the pre-selection, locating visualzier, or selection, selected visualiser), 
        `visualiser`: kinefxbasestate.KinefxRigVisualiser(the visualiser object that is being interacted with)
        :rtype: dict, dict
        .. note::
            If trying to select overlapping joints, returns None, None and shows the joints pop-up.
        """
    def updateDrawableScales(self, ui_event: hou.UIEvent) -> None:
        """
        Update the point and axes visualisers based on mouse wheel scrolling, in conjuction with 'CTRL' or 'SHIFT'.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        """

class KinefxJointPopup:
    """
    Build the KineFX joint popup visualiser and provide support methods for interacting with it.

    :param rigvis: KineFX rig visualiser
    :type rigvis: rigvisualisers.KinefxRigVisualiser
    :param pts: points to create popup visualisers for
    :type pts: list of hou.Point
    :param offset: offset the visualiser in screen space
    :type offset: hou.Vector2
    """
    rigvis: KinefxRigVisualiser
    pts: Sequence[hou.Point]
    highlight_pts: Container[hou.Point] | None
    pos_ref_pt: hou.Point
    scene_viewer: hou.SceneViewer
    offset: hou.Vector2
    highlight_color: tuple[float, float, float, float]
    label: hou.TextDrawable
    font_height: float
    line_height: float
    text_y_offset: float
    label_text: str
    dot: hou.GeometryDrawable
    dot_geo: hou.Geometry
    dot_colors: tuple[float, ...]
    prehighlight_indices: list[int]
    prehighlight_color_def: tuple[float, float, float, float]
    prehighlight_color: tuple[float, ...]
    ring: hou.GeometryDrawable
    highlight: bool
    is_persistent: bool
    def __init__(self, rigvis: KinefxRigVisualiser, pts: Sequence[hou.Point], offset: hou.Vector2 = ..., highlight_pts: Container[hou.Point] | None = None) -> None:
        """
        Builder method.
        """
    @property
    def screen_end(self) -> hou.Vector2:
        """
        Get the height of the line formed by all the popup visualisers currently drawn(when multiple points are overlapping
        multiple popups will be created, one on top of the other).

        :return: screen space size of all the popup visualisers currently drawn 
        :rtype: hou.Vector2
        .. note::
            x component(width) is 0
        """
    def draw(self, handle: int) -> None:
        """
        Draw the popup visualiser.

        :param draw_handle: handle for performing the render operation
        :type draw_handle: int
        """
    def onSelection(self, kwargs: ViewerStateSelectionKwargs, single_box_selection: bool) -> list[hou.Point]:
        """
        A handler for the viewer state's onSelection handler which is
        called when selections on drawables are identified.

        :param kwargs: The dictionary for the onSelection handler.
        :type kwargs: dict
        :param single_box_selection: If enabled, only the point with the lowest
                                     point number will be selected.
        :type single_box_selection: bool
        :return: A list of points selected on the rig visualiser's geometry.
        :rtype: Tuple of hou.Point
        """
    def onLocatedSelection(self, kwargs: ViewerStateSelectionKwargs, do_highlight: bool = True, single_box_selection: bool = False) -> list[hou.Point]:
        """
        A handler for the viewer state's onLocatedSelection handler which is
        called when selections on drawables are identified.

        :param kwargs: The dictionary for the onLocatedSelection handler
        :type kwargs: dict
        :param do_highlight: If enabled, all located points will be
                             pre-highlighted.
        :type do_highlight: bool
        :param single_box_selection: If enabled, only the point with the lowest
                                     point number will be located.
        :type single_box_selection: bool
        :return: A list of points located on the rig visualiser's geometry.
        :rtype: Tuple of hou.Point
        """
    def colorPreHighlightedPoints(self) -> None:
        """
        Re-colors the dots based upon which are pre-highlighted.
        """
    def setPreHighlightColor(self, pick_mod: _PickModifier) -> None:
        """
        Sets the color of the pre-highlighted points based upon the state of the
        requested pick modifier.

        :param pick_mod: The pick modifier
        :type pick_mod: hou.pickModifier
        """
    def intersect(self, ui_event: hou.UIEvent) -> hou.Selection | None:
        """
        Intersect the current popup visualiser, when persistent, and return the corresponding point as a selection.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        :return: corresponding point as a selection
        :rtype: hou.Selection
        """

class KinefxRigVisualiserCollection:
    """
    Stores multiple ``KinefxRigVisualiser`` objects in a collection and provides utility methods for dealing with them in bulk.

    :param rig_visualisers: visualisers to add to the collection
    :type rig_visualisers: list of kinefxbasestate.KinefxRigVisualiser
    """
    rig_visualisers: list[KinefxRigVisualiser]
    def __init__(self, rig_visualisers: Iterable[KinefxRigVisualiser] = ...) -> None:
        """
        Constructor method.
        """
    @typing.overload
    def __getitem__(self, key: str | int | hou.Geometry) -> KinefxRigVisualiser | None: ...
    @typing.overload
    def __getitem__(self, key: slice) -> list[KinefxRigVisualiser]: ...
    def __iter__(self) -> Iterator[KinefxRigVisualiser]: ...
    def __len__(self) -> int: ...
    def append(self, visualiser: KinefxRigVisualiser) -> None:
        """
        Append a visualiser to the collection if not already present
        in the collection.

        :param visualiser: visualiser to add
        :type visualiser: kinefxbasestate.KinefxRigVisualiser
        """
    def index(self, visualiser: KinefxRigVisualiser) -> int: ...
    def remove(self, visualiser: KinefxRigVisualiser | str | int) -> None:
        """
        Remove visualiser from the collection.

        :param visualiser: visualiser or name or index to remove
        :type visualiser: kinefxbasestate.KinefxRigVisualiser or str or int
        """
    def show(self, on: bool) -> None:
        """
        Show or hide the visualisers.
        :param on: whether to show or hide the visualisers
        :type on: bool
        """
    def draw(self, handle: int) -> None:
        """
        Draw the rig visualisers.

        :param handle: handle for performing the render operation
        :type handle: int
        """
    def drawableMask(self) -> list[str]:
        """
        Returns a list of the names of drawables that can be located by the
        onLocatedSelection callback.

        :return: A list of the names of the drawables owned by this
                 KinefxRigVisualiserCollection that can be located by the
                 onLocatedSelection callback.
        :rtype: Tuple of String
        """
    def getLocatedSelection(self, select_single_rig: bool = False) -> list[_LocatedSelection]:
        """
        Returns the result of the last located selection on the rig visualisers.

        :param select_single_rig: If enabled, the returned list of selection
                                  dictionaries will contain only the selection
                                  from the first rig visualiser in our list that
                                  has a non-empty selection.
        :type select_single_rig: bool
        :return: The result of the last call to onLocatedSelection.
        :rtype: Tuple of Dict
        """
    def clearLocatedSelection(self) -> None:
        """
        Clears the recorded result of the last call to onLocatedSelection on
        each visualiser.
        """
    def onSelection(self, kwargs: ViewerStateSelectionKwargs, select_single_rig: bool = False) -> list[_LocatedSelection]:
        """
        A handler for the viewer state's onSelection handler which is called
        when selections on drawables are identified.

        :param kwargs: The dictionary for the onSelection handler
        :type kwargs: dict
        :param select_single_rig: If enabled, the returned list of selection
                                  dictionaries will contain only the selection
                                  from the first rig visualiser in our list that
                                  has a non-empty selection.
        :type select_single_rig: bool
        :return: A list of the selections made on each visualiser, stored
                 in dictionaries.
        :rtype: Tuple of dict
        """
    def onLocatedSelection(self, kwargs: ViewerStateSelectionKwargs, select_single_rig: bool = False, highlight_all: bool = False) -> list[_LocatedSelection]:
        """
        A handler for the viewer state's onLocatedSelection handler which is
        called when selections on drawables are identified.

        :param kwargs: The dictionary for the onLocatedSelection handler.
        :type kwargs: dict
        :param select_single_rig: If enabled, the returned list of selection
                                  dictionaries will contain only the selection
                                  from the first rig visualiser in our list that
                                  has a non-empty selection.
        :type select_single_rig: bool
        :param highlight_all: If enabled, all located points and links will be
                              highlighted on each rig. Otherwise, links will
                              only be highlighted when not points are located.
                              This is determined on a per-rig basis.
        :type highligh_all: bool
        :return: A list of the selections located on each visualiser, stored
                 in dictionaries.
        :rtype: Tuple of dict
        """
    def setPreHighlightColor(self, pick_mod: _PickModifier) -> None:
        """
        Sets the color of the pre-highlighted points and edges for each
        visualiser based upon the requested pick modifier.

        :param pick_mod: The pick modifier
        :type pick_mod: hou.pickModifier
        """
    def updateDisplayOptions(self, display_options: ViewerStateDisplayOptions | None = None) -> None:
        """
        Update the display options(KineFX-specific python state menu entries and parameters).

        :param display_options: python state display options to update the visualisers from
        :type display_options: stateutils.ViewerStateDisplayOptions
        """
    def clear(self) -> None:
        """
        Disable and hide the rig visualisers.
        """
    def updateDrawableScales(self, ui_event: hou.UIEvent) -> None:
        """
        Update the point and axes visualisers based on mouse wheel scrolling, in conjuction with 'CTRL' or 'SHIFT'.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        """
    def freezePopups(self) -> None:
        """
        Make the point name popups persistent in the viewport.
        """
    def unfreezePopups(self) -> None:
        """
        Make the persistent point name popups in the viewport, non-persistent(make them disappear on next draw).
        """
    def clearPopups(self) -> None:
        """
        Clear the point name popups from the viewport.
        """
    def intersect(self, ui_event: hou.ViewerEvent) -> tuple[hou.Selection | None, KinefxRigVisualiser | None, bool] | tuple[None, None, None]:
        """
        Pre process the intersection across all visualisers so that we can display a
        popup of all the overlapping points, even from different geometries.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        :return: found intersection and visualiser that the intersection belongs to and a flag whether there is more than one
        visualiser in the current pre-selection
        :rtype: hou.Selection, kinefxbasestate.KinefxRigVisualiser, bool
        .. note::
            If trying to select overlapping joints, returns None, None and shows the joints pop-up.
        """
    def buildSelectionDictionary(self, ui_event: hou.ViewerEvent) -> tuple[_MouseSelectionArgs | None, _PreSelection | None]:
        """
        Handle visualiser interactions: locating and selecting. 
        Display pop-up text visualiser for overlapping joints from multiple geometries.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        :param dragger: state dragger object
        :type dragger: hou.ViewerStateDragger
        :return: selection and pre-selection dictionaries containing the following keys:
        `selection`: hou.Selection(the pre-selection, locating visualzier, or selection, selected visualiser), 
        `visualiser`: kinefxbasestate.KinefxRigVisualiser(the visualiser object that is being interacted with)
        :rtype: dict, dict
        .. note::
            If trying to select overlapping joints, returns None, None and shows the joints pop-up.
        """
    def highlightSelection(self, selection: hou.Selection) -> None:
        """
        Highlight selected point or edge visualisers.

        :param selection: custom state selection object to use for highlighting visualisers
        :type selection: hou.Selection
        """

class SkeletonActionPreview:
    """
    Build a dynamic **KinefxRigVisualiser** that gets updated based on mouse event.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    """
    scene_viewer: hou.SceneViewer
    geo: hou.Geometry
    def_color: tuple[float, float, float]
    preview_drawable: KinefxRigVisualiser
    drivers: dict[hou.Point, hou.Point | None]
    is_showing_event_pos_only: bool
    indices: list[int]
    def __init__(self, scene_viewer: hou.SceneViewer) -> None:
        """
        Constructor method.
        """
    def updateDrawableScales(self, ui_event: hou.UIEvent) -> None:
        """
        Update the scale of the dynamic drawble based on mouse wheel scaling, in conjuction with 'CTRL' or 'SHIFT'.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        """
    def __del__(self) -> None:
        """
        Set the drawable to `None`.
        """
    def buildParenting(self, parents: Iterable[hou.Point | None], children: Iterable[hou.Point | None]) -> None:
        """
        Build the bone links from each point in **children** to each point in **parents**.

        :param parent: points to use as the parents for the created bone links
        :type parents: list or tuple of hou.Point
        :param parent: points to use as the children for the created bone links
        :type parents: list or tuple of hou.Point
        """
    def showEventPosOnly(self, on: bool) -> None:
        """
        Show only the point dynamic drawable(hide the bone link).

        :param on:  whether to show or hide the point dynamic drawable
        :type on: bool
        """
    def clear(self) -> None:
        """
        Clear the dynamic visualiser.
        """
    def setColor(self, cd: tuple[float, ...] | None = None) -> None:
        """
        Set the color of the dynamic visualiser.

        :param cd: color to set the visualiser to
        :type cd: size 3 tuple of floats
        """
    def update(self, ui_event_pos: hou.Vector3 = ...) -> None:
        """
        Set the position of the point dynamic drawables.
        Lock the dynamic drawables for the already selected points to their world position and drive the current locator drawable 
        based on **ui_event_pos**.

        :param ui_event_pos: position of the current locator drawable(drawable underneath the mouse cursor)
        :type ui_event_pos: hou.Vector3
        """
    def draw(self, handle: int) -> None:
        """
        Draw the dynamic visualiser.

        :param handle: handle for performing the render operation
        :type handle: int
        """
    def show(self, on: bool) -> None:
        """
        Show or hide the dynamic visualiser.

        :param on: show or hide flag
        :type on: bool
        """
