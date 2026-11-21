# Houdini stubs generated from Houdini 22.0.466

import typing
from _typeshed import FileDescriptorOrPath as FileDescriptorOrPath, StrOrBytesPath as StrOrBytesPath
from typing import Literal

@typing.overload
def readFile(file_name: FileDescriptorOrPath, binary: Literal[False] = ...) -> str: ...
@typing.overload
def readFile(file_name: FileDescriptorOrPath, binary: Literal[True]) -> bytes: ...
@typing.overload
def readFile(file_name: FileDescriptorOrPath, binary: bool = ...) -> str | bytes: ...
@typing.overload
def writeFile(file_name: FileDescriptorOrPath, contents: str, binary: Literal[False] = ...) -> None: ...
@typing.overload
def writeFile(file_name: FileDescriptorOrPath, contents: bytes, binary: Literal[True]) -> None: ...
@typing.overload
def writeFile(file_name: FileDescriptorOrPath, contents: str | bytes, binary: bool = ...) -> None: ...
def ensureDirExists(dir_path: StrOrBytesPath) -> None: ...
def checksum(file_path: FileDescriptorOrPath) -> str:
    """Given a file path, return a checksum of the contents of the file."""
def humanReadableSize(num_bytes: float) -> str:
    """Given a size in bytes, return a string describing that size."""
def convertToWinPath(path: str, var_notation: str = '%') -> str:
    """Given a path, convert it to a Windows path and return it."""
def convertToWinVariables(s: str) -> str:
    """Given a string, replace any variables in the string (i.e. $FOO)
       with Windows variable notation (i.e. %FOO%).
    """
def splitVersionSuffix(filename: str, version_separator: str | None = None) -> tuple[str, str | None]:
    '''Split the basename and the version suffix from the given filename.

    Return a 2-tuple of (basename, version).  If there is no version
    suffix, then (basename, None) is returned.  Paths and file extensions
    are excluded from the basename.

    The version suffix is the largest set of digits at the end of the
    filename (excluding the extension).  If `version_separator` is
    set to a single character, then the version suffix is the largest
    set of digits at the end of the filename AND immediately after
    the character.  The `version_separator` is excluded from the basename.

    Some examples:
        splitVersionSuffix("myFilename.txt") => ("myFilename", None)
        splitVersionSuffix("myFilename2.txt") => ("myFilename", "2")
        splitVersionSuffix("myFilename_2.txt") => ("myFilename_", "2")
        splitVersionSuffix("myFilename_2.txt", \'_\') => ("myFilename", "2")
        splitVersionSuffix("myFilename2.txt", \'_\') => ("myFilename2", None)
    '''
def insertFileSuffix(filename: str, file_suffix: str | None) -> str: ...
