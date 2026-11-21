import os
import types
from collections.abc import Callable, Generator, Iterable, Mapping
from typing import Never, Protocol, TypeVar, overload, type_check_only

from houtypes import JSONLike, JSONValue

_S = TypeVar("_S", bound=None | bool | int | float | str)
_M = TypeVar("_M", bound=Mapping[str, JSONValue])
_I = TypeVar("_I", bound=Iterable[tuple[str, JSONValue]])

class _Dumps(Protocol):
    def __call__(self, obj: JSONLike, /, *, indent: int | None = ...) -> str: ...

json: types.ModuleType
dumps: _Dumps
loads: Callable[[str | bytes], JSONValue]

def utf8Loads(string: str | bytes) -> JSONValue: ...
def utf8Dumps(obj: JSONLike) -> str: ...
def dumpToFile(obj: JSONLike, file_path: str | os.PathLike[str]) -> None: ...
def loadFromFile(file_path: str | os.PathLike[str]) -> JSONValue: ...
def utf8LoadFromFile(file_path: str | os.PathLike[str]) -> JSONValue: ...
# Every dict in the result is a DictAsObject, itself a dict[str, JSONValue].
@overload
def object_from_json_data(obj: dict[str, JSONValue]) -> "DictAsObject": ...
@overload
def object_from_json_data(obj: list[JSONValue]) -> list[JSONValue]: ...
@overload
def object_from_json_data(
    obj: tuple[JSONValue, ...] | Generator[JSONValue, Never, object],
) -> tuple[JSONValue, ...]: ...
@overload
def object_from_json_data(obj: _S) -> _S: ...
# Other mappings and iterables are returned as is.
@overload
def object_from_json_data(obj: _M) -> _M: ...
@overload
def object_from_json_data(obj: _I) -> _I: ...

class DictAsObject(dict[str, JSONValue]):
    __dict__: dict[str, JSONValue]
    # Its keys are its attributes: its __dict__ is itself.
    @type_check_only
    def __getattr__(self, name: str) -> JSONValue: ...
    def __init__(
        self,
        *args: Mapping[str, JSONValue] | Iterable[tuple[str, JSONValue]],
        **kwargs: JSONValue,
    ) -> None: ...
