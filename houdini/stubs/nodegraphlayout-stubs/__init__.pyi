# Houdini stubs generated from Houdini 22.0.466

from canvaseventtypes import *
import hou
from collections.abc import Sequence

theBumpSize: float

class LayoutItem:
    item: hou.Node
    rect: hou.BoundingRect
    pos: hou.Vector2
    bumped: bool
    def __init__(self, item: hou.Node, rect: hou.BoundingRect) -> None: ...
    def bumpRect(self, amount: hou.Vector2 | Sequence[float], axis: int) -> None: ...
    def updateItem(self) -> bool: ...

def spaceNodes(editor: hou.NetworkEditor, axis: int) -> None: ...
def correctVopPositions(editor: hou.NetworkEditor) -> None: ...
