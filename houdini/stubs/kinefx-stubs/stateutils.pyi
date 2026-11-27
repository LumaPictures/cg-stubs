import hou
import typing
from collections import namedtuple as namedtuple
from collections.abc import Callable as Callable, Collection, Iterable, Iterator, Mapping, MutableMapping, Sequence
from houtypes import ViewerStateCommandKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs, ViewerStateParmChangeKwargs, ViewerStateSelectionKwargs, ViewerStateVolatileClientKwargs
from kinefx.ui.rigvisualisers import KinefxRigVisualiser as KinefxRigVisualiser, KinefxRigVisualiserCollection as KinefxRigVisualiserCollection
from typing import Generic, Literal, NamedTuple, Protocol
from typing_extensions import ReadOnly, Required, TypedDict

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_S = TypeVar('_S')
_E = TypeVar('_E')
_V = TypeVar('_V', bound=hou._FloatSequence)
_OptionArgT = TypeVar('_OptionArgT', bound=hou._OptionArg)
_Entry = TypeVar('_Entry', bound=Mapping[str, object], default=hou._OptionDict)
_PickModifier: TypeAlias = hou.EnumValue[hou.pickModifier]
_ParmTupleValue: TypeAlias = tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | tuple[hou.Ramp, ...] | tuple[dict[str, str], ...] | tuple[hou.Geometry | None, ...]
_MultiparmEntry: TypeAlias = dict[str, _ParmTupleValue]
_TransformOrder: TypeAlias = Literal['srt', 'str', 'rst', 'rts', 'tsr', 'trs']
_RotateOrder: TypeAlias = Literal['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx']
_DrawWhich: TypeAlias = Literal['all', 'face', 'line']
_VS = TypeVar('_VS', bound=_VolatileSelectionState)
class _SelectionArgs(TypedDict, total=False):
    selection: Required[ReadOnly[hou.Selection | str]]
    ui_event: ReadOnly[hou.UIEvent]
    pick_mod: ReadOnly[_PickModifier]
    visualiser: ReadOnly[KinefxRigVisualiser | None]
    joint_selection: ReadOnly[hou.Selection]
    link_selection: ReadOnly[hou.Selection]
    fromundo: ReadOnly[bool]
    inithandles: ReadOnly[bool]

class _SelectionUndoArgs(_SelectionArgs):
    selection: hou.Selection | str
    fromundo: bool

class _DrawableSelectionArgs(_SelectionArgs):
    selection: hou.Selection
    pick_mod: _PickModifier
    visualiser: KinefxRigVisualiser
    joint_selection: hou.Selection
    link_selection: hou.Selection

class _MouseSelectionArgs(_SelectionArgs, total=False):
    selection: Required[hou.Selection]
    visualiser: Required[KinefxRigVisualiser | None]
    ui_event: hou.ViewerEvent

class _PreSelection(TypedDict):
    selection: hou.Selection
    visualiser: KinefxRigVisualiser

class _LocatedSelection(TypedDict, total=False):
    visualiser: Required[KinefxRigVisualiser]
    joint_selection: Required[hou.Selection]
    link_selection: Required[hou.Selection]
    selection: hou.Selection
    pick_mod: _PickModifier

class _GroupSelectionArgs(TypedDict, total=False):
    selection: Required[ReadOnly[Sequence[hou.Selection | str]]]
    fromundo: ReadOnly[bool]
    inithandles: ReadOnly[bool]

class _GroupSelectionUndoArgs(_GroupSelectionArgs):
    selection: list[hou.Selection | str]
    fromundo: bool

class _VolatileKeyEventKwargs(ViewerStateEventKwargs, total=False):
    group_changed: bool

class _VolatileClientEventKwargs(ViewerStateVolatileClientKwargs, total=False):
    group_changed: bool

class _KeyResolveInfo(TypedDict, total=False):
    contexts: list[str]

class _KeyResolveInfoKwargs(ViewerStateKwargs, total=False):
    resolve_info: Required[_KeyResolveInfo]

class _PickState(Protocol):
    @property
    def scene_viewer(self) -> hou.SceneViewer: ...
    @property
    def pick_mod(self) -> _PickModifier: ...
    def setPickModifier(self, device: hou.UIEventDevice, /) -> object: ...

class _VolatileSelectionState(_PickState, Protocol):
    @property
    def state_name(self) -> str: ...
    @property
    def node(self) -> hou.OpNode | None: ...
    @property
    def rig_visualisers(self) -> KinefxRigVisualiserCollection: ...

class _StateCommand(Protocol):
    @property
    def name(self) -> str: ...
    @property
    def label(self) -> str: ...

theVector3_0: hou.Vector3
theVector3_010: hou.Vector3
theVector3_001: hou.Vector3
theVector3_00m1: hou.Vector3
theVector3_1: hou.Vector3
theMatrix4_1: hou.Matrix4
theMatrix4_1_Tuples: tuple[float, ...]
theMatrix4_m1: hou.Matrix4
theVector4_02020205: hou.Vector4
theVector4_1: hou.Vector4

def _quoteStringWithSpaces(s: str) -> str:
    '''
    Format a string that contains empty spaces by adding \'"\' at the beginning and end of it.

    :param s: string to format
    :type s: str 
    :return: formatted string
    :rtype: str
    '''
@typing.overload
def buildAttribGroupString(geo: hou.Geometry, sel: hou.Selection, attrib: hou.Attrib | None, as_list: Literal[False] = ...) -> str: ...
@typing.overload
def buildAttribGroupString(geo: hou.Geometry, sel: hou.Selection, attrib: hou.Attrib, as_list: Literal[True]) -> list[str]: ...
@typing.overload
def buildAttribGroupString(geo: hou.Geometry, sel: hou.Selection, attrib: hou.Attrib | None, as_list: bool = ...) -> list[str] | str: ...
def resolveSelection(geo: hou.Geometry, sel: hou.Selection) -> hou.Selection:
    """
    Resolve any primtive selections, giving priority to creating a point selection from
    any packed geometries included in the selection. In the case where there are mixed prim
    types, only the packed geometries are included in the output selection.

    :param geo: geometry to resolve the primitive selection from
    :type geo: hou.Geometry
    :param sel: primitive selection
    :type sel: hou.Selection
    :return: point selection
    :rtype: hou.Selection
    """

