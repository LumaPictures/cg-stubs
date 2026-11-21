# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Iterable, Mapping
from typing import IO, TypeAlias

from _typeshed import SupportsRead
from houtypes import JSONValue

# What hjson serializes: a dict as an object (its keys must be str or bytes), bytes as a string,
# and any other iterable (a tuple, set, generator, non-dict mapping, ...) as an array.
_Serializable: TypeAlias = (
    None
    | bool
    | int
    | float
    | str
    | bytes
    | Mapping[str, "_Serializable"]
    | Mapping[bytes, "_Serializable"]
    | Iterable["_Serializable"]
)
from typing import Any

def dump(obj: _Serializable, fp: IO[str] | IO[bytes], indent: int | None=..., binary: bool=..., precision: int=..., textwidth: int=..., 
comments: bool=..., maxrecursion: int=..., share_strings: bool=...) -> None:
    """dump(obj, fp, indent=-1, binary=False, precision=0, textwidth=0,
         comments=True, maxrecursion=32768, share_strings=True)

    Serialize ``obj`` as a JSON formatted stream to ``fp``
    If ``binary`` is set to True, the stream will be written as binary
    data (see $HH/public/hjson.py for a pure Python implementation.

    If ``indent`` is < 0 (or not specified), no pretty printing will
    be performed.  Otherwise, the value will be used as the indent level.

    If ``precision`` is greater than 0, floating point values will be
    printed with the given precision.

    If ``textwidth`` is greater than 0, long lines will be wrapped at
    approximately the given textwidth.

    Set the ``comments`` to a boolean to allow/disallow comments to
    to be written to the stream (this is currently a no-op).

    The ``maxrecursion`` argument specifies the limit of object nesting.
    For very deep nesting, you may need to increase this limit.

    When ``share_strings`` is True, shared string table will be used when
    saving binary JSON.  This option is ignored for ASCII JSON.

    """
def dumps(obj: _Serializable, indent: int | None=..., binary: bool=..., precision: int=..., textwidth: int=..., 
comments: bool=..., maxrecursion: int=..., share_strings: bool=...) -> str:
    """dumps(obj, indent=-1, binary=False, precision=0, textwidth=0,
         comments=True, maxrecursion=32768, share_strings=True) -> string

    Serialize ``obj`` to a formatted ``str``
    If ``binary`` is set to True, the stream will be written as binary
    data (see $HH/public/hjson.py for a pure Python implementation.

    If ``indent`` is < 0 (or not specified), no pretty printing will
    be performed.  Otherwise, the value will be used as the indent level.

    If ``precision`` is greater than 0, floating point values will be
    printed with the given precision.

    If ``textwidth`` is greater than 0, long lines will be wrapped at
    approximately the given textwidth.

    Set the ``comments`` to a boolean to allow/disallow comments to
    to be written to the stream (this is currently a no-op).

    The ``maxrecursion`` argument specifies the limit of object nesting.
    For very deep nesting, you may need to increase this limit.

    When ``share_strings`` is True, shared string table will be used when
    saving binary JSON.  This option is ignored for ASCII JSON.

    """
def load(fp: SupportsRead[str] | SupportsRead[bytes]) -> JSONValue:
    """load(fp) -> Object

    De-serialize ``fp`` (a file containing JSON) to a Python object.

    The contents of the file should be either ASCII or binary JSON"""
def loads(str: str | bytes) -> JSONValue:
    """loads(str) -> Object

    De-serialize ``str`` (a string containing JSON) to a Python object.

    The contents of the string should be either ASCII or binary JSON"""
