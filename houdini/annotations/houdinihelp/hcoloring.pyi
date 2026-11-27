import re
from collections.abc import Callable, Iterator, Sequence
from typing import ClassVar, TypeAlias

from pygments.lexer import RegexLexer, include
from pygments.token import _TokenType

_TokenAction: TypeAlias = _TokenType | Callable[[RegexLexer, re.Match[str]], Iterator[tuple[int, _TokenType, str]]]
_Rule: TypeAlias = tuple[str, _TokenAction] | tuple[str, _TokenAction, str] | include

def namedColorToHex(name: str) -> str: ...

class VexLexer(RegexLexer):
    name: ClassVar[str]
    aliases: ClassVar[Sequence[str]]
    filenames: ClassVar[Sequence[str]]
    mimetypes: ClassVar[Sequence[str]]
    tokens: ClassVar[dict[str, list[_Rule]]]

class OpenCLLexer(RegexLexer):
    name: ClassVar[str]
    aliases: ClassVar[Sequence[str]]
    filenames: ClassVar[Sequence[str]]
    mimetypes: ClassVar[Sequence[str]]
    tokens: ClassVar[dict[str, list[_Rule]]]

class HScriptLexer(RegexLexer):
    name: ClassVar[str]
    aliases: ClassVar[Sequence[str]]
    filenames: ClassVar[Sequence[str]]
    mimetypes: ClassVar[Sequence[str]]
    tokens: ClassVar[dict[str, list[_Rule]]]
