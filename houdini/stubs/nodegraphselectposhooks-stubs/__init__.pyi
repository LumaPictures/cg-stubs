# Houdini stubs generated from Houdini 22.0.466

from canvaseventtypes import *
import hou
from canvaseventtypes import NetworkComponent as NetworkComponent
from collections.abc import Sequence
from typing_extensions import Required, TypedDict

class _SelectPosContextData(TypedDict, total=False):
    inputs: Required[Sequence[tuple[hou.Node | hou.IndirectInput | None, int] | tuple[hou.Node | hou.IndirectInput | None, int, int]]]
    outputs: Required[Sequence[tuple[hou.Node | hou.NetworkDot, int, int]]]
    branch: Required[bool]
    nodetypename: str
    pos: hou.Vector2

def setSelectPosContextData(editor: hou.NetworkEditor, contextdata: _SelectPosContextData, locatedconn: NetworkComponent | None, locatedinput: NetworkComponent | None, locatedoutput: NetworkComponent | None) -> bool: ...
