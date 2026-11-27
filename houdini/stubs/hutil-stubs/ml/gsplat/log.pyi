from _typeshed import SupportsWrite
from collections.abc import Iterable, Iterator, Mapping
from types import TracebackType
from typing import Literal, NotRequired, Self, TextIO, TypedDict, Unpack

class _LogState(TypedDict):
    log_to_standard_output: bool
    log_file: TextIO | None
    _reopen_path: NotRequired[str]
    _reopen_encoding: NotRequired[str]

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
    """
    A file-like object that writes to both the original stdout and a log file.

    Use as a context manager to temporarily capture all stdout (including from
    external libraries that use print()) and tee it to the log file.

    Usage:
        with TeeStdout(log_file):
            # All print() calls in this block will also go to log_file
            some_library_function_that_prints()
    """
    log_file: TextIO | None
    original_stdout: TextIO
    log_to_standard_output: bool
    def __init__(self, log_file: TextIO | None, original_stdout: TextIO | None = None, log_to_standard_output: bool = True) -> None: ...
    def write(self, s: str) -> None: ...
    def flush(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> Literal[False]: ...

class Log:
    log_to_standard_output: bool
    log_file: TextIO | None
    def __init__(self, /, *, log_to_standard_output: bool = False, log_file: TextIO | None = None) -> None: ...
    def write(self, s: str, quiet: bool = False) -> None: ...
    def flush(self) -> None: ...

class Fail:
    """Utility to handle early exit after failure with logging."""
    def __init__(self, log: Log | None) -> None: ...
    def __call__(self, message: str) -> None: ...

class LoggedTqdm:
    '''
    A tqdm wrapper that logs progress as individual lines.

    When a Log instance is provided, disables tqdm\'s visual progress bar
    (which uses carriage returns) and instead outputs each update as a
    separate line. This avoids display issues in log viewers like Houdini\'s
    that don\'t interpret carriage returns.

    Usage:
        logged_pbar = LoggedTqdm(range(1000), log=logger, log_every=100)
        for step in logged_pbar:
            # do work
            logged_pbar.set_description(f"loss={loss:.3f}")
    '''
    def __init__(self, iterable: Iterable[int] | None = None, log: Log | None = None, log_every: int = 100, log_on_complete: bool = True, **tqdm_kwargs: Unpack[_TqdmKwargs]) -> None:
        """
        Initialize the logged tqdm wrapper.

        Parameters
        ----------
        iterable : iterable, optional
            Iterable to wrap (passed to tqdm)
        log : Log, optional
            Log instance for logging. When provided, disables tqdm's visual
            output and uses line-by-line logging instead.
        log_every : int
            Log progress every N iterations (default: 100)
        log_on_complete : bool
            Whether to log final status on completion (default: True)
        **tqdm_kwargs
            Additional arguments passed to tqdm.tqdm
        """
    def __iter__(self) -> Iterator[int]: ...
    def set_description(self, desc: str) -> None:
        """Set the description for logging."""
    def update(self, n: float = 1) -> None:
        """Update the progress bar."""
    def close(self) -> None:
        """Close the progress bar."""
    @property
    def n(self) -> float:
        """Current iteration count."""

def logged_trange(*args: int, log: Log | None = None, log_every: int = 100, log_on_complete: bool = True, **kwargs: Unpack[_TqdmKwargs]) -> LoggedTqdm:
    '''
    Shorthand for LoggedTqdm(range(*args), ...).

    Usage:
        for i in logged_trange(100, log=logger, desc="Processing"):
            # do work
    '''
