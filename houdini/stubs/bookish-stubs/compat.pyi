import array
import configparser
import io
import types
from collections.abc import Buffer, Callable as Callable, ItemsView, Iterable, Iterator, Mapping, ValuesView
from itertools import permutations as permutations
from operator import methodcaller as methodcaller
from pickle import dump as dump, dumps as dumps, load as load, loads as loads
from textwrap import indent as indent
from typing import Any, Protocol
from urllib.request import urlretrieve as urlretrieve

from typing import TypeVar
from typing import TypeVar
_K = TypeVar('_K')
_V = TypeVar('_V')
_T = TypeVar('_T')
_ArrT = TypeVar('_ArrT', int, float, str)
class _Exec(Protocol):
    def __call__(self, source: str | Buffer | types.CodeType, globals: dict[str, Any] | None = ..., locals: Mapping[str, object] | None = ..., /) -> None: ...

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
izip = zip
long_type = int
from builtins import next as next
StringIO: type[io.StringIO]
string_type = str
text_type = str
bytes_type = bytes
unichr = chr

def config_get(config: configparser.RawConfigParser, section: str, name: str, fallback: str | None = None) -> str | None: ...
def config_getboolean(config: configparser.RawConfigParser, section: str, name: str, fallback: bool = False) -> bool: ...
def config_getint(config: configparser.RawConfigParser, section: str, name: str, fallback: int = 0) -> int: ...
def byte(num: int) -> bytes: ...
def u(s: str | bytes) -> str: ...
def with_metaclass(meta: type[type], base: type[object] = ...) -> type[Any]: ...
xrange = range
from builtins import range as range
import html.parser
htmlparser = html.parser
from time import perf_counter as perf_counter
zip_: _Zip

def memoryview_(source: Buffer, offset: int | None = None, length: int | None = None) -> memoryview: ...
def array_tobytes(arry: array.array[_ArrT]) -> bytes: ...
def array_frombytes(arry: array.array[_ArrT], bs: Buffer) -> None: ...
