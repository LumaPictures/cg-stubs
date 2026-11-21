# Houdini stubs generated from Houdini 22.0.466

import inspect
import subprocess
import typing
import weakref
from collections.abc import Callable
from types import ModuleType
from typing import Any, Generic, Literal
from typing_extensions import TypeIs

from typing import TypeVar
from typing import TypeVar
_C = TypeVar('_C', bound=Callable[..., object])
_R = TypeVar('_R')
def isPy3() -> bool:
    """Return True if code is executing in a Python 3 environment and False
       otherwise."""
def isString(obj: object) -> TypeIs[str]:
    """Return True if the specified object is a string type and False
       otherwise."""
def reload(module: ModuleType) -> None: ...
def perfCounter() -> float: ...

unicodeType: type[str]

def subprocessCall(*args: Any, **kwargs: Any) -> int: ...
@typing.overload
def subprocessPopen(*args: Any, text: Literal[False], **kwargs: Any) -> subprocess.Popen[bytes]: ...
@typing.overload
def subprocessPopen(*args: Any, text: Literal[True] = ..., **kwargs: Any) -> subprocess.Popen[str]: ...
@typing.overload
def subprocessPopen(*args: Any, text: bool, **kwargs: Any) -> subprocess.Popen[str] | subprocess.Popen[bytes]: ...
def getfullargspec(obj: Callable[..., object]) -> inspect.FullArgSpec: ...

class _weak_callable(Generic[_R]):
    im_self: Any | None
    im_func: Callable[..., _R]
    def __init__(self, obj: object | None, func: Callable[..., _R]) -> None: ...
    def __call__(self, *args: object, **kws: object) -> _R: ...

class WeakMethod(Generic[_R]):
    def __init__(self, fn: Callable[..., _R]) -> None: ...
    def __call__(self) -> _weak_callable[_R] | None: ...

def weakMethod(func: _C) -> weakref.WeakMethod[_C]: ...
