import hou
from PySide6 import QtCore, QtGui, QtWidgets

from apex.ui.animationlayers.panel import AnimationLayersPanel

class SceneAnimateParmsPanel(QtWidgets.QWidget):
    def __init__(
        self,
        parent: QtWidgets.QWidget | None = ...,
        node_type: str = ...,
        show_parm_editor: bool = ...,
        splitter_orientation: QtCore.Qt.Orientation = ...,
    ) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def animLayersPane(self) -> AnimationLayersPanel: ...
    # The python panel's kwargs.get("paneTab"): the PythonPanel, or the ParameterEditor it is
    # shown in.
    def activate(self, pane: hou.PathBasedPaneTab | None) -> None: ...
    def deactivate(self, pane: hou.PathBasedPaneTab | None) -> None: ...
    def nodePathChanged(self, node: hou.OpNode | None) -> None: ...
