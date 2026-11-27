from collections.abc import Callable, Collection, Iterable, Iterator, Mapping, MutableMapping, Sequence
from typing import Generic, Literal, NamedTuple, Protocol, TypeAlias, TypeVar, overload

import hou
from houtypes import (
    ViewerStateCommandKwargs,
    ViewerStateEnterKwargs,
    ViewerStateEventKwargs,
    ViewerStateKwargs,
    ViewerStateMenuActionKwargs,
    ViewerStateMenuPreOpenKwargs,
    ViewerStateParmChangeKwargs,
    ViewerStateSelectionKwargs,
    ViewerStateVolatileClientKwargs,
)
from kinefx.ui.rigvisualisers import KinefxRigVisualiser, KinefxRigVisualiserCollection
from typing_extensions import ReadOnly, Required, TypedDict

_S = TypeVar("_S")
_E = TypeVar("_E")
_V = TypeVar("_V", bound=hou._FloatSequence)
_OptionArgT = TypeVar("_OptionArgT", bound=hou._OptionArg)
# A StashParmsCollection entry: the merged entries of its stash parms, keyed by their multiparm
# style names ("group#", ...).  States give theirs a TypedDict.
_Entry = TypeVar("_Entry", bound=Mapping[str, object], default=hou._OptionDict)

_PickModifier: TypeAlias = hou.EnumValue[hou.pickModifier]
# A multiparm instance's parm tuple value, as ParmTuple.eval() gives it.
_ParmTupleValue: TypeAlias = (
    tuple[int, ...]
    | tuple[float, ...]
    | tuple[str, ...]
    | tuple[hou.Ramp, ...]
    | tuple[dict[str, str], ...]
    | tuple[hou.Geometry | None, ...]
)
# A MultiparmCache entry: parm base name (without the instance number) -> its value.
_MultiparmEntry: TypeAlias = dict[str, _ParmTupleValue]
_TransformOrder: TypeAlias = Literal["srt", "str", "rst", "rts", "tsr", "trs"]
_RotateOrder: TypeAlias = Literal["xyz", "xzy", "yxz", "yzx", "zxy", "zyx"]
# Which of a highlighter's drawables draw() draws: the image and skin highlighters ignore it.
_DrawWhich: TypeAlias = Literal["all", "face", "line"]

# What a state's selection handler (the sel_handler/undo function these helpers call) is passed:
# basicDrawableSelectionHandler()'s, basicMouseEventHandler()'s or SelectionUndo's dictionary.
class _SelectionArgs(TypedDict, total=False):
    selection: Required[ReadOnly[hou.Selection | str]]
    ui_event: ReadOnly[hou.UIEvent]
    pick_mod: ReadOnly[_PickModifier]
    visualiser: ReadOnly[KinefxRigVisualiser | None]
    joint_selection: ReadOnly[hou.Selection]
    link_selection: ReadOnly[hou.Selection]
    fromundo: ReadOnly[bool]
    # Whether the joint limits state's handler re-initializes its handles (default True).
    inithandles: ReadOnly[bool]

# What SelectionUndo passes its function on undo/redo, for a single selection.
class _SelectionUndoArgs(_SelectionArgs):
    selection: hou.Selection | str
    fromundo: bool

# basicDrawableSelectionHandler()'s result: a visualiser's located selection, completed.
class _DrawableSelectionArgs(_SelectionArgs):
    selection: hou.Selection
    pick_mod: _PickModifier
    visualiser: KinefxRigVisualiser
    joint_selection: hou.Selection
    link_selection: hou.Selection

# The selection dictionary of KinefxRigVisualiser(Collection).buildSelectionDictionary(), which
# KinefxVolatileSelectionHandler.onMouseEvent() adds the event to.
class _MouseSelectionArgs(_SelectionArgs, total=False):
    selection: Required[hou.Selection]
    visualiser: Required[KinefxRigVisualiser | None]
    ui_event: hou.ViewerEvent

# The pre-selection dictionary of buildSelectionDictionary().
class _PreSelection(TypedDict):
    selection: hou.Selection
    visualiser: KinefxRigVisualiser

