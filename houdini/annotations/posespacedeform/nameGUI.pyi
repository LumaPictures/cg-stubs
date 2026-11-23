from collections.abc import Callable

from PySide6 import QtCore, QtGui, QtWidgets

from posespacedeform.ui.uiLineEdit import UiLineEdit

class NameGUI(QtWidgets.QMainWindow):
    current_name: str
    callback: Callable[[str | None], object]
    nameselect: UiLineEdit
    cancelpsd: QtWidgets.QPushButton
    openpsd: QtWidgets.QPushButton
    def __init__(
        self,
        parent: QtWidgets.QWidget | None,
        current_name: str,
        title: str,
        pos: QtCore.QPoint,
        callback: Callable[[str | None], object],
    ) -> None: ...
    def closeEvent(self, event: QtGui.QCloseEvent) -> None: ...
