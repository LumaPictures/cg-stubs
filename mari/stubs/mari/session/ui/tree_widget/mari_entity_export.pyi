from .mari_entity import MariEntityTreeWidget as MariEntityTreeWidget
from _typeshed import Incomplete

class MariEntityExportTreeWidget(MariEntityTreeWidget):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def checkCurrent(self) -> None: ...
    def checkAll(self) -> None: ...
    def checkNone(self) -> None: ...
    def populateView(self) -> None: ...
