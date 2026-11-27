import _apex
import apex
import hou
import weakref
from apex import mapping_2 as mapping, ragdollutils as ragdollutils, scene_2 as apexscene, selectionhandler_2 as selectionhandler
from apex.channelutils import _AnimateState as _ChannelState
from apex.control_2 import TransformControl as TransformControl
from apex.mapping_2 import ControlEndpoint as ControlEndpoint, MappingCollection as MappingCollection, MappingEndpoint as MappingEndpoint
from apex.pickwalker import PickWalkRig as PickWalkRig
from apex.ragdolltool_2 import _RagdollActivateKwargs
from apex.ragdollutils import _ShapeSelection
from apex.sceneevaluators import SceneEvaluator as SceneEvaluator
from apex.stateutils_2 import SetChannelsUndo as SetChannelsUndo
from apex.ui import apexmirror as apexmirror
from apex.ui.ragdollwidgets import RagdollBaseParameterWidget as RagdollBaseParameterWidget, RagdollBaseSliderWidget as RagdollBaseSliderWidget
from apex.ui.selectionmanager.model import SelectionManagerModel as SelectionManagerModel
from apex.ui.selectionmanager.modelconfig import ModelConfig as ModelConfig
from apex.utils import addAnimateStateUndo as addAnimateStateUndo
from apex.xformgadget import _HandleStartUpdateKwargs, _HandleUpdateKwargs
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from enum import Enum
from houtypes import ViewerStateDrawKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStatePlaybackChangeKwargs, ViewerStateVolatileClientKwargs
from kinefx.stateutils import KinefxPackedHighlighter
from statehud.parmutils import _HUDParmValue
from typing import Generic, Literal, Protocol, Sequence

