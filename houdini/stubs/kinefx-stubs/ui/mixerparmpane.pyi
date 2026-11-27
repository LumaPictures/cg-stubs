from kinefx.ui.mixerutils import *
import hou
from collections.abc import Sequence
from hutil.PySide import QtCore, QtWidgets

class ParmPane(QtWidgets.QWidget):
    myPane: hou.PythonPanel
    myParmEditor: hou.qt.ParmDialog
    myPrefSize: QtCore.QSize
    myMixerNodes: Sequence[hou.OpNode | None]
    def __init__(self, pane: hou.PythonPanel) -> None: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def setMixerNodes(self, nodes: Sequence[hou.OpNode | None]) -> None: ...
    def setShowHeader(self, v: int) -> None: ...
