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

# dump writes through the file's descriptor, so fp must be a real file (text or binary).
def dump(
    obj: _Serializable,
    fp: IO[str] | IO[bytes],
    indent: int | None = ...,
    binary: bool = ...,
    precision: int = ...,
    textwidth: int = ...,
    comments: bool = ...,
    maxrecursion: int = ...,
    share_strings: bool = ...,
) -> None: ...
def dumps(
    obj: _Serializable,
    indent: int | None = ...,
    binary: bool = ...,
    precision: int = ...,
    textwidth: int = ...,
    comments: bool = ...,
    maxrecursion: int = ...,
    share_strings: bool = ...,
) -> str: ...
def load(fp: SupportsRead[str] | SupportsRead[bytes]) -> JSONValue: ...
def loads(str: str | bytes) -> JSONValue: ...
