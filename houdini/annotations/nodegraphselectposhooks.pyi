from collections.abc import Sequence

import hou
from canvaseventtypes import NetworkComponent
from typing_extensions import Required, TypedDict

# The network editor's context data for the select-position state
# (hou.NetworkEditor.eventContextData(), from the tool script that started it), which
# nodegraphselectpos passes to the setSelectPosContextData() hooks to rewire: the items to
# wire into the new node's inputs (with an output index, and optionally the input index),
# the items to wire its outputs to (with their input index and its output index), whether
# to branch rather than insert, the new node's type name, and its position.
class _SelectPosContextData(TypedDict, total=False):
    inputs: Required[
        Sequence[tuple[hou.Node | hou.IndirectInput | None, int] | tuple[hou.Node | hou.IndirectInput | None, int, int]]
    ]
    outputs: Required[Sequence[tuple[hou.Node | hou.NetworkDot, int, int]]]
    branch: Required[bool]
    nodetypename: str
    pos: hou.Vector2

def setSelectPosContextData(
    editor: hou.NetworkEditor,
    contextdata: _SelectPosContextData,
    locatedconn: NetworkComponent | None,
    locatedinput: NetworkComponent | None,
    locatedoutput: NetworkComponent | None,
) -> bool: ...
