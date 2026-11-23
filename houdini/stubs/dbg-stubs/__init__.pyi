import dbg
import os
import types
import typing
from collections.abc import Callable as Callable, Iterable
from typing import Any, Protocol

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
class _Decorator(Protocol):
    def __call__(self, func: Callable[_P, _R], /) -> Callable[_P, _R]: ...

class _FilePrinter(Protocol):
    def __call__(self, *args: object, sep: str = ..., end: str = ...) -> None: ...

SHOW_CALLER: bool
SHOW_CLASS: bool

def formatFrame(current_frame: types.FrameType) -> str: ...
def msg(*args: object, frame: types.FrameType | None = None) -> None:
    """Outputs a message, prepending the file name, line number, and
       containing function."""
def trace(*args: object, frame: types.FrameType | None = None) -> None:
    """ Prints out the given arguments like msg() and then also outputs a stack
    """
def trace_exc(*args: object, frame: types.FrameType | None = None) -> None:
    """ Prints out the given arguments like msg() and then also outputs a stack
    """

PDB_ASSERTS: int
INIT_PDBPP_PATH: int
PDBPP_PATH: str

def initpdbpp() -> None:
    """Initialize the python path with a PDB++ path"""
def hassert(cond: object, msg: str = 'hassert') -> None:
    """Break in the python debugger if the condition is false"""

class DbgPrinter:
    """Debug printer object that can be enabled or disabled with an env var"""
    enabled: bool
    def __init__(self, enable_env: str = '') -> None:
        '''`enable_env` - (optional) Env variable that when set to "1" will
                          enable messages from this debug print object,
                          otherwise messages will be disabled.
                          Default is messages always enabled.'''
    def msg(self, *args: object) -> None:
        """Outputs a message, prepending the file name, line number, and
           containing function."""
    def trace(self, *args: object) -> None:
        """ Prints out the given arguments like msg() and then also outputs a stack
        """
    def trace_exc(self, *args: object) -> None:
        """ Prints out the given arguments like msg() and then also outputs a stack
        """

@typing.overload
def log(e: Callable[_P, _R], c: str | list[str] | None = ..., *, pr: Callable[[str], object] = ..., p: bool | int = ..., s: int = ..., o: str | Iterable[object] | None = ...) -> Callable[_P, _R]: ...
@typing.overload
def log(e: bool | int = ..., c: str | list[str] | None = ..., *, pr: Callable[[str], object] = ..., p: bool | int = ..., s: int = ..., o: str | Iterable[object] | None = ...) -> _Decorator: ...
def makeFilePrinter(path: str | os.PathLike[str], mode: str = 'a', flush: bool = True, encoding: str = 'utf-8') -> _FilePrinter:
    '''Return a print-like function that writes to a file.

    The returned callable is suitable for dbg.log\'s `pr=` argument.

    Args:
        path (str): Output file path.
        mode (str): File open mode, usually "a" (append) or "w" (overwrite).
        flush (bool): If True, flush after each call.
        encoding (str): File encoding.

    Returns:
        callable: fn(*args, sep=" ", end="\\n") -> None
    '''

DBG_ZONE_SCOPES: int

class ZoneScopedImpl:
    name: str
    text: str
    ctx: Any
    def __init__(self, n: str, text: str | None = None) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...

def ZoneScopedDecoratorImpl(func: Callable[_P, _R]) -> Callable[_P, _R]: ...

class ZoneScopedNoop:
    def __init__(self, n: str) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, tb: types.TracebackType | None) -> None: ...

def ZoneScopedDecoratorNoop(func: Callable[_P, _R]) -> Callable[_P, _R]: ...

ZoneScoped: type[ZoneScopedImpl] | type[ZoneScopedNoop]
ZoneScopedDecorator: _Decorator
ZoneScoped = ZoneScopedNoop
ZoneScopedDecorator = ZoneScopedDecoratorNoop