# KinefxRigVisualiser.getLocatedSelection()/onLocatedSelection(): basicDrawableSelectionHandler()
# adds selection and pick_mod to it.
class _LocatedSelection(TypedDict, total=False):
    visualiser: Required[KinefxRigVisualiser]
    joint_selection: Required[hou.Selection]
    link_selection: Required[hou.Selection]
    selection: hou.Selection
    pick_mod: _PickModifier

# What setGroupAndActiveSelection() takes: the new group selection, then optionally the new
# active one.
class _GroupSelectionArgs(TypedDict, total=False):
    selection: Required[ReadOnly[Sequence[hou.Selection | str]]]
    fromundo: ReadOnly[bool]
    # Whether the joint limits state's handler re-initializes its handles (default True).
    inithandles: ReadOnly[bool]

# What SelectionUndo passes its function on undo/redo, for a group and an active selection.
class _GroupSelectionUndoArgs(_GroupSelectionArgs):
    selection: list[hou.Selection | str]
    fromundo: bool

# KinefxVolatileSelectionHandler's key and volatile client events tell the calling state, in
# group_changed, whether they changed the group.
class _VolatileKeyEventKwargs(ViewerStateEventKwargs, total=False):
    group_changed: bool

class _VolatileClientEventKwargs(ViewerStateVolatileClientKwargs, total=False):
    group_changed: bool

class _KeyResolveInfo(TypedDict, total=False):
    contexts: list[str]

# The kwargs of a viewer state's onKeyGetResolveInfo.
class _KeyResolveInfoKwargs(ViewerStateKwargs, total=False):
    resolve_info: Required[_KeyResolveInfo]

# A state that basicMouseEventHandler() sets the pick modifier of.
class _PickState(Protocol):
    @property
    def scene_viewer(self) -> hou.SceneViewer: ...
    @property
    def pick_mod(self) -> _PickModifier: ...
    def setPickModifier(self, device: hou.UIEventDevice, /) -> object: ...

# The state a KinefxVolatileSelectionHandler serves.
class _VolatileSelectionState(_PickState, Protocol):
    @property
    def state_name(self) -> str: ...
    @property
    def node(self) -> hou.OpNode | None: ...
    @property
    def rig_visualisers(self) -> KinefxRigVisualiserCollection: ...

_VS = TypeVar("_VS", bound=_VolatileSelectionState)

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

def _quoteStringWithSpaces(s: str) -> str: ...
@overload
def buildAttribGroupString(
    geo: hou.Geometry, sel: hou.Selection, attrib: hou.Attrib | None, as_list: Literal[False] = ...
) -> str: ...
@overload
def buildAttribGroupString(
    geo: hou.Geometry, sel: hou.Selection, attrib: hou.Attrib, as_list: Literal[True]
) -> list[str]: ...
@overload
def buildAttribGroupString(
    geo: hou.Geometry, sel: hou.Selection, attrib: hou.Attrib | None, as_list: bool = ...
) -> list[str] | str: ...
def buildAttribGroupString(
    geo: hou.Geometry, sel: hou.Selection, attrib: hou.Attrib | None, as_list: bool = ...
) -> list[str] | str: ...
def resolveSelection(geo: hou.Geometry, sel: hou.Selection) -> hou.Selection: ...

class RollerBall:
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
    def __init__(self, scene_viewer: hou.SceneViewer) -> None: ...
    def isDragging(self) -> bool: ...
    def setBall(self) -> bool: ...
    def setCircle(self, N: hou.Vector3) -> bool: ...
    def setTransform(self, pivot: hou.Vector3, scale: float, normal: hou.Vector3 | None = ...) -> None: ...
    def setKnobPosition(self, pos: hou.Vector3) -> None: ...
    def show(self, on: bool) -> None: ...
    def draw(self, handle: int) -> None: ...
    @staticmethod
    def intersectPlaneThroughPoint(ui_event: hou.ViewerEvent, pos: hou.Vector3) -> hou.Vector3: ...
    def initDrag(
        self,
        start_transform: hou.Matrix4,
        ui_event: hou.ViewerEvent,
        twist_axis: hou.Vector3,
        bend_axis: hou.Vector3,
        drag_start_pos: hou.Vector3 = ...,
    ) -> None: ...
    def processDrag(self, ui_event: hou.ViewerEvent) -> hou.Matrix4: ...
    def endDrag(self) -> None: ...

