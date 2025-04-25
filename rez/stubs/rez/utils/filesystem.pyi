import _thread
from _typeshed import Incomplete
from collections.abc import Generator
from contextlib import contextmanager
from rez.util import which as which
from rez.utils.execution import Popen as Popen
from rez.utils.platform_ import platform_ as platform_
from typing import Any

is_windows: Incomplete

class TempDirs:
    """Tempdir manager.

    Makes tmpdirs and ensures they're cleaned up on program exit.
    """
    instances_lock: Incomplete
    instances: Incomplete
    tmpdir: Any
    prefix: Any
    dirs: set[Any]
    lock: _thread.LockType
    def __init__(self, tmpdir, prefix: str = 'rez_') -> None: ...
    def mkdtemp(self, cleanup: bool = True): ...
    def __del__(self) -> None: ...
    def clear(self) -> None: ...
    @classmethod
    def clear_all(cls) -> None: ...

@contextmanager
def make_path_writable(path) -> Generator[None]:
    """Temporarily make `path` writable, if possible.

    Args:
        path (str): Path to make temporarily writable
    """
@contextmanager
def retain_cwd() -> Generator[None]:
    """Context manager that keeps cwd unchanged afterwards.
    """
def get_existing_path(path, topmost_path: Incomplete | None = None):
    """Get the longest parent path in `path` that exists.

    If `path` exists, it is returned.

    Args:
        path (str): Path to test
        topmost_path (str): Do not test this path or above

    Returns:
        str: Existing path, or None if no path was found.
    """
def safe_listdir(path):
    """Safe listdir.

    Works in a multithread/proc scenario where dirs may be deleted at any time
    """
def safe_makedirs(path) -> None:
    """Safe makedirs.

    Works in a multithreaded scenario.
    """
def safe_remove(path) -> None:
    """Safely remove the given file or directory.

    Works in a multithreaded scenario.
    """
def forceful_rmtree(path) -> None:
    """Like shutil.rmtree, but may change permissions.

    Specifically, non-writable dirs within `path` can cause rmtree to fail. This
    func chmod's to writable to avoid this issue, if possible.

    Also handled:
        * path length over 259 char (on Windows)
        * unicode path
    """
def replacing_symlink(source, link_name) -> None:
    """Create symlink that overwrites any existing target.
    """
def replacing_copy(src, dest, follow_symlinks: bool = False) -> None:
    """Perform copy that overwrites any existing target.

    Will copy/copytree `src` to `dest`, and will remove `dest` if it exists,
    regardless of what it is.

    If `follow_symlinks` is False, symlinks are preserved, otherwise their
    contents are copied.

    Note that this behavior is different to `shutil.copy`, which copies src
    into dest if dest is an existing dir.
    """
def replace_file_or_dir(dest, source) -> None:
    """Replace `dest` with `source`.

    Acts like an `os.rename` if `dest` does not exist. Otherwise, `dest` is
    deleted and `src` is renamed to `dest`.
    """
def additive_copytree(src, dst, symlinks: bool = False, ignore: Incomplete | None = None) -> None:
    """Version of `copytree` that merges into an existing directory.
    """
@contextmanager
def make_tmp_name(name) -> Generator[Incomplete]:
    """Generates a tmp name for a file or dir.

    This is a tempname that sits in the same dir as `name`. If it exists on
    disk at context exit time, it is deleted.
    """
def is_subdirectory(path_a, path_b) -> bool:
    """Returns True if `path_a` is a subdirectory of `path_b`."""
def find_matching_symlink(path: str, source: str) -> str | None:
    """Find a symlink under `path` that points at `source`.

    If source is relative, it is considered relative to `path`.

    Returns:
        str: Name of symlink found, or None.
    """
def copy_or_replace(src: str, dst: str):
    """try to copy with mode, and if it fails, try replacing
    """
