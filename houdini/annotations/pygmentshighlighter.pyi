from collections.abc import Generator, Sequence
from typing import TypedDict, Unpack, type_check_only

from PySide6 import QtCore, QtGui
from pygments.lexer import Lexer, RegexLexer
from pygments.style import Style
from pygments.token import _TokenType

def get_tokens_unprocessed(
    self: RegexLexer, text: str, stack: Sequence[str] = ...
) -> Generator[tuple[int, _TokenType, str], None, None]: ...

# __init__ setattr()s each keyword onto the instance.
@type_check_only
class _BlockUserDataKwargs(TypedDict, total=False):
    syntax_stack: tuple[str, ...] | list[str]

class PygmentsBlockUserData(QtGui.QTextBlockUserData):
    syntax_stack: tuple[str, ...] | list[str]
    def __init__(self, **kwds: Unpack[_BlockUserDataKwargs]) -> None: ...
    def __repr__(self) -> str: ...

class PygmentsHighlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent: QtCore.QObject, lexer: Lexer | None = ...) -> None: ...
    def highlightBlock(self, string: str) -> None: ...
    def set_style(self, style: str | type[Style]) -> None: ...
    def set_style_sheet(self, stylesheet: str) -> None: ...