class RollerBall:
    """
    Create rotation visualizers used in combination with the rotation dragger.
    The rotation dragger functionality inside this class is out of date - use the startDragRotate method from inside the hou.ViewerStateDragger class instead.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    """
    geo: hou.Geometry
    knob_geo: hou.Geometry
    knob_pt: hou.Point
    scene_viewer: hou.SceneViewer
    sphere_verb: hou.SopVerb
    circle_verb: hou.SopVerb
    circle_geo: hou.Geometry
    drawable: hou.GeometryDrawable
    knob_drawable: hou.GeometryDrawable
    drawable_xform: hou.Matrix4
    circle_N: hou.Vector3
    start_transform: hou.Matrix4
    start_vec: hou.Vector3
    start_ray_dir: hou.Vector3
    start_ray_origin: hou.Vector3
    start_screen_pivot: hou.Vector2
    start_screen_pos: hou.Vector2
    twist_axis: hou.Vector3
    bend_axis: hou.Vector3
    axis: hou.Vector3
    screen_axis: hou.Vector3
    is_behind: bool
    is_ball: bool
    start_mouse_x: float
    start_mouse_y: float
    def __init__(self, scene_viewer: hou.SceneViewer) -> None:
        """
        Constructor method
        """
    def isDragging(self) -> bool: ...
    def setBall(self) -> bool:
        """
        Set geometry for the ball drawable.

        :return: whether the ball drawable is active or not
        :rtype: bool
        """
    def setCircle(self, N: hou.Vector3) -> bool:
        """
        Set geometry for the circle drawable.

        :param N: orientation axis of the circle drawable
        :type N: hou.Vector3
        :return: whether the circle drawable is active or not
        :rtype: bool
        """
    def setTransform(self, pivot: hou.Vector3, scale: float, normal: hou.Vector3 | None = None) -> None:
        """
        Set the transform of each drawable part of the RollerBall object.

        :param pivot: translation
        :type pivot: hou.Vector3
        :param scale: uniform scale
        :type scale: float
        :param normal: orientation axis
        :type normal: hou.Vector3
        """
    def setKnobPosition(self, pos: hou.Vector3) -> None:
        """
        Set the position of the knob drawable(the sphere rotating around the circle).

        :param pos: position
        :type pos: hou.Vector3
        """
    def show(self, on: bool) -> None:
        """
        Control the visibility of each drawable part of the RollerBall object.

        :param on: position
        :type on: bool
        """
    def draw(self, handle: int) -> None:
        """
        Draw each drawable part of the RollerBall object.

        :param handle: handle for performing the render operation
        :type handle: int
        """
    @staticmethod
    def intersectPlaneThroughPoint(ui_event: hou.ViewerEvent, pos: hou.Vector3) -> hou.Vector3:
        """
        Draw each drawable part of the RollerBall object.

        :param ui_event: current ui event
        :type ui_event: hou.UIEvent
        :param pos: origin of the plane to intersect with
        :type pos: hou.Vector3
        :return: XYZ coordinates of the intersection point between the line and plane
        :rtype: hou.Vector3
        """
    def initDrag(self, start_transform: hou.Matrix4, ui_event: hou.ViewerEvent, twist_axis: hou.Vector3, bend_axis: hou.Vector3, drag_start_pos: hou.Vector3 = ...) -> None:
        """
        Initialize rotation dragger. Method out of date - use the startDragRotate method from inside the hou.ViewerStateDragger class instead.

        :param start_transform: transformation matrix of the object you want to initialize the drag for
        :type start_transform: hou.Matrix4
        :param ui_event: current ui event
        :type ui_event: hou.UIEvent
        :param drag_start_pos: mouse position from where to start dragging
        :type drag_start_pos: hou.Vector3
        """
    def processDrag(self, ui_event: hou.ViewerEvent) -> hou.Matrix4:
        """
        Rotation dragger. Method out of date - use the startDragRotate method from inside the hou.ViewerStateDragger class instead.

        :param ui_event: current ui event
        :type ui_event: hou.UIEvent
        :param axis: axis to rotate around
        :type axis: hou.Vector3
        :param ref_vector: initial orientation axis 
        :type ref_vector: hou.Vector3
        :param screen_space: constrain rotation in screen space
        :type screen_space: bool
        :return: transformation matrix storing the delta rotation drag
        :rtype: hou.Matrix4
        """
    def endDrag(self) -> None: ...

class ViewerStateDisplayOptions:
    """
    Build and handle the KineFX-specific python state menu entries and parameters.
    Entries included:
    * Display Joints
    * Display Joint Axes
    * Display Links
    * Solid Links
    * Show Geometry

    :param state: python state to add the menu entries to(currently unused)
    :type state: hou.ViewerStateTemplate
    """
    update_callbacks: list[Callable[[], object]]
    show_joints: bool
    show_links: bool
    solid_links: bool
    show_axes: bool
    show_scene_geo: bool
    has_state_parms: bool
    def __init__(self, state: object = None) -> None:
        """
        Constructor method
        """
    def addUpdateCallback(self, f: Callable[[], object]) -> None:
        """
        Add new callback to the callback list, that will be run in **update**.

        :param f: callback function
        :type f: function
        """
    def update(self, other: ViewerStateDisplayOptions | None = None) -> None:
        """
        Update the menu entry cached values from another instance of this class and run all stored callbacks.

        :param other: another instance of hou.ViewerStateDisplayOptions class
        :type other: stateutils.ViewerStateDisplayOptions
        """
    def asDict(self) -> dict[str, bool]:
        """
        Store the menu entry cached values in a dictionary.

        :return: dictionary of values
        :rtype: dict
        """
    def storeToUserData(self, node: hou.Node | None) -> None:
        """
        Store the menu entry cached values as a string on the passed in node.

        :param node: node to store the values on
        :type node: hou.Node
        """
    def loadFromUserData(self, node: hou.Node) -> None:
        """
        Update the menu entry cached values from the node user data.

        :param node: node to read the values from
        :type node: hou.Node
        """
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """
        Update the menu entry cached values from the current node and set the python state parameters from them.

        :param kwargs: kwargs dictionary accessible from onEnter in a python state; 
        keys required by method are:
        * node: the current hou.Node
        * state_parms: dictionary of all state parameters using the following syntax:
        ``'state_parameter_name': {'enable': bool, 'value': parm_type, 'visible': bool, 'label': str}``
        :type kwargs: dict
        """
    def onGenerate(self, kwargs: ViewerStateKwargs) -> None:
        """
        Update the python state parameters from the menu entry cached values.

        :param kwargs: kwargs dictionary accessible from onEnter in a python state; 
        keys required by method are:
        * state_parms: dictionary of all state parameters using the following syntax:
        ``'state_parameter_name': {'enable': bool, 'value': parm_type, 'visible': bool, 'label': str}``
        :type kwargs: dict
        """
    def onExit(self, kwargs: ViewerStateKwargs) -> None:
        """
        Method that has no functionality currently.
        """
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> None:
        """
        Set the python state menu entry values from the menu entry cached values.

        :param kwargs: kwargs dictionary accessible from onMenuPreOpen in a python state; 
        key required by method is:
        * menu_item_states: dictionary of all state menu entries using the following syntax:
        ``'menu_entry_name': {'enable': bool, 'visible': bool, 'label': str, 'value': bool}``
        :type kwargs: dict
        """
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> bool:
        """
        Update the menu entry cached values and state parameters from the python state menu entry values.

        :param kwargs: kwargs dictionary accessible from onMenuAction in a python state; 
        keys required by method are:
        * state_parms: dictionary of all state parameters using the following syntax:
        ``'state_parameter_name': {'enable': bool, 'value': parm_type, 'visible': bool, 'label': str}``
        :type kwargs: dict
        * show_joints, show_links, solid_links, show_links, show_axes, show_scene_geo:
        value of the state menu entries used to update the state parameters
        :type kwargs: dict
        """
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> None:
        """
        Method that has no functionality currently.
        """
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None:
        """
        Update menu entry cached values from the python state parameters.

        :param kwargs: kwargs dictionary accessible from onParmChangeEvent in a python state; 
        keys required by method are:
        * parm_name: name of the parameter that has been changed
        * parm_value: new value of the parameter
        * state_parms: dictionary of all state parameters using the following syntax:
        ``'state_parameter_name': {'enable': bool, 'value': parm_type, 'visible': bool, 'label': str}``
        :type kwargs: dict
        """
    @staticmethod
    def addDisplayOptionsToMenu(menu: hou.ViewerStateMenu, defaults: Sequence[bool] | None = None) -> None:
        """
        Add the KineFX-specific entries to the passed in python state menu.

        :param menu: python state menu to add the entries to
        :type menu: hou.ViewerStateMenu
        :param defaults: default values for the python state menu items
        :type defaults: tuple of bool
        """
    @staticmethod
    def addDisplayParmsToState(template: hou.ViewerStateTemplate, defaults: Sequence[bool] | None = None) -> None:
        """
        Add the KineFX-specific entries as parameters to the passed in python state.

        :param template: python state to add the parameters to
        :type template: hou.ViewerStateTemplate
        :param defaults: default values for the python state parameters
        :type defaults: tuple of bool
        """

