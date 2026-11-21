from typing import ClassVar

from PySide6 import QtWidgets

from scenegraphdetails.arrayattribview import ArrayAttributeView
from scenegraphdetails.model import DetailsItem
from scenegraphdetails.panel import SceneGraphDetailsPanel
from scenegraphlayers.panel import SceneGraphLayersPanel

SUBPANEL_MINIMUM_HEIGHT: int

class ValueView(QtWidgets.QStackedWidget):
    theInitialTextLimit: ClassVar[int]
    panel: SceneGraphDetailsPanel | SceneGraphLayersPanel
    novalueview: QtWidgets.QWidget
    arrayattribview: ArrayAttributeView
    textvalueview: QtWidgets.QLabel
    textvalueviewscrollarea: QtWidgets.QScrollArea
    textlimit: int
    fulltext: str | None
    def __init__(self, panel: SceneGraphDetailsPanel | SceneGraphLayersPanel) -> None: ...
    def setText_(self, text: str | None) -> None: ...
    def setLimitedText_(self) -> None: ...
    def populateFromItem(self, item: DetailsItem | None, frame: float | None = ...) -> None: ...
