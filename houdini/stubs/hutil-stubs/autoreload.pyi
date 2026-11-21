import logging
import threading
from collections import defaultdict
from collections.abc import Callable as Callable, Iterable, Iterator
from pathlib import Path
from types import ModuleType
from typing import NoReturn

from typing import ParamSpec
from typing import TypeVar
from typing import TypeVarTuple
from typing import ParamSpec
from typing import TypeVar
from typing import TypeVarTuple
_P = ParamSpec('_P')
_T = TypeVar('_T')
_Ts = TypeVarTuple('_Ts')
AUTORELOAD_ENV: str
logger: logging.Logger

def check_errors(function: Callable[_P, object]) -> Callable[_P, None]: ...
def ensure_echo_on() -> None:
    """
    Ensure that echo mode is enabled. Some tools such as PDB disable
    it which causes usability issues after reload.
    """
def iter_all_python_module_files() -> frozenset[str]: ...
def cache_last_call(function: Callable[[*_Ts], _T]) -> Callable[[*_Ts], _T]: ...
@cache_last_call
def iter_modules_and_files(modules: Iterable[ModuleType], extra_files: Iterable[str]) -> frozenset[str]:
    """Iterate through all modules needed to be watched."""
def get_child_arguments() -> list[str | None]:
    """
    Return the executable. This contains a workaround for Windows if the
    executable is reported to not have the .exe extension which can cause bugs
    on reloading.
    """
def get_sys_executable() -> str | None: ...
def restart_with_reloader() -> int: ...

class StatReloader:
    main_thread: threading.Thread
    extra_files: set[str | Path]
    directory_globs: defaultdict[Path, set[str]]
    SLEEP_TIME: int
    def __init__(self, main_thread: threading.Thread) -> None: ...
    def watched_files(self, include_globs: bool = True) -> Iterator[str | Path]:
        """
        Yield all files that need to be watched, including module files and
        files within globs.
        """
    def run(self) -> None: ...
    def notify_file_changed(self, path: str | Path) -> NoReturn: ...
    def tick(self) -> Iterator[None]:
        """
        This generator is called in a loop from run. It's important that the
        method takes care of pausing or otherwise waiting for a period of time.
        This split between run() and tick() is to improve the testability of
        the reloader implementations by decoupling the work they do from the
        loop.
        """
    def snapshot_files(self) -> Iterator[tuple[str | Path, float]]: ...
    @property
    def should_stop(self) -> bool: ...
    def stop(self) -> None: ...

def start_server(main_func: Callable[_P, object], *args: _P.args, **kwargs: _P.kwargs) -> None: ...
def run_with_reloader(main_func: Callable[_P, object], *args: _P.args, **kwargs: _P.kwargs) -> None: ...
