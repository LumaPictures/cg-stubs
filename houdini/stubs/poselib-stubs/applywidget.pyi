import PySide6.QtGui
import PySide6.QtWidgets
import hou
from . import character as character, plglobals as plglobals
from hutil.Qt import QtCore, QtWidgets
from poselib.pose import PoseData as PoseData

class ApplyWidget(QtWidgets.QWidget):
    """Widget containing apply pose controls."""
    nodeChanged: QtCore.Signal
    def __init__(self, parent: PySide6.QtWidgets.QWidget) -> None: ...
    def cleanup(self) -> None:
        """This is called when the pose library interface is about to be
           destroyed."""
    def reset(self) -> None:
        """Reset the apply widget to its default state."""
    def selectedNode(self) -> hou.OpNode | None: ...
    def setNode(self, path: str) -> None: ...
    def ensureNodeSelected(self) -> None: ...
    def applyPose(self, pose: PoseData) -> None:
        """Applies a pose to the selected node."""
    def startBlend(self, pose: PoseData) -> None:
        """Start a blend pose operation."""
    def blendPose(self, pose: PoseData, blend_value: float) -> None:
        """Blend the selected pose with the current state of the selected
           node."""
    def endBlend(self, pose: PoseData) -> None:
        """End a blend pose operation."""

class _ApplyOptionsDialog(QtWidgets.QDialog):
    """Modal dialog containing advanced options for applying clips and poses."""
    def __init__(self) -> None: ...
    def bringToFocus(self) -> None:
        """Opens dialog if not already open, then brings it into focus."""
    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:
        """Handle 'X' button clicked."""
