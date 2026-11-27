import hou
from _apexscene import Scene as Scene
from apex.characterpicker.commands import ControlsFilter as ControlsFilter, ProjectionDirection as ProjectionDirection
from collections.abc import Iterable

def projectRigControls(scene: Scene, rig_path: str, controls_filter: ControlsFilter, selected_paths: Iterable[str] | None = None, projection_direction: ProjectionDirection = ..., viewport: hou.GeometryViewport | None = None) -> list[tuple[str, float, float]]:
    """Project transform-control world positions to 2D coordinates.

    Returns a list of (ctrl_path, x, y) tuples in projected space.
    """
def projectControls(scene: Scene, ctrl_paths: Iterable[str], projection_direction: ProjectionDirection = ..., viewport: hou.GeometryViewport | None = None) -> list[tuple[str, float, float]]:
    """Project the given controls' world positions to 2D coordinates.

    Returns a list of (ctrl_path, x, y) tuples in projected space.
    """
