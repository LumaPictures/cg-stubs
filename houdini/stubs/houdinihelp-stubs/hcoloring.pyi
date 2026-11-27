from collections.abc import Sequence
from pygments.lexer import RegexLexer
from pygments.style import Style as Style
from pygments.token import Error as Error, Generic as Generic, Literal as Literal, Other as Other, Whitespace as Whitespace
from typing import ClassVar

from typing import TypeAlias
from collections.abc import Callable
from collections.abc import Iterator
from pygments.lexer import include
from pygments.token import _TokenType
from typing import TypeAlias
import re
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
