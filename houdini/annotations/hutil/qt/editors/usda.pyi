import re
from collections.abc import Iterator

from hutil.qt.editors.syntax import HighlighterBase, Style

USDA_KEYWORDS: tuple[str, str, str, str, str, str, str, str, str]
SPEC_KEYWORDS: tuple[str, str, str]
MOD_KEYWORDS: tuple[str, str, str, str]
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

def tokens(state: State, line: str, pos: int) -> Iterator[tuple[Style, int, State]]: ...

class UsdaHighlighter(HighlighterBase):
    def highlightBlock(self, text: str) -> None: ...
