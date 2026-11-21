# Houdini stubs generated from Houdini 22.0.466

import hou
from . import model as model, view as view
from hutil.Qt import QtGui, QtWidgets

theRetargetWindow: RetargetWindow | None
MARGIN: int
OP_PREPEND: str
OP_FIND_REPLACE: str

class RetargetWindow(QtWidgets.QDialog):
    delete_button: QtWidgets.QPushButton
    def __init__(self, parent: QtWidgets.QWidget | None = None, node: hou.LopNode | None = None) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def setNode(self, node: hou.LopNode) -> None: ...
    def display(self) -> None: ...

def show(node: hou.LopNode) -> RetargetWindow:
    """
        Shows the (shared) Retarget Transforms dialog for the given node,
        creating it on first use.
    """
