from typing import TypeAlias

from pygments.lexer import RegexLexer
from pygments.token import _TokenType

_Rule: TypeAlias = tuple[str, _TokenType] | tuple[str, _TokenType, str]

class UsdLexer(RegexLexer):
    name: str
    aliases: list[str]
    filenames: list[str]
    mimetypes: list[str]
    tokens: dict[str, list[_Rule]]
