import re

from hutil.help.search import indexing
from hutil.help.search.searching import Predicate

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

class QueryParser:
    db: indexing.Db
    field_expr: re.Pattern[str]
    def __init__(self, db: indexing.Db) -> None: ...
    def paren_expr(self, text: str, pos: int = ...) -> tuple[Predicate, int]: ...
    def parse_expression(self, text: str, pos: int = ...) -> None: ...
