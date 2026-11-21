import hou
from ..common.qmlviews import CT as CT
from .primtreemodel import PrimTreeModel as PrimTreeModel
from hutil.PySide import QAction as QAction, QActionGroup as QActionGroup, QtGui as QtGui, QtWidgets as QtWidgets
from hutil.PySide.QtCore import Qt as Qt
from hutil.qt.common import config as config, core as core, qmlviews as qmlviews

DEBUG_QML: bool

class SceneConfig(config.BaseConfig):
    rowHeight: float
    treeIndentation: float

class SceneState(qmlviews.SharedState[SceneConfig]):
    outputIndex: int
    treeModel: PrimTreeModel

class SceneViewWidget(qmlviews.BaseQmlWidget[SceneState]):
    SOURCE_URL: str
    def setLopNode(self, node: hou.LopNode, output_index: int = -1) -> None: ...

class TestWindow(QtWidgets.QDialog):
    def __init__(self, *, parent: QtWidgets.QWidget | None = None) -> None: ...
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None: ...
    def setLopNode(self, node: hou.LopNode, output_index: int = -1) -> None: ...
