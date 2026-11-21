# Houdini stubs generated from Houdini 22.0.466

import enum
from . import CodeEditor as CodeEditor
from .syntax import HighlighterBase as HighlighterBase, Style as Style, bitstackPeek as bitstackPeek, bitstackPush as bitstackPush, bitstackReplace as bitstackReplace, bitstackTrim as bitstackTrim, number_expr as number_expr, unichar_expr as unichar_expr, ws_expr as ws_expr
from hutil.PySide import QtWidgets as QtWidgets
from hutil.PySide.QtCore import Qt as Qt

class JsonState(enum.IntEnum):
    object = 0
    object_key = 1
    array = 2

JSON_STATE_SIZE: int

def json_token(stackbits: int, line: str, pos: int, in_string: bool = False) -> tuple[Style, int, JsonState | int, bool]: ...

class JsonHighlighter(HighlighterBase):
    def highlightBlock(self, text: str) -> None: ...

class JsonpathHighlighter(HighlighterBase):
    """
    Highlighter for jsonpathfx syntax.
    """
    def highlightBlock(self, text: str) -> None: ...

class JsonEditor(CodeEditor):
    indent_after_chars: str
    dedent_after_chars: str
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