from typing import TypeVar
from typing import TypeVar
_HW_co = TypeVar('_HW_co', bound=RagdollBaseSliderWidget, default=RagdollBaseSliderWidget, covariant=True)
_SW_co = TypeVar('_SW_co', bound=RagdollBaseParameterWidget, default=RagdollBaseParameterWidget, covariant=True)
class _AnimateState(_ChannelState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only the members of the states it extends."""

DRAWABLE_EVALUATOR_KEY: str
RAGDOLL_ANIM_LAYER_NAME: str
RAGDOLL_MOTIONCLIP_SESSION_DATAIDS_PATH: str
TRANSFORMATION_ORDER: list[str]
ROTATION_ORDER: list[str]
SELSET_RAGDOLL_STATES: str
CHANNEL_PRIMS_EXTENSION: str
TOOL_PARMS_ATTRIB_NAME: str

class RagdollDrawableDisplayMode(Enum):
    CollisionShapes = 0
    Skin = 1

@dataclass
class RagdollCharacter:
    name: str
    path: str
    rig_path: str
    skel_path: str
    skel_output_path: str
    collision_shapes_path: str
    channel_prims_path: str
    motion_clip_path: str
    mapping_name: str
    visible: bool
    shape_drawable: apexscene.SceneOutputDrawable
    skin_drawable: apexscene.SceneOutputDrawable
    display_drawable: apexscene.SceneOutputDrawable | None
    debug_joints_drawable: apexscene.SceneOutputDrawable
    debug_intersect_drawable: apexscene.SceneOutputDrawable

class RagdollStateBase(Generic[_HW_co, _SW_co]):
    """
    A class that both ragdoll tool and ragdoll posing inherit from to 
    centralize methods they both need.
    RagdollPosing was inheriting from RagdollTool but that caused more
    issues than it fixed and maintenance was not trivial...
    """
    scene_viewer: hou.SceneViewer
    hud_widget: _HW_co | None
    settings_widget: _SW_co | None
    name: str
    drawable_offset: hou.Matrix4
    selection_handler: selectionhandler.DrawableSelector
    selection: _ShapeSelection
    cur_selection: tuple[()] | tuple[hou.SimpleDrawable | None, hou.Prim | None]
    prev_channels: list[hou.Geometry]
    offset_xforms: dict[str, dict[str, hou.Matrix4]]
    display_mode: int
    slider_hk: str
    hud_parm_hk: str
    toggle_display_hk: str
    _active: bool
    _scene_graph: apex.SceneGraph | None
    _display_mode: int
    _motion_clip_evaluator: RagdollMotionClipEvaluator
    _auto_reload_target_anim: bool
    _pin_channels: dict[str, list[str]]
    _pin_channels_pick_mod: hou.EnumValue[hou.pickModifier]
    _update_pinned_channels: bool
    _pending_channels: dict[str, dict[str, float]]
    _mapping: dict[str, MappingCollection]
    _record_poses: bool
    _tool_parms: hou._OptionDict
    hud_rows: list[hou._HudRow]
    _visible_char_paths: list[str]
    characters: list[RagdollCharacter]
    groundplane_drawable: apexscene.SceneOutputDrawable | None
    prehighlighters: dict[hou.Drawable, KinefxPackedHighlighter]
    highlighters: dict[hou.Drawable, KinefxPackedHighlighter]
    prev_layer_name: str
    def __init__(self, viewer_state: _AnimateState, name: str, parms_path: str) -> None:
        """
        Name: str -> name of tool (Ragdoll or Ragdoll Pose)
        path: str ->  path to graph    
        """
    @property
    def viewer_state(self) -> _AnimateState | None: ...
    @property
    def scene(self) -> apex.Scene: ...
    @property
    def anim_parms_path(self) -> str:
        """
        This stores the animation parameters for tether anchors
        but also forces...    
        """
    @property
    def channelprims_extension(self) -> str: ...
    @property
    def ragdoll_graph_name(self) -> str: ...
    @property
    def ragdoll_graph_path(self) -> str: ...
    @property
    def scene_graph(self) -> apex.SceneGraph | None: ...
    @property
    def graph(self) -> apex.Graph: ...
    @property
    def solver_parms_path(self) -> str: ...
    @property
    def default_display_mode(self) -> int: ...
    @property
    def mapping(self) -> dict[str, MappingCollection]: ...
    @mapping.setter
    def mapping(self, v: dict[str, MappingCollection]) -> None: ...
    @property
    def active(self) -> bool: ...
    def label(self) -> str: ...
    def hudTemplate(self) -> list[hou._HudRow]: ...
    def control_manager(self) -> apex.ControlManager: ...
    def control_template(self) -> hou.Geometry: ...
    def binding(self) -> apex.ChannelPrimBindings | None: ...
    def getStoredVisibleCharacters(self) -> list[str]:
        """
        Get the stored list of visible characters to restore
        when exiting the tool    
        """
    def getCharactersBoundingBox(self) -> hou.BoundingBox:
        """
        Returns total bounding box of visible ragdolls based on skeletons
        also returns pos which is the center of x and z and the max of y
        """
    def warn(self, message: str, duration: float = 1.0) -> None: ...
    def warnAboutLackOfConfigs(self) -> None:
        """
        When the user has no characters with a valid ragdoll configuration
        we should let them know    
        """
    def saveSolverParmsData(self) -> None:
        """
        Save the tool's parameters to the scene.
        """
    def loadSolverParmsData(self) -> None:
        """
        Load the tool's parameters from the scene.
        """
    def showSettingsWidget(self, on: bool = True) -> None: ...
    def showHudWidget(self, on: bool = True) -> None: ...
    def resetVisualiserOffset(self) -> None:
        """
        Reset the visualiser offset to the origin.
        """
    def showVisualiserOffsetHandle(self, v: bool) -> None:
        """
        Toggles whether the visualizer offset handle is displayed.
        """
    def showShapeIntersections(self, toggle: bool) -> None: ...
    def showShapesOutsideLimits(self, toggle: bool) -> None: ...
    def onSolverSliderWidgetValueChange(self, parms: apex.Dict, add_undo: bool = True) -> None:
        """
        Updates solver-related parameters, such as ground friction.
        """
    def onStaticSliderWidgetValueChange(self, slider_names: Sequence[str], vals: Sequence[float], add_undo: bool = True) -> None: ...
    def onSliderWidgetValueChange(self, slider_names: Iterable[str], vals: Sequence[float], key: bool = False, del_keys: bool = False, add_undo: bool = True, single: bool = False) -> None: ...
    def setChannelValue(self, cl_name: str, channel: hou.ChannelPrim, newval: float, key: bool = False, interpolation: hou.EnumValue[hou.segmentType] | None = None, frame: float | None = None) -> None:
        """
        Sets a value on a channel primitive    
        """
    def deleteChannelKeys(self, cl_name: str, channel: hou.ChannelPrim, single: bool = False) -> bool: ...
    def selectionSetsSelectControls(self, ctrl_paths: Sequence[str], cur_ctrl: str | None, pick_modifier: hou.EnumValue[hou.pickModifier]) -> None: ...
    def selectionSetsShowControls(self, ctrl_paths: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier]) -> None: ...
    def getVisibleControlPaths(self) -> list[str]: ...
    def getCurrentSelectedControlPath(self) -> str | None: ...
    def selectionSetsPinControls(self, ctrl_paths: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier]) -> None: ...
    def getAllCharacterPaths(self) -> list[str]: ...
    def getVisibleCharacterPaths(self) -> list[str]: ...
    def selectionSetsShowCharacters(self, char_paths: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier], update_cache: bool = True, highlight_shapes: bool = True) -> None: ...
    def loadToolSelectionSetData(self, model: SelectionManagerModel, config: ModelConfig) -> None:
        """ Load from config to model. """
    def saveToolSelectionSetData(self, model: SelectionManagerModel, config: ModelConfig) -> None:
        """ Save from model to config. """
    def frameSelectedControls(self) -> list[hou.Geometry]:
        """
        Must override
        Ragdoll Posing can just call _frameSelectedControls here
        Ragdoll should call _frameSelectedControls and add constraint
        handling
        """
    def _frameSelectedControls(self) -> list[hou.Geometry]: ...
    def getAllControlPaths(self) -> list[str]:
        """
        called by the main state to populate the selection sets window
        this function must return a list of paths
        Ragdoll Tool should override this to add constraints handling        
        """
    def _getAllControlPaths(self) -> list[str]: ...
    def buildShapeControlPath(self, ragdoll_char_path: str, shape_name: str) -> str:
        """
        Build the control path for a ragdoll shape, from the shape name and the
        ragdoll character path (e.g. '/electra_ragdoll.char')
        """
    @staticmethod
    def _parseShapeControlPath(control_path: str) -> tuple[str, str]:
        """
        The inverse of buildShapeControlPath(), returning the ragdoll
        character path and shape name.
        """
    def ctrlIsFromRagdollRigPath(self, control_path: str) -> bool: ...
    def getPinnedChannels(self) -> dict[str, list[str]]: ...
    def getScopedChannels(self) -> dict[str, list[str]]:
        """
        called by the main state when scoping channels
        get all ragdoll scoped channels
        Ragdoll Posing should just call _getScopedChannels
        Ragdoll should also account for constraints
        """
    def scopeChannels(self, channel_list: hou.ChannelList, scoped_channels: Mapping[str, Sequence[str]], pinned_channels: Mapping[str, Iterable[str]]) -> None:
        """
        Called by main state when scoping channels    
        Must override
        """
    def onSettingsWidgetVisibilityChange(self, on: bool) -> None:
        """ 
        Callback for when the settings widget window is shown or hidden. 
        """
    def onChannelWidgetVisibilityChange(self, on: bool) -> None:
        """ 
        Callback for when the channel widget window is shown or hidden. 
        """
    def getPendingChannels(self) -> dict[str, dict[str, float]]:
        """
        Called by main state    
        """
    def clearPendingChannels(self) -> None:
        """
        Called by main state    
        """
    def getSelectedControlPaths(self) -> list[str]:
        """
        called by the main state to populate the selection sets window
        this function must return a list of paths
        Ragdoll Tool should override this to deal with constraints
        """
    def _getSelectedControlPaths(self) -> list[str]: ...
    def saveLiveData(self) -> None:
        """
        Called by onPreSave
        Ragdoll Posing can use this as is
        Ragdoll should also save Constraint related parms    
        """
    def updateSimulation(self) -> None:
        """
        RagdollTool should override this to check for self._auto_reset_sim    
        """
    def getRigMirrorPatterns(self, rig_path: str) -> list[tuple[str, str]] | None: ...
    def getRigPathMappings(self) -> dict[str, dict[str, str]]:
        """
        Maps each character's source rig path to the temporary ragdoll rig
        path. Used by the animate state to maintain its control path ref
        registry.
        """
    def onActivate(self, kwargs: _RagdollActivateKwargs) -> bool: ...
    def onDeactivate(self) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onSelectionChanged(self, control_selection: tuple[str, ...]) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onPlaybackChangeEvent(self, kwargs: ViewerStatePlaybackChangeKwargs) -> None: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onUpdateParmsAndControlsFromWidget(self, control_parms: Sequence[str] | None = None) -> bool:
        """
        Called when a value is set in the Controls tab of the g hud    
        """
    def onAnimLayerChanged(self) -> None:
        """
        Called whenever a change is made to the animation layers stack, such
        as locking, muting, soloing, adding new layers, switching layers, etc.
        Must override
        """
    def onPreEvaluationEvent(self, time: float) -> None: ...
    def onPostEvaluationEvent(self, time: float) -> bool | None: ...
    def onPoseStartEvent(self, kwargs: ViewerStateEventKwargs | _HandleStartUpdateKwargs) -> None: ...
    def onPoseEvent(self, kwargs: ViewerStateEventKwargs | _HandleUpdateKwargs) -> bool | None: ...
    def onPoseEndEvent(self, kwargs: ViewerStateEventKwargs | _HandleUpdateKwargs) -> bool | None: ...
    def onPoseEndPreKeyEvent(self, kwargs: ViewerStateEventKwargs | _HandleUpdateKwargs) -> None: ...
    def _updateParmWidgetFromGraph(self) -> None: ...
    def onCommand(self, command: str, args: Mapping[str, object]) -> None: ...
    def onStartRecordingEvent(self, kwargs: Mapping[str, _HUDParmValue]) -> bool: ...
    def onStopRecordingEvent(self, kwargs: Mapping[str, _HUDParmValue]) -> bool: ...
    def onBakeEvent(self, kwargs: Mapping[str, _HUDParmValue]) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> Literal[False]: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> Literal[False]: ...
    def onResume(self, kwargs: ViewerStateKwargs) -> None: ...
    def onInterrupt(self, kwargs: ViewerStateKwargs) -> None: ...
    def onPreSave(self) -> None:
        """
        we absolutely need to save stuff to the scene right here because
        a user could save then close Houdini which means onDeactivate for
        the tool does not run and the settings don't persist...    
        """
    def onXformGadgetEvent(self, kwargs: _HandleUpdateKwargs) -> bool:
        """
        Called by main state     
        """
    def onXformGadgetEndEvent(self, kwargs: _HandleUpdateKwargs) -> bool:
        """
        Called by main state    
        """
    def getPickWalkData(self, rig_path: str) -> PickWalkRig | None:
        """ Get the pick walk data for the given rig path. """
    def _createPackedHighlighter(self, geo: hou.Geometry) -> KinefxPackedHighlighter: ...
    def _stashVisibleCharacters(self) -> None:
        """
        Hide non-ragdoll characters when entering the tool to avoid overlapping
        geometry.
        """
    def _restoreVisibleCharacters(self) -> None:
        """
        Restore the visibility of any characters hidden when entering the tool.
        """
    def _getSceneEvaluator(self) -> SceneEvaluator:
        """
        Returns the viewer state's primary scene evalautor, which updates
        the SceneOutputDrawables.
        """
    def getSelectedSourceControls(self) -> list[apex.Control]: ...
    def getAllSourceControls(self, rig_path: str) -> list[apex.Control]: ...
    def getAllShapes(self) -> dict[hou.SimpleDrawable, tuple[hou.Prim, ...]]: ...
    def toggleSelectedShapesActive(self) -> bool:
        """
        Toggles the selected shape's Active setting.
        Returns false if no shapes were selected.
        """
    def toggleShapesActive(self, sel: Mapping[hou.SimpleDrawable, Iterable[hou.Prim]], override: bool | None = None) -> bool: ...
    def forceRedraw(self) -> None: ...
    def clearSelection(self) -> None: ...
    def setSceneGraphParm(self, key: str, value: _apex._ValueArg) -> None: ...
    def addCharactersFromScene(self) -> None:
        """
        Add all characters from the scene which have ragdoll configurations,
        e.g. from the APEX Configure Character SOP
        """
    def _addCharacterToGraph(self, scene_graph: apex.Graph, char_name: str) -> None:
        """
        Ragdoll Pose needs to override this to make sure we build the graph
        differently...    
        """
    def _initChannelPrimsForCharacter(self, character: RagdollCharacter) -> None:
        """
        Creates the default channel prim geometry for a new character and
        adds it to the scene. This may be overridden by subclasses.
        """
    def _initMotionClipForCharacter(self, character: RagdollCharacter) -> None:
        """
        Creates the default motion clip geometry for a new character and
        adds it to the scene. This may be overridden by subclasses.
        """
    def buildMotionClip(self, rest_skel_path: str, output_skel_path: str, startframe: int, endframe: int, fps: float = ...) -> hou.Geometry:
        """
        Build a motionclip over the frame range, using the provided rest
        and output skeleton paths.
        """
    def setMotionClipEvaluatorActive(self, active: bool) -> None: ...
    def _updateXformGadget(self, name: str) -> bool: ...
    def _addXformGadgetInstance(self, name: str) -> None: ...
    def _removeXformGadgetInstance(self, name: str) -> None: ...
    def showXformGadget(self, name: str, on: bool) -> None: ...
    def resetGroundPlanePosition(self) -> None:
        """
        Resets the ground plane to the origin.
        """
    def enableGroundPlaneDisplay(self, enable: bool, add_undo: bool = False) -> None:
        """Toggles whether the ground plane is displayed."""
    def enableGroundPlane(self, enable: bool) -> None:
        """Toggles whether the ground plane is enabled in the solver."""
    def groundPositionSetting(self) -> hou.Vector3:
        """Setting for the ground plane position."""
    def groundRotationSetting(self) -> hou.Vector3:
        """Setting for the ground plane rotation."""
    def groundDisplaySetting(self) -> bool:
        """Setting for displaying the ground plane."""
    def groundEnableSetting(self) -> bool:
        """Setting for enabling the ground plane in the solver."""
    def gravitySetting(self) -> hou.Vector3:
        """Setting for the solver's gravity."""
    def groundBounceSetting(self) -> float:
        """Setting for the ground plane's bounce."""
    def groundFrictionSetting(self) -> float:
        """Setting for the ground plane's friction."""
    def timestepSetting(self) -> float:
        """Setting for the solver's timestep."""
    def getVisualiserOffset(self) -> hou.Vector3:
        """Setting for the visualiser offset position."""
    def getVisualiserOffsetHandlePivot(self) -> hou.Vector3:
        """Setting for the offset handle's pivot."""
    def getVisualiserOffsetHandleVisibility(self) -> bool:
        """Setting for whether the offset handle is visible."""
    def getShowShapeIntersections(self) -> bool:
        """Setting for shape intersection debug drawable."""
    def getShowShapesOutsideLimits(self) -> bool:
        """Setting for shape outside limits debug drawable."""
    def onDisplayModeChanged(self, mode: int) -> None:
        """
        Updates the current display mode for the ragdolls.
        """
    def _initDrawablesFromGraph(self) -> None: ...
    def _updateDrawables(self, time: float) -> None:
        """
        Updates the ragdoll-related drawables when runSceneCallbacks() is
        invoked. This should only be called by the RagdollDrawableEvaluator!
        """
    def _offsetDrawables(self) -> None: ...
    def showDebugDrawables(self) -> None: ...
    def _updateDrawablesVisibility(self) -> None: ...
    def removeSceneCallbacksDrawables(self) -> None: ...
    def viewerStateScopeChannels(self) -> None: ...
    def getRagdollSelectionFromSourceControls(self, source_controls: Iterable[apex.Control]) -> dict[hou.SimpleDrawable, list[hou.Prim]]:
        """
        Translate from the selected controls on the source character to a
        selection of ragdoll shapes (based on the mapping).
        This returns an object that mimics the self.selection that we are
        already using.
        """
    def getSelectedShapes(self) -> _ShapeSelection | Literal[False]: ...
    def _selectCollisionShapes(self, new_selection: Mapping[hou.SimpleDrawable, Sequence[hou.Prim]], cur_selection: tuple[hou.SimpleDrawable | None, hou.Prim | None] | None = None, pick_modifier: hou.EnumValue[hou.pickModifier] = ...) -> None: ...
    def setCursorIcon(self, text: str) -> None: ...
    def _updateSliderWidgetFromSelection(self, onlyAnimated: bool = False) -> bool | None: ...
    def reloadMotionClips(self, chars_to_reload: Sequence[RagdollCharacter], generate_undo: bool = True) -> None:
        """
        Reloads the target animation for the specified characters.
        """
    def addGeometryChannelCallbacks(self, collection_names: Iterable[str]) -> None: ...
    def removeGeometryChannelCallbacks(self) -> None: ...
    def onGeometryChannelsChanged(self, channels: tuple[str, ...], cl_name: str) -> None: ...
    def doBake(self, bakeframe: float | None = None, key_existing: bool = False, controls: Sequence[apex.Control] | None = None, build_layer: bool = True, increment: int = 1, do_resample: bool = True, bake_compute: bool = True, start_frame: float = 1, create_missing_bindings: bool = True) -> None:
        """
        New way to bake result of the ragdoll simulation onto the rig's controls
        using Bake.py in an effort to unify baking across tools     

        parm: bake_compute determines if we compute the xform from skeleton
        when set to false we just copy the keys over...   
        The reason we call this is any slight difference in the start pose 
        for the sim will cause the simulation to be entirely different.
        To make sure the starting conditions are exactly the same, we bake the 
        controls directly on the first frame on the simulation instead of 
        computing new transforms but looking at the result of the simulation    
        """
    def postBakeUpdate(self) -> None: ...
    def showBakeAdditiveLayerToggle(self, show: bool) -> None:
        """
        Shows / Hides Additive Layer toggle on the baking menu
        we do this because it's not relevant to ragdoll as 
        we always want to bake override layers    
        """
    def getSourceControlsToBake(self) -> list[apex.Control]:
        """
        If we have a source control selection, Bake Keys or Recording
        Poses will write to those. If we have nothing selected, we will write to 
        ALL source controls of all character that have a ragdoll representation.
        """
    def removeRagdollCtrls(self, controls: Iterable[apex.Control]) -> list[apex.Control]: ...
    def createMissingBindings(self, controls: Sequence[apex.Control]) -> None:
        """
        If a character has not been touched, then it has no bindings and we
        need bindings to be able to bake. This is unlikely to happen in the
        'real world' but is necessary.    
        """
    def buildRagdollLayer(self) -> None: ...
    def _readMapping(self) -> None: ...

class RagdollBaseDrawableEvaluator:
    """
    Scene callback which updates the ragdoll drawables after parameter
    changes, frame changes, etc.
    """
    drawables: list[apexscene.SceneOutputDrawable]
    def __init__(self, tool: RagdollStateBase) -> None: ...
    def __call__(self, time: float, **kwargs: object) -> None: ...

class RagdollMotionClipEvaluator:
    """
    Tracks whether the target animation needs to be reloaded when data ids from
    the animation bindings change.
    This runs during the pre-evaluation event, rather than as a scene callback,
    since this may update graph inputs.
    """
    def __init__(self, tool: RagdollStateBase) -> None: ...
    def loadSessionDataIds(self, scene: apex.Scene) -> None: ...
    def saveSessionDataIds(self, scene: apex.Scene) -> None:
        """
        Stash the data ids in the scene so that we can reload them when
        re-entering the tool and avoid unnecessary rebuilding of motion clips
        if the animation hasn't changed. Note that these shouldn't be saved to
        geometry since data ids are only valid in the current process,
        which works since python objects in apex.Scene are not saved.
        """
    def setActive(self, active: bool) -> None: ...
    def setNeedsUpdate(self) -> None: ...
    def updateChannelDataIds(self) -> list[RagdollCharacter]: ...
    def __call__(self, time: float) -> None: ...

class RagdollControlEndpoint(mapping.ControlEndpoint):
    """
    Defines a custom ControlEndpoint that inherits from mapping.ControlEndpoint
    This class stores the name of the character the control is associated with
    in self.character_rig_path
    """
    control_name: str
    character_rig_path: str
    def __init__(self, control_name: str, character_rig_path: str) -> None: ...

class RagdollJointEndpoint(mapping.MappingEndpoint):
    """
    Defines a custom ControlEndpoint that inherits from mapping.ControlEndpoint
    This class stores the name of the character the control is associated with
    in self.character_name along with a overriden xform method that gets the xform
    for the joint.
    """
    control_name: str
    character_name: str
    _tool: weakref.ref[RagdollStateBase]
    _output_name: str
    _offset_xform: hou.Matrix4
    def __init__(self, tool: RagdollStateBase, control_name: str, character_name: str, output_name: str = 'skeleton', offset_xform: hou.Matrix4 = ..., color: hou.Color = ...) -> None: ...
    @property
    def tool(self) -> RagdollStateBase | None: ...
    def xform(self, control_manager: apex.ControlManager | None) -> hou.Matrix4: ...
    def setOutputName(self, output_name: str) -> None: ...
    def color(self) -> hou.Color: ...
    @staticmethod
    def getJointFullTransform(scene: apex.Scene, graph: str, character_name: str, joint_name: str, output_name: str = 'skeleton') -> tuple[tuple[float, float, float], hou.Matrix3]: ...

class VisualiserOffsetXformGadgetUndo:
    prev_offset: hou.Vector3
    prev_pivot: hou.Vector3
    prev_visibility: bool
    offset: hou.Vector3
    pivot: hou.Vector3
    visibility: bool
    def __init__(self, state: RagdollStateBase, prev_offset: hou.Vector3, prev_pivot: hou.Vector3, prev_visibility: bool, offset: hou.Vector3, pivot: hou.Vector3, visibility: bool) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class ShowShapeIntersectionsUndo:
    prev_visibility: bool
    curr_visibility: bool
    def __init__(self, state: RagdollStateBase, prev_vis: bool, curr_vis: bool) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class ShowShapesOutsideLimitsUndo:
    prev_visibility: bool
    curr_visibility: bool
    def __init__(self, state: RagdollStateBase, prev_vis: bool, curr_vis: bool) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class SelectCollisionShapesUndo:
    prev_selection: _ShapeSelection
    selection: _ShapeSelection
    def __init__(self, state: RagdollStateBase, prev_selection: _ShapeSelection, selection: _ShapeSelection) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class GroundplaneXformGadgetUndo:
    def __init__(self, state: RagdollStateBase, prev_pos: hou.Vector3, prev_rot: hou.Vector3, pos: hou.Vector3, rot: hou.Vector3) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class DisplayGroundPlaneUndo:
    def __init__(self, state: RagdollStateBase, prev_val: bool, val: bool, update_settings: bool) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class EnableGroundPlaneUndo:
    def __init__(self, state: RagdollStateBase, prev_val: bool, val: bool) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class DisplayModeUndo:
    prev_val: int
    val: int
    def __init__(self, state: RagdollStateBase, prev_val: int, val: int) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class SetSolverParmsUndo:
    """
    Called when changing solver parameters in the CTRL + G HUD    
    """
    def __init__(self, state: RagdollStateBase, prev_parms: apex.Dict, parms: apex.Dict) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class SetRagdollChannelsUndo:
    data_path: str
    prev_channel_prims: hou.Geometry
    channel_prims: hou.Geometry
    add_to_playbar: bool
    def __init__(self, state: RagdollStateBase, data_path: str, prev_channel_prims: hou.Geometry, channel_prims: hou.Geometry, add_to_playbar: bool = True) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class ReloadTargetAnimationUndo:
    data_path: str
    prev_motionclip: hou.Geometry
    motionclip: hou.Geometry
    def __init__(self, state: RagdollStateBase, data_path: str, prev_motionclip: hou.Geometry, motionclip: hou.Geometry) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...
