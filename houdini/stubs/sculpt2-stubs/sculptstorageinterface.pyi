# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Mapping, Sequence
from frameworkstate.storageinterface import StorageInterface

from typing import TypeAlias
from typing import TypeAlias
_SculptStorageValue: TypeAlias = int | float | str | tuple[int, ...] | tuple[float, ...] | tuple[str, ...] | hou.Ramp
class SculptStorageInterface(StorageInterface[_SculptStorageValue]):
    node: hou.SopNode
    stringTypes: list[hou.EnumValue[hou.parmTemplateType]]
    floatTypes: list[hou.EnumValue[hou.parmTemplateType]]
    intTypes: list[hou.EnumValue[hou.parmTemplateType]]
    def __init__(self, node: hou.SopNode, bindings: Mapping[str, str]) -> None: ...
    def getStorageVal(self, storageKey: str) -> _SculptStorageValue: ...
    def storeStorageVal(self, storageKey: str, val: int | float | str | Sequence[float] | Sequence[str] | hou.Ramp | None) -> None: ...
