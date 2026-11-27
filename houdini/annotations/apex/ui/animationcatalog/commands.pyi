from collections.abc import Sequence
from typing import Literal

import hou

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

def sceneViewer() -> hou.SceneViewer | None: ...
def setDefaultSceneViewer(scene_viewer: hou.SceneViewer | None) -> None: ...
def addClip(
    name: str = ...,
    pose: bool = ...,
    folder: str | None = ...,
    thumbnail: bytes | None = ...,
    preview: bytes | None = ...,
    frame_range: Sequence[float] | None = ...,
    scene_viewer: hou.SceneViewer | None = ...,
) -> tuple[bool, str | None]: ...
# The state's handler passes `parent` to AnimationCatalog.addFolder as the folder's name.
def addFolder(parent: str | None = ..., scene_viewer: hou.SceneViewer | None = ...) -> tuple[bool, str | None]: ...
def duplicateClip(item_id: str, scene_viewer: hou.SceneViewer | None = ...) -> tuple[bool, str | None]: ...
# SideFX annotates these three `-> bool`, but they return nothing.
def selectClipControls(item_id: str, scene_viewer: hou.SceneViewer | None = ...) -> None: ...
def applyClip(
    item_id: str,
    new_layer: bool = ...,
    clip_range: Sequence[float] | None = ...,
    # "replace", "insert" or "blend"; the state falls back to replace for any other.
    mode: str = ...,
    scene_viewer: hou.SceneViewer | None = ...,
) -> None: ...
def blendPose(
    item_id: str,
    percent: float,
    blend_state: Literal["started", "updated", "finished"],
    new_layer: bool = ...,
    scene_viewer: hou.SceneViewer | None = ...,
) -> None: ...
# PNG data.
def captureScreenshot(scene_viewer: hou.SceneViewer | None = ...) -> bytes | None: ...
# GIF data.
def captureVideo(frame_start: int, frame_end: int, scene_viewer: hou.SceneViewer | None = ...) -> bytes | None: ...
