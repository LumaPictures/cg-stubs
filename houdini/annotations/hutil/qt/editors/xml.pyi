import re

from hutil.qt.editors.syntax import HighlighterBase

identifier_expr: re.Pattern[str]
tag_open_expr: re.Pattern[str]
entity_expr: re.Pattern[str]

class XmlHighlighter(HighlighterBase):
    def highlightBlock(self, line: str) -> None: ...
