import hou
from collections.abc import Mapping
from houtypes import RadialMenuKwargs
from typing import Literal, NotRequired, Protocol, TypedDict, Unpack

class _RadialMenuScript(Protocol):
    def __call__(self, **kwargs: Unpack[RadialMenuKwargs]) -> object: ...

class _RadialMenuItem(TypedDict):
    type: Literal['script_action', 'script_submenu']
    label: str
    icon: NotRequired[str]
    script: _RadialMenuScript

class _RadialMenuModule(Protocol):
    def setRadialMenu(self, menu: Mapping[str, _RadialMenuItem], /) -> None: ...

def makeBaseMenu(radialmenu: _RadialMenuModule, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
def makeBezierMenu(radialmenu: _RadialMenuModule, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
def makePolygonMenu(radialmenu: _RadialMenuModule, node: hou.SopNode) -> dict[str, _RadialMenuItem]: ...
def makeMenu(radialmenu: _RadialMenuModule, node: hou.SopNode | None) -> dict[str, _RadialMenuItem]: ...
