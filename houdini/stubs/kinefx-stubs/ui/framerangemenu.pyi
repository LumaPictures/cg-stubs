import typing
from collections.abc import Callable as Callable, Iterable
from houtypes import ParmActionButtonKwargs
from typing import Generic

from typing import TypeVar
from typing import TypeVar
_K = TypeVar('_K')
class FrameRangeMenuEntry(Generic[_K]):
    """
    Custom object for referecing components like name, icon and callback more easily in frameRangeMenu
    """
    name: str
    icon: str | None
    cb: Callable[[_K], object]
    def __init__(self, name: str, icon: str | None, cb: Callable[[_K], object]) -> None: ...

def frameRangeMenuBuiltinEntries() -> list[FrameRangeMenuEntry[ParmActionButtonKwargs]]:
    """
    Build the menu entries for frameRangeMenu
    """
@typing.overload
def frameRangeMenu(kwargs: ParmActionButtonKwargs, builtin_entries_func: Callable[[], Iterable[FrameRangeMenuEntry[ParmActionButtonKwargs]]] = ...) -> None: ...
@typing.overload
def frameRangeMenu(kwargs: _K, builtin_entries_func: Callable[[], Iterable[FrameRangeMenuEntry[_K]]]) -> None: ...