class ViewerStateDisplayOptions:
    # addUpdateCallback() appends the callback itself, which update() calls and then calls what
    # it returns unless that is None (it means to store a weak reference to it).
    update_callbacks: list[Callable[[], object]]
    # The state is unused.
    def __init__(self, state: object = ...) -> None: ...
    def addUpdateCallback(self, f: Callable[[], object]) -> None: ...
    def update(self, other: "ViewerStateDisplayOptions | None" = ...) -> None: ...
    def asDict(self) -> dict[str, bool]: ...
    def storeToUserData(self, node: hou.Node | None) -> None: ...
    def loadFromUserData(self, node: hou.Node) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def onGenerate(self, kwargs: ViewerStateKwargs) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> None: ...
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> bool: ...
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None: ...
    @staticmethod
    def addDisplayOptionsToMenu(menu: hou.ViewerStateMenu, defaults: Sequence[bool] | None = ...) -> None: ...
    @staticmethod
    def addDisplayParmsToState(template: hou.ViewerStateTemplate, defaults: Sequence[bool] | None = ...) -> None: ...

class KinefxPackedHighlighter:
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
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        geo: hou.Geometry,
        enable_highlight_outline: bool = ...,
        enable_prehighlight_outline: bool = ...,
        is_control: bool = ...,
    ) -> None: ...
    def setColor(
        self, cd: hou.Vector4 | Sequence[float] | None = ..., pick_mod: _PickModifier | None = ...
    ) -> None: ...
    # A selection needs src_geo; prims default to the first one's geometry.
    def setPrims(self, src_prims: hou.Selection | Sequence[hou.Prim], src_geo: hou.Geometry | None = ...) -> None: ...
    def setPreHighlightPrims(
        self, src_prims: hou.Selection | Sequence[hou.Prim], src_geo: hou.Geometry | None = ...
    ) -> None: ...
    def setTransform(self, xform: hou.Matrix4) -> None: ...
    def show(self, on: bool) -> None: ...
    def draw(self, handle: int, which: _DrawWhich = ...) -> None: ...

class KinefxImageHighlighter:
    image_map: Mapping[str, str]
    highlight_drawable: hou.GeometryDrawable | None
    prehighlight_drawable: hou.GeometryDrawable
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        geo: hou.Geometry,
        image_map: Mapping[str, str] = ...,
        use_highlighter: bool = ...,
        is_control: bool = ...,
    ) -> None: ...
    def setImageMap(self, image_map: Mapping[str, str]) -> None: ...
    def setColor(
        self, cd: hou.Vector4 | Sequence[float] | None = ..., pick_mod: _PickModifier | None = ...
    ) -> None: ...
    # src_geo is unused (the other highlighters take it).
    def setPrims(self, src_prims: Iterable[hou.PackedGeometry], src_geo: hou.Geometry | None = ...) -> None: ...
    def setPreHighlightPrims(self, src_prims: Iterable[hou.PackedGeometry], src_geo: hou.Geometry | None = ...) -> None: ...
    def draw(self, handle: int, which: _DrawWhich = ...) -> None: ...
    def _buildHighlightGeo(self, src_prims: Iterable[hou.PackedGeometry], z_shift: float) -> hou.Geometry: ...

class KinefxSkinPackedHighlighter(KinefxPackedHighlighter):
    query_attrib: str
    use_line: bool
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        geo: hou.Geometry,
        query_attrib: str,
        use_line: bool = ...,
        is_control: bool = ...,
    ) -> None: ...
    def primsByAttribValues(self, values: Iterable[str | int]) -> tuple[hou.Prim, ...] | list[hou.Prim]: ...

