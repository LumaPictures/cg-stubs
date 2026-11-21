# Houdini stubs generated from Houdini 22.0.466

import hou
from hrecipes import rtypes

def insertInput(self: hou.NetworkDot, input_index: int, item_to_become_input: hou.NetworkMovableItem | None, output_index: int = 0) -> None:
    """
insertInput(self, input_index, item_to_become_input, output_index=0)

    Connects a network item to the input of this dot, exactly like the
    two parameter form of setInput. But this method name and signature
    matches the signature of hou.Node.insertInput, which allows code to
    run on either a network dot or a node. The value of the input_index
    is ignored.

"""
def asData(self: hou.NetworkDot, **networkdot_opts: bool) -> rtypes.NetworkDotData:
    """
asData(inputs=True, position=False, metadata=False, verbose=False) ->
dict[str, Any]

    Returns a JSON-like data structure representing this network dot.


    inputs
        If this is True, the capture process saves input connections.

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
def setFromData(self: hou.NetworkDot, data: rtypes.NetworkDotData) -> None:
    """
setFromData(data: dict[str, Any]) -> None

    Updates the parameters, options, and contents of this node from
    data, as returned by OpNode.asData().


    data
        The network item data that describes a network item as data.

"""
