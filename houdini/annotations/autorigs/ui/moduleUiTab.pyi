from typing import Protocol

from PySide6 import QtWidgets

class _LinkedWidget(Protocol):
    def unlinkParms(self) -> None: ...

class ModuleUiTab(QtWidgets.QWidget):
    linkedwidgets: list[_LinkedWidget]

    def __init__(self) -> None: ...
    def unlinkAllNodes(self) -> None: ...
