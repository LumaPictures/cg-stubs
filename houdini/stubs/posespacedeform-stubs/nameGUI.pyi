from .ui.uiActions import *
from .ui.uiLineEdit import *
from .ui.uiNavigation import *
from .Builder import *
from .defaults import *
from PySide6 import QtGui as QtGui
from collections.abc import Callable as Callable
from hutil.Qt import QtCore, QtWidgets
from posespacedeform.ui.uiLineEdit import UiLineEdit as UiLineEdit

class NameGUI(QtWidgets.QMainWindow):
    current_name: str
    callback: Callable[[str | None], object]
    nameselect: UiLineEdit
    cancelpsd: QtWidgets.QPushButton
    openpsd: QtWidgets.QPushButton
    def __init__(self, parent: QtWidgets.QWidget | None, current_name: str, title: str, pos: QtCore.QPoint, callback: Callable[[str | None], object]) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
