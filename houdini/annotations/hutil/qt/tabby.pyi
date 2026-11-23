from typing import ClassVar

import hou
from PySide6 import QtCore, QtWidgets

from hutil.qt.toolmodel import Group, GroupTreeModel, ToolListModel

TOOLVIEW_SOURCE_URL: QtCore.QUrl

class SharedState:
    zoom: float
    toolTipDelay: int
    toolModel: ToolListModel
    groupModel: GroupTreeModel
    groups: list[Group]
    groupFilter: str
    nodeTypeCategory: str
    inWindow: bool
    gearMenuRequested: ClassVar[QtCore.Signal]
    windowCloseRequested: ClassVar[QtCore.Signal]
    startMove: ClassVar[QtCore.Signal]
    toolActivated: ClassVar[QtCore.Signal]
    favoriteStatusChanged: ClassVar[QtCore.Signal]

class TabConfig:
    showHelp: bool
    showAllHelp: bool
    collapsed: bool
    showFavorites: bool
    showGroups: bool
    showRecent: bool

class TabWidget:
    finished: ClassVar[QtCore.Signal]
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def toolHelp(self, tool_name: str) -> None: ...
    def setEditor(self, editor: hou.PaneTab) -> None: ...

class TabMenu:
    def __init__(self, *, parent: QtWidgets.QWidget | None = ...) -> None: ...
    def setEditor(self, editor: hou.PaneTab) -> None: ...

def showTabMenu(editor: hou.PaneTab) -> None: ...
