import hou
from .pick import pick_on_plane as pick_on_plane
from .tool_helpers import point_group_string as point_group_string
from curvestate.curve3.controller import Curve3Controller as Curve3Controller
from houtypes import ViewerStateEventKwargs

class Curve3Clipboard:
    """Manage state-local copied curve geometry and paste placement."""
    controller: Curve3Controller
    geo: hou.Geometry | None
    view_rotation: hou.Matrix3 | None
    paste_position: hou.Vector3 | None
    def __init__(self, controller: Curve3Controller) -> None:
        """Store the controller used for geometry access, verbs, and state commits."""
    def copy_selected_curves(self) -> bool:
        """Copy whole curves touched by the current point selection."""
    def paste(self, args: object) -> bool:
        """Paste copied curves at the last cached paste position and merge them into the node."""
    def update_paste_position(self, pos: hou.Vector3 | None, *, source: str) -> None:
        """Cache an explicit world position for later paste hotkeys."""
    def update_paste_position_from_event(self, kwargs: ViewerStateEventKwargs) -> None:
        """Cache the last editable plane position for later paste hotkeys."""
