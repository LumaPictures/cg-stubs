import inspect
import subprocess
import weakref
from _typeshed import StrOrBytesPath
from collections.abc import Callable, Collection, Iterable, Mapping
from types import ModuleType
from subprocess import _CMD, _FILE
from typing import Any, Generic, Literal, TypeVar, overload
from typing_extensions import TypeIs

_C = TypeVar("_C", bound=Callable[..., object])
_R = TypeVar("_R")

unicodeType: type[str]

def isPy3() -> bool: ...
def isString(obj: object) -> TypeIs[str]: ...
def reload(module: ModuleType) -> None: ...
def perfCounter() -> float: ...
@overload
def subprocessCall(
    args: _CMD,
    /,
    bufsize: int = ...,
    executable: StrOrBytesPath | None = ...,
    stdin: _FILE = ...,
    stdout: _FILE = ...,
    stderr: _FILE = ...,
    preexec_fn: Callable[[], object] | None = ...,
    close_fds: bool = ...,
    shell: bool = ...,
    cwd: StrOrBytesPath | None = ...,
    env: Mapping[str, str] | None = ...,
    universal_newlines: bool | None = ...,
    startupinfo: object = ...,
    creationflags: int = ...,
    restore_signals: bool = ...,
    start_new_session: bool = ...,
    pass_fds: Collection[int] = ...,
    *,
    timeout: float | None = ...,
    text: bool | None = ...,
    encoding: str | None = ...,
    user: str | int | None = ...,
    group: str | int | None = ...,
    extra_groups: Iterable[str | int] | None = ...,
    umask: int = ...,
    pipesize: int = ...,
    process_group: int | None = ...,
) -> int: ...
@overload
def subprocessCall(
    *,
    args: _CMD,
    bufsize: int = ...,
    executable: StrOrBytesPath | None = ...,
    stdin: _FILE = ...,
    stdout: _FILE = ...,
    stderr: _FILE = ...,
    preexec_fn: Callable[[], object] | None = ...,
    close_fds: bool = ...,
    shell: bool = ...,
    cwd: StrOrBytesPath | None = ...,
    env: Mapping[str, str] | None = ...,
    universal_newlines: bool | None = ...,
    startupinfo: object = ...,
    creationflags: int = ...,
    restore_signals: bool = ...,
    start_new_session: bool = ...,
    pass_fds: Collection[int] = ...,
    timeout: float | None = ...,
    text: bool | None = ...,
    encoding: str | None = ...,
    user: str | int | None = ...,
    group: str | int | None = ...,
    extra_groups: Iterable[str | int] | None = ...,
    umask: int = ...,
    pipesize: int = ...,
    process_group: int | None = ...,
) -> int: ...
def subprocessCall(*args: Any, **kwargs: Any) -> int: ...
@overload
def subprocessPopen(
    args: _CMD,
    bufsize: int = ...,
    executable: StrOrBytesPath | None = ...,
    stdin: _FILE = ...,
    stdout: _FILE = ...,
    stderr: _FILE = ...,
    preexec_fn: Callable[[], object] | None = ...,
    close_fds: bool = ...,
    shell: bool = ...,
    cwd: StrOrBytesPath | None = ...,
    env: Mapping[str, str] | None = ...,
    universal_newlines: Literal[False] | None = ...,
    startupinfo: object = ...,
    creationflags: int = ...,
    restore_signals: bool = ...,
    start_new_session: bool = ...,
    pass_fds: Collection[int] = ...,
    *,
    text: Literal[False],
    encoding: None = ...,
    errors: None = ...,
    user: str | int | None = ...,
    group: str | int | None = ...,
    extra_groups: Iterable[str | int] | None = ...,
    umask: int = ...,
    pipesize: int = ...,
    process_group: int | None = ...,
) -> subprocess.Popen[bytes]: ...
@overload
def subprocessPopen(
    args: _CMD,
    bufsize: int = ...,
    executable: StrOrBytesPath | None = ...,
    stdin: _FILE = ...,
    stdout: _FILE = ...,
    stderr: _FILE = ...,
    preexec_fn: Callable[[], object] | None = ...,
    close_fds: bool = ...,
    shell: bool = ...,
    cwd: StrOrBytesPath | None = ...,
    env: Mapping[str, str] | None = ...,
    universal_newlines: bool | None = ...,
    startupinfo: object = ...,
    creationflags: int = ...,
    restore_signals: bool = ...,
    start_new_session: bool = ...,
    pass_fds: Collection[int] = ...,
    *,
    text: Literal[True] = ...,
    encoding: str | None = ...,
    errors: str | None = ...,
    user: str | int | None = ...,
    group: str | int | None = ...,
    extra_groups: Iterable[str | int] | None = ...,
    umask: int = ...,
    pipesize: int = ...,
    process_group: int | None = ...,
) -> subprocess.Popen[str]: ...
@overload
def subprocessPopen(
    args: _CMD,
    bufsize: int = ...,
    executable: StrOrBytesPath | None = ...,
    stdin: _FILE = ...,
    stdout: _FILE = ...,
    stderr: _FILE = ...,
    preexec_fn: Callable[[], object] | None = ...,
    close_fds: bool = ...,
    shell: bool = ...,
    cwd: StrOrBytesPath | None = ...,
    env: Mapping[str, str] | None = ...,
    universal_newlines: bool | None = ...,
    startupinfo: object = ...,
    creationflags: int = ...,
    restore_signals: bool = ...,
    start_new_session: bool = ...,
    pass_fds: Collection[int] = ...,
    *,
    text: bool | None,
    encoding: str | None = ...,
    errors: str | None = ...,
    user: str | int | None = ...,
    group: str | int | None = ...,
    extra_groups: Iterable[str | int] | None = ...,
    umask: int = ...,
    pipesize: int = ...,
    process_group: int | None = ...,
) -> subprocess.Popen[str] | subprocess.Popen[bytes]: ...
def subprocessPopen(*args: Any, **kwargs: Any) -> subprocess.Popen[str] | subprocess.Popen[bytes]: ...
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
