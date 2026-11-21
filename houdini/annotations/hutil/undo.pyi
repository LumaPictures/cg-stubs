from collections.abc import Callable
from typing import Generic, NotRequired, TypedDict, TypeVar, Unpack, overload

_D = TypeVar("_D")

# cmd_func is called with the undo state (DO, UNDO or REDO) and the command's data.
class _CommandArgs(TypedDict, Generic[_D]):
    cmd_func: Callable[[int, _D], object]
    label: NotRequired[str]
    tag: NotRequired[str | None]
    data: _D

# Without data, cmd_func gets None until do() or run() is given some.
class _CommandArgsNoData(TypedDict, Generic[_D]):
    cmd_func: Callable[[int, _D | None], object]
    label: NotRequired[str]
    tag: NotRequired[str | None]

class _DoArgs(TypedDict, Generic[_D], total=False):
    data: _D
    label: str
    tag: str | None

class Command(Generic[_D]):
    DO: int
    UNDO: int
    REDO: int
    @overload
    def __init__(self, **kwargs: Unpack[_CommandArgs[_D]]) -> None: ...
    @overload
    def __init__(self, **kwargs: Unpack[_CommandArgsNoData[_D]]) -> None: ...
    def data(self) -> _D | None: ...
    def label(self) -> str: ...
    def tag(self) -> str | None: ...
    def do(self, add_undo: bool = ..., **kwargs: Unpack[_DoArgs[_D]]) -> None: ...
    def run(self, use_state: bool = ..., **kwargs: Unpack[_DoArgs[_D]]) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...
