import re
from collections.abc import Callable, Iterable, Iterator, Mapping, MutableMapping, Sequence
import io
from types import TracebackType
from typing import Any, Generic, Self, TypeAlias, Unpack, type_check_only

from typing_extensions import TypedDict, TypeVar

from bookish.avenue import avenue
from bookish.avenue.patterns import Pattern
from bookish.wiki.wikipages import _WikiBlock, _WikiSpan, _WikiText

_Charmap: TypeAlias = Iterable[tuple[str, str]]
_Block: TypeAlias = "_WikiBlock | list[_WikiBlock] | tuple[_WikiBlock, ...]"
_RootT = TypeVar("_RootT", bound=_Block, default=_Block)

@type_check_only
class _EmitKwargs(TypedDict, total=False):
    indent: int
    wrap: bool
    top: int
    bottom: int
    first: str
    rest: str
    upper: bool
    lower: bool
    before: str
    after: str

# TextifierBase.push()'s options; any other keyword becomes a frame variable.
@type_check_only
class _PushKwargs(TypedDict, total=False, extra_items=int):  # type: ignore[call-arg]
    indent: int
    left: int | None
    top: int
    bottom: int
    width: int | None
    padding_top: int
    padding_bottom: int
    replacements: _Charmap | None
    buffered: bool
    charfilter: bool | None
    charmap: _Charmap | None
    xform: Callable[[str], str] | None

default_charmap: tuple[tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str], tuple[str, str]]
normalize_exp: re.Pattern[str]
lstrip_exp: re.Pattern[str]

def dechar(text: str, charmap: _Charmap = ...) -> str: ...
def addindent(first: str, subsequent: str, text: str, trim: bool = ...) -> str: ...
def format_block(
    text: str,
    left: int = ...,
    width: int = ...,
    wrap: bool = ...,
    first: str = ...,
    rest: str = ...,
    upper: bool = ...,
    lower: bool = ...,
    xform: Callable[[str], str] | None = ...,
    charfilter: bool = ...,
    charmap: _Charmap | None = ...,
    normalize: bool = ...,
) -> str: ...
def join(arg: str | tuple[str, ...] | list[str], *args: str | list[str] | tuple[str, ...]) -> str: ...

class TextFrame(object):
    display_vars: Sequence[str]
    parent: "TextFrame | None"
    left: int
    top: int
    bottom: int
    width: int
    padding_top: int
    padding_bottom: int
    replacements: _Charmap | None
    buffered: bool
    vars: MutableMapping[str, int] | None
    charmap: _Charmap | None
    xform: Callable[[str], str] | None
    charfilter: bool
    buffer: io.StringIO | None
    def __init__(
        self,
        parent: "TextFrame | None",
        left: int = ...,
        top: int = ...,
        bottom: int = ...,
        width: int = ...,
        padding_top: int = ...,
        padding_bottom: int = ...,
        replacements: _Charmap | None = ...,
        buffered: bool = ...,
        vars: MutableMapping[str, int] | None = ...,
        charfilter: bool | None = ...,
        charmap: _Charmap | None = ...,
        xform: Callable[[str], str] | None = ...,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def emit(
        self,
        string: str,
        indent: int = ...,
        wrap: bool = ...,
        first: str = ...,
        rest: str = ...,
        upper: bool = ...,
        lower: bool = ...,
        normalize: bool = ...,
        before: str = ...,
        after: str = ...,
    ) -> None: ...
    def get(self, name: str) -> int | None: ...
    def inc(self, name: str) -> int: ...
    def write(self, string: str) -> None: ...
    def getvalue(self) -> str: ...
    def finish(self) -> None: ...

class TextifierBase(Generic[_RootT]):
    root: _RootT
    path: str
    frames: list[TextFrame]
    gap: int
    eat_top: bool
    aves: avenue.AvenueManager
    def __init__(
        self,
        root: _RootT,
        left: int = ...,
        top: int = ...,
        bottom: int = ...,
        width: int = ...,
        vars: MutableMapping[str, int] | None = ...,
        charfilter: bool = ...,
    ) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    def transform(self) -> str: ...
    @property
    def frame(self) -> TextFrame: ...
    def push(
        self,
        indent: int = ...,
        left: int | None = ...,
        top: int = ...,
        bottom: int = ...,
        width: int | None = ...,
        padding_top: int = ...,
        padding_bottom: int = ...,
        replacements: _Charmap | None = ...,
        buffered: bool = ...,
        charfilter: bool | None = ...,
        charmap: _Charmap | None = ...,
        xform: Callable[[str], str] | None = ...,
        **kwargs: int,
    ) -> Self: ...
    def pop(self) -> None: ...
    def find(self, block: object, ave: str | Pattern, **vars: object) -> Iterator[Any]: ...
    def write(self, string: str) -> None: ...
    def blank_lines(self, n: int) -> None: ...
    def render_body(
        self, body: _WikiBlock | Sequence[_WikiBlock], eat_top: bool = ..., **kwargs: Unpack[_PushKwargs]
    ) -> None: ...
    def render_super(self, block: _Block) -> None: ...
    def render(self, block: _Block, ns: object = ...) -> None: ...
    def render_text(
        self, text: _WikiText | _WikiSpan | tuple[str | _WikiSpan, ...]
    ) -> str: ...
    def render_span(self, span: str | _WikiSpan) -> str: ...
    def emit(
        self,
        text: str,
        indent: int = ...,
        wrap: bool = ...,
        top: int = ...,
        bottom: int = ...,
        first: str = ...,
        rest: str = ...,
        upper: bool = ...,
        lower: bool = ...,
        before: str = ...,
        after: str = ...,
    ) -> None: ...
    def emit_block_text(self, block: _WikiBlock, **kwargs: Unpack[_EmitKwargs]) -> None: ...

class BookishTextifier(TextifierBase[_RootT]):
    def para_block(self, block: _WikiBlock) -> None: ...
    def bullet_group_block(self, block: _WikiBlock) -> None: ...
    def bullet_block(self, block: _WikiBlock) -> None: ...
    def ord_group_block(self, block: _WikiBlock) -> None: ...
    def ord_block(self, block: _WikiBlock) -> None: ...
    def section_block(self, block: _WikiBlock) -> None: ...
    def h_block(self, block: _WikiBlock) -> None: ...
    def note_block(self, block: _WikiBlock) -> None: ...
    def tip_block(self, block: _WikiBlock) -> None: ...
    def warning_block(self, block: _WikiBlock) -> None: ...
    def dt_block(self, block: _WikiBlock) -> None: ...
    def item_block(self, block: _WikiBlock) -> None: ...
    def list_block(self, block: _WikiBlock) -> None: ...
    def subtopics_block(self, block: _WikiBlock) -> None: ...
    def pre_block(self, block: _WikiBlock) -> None: ...
    def var_span(self, span: _WikiSpan) -> str: ...
    def strong_span(self, span: _WikiSpan) -> str: ...
    def em_span(self, span: _WikiSpan) -> str: ...
    def ui_span(self, span: _WikiSpan) -> str: ...
    def code_span(self, span: _WikiSpan) -> str: ...
    def keys_span(self, span: _WikiSpan) -> str: ...
