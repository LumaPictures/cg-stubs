import _apex
import apex
import hou
import typing
from PySide6 import QtCore as QtCore
from apex.animstack import ApexAnimStack as ApexAnimStack
from apex.apexanimatemodules.cameras import _AnimationPreferences
from apex.apexanimatemodules.channellist import ApexAnimateChannelList as ApexAnimateChannelList
from apex.apexanimatemodules.selectionsets import ApexAnimateSelectionSets as ApexAnimateSelectionSets
from apex.pickwalker import PickWalker as PickWalker
from apex.sceneevaluators import _SceneCallbacks
from apex.selectionhandler_2 import DrawableSelector as DrawableSelector
from apex.ui.selectionmanager.hudpanel import SelectionSetHUDPanel as SelectionSetHUDPanel
from apex.ui.selectionmanager.model import SelectionManagerModel as SelectionManagerModel
from apex.ui.splitchannelwidget import SplitChannelWidgetHandler as SplitChannelWidgetHandler
from apex.utils import addAnimateStateUndo as addAnimateStateUndo
from apex.xformgadget import ApexXformHandle as ApexXformHandle, TOGGLE_HANDLE_VIS_SYMBOL as TOGGLE_HANDLE_VIS_SYMBOL
from collections.abc import Collection, Container, Generator, Iterable, Mapping, Sequence
from contextlib import contextmanager
from houtypes import ViewerStateCommandKwargs, ViewerStateMenuPreOpenKwargs
from resourceutils import CursorIcon
from typing import Any, Protocol

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
class _UndoAction(Protocol):
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class _ChannelsUndoState(Protocol):
    """The members of the Animate viewer state (`viewer_states/apexanimate.py`) `SetChannelsUndo` uses."""
    @property
    def scene(self) -> apex.Scene: ...
    @property
    def hud_channel_panel(self) -> SplitChannelWidgetHandler | None: ...
    def muteSceneReload(self) -> None: ...
    def unmuteSceneReload(self) -> None: ...
    def pushChannels(self, include_pinned_channels: bool = ...) -> None: ...

class _NonAnimatableParmsUndoState(Protocol):
    """The members of the Animate viewer state `SetNonAnimatableParmsUndo` uses."""
    @property
    def scene(self) -> apex.Scene: ...
    def muteSceneReload(self) -> None: ...
    def unmuteSceneReload(self) -> None: ...
    def createAnimBinding(self, rig_path: str) -> apex.ChannelPrimBindings: ...
    def runSceneCallbacks(self, update_handle: bool = ..., force: bool = ...) -> None: ...

class _Tool(Protocol):
    """A tool of the Animate viewer state: what a tool module's `load(viewer_state)` returns. Tool
    classes share no base; the state calls their event handlers by name (`toolEvent()`), and the
    optional members (`hud_widget`, `settings_widget`, `category()`, ...) after `hasattr()`."""
    module_name: str
    def label(self) -> str: ...

