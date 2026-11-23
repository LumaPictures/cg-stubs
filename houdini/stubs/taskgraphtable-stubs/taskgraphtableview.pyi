from PySide6 import QtGui as QtGui
from hutil.Qt import QtWidgets

MAX_COLUMN_WIDTH: int

class TaskGraphTableView(QtWidgets.QTableView):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """Close the work item info window if the middle mouse was released."""
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """Resize column to contents, if enabled."""
