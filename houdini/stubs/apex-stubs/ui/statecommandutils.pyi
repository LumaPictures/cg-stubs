import _apex
import apex
import hou
from apex.apexanimatemodules.base import _AnimateState as _BaseAnimateState
from collections.abc import Collection, Iterable, Mapping, Sequence
from typing import Any, Final, Protocol, TypedDict

class _AnimateState(_BaseAnimateState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`), as getAnimateState() gives it."""

class _SnapConfig(TypedDict, total=False):
    """An entry of the Animate state's snapSelectedControls() config. Entries without both
    patterns are skipped."""
    pattern_from: str
    pattern_to: str
    use_t: bool
    use_r: bool
    use_s: bool
    lookat: bool
    lookup: hou.Vector3
    lookaxis: hou.Vector3
    snap_to_selections: bool

class _ToolboxParmUpdate(TypedDict, total=False):
    """What updateToolbox() merges into a toolbox state parm's properties."""
    value: bool | int | float | str | list[int] | list[float]
    enable: bool | int
    visible: bool | int
    label: str

GET_STATE: Final[str]
GET_SCENE_DATA_CMD: Final[str]
FIND_SCENE_DATA_PATHS_CMD: Final[str]
REGISTER_SELECTION_CHANGED_CALLBACK: Final[str]
REMOVE_SELECTION_CHANGED_CALLBACK: Final[str]
SWITCH_HANDLE_TOOL_CMD: Final[str]
UPDATE_TOOLBOX_CMD: Final[str]
GET_CONTROL_COLORS: Final[str]
GET_CALLBACK_CONTROLS: Final[str]
GET_SCENE_NODE: Final[str]
CHANNELS_CHANGED: Final[str]
BUILD_PATH_REFS: Final[str]
RESOLVE_PATH_REFS: Final[str]
_animate_state_typenames: set[str]

def registerAnimateState(state_typename: str) -> None:
    """
    Registers the type name for the Animate state.
    """
def getSceneViewer() -> hou.SceneViewer | None:
    """ Try to find a scene viewer. """
def inAnimateState(scene_viewer: hou.SceneViewer | None = None) -> bool:
    """
    Whether the given scene viewer's current state is the Animate state.
    """
def sendCommand(command_name: str, args: Mapping[str, object], scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command 'command_name' with arguments 'args' to the active
    viewer state running in the given scene_viewer.

    If the scene_viewer is None, then it will try to find A scene viewer
    to run the command on.
    """
def getAnimateState(scene_viewer: hou.SceneViewer | None = None) -> _AnimateState | None:
    """Returns the animate state in the scene viewer.
    If the scene viewer does not have an active animate state, returns None.

    NB: The animate state should be stored in a weakref to avoid runaway memory
    consumption (if it's desirable to keep it persistent). If it goes out of
    scope, request a new animate state.
    """
def getControlsByRig() -> dict[str, list[str]]: ...
def getControlTransforms(ctrl_paths: Iterable[str], group_by_rig: bool = False) -> dict[str, hou.Matrix4]: ...
def getSceneData(path: str, scene_viewer: hou.SceneViewer | None = None) -> Any: ...
def setSceneData(path: str, data: object, scene_viewer: hou.SceneViewer | None = None) -> None: ...
def findSceneDataPaths(pattern: str, scene_viewer: hou.SceneViewer | None = None) -> list[str]: ...
def buildPathRefs(paths: Collection[str], scene_viewer: hou.SceneViewer | None = None) -> list[str]:
    """ Convert fully-qualified paths (control or rig) to their
        tool-prefixed ref form for persistence. Paths without an active
        tool mapping are returned unchanged.
    """
def resolvePathRefs(refs: Collection[str], scene_viewer: hou.SceneViewer | None = None) -> list[str]:
    """ Resolve a list of tool-prefixed path refs to their fully-qualified
        paths (control or rig). Refs without a recognized prefix are
        returned unchanged.
    """
def updateControls(trs: Mapping[str, Mapping[str, _apex._ValueArg]], controls: Iterable[str], update_channel_widget: bool = True) -> None: ...
def startTool(tool_module_name: str, on_activate_kwargs: Mapping[str, object]) -> None: ...
def switchToPreviousTool() -> None: ...
def exitCurrentTool() -> None: ...
def getSceneControlManager() -> apex.ControlManager: ...
def updateTransientConstraint(bookmark_id: int | None = None, store: bool = False) -> None: ...
def snapSelectedControls(snap_config: Iterable[_SnapConfig] = ...) -> None: ...
def setControlXforms(mapping: Mapping[str, hou.Matrix4] = ..., scope: bool = True) -> None: ...
def switchHandleTool(tool_name: str) -> None: ...
def setXformForControls(xform: hou.Matrix4, control_paths: Iterable[str] = ...) -> None: ...
def getPrimaryControl(scene_viewer: hou.SceneViewer | None = None) -> str | None: ...
def getControlColors(control_paths: Iterable[str]) -> dict[str, tuple[float, float, float] | None]:
    """
    Return the color of each control as a dict { control_path: color }
    """
def getCallbackControls(control_paths: Iterable[str]) -> set[str]:
    """
    Return the subset of input control paths that have a properties
    script callback registered.
    """
def channelList() -> hou.ChannelList: ...
def getGraphOutputData(path: str, scene_viewer: hou.SceneViewer | None = None) -> _apex._Value | None: ...
def getSceneNode(scene_viewer: hou.SceneViewer | None = None) -> hou.SopNode | hou.LopNode | None: ...
def channelsChanged(channels: Sequence[str], collection: str, write_animation: bool, anim_path: str, scene_viewer: hou.SceneViewer | None = None) -> None:
    '''
    Notify the State that channels have changed externally. 
    The State will grab the channels from the animation editor and write them into geometry.
    This command can update layers that aren\'t the active layer.

    @param channels: list of channel names.

    @param collection: name of the collection to update from.

    @param write_animation: whether the State should write the channels back into
        the animation geometry.

    @param anim_path: path into the APEX scene. This should be
        `f"{active_clip}/{layer}/{collection_name}"`
        or, for the base layer,
        `f"{active_clip}/{collection_name}"`.
    '''
def updateToolbox(scene_viewer: hou.SceneViewer | None, parms: Mapping[str, _ToolboxParmUpdate]) -> None:
    """
    Should be called by tools onHUDSettingEvent to update the toolbox
    with the updated parameters    
    """
