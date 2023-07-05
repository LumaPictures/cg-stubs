# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
from typing import ClassVar

class InteractiveIconTabBar(PyQt5.QtWidgets.QTabBar):
    BIG_ICON_SIZE: ClassVar[int] = ...
    tabIconClicked: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    tabIconEnterEvent: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    tabIconLeaveEvent: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent): ...
    def getIconIndex(self, pos): ...
    def getIconRect(self, index): ...
    def getMouseOverIndex(self): ...
    def mouseMoveEvent(self, ev): ...
    def mousePressEvent(self, ev): ...