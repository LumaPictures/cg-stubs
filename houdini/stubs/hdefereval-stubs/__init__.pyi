import typing
from collections.abc import Callable as Callable, Iterator
from types import CodeType
from typing import Any

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_T = TypeVar('_T')
@typing.overload
def executeDeferred(code: Callable[_P, object], *args: _P.args, **kwargs: _P.kwargs) -> None: ...
@typing.overload
def executeDeferred(code: str | CodeType) -> None: ...
execute_deferred = executeDeferred

@typing.overload
def executeDeferredAfterWaiting(code: Callable[_P, object], num_waits: int, *args: _P.args, **kwargs: _P.kwargs) -> None: ...
@typing.overload
def executeDeferredAfterWaiting(code: str | CodeType, num_waits: int) -> None: ...
execute_deferred_after_waiting = executeDeferredAfterWaiting

@typing.overload
def executeInMainThreadWithResult(code: Callable[_P, _T], *args: _P.args, **kwargs: _P.kwargs) -> _T: ...
@typing.overload
def executeInMainThreadWithResult(code: str | CodeType) -> Any: ...
execute_in_main_thread_with_result = executeInMainThreadWithResult

def in_separate_thread(function: Callable[_P, object]) -> Callable[_P, None]:
    """This decorator marks a function as running in a new thread.  Calling
    the function will automatically start a new thread that runs the
    undecorated version.
    """
inSeparateThread = in_separate_thread

def do_work_in_background_thread(function: Callable[_P, Iterator[object]]) -> Callable[_P, None]:
    '''This decorator marks a generator function as alternating its execution
    between the main thread and a new thread.  The intial code is run in
    the current thread until it yields, the next piece of code is run in a
    new thread until it yields, and the next code is run in the main thread.
    More pairs of worker thread/main thread blocks may be added at the end.

    Here is an example:
    @do_work_in_background_thread
    def func():
        print "initializing in main thread"
        yield

        print "computing result in other thread"
        result = 3
        yield

        print "processing result in main thread", result
    '''
doWorkInBackgroundThread = do_work_in_background_thread
