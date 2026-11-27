from pygments.token import *
from collections.abc import Sequence
from pygments.lexer import RegexLexer
from typing import ClassVar

from typing import TypeAlias
from pygments.token import _TokenType
from typing import TypeAlias
_Rule: TypeAlias = tuple[str, _TokenType] | tuple[str, _TokenType, str]
class UsdLexer(RegexLexer):
    name: ClassVar[str]
    aliases: ClassVar[Sequence[str]]
    filenames: ClassVar[Sequence[str]]
    mimetypes: ClassVar[Sequence[str]]
    tokens: ClassVar[dict[str, list[_Rule]]]
