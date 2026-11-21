# Houdini stubs generated from Houdini 22.0.466

import enum
from .syntax import HighlighterBase as HighlighterBase, Style as Style
from hutil.PySide import QtWidgets as QtWidgets
from hutil.PySide.QtCore import Qt as Qt

class RegexState(enum.Enum):
    normal = enum.auto()
    char_set_start = enum.auto()
    char_set = enum.auto()

class RegexHighlighter(HighlighterBase):
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def setActive(self, active: bool) -> None: ...
    def highlightBlock(self, line: str) -> None: ...