class KinefxPackedHighlighter:
    """
    Build geometry drawables for highlighting(is selected) and pre-highlighting(is located) KineFX control geometry(packed primitives).
    Only packed primitives will be highlighted.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param geo: geometry to create the drawables for
    :type geo: hou.Geometry
    """
    scene_viewer: hou.SceneViewer
    geo: hou.Geometry
    highlight_geo: hou.Geometry
    prehighlight_geo: hou.Geometry
    highlight_drawable: hou.GeometryDrawable
    line_highlight_drawable: hou.GeometryDrawable
    prehighlight_drawable: hou.GeometryDrawable
    line_prehighlight_drawable: hou.GeometryDrawable
    outline_highlight_drawable: hou.SimpleDrawable | None
    outline_prehighlight_drawable: hou.SimpleDrawable | None
    def __init__(self, scene_viewer: hou.SceneViewer, geo: hou.Geometry, enable_highlight_outline: bool = False, enable_prehighlight_outline: bool = False, is_control: bool = False) -> None:
        """
        Constructor method
        """
    def setColor(self, cd: hou.Vector4 | Sequence[float] | None = None, pick_mod: _PickModifier | None = None) -> None: ...
    def setPrims(self, src_prims: hou.Selection | Sequence[hou.Prim], src_geo: hou.Geometry | None = None) -> None:
        """
        Set the highlight drawable geometry from the passed in packed primitives.

        :param prims: primitives to build the highlight drawable for
        :type prims: hou.PackedGeometry
        """
    def setPreHighlightPrims(self, src_prims: hou.Selection | Sequence[hou.Prim], src_geo: hou.Geometry | None = None) -> None:
        """
        Set the pre-highlight drawable geometry from the passed in packed primitives.

        :param prims: primitives to build the pre-highlight drawable for
        :type prims: hou.PackedGeometry
        """
    def setTransform(self, xform: hou.Matrix4) -> None: ...
    def show(self, on: bool) -> None: ...
    def draw(self, handle: int, which: _DrawWhich = 'all') -> None:
        """
        Draw the highlight and pre-highlight drawables.

        :param handle: handle for performing the render operation
        :type handle: int
        """

class KinefxImageHighlighter:
    """
    Build geometry drawables for highlighting (is selected) and pre-highlighting
    (is located) KineFX image control geometry (points). Only sprites will be
    highlighted.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param geo: geometry to create the drawables for
    :type geo: hou.Geometry
    :param use_highlighter: whether to use the highlight drawable. Necessary 
    since the animate state only uses the prehighlighters
    :type use_highlighter: bool
    """
    highlight_drawable: hou.GeometryDrawable | None
    prehighlight_drawable: hou.GeometryDrawable
    scene_viewer: hou.SceneViewer
    geo: hou.Geometry
    highlight_geo: hou.Geometry
    prehighlight_geo: hou.Geometry
    image_map: Mapping[str, str]
    def __init__(self, scene_viewer: hou.SceneViewer, geo: hou.Geometry, image_map: Mapping[str, str] = ..., use_highlighter: bool = False, is_control: bool = False) -> None:
        """
        Constructor method.
        """
    def setImageMap(self, image_map: Mapping[str, str]) -> None:
        """Set the image mapping used by the highlight drawables."""
    def setColor(self, cd: hou.Vector4 | Sequence[float] | None = None, pick_mod: _PickModifier | None = None) -> None:
        """Set the highlighter and prehighlighter colors."""
    def setPrims(self, src_prims: Iterable[hou.PackedGeometry], src_geo: hou.Geometry | None = None) -> None:
        """
        Set the highlight drawable geometry from the passed in packed primitives.

        :param src_prims: primitives to build the highlight drawable for.
        :type src_prims: list[hou.PackedGeometry]
        :param src_geo: geometry to copy prims from. Only exists on
        KinefxImageHighlighter for compatability with other highlighters.
        :type src_geo: hou.Geometry
        """
    def setPreHighlightPrims(self, src_prims: Iterable[hou.PackedGeometry], src_geo: hou.Geometry | None = None) -> None:
        """
        Set the pre-highlight drawable geometry from the passed in packed primitives.

        :param src_prims: primitives to build the highlight drawable for.
        :type src_prims: list[hou.PackedGeometry]
        :param src_geo: geometry to copy prims from. Only exists on
        KinefxImageHighlighter for compatability with other highlighters.
        :type src_geo: hou.Geometry
        """
    def setTransform(self, xform: hou.Matrix4) -> None:
        """Set the highlight drawable transforms."""
    def show(self, on: bool) -> None:
        """Show the highlight drawables."""
    def draw(self, handle: int, which: _DrawWhich = 'all') -> None:
        """
        Draw the highlight and pre-highlight drawables.

        :param handle: handle for performing the render operation.
        :type handle: int
        :param which: category of drawables to display. Only exists on
        KinefxImageHighlighter for compatability with other highlighters.
        :type which: str
        """
    def _buildHighlightGeo(self, src_prims: Iterable[hou.PackedGeometry], z_shift: float) -> hou.Geometry:
        """
        Builds a highlighter geometry with the specified prims visible.

        Point offsets are one-to-one with packed primitive numbers.

        :param src_prims: primitives to build the highlight drawable for.
        :type src_prims: list[hou.PackedGeometry]
        """

class KinefxSkinPackedHighlighter(KinefxPackedHighlighter):
    query_attrib: str
    use_line: bool
    def __init__(self, scene_viewer: hou.SceneViewer, geo: hou.Geometry, query_attrib: str, use_line: bool = False, is_control: bool = False) -> None: ...
    def primsByAttribValues(self, values: Iterable[str | int]) -> tuple[hou.Prim, ...] | list[hou.Prim]:
        """get a prim group based on values for the query attrib"""

