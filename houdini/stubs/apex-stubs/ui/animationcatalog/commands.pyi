import hou
from collections.abc import Sequence
from typing import Literal

class Commands:
    ADD_CLIP: str
    ADD_FOLDER: str
    DUPLICATE_CLIP: str
    SELECT_CLIP_CONTROLS: str
    APPLY_CLIP: str
    BLEND_POSE: str
    CAPTURE_SCREENSHOT: str
    CAPTURE_VIDEO: str

default_scene_viewer: hou.SceneViewer | None

def sceneViewer() -> hou.SceneViewer | None:
    """
    Find and return a scene viewer
    """
def setDefaultSceneViewer(scene_viewer: hou.SceneViewer | None) -> None: ...
def addClip(name: str = 'New Clip', pose: bool = True, folder: str | None = None, thumbnail: bytes | None = None, preview: bytes | None = None, frame_range: Sequence[float] | None = None, scene_viewer: hou.SceneViewer | None = None) -> tuple[bool, str | None]:
    """
    Creates a new clip by sending a ADD_CLIP command to the state.
    If no folder is specified, the first selected folder in the panel will be
    used. If no panels are active, or no folders are selected, the item
    will be created in the root.
    Returns:
    - success: True if the clip was successfully created, False otherwise
    - clip_id: Unique id of the newly created clip
    """
def addFolder(parent: str | None = None, scene_viewer: hou.SceneViewer | None = None) -> tuple[bool, str | None]:
    """
    Creates a new folder by sending a ADD_FOLDER command to the state.
    If no parent is specified, the first selected folder in the panel will be
    used. If no panels are active, or no folders are selected, the folder
    will be created in the root.
    Returns:
    - success: True if the folder was successfully created, False otherwise
    - folder_id: Unique id of the newly created folder
    """
def duplicateClip(item_id: str, scene_viewer: hou.SceneViewer | None = None) -> tuple[bool, str | None]: ...
def selectClipControls(item_id: str, scene_viewer: hou.SceneViewer | None = None) -> None:
    """
    Select the controls in the given clip by sending a SELECT_CLIP_CONTROLS
    command to the state.
    """
def applyClip(item_id: str, new_layer: bool = False, clip_range: Sequence[float] | None = None, mode: str = 'replace', scene_viewer: hou.SceneViewer | None = None) -> None:
    '''
    Select the controls in the given clip by sending a SELECT_CLIP_CONTROLS
    command to the state.
    :param item_id: Asset Gallery Data Source Item Id to blend. Must be a pose
                    type, and not an animation.
    :param new_layer: Whether or not to create a new layer for this blend. The
                      layer will ONLY be created when blend_state="started".
    :param clip_range: Range of the source clip to apply. If None, the full clip
                       is used.
    :param mode: How to merge the clip in to the scene.
                 Must be one of ("replace"|"insert")
    :param scene_viewer: The scene viewer to send the command to. If None, picks
                         the first visibile viewer.
    '''
def blendPose(item_id: str, percent: float, blend_state: Literal['started', 'updated', 'finished'], new_layer: bool = False, scene_viewer: hou.SceneViewer | None = None) -> None:
    '''
    Blend a pose from the animation catalog with the current pose.
    :param item_id: Asset Gallery Data Source Item Id to blend. Must be a pose
                    type, and not an animation.
    :param percent: Percent [0.0, 1.0] to blend the clip pose with the existing
                    pose, where 0.0 is fully weighted to the current pose, and
                    1.0 to the clip pose.
    :param blend_state: One of "started", "updated", "finished".
    :param new_layer: Whether or not to create a new layer for this blend. The
                      layer will ONLY be created when blend_state="started".
    :param scene_viewer: The scene viewer to send the command to. If None, picks
                         the first visibile viewer.
    '''
def captureScreenshot(scene_viewer: hou.SceneViewer | None = None) -> bytes | None:
    """
    Capture a screenshot of the viewport state, returning the raw png data
    """
def captureVideo(frame_start: int, frame_end: int, scene_viewer: hou.SceneViewer | None = None) -> bytes | None:
    """
    Capture an animated video of the viewport in .gif format, returning the raw
    data
    """