class KinefxSkinHighlighter:
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
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        geo: hou.Geometry,
        query_attrib: str,
        use_line: bool = ...,
        is_control: bool = ...,
    ) -> None: ...
    def setColor(
        self, cd: hou.Vector4 | Sequence[float] | None = ..., pick_mod: _PickModifier | None = ...
    ) -> None: ...
    def primsByAttribValues(self, values: Iterable[str | int]) -> tuple[hou.Prim, ...] | list[hou.Prim]: ...
    def setPrims(self, src_prims: Iterable[hou.Prim], src_geo: hou.Geometry | None = ...) -> None: ...
    def setPreHighlightPrims(self, src_prims: Sequence[hou.Prim], src_geo: hou.Geometry | None = ...) -> None: ...
    def draw(self, handle: int, which: _DrawWhich = ...) -> None: ...
    def setTransform(self, xform: hou.Matrix4) -> None: ...
    def show(self, on: bool) -> None: ...

class KinefxSelection:
    # The creator is unused.
    def __init__(self, geo: hou.Geometry, selection: hou.Selection, creator: object = ...) -> None: ...
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
    def copyAndConvert(
        self, geotype: hou.EnumValue[hou.geometryType], select_only_whole: bool = ...
    ) -> hou.Selection | None: ...
    def selectionType(self) -> hou.EnumValue[hou.geometryType]: ...
    def combine(self, other: hou.Selection, pick_mod: _PickModifier) -> None: ...
    def freeze(self, selection: bool = ..., geometry: bool = ...) -> "KinefxSelection": ...
    def buildGroupStringFromAttrib(self, attrib_name: str) -> str: ...

class KinefxMultiSelection:
    @overload
    def __getitem__(self, key: int) -> KinefxSelection: ...
    @overload
    def __getitem__(self, key: slice) -> list[KinefxSelection]: ...
    def __getitem__(self, key: int | slice) -> KinefxSelection | list[KinefxSelection]: ...
    def __iter__(self) -> Iterator[KinefxSelection]: ...
    def append(self, sel: KinefxSelection) -> None: ...
    def remove(self, sel: KinefxSelection) -> None: ...
    def find(self, key: hou.SopNode | hou.Selection) -> KinefxSelection | None: ...
    def findSelectionWithPoint(self, pt: hou.Point) -> KinefxSelection | None: ...
    def freeze(self, selection: bool = ..., geometry: bool = ...) -> "KinefxMultiSelection": ...
    # Anything but a valid index is ignored.
    def setActive(self, idx: int | None) -> None: ...
    def getActive(self) -> int | None: ...
    def size(self) -> int: ...

def snapPoint(
    geo: hou.Geometry,
    scene_viewer: hou.SceneViewer,
    ui_event: hou.UIEvent,
    gravity: float = ...,
    valid_pts: Collection[hou.Point] | None = ...,
) -> tuple[hou.Point, float] | tuple[None, float]: ...
def screenDistToWorld(scene_viewer: hou.SceneViewer, world_pos: hou.Vector3, pixels: float) -> float: ...
def viewportRay(scene_viewer: hou.SceneViewer) -> tuple[hou.Vector3, hou.Vector3]: ...

class MultiparmCache:
    multiparm: hou.Parm
    parm_keys: Sequence[str]
    first_instance: int
    data: list[_MultiparmEntry]
    def __init__(self, multiparm: hou.Parm, parm_keys: Sequence[str], first_instance: int = ...) -> None: ...
    @property
    def node(self) -> hou.OpNode: ...
    @staticmethod
    def findMultiparmInstanceBaseName(parm_t: hou.Parm | hou.ParmTuple) -> tuple[str, int] | tuple[None, None]: ...
    def addMultiparmEntry(self) -> _MultiparmEntry: ...
    def deleteMultiparmEntries(self, indices: Iterable[int]) -> None: ...
    def getData(self, index: int) -> _MultiparmEntry: ...
    # update_d writes back the values set (the cached ones for locked components).
    def setData(
        self, index: int, d: MutableMapping[str, _ParmTupleValue], update_d: bool = ...
    ) -> None: ...
    def update(self, parm_t: hou.Parm | hou.ParmTuple | None = ...) -> None: ...
    def getDataFromSelected(
        self, geo: hou.Geometry, selection: hou.Selection, group_parmname: str = ..., filter_key: str | None = ...
    ) -> tuple[list[int], list[_MultiparmEntry]]: ...
    def getPointGroupFromMultiparm(self, group_parmname: str = ...) -> str: ...
    def isLocked(self, index: int, parm_key: str) -> list[bool]: ...

