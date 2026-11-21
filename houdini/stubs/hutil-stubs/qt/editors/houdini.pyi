# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtGui
import PySide6.QtWidgets
import enum
import re
from . import CodeEditor as CodeEditor
from .syntax import HighlighterBase as HighlighterBase, Style as Style, keywordExpr as keywordExpr, ws_expr as ws_expr
from collections.abc import Iterator
from hutil.PySide.QtCore import Qt as Qt
from typing import ClassVar

class VexEditor(CodeEditor):
    indent_after_chars: str
    dedent_after_chars: str
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None) -> None: ...
    def setDocument(self, document: PySide6.QtGui.QTextDocument) -> None: ...
    def helpForWord(self, word: str) -> str | None: ...

class ExpressionHighlighter(HighlighterBase):
    func_expr: ClassVar[re.Pattern[str]]
    var_expr: ClassVar[re.Pattern[str]]
    def highlightBlock(self, line: str) -> None: ...

class PrimPatternHighlighter(HighlighterBase):
    ws_expr: ClassVar[re.Pattern[str]]
    word_expr: ClassVar[re.Pattern[str]]
    auto_expr: ClassVar[re.Pattern[str]]
    func_expr: ClassVar[re.Pattern[str]]
    exprs: ClassVar[dict[Style, re.Pattern[str]]]
    @staticmethod
    def matchStyle(line: str, pos: int) -> tuple[Style, int] | None: ...
    def highlightBlock(self, line: str) -> None: ...

VEX_KEYWORDS: tuple[str, ...]
VEX_TYPES: tuple[str, ...]
kw_expr: re.Pattern[str]
type_expr: re.Pattern[str]
attr_expr: re.Pattern[str]
call_expr: re.Pattern[str]
identifier_expr: re.Pattern[str]
number_expr: re.Pattern[str]

class VexState(enum.IntEnum):
    normal = 0
    double_quoted = 1
    single_quoted = 2
    line_comment = 3
    block_comment = 4
    preproc_comment = 5
    attribute = 6

def vex_token(state: VexState, line: str, pos: int = 0) -> tuple[Style, int, VexState]: ...

class VexHighlighter(HighlighterBase):
    def highlightBlock(self, text: str) -> None: ...

class LSystemHighlighter(HighlighterBase):
    funcs: ClassVar[str]
    moves: ClassVar[str]
    mods: ClassVar[str]
    utils: ClassVar[str]
    vrbls: ClassVar[str]
    expr: ClassVar[re.Pattern[str]]
    @classmethod
    def highlights(cls, text: str) -> Iterator[tuple[int, int, Style]]: ...
    def convertToHtml(self, text: str) -> str: ...
    def highlightBlock(self, text: str) -> None: ...
