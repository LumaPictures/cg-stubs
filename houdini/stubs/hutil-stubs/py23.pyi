import inspect
import subprocess
import typing
import weakref
from _typeshed import StrOrBytesPath as StrOrBytesPath
from collections.abc import Callable, Collection, Iterable, Mapping
from subprocess import _CMD, _FILE
from types import ModuleType
from typing import Generic, Literal
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

@typing.overload
def subprocessCall(args: _CMD, /, bufsize: int = ..., executable: StrOrBytesPath | None = ..., stdin: _FILE = ..., stdout: _FILE = ..., stderr: _FILE = ..., preexec_fn: Callable[[], object] | None = ..., close_fds: bool = ..., shell: bool = ..., cwd: StrOrBytesPath | None = ..., env: Mapping[str, str] | None = ..., universal_newlines: bool | None = ..., startupinfo: object = ..., creationflags: int = ..., restore_signals: bool = ..., start_new_session: bool = ..., pass_fds: Collection[int] = ..., *, timeout: float | None = ..., text: bool | None = ..., encoding: str | None = ..., user: str | int | None = ..., group: str | int | None = ..., extra_groups: Iterable[str | int] | None = ..., umask: int = ..., pipesize: int = ..., process_group: int | None = ...) -> int: ...
@typing.overload
def subprocessCall(*, args: _CMD, bufsize: int = ..., executable: StrOrBytesPath | None = ..., stdin: _FILE = ..., stdout: _FILE = ..., stderr: _FILE = ..., preexec_fn: Callable[[], object] | None = ..., close_fds: bool = ..., shell: bool = ..., cwd: StrOrBytesPath | None = ..., env: Mapping[str, str] | None = ..., universal_newlines: bool | None = ..., startupinfo: object = ..., creationflags: int = ..., restore_signals: bool = ..., start_new_session: bool = ..., pass_fds: Collection[int] = ..., timeout: float | None = ..., text: bool | None = ..., encoding: str | None = ..., user: str | int | None = ..., group: str | int | None = ..., extra_groups: Iterable[str | int] | None = ..., umask: int = ..., pipesize: int = ..., process_group: int | None = ...) -> int: ...
@typing.overload
def subprocessPopen(args: _CMD, bufsize: int = ..., executable: StrOrBytesPath | None = ..., stdin: _FILE = ..., stdout: _FILE = ..., stderr: _FILE = ..., preexec_fn: Callable[[], object] | None = ..., close_fds: bool = ..., shell: bool = ..., cwd: StrOrBytesPath | None = ..., env: Mapping[str, str] | None = ..., universal_newlines: Literal[False] | None = ..., startupinfo: object = ..., creationflags: int = ..., restore_signals: bool = ..., start_new_session: bool = ..., pass_fds: Collection[int] = ..., *, text: Literal[False], encoding: None = ..., errors: None = ..., user: str | int | None = ..., group: str | int | None = ..., extra_groups: Iterable[str | int] | None = ..., umask: int = ..., pipesize: int = ..., process_group: int | None = ...) -> subprocess.Popen[bytes]: ...
@typing.overload
def subprocessPopen(args: _CMD, bufsize: int = ..., executable: StrOrBytesPath | None = ..., stdin: _FILE = ..., stdout: _FILE = ..., stderr: _FILE = ..., preexec_fn: Callable[[], object] | None = ..., close_fds: bool = ..., shell: bool = ..., cwd: StrOrBytesPath | None = ..., env: Mapping[str, str] | None = ..., universal_newlines: bool | None = ..., startupinfo: object = ..., creationflags: int = ..., restore_signals: bool = ..., start_new_session: bool = ..., pass_fds: Collection[int] = ..., *, text: Literal[True] = ..., encoding: str | None = ..., errors: str | None = ..., user: str | int | None = ..., group: str | int | None = ..., extra_groups: Iterable[str | int] | None = ..., umask: int = ..., pipesize: int = ..., process_group: int | None = ...) -> subprocess.Popen[str]: ...
@typing.overload
def subprocessPopen(args: _CMD, bufsize: int = ..., executable: StrOrBytesPath | None = ..., stdin: _FILE = ..., stdout: _FILE = ..., stderr: _FILE = ..., preexec_fn: Callable[[], object] | None = ..., close_fds: bool = ..., shell: bool = ..., cwd: StrOrBytesPath | None = ..., env: Mapping[str, str] | None = ..., universal_newlines: bool | None = ..., startupinfo: object = ..., creationflags: int = ..., restore_signals: bool = ..., start_new_session: bool = ..., pass_fds: Collection[int] = ..., *, text: bool | None, encoding: str | None = ..., errors: str | None = ..., user: str | int | None = ..., group: str | int | None = ..., extra_groups: Iterable[str | int] | None = ..., umask: int = ..., pipesize: int = ..., process_group: int | None = ...) -> subprocess.Popen[str] | subprocess.Popen[bytes]: ...
def getfullargspec(obj: Callable[..., object]) -> inspect.FullArgSpec: ...

class _weak_callable(Generic[_R]):
    im_self: object | None
    im_func: Callable[..., _R]
    def __init__(self, obj: object | None, func: Callable[..., _R]) -> None: ...
    def __call__(self, *args: object, **kws: object) -> _R: ...

class WeakMethod(Generic[_R]):
    def __init__(self, fn: Callable[..., _R]) -> None: ...
    def __call__(self) -> _weak_callable[_R] | None: ...

def weakMethod(func: _C) -> weakref.WeakMethod[_C]: ...
