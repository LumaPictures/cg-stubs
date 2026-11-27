from collections.abc import Callable, Collection, Iterable, Mapping
from typing import Concatenate, Generic

import hou
from apex.stateutils_2 import Hotkeys
from typing_extensions import NotRequired, TypedDict, TypeVar

_ToolT = TypeVar("_ToolT")
_R_co = TypeVar("_R_co", covariant=True)

# The keyword arguments of a ToolAction, as createActions() takes them for each action.
class _ToolActionDict(TypedDict, Generic[_ToolT]):
    label: str
    tooltip: NotRequired[str]
    icon: NotRequired[str | None]
    hotkey: NotRequired[str]
    """The name of a `Hotkeys` attribute."""
    function: NotRequired[Callable[Concatenate[_ToolT, ...], object] | None]
    """A tool method, called with the tool and the action's arguments; its result is ignored."""

class ToolAction(Generic[_ToolT, _R_co]):
    name: str
    label: str
    tooltip: str
    icon: str | None
    hotkey: str
    # Called unbound, with the tool first: the tools' own action methods.
    function: Callable[Concatenate[_ToolT, ...], _R_co] | None
    def __init__(
        self,
        name: str,
        label: str,
        tooltip: str = ...,
        icon: str | None = ...,
        hotkey: str = ...,
        function: Callable[Concatenate[_ToolT, ...], _R_co] | None = ...,
    ) -> None: ...
    # Raises TypeError for an action without a function.
    def __call__(self, tool: _ToolT, *args: object, **kwargs: object) -> _R_co: ...
    def bindStateParameter(self, template: hou.ViewerStateTemplate, align: bool = ...) -> None: ...
    def bindMenuItem(self, menu: hou.ViewerStateMenu, hotkeys: Hotkeys) -> None: ...

def createActions(actions_dict: Mapping[str, _ToolActionDict[_ToolT]], prefix: str = ...) -> list[ToolAction[_ToolT, object]]: ...
def bindStateParameters(actions: Collection[ToolAction[_ToolT, object]], template: hou.ViewerStateTemplate) -> None: ...
def bindActionMenu(name: str, label: str, actions: Iterable[ToolAction[_ToolT, object]], menu: hou.ViewerStateMenu, hotkeys: Hotkeys) -> None: ...
def executeAction(tool: _ToolT, actions: Iterable[ToolAction[_ToolT, object]], name: str, *args: object, **kwargs: object) -> bool: ...
def getToolActionList(actions: Iterable[ToolAction[_ToolT, object]], menu_name: str | None = ...) -> list[str]: ...
