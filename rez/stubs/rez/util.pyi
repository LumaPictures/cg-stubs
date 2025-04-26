import _io
import atexit
from _typeshed import Incomplete
from collections.abc import Generator
from rez.exceptions import RezError as RezError
from rez.vendor.progress.bar import Bar as Bar  # type: ignore[import-not-found]
from typing import Iterable, TypeGuard, TypeVar

T = TypeVar('T')

class ProgressBar(Bar):
    file: _io.TextIOWrapper[_io._WrappedBuffer]
    close_file: bool
    hide_cursor: bool
    def __init__(self, label, max) -> None: ...
    def __del__(self) -> None: ...

def dedup(seq) -> Generator[Incomplete]:
    """Remove duplicates from a list while keeping order."""

_find_unsafe: Incomplete

def shlex_join(value: Iterable[str], unsafe_regex: Incomplete | None = None, replacements: Incomplete | None = None, enclose_with: str = '"'):
    """Join args into a valid shell command.
    """
def which(*programs, **shutilwhich_kwargs): ...
def get_close_matches(term, fields, fuzziness: float = 0.4, key: Incomplete | None = None): ...
def get_close_pkgs(pkg, pkgs, fuzziness: float = 0.4): ...
def find_last_sublist(list_, sublist):
    """Given a list, find the last occurance of a sublist within it.

    Returns:
        Index where the sublist starts, or None if there is no match.
    """
@atexit.register
def _atexit() -> None: ...
def is_non_string_iterable(arg: str | Iterable[str] | None) -> TypeGuard[Iterable[str]]:
    """Python 2 and 3 compatible non-string iterable identifier"""
def get_function_arg_names(func):
    """Get names of a function's args.

    Gives full list of positional and keyword-only args.
    """
def load_module_from_file(name: str, filepath: str):
    """Load a python module from a sourcefile.

    Args:
        name (str): Module name.
        filepath (str): Python sourcefile.

    Returns:
        `module`: Loaded module.
    """
