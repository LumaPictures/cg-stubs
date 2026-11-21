# Houdini stubs generated from Houdini 22.0.466

from typing import Never
import types
from typing import Any, overload

class FileReader:
    def __init__(self, path: str, binary: bool = ...) -> None:
        """__init__(self, path: str, binary: bool = False) -> None"""
    def close(self) -> None:
        """close(self) -> None

        Closes the stream"""
    def closed(self) -> bool:
        """closed(self) -> bool

        [readonly] True if the file is closed"""
    def read(self, size: int = ...) -> str | bytes:
        """read(self, size: int = 0) -> object

        Reads at most size bytes, returned as bytes.

        If the size is negative or ommited, return until EOF is reached."""
    def readable(self) -> bool:
        """readable(self) -> bool

        Returns True if the stream can be read from."""
    def readline(self) -> str | bytes | None:
        """readline(self) -> object

        Reads the next line from the file as bytes."""
    def seek(self, offset: int, whence: int = ...) -> None:
        """seek(self, offset: int, whence: int = 0) -> object

        Move to new file position.
        Argument offset is a byte count.  Optional argument whence defaults to 0 (offset from start of file, offset should be >= 0); other values are 1 (move relative to current position, positive or negative), and 2 (move relative to end of file, usually negative)."""
    @overload
    def seekable(self) -> bool:
        """seekable(self) -> bool

        Returns True if the stream is seekable (random access)."""
    @overload
    def seekable(self, randomaccess: Never) -> bool:
        """seekable(self) -> bool

        Returns True if the stream is seekable (random access)."""
    def tell(self) -> int:
        """tell(self) -> object

        Returns current file position"""
    def writable(self) -> bool:
        """writable(self) -> bool

        Returns True if the stream is writeable."""
    def __enter__(self) -> FileReader:
        """__enter__(self) -> _houfs.FileReader"""
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool:
        """__exit__(self, exc_type: object | None = None, exc_value: object | None = None, traceback: object | None = None) -> bool"""
    def __iter__(self) -> FileReader:
        """__iter__(self) -> object"""
    def __next__(self) -> str | bytes:
        """__next__(self) -> object"""

class FileWriter:
    def __init__(self, path: str, binary: bool = ...) -> None:
        """__init__(self, path: str, binary: bool = False) -> None"""
    def close(self) -> None:
        """close(self) -> None

        Closes the stream"""
    def closed(self) -> bool:
        """closed(self) -> bool

        [readonly] True if the file is closed"""
    def flush(self) -> None:
        """flush(self) -> None

        Flushes underlying buffers"""
    def readable(self) -> bool:
        """readable(self) -> bool

        Returns True if the stream can be read from."""
    def seek(self, offset: int, whence: int = ...) -> None:
        """seek(self, offset: int, whence: int = 0) -> object

        Move to new file position.
        Argument offset is a byte count. Optional argument whence defaults to 0 (offset from start of file, offset should be >= 0); other values are 1 (move relative to current position, positive or negative), and 2 (move relative to end of file, usually negative"""
    @overload
    def seekable(self) -> bool:
        """seekable(self) -> bool

        Returns True if the stream is seekable (random access)."""
    @overload
    def seekable(self, randomaccess: Never) -> bool:
        """seekable(self) -> bool

        Returns True if the stream is seekable (random access)."""
    def tell(self) -> int:
        """tell(self) -> object

        Returns current file position"""
    def writable(self) -> bool:
        """writable(self) -> bool

        Returns True if the stream is writeable."""
    def write(self, data: str | bytes) -> int:
        """write(self, data: object) -> object

        Writes the given string or bytes, returns the file position after writing."""
    def __enter__(self) -> FileWriter:
        """__enter__(self) -> _houfs.FileWriter"""
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> bool:
        """__exit__(self, exc_type: object | None = None, exc_value: object | None = None, traceback: object | None = None) -> bool"""

class Path:
    def __init__(self, path: str) -> None:
        """__init__(self, path: str) -> None"""
    def exists(self) -> bool:
        """exists(self) -> bool

        Whether the path points to an existing file or directory."""
    def glob(self, pattern: str) -> list[Path]:
        """glob(self, pattern: str) -> list[_houfs.Path]

        Glob the given relative pattern in the directory represented by this path, yielding all matching files (of any kind)."""
    def is_dir(self) -> bool:
        """is_dir(self) -> bool

        Return True if the path points to a directory (or a symbolic link pointing to a directory), False if it points a file.

        False is also returned if the path doesn't exist."""
    def is_file(self) -> bool:
        """is_file(self) -> bool

        Return True if the path points to a regular file (or a symbolic link pointing to a regular file), False if it points to a directory.

        False is also returned if the path doesn't exist or if the user doesn't have read access."""
    def iterdir(self) -> list[Path]:
        """iterdir(self) -> list[_houfs.Path]

        When the path points to a directory, yield path objects of the directory contents."""
    def match(self, pattern: str) -> bool:
        """match(self, pattern: str) -> bool

        Match the path string against the provided glob-style pattern. Return True if matching is successful, False otherwise. Multiple patterns can be given if separated by commas: ` ,`."""
    def mkdir(self, mode: int = ..., ignore_umask: bool = ...) -> None:
        """mkdir(self, mode: int = 511, ignore_umask: bool = False) -> None

        Create a new directory and all the parent directories needed. By default, the users umask will be used in conjunction with the mode. ignore_umask will force the mode to be the given value."""
    def open(self, mode: str) -> FileReader | FileWriter:
        """open(self, mode: str) -> object

        Open the file pointed to by the path for reading or writing, similar to python's built-in open()"""
