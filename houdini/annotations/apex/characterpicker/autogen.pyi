from collections.abc import Iterable

import hou
from _apexscene import Scene
from apex.characterpicker.commands import ControlsFilter, ProjectionDirection

def projectRigControls(
    scene: Scene,
    rig_path: str,
    controls_filter: ControlsFilter,
    selected_paths: Iterable[str] | None = ...,
    projection_direction: ProjectionDirection = ...,
    viewport: hou.GeometryViewport | None = ...,
) -> list[tuple[str, float, float]]: ...
def projectControls(
    scene: Scene,
    ctrl_paths: Iterable[str],
    projection_direction: ProjectionDirection = ...,
    viewport: hou.GeometryViewport | None = ...,
) -> list[tuple[str, float, float]]: ...
