# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtGui
import PySide6.QtWidgets
from hutil.Qt import QtWidgets

class PathListView(QtWidgets.QListView):
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None: ...
    def selectedPrims(self) -> list[str]: ...
