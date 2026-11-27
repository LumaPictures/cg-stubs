import dataclasses
import enum
import re
from collections.abc import Mapping
from typing import Callable, Collection, Generic, TypeAlias, TypeVar

from typing import TypeAlias
from typing import TypeVar
from typing import Never
K = TypeVar('K', bound=enum.Enum)
T = TypeVar('T')
_PrefixF = TypeVar('_PrefixF', bound=Callable[[Never, Never], object])
_InfixF = TypeVar('_InfixF', bound=Callable[[Never, Never, Never], object])
LexerFn: TypeAlias = Callable[[str, int], 'tuple[Token[K], int] | None']
PrefixParselet: TypeAlias = Callable[['Token[K]'], T]
InfixParselet: TypeAlias = Callable[[T, 'Token[K]'], T]
ws_expr: re.Pattern[str]

class ParserError(Exception):
    pos: int
    end_pos: int
    def __init__(self, msg: str, pos: int, end_pos: int) -> None: ...

class StdKind(enum.Enum):
    ws = enum.auto()
    eof = enum.auto()
    string = enum.auto()
    open_paren = enum.auto()
    close_paren = enum.auto()
    comment = enum.auto()

@dataclasses.dataclass(frozen=True)
class Token(Generic[K]):
    kind: StdKind | K
    payload: str
    pos: int
    end_pos: int
    groupdict: dict[str, str] | None = ...

def prefix(kind: enum.Enum) -> Callable[[_PrefixF], _PrefixF]: ...
def infix(kind: enum.Enum, precedence: int = 1) -> Callable[[_InfixF], _InfixF]: ...
def parse_string(text: str, pos: int) -> tuple[str, int] | None: ...

class Parser(Generic[K, T]):
    token_exprs: dict[StdKind | K, str | re.Pattern[str] | LexerFn[K]]
    ignore_kinds: set[StdKind | K]
    text: str
    prefixes: dict[StdKind | K, PrefixParselet[K, T]]
    infixes: dict[StdKind | K, InfixParselet[T, K]]
    tokens: list[Token[K]]
    def __init__(self, token_exprs: Mapping[StdKind | K, str | re.Pattern[str] | LexerFn[K]], ignore_kinds: Collection[StdKind | K] = ..., ignore_whitespace: bool = True) -> None: ...
    def addStringParsing(self) -> None: ...
    def lex_string_literal(self, text: str, pos: int) -> tuple[Token[K], int] | None: ...
    def lex_token(self, text: str, pos: int) -> tuple[Token[K], int] | None: ...
    def lex(self, text: str) -> list[Token[K]]: ...
    def has_next(self) -> bool: ...
    def take(self, kind: StdKind | K) -> Token[K] | None: ...
    def consume(self, kind: StdKind | K | None = None) -> Token[K]: ...
    def current(self) -> Token[K]: ...
    def lookahead(self, distance: int) -> Token[K]: ...
    def current_infix(self) -> InfixParselet[T, K] | None: ...
    def infix_precedence(self) -> int: ...
    def expression(self, precedence: int = 0) -> T: ...
    def parse(self, text: str) -> T: ...
