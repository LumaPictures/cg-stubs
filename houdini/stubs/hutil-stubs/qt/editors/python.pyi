import enum
import re
from .syntax import HighlighterBase as HighlighterBase, Style as Style, number_expr as number_expr
from hutil.PySide.QtCore import Qt as Qt
from typing import NamedTuple

c_escape: re.Pattern[str]
x_escape: re.Pattern[str]
u_escape: re.Pattern[str]
line_cont: re.Pattern[str]
kw_expr: re.Pattern[str]
return_anno: re.Pattern[str]
soft_kw_expr: re.Pattern[str]
func_expr: re.Pattern[str]
class_expr: re.Pattern[str]
def_expr: re.Pattern[str]
arrow_expr: re.Pattern[str]
colon_expr: re.Pattern[str]
special_expr: re.Pattern[str]
decorator_expr: re.Pattern[str]

class State(enum.IntEnum):
    normal = enum.auto()
    in_class = enum.auto()
    in_def = enum.auto()
    sq_string = enum.auto()
    dq_string = enum.auto()
    tri_sq_string = enum.auto()
    tri_dq_string = enum.auto()

class Token(NamedTuple):
    style: Style
    end_pos: int
    new_state: State | int
    continues: bool = ...

def token(state_int: int, line: str, pos: int = 0) -> Token: ...

class PythonHighlighter(HighlighterBase):
    def highlightBlock(self, text: str) -> None: ...
