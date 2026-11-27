from collections.abc import Iterable

import hou

def sendProjectRigControls(
    scene_viewer: hou.SceneViewer,
    rig_path: str,
    controls_filter: ControlsFilter,
    projection_direction: ProjectionDirection | None = ...,
) -> list[tuple[str, float, float]] | None: ...
def sendProjectControls(
    scene_viewer: hou.SceneViewer, ctrl_paths: Iterable[str], projection_direction: ProjectionDirection | None = ...
) -> list[tuple[str, float, float]] | None: ...