class GeoParms:
    nest_under_dict: bool
    dict_name: str
    flatten_array: bool
    array_as_dict: bool
    def __init__(
        self,
        init_geo: hou.Geometry | None,
        nest_under_dict: bool = ...,
        dict_name: str = ...,
        flatten_array: bool = ...,
        array_as_dict: bool = ...,
    ) -> None: ...
    @property
    def geo(self) -> hou.Geometry: ...
    def getEntries(self) -> list[hou._OptionDict]: ...
    def setEntries(self, indices: Collection[int], data: Sequence[Mapping[str, hou._OptionArg]]) -> None: ...
    def getEntriesFromSelection(
        self, geo: hou.Geometry, selection: hou.Selection, group_parmname: str = ...
    ) -> tuple[list[int], list[hou._OptionDict]]: ...
    def addNewEntries(self, data: Sequence[hou._OptionDictArg[_OptionArgT]]) -> None: ...
    def deleteEntries(self, indices: Collection[int]) -> None: ...

class StashParms:
    stash_parm: hou.Parm
    dict_name: str
    nest_under_dict: bool
    flatten_array: bool
    array_as_dict: bool
    def __init__(
        self,
        stash_parm: hou.Parm,
        nest_under_dict: bool = ...,
        dict_name: str = ...,
        flatten_array: bool = ...,
        array_as_dict: bool = ...,
    ) -> None: ...
    @property
    def node(self) -> hou.OpNode: ...
    @property
    def geo(self) -> hou.Geometry: ...
    @property
    def name(self) -> str: ...
    def getEntries(self) -> list[hou._OptionDict]: ...
    def setEntries(self, indices: Collection[int], data: Sequence[Mapping[str, hou._OptionArg]]) -> None: ...
    def getEntriesFromSelection(
        self, geo: hou.Geometry, selection: hou.Selection, group_parmname: str = ...
    ) -> tuple[list[int], list[hou._OptionDict]]: ...
    def addNewEntries(self, data: Sequence[hou._OptionDictArg[_OptionArgT]]) -> None: ...
    def deleteEntries(self, indices: Collection[int]) -> None: ...

class StashParmsCollection(Generic[_Entry]):
    stash_parms: list[GeoParms | StashParms]
    # The keys of the entries that go to each of stash_parms.
    configuration: list[Collection[str]]
    def __init__(
        self, stash_parms: Iterable[GeoParms | StashParms] = ..., configuration: Iterable[Collection[str]] = ...
    ) -> None: ...
    @overload
    def __getitem__(self, key: int) -> GeoParms | StashParms | None: ...
    @overload
    def __getitem__(self, key: slice) -> list[GeoParms | StashParms]: ...
    def __getitem__(self, key: int | slice) -> GeoParms | StashParms | list[GeoParms | StashParms] | None: ...
    def __iter__(self) -> Iterator[GeoParms | StashParms]: ...
    def append(self, stash_parm: GeoParms | StashParms) -> None: ...
    def index(self, stash_parm: GeoParms | StashParms) -> int: ...
    def isValid(self) -> bool: ...
    def getEntries(self) -> list[_Entry]: ...
    # data: entries, or mappings with some of their keys.
    def setEntries(self, indices: Collection[int], data: Iterable[_Entry | Mapping[str, hou._OptionArg]]) -> None: ...
    def getEntriesFromSelection(
        self, geo: hou.Geometry, selection: hou.Selection, group_parmname: str = ...
    ) -> tuple[list[int], list[_Entry]]: ...
    def addNewEntries(self, data: Sequence[_Entry | Mapping[str, hou._OptionArg]]) -> None: ...
    def deleteEntries(self, indices: Collection[int]) -> None: ...