class _AnimateState(Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): the members that several modules
    use. Each module's own `_AnimateState` extends this with the members only it uses."""
    scene_viewer: hou.SceneViewer
    sel_handlers: list[DrawableSelector]
    primary_control: str | None
    control_selection: tuple[str, ...]
    is_scrubbing: bool
    @property
    def scene(self) -> apex.Scene: ...
    @property
    def scene_node(self) -> hou.SopNode | None: ...
    @property
    def scene_callbacks(self) -> _SceneCallbacks: ...
    @property
    def control_manager(self) -> apex.ControlManager: ...
    @property
    def hotkeys(self) -> Hotkeys: ...
    @property
    def animstack(self) -> ApexAnimStack: ...
    @property
    def is_playing_back(self) -> bool: ...
    @property
    def cursor_icon(self) -> CursorIcon: ...
    @property
    def xform_gadget(self) -> ApexXformHandle: ...
    @property
    def pick_walker(self) -> PickWalker: ...
    @property
    def selection_manager_model(self) -> SelectionManagerModel: ...
    @property
    def hud_channel_panel(self) -> SplitChannelWidgetHandler | None: ...
    @property
    def hud_sel_panel(self) -> SelectionSetHUDPanel | None: ...
    @property
    def tools(self) -> dict[str, _Tool]: ...
    @property
    def active_tool(self) -> _Tool | None: ...
    def toolEvent(self, eventname: str, *args: object, **kwargs: object) -> Any: ...
    def getConfigValue(self, key: str, default: object = ...) -> Any: ...
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool: ...
    def channelListModule(self) -> ApexAnimateChannelList: ...
    def selectionSetsModule(self) -> ApexAnimateSelectionSets: ...
    def channelList(self) -> hou.ChannelList: ...
    def updateChannelList(self, update_pending: bool = ...) -> None: ...
    def updateChannelListPending(self) -> None: ...
    def updateSelectionManagerModel(self) -> None: ...
    def updateHUD(self) -> None: ...
    def runSceneCallbacks(self, update_handle: bool = ..., force: bool = ...) -> None: ...
    def pushChannels(self, include_pinned_channels: bool = ...) -> None: ...
    def muteSceneReload(self) -> None: ...
    def unmuteSceneReload(self) -> None: ...
    def createAnimBinding(self, rig_path: str) -> apex.ChannelPrimBindings: ...
    def findOrCreateAnimBinding(self, rig_path: str) -> apex.ChannelPrimBindings: ...
    def handleAnimLayerChanged(self, scope_channels: bool = ..., write_animation: bool = ...) -> None: ...
    def getScopedParms(self, components: str = ..., include_controlgroups: bool = ..., include_non_animatable: bool = ...) -> dict[str, list[str]]: ...
    def getScopedChannels(self) -> dict[str, list[str]]: ...
    def setKeysOrPending(self, controls: Iterable[str] | None = ...) -> None: ...
    def _updateNonAnimatableParms(self, controls: Iterable[str] | None = ...) -> None: ...
    def updateChannelPrimsFromParmComponents(self, components: str | Sequence[str], setKey: bool = ..., component_indices: Sequence[int] | None = ..., remove_keys: bool | None = ..., include_controgroups: bool = ...) -> None: ...
    def showBakeParms(self, parm_names: Iterable[str], on: bool = ...) -> None: ...
    def captureScreenshot(self) -> QtCore.QByteArray: ...
    def captureVideo(self, start_frame: int, end_frame: int, increment: int = ...) -> QtCore.QByteArray | None: ...
    def _getAnimationPreferences(self) -> _AnimationPreferences: ...
    def _nodeIsWritable(self) -> bool | hou.Parm | None: ...
    def _writeAnimationToGeometryParm(self, animation_parm: hou.Parm, pattern: str = ...) -> None: ...
    def writeToSopNode(self) -> None: ...
    def flashWarning(self, msg: str, duration: float = ...) -> None: ...
    def setCursorDescription(self, text: str | None = ..., prompt_only: bool = ...) -> None: ...
    def setDefaultCursorIcon(self, iconpath: str | None = ...) -> None: ...
    def showXformGadget(self, on: bool, force: bool = ...) -> None: ...
    def enableSelectOnly(self, on: bool) -> None: ...
    def _getAllCharacters(self, include_tool: bool = ...) -> list[str]: ...
    def _getAllControlPaths(self, include_internal: bool = ..., expand_multi_ctrls: bool = ..., include_constraints: bool = ...) -> list[str]: ...
    def _getControlSelectionList(self, include_public: bool = ..., include_tool: bool = ..., expand_multi_ctrls: bool = ...) -> list[str]: ...
    def _showCharacters(self, characters: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier] | None = ..., update_sel_sets: bool = ...) -> None: ...
    def _showControlsCmd(self, controls: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier] | None, hide_full_group: bool = ...) -> None: ...
    def showAllChars(self) -> None: ...
    def hideAllChars(self) -> None: ...
    def showAllControls(self) -> None: ...
    def hideAllControls(self) -> None: ...
    def updateControls(self, trs: apex.Dict, controls: Iterable[str], update_channel_widget: bool = ...) -> None: ...
    def setPinnedControls(self, ctrl_paths: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier]) -> None: ...
    def selectControlsCmd(self, ctrl_paths: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier], primary_control: str | None = ..., update_channel_widget: bool = ..., resolve_groups: bool = ..., run_control_callbacks: bool = ...) -> None: ...
    def _selectControls(self, ctrl_paths: Iterable[str], pick_modifier: hou.EnumValue[hou.pickModifier] | None = ..., primary_control: str | None = ..., update_sel_mgr: bool = ..., update_channel_list: bool = ..., update_channel_widget: bool = ..., run_control_callbacks: bool = ...) -> None: ...
    def setControlXforms(self, mapping_dict: Mapping[str, hou.Matrix4] | apex.Dict, use_t: bool = ..., use_r: bool = ..., use_s: bool = ..., smooth_rotate: bool = ...) -> None: ...
    def setXformForControls(self, ctrl_paths: Iterable[str], xform: hou.Matrix4, use_t: bool = ..., use_r: bool = ..., use_s: bool = ..., smooth_rotate: bool = ...) -> None: ...

