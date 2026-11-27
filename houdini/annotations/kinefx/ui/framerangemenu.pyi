from collections.abc import Callable, Iterable
from typing import Generic, TypeVar, overload

from houtypes import ParmActionButtonKwargs

_K = TypeVar("_K")

class FrameRangeMenuEntry(Generic[_K]):
    name: str
    icon: str | None
    cb: Callable[[_K], object]
    def __init__(self, name: str, icon: str | None, cb: Callable[[_K], object]) -> None: ...

def frameRangeMenuBuiltinEntries() -> list[FrameRangeMenuEntry[ParmActionButtonKwargs]]: ...

# The menu passes kwargs to the chosen entry's callback; the builtin entries set a frame range
# parameter tuple from an action button's kwargs (and inputindex, if a script set it).
@overload
def frameRangeMenu(
    kwargs: ParmActionButtonKwargs,
    builtin_entries_func: Callable[[], Iterable[FrameRangeMenuEntry[ParmActionButtonKwargs]]] = ...,
) -> None: ...
@overload
def frameRangeMenu(kwargs: _K, builtin_entries_func: Callable[[], Iterable[FrameRangeMenuEntry[_K]]]) -> None: ...
def frameRangeMenu(kwargs: _K, builtin_entries_func: Callable[[], Iterable[FrameRangeMenuEntry[_K]]] = ...) -> None: ...
