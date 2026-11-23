import enum
import re
from .syntax import HighlighterBase as HighlighterBase, Style as Style, number_expr as number_expr
from hutil.PySide.QtCore import Qt as Qt

class XmlState(enum.Enum):
    text = enum.auto()
    cdata = enum.auto()
    start_tag = enum.auto()
    end_tag = enum.auto()
    attr = enum.auto()
    attr_value = enum.auto()
    decl = enum.auto()
    sq_attr = enum.auto()
    dq_attr = enum.auto()

identifier_expr: re.Pattern[str]
tag_open_expr: re.Pattern[str]
entity_expr: re.Pattern[str]

class XmlHighlighter(HighlighterBase):
    def highlightBlock(self, line: str) -> None: ...
