from frameworkstate.parameterwidget import ParameterWidget as ParameterWidget
from houtypes import ViewerStateEventKwargs
from sculpt2 import groomparms as groomparms
from sculpt2.groomtool import GroomTool as GroomTool, _GroomToolState
from sidefx_stroke import StrokeCursor as StrokeCursor
from typing import Literal

from typing import TypeAlias
from typing import TypeAlias
_HudRow: TypeAlias = dict[str, str | int | list[dict[str, str]]]
class AttributeGroomTool(GroomTool):
    HOTKEY_TOOLS: list[tuple[str, str]]
    hud_rows: list[_HudRow]
    name: str
    def __init__(self, state: _GroomToolState) -> None: ...
    def label(self) -> str:
        """
        that label is being used in the hud to show the current tool name 
        """
    def getToolParm(self) -> Literal['attributetool']: ...
    def getIsPaintMode(self) -> bool: ...
    def getMode(self) -> str: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool | None:
        """shows how to use the hotkeys of the framework
        """

def load(viewer_state: _GroomToolState) -> AttributeGroomTool: ...
