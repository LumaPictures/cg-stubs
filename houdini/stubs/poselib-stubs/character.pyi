import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import hou
from . import chopdata as chopdata, plglobals as plglobals, pose as pose
from hutil.PySide import QtCore, QtWidgets
from poselib.pose import PoseData as PoseData

class PoseCapture:
    """Provides interface for capturing poses."""
    def capturePose(self, node: hou.OpNode, frame: float, all_parms: bool = False) -> PoseData: ...
    def captureClip(self, node: hou.OpNode, start: float, end: float, sample_rate: float, bake_clip: bool, use_bclip: bool = True, use_blosc_compression: bool = True) -> PoseData | None: ...
    def _capture(self, node: hou.OpNode, start: float, end: float, bake_clip: bool = True, sample_rate: float = 1, all_parms: bool = False) -> PoseData:
        """Captures clip of node in provided range of frames.

        @param node: hou.Node instance to which pose is being applied.
        @param start: Frame number of start of clip.
        @param end: Frame number of end of clip.
        @param bake_clip: True if baking clip.
        @param sample_rate: Determines sample rate for baking clip.
        @param capAllParams: True if all parameters are to be captured.
        """

class PoseApply:
    """Provides interface for applying and blending poses."""
    blendDict: dict[str, int | float | str]
    def __init__(self) -> None: ...
    def applyPose(self, node: hou.OpNode, pose: PoseData) -> None: ...
    def applyClip(self, node: hou.OpNode, clip: PoseData, chop: bool = False, root: str | None = None) -> None: ...
    def captureBlend(self, node: hou.OpNode) -> None: ...
    def blendPose(self, node: hou.OpNode, clip: PoseData, amount: float) -> None: ...

class _NodeTextField(QtWidgets.QLineEdit):
    """Text field for storing the node path."""
    def dropEvent(self, event: PySide6.QtGui.QDropEvent) -> None:
        """Handle data dropped on the field."""

class NodeChooserWidget(QtWidgets.QWidget):
    """Widget for choosing a node."""
    clearHistoryAction: PySide6.QtGui.QAction
    nodeChanged: QtCore.Signal
    MAX_RECENTS: int
    def __init__(self, parent: PySide6.QtWidgets.QWidget) -> None: ...
    def cleanup(self) -> None: ...
    def reset(self) -> None: ...
    def ensureNodeSelected(self) -> hou.OpNode | None:
        """Checks if a valid node is present and prompts the user to
           select one if needed.
           
        Return selected node if any, and None otherwise.
        """
    def selectedNode(self) -> hou.OpNode | None: ...
    def setNode(self, path: str) -> bool:
        """Sets the current node to that at the given path.
        
        Return the True if node was successfully selected and False otherwise.
        """
    def eventFilter(self, widget: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool: ...
