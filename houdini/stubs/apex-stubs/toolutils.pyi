import hou
from apex.stateutils_2 import Hotkeys as Hotkeys
from collections.abc import Callable as Callable, Collection, Iterable, Mapping
from typing import Concatenate, Generic
from typing_extensions import NotRequired, TypedDict

from typing import TypeVar
from typing_extensions import TypeVar
_ToolT = TypeVar('_ToolT')
_R_co = TypeVar('_R_co', covariant=True)
class _ToolActionDict(TypedDict, Generic[_ToolT]):
    label: str
    tooltip: NotRequired[str]
    icon: NotRequired[str | None]
    hotkey: NotRequired[str]
    function: NotRequired[Callable[Concatenate[_ToolT, ...], object] | None]

class ToolAction(Generic[_ToolT, _R_co]):
    """
    A class to hold all of the information necessary for the registration and
    execution of Viewer State Tool actions.
    These actions can be registered as state parameters and menu actions.
    :param name: The internal name of the action.
    :param label: The label displayed for the action.
    :param tooltip: The tooltip for the action.
    :param icon: The name of icon representing the action. If this remains None,
                 the label will be used instead.
    :param hokey: The name of the attribute in the hotkeys for the state.
                  For the animate state, this comes from apex.stateutils_2.Hotkeys.
    :param function: The function on the tool to be called when the action is performed.
    """
    name: str
    label: str
    tooltip: str
    icon: str | None
    hotkey: str
    function: Callable[Concatenate[_ToolT, ...], _R_co] | None
    def __init__(self, name: str, label: str, tooltip: str = '', icon: str | None = None, hotkey: str = '', function: Callable[Concatenate[_ToolT, ...], _R_co] | None = None) -> None: ...
    def __call__(self, tool: _ToolT, *args: object, **kwargs: object) -> _R_co: ...
    def bindStateParameter(self, template: hou.ViewerStateTemplate, align: bool = False) -> None:
        """
        Binds an action button to the viewer state parameters
        """
    def bindMenuItem(self, menu: hou.ViewerStateMenu, hotkeys: Hotkeys) -> None:
        """
        Binds an action menu item to the viewer state's right-click menu.
        """

def createActions(actions_dict: Mapping[str, _ToolActionDict[_ToolT]], prefix: str = '') -> list[ToolAction[_ToolT, object]]:
    """
    Creates a list of ToolAction objects from a dictionary with <name : action_dict>
    key value pairs.
    The keys in the inner action dictionaries should be the other inputs to 
    ToolAction.__init__
    """
def bindStateParameters(actions: Collection[ToolAction[_ToolT, object]], template: hou.ViewerStateTemplate) -> None:
    """
    Binds the provided actions as state parameters.
    """
def bindActionMenu(name: str, label: str, actions: Iterable[ToolAction[_ToolT, object]], menu: hou.ViewerStateMenu, hotkeys: Hotkeys) -> None:
    """
    Binds an action sub-menu to the viewer state right click menu, adding the
    given actions as individual entries.
    """
def executeAction(tool: _ToolT, actions: Iterable[ToolAction[_ToolT, object]], name: str, *args: object, **kwargs: object) -> bool:
    """
    Given a list of actions, a tool, and an action name, this will find the
    matching action in the list and execute it.
    This returns True if and only if the action was found.
    """
def getToolActionList(actions: Iterable[ToolAction[_ToolT, object]], menu_name: str | None = None) -> list[str]:
    """
    Returns a list of the names of the given actions.
    If `menu_name` is not None, it will be appended to the list.
    """
