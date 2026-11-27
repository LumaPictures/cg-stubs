from _typeshed import SupportsWrite
from collections.abc import Iterable, Iterator, Mapping
from types import TracebackType
from typing import Any, Literal, NotRequired, Self, TextIO, TypedDict, Unpack, type_check_only

# What __setstate__ unpickles: an open log file is replaced by how to reopen it.
@type_check_only
class _LogState(TypedDict):
    log_to_standard_output: bool
    log_file: TextIO | None
    _reopen_path: NotRequired[str]
    _reopen_encoding: NotRequired[str]

# The keywords tqdm.tqdm accepts after its iterable.
@type_check_only
class _TqdmKwargs(TypedDict, total=False):
    desc: str | None
    total: float | None
    leave: bool | None
    file: SupportsWrite[str] | None
    ncols: int | None
    mininterval: float
    maxinterval: float
    miniters: float | None
    ascii: bool | str | None
    disable: bool | None
    unit: str
    unit_scale: bool | float
    dynamic_ncols: bool
    smoothing: float
    bar_format: str | None
    initial: float
    position: int | None
    postfix: Mapping[str, object] | str | None
    unit_divisor: float
    write_bytes: bool
    lock_args: tuple[bool | None, float | None] | tuple[bool | None] | None
    nrows: int | None
    colour: str | None
    delay: float | None
    gui: bool


class TeeStdout:
    log_file: TextIO | None
    original_stdout: TextIO
    log_to_standard_output: bool
    def __init__(self, log_file: TextIO | None, original_stdout: TextIO | None = ..., log_to_standard_output: bool = ...) -> None: ...
    def write(self, s: str) -> None: ...
    def flush(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> Literal[False]: ...

class Log:
    log_to_standard_output: bool
    log_file: TextIO | None
    def __init__(self, /, *, log_to_standard_output: bool = ..., log_file: TextIO | None = ...) -> None: ...
    def __getstate__(self) -> dict[str, Any]: ...
    def __setstate__(self, state: _LogState) -> None: ...
    def write(self, s: str, quiet: bool = ...) -> None: ...
    def flush(self) -> None: ...

class Fail:
    def __init__(self, log: Log | None) -> None: ...
    def __call__(self, message: str) -> None: ...

class LoggedTqdm:
    def __init__(self, iterable: Iterable[int] | None = ..., log: Log | None = ..., log_every: int = ..., log_on_complete: bool = ..., **tqdm_kwargs: Unpack[_TqdmKwargs]) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def set_description(self, desc: str) -> None: ...
    def update(self, n: float = ...) -> None: ...
    def close(self) -> None: ...
    @property
    def n(self) -> float: ...

def logged_trange(*args: int, log: Log | None = ..., log_every: int = ..., log_on_complete: bool = ..., **kwargs: Unpack[_TqdmKwargs]) -> LoggedTqdm: ...
