import hou
from gzip import GzipFile as GzipFile
from hutil.PySide import QAction as QAction, QActionGroup as QActionGroup, QtCore as QtCore, QtWidgets as QtWidgets
from hutil.PySide.QtCore import Qt as Qt
from hutil.qt.info import config as config, core as core, window as window
from hutil.qt.pluto import colors as colors
from hutil.qt.toolmodel import Group as Group, GroupTreeModel as GroupTreeModel, ToolListModel as ToolListModel
from operator import attrgetter as attrgetter
from typing import ClassVar

TOOLVIEW_SOURCE_URL: QtCore.QUrl

class SharedState(core.Info):
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

class TabConfig(config.BaseConfig):
    showHelp: bool
    showAllHelp: bool
    collapsed: bool
    showFavorites: bool
    showGroups: bool
    showRecent: bool

class TabWidget(window.BaseQmlWidget):
    finished: ClassVar[QtCore.Signal]
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def toolHelp(self, tool_name: str) -> None: ...
    def setEditor(self, editor: hou.PaneTab) -> None: ...

class TabMenu(QtWidgets.QMainWindow):
    def __init__(self, *, parent: QtWidgets.QWidget | None = None) -> None: ...
    def setEditor(self, editor: hou.PaneTab) -> None: ...

def showTabMenu(editor: hou.PaneTab) -> None: ...
