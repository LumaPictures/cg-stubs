from collections.abc import Generator, Iterable, Iterator, Sequence
from typing import Generic, Protocol, TypedDict, TypeVar

import _apex
import apex
import hou
import apex.stateutils_2 as asu
# Other modules import Scene from here (the source binds it by `from apex import Scene`).
from apex import Scene as Scene
from apex.motionpath import _AnimateState as _MotionPathState
from apex.sceneevaluators import AnimationEvaluatorCollection, SceneEvaluator
from houtypes import ViewerStateDrawKwargs

_K = TypeVar("_K")
_V = TypeVar("_V")

class _AnimateState(asu._AnimateState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only the members `apex.stateutils_2._AnimateState` declares."""

class _SceneEvaluators(TypedDict):
    """What buildEvaluatorsForRigs() makes: the Animate state's `scene_callbacks`."""

    anim: AnimationEvaluatorCollection
    scene: SceneEvaluator

class _InvokeOutput(Protocol):
    """An output of the Scene Invoke SOP (the `Output` class local to SceneInvokeSop.invoke0_)."""

    path: str
    key: str
    init_portpath: bool
    portpath: str
    portpath1: str
    path_fixed: str
    # -1 until the first evaluation, then 0 or 1.
    is_geo: int
    is_dict: int
    frozen_geo: hou.Geometry
    eval_dict: int
    def eval(self, scene: apex.Scene) -> _apex._Value | None: ...

def loadPreProcessor() -> apex.Graph: ...

preprocessor: apex.Graph

class SingleLookup(Generic[_K, _V]):
    def __getitem__(self, k: _K) -> _V: ...
    def __setitem__(self, k: _K, v: _V) -> None: ...
    def keys(self) -> Generator[_K, None, None]: ...
    def values(self) -> Generator[_V, None, None]: ...
    def findKeyFromValue(self, v: _V) -> _K: ...
    def items(self) -> Generator[tuple[_K, _V], None, None]: ...

class SceneShapeOutputDrawable:
    scene_viewer: hou.SceneViewer
    data_key: str
    output_path: str
    # Always None: shape outputs have no image drawable.
    img_drawable: None
    hide_on_playback: bool
    levels_of_detail: Sequence[str]
    current_lod: int
    lod_lookup: dict[str, int]
    rig_path: str
    output_name: str
    xform: hou.Matrix4
    drawable: hou.SimpleDrawable
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        scene: apex.Scene,
        output: str,
        key: str,
        levels_of_detail: Sequence[str] | None = ...,
    ) -> None: ...
    @property
    def scene(self) -> apex.Scene | None: ...
    def rig(self) -> apex.SceneGraph: ...
    # A level of detail's index, or its name.
    def setLevelOfDetail(self, lod: int | str) -> None: ...
    def show(self, on: bool) -> None: ...
    def isVisible(self) -> bool: ...
    def setTransform(self, xform: hou.Matrix4) -> None: ...
    def update(self, force: bool = ...) -> None: ...
    def setVisibleInAllViewports(self) -> None: ...
    def setVisibleInViewport(self, vp: hou.GeometryViewport) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def saveToGeometry(self, geo: hou.Geometry) -> None: ...

class SceneOutputDrawable:
    scene_viewer: hou.SceneViewer
    data_key: str
    highlight_data_key: str | None
    disabled_data_key: str | None
    img_data_key: str | None
    img_highlight_data_key: str | None
    img_path_list: list[str]
    output_path: str
    # None when the output is not a rig's.
    rig_path: str | None
    output_name: str
    hide_on_playback: bool
    xform: hou.Matrix4
    drawable: hou.SimpleDrawable
    # The (output name, key) of each tracked output.
    outputs: list[tuple[str, str]]
    highlight_outline_drawable: hou.SimpleDrawable | None
    highlight_drawables: tuple[hou.GeometryDrawable, ...]
    disabled_drawable: hou.SimpleDrawable | None
    img_drawable: hou.GeometryDrawable | None
    img_highlight_drawables: tuple[hou.GeometryDrawable, ...]
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        scene: apex.Scene,
        output: str,
        key: str,
        highlight_key: str | None = ...,
        disabled_key: str | None = ...,
        hide_on_playback: bool = ...,
        img_key: str | None = ...,
        img_highlight_key: str | None = ...,
        is_control: bool | None = ...,
        is_xray: bool = ...,
        shaded: bool = ...,
    ) -> None: ...
    @property
    def scene(self) -> apex.Scene | None: ...
    def show(self, on: bool, transient: bool = ...) -> None: ...
    def isVisible(self) -> bool: ...
    def setTransform(self, xform: hou.Matrix4) -> None: ...
    def update(self, force: bool = ...) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def setVisibleInAllViewports(self) -> None: ...
    def setVisibleInViewport(self, vp: hou.GeometryViewport) -> None: ...
    def saveToGeometry(self, geo: hou.Geometry) -> None: ...

class SceneSkinOutputDrawable(SceneOutputDrawable):
    skin_control_key: str | None
    skin_highlight_drawables: tuple[hou.GeometryDrawable, ...]
    skin_highlight_outline_drawable: hou.SimpleDrawable | None
    skin_visible: bool
    checked_prims: bool
    def __init__(
        self,
        scene_viewer: hou.SceneViewer,
        scene: apex.Scene,
        output: str,
        key: str,
        highlight_key: str | None = ...,
        disabled_key: str | None = ...,
        hide_on_playback: bool = ...,
        skin_control_key: str | None = ...,
        img_key: str | None = ...,
        img_highlight_key: str | None = ...,
        is_control: bool | None = ...,
        is_xray: bool = ...,
    ) -> None: ...
    def skinActive(self) -> bool: ...
    def skinVisible(self) -> bool: ...
    def showSkin(self, on: bool) -> None: ...
    def update(self, force: bool = ...) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def saveToGeometry(self, geo: hou.Geometry) -> None: ...

