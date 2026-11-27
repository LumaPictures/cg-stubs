import apex
import hou
from apex import ragdollconstraints as ragdollconstraints, ragdollutils as ragdollutils, scene_2 as scene
from apex.autorigtool import _ToolActivateKwargs
from apex.control_2 import ControlManager as ControlManager
from apex.ragdollbase import DRAWABLE_EVALUATOR_KEY as DRAWABLE_EVALUATOR_KEY, RAGDOLL_ANIM_LAYER_NAME as RAGDOLL_ANIM_LAYER_NAME, RagdollCharacter as RagdollCharacter, RagdollDrawableDisplayMode as RagdollDrawableDisplayMode, RagdollJointEndpoint as RagdollJointEndpoint, RagdollStateBase as RagdollStateBase, _AnimateState as _RagdollBaseState
from apex.ragdollconstraints import ConstraintsStateHolder as ConstraintsStateHolder, RagdollConstraintsGadgetEvalMode as RagdollConstraintsGadgetEvalMode
from apex.ragdollforces import ForcesStateHolder as ForcesStateHolder, RagdollAnimStackGetter as RagdollAnimStackGetter, RagdollForcesManager as RagdollForcesManager, RagdollForcesRigBuilder as RagdollForcesRigBuilder, RagdollForcesType as RagdollForcesType
from apex.stateutils_2 import Hotkeys as Hotkeys
from apex.ui.ragdollwidgets import RagdollBaseParameterWidget as RagdollBaseParameterWidget, RagdollTabs as RagdollTabs, RagdollToolParameterWidget as RagdollToolParameterWidget, RagdollToolSliderWidget as RagdollToolSliderWidget
from apex.ui.statecommandutils import updateToolbox as updateToolbox
from apex.utils import addAnimateStateUndo as addAnimateStateUndo
from apex.xformgadget import _HandleStartUpdateKwargs, _HandleUpdateKwargs
from collections.abc import Collection, Container, Iterable, Mapping, Sequence
from enum import StrEnum
from houtypes import ViewerParmProperties, ViewerStateDrawKwargs, ViewerStateEventKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs, ViewerStateParmChangeKwargs, ViewerStatePlaybackChangeKwargs
from kinefx.stateutils import KinefxPackedHighlighter
from statehud.parmutils import _HUDParmValue
from statehud.window import _ParmEventDict
from typing import Literal, Protocol