def copytree(src: str, dst: str, symlinks: bool = False, ignore: Incomplete | None = None, hardlinks: bool = False):
    """copytree that supports hard-linking
    """
def movetree(src, dst) -> None:
    """Attempts a move, and falls back to a copy+delete if this fails
    """
def safe_chmod(path, mode) -> None:
    """Set the permissions mode on path, but only if it differs from the current mode.
    """
def to_nativepath(path): ...
def to_ntpath(path): ...
def to_posixpath(path): ...
def canonical_path(path, platform: Incomplete | None = None):
    """ Resolves symlinks, and formats filepath.

    Resolves symlinks, lowercases if filesystem is case-insensitive,
    formats filepath using slashes appropriate for platform.

    Args:
        path (str): Filepath being formatted
        platform (rez.utils.platform\\_.Platform): Indicates platform path is being
            formatted for. Defaults to current platform.

    Returns:
        str: Provided path, formatted for platform.
    """
def encode_filesystem_name(input_str):
    '''Encodes an arbitrary unicode string to a generic filesystem-compatible
    non-unicode filename.

    The result after encoding will only contain the standard ascii lowercase
    letters (a-z), the digits (0-9), or periods, underscores, or dashes
    (".", "_", or "-").  No uppercase letters will be used, for
    comaptibility with case-insensitive filesystems.

    The rules for the encoding are:

    1. Any lowercase letter, digit, period, or dash (a-z, 0-9, ., or -) is
    encoded as-is.

    2. Any underscore is encoded as a double-underscore (``__``)

    3. Any uppercase ascii letter (A-Z) is encoded as an underscore followed
    by the corresponding lowercase letter (ie, "A" => "_a")

    4. All other characters are encoded using their UTF-8 encoded unicode
       representation, in the following format: ``_NHH...``, where:

       * N represents the number of bytes needed for the UTF-8 encoding,
         except with N=0 for one-byte representation (the exception for N=1
         is made both because it means that for "standard" ascii characters
         in the range 0-127, their encoding will be _0xx, where xx is their
         ascii hex code; and because it mirrors the ways UTF-8 encoding
         itself works, where the number of bytes needed for the character can
         be determined by counting the number of leading "1"s in the binary
         representation of the character, except that if it is a 1-byte
         sequence, there are 0 leading 1\'s).
       * HH represents the bytes of the corresponding UTF-8 encoding, in
         hexadecimal (using lower-case letters)

         As an example, the character ``*``, whose (hex) UTF-8 representation
         of 2A, would be encoded as "_02a", while the "euro" symbol, which
         has a UTF-8 representation of E2 82 AC, would be encoded as
         "_3e282ac".  (Note that, strictly speaking, the "N" part of the
         encoding is redundant information, since it is essentially encoded
         in the UTF-8 representation itself, but it makes the resulting
         string more human-readable, and easier to decode).

    As an example, the string "Foo_Bar (fun).txt" would get encoded as ``_foo___bar_020_028fun_029.txt``.
    '''

_FILESYSTEM_TOKEN_RE: Incomplete
_HEX_RE: Incomplete

def decode_filesystem_name(filename):
    """Decodes a filename encoded using the rules given in encode_filesystem_name
    to a unicode string.
    """
def test_encode_decode() -> None: ...
def walk_up_dirs(path) -> Generator[Incomplete]:
    """Yields absolute directories starting with the given path, and iterating
    up through all it's parents, until it reaches a root directory"""
def windows_long_path(dos_path):
    """Prefix '\\?' for path longer than 259 char (Win32API limitation)
    """
def rename(src, dst) -> None:
    """Utility function to rename a file or folder src to dst with retrying.

    This function uses the built-in `os.rename()` function and falls back to `robocopy` tool
    if `os.rename` raises a `PermissionError` exception.

    Args:
        src (str): The original name (path) of the file or folder.
        dst (str): The new name (path) for the file or folder.

    Raises:
        OSError: If renaming fails after all attempts.

    """
