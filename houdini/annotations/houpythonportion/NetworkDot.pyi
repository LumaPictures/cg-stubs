from hrecipes import rtypes

import hou

def insertInput(
    self: hou.NetworkDot,
    input_index: int,
    item_to_become_input: hou.NetworkMovableItem | None,
    output_index: int = ...,
) -> None: ...
def asData(self: hou.NetworkDot, **networkdot_opts: bool) -> rtypes.NetworkDotData: ...
def setFromData(self: hou.NetworkDot, data: rtypes.NetworkDotData) -> None: ...