CONFIG_FUNCTION: str
ANIM_NODE_CONFIG: str
EXCLUDE_GEO_PATTERN_CONFIG: str
DISABLE_AUTO_CHARACTER_CLEANUP_CONFIG: str
DISABLE_ANIM_TOOLS_CONFIG: str
DEFAULT_TOOL_CONFIG: str
TOOLS_CONFIG: str
USE_SPLIT_VIEW_CONFIG: str
HIDE_CONTROL_PARMS_CONFIG: str
RADIAL_TOOL_MENU: str
TOOL_CONSTRAINTS: str
TOOL_LOCATORS: str
TOOL_DYNAMICMOTION: str
TOOL_RAGDOLL: str
TOOL_RAGDOLL_POSING: str
TOOL_FBIK: str
TOOL_FBIK_POSING: str
TOOL_SECONDARYMOTION: str
TOOL_ANIMATE: str
TOOL_CUSTOM: str
TOOL_EFFECT: str
TOOLS_ANIMATION: list[str]
ANIMATION_TOOLS_STR_TO_LABEL: dict[str, str]
ANIMATION_TOOLS_STR_TO_ICON_NAME: dict[str, str]
ANIMATION_TOOLS_STR_TO_RADIAL_LOCATION: dict[str, hou.EnumValue[hou.radialItemLocation]]
ANIMATION_TOOLS_ITEMS: list[tuple[str, str | None, str | None]]
TOOL_AUTORIG: str
TOOLS_RIGGING: list[str]
DEFAULT_TOOLS: list[str]
SELECT_ONLY_ACTION: str
TEMP_HIDE_ALL_ACTION: str
TOGGLE_ALL_CONTROLS_SYMBOL: str
TOGGLE_ALL_CHARS_SYMBOL: str
SELECT_ALL_SYMBOL: str
CHILD_COMPENSATE_MODE: str
SELECT_DESCENDANTS_SYMBOL: str
PICK_WALK_UP_SYMBOL: str
PICK_WALK_GROW_UP_SYMBOL: str
PICK_WALK_SHRINK_UP_SYMBOL: str
PICK_WALK_DOWN_SYMBOL: str
PICK_WALK_GROW_DOWN_SYMBOL: str
PICK_WALK_SHRINK_DOWN_SYMBOL: str
PICK_WALK_LEFT_SYMBOL: str
PICK_WALK_GROW_LEFT_SYMBOL: str
PICK_WALK_SHRINK_LEFT_SYMBOL: str
PICK_WALK_RIGHT_SYMBOL: str
PICK_WALK_GROW_RIGHT_SYMBOL: str
PICK_WALK_SHRINK_RIGHT_SYMBOL: str
OPEN_LOG_ACTION: str
BAKE_ACTION: str
COPY_ACTION: str
PASTE_WORLD_XFORMS_ACTION: str
PASTE_LOCAL_XFORMS_ACTION: str
BIND_MOTION_PATH: str
CUSTOM_MIRROR_ACTION: str
DEFAULT_MIRROR_ACTION: str
SAVE_ANIM_CATALOG: str
SAVE_POSE_CATALOG: str
CREATE_CATALOG_FOLDER: str
RESET_ALL: str
RESET_CUSTOM: str
RESET_ANIMATION: str
EDIT_ANIMATION: str
NEW_CLIP: str
TOOL_HK: str
HK_RADIAL_MENU: str
HK_TOGGLE_ALL_HUDS: str
SUPPRESS_HOTKEYS: list[str]

class Hotkeys:
    """
    The hotkey symbols used in the Animate state.
    """
    hud_slider: str
    hud_parms: str
    frame_selected: str
    hud_sel: str
    hud_sel_main: str
    temp_hide_all: str
    toggle_all_ctrls: str
    toggle_all_chars: str
    select_all: str
    child_compensate: str
    reload: str
    select_only: str
    copy: str
    paste_world_xforms: str
    paste_local_xforms: str
    custom_mirror: str
    default_mirror: str
    bake: str
    save_anim_catalog: str
    save_pose_catalog: str
    create_catalog_folder: str
    reset_all: str
    reset_custom: str
    reset_animation: str
    new_clip: str
    edit_animation: str
    pick_walk_up: str
    pick_walk_grow_up: str
    pick_walk_shrink_up: str
    pick_walk_down: str
    pick_walk_grow_down: str
    pick_walk_shrink_down: str
    pick_walk_left: str
    pick_walk_grow_left: str
    pick_walk_shrink_left: str
    pick_walk_right: str
    pick_walk_grow_right: str
    pick_walk_shrink_right: str
    select_descendants: str
    tool_key_h: str
    tool_key_ctrl_h: str
    tool_key_shift_h: str
    tool_key_o: str
    tool_key_ctrl_e: str
    tool_key_enter: str
    tool_key_esc: str
    def __init__(self, state_typename: str, state_cat: hou.NodeTypeCategory) -> None: ...
    def definitions(self) -> hou.PluginHotkeyDefinitions:
        """
        Returns the hotkey definitions which can be registered with the
        viewer state template.
        """
    def context(self) -> str:
        """
        The hotkey context symbol for the state.
        """

