from collections.abc import Callable as Callable, Sequence
from typing import TypedDict

from typing import TypeVar
from typing import TypeVar
_T1 = TypeVar('_T1')
_T2 = TypeVar('_T2')
class _VideoKwargs(TypedDict):
    imagefiles: Sequence[str]
    framerate: float

def run(args: Sequence[str], suppresswindow: bool = True) -> tuple[int, tuple[str, str]]:
    """ Run an external program, returning an (exit_code, (stdout, stderr))
        tuple, where stdout and stderr are strings whose contents match those
        of the standard output and standard error file handles, respectively.

        args is a sequence of program arguments, the program to execute being
        the first itsem in the sequence.
    """
def runAsynchronous(args: Sequence[str], suppresswindow: bool = True, stdoutcallback: tuple[Callable[[str, _T1], object], _T1] | None = None, stderrcallback: tuple[Callable[[str, _T2], object], _T2] | None = None) -> tuple[int, tuple[str, str]]:
    """ Run an external program, returning an (exit_code, (stdout, stderr))
        tuple, where stdout and stderr are strings whose contents match those
        of the standard output and standard error file handles, respectively.

        args is a sequence of program arguments, the program to execute being
        the first itsem in the sequence.

        stdoutcallback and stderrcallback are 2-tuples of the form (func, data).
        The callback function is called as func(line, data) where line is the
        next line extracted from the respective pipe.  Each callback function
        is processed within its own thread.
    """
def videoDuration(kwargs: _VideoKwargs) -> float:
    """ Returns the duration of the input image files in seconds.
    """
