import hou
from canvaseventtypes import KeyboardEvent as KeyboardEvent, MouseEvent as MouseEvent
from collections.abc import Sequence
from typing import TypedDict, Unpack

class _RadialMenuData(TypedDict, total=False):
    branch: bool
    src_items: Sequence[hou.NetworkMovableItem]
    src_connector_indexes: Sequence[int]
    dest_items: Sequence[hou.NetworkMovableItem]
    dest_connector_indexes: Sequence[int]
    node_position: hou.Vector2

def openRadialMenu(uievent: MouseEvent | KeyboardEvent, modal: bool = False, **kwargs: Unpack[_RadialMenuData]) -> None: ...
