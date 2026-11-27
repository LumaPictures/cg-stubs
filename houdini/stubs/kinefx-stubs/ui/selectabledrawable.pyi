import hou
from houtypes import ViewerStateSelectionKwargs
from kinefx import attribwatcher as attribwatcher, rigapi as rigapi

POINT_ALPHA: float
LINE_ALPHA: float
FACE_ALPHA: float
SELECT_ALPHA_DIF: float

class KinefxSelectableDrawable:
    """
    Build the KineFX Selectable Drawable and provide support methods for
    interacting & visualising it.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param geo: geometry to build the visualiser for
    :type geo: hou.Geometry
    :param name: the base name of the drawables
    :type name: String
    """
    scene_viewer: hou.SceneViewer
    geo: hou.Geometry
    point_drawable: hou.GeometryDrawable
    line_drawable: hou.GeometryDrawable
    face_drawable: hou.GeometryDrawable
    point_highlight_drawable: hou.GeometryDrawable
    line_highlight_drawable: hou.GeometryDrawable
    face_highlight_drawable: hou.GeometryDrawable
    def __init__(self, scene_viewer: hou.SceneViewer, geo: hou.Geometry | None, name: str) -> None:
        """
        Constructor method.
        """
    def geometry(self) -> hou.Geometry:
        """
        Returns the geometry of the selectable drawable
        """
    def name(self) -> str:
        """
        Returns the name of the selectable drawable
        """
    def visible(self) -> bool:
        """
        Returns True iff one of the point, line, or face drawables are visible
        """
    def show(self, points: bool, lines: bool, faces: bool) -> None:
        """
        Set the visualiser's visibility.

        :param points: Whether the point drawable is visible
        :type show: boolean
        :param lines: Whether the line drawable is visible
        :type show: boolean
        :param face: Whether the face drawable is visible
        :type show: boolean
        """
    def setPointDrawableParams(self, params: hou._DrawableParams, highlight_drawable: bool = False) -> None:
        """
        Set the point visualiser's parameters.

        :param params: parameters to set
        :type params: dict
        :param highlight_drawable: whether to set the highlighted drawable's parameters
        :type: boolean
        """
    def setLineDrawableParams(self, params: hou._DrawableParams, highlight_drawable: bool = False) -> None:
        """
        Set the line visualiser's parameters.

        :param params: parameters to set
        :type params: dict
        :param highlight_drawable: whether to set the highlighted drawable's parameters
        :type: boolean
        """
    def setFaceDrawableParams(self, params: hou._DrawableParams, highlight_drawable: bool = False) -> None:
        """
        Set the face visualiser's parameters.

        :param params: parameters to set
        :type params: dict
        :param highlight_drawable: whether to set the highlighted drawable's parameters
        :type: boolean
        """
    def setGeometry(self, geo: hou.Geometry | None) -> None:
        """
        Set the geometry of the visualiser.

        :param geo: geometry to set
        :type geo: hou.Geometry
        """
    def draw(self, draw_handle: int) -> None:
        """
        Draw the visualiser.

        :param draw_handle: handle for performing the render operation
        :type draw_handle: int
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
    def selected(self) -> bool:
        """
        Returns whether the drawable is selected.

        :return: Whether the drawable is selected
        :rtype: boolean
        """
    def setSelected(self, select: bool) -> None:
        """
        Sets whether the drawable is selected and sets the color of the
        highlighted drawable.

        :param select: Whether to select the drawable
        :type select: boolean
        """
    def preSelected(self) -> bool:
        """
        Returns whether the drawable is pre-selected.

        :return: Whether the drawable is pre-selected
        :rtype: boolean
        """
    def setPreSelected(self, pre_select: bool) -> None:
        """
        Sets whether the drawable is pre-selected and sets the color of the
        highlighted drawable.
        If the drawable is already selected, the pre-select color will not
        be set.

        :param select: Whether to pre-selected the drawable
        :type select: boolean
        """
    def onSelection(self) -> bool:
        """
        A handler for the viewer state's onSelection handler which is called
        when selections on drawables are identified.

        :return: Whether the drawable was selected
        :rtype: boolean
        """
    def onLocatedSelection(self, kwargs: ViewerStateSelectionKwargs) -> bool:
        """
        A handler for the viewer state's onLocatedSelection handler which is
        called when selections on drawables are identified.

        :param kwargs: The dictionary for the onLocatedSelection handler.
        :type kwargs: dict
        :return: whether the drawable was located
        :rtype: boolean
        """
    def intersect(self, ui_event: hou.ViewerEvent) -> tuple[bool, bool]:
        """
        Get whether the mouse intersects with the geometry.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        :return: whether the mouse intersects with the geometry and
                 whether the geometry is selected.
        :rtype: boolean
        """

class KinefxSelectableDrawableCollection:
    """
    Manage a Collection of KineFX Selectable Drawables.

    :param single_selection: Whether the selections should be limited to a
                             single drawable.
    :type scene_viewer: boolean
    """
    drawables: list[KinefxSelectableDrawable]
    single_selection: bool
    def __init__(self, single_selection: bool) -> None:
        """
        Constructor method.
        """
    def append(self, selectable_drawable: KinefxSelectableDrawable) -> None:
        """
        Add a KineFX Selecable Drawable to the collection

        :param selectable_drawable: The KinefxSelectableDrawable to add
        :type selectable_drawable: KinefxSelectableDrawable
        """
    def draw(self, draw_handle: int) -> None:
        """
        Draw the Selectable Drawables.

        :param draw_handle: handle for performing the render operation
        :type draw_handle: int
        """
    def drawableMask(self) -> None:
        """
        Returns a list of the names of all drawables in the KineFX Selectable
        Drawable list that can be located by the onLocatedSelection callback.

        :return: A list of the names of the drawables owned by this list of
                 KinfexSelectableDrawables that can be located by the
                 onLocatedSelection callback.
        :rtype: Tuple of Strings
        """
    def onSelection(self) -> list[KinefxSelectableDrawable]:
        """
        A handler for the viewer state's onSelection handler which is called
        when selections on drawables are identified.

        :return: A list of the selected KinefxSelectableDrawables.
        :rtype: Tuple of KinefxSelectableDrawable
        """
    def onLocatedSelection(self, kwargs: ViewerStateSelectionKwargs) -> list[KinefxSelectableDrawable]:
        """
        A handler for the viewer state's onLocatedSelection handler which is
        called when selections on drawables are identified.

        :param kwargs: The dictionary for the onLocatedSelection handler.
        :type kwargs: dict
        :return: A list of the located KinefxSelectableDrawables
        :rtype: Tuple of KinefxSelectableDrawable
        """
    def intersect(self, ui_event: hou.ViewerEvent) -> tuple[KinefxSelectableDrawable | None, bool]:
        """
        Get whether the mouse intersects with the selectable drawbles and whether
        the drawable is being selected.

        :param ui_event: active ui event
        :type ui_event: hou.UIEvent
        :return: which drawable is intersected and whether it is being selected
        :rtype: KinefxSelectableDrawable, boolean
        """
    def clearSelection(self) -> None:
        """
        Resets the selection on the drawables.
        """
