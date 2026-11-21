# Houdini stubs generated from Houdini 22.0.466

import enum
import re
from .syntax import HighlighterBase as HighlighterBase, Style as Style, keywordExpr as keywordExpr, number_expr as number_expr
from collections.abc import Iterator
from hutil.PySide.QtCore import Qt as Qt

USDA_KEYWORDS: tuple[str, ...]
SPEC_KEYWORDS: tuple[str, ...]
MOD_KEYWORDS: tuple[str, ...]
PROPSPEC_KEYWORDS: tuple[str, ...]
newline_expr: re.Pattern[str]
ws_expr: re.Pattern[str]
kw_expr: re.Pattern[str]
singleton_expr: re.Pattern[str]
unicode_id_pattern: str
ascii_id_pattern: str
id_pattern: str
id_expr: re.Pattern[str]
format_expr: re.Pattern[str]
stage_ref_expr: re.Pattern[str]
external_expr: re.Pattern[str]
prim_spec_expr: re.Pattern[str]
prop_expr: re.Pattern[str]
variantset_expr: re.Pattern[str]
metadata_expr: re.Pattern[str]

class State(enum.IntEnum):
    normal = enum.auto()
    array = enum.auto()
    double_quoted = enum.auto()
    single_quoted = enum.auto()
    triple_single_quoted = enum.auto()
    triple_double_quoted = enum.auto()

def tokens(state: State, line: str, pos: int) -> Iterator[tuple[Style, int, State]]: ...

class UsdaHighlighter(HighlighterBase):
    def highlightBlock(self, text: str) -> None: ...
