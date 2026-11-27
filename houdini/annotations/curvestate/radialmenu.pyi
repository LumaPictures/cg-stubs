from collections.abc import Mapping
from typing import Literal, NotRequired, Protocol, TypedDict, Unpack

import hou
from houtypes import RadialMenuKwargs

class _RadialMenuScript(Protocol):
    def __call__(self, **kwargs: Unpack[RadialMenuKwargs]) -> object: ...

class _RadialMenuItem(TypedDict):
    type: Literal["script_action", "script_submenu"]
    label: str
    icon: NotRequired[str]
    script: _RadialMenuScript

# The `radialmenu` module, which Houdini's radial menu scripts get as a global and pass on.
class _RadialMenuModule(Protocol):
    def setRadialMenu(self, menu: Mapping[str, _RadialMenuItem], /) -> None: ...

def makeBaseMenu(radialmenu: _RadialMenuModule, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
def makeBezierMenu(radialmenu: _RadialMenuModule, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
def makePolygonMenu(radialmenu: _RadialMenuModule, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
def makeMenu(radialmenu: _RadialMenuModule, node: hou.SopNode | None) -> dict[str, _RadialMenuItem]: ...
