# Houdini stubs generated from Houdini 22.0.466

import os
import types
import typing
from collections.abc import Callable as Callable, Generator, Iterable, Mapping
from houtypes import JSONLike, JSONValue
from typing import Never, Protocol

from typing import TypeVar
from typing import TypeVar
_S = TypeVar('_S', bound=None | bool | int | float | str)
_M = TypeVar('_M', bound=Mapping[str, JSONValue])
_I = TypeVar('_I', bound=Iterable[tuple[str, JSONValue]])
class _Dumps(Protocol):
    def __call__(self, obj: JSONLike, /, *, indent: int | None = ...) -> str: ...

json: types.ModuleType
dumps: _Dumps
loads: Callable[[str | bytes], JSONValue]

def utf8Loads(string: str | bytes) -> JSONValue:
    """Like loads, but all strings in the result object are utf8-encoded
    and not unicode.
    """
def utf8Dumps(obj: JSONLike) -> str:
    """Like dumps, but ensures that the result is not a unicode object by
    utf-8 encoding it."""
def dumpToFile(obj: JSONLike, file_path: str | os.PathLike[str]) -> None:
    """Save the JSON-encoded representation of an object to a file."""
def loadFromFile(file_path: str | os.PathLike[str]) -> JSONValue:
    """Given a file containing JSON-encoded data, return the decoded object."""
def utf8LoadFromFile(file_path: str | os.PathLike[str]) -> JSONValue:
    """Like loadFromFile, except the strings in the decoded object are utf8-
    encoded.
    """
@typing.overload
def object_from_json_data(obj: dict[str, JSONValue]) -> DictAsObject: ...
@typing.overload
def object_from_json_data(obj: list[JSONValue]) -> list[JSONValue]: ...
@typing.overload
def object_from_json_data(obj: tuple[JSONValue, ...] | Generator[JSONValue, Never, object]) -> tuple[JSONValue, ...]: ...
@typing.overload
def object_from_json_data(obj: _S) -> _S: ...
@typing.overload
def object_from_json_data(obj: _M) -> _M: ...
@typing.overload
def object_from_json_data(obj: _I) -> _I: ...

class DictAsObject(dict[str, JSONValue]):
    __dict__: dict[str, JSONValue]
    def __init__(self, *args: Mapping[str, JSONValue] | Iterable[tuple[str, JSONValue]], **kwargs: JSONValue) -> None: ...
    def __getattr__(self, name: str) -> JSONValue: ...
