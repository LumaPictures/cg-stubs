import re
from . import indexing as indexing
from .searching import Fts5Predicate as Fts5Predicate, Need as Need, Predicate as Predicate, Query as Query, SqlPredicate as SqlPredicate

class NoMatch(Exception): ...

op_patterns: str
ws_expr: re.Pattern[str]
word_expr: re.Pattern[str]
quote_expr: re.Pattern[str]
tag_expr: re.Pattern[str]
and_expr: re.Pattern[str]
or_expr: re.Pattern[str]
not_expr: re.Pattern[str]
open_paren_expr: re.Pattern[str]
close_paren_expr: re.Pattern[str]

def lex_string_literal(text: str, pos: int) -> tuple[str, int] | None: ...

class QueryParser:
    db: indexing.Db
    field_expr: re.Pattern[str]
    def __init__(self, db: indexing.Db) -> None: ...
    def paren_expr(self, text: str, pos: int = 0) -> tuple[Predicate, int]: ...
    def parse_expression(self, text: str, pos: int = 0) -> None: ...
