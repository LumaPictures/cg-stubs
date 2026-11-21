# Houdini stubs generated from Houdini 22.0.466

import hou
from . import model as model
from enum import IntEnum
from hutil.PySide import QtWidgets
from scenegraphdetails.model import DetailsItem as DetailsItem

ICON_SIZE: int

class Columns(IntEnum):
    JUMP_TO = 0
    ICON = 1
    NODE_PATH = 2
    VALUE = 3

class EditorNodesView(QtWidgets.QTableWidget):
    panetab: hou.PythonPanel | None
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def setPaneTab(self, panetab: hou.PythonPanel | None) -> None: ...
    def populateFromItem(self, item: DetailsItem | None) -> None: ...
