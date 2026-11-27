from typing import TypedDict

from PySide6.QtCore import QObject, QRegularExpression
from PySide6.QtGui import QTextCharFormat

# color is a color name; style contains "bold" and/or "italic".
def format(color: str, style: str = ...) -> QTextCharFormat: ...

class _Styles(TypedDict):
    keyword: QTextCharFormat
    operator: QTextCharFormat
    brace: QTextCharFormat
    defclass: QTextCharFormat
    string: QTextCharFormat
    string2: QTextCharFormat
    comment: QTextCharFormat
    self: QTextCharFormat
    numbers: QTextCharFormat

STYLES: _Styles

class PythonHighlighter:
    keywords: list[str]
    operators: list[str]
    braces: list[str]
    # (delimiter, block state, format)
    tri_single: tuple[QRegularExpression, int, QTextCharFormat]
    tri_double: tuple[QRegularExpression, int, QTextCharFormat]
    # (expression, the group to format, format)
    rules: list[tuple[QRegularExpression, int, QTextCharFormat]]
    # A QTextDocument, or a text edit whose document to highlight.
    def __init__(self, document: QObject) -> None: ...
    def highlightBlock(self, text: str) -> None: ...
    def match_multiline(self, text: str, delimiter: QRegularExpression, in_state: int, style: QTextCharFormat) -> bool: ...