class KinefxSkinHighlighter:
    """
    Build geometry drawables for highlighting(is selected) and pre-highlighting(is located) APEX/KineFX 
    unpacked skin control geometry as in areas of a skinned character that can be used to as selection
    triggers for controls

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param geo: geometry to create the drawables for
    :type geo: hou.Geometry
    """
    scene_viewer: hou.SceneViewer
    geo: hou.Geometry
    query_attrib: str
    use_line: bool
    highlight_drawable: hou.GeometryDrawable
    prehighlight_drawable: hou.GeometryDrawable
    line_geo: hou.Geometry
    line_prehighlight_drawable: hou.SimpleDrawable
    highlight_indices: list[int]
    prehighlight_indices: list[int]
    src_grp: hou.PrimGroup | None
    def __init__(self, scene_viewer: hou.SceneViewer, geo: hou.Geometry, query_attrib: str, use_line: bool = True, is_control: bool = False) -> None:
        """
        Constructor method
        """
    def setColor(self, cd: hou.Vector4 | Sequence[float] | None = None, pick_mod: _PickModifier | None = None) -> None: ...
    def primsByAttribValues(self, values: Iterable[str | int]) -> tuple[hou.Prim, ...] | list[hou.Prim]:
        """get a prim group based on values for the query attrib"""
    def setPrims(self, src_prims: Iterable[hou.Prim], src_geo: hou.Geometry | None = None) -> None:
        """
        Set the highlight drawable geometry from the passed in primitives.

        :param prims: primitives to build the highlight drawable for
        :type prims: hou.PackedGeometry
        """
    def setPreHighlightPrims(self, src_prims: Sequence[hou.Prim], src_geo: hou.Geometry | None = None) -> None:
        """
        Set the pre-highlight drawable geometry from the passed in primitives.

        :param prims: primitives to build the pre-highlight drawable for
        :type prims: hou.PackedGeometry
        """
    def draw(self, handle: int, which: _DrawWhich = 'all') -> None:
        """
        Draw the highlight and pre-highlight drawables.

        :param handle: handle for performing the render operation
        :type handle: int
        """
    def setTransform(self, xform: hou.Matrix4) -> None: ...
    def show(self, on: bool) -> None: ...

class KinefxSelection:
    """
    Store a selection and a geometry and provide helper methods for working with the two.
    Convenience method that allows for direct calling of `KinefxSelection.points()` without having to constantly specify the geometry.
    Convenience method that, together with `KinefxMultiSelection`, facilitates a proper storage of selections from multiple geometries.
    """
    def __init__(self, geo: hou.Geometry, selection: hou.Selection, creator: object = None) -> None:
        """
        Constructor method
        """
    @property
    def sopNode(self) -> hou.SopNode | None: ...
    @property
    def geo(self) -> hou.Geometry: ...
    @property
    def selection(self) -> hou.Selection: ...
    @property
    def points(self) -> tuple[hou.Point, ...]: ...
    @property
    def prims(self) -> tuple[hou.Prim, ...]: ...
    @property
    def edges(self) -> tuple[hou.Edge, ...]: ...
    def copyAndConvert(self, geotype: hou.EnumValue[hou.geometryType], select_only_whole: bool = False) -> hou.Selection | None: ...
    def selectionType(self) -> hou.EnumValue[hou.geometryType]: ...
    def combine(self, other: hou.Selection, pick_mod: _PickModifier) -> None: ...
    def freeze(self, selection: bool = True, geometry: bool = False) -> KinefxSelection: ...
    def clear(self) -> None: ...
    def buildGroupStringFromAttrib(self, attrib_name: str) -> str: ...

class KinefxMultiSelection:
    def __init__(self) -> None: ...
    @typing.overload
    def __getitem__(self, key: int) -> KinefxSelection: ...
    @typing.overload
    def __getitem__(self, key: slice) -> list[KinefxSelection]: ...
    def __iter__(self) -> Iterator[KinefxSelection]: ...
    def append(self, sel: KinefxSelection) -> None: ...
    def remove(self, sel: KinefxSelection) -> None: ...
    def clear(self) -> None: ...
    def find(self, key: hou.SopNode | hou.Selection) -> KinefxSelection | None:
        """Find an entry in the collection using either a hou.SopNode or
        a hou.Selection as the key."""
    def findSelectionWithPoint(self, pt: hou.Point) -> KinefxSelection | None: ...
    def freeze(self, selection: bool = True, geometry: bool = False) -> KinefxMultiSelection: ...
    def setActive(self, idx: int | None) -> None: ...
    def getActive(self) -> int | None: ...
    def size(self) -> int: ...

def snapPoint(geo: hou.Geometry, scene_viewer: hou.SceneViewer, ui_event: hou.UIEvent, gravity: float = 10, valid_pts: Collection[hou.Point] | None = None) -> tuple[hou.Point, float] | tuple[None, float]:
    """
    Snap the mouse cursor to an available point from **valid_pts** or **geo**, if within the specified **gravity** threshold.

    :param geo: potential geometry points to snap to; overridden by **valid_pts** if provided
    :type geo: hou.Geometry
    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param ui_event: active ui event
    :type ui_event: hou.UIEvent
    :param gravity: mouse snap distance threshold
    :type gravity: float
    :param valid_pts: tuple of potential points to snap to
    :type valid_pts: tuple of hou.Point
    :return: point snapped to and distance from the mouse cursor to that point
    :rtype: hou.Point, float
    """
def screenDistToWorld(scene_viewer: hou.SceneViewer, world_pos: hou.Vector3, pixels: float) -> float:
    """
    Convert a screen space distance, given in **pixels**, to a world space distance.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param world_pos: position to calculate the distance from
    :type world_pos: hou.Vector3
    :param pixels: distance in screen space
    :type pixels: int
    :return: distance in world space 
    :rtype: float
    """
def viewportRay(scene_viewer: hou.SceneViewer) -> tuple[hou.Vector3, hou.Vector3]:
    """
    Get the ray that starts in the center of the current view and is aligned to its lookat vector.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :return: origin and direction of the viewport ray
    :rtype: hou.Vector3, hou.Vector3
    """

