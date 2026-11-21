# Houdini stubs generated from Houdini 22.0.466

import hou
from houtypes import RadialMenuKwargs
from typing import NotRequired, Protocol, TypedDict, Unpack

class _RadialMenuScript(Protocol):
    def __call__(self, **kwargs: Unpack[RadialMenuKwargs]) -> object: ...

class _RadialMenuItem(TypedDict):
    type: str
    label: str
    icon: NotRequired[str]
    script: _RadialMenuScript

def makeMenuVersion2(radialmenu: hou.RadialMenu, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
def makeMenuVersion3(radialmenu: hou.RadialMenu, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
def makeMenu(radialmenu: hou.RadialMenu, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
