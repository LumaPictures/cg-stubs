import re
from collections.abc import Sequence
from types import TracebackType
from typing import ClassVar, Self, TypeAlias

import hou
from bookish.search import WhooshSearcher
from bookish.wiki.wikipages import WikiPages, _WikiBlock, _WikiContent
from houdinihelp.api import ParmSpec
from lxml import etree
from PySide6 import QtCore, QtGui, QtQml, QtQuick
from PySide6.QtCore import Qt

from hutil.qt.common import config, qmlviews

_JsonBlocks: TypeAlias = _WikiBlock | list[_WikiBlock]

def scaledSize(scale: float, size: float) -> float: ...

STYLESHEET: str
help_server_url: QtCore.QUrl
nl_expr: re.Pattern[str]
ws_expr: re.Pattern[str]
parser: etree.HTMLParser

def perfTime(time: float) -> float: ...
def assetInlineHelp(nodetype: hou.NodeType) -> str: ...
def parseInlineParmHelp(
    template: hou.ParmTemplate, pages: WikiPages
) -> list[_WikiBlock] | _WikiBlock | None: ...
def parameterDefault(template: hou.ParmTemplate) -> str: ...
def serverUrl(path: str) -> QtCore.QUrl: ...
def formatPlainText(path: str, plain_text: str, pages: WikiPages) -> str: ...
def findSummary(path: str, json_data: _JsonBlocks, pages: WikiPages) -> str: ...
def getHelpSummary(path: str, pages: WikiPages) -> str: ...

image_expr: re.Pattern[str]
icons_expr: re.Pattern[str]
img_path_expr: re.Pattern[str]

class Replacer:
    limit: int
    count: int
    def __init__(self, limit: int = ...) -> None: ...
    def repl(self, match: re.Match[str]) -> str: ...

def blocksToHtml(
    path: str, json_data: _WikiContent, pages: WikiPages, searcher: WhooshSearcher | None = ...
) -> str: ...
def htmlToPlainText(html: str) -> str: ...

class HelpNotFound(Exception): ...

class ResizingProvider(QtQuick.QQuickImageProvider):
    width: int
    baseUrl: QtCore.QUrl
    def __init__(self) -> None: ...
    def requestPixmap(self, name: str, size: QtCore.QSize, req_size: QtCore.QSize) -> QtGui.QPixmap: ...

class TipState(qmlviews.SharedState[config.BaseConfig]):
    type: str
    origin: str
    alignment: str
    title: str
    html: str
    plainText: str
    fixedFont: bool
    internalName: str
    iconName: str
    bars: list[dict[str, str | float]]
    default: str
    hotkeySymbol: str
    hotkeyString: str
    hasHelpUrl: bool
    helpUrl: QtCore.QUrl | None
    baseUrl: QtCore.QUrl | None
    isError: bool
    windowHideRequested: ClassVar[QtCore.Signal]
    updateStarted: ClassVar[QtCore.Signal]
    updateFinished: ClassVar[QtCore.Signal]
    def setupEngine(self, engine: QtQml.QQmlEngine, **kwargs: object) -> None: ...
    def setServerPath(self, path: str) -> None: ...
    def convertHtmlToPlainText(self) -> None: ...
    def clear(self) -> None: ...

class TipView(qmlviews.BaseQmlView[TipState]):
    SOURCE_URL: str
    pages: WikiPages
    def __init__(self, *, parent_window: QtGui.QWindow | None = ...) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    def setHotkey(self, hotkey_symbol: str, hotkey_string: str) -> None: ...
    def setText(
        self, text: str, title: str = ..., hotkey_symbol: str = ..., hotkey_string: str = ..., fixed_font: bool = ...
    ) -> None: ...
    def setFrom(
        self,
        url: str,
        type: str = ...,
        title: str = ...,
        text: str = ...,
        hotkey_symbol: str = ...,
        hotkey_string: str = ...,
        fixed_font: bool = ...,
    ) -> None: ...
    def setPerformanceStats(self, title: str, text: str, bars: Sequence[tuple[str, float]]) -> None: ...
    def fillFromTool(self, name: str) -> None: ...
    def fillFromNodeType(self, nodepath: str, nodetype: hou.NodeType) -> None: ...
    def fillFromParm(self, parmspec: ParmSpec) -> None: ...
    def fillFromHelpPath(self, path: str, text: str, fragment: str = ...) -> None: ...
    def display(self, pos: QtCore.QPoint | None = ..., target: QtCore.QRect | None = ...) -> None: ...
    def undisplay(self) -> None: ...

tooltip_window: TipView | None

def getView() -> TipView: ...
def displayHtml(
    title: str,
    html: str,
    x: int,
    y: int,
    w: int,
    h: int,
    hotkey: str = ...,
    help_url: str = ...,
    alignment: str = ...,
) -> None: ...
def openToolTip(
    url: str,
    text: str,
    x: int,
    y: int,
    w: int,
    h: int,
    title: str,
    hotkey_symbol: str,
    hotkey_string: str,
    use_fixed_font: bool,
) -> None: ...
def openPerfMonToolTip(
    title: str, text: str, bars: Sequence[tuple[str, float]], x: int, y: int, w: int, h: int
) -> None: ...
def closeToolTips() -> None: ...