class MultiparmCache:
    """
    Store the **multiparm** instance values, specified by **parm_keys**, in a list of dictionaries, where each dictioanry 
    represent one instance of the multiparm. Provide methods to update and filter these values.
    Dictionary format:
        ``'parameter_basename':(parameter_value, )``
    Effectively store a rolling cache of the multiparm instances to avoid having to read them from the node every time.

    :param multiparm: multiparm to cache from
    :type multiparm: hou.Parm
    :param parm_keys: base name(without `#` at the end) of the multiparm parameters that we want to cache
    :type parm_keys: tuple of str
    :param first_instance: first instance index of the multiparm
    :type first_instance: int 
    """
    multiparm: hou.Parm
    parm_keys: Sequence[str]
    first_instance: int
    data: list[_MultiparmEntry]
    def __init__(self, multiparm: hou.Parm, parm_keys: Sequence[str], first_instance: int = 0) -> None:
        """
        Constructor method
        """
    @property
    def node(self) -> hou.OpNode:
        """
        Get the node that the multiparm belongs to.

        :return: node that the multiparm belongs to
        :rtype: hou.Node
        """
    @staticmethod
    def findMultiparmInstanceBaseName(parm_t: hou.Parm | hou.ParmTuple) -> tuple[str, int] | tuple[None, None]:
        """
        Return the base name and cache index of a multiparm instance parameter.
        The index represents the multiparm instance that the parameter is a part of.

        :param parm_t: multiparm instance parameter
        :type parm_t: hou.Parm or hou.ParmTuple
        :return: base name(parameter name without `#` at the end) and cache index
        :rtype: str, int
        """
    def addMultiparmEntry(self) -> _MultiparmEntry:
        """
        Add a new entry in the multiparm and in the multiparm cache.

        :return: dictionary storing the addded multiparm instance parameter values
        :rtype: dict
        """
    def deleteMultiparmEntries(self, indices: Iterable[int]) -> None:
        """
        Deletes the entries in the multiparm and multiparm cache at indices.

        :param indices: list of indices to remove from the multiparm
        :type indices: list of int
        """
    def getData(self, index: int) -> _MultiparmEntry:
        """
        Store the data from the node multiparm **index** instance in a dictionary and add it to the cache list. 

        :param index: multiparm instance to read the data from
        :type index: int
        :return: dictionary storing the **index** instance parameter values
        :rtype: dict
        """
    def setData(self, index: int, d: MutableMapping[str, _ParmTupleValue], update_d: bool = True) -> None:
        """
        Set the parameter values from the passed in dictionary to the node multiparm **index** instance.

        :param index: multiparm instance to set the data on
        :type index: int
        :param d: dictionary to get the data from
        :type d: dict
        :param update_d: update the passed in **d** from the previous cache if the parameter that it is trying to set is locked
        :type update_d: bool
        """
    def update(self, parm_t: hou.Parm | hou.ParmTuple | None = None) -> None:
        """
        Update the cache from the passed in parameter instance. 
        When **parm_t** is the multiparm, rebuild the whole cache. 
        When **parm_t** is a parameter instance, only update that parameter from that particular instance in the cache.

        :param parm_t: parameter instance to update in the cache
        :type parm_t: hou.Parm
        """
    def getDataFromSelected(self, geo: hou.Geometry, selection: hou.Selection, group_parmname: str = 'group', filter_key: str | None = None) -> tuple[list[int], list[_MultiparmEntry]]:
        """
        Get the cached dictionaries corresponding to the currently selected points and filter them based on the **filter_key**.
        If the value of the dictionary entry, named **filter_key**, is ``False``, the entry will not get returned.
        'group_parmname' needs to exist in the 'parm_keys'

        :param geo: geometry to resolve the selection against
        :type geo: hou.Geometry
        :param selection: selected points
        :type selection: hou.Selection
        :param group_parmname: name of the multiparm parameter instance that holds the name of the joint
        :type group_parmname: str
        :param filter_key: parameter base name stored in the cache to evaluate
        :type filter_key: str
        :return: cache index(multiparm instance) and cached dictionary for each selected point
        :rtype: list of int, list of dict
        """
    def getPointGroupFromMultiparm(self, group_parmname: str = 'group') -> str:
        """
        Get the group string holding all the joint names that have an entry in the multiparm.

        :param group_parmname: name of the multiparm parameter instance that holds the name of the joint
        :type group_parmname: str
        :return: group string holding all the points found in the multiparm
        :rtype: str
        """
    def isLocked(self, index: int, parm_key: str) -> list[bool]:
        """
        Return whether the **parm_key** node instance parameter has any of its components locked.

        :param index: multiparm instance to read the parameter from
        :type index: int
        :param parm_key: name of the parameter(without the instance index)
        :type parm_key: str
        :return: list of bool types that indicate which component of the instance parameter is locked
        :rtype: list of bool
        """

class GeoParms:
    '''
    Helper class for storing data, in form of an array of dictionaries, on a geometry.
    The format of the data that is expected is as follows:
         [
            {
                "mykey1#": val1,
                "mykey2#": val1,
                ...
            },
            {
                "mykey1#": val2,
                "mykey2#": val2,
                ...
            },
         ]
    * note the "#" at the end of each key - this mimics the data format that the attribfromparms generates when
    reading in multiparms

    This is meant as a prototype idea for replacing the usage of node multiparms and for replacing the MultiparmCache class.
    This class provides a few options for the data storage format.

    What we then do with this geometry depends on the context: if we are running a nodeless state, we can use it as such
    and invoke an Apex graph with it, for example. In case of a node state, we can use the StashParms class which is
    just a thin wrapper around this class, for storing the geometry on a stash parameter on the node itself.

    :param stash_geo: geometry to initialize the cache from; this object will not be overridden
    :type stash_geo: hou.Geometry
    :param nest_under_dict: option to store the array of dictionaries under another dictionary; this mimics the data format
        that attribfromparms outputs when reading from a multiparm
    :type nest_under_dict: bool
    :param dict_name: if nest_under_dict is True, name of the dictionary to store the array under; 
        if array_as_dict is True, name of each dictionary that gets build from the array elements(the name will be correctly
        incremented to avoid key duplicates)
    :type dict_name: str
    :param flatten_array: option to store the array of dictionaries as a flat dictionary, replacing the "#" at the end of
        each key with the proper index
    :type flatten_array: bool 
    :param array_as_dict: option to store each element in the array of dictionaries as its own dictionary
    :type array_as_dict: bool 
    '''
    nest_under_dict: bool
    dict_name: str
    flatten_array: bool
    array_as_dict: bool
    def __init__(self, init_geo: hou.Geometry | None, nest_under_dict: bool = False, dict_name: str = '', flatten_array: bool = False, array_as_dict: bool = False) -> None:
        """
        Constructor method
        """
    @property
    def geo(self) -> hou.Geometry: ...
    def getEntries(self) -> list[hou._OptionDict]: ...
    def setEntries(self, indices: Collection[int], data: Sequence[Mapping[str, hou._OptionArg]]) -> None: ...
    def getEntriesFromSelection(self, geo: hou.Geometry, selection: hou.Selection, group_parmname: str = 'group#') -> tuple[list[int], list[hou._OptionDict]]: ...
    def addNewEntries(self, data: Sequence[hou._OptionDictArg[_OptionArgT]]) -> None: ...
    def deleteEntries(self, indices: Collection[int]) -> None: ...

class StashParms:
    stash_parm: hou.Parm
    dict_name: str
    nest_under_dict: bool
    flatten_array: bool
    array_as_dict: bool
    def __init__(self, stash_parm: hou.Parm, nest_under_dict: bool = False, dict_name: str = '', flatten_array: bool = False, array_as_dict: bool = False) -> None:
        """
        Constructor method
        """
    @property
    def node(self) -> hou.OpNode: ...
    @property
    def geo(self) -> hou.Geometry: ...
    @property
    def name(self) -> str: ...
    def getEntries(self) -> list[hou._OptionDict]: ...
    def setEntries(self, indices: Collection[int], data: Sequence[Mapping[str, hou._OptionArg]]) -> None: ...
    def getEntriesFromSelection(self, geo: hou.Geometry, selection: hou.Selection, group_parmname: str = 'group#') -> tuple[list[int], list[hou._OptionDict]]: ...
    def addNewEntries(self, data: Sequence[hou._OptionDictArg[_OptionArgT]]) -> None: ...
    def deleteEntries(self, indices: Collection[int]) -> None: ...