# The rig graph's `update_sops` property (a Dict of each SOP's char_path and path), or {} when
# the rig has none.
def getUpdateSopsFromRigPath(scene: apex.Scene, rig_path: str) -> apex.Dict | dict[str, apex.Dict]: ...
def getGeometryInputCallbacksDefaults(scene: apex.Scene, rig_path: str) -> apex.Dict: ...
# None when the scene has no rig at rigpath.
def buildDrawableForControls(
    scene: apex.Scene,
    scene_viewer: hou.SceneViewer,
    rigpath: str,
    hide_on_playback: bool = ...,
    skin_control: str | None = ...,
    add_control_graph: bool = ...,
    shaded: bool = ...,
) -> SceneOutputDrawable | None: ...
def buildDrawableForControlDrag(scene: apex.Scene, scene_viewer: hou.SceneViewer) -> SceneOutputDrawable: ...

control_blacklist: tuple[str]

# sop_node is unused.
def buildEvaluatorsForRigs(
    state: _MotionPathState,
    scene: apex.Scene,
    scene_viewer: hou.SceneViewer,
    sop_node: hou.OpNode,
    use_motionpath: bool = ...,
) -> _SceneEvaluators: ...
# Each pair is an input port and the output port whose wires it takes over.
def rewirePortPairs(graph: apex.Graph, pairs: Iterable[tuple[int, int]]) -> None: ...
def removeAndRewire(graph: apex.Graph, nodeids: Sequence[int]) -> None: ...
def isConstraintEnabled(scene: apex.Scene, constraint_path: str) -> bool: ...
def getConstrainedControls(
    scene: apex.Scene, constraint_paths: Iterable[str] | None = ..., pending_only: bool = ...
) -> list[str]: ...
# Without a single constraint on the control, a generator of the active constraints' driven paths
# (from Scene.getActiveConstraints(), which does not exist).
def isControlConstrained(scene: apex.Scene, ctrl_path: str) -> bool | Generator[str, None, None]: ...
def getConstrainedParmsForRig(
    scene: apex.Scene, rig_path: str, constraint_paths: Iterable[str] | None = ..., pending_only: bool = ...
) -> list[str]: ...
def getConstrainedParmsForControl(scene: apex.Scene, ctrl_path: str) -> list[str]: ...
def constraintPathsForControl(scene: apex.Scene, ctrl_path: str) -> list[str]: ...
def removeCharacter(state: _AnimateState, scene: apex.Scene, char_path: str) -> None: ...
def removeRig(state: _AnimateState, scene: apex.Scene, rig_path: str, keep_anim_binding: bool = ...) -> None: ...

class SceneGeometryOutput:
    name: str
    casts_shadows: bool
    is_control: bool
    def __init__(self, name: str, casts_shadows: bool = ..., is_control: bool = ...) -> None: ...

def createRig(
    state: _AnimateState,
    rig_path: str,
    rig_graph: apex.Graph,
    geo_outputs: Iterable[SceneGeometryOutput],
    write_to_geometry: bool = ...,
    constrainable: bool = ...,
    mute_anim: bool = ...,
) -> apex.SceneGraph | None: ...
def loadRig(
    state: _AnimateState,
    rig_path: str,
    geo_outputs: Iterable[SceneGeometryOutput],
    constrainable: bool = ...,
    mute_anim: bool = ...,
) -> apex.SceneGraph | None: ...
def recreateRig(state: _AnimateState, rig_path: str, rig_graph: apex.Graph, mute_anim: bool = ...) -> apex.SceneGraph | None: ...

class SceneInvokeSop:
    needs_reload: bool
    needs_dict_reload: bool
    needs_channel_reload: bool
    cached_data_id: tuple[int, ...] | None
    last_dict_target: str
    rig_path: str | None
    output_dict: apex.Dict
    geo: hou.Geometry
    # The Scene Invoke SOP's parameters, from its first input's `parms` detail attribute.
    parms: hou._OptionDict | None
    needs_parms_reload: bool
    cached_parms_data_id: tuple[int, ...] | None
    parms_animationclip: str
    parms_animationtarget: str
    parms_channelprimdatapath: str
    parms_debugscenegraph: int
    parms_bindmultipleoutputs: int
    # The outputs multiparm: each instance's outputpath# and outputkey#.
    parms_outputs: tuple[dict[str, str], ...]
    parms_outputpathsingle: str
    parms_outputkeysingle: str
    parms_useframe: int
    parms_usecurrentframe: bool
    scene: apex.Scene
    parms_outputs_: list[_InvokeOutput]
    dictsrc_data_id: tuple[int, ...]
    # Stub generation gives the class the attributes of invoke0_'s local Output class.
    path: str
    key: str
    frozen_geo: hou.Geometry
    channelprims_data_id: tuple[int, ...] | None
    # node is the Python SOP inside the Scene Invoke SOP.
    def invoke(self, node: hou.SopNode, do_init: bool, do_eval: bool) -> None: ...
    def invoke0_(self, node: hou.SopNode) -> None: ...
    def invoke1_(self, node: hou.SopNode) -> None: ...