def isValidNode(node: hou.OpNode | None) -> bool: ...
def showViewportGeo(scene_viewer: hou.SceneViewer, node: hou.OpNode, show: bool, call_draw: bool = ...) -> None: ...

class ScreenSpaceRect:
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
    state: _S
    pre_sel: hou.Selection | str | list[hou.Selection | str]
    sel: hou.Selection | str | list[hou.Selection | str]
    func: Callable[[_S, _SelectionUndoArgs], object] | Callable[[_S, _GroupSelectionUndoArgs], object] | None
    # A list of selections is for a group and an active selection (setGroupAndActiveSelection()).
    @overload
    def __init__(
        self,
        state: _S,
        pre_sel: hou.Selection | str,
        sel: hou.Selection | str,
        func: Callable[[_S, _SelectionUndoArgs], object] | None = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        state: _S,
        pre_sel: list[hou.Selection | str],
        sel: Iterable[hou.Selection | str],
        func: Callable[[_S, _GroupSelectionUndoArgs], object] | None = ...,
    ) -> None: ...
    def __init__(
        self,
        state: _S,
        pre_sel: hou.Selection | str | list[hou.Selection | str],
        sel: hou.Selection | str | Iterable[hou.Selection | str],
        func: Callable[[_S, _SelectionUndoArgs], object] | Callable[[_S, _GroupSelectionUndoArgs], object] | None = ...,
    ) -> None: ...

class KeyPressTimer:
    def selectionLikeKeyPress(self, down: bool, in_mode: bool) -> bool: ...

class SnappingResult(NamedTuple):
    is_snapped: bool
    snapped_pos: hou.Vector3
    snapped_geo: hou.Geometry | None
    snapped_prims: list[int]

class KinefxVolatileSelectionHandler(Generic[_VS]):
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
    def __init__(
        self,
        state: _VS,
        sel_handler: Callable[[_VS, _SelectionArgs], object],
        group_parm: str,
        vis_name: str,
        set_on_exit: bool = ...,
        prompt: str | None = ...,
    ) -> None: ...
    def inSelectMode(self) -> bool: ...
    def setGeometry(self, geo: hou.Geometry | None) -> None: ...
    @property
    def pick_mod(self) -> _PickModifier: ...
    @property
    def node(self) -> hou.OpNode | None: ...
    @property
    def rig_visualisers(self) -> KinefxRigVisualiserCollection: ...
    @property
    def scene_viewer(self) -> hou.SceneViewer: ...
    def onSelection(self, kwargs: ViewerStateSelectionKwargs, force: bool = ...) -> None: ...
    def onStopSelection(self, kwargs: ViewerStateSelectionKwargs) -> None: ...
    @classmethod
    def registerHotkeys(
        cls, hotkey_definitions: hou.PluginHotkeyDefinitions, state_name: str, state_cat: hou.NodeTypeCategory
    ) -> list[str]: ...
    def onKeyGetResolveInfo(self, kwargs: _KeyResolveInfoKwargs) -> None: ...
    def onVolatileClientEvent(self, kwargs: _VolatileClientEventKwargs) -> bool: ...
    def onKeyTransitEvent(
        self, kwargs: _VolatileKeyEventKwargs, set_pick_mod: bool = ..., set_parm: bool = ...
    ) -> bool: ...
    def onKeyEvent(self, kwargs: _VolatileKeyEventKwargs, set_parm: bool = ...) -> bool: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs, force: bool = ...) -> bool: ...
    def consumeSelection(
        self, kwargs: _SelectionArgs, undo_sel_handler: Callable[[_VS, _SelectionUndoArgs], object] | None = ...
    ) -> None: ...
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool: ...

