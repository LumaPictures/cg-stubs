import hou
from apex.ui.animationlayers.membership import AnimationLayerMembershipModel as AnimationLayerMembershipModel
from apex.ui.animationlayers.model import AnimationLayersModelHandle as AnimationLayersModelHandle, _WeightChangeType
from collections.abc import Mapping, Sequence
from typing import Never, TypedDict

class _RenameLayerResult(TypedDict):
    new_name: str
    success: bool

class Commands:
    CREATE_LAYER: str
    DUPLICATE_LAYERS: str
    DELETE_LAYERS: str
    MOVE_LAYERS: str
    FORK_INHERITED_LAYERS: str
    SET_ACTIVE_LAYER: str
    SET_LAYER_WEIGHT: str
    LOCK_LAYERS: str
    MUTE_LAYERS: str
    SOLO_LAYERS: str
    SET_LAYERS_ADDITIVE: str
    SET_LAYERS_COLOR: str
    INSERT_LAYER_WEIGHT_KEYFRAME: str
    DESTROY_LAYER_WEIGHT_KEYFRAME: str
    SET_LAYER_WEIGHT_FROM_PLAYBAR: str
    DELETE_LAYER_WEIGHT_CHANNELS: str
    RESET_WEIGHTS: str
    SCOPE_LAYER_WEIGHT: str
    ADD_SELECTED_CONTROLS_TO_LAYERS: str
    REMOVE_SELECTED_CONTROLS_FROM_LAYERS: str
    SELECT_LAYER_CONTROLS: str
    RENAME_LAYER: str
    BAKE_LAYERS: str
    RETRIEVE_ANIMLAYERS_MODEL: str
    RETRIEVE_LAYER_MEMBERSHIP_MODEL: str
    GET_LAYER_CONTROLS: str
    GET_LAYER_PARMS: str
    REMOVE_PARMS_FROM_LAYER: str
    ADD_PARMS_TO_LAYER: str
    SET_ACTIVE_CLIP: str

def sceneViewer() -> hou.SceneViewer | None:
    """
    Find and return a scene viewer
    """
def createEmptyLayer(name: str, parent_layer: str | None = None, additive: bool = False, activate: bool = True, index: int = -1, color: hou.Color | None = None, scene_viewer: hou.SceneViewer | None = None) -> tuple[bool, str]:
    """
    Creates an Empty Layer utilizing the CREATE_LAYER command.
    Returns:
    - success: True if the layer was successfully created, False otherwise
    - name: New name if the state changed the input name (due to being an
            invalid format or a duplicate)
    """
def duplicateLayers(layers: Sequence[str], selected_controls_only: bool = False, activate: bool = True, scene_viewer: hou.SceneViewer | None = None) -> tuple[bool, list[str]]:
    """
    Duplicates layers, inserting each duplicated layer above the layer which was
    copied.
    If selected_controls_only is set to True, only the currently selected
    controls will be copied into the new layer.
    If activate is true, and the original layer is active, will activate the
    duplicate layer.
    Returns:
    - success: True if the layer was successfully created, False otherwise
    - names: Names of the new layers, in the same order as the original layers.
             Will be the copied layer's name with '_copy' appended.
    """
def deleteLayers(layers: Sequence[str], scene_viewer: hou.SceneViewer | None = None) -> bool: ...
def moveLayers(source_parent: str, source_indices: Sequence[int], destination_parent: str, destination_index: int, scene_viewer: hou.SceneViewer | None = None) -> bool:
    """
    Send a command to the state to move the given layers to the destination.
    source_layers must be a dictionary mapping parent layers to a SORTED list of
    child indices to move. The destination parent may or may not be the same
    as any of the source parents. The BaseAnimation layer cannot be moved.
    Returns True if successful, False otherwise
    """
def forkInheritedLayers(layers: Sequence[str], scene_viewer: hou.SceneViewer | None = None) -> None: ...
def setActiveLayer(layer: str, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to set the active layer
    """
def addSelectedControlsToLayers(layers: Sequence[str], scene_viewer: hou.SceneViewer | None = None) -> None: ...
def removeSelectedControlsFromLayer(layers: Sequence[str], scene_viewer: hou.SceneViewer | None = None) -> None: ...
def selectLayerControls(layer: str, scene_viewer: hou.SceneViewer | None = None) -> None: ...
def setLayerWeight(layers: Sequence[str], weight: float, change_type: _WeightChangeType, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to set weight of a layer
    """
def renameLayer(previous_name: str, new_name: str, scene_viewer: hou.SceneViewer | None = None) -> _RenameLayerResult:
    """
    Send a command to the state to rename a layer.
    Returns True if the layer was successfully renamed, False otherwise.
    """
def retrieveModel(scene_viewer: hou.SceneViewer | None = None) -> AnimationLayersModelHandle | None:
    """
    Send a state command to the state 'retrieveAnimLayersModel'.
    """
def retrieveMembershipModel(scene_viewer: hou.SceneViewer | None = None) -> AnimationLayerMembershipModel | None:
    """
    Send a state command to the state 'retrieveLayerMembershipModel'.
    """
def lockLayers(layers: Sequence[str], lock: bool, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to mute or unmute a layer.
    """
def muteLayers(layers: Sequence[str], mute: bool, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to mute or unmute a layer.
    """
def soloLayers(layers: Sequence[str], solo: bool, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to solo or unsolo a layer.
    """
def setLayersAdditive(layers: Sequence[str], additive: bool, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to set a layer type as additive or override.
    """
def setLayersColor(layer: Sequence[str], color: hou.Color, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to set a layer's color.
    """
def insertLayerWeightKeyframe(layers: Sequence[str], frame: float | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to key the layer weight channel.
    """
def destroyLayerWeightKeyframe(layers: Sequence[str], frame: float | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to remove a key from the layer weight channel.
    """
def resetWeights(layers: Sequence[str], scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to reset the layer weights to their default
    values at the current frame
    """
def addWeightToChannelList(layers: Sequence[str], scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to scope the layer's weight channel.
    """
def setWeightFromPlaybarSelection(layers: Sequence[str], scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to set the layer weights from the playbar.
    """
def deleteWeightChannels(layers: Sequence[str], scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to delete layer weight channels.
    """
def bakeLayers(replace: bool = True, start_layer: str | None = None, end_layer: str | None = None, keys_only: bool = True, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to bake all animation layers.
    """
def getLayerControls(layer: str, scene_viewer: hou.SceneViewer | None = None) -> dict[str, list[str]] | list[Never]:
    """
    Send a command to the state to retrieve the controls associated with the
    given layer.
    """
def getLayerParms(layer: str, scene_viewer: hou.SceneViewer | None = None) -> dict[str, list[str]]:
    """
    Send a command to the state to retrieve the parms associated with the
    given layer, organized by rig path
    """
def removeParmsFromLayer(layer: str, parms: Mapping[str, Sequence[str]], scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to remove parms from a layer, where the parms
    are of the format { rig_path: [list, of, parms] }
    """
def addParmsToLayer(layer: str, parms: Mapping[str, Sequence[str]], scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to remove parms from a layer, where the parms
    are of the format { rig_path: [list, of, parms] }
    """
def setActiveClip(clip: str, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Send a command to the state to switch the active animation clip.
    """