class StashParmsCollection(Generic[_Entry]):
    """
    Helper class around GeoParms or StashParms for working with multiple instances of these classes.
    Useful for setting and getting data from multiple sources.

    :param stash_parms: GeoParms or StashParms objects to read/write data to
    :type stash_parms: tuple of GeoParms or tuple of StashParms
    :param configuration: specify which keys from the dictionary array element we want to write to which stash_parms;
        this allows for using a dense data structure for writing out and ensures that each piece of that data
        lands on the correct geometry/stash
    :type configuration: tuple of tuple of str
    """
    stash_parms: list[GeoParms | StashParms]
    configuration: list[Collection[str]]
    def __init__(self, stash_parms: Iterable[GeoParms | StashParms] = ..., configuration: Iterable[Collection[str]] = ...) -> None:
        """
        Constructor method
        """
    @typing.overload
    def __getitem__(self, key: int) -> GeoParms | StashParms | None: ...
    @typing.overload
    def __getitem__(self, key: slice) -> list[GeoParms | StashParms]: ...
    def __iter__(self) -> Iterator[GeoParms | StashParms]: ...
    def __len__(self) -> int: ...
    def append(self, stash_parm: GeoParms | StashParms) -> None: ...
    def index(self, stash_parm: GeoParms | StashParms) -> int: ...
    def isValid(self) -> bool:
        """
        Check if all stash_parms have the same number of entries.
        We expect them all to have the same length but given that we are setting multiple node parms, there is a chance
        that some method, like for example a handle update, will be called for every parm update which will result in a series
        of invalid querries to getEntries.
        """
    def getEntries(self) -> list[_Entry]: ...
    def setEntries(self, indices: Collection[int], data: Iterable[_Entry | Mapping[str, hou._OptionArg]]) -> None: ...
    def getEntriesFromSelection(self, geo: hou.Geometry, selection: hou.Selection, group_parmname: str = 'group#') -> tuple[list[int], list[_Entry]]: ...
    def addNewEntries(self, data: Sequence[_Entry | Mapping[str, hou._OptionArg]]) -> None: ...
    def deleteEntries(self, indices: Collection[int]) -> None: ...

def isValidNode(node: hou.OpNode | None) -> bool:
    """
    Check if the passed in node is valid and has thrown no errors.

    :param node: node to check
    :type node: hou.Node
    :return: whether the node is valid
    :rtype: bool
    """
def showViewportGeo(scene_viewer: hou.SceneViewer, node: hou.OpNode, show: bool, call_draw: bool = True) -> None:
    """
    Show or hide the current node's output geometry.

    :param scene_viewer: active scene viewer
    :type scene_viewer: hou.SceneViewer
    :param node: node which geometry to show or hide
    :type node: hou.Node
    :param show: show or hide
    :type show: bool
    :param call_draw: call the viewport's draw() method
    :type show: bool
    """

class ScreenSpaceRect:
    """
    Handle box selection in a python state.
    Temporary method - it will probably be moved away from KineFX.
    """
    scene_viewer: hou.SceneViewer
    start: hou.Vector2 | hou.Vector3
    end: hou.Vector2 | hou.Vector3
    geo: hou.Geometry
    drawable_params: hou._DrawableParams
    screen_space: list[float]
    drawable: hou.GeometryDrawable
    outline_drawable: hou.GeometryDrawable
    def __init__(self, scene_viewer: hou.SceneViewer) -> None: ...
    def show(self, on: bool) -> None: ...
    def setStart(self, pos: hou.Vector2 | hou.Vector3) -> None: ...
    def setEnd(self, pos: hou.Vector2 | hou.Vector3) -> None: ...
    def draw(self, handle: int) -> None: ...
    def containedPoints(self, geo: hou.Geometry) -> tuple[hou.Point, ...]: ...

class SelectionUndo(Generic[_S]):
    """
    Method for custom undo-redo handling in a python state.
    Build a selection dictionary and pass it to **func**, together with a ``fromundo`` key that can be customly handled in **func**.
    **func** is considered to be a custom selection handling function that consumes a selection dictionary and processes that selection.
    (see `mySelectionHandler`` in most KineFX python states as an example)

    :param state: state instance to call **func** from
    :type state: custom state class
    :param pre_sel: previously stored selection that will be reinstated on ``undo``
    :type pre_sel: hou.Selection
    :param sel: current selection that will be reinstated on ``redo``
    :type sel: hou.Selection
    :param func: custom selection handling function
    :type func: method
    """
    state: _S
    pre_sel: hou.Selection | str | list[hou.Selection | str]
    sel: hou.Selection | str | list[hou.Selection | str]
    func: Callable[[_S, _SelectionUndoArgs], object] | Callable[[_S, _GroupSelectionUndoArgs], object] | None
    @typing.overload
    def __init__(self, state: _S, pre_sel: hou.Selection | str, sel: hou.Selection | str, func: Callable[[_S, _SelectionUndoArgs], object] | None = ...) -> None: ...
    @typing.overload
    def __init__(self, state: _S, pre_sel: list[hou.Selection | str], sel: Iterable[hou.Selection | str], func: Callable[[_S, _GroupSelectionUndoArgs], object] | None = ...) -> None: ...
    def undo(self) -> None:
        """
        Perform an undo.
        """
    def redo(self) -> None:
        """
        Perform a redo.
        """

class KeyPressTimer:
    """
    A class for determining whether a key has been tapped or held so that we
    can mimic the behaviour of volatile states when their key is pressed
    or held.
    """
    KEY_PRESS_CUTOFF_TIME: float
    start_time: int
    delta_time: int
    exit_on_key_up: bool
    def __init__(self) -> None:
        """
        Constructor method
        """
    def selectionLikeKeyPress(self, down: bool, in_mode: bool) -> bool:
        """
        Mimics the behvaiour of the key press for entering volatile states by
        returning True if the key is pressed or was released within N ms of
        being pressed.
        This should be called from the onKeyTransitEvent function.
        If this is being used to override another hotkey, onKeyEvent should
        return true when the same key is pressed.

        :param down: Whether the key is currently pressed.
        :type down: bool
        :param in_mode: Whether the state is currently in the mode that is tied
                        to the key.
        :type in_mode: bool
        :return: Returns True if the key was pressed down or was released within 
                 KEY_PRESS_CUTOFF_TIME seconds of being pressed. False otherwise.
        :rtype: bool
        """

class SnappingResult(NamedTuple):
    is_snapped: bool
    snapped_pos: hou.Vector3
    snapped_geo: hou.Geometry | None
    snapped_prims: list[int]

