from typing import TypedDict

import hou

class _MoveSelectionKwargs(TypedDict):
    lop: hou.LopNode | None
    lopnet: hou.LopNetwork | None

theTransformHandles: set[str]
EDIT_STATE_NAME: str
ANIMATE_STATE_NAME: str
LIGHTMIXER_STATE_NAME: str
STAGEMANAGER_STATE_NAME: str
PAINTINSTANCES_STATE_NAME: str

def hasTransformHandle(node_type: hou.OpNodeType) -> bool: ...
def getStateToMoveSelection(kwargs: _MoveSelectionKwargs) -> dict[str, str | None]: ...
