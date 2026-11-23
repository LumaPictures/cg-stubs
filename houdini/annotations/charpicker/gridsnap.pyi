from PySide6 import QtCore, QtGui, QtWidgets

from charpicker.tabview import TabView


class GridSnap(QtWidgets.QWidget):
    parent: TabView
    cursor: QtGui.QCursor
    snapDistance: int
    cellSize: int
    cellScaledSize: float
    topLeft: QtCore.QPoint | None
    topRight: QtCore.QPoint | None
    bottomLeft: QtCore.QPoint | None
    bottomRight: QtCore.QPoint | None
    distTopLeft: QtCore.QPoint | None
    distTopRight: QtCore.QPoint | None
    distBotLeft: QtCore.QPoint | None
    distBotRight: QtCore.QPoint | None
    grayPointStyleSheet: str
    cyanPointStyleSheet: str
    rowRange: list[int]
    colRange: list[int]
    topLeftPoint: QtWidgets.QLabel
    topRightPoint: QtWidgets.QLabel
    bottomLeftPoint: QtWidgets.QLabel
    bottomRightPoint: QtWidgets.QLabel

    def __init__(self, parent: TabView, size: QtCore.QSize, cell_size: int) -> None: ...
    def setShowGrid(self, show: bool) -> None: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...
    def setCellSize(self, new_cell_size: int) -> None: ...
    def setGridSize(self, size: QtCore.QSize) -> None: ...
    def scaleGrid(self, size: QtCore.QSize) -> None: ...
    def setSnapDistance(self, distance: int) -> None: ...
    def snapEvent(self, button: QtWidgets.QWidget) -> None: ...
    def updateSnapPoints(self) -> bool: ...
    def applySnapToButton(self, button: QtWidgets.QWidget) -> bool: ...
    def hidePoints(self) -> None: ...
    def cleanUpUponClose(self) -> None: ...
