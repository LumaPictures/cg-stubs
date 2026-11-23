import array
import configparser
import io
import types
from collections.abc import Buffer, ItemsView, Iterable, Iterator, Mapping, ValuesView
from collections.abc import Callable
from typing import Any, Protocol, TypeVar

_K = TypeVar("_K")
_V = TypeVar("_V")
_T = TypeVar("_T")
_ArrT = TypeVar("_ArrT", int, float, str)

class _Exec(Protocol):
    def __call__(
        self,
        source: str | Buffer | types.CodeType,
        globals: dict[str, Any] | None = ...,
        locals: Mapping[str, object] | None = ...,
        /,
    ) -> None: ...

class _IterItems(Protocol):
    def __call__(self, o: Mapping[_K, _V], /) -> ItemsView[_K, _V]: ...

class _IterValues(Protocol):
    def __call__(self, o: Mapping[_K, _V], /) -> ValuesView[_V]: ...

class _IterKeys(Protocol):
    def __call__(self, o: Mapping[_K, _V], /) -> Iterator[_K]: ...

class _Zip(Protocol):
    def __call__(self, *args: Iterable[_T]) -> list[tuple[_T, ...]]: ...

def b(s: str) -> bytes: ...

BytesIO: type[io.BytesIO]
callable: Callable[[object], bool]
exec_: _Exec
integer_types: tuple[type[int]]
iteritems: _IterItems
itervalues: _IterValues
iterkeys: _IterKeys
StringIO: type[io.StringIO]

def config_get(config: configparser.RawConfigParser, section: str, name: str, fallback: str | None = ...) -> str | None: ...
def config_getboolean(config: configparser.RawConfigParser, section: str, name: str, fallback: bool = ...) -> bool: ...
def config_getint(config: configparser.RawConfigParser, section: str, name: str, fallback: int = ...) -> int: ...
def byte(num: int) -> bytes: ...
def u(s: str | bytes) -> str: ...
def with_metaclass(meta: type[type], base: type[object] = ...) -> type[Any]: ...

zip_: _Zip

def memoryview_(source: Buffer, offset: int | None = ..., length: int | None = ...) -> memoryview: ...
def array_tobytes(arry: array.array[_ArrT]) -> bytes: ...
def array_frombytes(arry: array.array[_ArrT], bs: Buffer) -> None: ...
