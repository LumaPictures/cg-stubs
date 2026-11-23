from collections.abc import Callable
from typing import Any, ClassVar, Generic, TypeVar

import hou
from bookish.search import WhooshSearcher
from bookish.wiki.wikipages import WikiPages, _WikiBlock
from PySide6 import QtCore, QtGui, QtQml, QtQuick, QtQuickWidgets, QtWidgets

from . import core

SST = TypeVar("SST", bound="SharedState[Any]")

HFS_DIR: str
HFS_URL: QtCore.QUrl
NEW_UI: bool
DEBUG_QML: bool
QML_RESOURCE_PATH: str
USE_QML_RESOURCE: bool
BASE_URL: QtCore.QUrl
NODE_EVENTS: tuple[hou.EnumValue[hou.nodeEventType], ...]

def copyTextToClipboard(text: str) -> None: ...

class HelpCache:
    pages: WikiPages
    searcher: WhooshSearcher
    json_data: _WikiBlock | None
    def __init__(self) -> None: ...
    def prep(self, path: str, callback: Callable[[], object], item_type: str = ...) -> None: ...
    def hasHtml(self, path: str, help_id: str) -> bool: ...

class SharedState(core.Info, Generic[CT]):
    selectionCleared: ClassVar[QtCore.Signal]
    windowCloseRequested: ClassVar[QtCore.Signal]
    copiedToClipboard: ClassVar[QtCore.Signal]
    contentHeightChanged: ClassVar[QtCore.Signal]
    expanderKeyPressed: ClassVar[QtCore.Signal]
    expanderToggled: ClassVar[QtCore.Signal]
    helpReady: ClassVar[QtCore.Signal]
    def __init__(self, **kwargs: object) -> None: ...
    def setupEngine(self, engine: QtQml.QQmlEngine, **kwargs: object) -> None: ...
    def showHelpTip(self, title: str, text: str, tip_id: str, x: float = ..., y: float = ..., w: float = ..., h: float = ..., alignment: str = ...) -> None: ...

class BaseQmlWidget(QtQuickWidgets.QQuickWidget, Generic[SST]):
    SOURCE_URL: str
    _state: SST
    def __init__(self, *, state: SST | None = ..., parent: QtWidgets.QWidget | None = ...) -> None: ...

class BaseQmlView(QtQuick.QQuickView, Generic[SST]):
    SOURCE_URL: str
    _state: SST
    DEFAULT_SIZE: QtCore.QSize
    MINIMUM_SIZE: QtCore.QSize
    def __init__(self, *, state: SST | None = ..., parent_window: QtGui.QWindow | None = ...) -> None: ...
    def tryToClose(self, *args: object, **kwargs: object) -> None: ...
    def placeNearMouse(self) -> None: ...
