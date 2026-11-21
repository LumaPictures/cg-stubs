import typing
from collections.abc import Callable as Callable
from typing import Generic, NotRequired, TypedDict, Unpack

from typing import TypeVar
from typing import TypeVar
_D = TypeVar('_D')
class _CommandArgs(TypedDict, Generic[_D]):
    cmd_func: Callable[[int, _D], object]
    label: NotRequired[str]
    tag: NotRequired[str | None]
    data: _D

class _CommandArgsNoData(TypedDict, Generic[_D]):
    cmd_func: Callable[[int, _D | None], object]
    label: NotRequired[str]
    tag: NotRequired[str | None]

class _DoArgs(TypedDict, Generic[_D], total=False):
    data: _D
    label: str
    tag: str | None

class Command(Generic[_D]):
    """ Class utility for implementing undoable functionality. 
        The user provides a single function for the undo/redo 
        implementation, the class takes care of interfacing with 
        Houdini for undo/redo.        
    """
    DO: int
    UNDO: int
    REDO: int
    @typing.overload
    def __init__(self, **kwargs: Unpack[_CommandArgs[_D]]) -> None: ...
    @typing.overload
    def __init__(self, **kwargs: Unpack[_CommandArgsNoData[_D]]) -> None: ...
    def data(self) -> _D | None: ...
    def label(self) -> str: ...
    def tag(self) -> str | None: ...
    def do(self, add_undo: bool = True, **kwargs: Unpack[_DoArgs[_D]]) -> None:
        """ Client must call do() to execute the Command.
        """
    def run(self, use_state: bool = False, **kwargs: Unpack[_DoArgs[_D]]) -> None:
        """ If use_state is True, the command is executed based on its 
            current state. If False, the do part is executed.
        """
    def undo(self) -> None: ...
    def redo(self) -> None: ...
