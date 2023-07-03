import PySide2.QtWidgets as QtWidgets
from . import megascans as megascans
from _typeshed import Incomplete

class TextureSetsTabWidget(QtWidgets.QTabWidget):
    tabList: Incomplete
    MegascanWidget: Incomplete
    def __init__(self) -> None: ...
    def repoRootChanged(self) -> None: ...

def makePalette() -> None: ...
