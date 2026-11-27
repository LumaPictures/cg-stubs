import hou
from collections.abc import Mapping
from houtypes import RadialMenuKwargs
from typing import NotRequired, Protocol, TypedDict, Unpack

class _RadialMenuScript(Protocol):
    def __call__(self, **kwargs: Unpack[RadialMenuKwargs]) -> object: ...

class _RadialMenuItem(TypedDict):
    type: str
    label: str
    icon: NotRequired[str]
    script: _RadialMenuScript

class _RadialMenuModule(Protocol):
    def setRadialMenu(self, menu: Mapping[str, _RadialMenuItem], /) -> None: ...

def makeMenuVersion2(radialmenu: _RadialMenuModule, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
def makeMenuVersion3(radialmenu: _RadialMenuModule, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
def makeMenu(radialmenu: _RadialMenuModule, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