from typing import TypeAlias
from typing import TypeAlias
_CurSelection: TypeAlias = tuple[hou.SimpleDrawable | None, hou.Prim | None] | tuple[()]
class _AnimateState(_RagdollBaseState, Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) this module uses."""
    @property
    def hide_ctrls_during_playback(self) -> bool: ...
    @property
    def hide_ctrls_during_drag(self) -> bool: ...
    @property
    def hide_ctrls_during_scrub(self) -> bool: ...

class _RagdollActivateKwargs(_ToolActivateKwargs, total=False):
    ragdollgraph: apex.SceneGraph

RAGDOLL_SOLVER_PARMS_PATH: str
RAGDOLL_CONSTRAINTS_PARMS_PATH: str
RAGDOLL_CONSTRAINTS_CHANNELPRIMS_PATH: str
CONSTRAINTS_PARMS_ATTRIB_NAME: str
RAGDOLL_MOTIONCLIP_SESSION_DATAIDS_PATH: str
PROPERTY_AUTO_RESET_SIM: str
PROPERTY_AUTO_RELOAD_TARGET_ANIM: str
PROPERTY_START_FRAME: str

class RagdollToolbox(StrEnum):
    Tool = 'apex_ragdoll'
    Tether = 'apex_ragdoll_tether'
    Force = 'apex_ragdoll_force'
    Delete = 'apex_ragdoll_delete'
    Display = 'apex_ragdoll_display'
    Shapes = 'apex_ragdoll_shapes'
    Skin = 'apex_ragdoll_skin'
    Wind = 'apex_ragdoll_wind'
    Drag = 'apex_ragdoll_drag'
    Magnet = 'apex_ragdoll_magnet'
    Turbulence = 'apex_ragdoll_turbulence'

class RagdollTool(RagdollStateBase[RagdollToolSliderWidget, RagdollToolParameterWidget]):
    constraints_manager: ragdollconstraints.RagdollConstraintsManager
    bm_manager: ragdollconstraints.RagdollBookmarkManager
    forces_manager: RagdollForcesManager
    forces_stack_getter: RagdollAnimStackGetter | None
    add_hk: str
    delete_hk: str
    slider_hk: str
    hud_parm_hk: str
    add_force_hk: str
    hud_rows: list[hou._HudRow]
    hud_widget: RagdollToolSliderWidget | None
    settings_widget: RagdollToolParameterWidget | None
    groundplane_drawable: scene.SceneOutputDrawable | None
    selection: ragdollutils._ShapeSelection
    cur_selection: _CurSelection
    prehighlighters: dict[hou.Drawable, KinefxPackedHighlighter]
    forces_visualiser: scene.SceneOutputDrawable | None
    sprite_gadget: ragdollutils.RagdollSpriteGadget | None
    def __init__(self, viewer_state: _AnimateState) -> None: ...
    @property
    def constraints_parms_path(self) -> str:
        """The scene graph path where the constraints parms are saved. """
    @property
    def constraints_channelprims_path(self) -> str:
        """The scene graph path where the constraints channel prims are saved. """
    @property
    def default_display_mode(self) -> int:
        """The default display mode if no previous setting exists."""
    def saveArbitraryParmsData(self, attrib_name: str, parms: apex.Dict, path: str) -> None: ...
    def loadForcesParmsData(self) -> None:
        """
        Load the constraints parameters from the scene  
        """
    def saveForcesParmsData(self) -> None: ...
    def loadForcesIntoRig(self) -> None: ...
    def saveConstraintsParmsData(self) -> None:
        """
        Save the constraints parameters to the scene.
        """
    def loadConstraintsParmsData(self) -> None:
        """
        Load the constraints parameters from the scene  
        """
    def deleteBookmarkManager(self) -> None: ...
    def saveBookmarks(self) -> None:
        """
        save bookmarks to scene.
        This should always be called after saveConstraintsParmsData    
        """
    def loadBookmarks(self) -> None:
        """
        load saved bookmarks into the manager    
        """
    def saveConstraintsChannelprims(self) -> None:
        """
        Save the constraints channelprims to the scene    
        """
    def saveLiveData(self) -> None:
        """
        Saves solver parms, constraints parms and constraints
        channel prims to the scene    
        """
    def loadConstraintsParmsDataIntoRig(self) -> None: ...
    def loadConstraintsChannelprimsIntoRig(self) -> None: ...
    def loadConstraintsChannelPrims(self) -> None:
        """
        Load the constraints channel prims from the scene    
        """
    def getConstraintsHandleParms(self) -> hou._OptionDict:
        """
        Returns the dict containing the constraint handle parameters
        this is saved on the channel prims as we made the handles non
        animatable    
        """
    def getConstraintsGadgetEvalMode(self) -> RagdollConstraintsGadgetEvalMode: ...
    def setConstraintsGadgetEvalMode(self, mode: ragdollconstraints.RagdollConstraintsGadgetEvalMode) -> None: ...
    def removeConstraintHandleFromParms(self, base_parms: apex.Dict, constraints: Container[str]) -> apex.Dict: ...
    def updateConstraintsHandleParms(self, parms: apex.Dict) -> None: ...
    def setActiveRangeForConstraints(self, names: Iterable[str], frame_range: hou.Vector2, delete: bool = False) -> None:
        '''
        For selected constraints, assuming the user selected a range
        set keys for "enable" on the constraints.
        sets enable = 0 on pre_start and on post_end
        sets enable = 1 on start -> end

        delete is a poorly named bool but essentially when set to True it
        destroys the key based on the range, otherwise it either shrinks
        or extends
        
        '''
    def overrideAngularStiffness(self, value: bool, constraint_name: str) -> None:
        """
        When toggling the override on or off, we need to load or unload
        angular stiffness channel prims into the rig    
        """
    def createDefaultAngularStiffnessChannel(self, constraint_name: str, geo: hou.Geometry) -> None: ...
    def getSelectedForces(self) -> list[str]:
        """
        returns a tuple of all the controls associated with a ragdoll force    
        """
    def createForce(self, force_name_type: str) -> None: ...
    def createForceFromGadget(self, name: str, unused: int, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None) -> None:
        """
        unused and pick modifier are required by the callback but
        we don't use them    
        """
    def selectCreatedForce(self, name: str) -> None: ...
    def addCreatedForceToActiveLayer(self) -> None: ...
    def initForceInfluenceChannelPrims(self, idx: int) -> None: ...
    def createMissingForceInfluenceChannels(self) -> None: ...
    def deleteForceEvent(self, forces: Collection[str]) -> None: ...
    def clearForcesFromRig(self) -> None: ...
    def removeForceChannelPrims(self, forces: Collection[str]) -> None: ...
    def removeForceInfluenceChannelPrims(self, forces: Collection[str]) -> None: ...
    def getCurrentForceState(self) -> ForcesStateHolder:
        """
        Get a current state that we can revert to when undoing a 
        force authoring (creation / deletion)    
        """
    def getAllControlPaths(self) -> list[str]: ...
    def getSelectedControlPaths(self) -> list[str]: ...
    def getVisibleControlPaths(self) -> list[str]:
        """
        Called by the main state to populate the selection sets window
        This function must return a list of paths
        """
    def getCurrentSelectedControlPath(self) -> str | None: ...
    def selectionSetsSelectControls(self, ctrl_paths: Sequence[str], cur_ctrl: str | None, pick_modifier: hou.EnumValue[hou.pickModifier]) -> None: ...
    def selectionSetsShowControls(self, ctrl_paths: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier]) -> None: ...
    def selectionSetsPinControls(self, ctrl_paths: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier]) -> None: ...
    def onActivate(self, kwargs: _RagdollActivateKwargs) -> Literal[True]: ...
    def onDeactivate(self) -> None: ...
    def onDrawInterrupt(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    def onSelectionChanged(self, control_selection: tuple[str, ...]) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onPlaybackChangeEvent(self, kwargs: ViewerStatePlaybackChangeKwargs) -> None: ...
    def onUpdateParmsAndControlsFromWidget(self, control_parms: Sequence[str] | None = None) -> Literal[True]:
        """
        Called when a value is set in the Controls tab of the g hud    
        """
    def onAnimLayerChanged(self) -> None:
        """
        Called whenever a change is made to the animation layers stack, such
        as locking, muting, soloing, adding new layers, switching layers, etc.
        """
    def onPoseEvent(self, kwargs: ViewerStateEventKwargs | _HandleUpdateKwargs) -> Literal[True]: ...
    def onPoseEndEvent(self, kwargs: ViewerStateEventKwargs | _HandleUpdateKwargs) -> Literal[True]: ...
    def onPreEvaluationEvent(self, time: float) -> None: ...
    def onPostEvaluationEvent(self, time: float) -> None: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onHUDSettingEvent(self, kwargs: _ParmEventDict) -> None:
        """
        Call updatetoolbox to run a state command on the animate state
        that updates our toolbox
        """
    def displayModeToken(self, mode: int) -> str: ...
    def displayModeFromString(self, mode: str) -> int: ...
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> None:
        """
        Called before the right click menu is open
        should update ragdoll specific options    
        """
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> None:
        """
        Called when a ragdoll specific option is clicked in the right click
        context menu    
        """
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None: ...
    def updateStateParms(self, state_parms: Mapping[str, ViewerParmProperties]) -> None: ...
    def createConstraintEvent(self) -> bool: ...
    def deleteConstraintEvent(self) -> None: ...
    def showSelectedBookmarks(self) -> None: ...
    def constraintHandlesCleanup(self, handleparms: apex.Dict) -> None:
        """
        Wraps a few methods that clean up the the handles based on parms
        and recreates the necessary handles    
        """
    def getConstraintsState(self) -> ConstraintsStateHolder: ...
    def getCurrConstraintsState(self, prev_state: ConstraintsStateHolder) -> ConstraintsStateHolder:
        """
        prev_state is a ConstraintsStateHolder
        this also does the deletion which maybe it shouldnt...    
        """
    def recomputeConstraintOffset(self) -> bool: ...
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> Literal[True]: ...
    def onCommand(self, command: str, args: Mapping[str, object]) -> None: ...
    def onPoseStartEvent(self, kwargs: ViewerStateEventKwargs | _HandleStartUpdateKwargs) -> None: ...
    def onPoseEndPreKeyEvent(self, kwargs: ViewerStateEventKwargs | _HandleUpdateKwargs) -> None: ...
    def setResetSimEvaluatorActive(self, on: bool) -> None: ...
    def getMatchWorldVisibility(self) -> int:
        """Setting for whether to show match world constraints """
    def getAngularLimitStiffness(self) -> float:
        """Setting for Angular Limit Stiffness (cone twist constraints)"""
    def getAngularLimitDampingRatio(self) -> float:
        """Setting for Angular Limit Damping Ratio (cone twist constraints)"""
    def buildConstraintsGadget(self, active: bool = False) -> None:
        """    

        If we really need to, we could have RagdollJointEndpoint take in a shared
        object with the evaluated geometry so each endpoint does not have
        to evaluate the graph everytime
        
        """
    def updateConstraintsGadget(self) -> None: ...
    def hideConstraintsGadget(self) -> None: ...
    def showConstraintsGadget(self) -> None: ...
    def updateGadgetFromPose(self, update_eval: bool = False) -> None: ...
    def addConstraintHandlesToRig(self) -> None:
        """
        This creates the necessary nodes to add transform objects
        to the ragdoll rig for the constraint  
        """
    def setGadgetHighlighting(self, on: bool) -> None: ...
    def clearGadgetHighlighting(self) -> None: ...
    def updateGadgetHighlighting(self) -> None: ...
    def getGadgetGeometry(self) -> hou.Geometry: ...
    def buildGadgetHighlightingFromNames(self, names: Collection[str]) -> None: ...
    def buildGadgetHighlightingFromConstraintNames(self, names: Iterable[str]) -> None: ...
    def addDrawablesForSimUtilities(self) -> None:
        """
        when adding a constraint we need to add a character which means
        building the drawables for the anchor controls and adding an entry in the
        selection manager model    
        """
    def deleteSimUtilities(self) -> None: ...
    def addConstraintHandlesToGraphParms(self, cst_names: Iterable[str]) -> apex.Dict:
        """
        handles read graph parms to then update the transform objects but
        as we're creating those on the fly they don't appear in the graph parms
        which causes the handles to error out.
        we need to manually do that unfortunately because that process only happens when
        first loading the rigs    
        """
    def deleteConstraintFromGraphParms(self, constraint: str) -> None:
        """
        deletes the entry in the parms dict associated with the constraint
        otherwise we can run into the situation where a user sets up a constraint
        deletes it, then when they recreate a constraint it reads in those values
        as they're tied to the constraint name    
        """
    def updateSimUtilities(self) -> None:
        """
        Scene Objects refer to either ragdoll forces
        or ragdoll constraints / tethers
        This should be called when a force or tether is authored
        to make sure everything related is properly updated    
        """
    def updateStackBindings(self) -> bool:
        """
        Make sure we pull the latest components for our animstack
        so our forces stay up to date    
        """
    def deleteConstraintsHandles(self) -> None: ...
    def frameSelectedControls(self) -> list[hou.Geometry]: ...
    def isRecordingPoses(self) -> bool: ...
    def setChannelValue(self, cl_name: str, channel: hou.ChannelPrim, newval: float, key: bool = False, interpolation: hou.EnumValue[hou.segmentType] | None = None, frame: float | None = None) -> None: ...
    def onChannelsChangeEndEvent(self, collection_name: str, channel_names: Sequence[str]) -> None: ...
    def onGeometryChannelsChanged(self, channels: tuple[str, ...], cl_name: str) -> None: ...
    def addGeometryChannelCallbacks(self, collection_names: Iterable[str]) -> None: ...
    def removeGeometryChannelCallbacks(self) -> None: ...
    def getScopedChannels(self) -> dict[str, list[str]]: ...
    def scopeChannels(self, channel_list: hou.ChannelList, scoped_channels: Mapping[str, Sequence[str]], pinned_channels: Mapping[str, Iterable[str]]) -> None: ...
    def onChannelWidgetVisibilityChange(self, on: bool) -> None:
        """ Callback for when the channel widget window is shown or hidden. """
    def updateConstraintsSliderWidgetFromSelection(self, onlyAnimated: bool = True, scope: bool = True) -> bool:
        """
        Update Constraints TAB    
        """
    def reloadTargetAnimation(self) -> None: ...
    def onStartRecordingEvent(self, kwargs: Mapping[str, _HUDParmValue]) -> Literal[True]: ...
    def onStopRecordingEvent(self, kwargs: Mapping[str, _HUDParmValue]) -> Literal[True]: ...
    def onBakeEvent(self, kwargs: Mapping[str, _HUDParmValue]) -> Literal[True]:
        """
        {
            'bake_useframerange': True 
            
                -> when False, use playbar selection or playbar as fallback

            'bake_framerange': hou.Vector2 [1, 240]

                -> frame range used for baking
            
            'bake_keep': False 
                
                -> whether to keep existing keys
            
            'bake_resample': True 
            
                -> when False, only bake to existing keys, else bake to 
                   bake_frequency 
            
            'bake_frequency': 1 
            
                -> bake every # frame
            
            'bake_newlayer': False 
            
                -> whether to bake to a new layer 
            
            'bake_additivelayer': True 
            
                -> whether the new layer is over or add
                we disregard this in ragdoll...
        }
        """
    def doFrameRangeBake(self, frameRange: Sequence[int], key_existing: bool = False, build_layer: bool = True, resample_keys: bool = True) -> None: ...
    def showMatchWorld(self, v: bool) -> None:
        """
        Toggles whether the constraint visualizer also displays
        match world constraints    
        """
    def enableAutoReloadTargetAnim(self, enable: bool) -> None:
        """
        Toggle whether the auto reload animation mode is enabled.
        """
    def resetSim(self) -> None:
        """
        Ensure the next graph evaluation has 'forceresetsim' enabled to clear
        cached frames.
        """
    def enableAutoResetSim(self, enable: bool) -> None:
        """
        Toggle whether the auto resim mode is enabled.
        """
    def doScopeRagdollParameters(self, v: bool) -> None:
        """
        Imagine you have keyed a bunch of parameters on the hand shape,
        like stiffness etc...
        and you also have keys on the rig control tied to that hand like
        ik_hand_l or something
        when selecting that rig control and adding a key, the ragdoll
        geometry channels will also get scoped which means you're adding 
        unnecessary keys to the ragdoll parameters.
        Turning this option off means the channels will not get scoped when
        a rig control is selected.    
        """
    def writeRigToSceneGraph(self, v: bool) -> None:
        """
        Toggle the setting for writing the rig to the scene graph on exit.
        """
    def resetTool(self) -> None:
        """
        Start anew. This means destroying forces and constraints and
        setting all the other parameters to default    
        """
    def onConstraintsWidgetValueChange(self, slider_names: Sequence[str], vals: Sequence[float], key: bool = False, del_keys: bool = False, add_undo: bool = True, single: bool = False) -> None:
        """
        Creates channel prims for the selected constraint    
        """
    def setStartTime(self, v: float, add_undo: bool = True) -> None:
        """
        Updates the time of the first simulation frame.
        """
    def updateSimulation(self) -> None:
        """
        Updates the simulation after a parameter change.
        This either resimulates the current frame or resets the sim depending
        on the tool's settings, and updates the drawables.
        """
    def doScopeSetting(self) -> bool:
        """
        Setting for enabling/disabling the scoping of ragdoll channels when
        selecting a rig control    
        See doScopeRagdollParameters method
        """
    @property
    def viewer_state(self) -> _AnimateState | None: ...

class RagdollDrawableEvaluator:
    """
    Scene callback which updates the ragdoll drawables after parameter
    changes, frame changes, etc.
    """
    drawables: list[scene.SceneOutputDrawable]
    def __init__(self, tool: RagdollTool) -> None: ...
    def __call__(self, time: float, **kwargs: object) -> None: ...

class RagdollResetSimEvaluator:
    """
    Tracks whether the simulation needs to be reset when the ragdoll's channel
    prims or motionclip have changed, if Auto Reset is enabled in the tool.
    """
    cached_dataids: dict[str, list[hou.AttribDataId] | tuple[int, ...]]
    active: bool
    def __init__(self, tool: RagdollTool) -> None: ...
    @property
    def tool(self) -> RagdollTool | None: ...
    def dirtyAll(self) -> None: ...
    def updateDataIds(self) -> bool: ...
    def __call__(self, time: float) -> None: ...

class DoScopeRagdollParmsUndo:
    def __init__(self, state: RagdollStateBase, prev_val: bool, val: bool) -> None: ...
    @property
    def state(self) -> RagdollStateBase | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class ShowConstraintsUndo:
    prev_vis: int
    vis: int
    def __init__(self, state: RagdollTool, prev_vis: int, vis: int) -> None: ...
    @property
    def state(self) -> RagdollTool | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class ShowMatchWorldUndo:
    prev_vis: int
    vis: int
    def __init__(self, state: RagdollTool, prev_vis: int, vis: int) -> None: ...
    @property
    def state(self) -> RagdollTool | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class SetStartTimeUndo:
    prev_starttime: float
    starttime: float
    def __init__(self, state: RagdollTool, prev_starttime: float, starttime: float) -> None: ...
    @property
    def state(self) -> RagdollTool | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class EnableAutoReloadTargetAnimUndo:
    prev_val: bool
    val: bool
    def __init__(self, state: RagdollTool, prev_val: bool, val: bool) -> None: ...
    @property
    def state(self) -> RagdollTool | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class UpdateFrameUndo:
    start: int
    end: int
    def __init__(self, state: RagdollTool, start: int, end: int) -> None: ...
    @property
    def state(self) -> RagdollTool | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...
    def doUpdateFrame(self, frame: float) -> None: ...

class EnableAutoResetSimUndo:
    prev_val: bool
    val: bool
    def __init__(self, state: RagdollTool, prev_val: bool, val: bool) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...
    @property
    def state(self) -> RagdollTool | None: ...

class WriteRigToSceneGraphUndo:
    prev_val: bool
    val: bool
    def __init__(self, state: RagdollTool, prev_val: bool, val: bool) -> None: ...
    @property
    def state(self) -> RagdollTool | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class SetConstraintsChannelsUndo:
    """
    Called when the user hits ctrl+Z after setting a value on a slider
    in the constraints tab    
    """
    prev_channel_prims: hou.Geometry
    curr_channel_prims: hou.Geometry
    def __init__(self, state: RagdollTool, prev_channel_prims: hou.Geometry, curr_channel_prims: hou.Geometry) -> None: ...
    @property
    def state(self) -> RagdollTool | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class AuthorConstraintsUndo:
    """
    This undo is used when either destroying or creating a constraint 
    so I needed a word that evokes both. 
    Author came to mind because USD, although 
    USD is famously non-destructive...    
    """
    prev_state: ConstraintsStateHolder
    curr_state: ConstraintsStateHolder
    def __init__(self, state: RagdollTool, prev_state: ConstraintsStateHolder, curr_state: ConstraintsStateHolder) -> None: ...
    @property
    def state(self) -> RagdollTool | None: ...
    def redo(self) -> None: ...
    def undo(self) -> None: ...

class ConstraintActiveRangeSetterUndo:
    """
    Called when a user hits 'h' with a range and a constraint selected    
    """
    prev_bmdata: apex.Dict
    curr_bmdata: apex.Dict
    prev_channels: hou.Geometry
    curr_channels: hou.Geometry
    def __init__(self, tool: RagdollTool, prev_bmdata: apex.Dict, curr_bmdata: apex.Dict, prev_channels: hou.Geometry, curr_channels: hou.Geometry) -> None: ...
    @property
    def state(self) -> RagdollTool | None: ...
    def redo(self) -> None: ...
    def undo(self) -> None: ...

class AuthorForcesUndo:
    """
    This undo is used when either destroying or creating forces
    based on AuthorConstraintsUndo
    """
    prev_state: ForcesStateHolder
    curr_state: ForcesStateHolder
    def __init__(self, state: RagdollTool, prev_state: ForcesStateHolder, curr_state: ForcesStateHolder) -> None: ...
    @property
    def state(self) -> RagdollTool | None: ...
    def redo(self) -> None: ...
    def undo(self) -> None: ...

def load(viewer_state: _AnimateState) -> RagdollTool:
    """
    Necessary Entry Point    
    """
def bindParametersToTemplate(template: hou.ViewerStateTemplate) -> None:
    """
    Called by the animate state template builder to add to the tool box    
    """
def bindActionsToMenu(menu: hou.ViewerStateMenu, hotkeys: Hotkeys) -> None:
    """
    Called by the animate state template builder 
    to add to the right click menu   
    """
def getToolStateParms() -> list[str]:
    """
    Called by the animate state to figure out which parms to hide    
    must return a list of all the state parms used by the tool
    """
def getToolMenuActions() -> list[str]:
    """
    Called by the animate state to figure out 
    which menu actions to hide / show  when entering / exiting the tool   
    """
