from collections.abc import Sequence
from typing import ClassVar, TypeAlias

from pygments.lexer import RegexLexer
from pygments.token import _TokenType

_Rule: TypeAlias = tuple[str, _TokenType] | tuple[str, _TokenType, str]

class UsdLexer(RegexLexer):
    name: ClassVar[str]
    aliases: ClassVar[Sequence[str]]
    filenames: ClassVar[Sequence[str]]
    mimetypes: ClassVar[Sequence[str]]
    tokens: ClassVar[dict[str, list[_Rule]]]
