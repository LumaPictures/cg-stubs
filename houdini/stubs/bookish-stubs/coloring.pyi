# Houdini stubs generated from Houdini 22.0.466

from bookish import functions as functions, util as util
from bookish.wiki.wikipages import _WikiBlock
from collections.abc import Mapping, Sequence
from markupsafe import Markup
from pygments.lexer import Lexer as Lexer
from pygments.style import Style
from pygments.token import _TokenType

def jinja_format_code(block: _WikiBlock, lexername: str | None = None, pre: bool = False, extras: Mapping[str, Lexer | type[Lexer]] | None = None) -> Markup: ...
def lexer_for(name: str | None) -> Lexer | None: ...
def format_block(block: _WikiBlock, lexername: str | None = None, lexer: Lexer | None = None, pre: bool = False, extras: Mapping[str, Lexer | type[Lexer]] | None = None) -> str: ...
def format_string(source: str, lexername: str | None = None, lexer: Lexer | None = None, look: str = '', hl_lines: Sequence[int] | None = None, pre: bool = False) -> str: ...
def code_chars(code: int | str) -> str: ...

class Ansi:
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
