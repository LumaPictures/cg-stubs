from PySide6 import QtCore, QtGui, QtWidgets

from .bvhtree import BVHTree, BVHTreeNode
from .colormanager import ColorManager

class BVHViewer(QtWidgets.QGraphicsScene):
    rotation: list[float]
    translation: list[float]
    lastPos: QtCore.QPointF | None
    zoom: float
    bvhTree: BVHTree
    selectedNodes: list[BVHTreeNode]
    parentNodes: list[BVHTreeNode]
    siblingNodes: list[BVHTreeNode]
    loadButton: QtWidgets.QPushButton
    writeButton: QtWidgets.QPushButton
    resetButton: QtWidgets.QPushButton
    treeView: QtWidgets.QTreeView
    model: QtGui.QStandardItemModel
    colorManager: ColorManager
    parentCheckbox: QtWidgets.QCheckBox
    siblingCheckbox: QtWidgets.QCheckBox
    overlapCheckbox: QtWidgets.QCheckBox
    fileLabel: QtWidgets.QLabel
    controlWidget: QtWidgets.QWidget
    def __init__(self) -> None: ...
    def resetViewport(self) -> None: ...
    def selectionChanged(self, newSelection: QtCore.QItemSelection, oldSelection: QtCore.QItemSelection) -> None: ...
    def loadData(self) -> None: ...
    def writeData(self) -> None: ...
    def wheelEvent(self, event: QtWidgets.QGraphicsSceneWheelEvent) -> None: ...
    def mousePressEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None: ...
    def mouseMoveEvent(self, event: QtWidgets.QGraphicsSceneMouseEvent) -> None: ...
    def drawBackground(self, painter: QtGui.QPainter, rect: QtCore.QRectF) -> None: ...
