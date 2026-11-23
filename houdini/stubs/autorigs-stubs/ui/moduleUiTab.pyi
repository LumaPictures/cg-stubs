from hutil.Qt import QtWidgets
from typing import Protocol

class _LinkedWidget(Protocol):
    def unlinkParms(self) -> None: ...

class ModuleUiTab(QtWidgets.QWidget):
    linkedwidgets: list[_LinkedWidget]
    def __init__(self) -> None: ...
    def unlinkAllNodes(self) -> None: ...
