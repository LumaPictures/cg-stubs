import PySide6.QtCore
import PySide6.QtGui
import enum
import re
import typing
from hutil.PySide import QtCore as QtCore, QtGui as QtGui
from hutil.PySide.QtCore import Qt as Qt
from hutil.util import find_object as find_object
from typing import ClassVar, Iterable

from typing import TypeVar
from typing import TypeVar
_H = TypeVar('_H', bound=PySide6.QtGui.QSyntaxHighlighter)
QML_IMPORT_NAME: str
QML_IMPORT_MAJOR_VERSION: int
QML_IMPORT_MINOR_VERSION: int
ws_expr: re.Pattern[str]
unichar_expr: re.Pattern[str]
number_expr: re.Pattern[str]
syntax_classes: dict[str, str | type[PySide6.QtGui.QSyntaxHighlighter]]

def find_highlighter_class(spec: str | type[PySide6.QtGui.QSyntaxHighlighter]) -> type[PySide6.QtGui.QSyntaxHighlighter]: ...

class SyntaxHighlight(QtCore.QObject):
    documentChanged: ClassVar[PySide6.QtCore.Signal]
    languageChanged: ClassVar[PySide6.QtCore.Signal]
    colorsChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self) -> None: ...
    document: PySide6.QtCore.Property
    language: PySide6.QtCore.Property
    colors: PySide6.QtCore.Property

class BlockStats(QtCore.QObject):
    documentChanged: ClassVar[PySide6.QtCore.Signal]
    layoutChanged: ClassVar[PySide6.QtCore.Signal]
    blockCountChanged: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, parent: PySide6.QtCore.QObject | None = None) -> None: ...
    document: PySide6.QtCore.Property
    def blockCount(self) -> int: ...
    def blockHeight(self, block_num: int) -> float | None: ...

class Style(enum.Enum):
    plain = enum.auto()
    string = enum.auto()
    var = enum.auto()
    func = enum.auto()
    keyword = enum.auto()
    quote = enum.auto()
    number = enum.auto()
    ref = enum.auto()
    comment = enum.auto()
    error = enum.auto()
    type = enum.auto()
    extra = enum.auto()

style_to_hcs_name: dict[Style, str]
default_colors: dict[Style, PySide6.QtGui.QColor]

def nullStyleColor(style: Style) -> PySide6.QtGui.QColor: ...
def defaultStyleColor(style: Style) -> PySide6.QtGui.QColor: ...
def alts(names: Iterable[str]) -> str: ...
def keywordExpr(names: Iterable[str]) -> re.Pattern[str]: ...
def bitstackPush(stackbits: int, bits: int, size: int = 2) -> int: ...
def bitstackPop(stackbits: int, size: int) -> tuple[int, int]: ...
def bitstackTrim(stackbits: int, size: int) -> int: ...
def bitstackReplace(stackbits: int, bits: int, size: int) -> int: ...
def bitstackPeek(stackbits: int, size: int) -> int: ...
@typing.overload
def syntaxHighlighterConverter(hiliter: str) -> type[PySide6.QtGui.QSyntaxHighlighter]: ...
@typing.overload
def syntaxHighlighterConverter(hiliter: _H) -> _H: ...

class HighlighterBase(QtGui.QSyntaxHighlighter):
    def __init__(self, parent: PySide6.QtCore.QObject | None = None) -> None: ...
    def styleColor(self, style: Style) -> PySide6.QtGui.QColor: ...

def convertToHtml(cls: type[HighlighterBase] | str, text: str) -> str: ...
