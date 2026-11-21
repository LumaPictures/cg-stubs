import re
from typing import NamedTuple

from hutil.qt.editors.syntax import HighlighterBase, Style

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

class Token(NamedTuple):
    style: Style
    end_pos: int
    new_state: State | int
    continues: bool

def token(state_int: int, line: str, pos: int = ...) -> Token: ...

class PythonHighlighter(HighlighterBase):
    def highlightBlock(self, text: str) -> None: ...
