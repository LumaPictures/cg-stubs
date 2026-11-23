from collections.abc import Hashable, Iterable, Iterator, Sequence
from typing import Any, Generic, Self, TypeVar

import jinja2

from hutil.help import zones
from hutil.help.blocks import BlockType, Text

_H = TypeVar("_H", bound=Hashable)

PRE_PROC_KEY: str
POST_PROC_KEY: str

class Processor:
    name: str

class MultiModifier(Modifier):
    def __repr__(self) -> str: ...
    def add(self, modifier: Modifier) -> None: ...

class Hierarchy(Processor):
    attr: str
    default: int
    def __init__(self, attr: str = ..., default: int = ...) -> None: ...

class SortHeadings(Processor):
    after: Sequence[str]

class Groups(Processor):
    after: Sequence[str]
    types: frozenset[str]
    blacklist: frozenset[str]
    def __init__(self, types: Iterable[str] = ..., blacklist: Iterable[str] = ...) -> None: ...

class Properties(Processor):
    after: Sequence[str]

class Sections(Processor):
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext, itemtype: str | None = ...) -> None: ...

class Includes(Processor):
    after: Sequence[str]

class Templates(Modifier):
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext, parent_defs: dict[str, jinja2.Template] | None = ...) -> None: ...

class Tables(Processor):
    after: Sequence[str]

class RenumberHeadings(Processor):
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext, level: int = ...) -> None: ...

class LinkProcessor(Modifier):
    def text(self, context: zones.WikiContext, text: Text) -> None: ...

class Flow(Processor):
    after: Sequence[str]

class DeleteNotImplemented(Processor):
    after: Sequence[str]

class DependencyGraph(Generic[_H]):
    def __init__(self, values: Sequence[_H] = ...) -> None: ...
    def add(self, value: _H) -> None: ...
    def dependency(self, value: _H, prereq: _H) -> None: ...
    def resolve(self, values: Sequence[_H] = ...) -> Iterator[_H]: ...

class Pipeline(Processor):
    procs: list[Processor]
    def __init__(self, procs: Sequence[Processor] = ...) -> None: ...
    @classmethod
    def with_procs(cls, procs: Sequence[Processor]) -> Self: ...
    def add(self, proc: Processor) -> None: ...
