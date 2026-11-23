import logging
from collections.abc import Callable, Container, MutableSequence
from typing import TypeAlias

from bookish import util
from bookish.wiki.wikipages import _WikiBlock, _WikiNode

_Finder: TypeAlias = Callable[[_WikiBlock], _WikiNode | None]

logger: logging.Logger

class CircularIncludeError(Exception): ...

def make_include(
    ref: str,
    name: str | None = ...,
    value: str | None = ...,
    unwrap: bool | str | None = ...,
    retain: str | Container[str] | None = ...,
    remove: str | Container[str] | None = ...,
    newtype: str | None = ...,
    newid: str | None = ...,
) -> _WikiBlock: ...
def denull(blocks: MutableSequence[_WikiBlock]) -> None: ...
def get_raw_source(
    block: _WikiBlock, context: util.Context, root: _WikiBlock
) -> list[_WikiBlock] | None: ...
def parse_include_path(
    incpath: str | None,
) -> tuple[str, str | None, str | None, bool] | tuple[None, None, None, None]: ...
def spec_from_path(basepath: str, ref: str | None) -> tuple[str | None, _Finder | None, str, bool | str | None]: ...
def spec_from_block(block: _WikiBlock, basepath: str) -> tuple[str | None, _Finder | None, str, bool | str | None]: ...
def get_finder(name: str | None, value: str | None) -> _Finder | None: ...
def get_included(
    block: _WikiBlock, context: util.Context, root: _WikiBlock
) -> list[_WikiBlock] | None: ...
def load_include(
    block: _WikiBlock, context: util.Context, root: _WikiBlock
) -> list[_WikiBlock] | None: ...
def load_include_path(
    basepath: str, ref: str, context: util.Context, root: _WikiBlock
) -> list[_WikiBlock] | None: ...
def load_include_impl(
    path: str | None,
    finder: _Finder | None,
    key: str,
    unwrap: bool | str | None,
    context: util.Context,
    root: _WikiBlock,
) -> list[_WikiBlock] | None: ...
def target(root: _WikiBlock, finder: _Finder | None, unwrap: bool | str | None) -> list[_WikiBlock] | None: ...
