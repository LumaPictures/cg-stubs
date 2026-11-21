from charpicker.tabview import TabView as TabView
from hutil.Qt import QtCore, QtGui, QtWidgets

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
    def setCellSize(self, new_cell_size: int) -> None:
        """ Sets square size of the grid cells. """
    def setGridSize(self, size: QtCore.QSize) -> None:
        """ Resizes grid based on given size.  """
    def scaleGrid(self, size: QtCore.QSize) -> None:
        """ Resizes grid and scales the grid cells, based on the number of
        rows and columns, and the given size.
        """
    def setSnapDistance(self, distance: int) -> None:
        """ Sets distance indicator between cursor and corner point for
        when snapping should occur.
        """
    def snapEvent(self, button: QtWidgets.QWidget) -> None:
        """ Snap center of button to a grid line intersection point and make
        the point a cyan color if distance between point and cursor is within
        snapping distance range. Similar to the Scene Viewer, if there are
        multiple buttons selected and a new button is not being added, all
        other selected buttons are shifted relative to the snapping button.
        """
    def updateSnapPoints(self) -> bool:
        """ Calculate snap points based on current cursor position.
        Call this once before applying snap to multiple buttons.
        Returns True if valid snap points were calculated.
        """
    def applySnapToButton(self, button: QtWidgets.QWidget) -> bool:
        """ Apply snap to a button using previously calculated snap points.
        Call updateSnapPoints() first before calling this method.
        """
    def hidePoints(self) -> None:
        """ Hides the snapping points. """
    def cleanUpUponClose(self) -> None:
        """Removes parent and signal-slot connections to allow for complete
        cleanup upon garbage collection.
        """
