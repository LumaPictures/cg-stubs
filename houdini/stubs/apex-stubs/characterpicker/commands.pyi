import enum
import hou
from collections.abc import Iterable

class Commands:
    RETRIEVE_PICKER_LAYOUT: str
    SAVE_PICKER_LAYOUT: str
    PROJECT_RIG_CONTROLS: str
    PROJECT_CONTROLS: str

class ControlsFilter(enum.Enum):
    ALL = 'all'
    SELECTED = 'selected'

class ProjectionDirection(enum.Enum):
    FRONT = 'front'
    BACK = 'back'
    LEFT = 'left'
    RIGHT = 'right'
    TOP = 'top'
    VIEWPORT = 'viewport'

def sendProjectRigControls(scene_viewer: hou.SceneViewer, rig_path: str, controls_filter: ControlsFilter, projection_direction: ProjectionDirection | None = None) -> list[tuple[str, float, float]] | None:
    """Ask the state to project the rig's transform-control positions to 2D.

    Returns a list of (ctrl_path, x, y) tuples in projected space (empty if no
    placeable controls), or None if the state did not handle the command. The
    caller is responsible for fitting the cluster to a canvas.
    """
def sendProjectControls(scene_viewer: hou.SceneViewer, ctrl_paths: Iterable[str], projection_direction: ProjectionDirection | None = None) -> list[tuple[str, float, float]] | None:
    """Project the given controls' positions to 2D.

    Returns a list of (ctrl_path, x, y) tuples in projected space, or None if
    the state did not handle the command.
    """
