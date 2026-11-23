from collections.abc import Callable, Mapping, Sequence
from typing import Any, Generic, TypedDict, overload

from typing_extensions import TypeVar

_T = TypeVar("_T")
_I = TypeVar("_I")
# The type of the collection given to the constructor, before any wrapper_class.
_C = TypeVar("_C", default=Sequence[_I] | None)

class _PageLink(TypedDict):
    type: str
    value: str
    attrs: Mapping[str, object]
    href: str
    number: int | None

class _CurrentPage(TypedDict):
    type: str
    value: int
    attrs: Mapping[str, object]
    href: str

class _LinkMap(TypedDict):
    first_page: _PageLink | None
    last_page: _PageLink | None
    previous_page: _PageLink | None
    next_page: _PageLink | None
    current_page: _CurrentPage | None
    radius: int
    range_pages: list[_PageLink]

__author__: str
__copyright__: str
__credits__: list[str]
__license__: str
__version__: str
__maintainer__: str
__email__: str
__status__: str

class Page(list[_I], Generic[_I, _C]):
    collection: Sequence[_I]
    collection_type: type[_C]
    url_maker: Callable[[int], str]
    kwargs: dict[str, Any]
    page: int
    items_per_page: int
    items: list[_I]
    item_count: int
    first_page: int | None
    page_count: int
    last_page: int | None
    first_item: int | None
    last_item: int | None
    previous_page: int | None
    next_page: int | None
    curpage_attr: Mapping[str, object]
    separator: str
    link_attr: Mapping[str, object]
    dotdot_attr: Mapping[str, object]
    url: str | None
    link_tag: Callable[[_PageLink], str]
    radius: int
    @overload
    def __init__(
        self: "Page[_I, Sequence[_I] | None]",
        collection: Sequence[_I] | None,
        page: int | str = ...,
        items_per_page: int = ...,
        item_count: int | None = ...,
        wrapper_class: None = ...,
        url_maker: Callable[[int], str] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    @overload
    def __init__(
        self: "Page[_I, _T]",
        collection: _T,
        page: int | str = ...,
        items_per_page: int = ...,
        item_count: int | None = ...,
        *,
        wrapper_class: Callable[[_T], Sequence[_I]],
        url_maker: Callable[[int], str] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def __init__(
        self,
        collection: Any,
        page: int | str = ...,
        items_per_page: int = ...,
        item_count: int | None = ...,
        wrapper_class: Callable[[Any], Sequence[_I]] | None = ...,
        url_maker: Callable[[int], str] | None = ...,
        **kwargs: Any,
    ) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def pager(
        self,
        format: str = ...,
        url: str | None = ...,
        show_if_single_page: bool = ...,
        separator: str = ...,
        symbol_first: str = ...,
        symbol_last: str = ...,
        symbol_previous: str = ...,
        symbol_next: str = ...,
        link_attr: Mapping[str, object] = ...,
        curpage_attr: Mapping[str, object] = ...,
        dotdot_attr: Mapping[str, object] = ...,
        link_tag: Callable[[_PageLink], str] | None = ...,
    ) -> str: ...
    def link_map(
        self,
        format: str = ...,
        url: str | None = ...,
        show_if_single_page: bool = ...,
        separator: str = ...,
        symbol_first: str = ...,
        symbol_last: str = ...,
        symbol_previous: str = ...,
        symbol_next: str = ...,
        link_attr: Mapping[str, object] = ...,
        curpage_attr: Mapping[str, object] = ...,
        dotdot_attr: Mapping[str, object] = ...,
    ) -> _LinkMap: ...
    @staticmethod
    def default_link_tag(item: _PageLink) -> str: ...

def make_html_tag(tag: str, text: str | None = ..., **params: object) -> str: ...
