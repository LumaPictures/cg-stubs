import hou
from collections.abc import Sequence
from hutil.PySide import QtCore, QtGui, QtWidgets
from typing import Any

class UiConst:
    class __UiConst:
        SIZE2: int
        SIZE4: int
        SIZE5: int
        SIZE6: int
        SIZE8: int
        SIZE9: int
        SIZE10: int
        SIZE16: int
        SIZE20: int
        SIZE22: int
        SIZE26: int
        SIZE28: int
        SIZE30: int
        SIZE32: int
        MARGIN0: QtCore.QMargins
        MARGIN2: QtCore.QMargins
        MARGIN4: QtCore.QMargins
        MARGIN6: QtCore.QMargins
        MARGIN8: QtCore.QMargins
        SMARGIN2: QtCore.QMargins
        SMARGIN4: QtCore.QMargins
        SMARGIN6: QtCore.QMargins
        SMARGIN8: QtCore.QMargins
        ICON_SIZE: QtCore.QSize
        MARGIN_W: int
        MARGIN_H: int
        HIGHL_W: int
        EDIT_H: int
        ITEM_W: int
        ITEM_H: int
        EDIT_W: int
        MARKER_W: int
        MARKER_H: int
        ITEM_SIZE: QtCore.QSize
        BRUSH_TOOLBAR_HEIGHT: int
        BRUSH_TOOLBAR_SPACING: int
        def __init__(self) -> None: ...
        def toolbarItemSize(self) -> QtCore.QSize: ...
        def toolbarIconSize(self) -> QtCore.QSize: ...
        def toolbarIcon(self) -> hou.qt.Icon: ...
        def makeTitleLabel(self, title: str) -> tuple[QtWidgets.QLabel, QtWidgets.QVBoxLayout]:
            """ Create a title label in a vertical layout.
            """
    instance: UiConst.__UiConst | None
    def __new__(cls) -> UiConst.__UiConst: ...
    def __getattr__(self, name: str) -> Any: ...

class PanelCommandWidget(QtWidgets.QWidget):
    def __init__(self, buttons: Sequence[QtWidgets.QWidget], title: str = '', parent: QtWidgets.QWidget | None = None) -> None: ...
    def setTitle(self, title: str) -> None: ...
    def setIcon(self, icon: QtGui.QIcon | None) -> None: ...
