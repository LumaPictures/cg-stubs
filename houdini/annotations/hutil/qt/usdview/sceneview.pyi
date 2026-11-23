import hou
from PySide6 import QtGui, QtWidgets

from hutil.qt.common import config, qmlviews

from .primtreemodel import PrimTreeModel

DEBUG_QML: bool

class SceneConfig(config.BaseConfig):
    rowHeight: float
    treeIndentation: float

class SceneState(qmlviews.SharedState[SceneConfig]):
    outputIndex: int
    treeModel: PrimTreeModel

class SceneViewWidget(qmlviews.BaseQmlWidget[SceneState]):
    SOURCE_URL: str
    def setLopNode(self, node: hou.LopNode, output_index: int = ...) -> None: ...

class TestWindow(QtWidgets.QDialog):
    def __init__(self, *, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None: ...
    def setLopNode(self, node: hou.LopNode, output_index: int = ...) -> None: ...
