# Houdini stubs generated from Houdini 22.0.466

from bookish.avenue.patterns import Pattern as Pattern
from bookish.compat import string_type as string_type
from bookish.parser.rules import Miss as Miss
from collections.abc import Iterator, Mapping
from typing import Any, Generic

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing_extensions import TypeVar
_T = TypeVar('_T')
_RootT = TypeVar('_RootT', default=Any)
_Container: TypeAlias = dict[Any, Any] | list[Any]
class AvenueParserError(Exception): ...

def make_parents(data: object) -> dict[int, _Container | None]: ...
def get_parent(parents: Mapping[int, _T], obj: object) -> _T: ...

class AvenueContext(dict[str, Any], Generic[_RootT]):
    root: _RootT
    def __init__(self, root: _RootT, **kwargs: object) -> None: ...
    def parent(self, obj: object) -> _Container | None: ...

def parse(avestring: str) -> Pattern: ...
def find(parsed: Pattern, root: object, **vars: object) -> Iterator[Any]: ...

class AvenueManager:
    """
    Simple class that provides caching of compiled Avenue strings.
    """
    def __init__(self) -> None: ...
    def compile(self, avestring: str) -> Pattern: ...
    def find(self, ave: str | Pattern, root: object, start: object, **vars: object) -> Iterator[Any]: ...
