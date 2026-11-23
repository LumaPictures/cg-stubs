from collections.abc import Callable, Sequence
from typing import TypedDict, TypeVar

# The parts of mplay's movie export kwargs (scripts/mvexport/*.py) that videoDuration reads.
class _VideoKwargs(TypedDict):
    imagefiles: Sequence[str]
    framerate: float

_T1 = TypeVar("_T1")
_T2 = TypeVar("_T2")

def run(args: Sequence[str], suppresswindow: bool = ...) -> tuple[int, tuple[str, str]]: ...
def runAsynchronous(
    args: Sequence[str],
    suppresswindow: bool = ...,
    stdoutcallback: tuple[Callable[[str, _T1], object], _T1] | None = ...,
    stderrcallback: tuple[Callable[[str, _T2], object], _T2] | None = ...,
) -> tuple[int, tuple[str, str]]: ...
def videoDuration(kwargs: _VideoKwargs) -> float: ...