def basicGetPickModifier(device: hou.UIEventDevice | None) -> _PickModifier: ...
# Selects on the named visualiser of a collection, or on a single visualiser.
@overload
def basicDrawableSelectionHandler(
    kwargs: ViewerStateSelectionKwargs,
    rig_visualisers: KinefxRigVisualiserCollection,
    pick_mod: _PickModifier,
    vis_name: str,
    clear_sel: bool = ...,
) -> _DrawableSelectionArgs: ...
@overload
def basicDrawableSelectionHandler(
    kwargs: ViewerStateSelectionKwargs,
    rig_visualisers: KinefxRigVisualiser,
    pick_mod: _PickModifier,
    vis_name: None = ...,
    clear_sel: bool = ...,
) -> _DrawableSelectionArgs: ...
def basicDrawableSelectionHandler(
    kwargs: ViewerStateSelectionKwargs,
    rig_visualisers: KinefxRigVisualiser | KinefxRigVisualiserCollection,
    pick_mod: _PickModifier,
    vis_name: str | None = ...,
    clear_sel: bool = ...,
) -> _DrawableSelectionArgs: ...
def basicMouseEventHandler(
    kwargs: ViewerStateEventKwargs,
    state: _PickState,
    rig_visualisers: KinefxRigVisualiser | KinefxRigVisualiserCollection,
    drawable_selector: str | None = ...,
) -> tuple[bool, _MouseSelectionArgs | None, _PreSelection | None]: ...
@overload
def updateSelection(
    selection: hou.Selection,
    new_sel: hou.Selection | str,
    geo: hou.Geometry,
    parm: hou.Parm,
    pick_mod: _PickModifier,
    skip_undo: bool,
) -> tuple[str, str]: ...
@overload
def updateSelection(
    selection: hou.Selection,
    new_sel: hou.Selection | str,
    geo: hou.Geometry,
    parm: None,
    pick_mod: _PickModifier,
    skip_undo: bool,
) -> tuple[None, None]: ...
@overload
def updateSelection(
    selection: hou.Selection,
    new_sel: hou.Selection | str,
    geo: hou.Geometry,
    parm: hou.Parm | None,
    pick_mod: _PickModifier,
    skip_undo: bool,
) -> tuple[str, str] | tuple[None, None]: ...
def updateSelection(
    selection: hou.Selection,
    new_sel: hou.Selection | str,
    geo: hou.Geometry,
    parm: hou.Parm | None,
    pick_mod: _PickModifier,
    skip_undo: bool,
) -> tuple[str, str] | tuple[None, None]: ...
# The state is only asked for its pick modifier (getPickModifier(), if it has one).
def basicSelectionHandler(
    kwargs: _SelectionArgs,
    state: _S,
    node: hou.OpNode | None,
    selection: hou.Selection,
    geo: hou.Geometry | None,
    vis_name: str | None = ...,
    sel_handler: Callable[[_S, _SelectionUndoArgs], object] | None = ...,
    group_parm: str | None = ...,
    tag: str | None = ...,
) -> None: ...
def setGroupAndActiveSelection(
    kwargs: _GroupSelectionArgs,
    state: _S,
    node: hou.OpNode | None,
    geo: hou.Geometry | None,
    group_sel: hou.Selection,
    active_sel: hou.Selection,
    group_parm_name: str | None,
    active_parm_name: str | None,
    undo_function: Callable[[_S, _GroupSelectionUndoArgs], object] | None,
    active_geo: hou.Geometry | None = ...,
) -> None: ...
# interior_snapping: 0/1 view/normal based interior snapping, 3 surface snapping.
def doInteriorSnapping(
    scene_viewer: hou.SceneViewer, ui_event: hou.ViewerEvent, interior_snapping: int | None = ...
) -> SnappingResult: ...
def createBasicStateRegTest(node: hou.OpNode) -> None: ...
def iterEnumValues(enum_type: type[_E]) -> list[hou.EnumValue[_E]]: ...
def buildRadialMenuFromStateCommands(name: str, label: str, commands: Sequence[_StateCommand]) -> hou.RadialMenu: ...
def parentSpaceHandleParmKeys() -> list[str]: ...
def parentSpaceHandleParmVals(
    parent_xform: hou.Matrix3 | hou.Matrix4 | dict[str, _V],
    transform_order: _TransformOrder = ...,
    rotate_order: _RotateOrder = ...,
) -> dict[str, float]: ...
def togglePointsFromGroupPattern(
    geo: hou.Geometry, group_string: str, sel: hou.Selection, pick_modifier: _PickModifier = ...
) -> str: ...
