import _apex
import apex
import apex.stateutils_2 as asu
import hou
from apex.motionpath import _AnimateState as _MotionPathState
from apex.sceneevaluators import AnimationEvaluatorCollection as AnimationEvaluatorCollection, SceneEvaluator as SceneEvaluator
from apex.utils import loadGraph as loadGraph, saveDrawableToGeometry as saveDrawableToGeometry
from collections.abc import Generator, Iterable, Iterator as Iterator, Sequence
from houtypes import ViewerStateDrawKwargs
from typing import Generic, Protocol, TypedDict

from typing import TypeVar
from typing import TypeVar
_K = TypeVar('_K')
_V = TypeVar('_V')
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
    is_geo: int
    is_dict: int
    frozen_geo: hou.Geometry
    eval_dict: int
    def eval(self, scene: apex.Scene) -> _apex._Value | None: ...

PREPROCESSOR_PATH: str
DRAG_DRAWABLE_PATH: str
SKIN_CONTROL_PROPERTY: str

def loadPreProcessor() -> apex.Graph: ...

preprocessor: apex.Graph

class SingleLookup(Generic[_K, _V]):
    def __init__(self) -> None: ...
    def __getitem__(self, k: _K) -> _V: ...
    def __setitem__(self, k: _K, v: _V) -> None: ...
    def keys(self) -> Generator[_K, None, None]: ...
    def values(self) -> Generator[_V, None, None]: ...
    def findKeyFromValue(self, v: _V) -> _K: ...
    def clear(self) -> None: ...
    def items(self) -> Generator[tuple[_K, _V], None, None]: ...

class SceneShapeOutputDrawable:
    scene_viewer: hou.SceneViewer
    data_key: str
    output_path: str
    img_drawable: None
    hide_on_playback: bool
    levels_of_detail: Sequence[str]
    current_lod: int
    lod_lookup: dict[str, int]
    rig_path: str
    output_name: str
    xform: hou.Matrix4
    drawable: hou.SimpleDrawable
    def __init__(self, scene_viewer: hou.SceneViewer, scene: apex.Scene, output: str, key: str, levels_of_detail: Sequence[str] | None = None) -> None: ...
    @property
    def scene(self) -> apex.Scene | None: ...
    def rig(self) -> apex.SceneGraph: ...
    def setLevelOfDetail(self, lod: int | str) -> None: ...
    def show(self, on: bool) -> None: ...
    def isVisible(self) -> bool: ...
    def setTransform(self, xform: hou.Matrix4) -> None:
        """
        Sets a pre-transform for the drawables
        """
    def update(self, force: bool = False) -> None:
        """
        Update the visible drawables
        """
    def setVisibleInAllViewports(self) -> None: ...
    def setVisibleInViewport(self, vp: hou.GeometryViewport) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def saveToGeometry(self, geo: hou.Geometry) -> None:
        """
        Save the visible drawables to a geometry
        """

class SceneOutputDrawable:
    scene_viewer: hou.SceneViewer
    data_key: str
    highlight_data_key: str | None
    disabled_data_key: str | None
    img_data_key: str | None
    img_highlight_data_key: str | None
    img_path_list: list[str]
    output_path: str
    rig_path: str | None
    output_name: str
    hide_on_playback: bool
    xform: hou.Matrix4
    drawable: hou.SimpleDrawable
    outputs: list[tuple[str, str]]
    highlight_outline_drawable: hou.SimpleDrawable | None
    highlight_drawables: tuple[hou.GeometryDrawable, ...]
    disabled_drawable: hou.SimpleDrawable | None
    img_drawable: hou.GeometryDrawable | None
    img_highlight_drawables: tuple[hou.GeometryDrawable, ...]
    def __init__(self, scene_viewer: hou.SceneViewer, scene: apex.Scene, output: str, key: str, highlight_key: str | None = None, disabled_key: str | None = None, hide_on_playback: bool = True, img_key: str | None = None, img_highlight_key: str | None = None, is_control: bool | None = None, is_xray: bool = False, shaded: bool = False) -> None: ...
    @property
    def scene(self) -> apex.Scene | None: ...
    def show(self, on: bool, transient: bool = False) -> None: ...
    def isVisible(self) -> bool: ...
    def setTransform(self, xform: hou.Matrix4) -> None:
        """
        Sets a pre-transform for the drawables
        """
    def update(self, force: bool = False) -> None:
        """
        Update the visible drawables
        """
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def setVisibleInAllViewports(self) -> None: ...
    def setVisibleInViewport(self, vp: hou.GeometryViewport) -> None: ...
    def saveToGeometry(self, geo: hou.Geometry) -> None:
        """
        Save the visible drawables to a geometry
        """

class SceneSkinOutputDrawable(SceneOutputDrawable):
    """specialized drawable setup for skin control surfaces. we need here some """
    skin_control_key: str | None
    skin_highlight_drawables: tuple[hou.GeometryDrawable, ...]
    skin_highlight_outline_drawable: hou.SimpleDrawable | None
    skin_visible: bool
    checked_prims: bool
    def __init__(self, scene_viewer: hou.SceneViewer, scene: apex.Scene, output: str, key: str, highlight_key: str | None = None, disabled_key: str | None = None, hide_on_playback: bool = True, skin_control_key: str | None = None, img_key: str | None = None, img_highlight_key: str | None = None, is_control: bool | None = None, is_xray: bool = False) -> None: ...
    def skinActive(self) -> bool: ...
    def skinVisible(self) -> bool: ...
    def showSkin(self, on: bool) -> None: ...
    def update(self, force: bool = False) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def saveToGeometry(self, geo: hou.Geometry) -> None: ...

