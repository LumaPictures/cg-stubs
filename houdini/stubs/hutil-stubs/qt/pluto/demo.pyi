# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtGui
import PySide6.QtWidgets
from hutil.PySide import QAction as QAction, QtWidgets as QtWidgets
from hutil.PySide.QtCore import Qt as Qt
from hutil.qt.pluto import colors as colors, parts as parts, style as style, widgets as widgets

class DemoWindow(QtWidgets.QDialog):
    def __init__(self, gradient_bg: bool = False, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...

def openDemoWindow(scale: float = 1.0, holo: bool = False) -> None: ...
