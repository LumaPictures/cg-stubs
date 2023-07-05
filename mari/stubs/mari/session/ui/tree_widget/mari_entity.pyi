from PySide2 import QtWidgets
from _typeshed import Incomplete

class MariEntityTreeWidget(QtWidgets.QTreeWidget):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    @property
    def project(self): ...
    def loadMSF(self, filePath) -> None: ...
    def loadSessionData(self) -> None: ...
    def onItemChanged(self, item, column) -> None: ...
    def onItemSelectionChanged(self) -> None: ...
    def populateView(self) -> None: ...
    def refreshView(self) -> None: ...