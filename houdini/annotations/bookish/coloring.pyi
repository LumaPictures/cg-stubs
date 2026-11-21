from collections.abc import Mapping, Sequence

from bookish.wiki.wikipages import _WikiBlock

from markupsafe import Markup
from pygments.lexer import Lexer
from pygments.style import Style
from pygments.token import _TokenType

def jinja_format_code(block: _WikiBlock, lexername: str | None = ..., pre: bool = ..., extras: Mapping[str, Lexer | type[Lexer]] | None = ...) -> Markup: ...
def lexer_for(name: str | None) -> Lexer | None: ...
def format_block(block: _WikiBlock, lexername: str | None = ..., lexer: Lexer | None = ..., pre: bool = ..., extras: Mapping[str, Lexer | type[Lexer]] | None = ...) -> str: ...
def format_string(source: str, lexername: str | None = ..., lexer: Lexer | None = ..., look: str = ..., hl_lines: Sequence[int] | None = ..., pre: bool = ...) -> str: ...
def code_chars(code: int | str) -> str: ...

class Ansi(object):
    black: str
    red: str
    green: str
    yellow: str
    blue: str
    magenta: str
    cyan: str
    white: str
    reset: str
    black_back: str
    red_back: str
    green_back: str
    yellow_back: str
    blue_back: str
    magenta_back: str
    cyan_back: str
    white_back: str
    reset_back: str
    bright: str
    dim: str
    normal: str
    reset_all: str

def cstring(code: str, string: str) -> str: ...

class DraculaStyle(Style):
    background_color: str
    default_style: str
    styles: dict[_TokenType, str]
