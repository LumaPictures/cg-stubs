from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from enum import Enum
from rez.config import config as config
from rez.exceptions import InvalidPackageError as InvalidPackageError, ResourceError as ResourceError
from rez.package_resources import package_rex_keys as package_rex_keys
from rez.util import get_function_arg_names as get_function_arg_names
from rez.utils.data_utils import ModifyList as ModifyList
from rez.utils.execution import add_sys_paths as add_sys_paths
from rez.utils.filesystem import TempDirs as TempDirs
from rez.utils.memcached import memcached as memcached
from rez.utils.scope import ScopeContext as ScopeContext
from rez.utils.sourcecode import SourceCode as SourceCode, early as early, include as include, late as late
from rez.vendor import yaml as yaml  # type: ignore[import-not-found]
from rez.vendor.atomicwrites import atomic_write as atomic_write  # type: ignore[import-not-found]
from typing import Any

tmpdir_manager: Incomplete
debug_print: Incomplete
file_cache: Incomplete

class FileFormat(Enum):
    py = ('py',)
    yaml = ('yaml',)
    txt = ('txt',)
    __order__ = 'py,yaml,txt'
    extension: Any
    def __init__(self, extension) -> None: ...

@contextmanager
def open_file_for_write(filepath, mode: Incomplete | None = None) -> Generator[Incomplete]:
    """Writes both to given filepath, and tmpdir location.

    This is to get around the problem with some NFS's where immediately reading
    a file that has just been written is problematic. Instead, any files that we
    write, we also write to /tmp, and reads of these files are redirected there.

    Args:
        filepath (str): File to write.
        mode (int): Same mode arg as you would pass to `os.chmod`.

    Yields:
        File-like object.
    """
def load_from_file(filepath, format_=..., update_data_callback: Incomplete | None = None, disable_memcache: bool = False):
    """Load data from a file.

    Note:
        Any functions from a .py file will be converted to :class:`.SourceCode` objects.

    Args:
        filepath (str): File to load.
        format_ (FileFormat): Format of file contents.
        update_data_callback (typing.Callable): Used to change data before it is
            returned or cached.
        disable_memcache (bool): If True, don't r/w to memcache.

    Returns:
        dict:
    """
def _load_from_file__key(filepath, format_, update_data_callback): ...
def _load_from_file(filepath, format_, update_data_callback): ...
def _load_file(filepath, format_, update_data_callback, original_filepath: Incomplete | None = None): ...

_set_objects: Incomplete
default_objects: Incomplete

def get_objects():
    """Get currently bound variables for evaluation of early-bound attribs.

    Returns:
        dict.
    """
@contextmanager
def set_objects(objects) -> Generator[None]:
    """Set the objects made visible to early-bound attributes.

    For example, `objects` might be used to set a 'build_variant_index' var, so
    that an early-bound 'private_build_requires' can change depending on the
    currently-building variant.

    Args:
        objects (dict): Variables to set.
    """
def load_py(stream, filepath: Incomplete | None = None):
    """Load python-formatted data from a stream.

    Args:
        stream (typing.IO):

    Returns:
        dict:
    """
def _load_py(stream, filepath: Incomplete | None = None): ...

class EarlyThis:
    """The ``this`` object for ``@early`` bound functions.

    Just exposes raw package data as object attributes.
    """
    _data: Any
    def __init__(self, data) -> None: ...
    def __getattr__(self, attr): ...

def process_python_objects(data, filepath: Incomplete | None = None):
    """Replace certain values in the given package data dict.

    Does things like:

    * evaluates ``@early`` decorated functions, and replaces with return value;
    * converts functions into :class:`.SourceCode` instances so they can be serialized
      out to installed packages, and evaluated later;
    * strips some values (modules, ``__``-leading variables) that are never to be
      part of installed packages.

    Returns:
        dict: Updated dict.
    """
def load_yaml(stream, **kwargs):
    """Load yaml-formatted data from a stream.

    Args:
        stream (typing.IO):

    Returns:
        dict:
    """
def load_txt(stream, **kwargs):
    """Load text data from a stream.

    Args:
        stream (typing.IO):

    Returns:
        str:
    """
def clear_file_caches() -> None:
    """Clear any cached files."""

load_functions: Incomplete