class KinefxVolatileSelectionHandler(Generic[_VS]):
    '''
    A class used to override a volatile selector. This class provides a number
    of methods for handling user interaction with a state and works particularly
    well when the only method of selection in the state is through this volatile
    selector.
    
    If this is used, a few functions and variables must be present on the class
    Method:
    - getPickModifier(self, hou.uiEvent.Device)
    - setPickModifier(self, hou.uiEvent.Device)
    Variables:
    - state_name - Template name of the state.
    - pick_mod - A hou.pickModifier object.
    - node - The node for the viewer state.
    - rig_visualisers - The KinefxRigVisualisers for the state. The selection
                        must be made on one of those visualisers.
    - scene_viewer - The hou.SceneViewer that the state is active in.
    
    Additionally, the state must have a drawable selector named "drawable_selector".


    :param state: The state that owns this class.
    :type state: custom state class
    :param sel_handler: The function to call on **state** to handle selections.
    :type sel_handler: method
    :param group_parm: The token of the group parameter to set.
    :type group_parm: String
    :param vis_name: The name of the visualiser on which to make the selection
    :type vis_name: String
    :param set_on_exit: If True, the group parameter will only be set when exiting
                        the volatile selection mode.
                        If False, the group parameter will be set whenever the
                        selection is changed
    :type set_on_exit: Boolean
    :param prompt:
    :type prompt: String
    '''
    state: _VS
    sel_handler: Callable[[_VS, _SelectionArgs], object]
    geo: hou.Geometry | None
    group_parm: str
    vis_name: str
    set_on_exit: bool
    prompt: str | None
    selection: hou.Selection
    hk_ctxt: str
    hk_volatile_select: str
    hk_accept_selection: str
    hk_cancel_selection: str
    default_prompt: str
    in_select_mode: bool
    set_parm_on_volatile_exit: bool
    hk_cancellable_ctxt: str
    def __init__(self, state: _VS, sel_handler: Callable[[_VS, _SelectionArgs], object], group_parm: str, vis_name: str, set_on_exit: bool = False, prompt: str | None = None) -> None:
        """
        Constructor method.
        """
    def clearUndos(self) -> None:
        """
        Used when the group parm is only set when exiting the volatile
        selection mode.
        Clears the entries in the undo state that were set while in the
        volatile selection mode.
        """
    def inSelectMode(self) -> bool:
        """
        Returns whether the volatile selector is active.
        """
    def setGeometry(self, geo: hou.Geometry | None) -> None:
        """
        Sets the geometry for the selector.
        """
    @property
    def pick_mod(self) -> _PickModifier:
        """
        The pick modifier recorded by the state.
        """
    @property
    def node(self) -> hou.OpNode | None:
        """
        The node using that invoked the current state.
        """
    @property
    def rig_visualisers(self) -> KinefxRigVisualiserCollection:
        """
        The rig visualisers for the state.
        """
    @property
    def scene_viewer(self) -> hou.SceneViewer:
        """
        The scene_viewer that the state is active in.
        """
    def exitSelector(self, set_group_parm: bool = False) -> None:
        """
        Exits the selection mode.

        :param set_group_parm: If true, the group parm will be set to match
                               the current selection.
        :type set_group_parm: Boolean
        """
    def onSelection(self, kwargs: ViewerStateSelectionKwargs, force: bool = False) -> None:
        """
        Handles the selection made by the state's drawable selector when in
        the volatile selection mode.
        This should only be called after verifying that the selector is the
        drawable selector.

        :param kwargs: The dictionary received by the state's onSelection function
        :type kwargs: Dict
        """
    def onStopSelection(self, kwargs: ViewerStateSelectionKwargs) -> None:
        """
        Handles the state's onStopSelection function after verifying that the selector
        is the drawable selector.

        :param kwargs: The dictionary received by the state's onSelection function.
        :type kwargs: Dict
        """
    @classmethod
    def registerHotkeys(cls, hotkey_definitions: hou.PluginHotkeyDefinitions, state_name: str, state_cat: hou.NodeTypeCategory) -> list[str]:
        """
        This method registers the hotkeys that we implement in the context of
        the given state type.
        """
    def onKeyGetResolveInfo(self, kwargs: _KeyResolveInfoKwargs) -> None:
        """
        Attempts to handle the state's onKeyGetResolveInfo function.

        :param kwargs: The dictionary given to the state's onKeyGetResolveInfo function.
        :type kwargs: Dict
        """
    def onVolatileClientEvent(self, kwargs: _VolatileClientEventKwargs) -> bool:
        """
        Attempts to handle the state's onVolatileClientEvent function.  This
        function uses the set_parm argument from the onKeyTransitEvent() call
        that added the volatile client, and so does not take one itself.

        :param kwargs: The dictionary given to the state's onVolatileClientEvent function.
        :type kwargs: Dict
        """
    def onKeyTransitEvent(self, kwargs: _VolatileKeyEventKwargs, set_pick_mod: bool = True, set_parm: bool = True) -> bool:
        """
        Attempts to handle the state's onKeyTransitEvent function.
        This mimics the ability of the volatile selector to either be toggled or
        be active while holding the 's' key.

        :param kwargs: The dictionary given to the state's onKeyTransitEvent function.
        :type kwargs: Dict
        :param set_pick_mod: If true, the state's pick_mod variable will be set.
        :type set_pick_mod: Boolean
        :param set_parm: If true and set_on_exit was set to True in the constructor,
                         the group parameter will be set when the selector ends.
        :type set_parm: Boolean
        :return: Whether this handled the onKeyTransitEvent
        :rtype: Boolean
        """
    def onKeyEvent(self, kwargs: _VolatileKeyEventKwargs, set_parm: bool = True) -> bool:
        """
        Attempts to handle the state's onKeyEvent function.
        This is used to exit the volatile selector using the 'Enter' or 'Esc'
        keys when setting the group parm on exit.
        Additionally, this prevents this ensures that box selection can still
        occur while Shift+S is pressed.

        :param set_parm: If true and set_on_exit was set to True in the constructor,
                         the group parameter will be set when the selector ends.
        :type set_parm: Boolean
        :return: Whether this handled the onKeyEvent
        :rtype: Boolean
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, force: bool = False) -> bool:
        """
        Handles the mouse event for the state including entering into the
        drawable selector.
        """
    def consumeSelection(self, kwargs: _SelectionArgs, undo_sel_handler: Callable[[_VS, _SelectionUndoArgs], object] | None = None) -> None:
        """
        Consumes a selection made on the rig visualiser from the onSelection
        or onMouseEvent functions.

        :param kwargs: A dictionary with the following keys:
                       'selection': The new selection
                       'ui_event' (optional): The current hou.uiEvent.
                                              This is used to get the pick mod.
                       'pick_mod' (optional): This pick modifier used to combine
                                              the current and new selections.
                       'visualiser (optional)': This rig visualiser on which the
                                                selection was made.
        :type kwargs: Dict
        """
    def setGroupParm(self) -> None:
        """
        Sets the group parameter to the current selection.
        """
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool:
        """
        Attempts to handle the onCommand function for the state. This will
        prevent the default volatile selector from starting.
        """
    def setSelectionFromParm(self) -> None:
        """
        Sets the current selection from the parameter if the selector mode is
        inactive or if set_on_exit is False.
        """
    def setDisplayGeometry(self) -> None:
        """
        Sets the current selection from the parameter, highlights that selection,
        and then hides all other rigs if in the select mode.
        """

def basicGetPickModifier(device: hou.UIEventDevice | None) -> _PickModifier:
    """
    A function which takes a hou.uiEvent.Device and returns the pick modifier
    corresponding to the set of Shift and Ctrl keys pressed.
    """
@typing.overload
def basicDrawableSelectionHandler(kwargs: ViewerStateSelectionKwargs, rig_visualisers: KinefxRigVisualiserCollection, pick_mod: _PickModifier, vis_name: str, clear_sel: bool = ...) -> _DrawableSelectionArgs: ...
@typing.overload
def basicDrawableSelectionHandler(kwargs: ViewerStateSelectionKwargs, rig_visualisers: KinefxRigVisualiser, pick_mod: _PickModifier, vis_name: None = ..., clear_sel: bool = ...) -> _DrawableSelectionArgs: ...
def basicMouseEventHandler(kwargs: ViewerStateEventKwargs, state: _PickState, rig_visualisers: KinefxRigVisualiser | KinefxRigVisualiserCollection, drawable_selector: str | None = None) -> tuple[bool, _MouseSelectionArgs | None, _PreSelection | None]:
    """
    A mouse event handler that can be used by viewer states to set the pick
    modifier for the state, get the selection and pre selection from the state's
    rig visualiser(s), and enter the drawable selector when dragging in empty
    space.
    This does not call a selection handler.

    :param state: The viewer state.
    :type state: a custom viewer state.
    :param rig_visualisers: The state's rig visualiser or rig visualiser collection.
    :type rig_visualisers: KinefxRigVisualiser or KinefxRigVisualiserCollection
    :param drawable_selector: The name of the state's drawable selector.
    :type drawable_selector: String or None
    :return: Whether the mouse event should be handled and the sel and pre_sel
             returned by the KinefxRigVisualiser.buildSelectionDictionary
             function.
    :rtype: Boolean, Dict, Dict
    """
@typing.overload
def updateSelection(selection: hou.Selection, new_sel: hou.Selection | str, geo: hou.Geometry, parm: hou.Parm, pick_mod: _PickModifier, skip_undo: bool) -> tuple[str, str]: ...
@typing.overload
def updateSelection(selection: hou.Selection, new_sel: hou.Selection | str, geo: hou.Geometry, parm: None, pick_mod: _PickModifier, skip_undo: bool) -> tuple[None, None]: ...
@typing.overload
def updateSelection(selection: hou.Selection, new_sel: hou.Selection | str, geo: hou.Geometry, parm: hou.Parm | None, pick_mod: _PickModifier, skip_undo: bool) -> tuple[str, str] | tuple[None, None]: ...
def basicSelectionHandler(kwargs: _SelectionArgs, state: _S, node: hou.OpNode | None, selection: hou.Selection, geo: hou.Geometry | None, vis_name: str | None = None, sel_handler: Callable[[_S, _SelectionUndoArgs], object] | None = None, group_parm: str | None = None, tag: str | None = None) -> None:
    """
    A basic handler for the selection made by the drawable selector or mouse
    event on a rig visualiser.

    :param kwargs: A dictionary with the following keys:
                   'selection': The new selection
                   'ui_event' (optional): The current hou.uiEvent. This is
                                          used to get the pick mod.
                   'pick_mod' (optional): This pick modifier used to combine
                                          the current and new selections.
                   'visualiser (optional)': This rig visualiser on which the
                                            selection was made.
    :type kwargs: Dict
    :param state: The viewer state
    :type state: A custom viewer state
    :param node: The node for the viewer state.
    :type node: hou.sopNode
    :param selection: The state's current selection. This is set by the function.
    :type selection: hou.Selection
    :param geo: The geometry corresponding to the selection.
    :type geo: hou.Geometry
    :param vis_name: The name of the visualiser on which to selection was
                     expected. If this is set and the selection was not made
                     on a visualiser with this name. The function will return
                     early.
    :type vis_name: String
    :param sel_handler: The function to call on the state for the undo.
                        An undo block will be added if and only if this is set.
    :type sel_handler: function
    :param group_parm: The tag of a group parameter to set to the result of the
                       selection.
    :type group_parm: String
    :param tag: A tag for the undo block.
    :type tag: String
    """
def setGroupAndActiveSelection(kwargs: _GroupSelectionArgs, state: _S, node: hou.OpNode | None, geo: hou.Geometry | None, group_sel: hou.Selection, active_sel: hou.Selection, group_parm_name: str | None, active_parm_name: str | None, undo_function: Callable[[_S, _GroupSelectionUndoArgs], object] | None, active_geo: hou.Geometry | None = None) -> None:
    """
    A function that can be used by states which have a KinefxVolatileSelectionHandler
    but should also be able to make selections.
    This function is used after the group parameter is set by the volatile selection
    handler to adjust the other selection so that it is a subset of the selection
    defined by the group parameter. Both selections must be made on geometries with
    the same sets of points such as the same skeleton in different positions.
    When creating the undo block for this operation, the selection is stored as a string
    when the corresponding parameter is being set.

    :param kwargs: A dictionary containing the following keys:
                    :selection: A list of at least 1 hou.Selection or String objects.
                                The first is the new group selection.
                                The optional second is the new active selection.
    :type kwargs: Dict
    :param state: The viewer state that is calling this function.
    :type state: A custom viewer state
    :param node: The state's node
    :type node: hou.SopNode
    :param geo: The geometry for both selections.
    :type geo: hou.Geometry
    :param group_sel: The state's group selection
    :type group_sel: hou.Selection
    :param active_sel: The state's active selection
    :type active_sel: hou.Selection
    :param group_parm_name: A parameter on the node to set to the volatile selector's group.
    :type group_parm_name: String
    :param active_parm_name: A parameter on the node to set to the active selection.
    :type active_parm_name: String or None
    :param undo_function: A function on the viewer state that can be called to undo
                          this operation.
    :type undo_function: A custom function on the state or None
    :param active_geo: The geometry for the active selection. If this is None, geo
                       is used for the active selection instead.
    :type active_geo: hou.Geometry or None
    """
def doInteriorSnapping(scene_viewer: hou.SceneViewer, ui_event: hou.ViewerEvent, interior_snapping: int | None = None) -> SnappingResult: ...
def createBasicStateRegTest(node: hou.OpNode) -> None: ...
def iterEnumValues(enum_type: type[_E]) -> list[hou.EnumValue[_E]]: ...
def buildRadialMenuFromStateCommands(name: str, label: str, commands: Sequence[_StateCommand]) -> hou.RadialMenu:
    """Just a prototype for now. Not currently used."""
def parentSpaceHandleParmKeys() -> list[str]:
    """
    Return list of handle parm names updated by parentSpaceHandleParmVals()
    """
def parentSpaceHandleParmVals(parent_xform: hou.Matrix3 | hou.Matrix4 | dict[str, _V], transform_order: _TransformOrder = 'srt', rotate_order: _RotateOrder = 'xyz') -> dict[str, float]:
    """
    Return handle parms dictionary with `parent_xfo` keys set with the matrix
    values from parent_xform. parent_xform can be a hou.Matrix3, hou.Matrix4,
    or a values_dict to be used with hou.hmath.buildTransform().
    """
def togglePointsFromGroupPattern(geo: hou.Geometry, group_string: str, sel: hou.Selection, pick_modifier: _PickModifier = ...) -> str:
    '''
    Modify the passed in group_string from the passed in sel but try to maintain any
    geometry point groups specified in the pattern. For example: passing in a "group1 @name=foot_l" and trying to remove
    the joint called "foot_l" from that group(by passing in a sel that contains all the joints in group1)
    will result in the following pattern: "group1".
    '''
