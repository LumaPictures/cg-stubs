from pygments.token import *
from pygments.lexer import RegexLexer

from typing import TypeAlias
from pygments.token import _TokenType
from typing import TypeAlias
_Rule: TypeAlias = tuple[str, _TokenType] | tuple[str, _TokenType, str]
class UsdLexer(RegexLexer):
    name: str
    aliases: list[str]
    filenames: list[str]
    mimetypes: list[str]
    tokens: dict[str, list[_Rule]]
