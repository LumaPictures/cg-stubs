# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import QT4Widgets.WidgetUtils as WidgetUtils
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from typing import ClassVar, Set, Tuple

class HidingFrame(PyQt5.QtWidgets.QFrame):
    hideSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    showSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def hideEvent(self, e): ...
    def showEvent(self, e): ...

class PopupButton(ToolbarButton):
    aboutToShow: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, *args, **kwds) -> None: ...
    def _PopupButton__buildPopup(self): ...
    def _PopupButton__mousePressEvent(self, event): ...
    def _PopupButton__popupHidden(self): ...
    def _PopupButton__popupShow(self): ...
    def getPopup(self): ...
    def setDesiredHeight(self, h): ...
    def setDesiredWidth(self, w): ...
    def setHorizontallyResizable(self, horizontallyResizable): ...
