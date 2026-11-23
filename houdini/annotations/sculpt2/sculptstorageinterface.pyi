from collections.abc import Mapping, Sequence
from typing import TypeAlias

import hou
from frameworkstate.storageinterface import StorageInterface

# The values of the node's parms the HUD parms are bound to.
_SculptStorageValue: TypeAlias = int | float | str | tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | hou.Ramp

class SculptStorageInterface(StorageInterface[_SculptStorageValue]):
    stringTypes: list[hou.EnumValue[hou.parmTemplateType]]
    floatTypes: list[hou.EnumValue[hou.parmTemplateType]]
    intTypes: list[hou.EnumValue[hou.parmTemplateType]]
    node: hou.SopNode
    def __init__(self, node: hou.SopNode, bindings: Mapping[str, str]) -> None: ...
    def getStorageVal(self, storageKey: str) -> _SculptStorageValue: ...
    def storeStorageVal(
        self, storageKey: str, val: int | float | str | Sequence[float] | Sequence[str] | hou.Ramp | None
    ) -> None: ...