def getUpdateSopsFromRigPath(scene: apex.Scene, rig_path: str) -> apex.Dict | dict[str, apex.Dict]:
    """ Returns the 'update_sops 'rig property or None on failure."""
def getGeometryInputCallbacksDefaults(scene: apex.Scene, rig_path: str) -> apex.Dict:
    """ Get Default values for geometries from SOP nodes for the
        registered callbacks but only for the given rig_path.
        This doesn't pull from the SOPs.
        It looks at the paths and returns matching paths from the scene.
        Returns the geometries in an apex.Dict()
    """
def buildDrawableForControls(scene: apex.Scene, scene_viewer: hou.SceneViewer, rigpath: str, hide_on_playback: bool = True, skin_control: str | None = None, add_control_graph: bool = True, shaded: bool = False) -> SceneOutputDrawable | None: ...
def buildDrawableForControlDrag(scene: apex.Scene, scene_viewer: hou.SceneViewer) -> SceneOutputDrawable: ...

control_blacklist: tuple[str]

def buildEvaluatorsForRigs(state: _MotionPathState, scene: apex.Scene, scene_viewer: hou.SceneViewer, sop_node: hou.OpNode, use_motionpath: bool = False) -> _SceneEvaluators: ...
def rewirePortPairs(graph: apex.Graph, pairs: Iterable[tuple[int, int]]) -> None: ...
def removeAndRewire(graph: apex.Graph, nodeids: Sequence[int]) -> None: ...
def isConstraintEnabled(scene: apex.Scene, constraint_path: str) -> bool: ...
def getConstrainedControls(scene: apex.Scene, constraint_paths: Iterable[str] | None = None, pending_only: bool = False) -> list[str]: ...
def isControlConstrained(scene: apex.Scene, ctrl_path: str) -> bool | Generator[str, None, None]: ...
def getConstrainedParmsForRig(scene: apex.Scene, rig_path: str, constraint_paths: Iterable[str] | None = None, pending_only: bool = False) -> list[str]: ...
def getConstrainedParmsForControl(scene: apex.Scene, ctrl_path: str) -> list[str]: ...
def constraintPathsForControl(scene: apex.Scene, ctrl_path: str) -> list[str]: ...
def removeCharacter(state: _AnimateState, scene: apex.Scene, char_path: str) -> None: ...
def removeRig(state: _AnimateState, scene: apex.Scene, rig_path: str, keep_anim_binding: bool = False) -> None: ...

class SceneGeometryOutput:
    name: str
    casts_shadows: bool
    is_control: bool
    def __init__(self, name: str, casts_shadows: bool = True, is_control: bool = False) -> None: ...

def createRig(state: _AnimateState, rig_path: str, rig_graph: apex.Graph, geo_outputs: Iterable[SceneGeometryOutput], write_to_geometry: bool = True, constrainable: bool = True, mute_anim: bool = False) -> apex.SceneGraph | None: ...
def loadRig(state: _AnimateState, rig_path: str, geo_outputs: Iterable[SceneGeometryOutput], constrainable: bool = True, mute_anim: bool = False) -> apex.SceneGraph | None: ...
def recreateRig(state: _AnimateState, rig_path: str, rig_graph: apex.Graph, mute_anim: bool = False) -> apex.SceneGraph | None: ...

class SceneInvokeSop:
    needs_reload: bool
    needs_dict_reload: bool
    needs_channel_reload: bool
    cached_data_id: tuple[int, ...] | None
    last_dict_target: str
    rig_path: str | None
    output_dict: apex.Dict
    geo: hou.Geometry
    parms: hou._OptionDict | None
    needs_parms_reload: bool
    cached_parms_data_id: tuple[int, ...] | None
    parms_animationclip: str
    parms_animationtarget: str
    parms_channelprimdatapath: str
    parms_debugscenegraph: int
    parms_bindmultipleoutputs: int
    parms_outputs: tuple[dict[str, str], ...]
    parms_outputpathsingle: str
    parms_outputkeysingle: str
    parms_useframe: int
    parms_usecurrentframe: bool
    scene: apex.Scene
    parms_outputs_: list[_InvokeOutput]
    dictsrc_data_id: tuple[int, ...]
    path: str
    key: str
    frozen_geo: hou.Geometry
    channelprims_data_id: tuple[int, ...] | None
    def __init__(self) -> None: ...
    def invoke(self, node: hou.SopNode, do_init: bool, do_eval: bool) -> None:
        """ Code for init_scene Python SOP inside the Scene Invoke SOP.
            @node is hou.pwd() from Python SOP, not the parent.
        """
    def invoke0_(self, node: hou.SopNode) -> None: ...
    def invoke1_(self, node: hou.SopNode) -> None: ...
