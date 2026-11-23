import hou
from PySide6 import QtWidgets

from scenegraphdetails.model import DetailsItem

ICON_SIZE: int

class EditorNodesView(QtWidgets.QTableWidget):
    panetab: hou.PythonPanel | None
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def setPaneTab(self, panetab: hou.PythonPanel | None) -> None: ...
    def populateFromItem(self, item: DetailsItem | None) -> None: ...
