# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Sequence
from hrecipes import rtypes

def isPicked(self: hou.NetworkMovableItem) -> bool:
    """
isPicked(self) -> bool

    Equivalent to calling hou.NetworkMovableItem.isSelected.

"""
def setPicked(self: hou.NetworkMovableItem, on: bool) -> None:
    """
setPicked(self, on)

    Equivalent to calling hou.NetworkMovableItem.setSelected with
    default values for all optional parameters.

"""
def shiftPosition(self: hou.NetworkMovableItem, delta: hou.Vector2 | Sequence[float]) -> None:
    """
shiftPosition(self, vector2)

    Equivalent to calling hou.NetworkMovableItem.move.

"""
def asData(self: hou.NetworkBox, **networkbox_opts: bool) -> rtypes.NetworkBoxData:
    """
asData(box_content=True, position=False, metadata=False, verbose=False)
-> dict[str, Any]

    Returns a JSON-like structure representing this object.


    box_content
        Whether to record items assigned to this network box.

    position
        If this is True, the capture process saves the node position.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

"""
def setFromData(self: hou.NetworkBox | hou.StickyNote, data: rtypes.NetworkItemData) -> dict[str, hou.NetworkMovableItem]:
    """
setFromData(data: dict[str, Any]) -> None

    Updates this object's settings from data, as returned by
    NetworkBox.asData().


    data
        The network item data that describes a network item as data.

"""
