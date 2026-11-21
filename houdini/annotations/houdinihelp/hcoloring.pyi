import re
from collections.abc import Callable, Iterator
from typing import TypeAlias

from pygments.lexer import RegexLexer, include
from pygments.token import _TokenType

_TokenAction: TypeAlias = _TokenType | Callable[[RegexLexer, re.Match[str]], Iterator[tuple[int, _TokenType, str]]]
_Rule: TypeAlias = tuple[str, _TokenAction] | tuple[str, _TokenAction, str] | include

def namedColorToHex(name: str) -> str: ...

class VexLexer(RegexLexer):
    name: str
    aliases: list[str]
    filenames: list[str]
    mimetypes: list[str]
    tokens: dict[str, list[_Rule]]

class OpenCLLexer(RegexLexer):
    name: str
    aliases: list[str]
    filenames: list[str]
    mimetypes: list[str]
    tokens: dict[str, list[_Rule]]

class HScriptLexer(RegexLexer):
    name: str
    aliases: list[str]
    filenames: list[str]
    mimetypes: list[str]
    tokens: dict[str, list[_Rule]]
