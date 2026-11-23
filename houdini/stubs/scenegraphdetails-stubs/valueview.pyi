from . import arrayattribview as arrayattribview, model as model
from hutil.Qt import QtWidgets
from scenegraphdetails.arrayattribview import ArrayAttributeView as ArrayAttributeView
from scenegraphdetails.model import DetailsItem as DetailsItem
from scenegraphdetails.panel import SceneGraphDetailsPanel as SceneGraphDetailsPanel
from scenegraphlayers.panel import SceneGraphLayersPanel
from typing import ClassVar

SUBPANEL_MINIMUM_HEIGHT: int

class ValueView(QtWidgets.QStackedWidget):
    panel: SceneGraphDetailsPanel | SceneGraphLayersPanel
    novalueview: QtWidgets.QWidget
    arrayattribview: ArrayAttributeView
    textvalueview: QtWidgets.QLabel
    textvalueviewscrollarea: QtWidgets.QScrollArea
    textlimit: int
    fulltext: str | None
    theInitialTextLimit: ClassVar[int]
    def __init__(self, panel: SceneGraphDetailsPanel | SceneGraphLayersPanel) -> None: ...
    def setText_(self, text: str | None) -> None: ...
    def setLimitedText_(self) -> None: ...
    def populateFromItem(self, item: DetailsItem | None, frame: float | None = None) -> None: ...
