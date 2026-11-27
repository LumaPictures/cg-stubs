import hou
from PySide6 import QtCore as QtCore, QtGui as QtGui
from apex.ui.animationlayers.panel import AnimationLayersPanel as AnimationLayersPanel
from hutil.PySide import QtWidgets

class SceneAnimateParmsPanel(QtWidgets.QWidget):
    """
    Parameters panel for the APEX Scene Animate node including embedded
    Animation Layers.
    """
    def __init__(self, parent: QtWidgets.QWidget | None = None, node_type: str = 'apex::sceneanimate', show_parm_editor: bool = False, splitter_orientation: QtCore.Qt.Orientation = ...) -> None: ...
    def setupUI(self) -> None:
        """Set up the panel interface."""
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """Consume key events that would otherwise propagate to other
        Houdini panes."""
    def animLayersPane(self) -> AnimationLayersPanel: ...
    def activate(self, pane: hou.PathBasedPaneTab | None) -> None:
        """Called when the panel is activated."""
    def deactivate(self, pane: hou.PathBasedPaneTab | None) -> None:
        """Called when the panel is deactivated."""
    def nodePathChanged(self, node: hou.OpNode | None) -> None: ...
    def cleanup(self) -> None:
        """Clean up resources."""