THE_TYPE_MAP: dict[str, str]

class SetChannelsUndo:
    binding_path: str
    prev_channels: hou.Geometry | None
    channels: hou.Geometry | None
    layer: str
    def __init__(self, state: _ChannelsUndoState, binding_path: str, prev_channels: hou.Geometry | None = None, channels: hou.Geometry | None = None, layer: str | None = None) -> None: ...
    @property
    def state(self) -> _ChannelsUndoState | None: ...
    def cachePostChannels(self) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class SetChannelsUndoBuilder:
    binding_path: str
    layer: str | None
    label: str
    channels_undo: SetChannelsUndo
    undos: list[_UndoAction]
    def __init__(self, state: _ChannelsUndoState, binding_path: str, layer: str | None = None, label: str | None = None) -> None: ...
    @property
    def state(self) -> _ChannelsUndoState | None: ...
    def __del__(self) -> None: ...
    def append(self, undo: _UndoAction) -> None: ...

@contextmanager
def setChannelsUndo(state: _ChannelsUndoState, binding_path: str, layer: str | None = None, label: str | None = None) -> Generator[SetChannelsUndoBuilder]: ...

class SetNonAnimatableParmsUndo:
    rig_path: str
    prev_parms: apex.Dict
    next_parms: apex.Dict
    def __init__(self, state: _NonAnimatableParmsUndoState, rig_path: str, prev_parms: apex.Dict, next_parms: apex.Dict) -> None: ...
    @property
    def state(self) -> _NonAnimatableParmsUndoState | None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

def tupleSetUnion(a: Iterable[_T], b: Collection[_T]) -> tuple[_T, ...]: ...
def tupleSetIntersection(a: Collection[_T], b: Collection[_T]) -> tuple[_T, ...]: ...
def tupleSetSubtract(a: Iterable[_T], b: Container[_T]) -> tuple[_T, ...]: ...
def tupleSetDifference(a: Collection[_T], b: Collection[_T]) -> tuple[_T, ...]: ...
@typing.overload
def tupleSetModify(a: Collection[_T], b: tuple[_T, ...], pick_mod: hou.EnumValue[hou.pickModifier]) -> tuple[_T, ...]: ...
@typing.overload
def tupleSetModify(a: Collection[_T], b: Collection[_T], pick_mod: hou.EnumValue[hou.pickModifier]) -> Collection[_T]: ...

parm_format: str

def getParmTypeFromApexType(apex_type_name: str) -> str: ...
def dsScriptFromGraphSignature(groupname: str, signature: _apex.Signature) -> str: ...
def addGraphParmsToOpNode(opnode: hou.OpNode, groupname: str, signature: _apex.Signature) -> None: ...
def dumpApexDict(d: apex.Dict, indent: int = 0) -> None: ...
def getRigOutputData(rig_path: str, output_name: str | None = None) -> tuple[str, str]:
    """
    get the output path and the output key in order to query from an APEX Animation Scene a given rig output 
    based on a rigpath and a name of a rig output element
    """
def getRigOutput(scene: apex.Scene, output_path: str, output_key: str) -> _apex._Value | None:
    """return a given rig output calculates by the APEX Animation Scene"""
def toggleControlAction(state: _AnimateState, ctrl_path: str | None = None) -> bool | None:
    """toggles the state of a given boolparm of a control, this action is currently tight to a single control
    and defaults to the currently selected one if no path is given
    """
def pinControlAction(state: _AnimateState) -> None: ...
def spaceSwitchControlAction(state: _AnimateState, setkeys: bool = False) -> None:
    """executes an update of the xform position of a given set of controls to a new position based on a parameter change
    that redifines that xform spaces of the given set of controls. 
    

    :param state: _description_
    """
def getAnimStack(scene: apex.Scene | None, rig_path: str) -> apex.Dict:
    """
    Returns a dictionary containing the 4 keys necessary to build
    an anim stack with the ch::AnimStackBuild callback
    Parms:
    scene-> apex.Scene    
    """
def enableToolSpecificActions(kwargs: ViewerStateMenuPreOpenKwargs, actions: Iterable[str]) -> None:
    """
    Call this onMenuPreOpen
    kwargs should be the kwargs from onMenuPreOpen
    actions should be a list like
    LOCATOR_ACTIONS as defined at the top of this file    
    """
