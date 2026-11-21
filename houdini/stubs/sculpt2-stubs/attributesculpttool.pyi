# Houdini stubs generated from Houdini 22.0.466

from frameworkstate.parameterwidget import ParameterWidget as ParameterWidget
from houtypes import ViewerStateEventKwargs
from sculpt2 import sculptparms as sculptparms
from sculpt2.sculpttool import SculptTool as SculptTool, _SculptToolState
from sidefx_stroke import StrokeCursor as StrokeCursor
from typing import Literal

from typing import TypeAlias
from typing import TypeAlias
_HudRow: TypeAlias = dict[str, str | int | list[dict[str, str]]]
class AttributeSculptTool(SculptTool):
    HOTKEY_BRUSHES: list[tuple[str, str]]
    hud_rows: list[_HudRow]
    name: str
    def __init__(self, state: _SculptToolState) -> None: ...
    def label(self) -> str:
        """
        that label is being used in the hud to show the current tool name
        """
    def getBrushParm(self) -> Literal['attributebrush']: ...
    def getMode(self) -> str: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool | None:
        """shows how to use the hotkeys of the framework
        """

def load(viewer_state: _SculptToolState) -> AttributeSculptTool: ...
