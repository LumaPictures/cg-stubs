from PySide6.QtCore import QObject, QRegularExpression
from hutil.PySide.QtGui import QSyntaxHighlighter, QTextCharFormat
from typing import TypedDict

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

def format(color: str, style: str = '') -> QTextCharFormat:
    """Return a QTextCharFormat with the given attributes.
    """

STYLES: _Styles

class PythonHighlighter(QSyntaxHighlighter):
    """Syntax highlighter for the Python language.
    """
    tri_single: tuple[QRegularExpression, int, QTextCharFormat]
    tri_double: tuple[QRegularExpression, int, QTextCharFormat]
    rules: list[tuple[QRegularExpression, int, QTextCharFormat]]
    keywords: list[str]
    operators: list[str]
    braces: list[str]
    def __init__(self, document: QObject) -> None: ...
    def highlightBlock(self, text: str) -> None:
        """Apply syntax highlighting to the given block of text.
        """
    def match_multiline(self, text: str, delimiter: QRegularExpression, in_state: int, style: QTextCharFormat) -> bool:
        """Do highlighting of multi-line strings. ``delimiter`` should be a
           ``QRegularExpression`` for triple-single-quotes or
           triple-double-quotes, and ``in_state`` should be a unique integer to
           represent the corresponding state changes when inside those strings.

        Returns True if we're still inside a multi-line string when this
        function is finished.
        """
