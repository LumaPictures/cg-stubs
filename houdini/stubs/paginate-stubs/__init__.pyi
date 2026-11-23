import typing
from collections.abc import Callable as Callable, Mapping, Sequence
from typing import Any, Generic, TypedDict

from typing import TypeVar
from typing_extensions import TypeVar
_T = TypeVar('_T')
_I = TypeVar('_I')
_C = TypeVar('_C', default=Sequence[_I] | None)
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

__credits__: list[str]
__version__: str
__maintainer__: str
__status__: str

class Page(list[_I], Generic[_I, _C]):
    '''A list/iterator representing the items on one page of a larger collection.
    An instance of the "Page" class is created from a _collection_ which is any
    list-like object that allows random access to its elements.
    The instance works as an iterator running from the first item to the last item on the given
    page. The Page.pager() method creates a link list allowing the user to go to other pages.
    A "Page" does not only carry the items on a certain page. It gives you additional information
    about the page in these "Page" object attributes:
    item_count
        Number of items in the collection
        **WARNING:** Unless you pass in an item_count, a count will be
        performed on the collection every time a Page instance is created.
    page
        Number of the current page
    items_per_page
        Maximal number of items displayed on a page
    first_page
        Number of the first page - usually 1 :)
    last_page
        Number of the last page
    previous_page
        Number of the previous page. If this is the first page it returns None.
    next_page
        Number of the next page. If this is the last page it returns None.
    page_count
        Number of pages
    items
        Sequence/iterator of items on the current page
    first_item
        Index of first item on the current page - starts with 1
    last_item
        Index of last item on the current page
    '''
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
    @typing.overload
    def __init__(self: Page[_I, Sequence[_I] | None], collection: Sequence[_I] | None, page: int | str = ..., items_per_page: int = ..., item_count: int | None = ..., wrapper_class: None = ..., url_maker: Callable[[int], str] | None = ..., **kwargs: Any) -> None: ...
    @typing.overload
    def __init__(self: Page[_I, _T], collection: _T, page: int | str = ..., items_per_page: int = ..., item_count: int | None = ..., *, wrapper_class: Callable[[_T], Sequence[_I]], url_maker: Callable[[int], str] | None = ..., **kwargs: Any) -> None: ...
    def pager(self, format: str = '~2~', url: str | None = None, show_if_single_page: bool = False, separator: str = ' ', symbol_first: str = '&lt;&lt;', symbol_last: str = '&gt;&gt;', symbol_previous: str = '&lt;', symbol_next: str = '&gt;', link_attr: Mapping[str, object] = ..., curpage_attr: Mapping[str, object] = ..., dotdot_attr: Mapping[str, object] = ..., link_tag: Callable[[_PageLink], str] | None = None) -> str:
        """
        Return string with links to other pages (e.g. '1 .. 5 6 7 [8] 9 10 11 .. 50').
        format:
            Format string that defines how the pager is rendered. The string
            can contain the following $-tokens that are substituted by the
            string.Template module:
            - $first_page: number of first reachable page
            - $last_page: number of last reachable page
            - $page: number of currently selected page
            - $page_count: number of reachable pages
            - $items_per_page: maximal number of items per page
            - $first_item: index of first item on the current page
            - $last_item: index of last item on the current page
            - $item_count: total number of items
            - $link_first: link to first page (unless this is first page)
            - $link_last: link to last page (unless this is last page)
            - $link_previous: link to previous page (unless this is first page)
            - $link_next: link to next page (unless this is last page)
            To render a range of pages the token '~3~' can be used. The
            number sets the radius of pages around the current page.
            Example for a range with radius 3:
            '1 .. 5 6 7 [8] 9 10 11 .. 50'
            Default: '~2~'
        url
            The URL that page links will point to. Make sure it contains the string
            $page which will be replaced by the actual page number.
            Must be given unless a url_maker is specified to __init__, in which
            case this parameter is ignored.
        symbol_first
            String to be displayed as the text for the $link_first link above.
            Default: '&lt;&lt;' (<<)
        symbol_last
            String to be displayed as the text for the $link_last link above.
            Default: '&gt;&gt;' (>>)
        symbol_previous
            String to be displayed as the text for the $link_previous link above.
            Default: '&lt;' (<)
        symbol_next
            String to be displayed as the text for the $link_next link above.
            Default: '&gt;' (>)
        separator:
            String that is used to separate page links/numbers in the above range of pages.
            Default: ' '
        show_if_single_page:
            if True the navigator will be shown even if there is only one page.
            Default: False
        link_attr (optional)
            A dictionary of attributes that get added to A-HREF links pointing to other pages. Can
            be used to define a CSS style or class to customize the look of links.
            Example: { 'style':'border: 1px solid green' }
            Example: { 'class':'pager_link' }
        curpage_attr (optional)
            A dictionary of attributes that get added to the current page number in the pager (which
            is obviously not a link). If this dictionary is not empty then the elements will be
            wrapped in a SPAN tag with the given attributes.
            Example: { 'style':'border: 3px solid blue' }
            Example: { 'class':'pager_curpage' }
        dotdot_attr (optional)
            A dictionary of attributes that get added to the '..' string in the pager (which is
            obviously not a link). If this dictionary is not empty then the elements will be wrapped
            in a SPAN tag with the given attributes.
            Example: { 'style':'color: #808080' }
            Example: { 'class':'pager_dotdot' }
        link_tag (optional)
            A callable that accepts single argument `page` (page link information)
            and generates string with html that represents the link for specific page.
            Page objects are supplied from `link_map()` so the keys are the same.
        """
    def link_map(self, format: str = '~2~', url: str | None = None, show_if_single_page: bool = False, separator: str = ' ', symbol_first: str = '&lt;&lt;', symbol_last: str = '&gt;&gt;', symbol_previous: str = '&lt;', symbol_next: str = '&gt;', link_attr: Mapping[str, object] = ..., curpage_attr: Mapping[str, object] = ..., dotdot_attr: Mapping[str, object] = ...) -> _LinkMap:
        """ Return map with links to other pages if default pager() function is not suitable solution.
        format:
            Format string that defines how the pager would be normally rendered rendered. Uses same arguments as pager()
            method, but returns a simple dictionary in form of:
            {'current_page': {'attrs': {},
                                     'href': 'http://example.org/foo/page=1',
                                     'value': 1},
                    'first_page': {'attrs': {},
                                   'href': 'http://example.org/foo/page=1',
                                   'type': 'first_page',
                                   'value': 1},
                    'last_page': {'attrs': {},
                                  'href': 'http://example.org/foo/page=8',
                                  'type': 'last_page',
                                  'value': 8},
                    'next_page': {'attrs': {}, 'href': 'HREF', 'type': 'next_page', 'value': 2},
                    'previous_page': None,
                    'range_pages': [{'attrs': {},
                                     'href': 'http://example.org/foo/page=1',
                                     'type': 'current_page',
                                     'value': 1},
                                     ....
                                    {'attrs': {}, 'href': '', 'type': 'span', 'value': '..'}]}
            The string can contain the following $-tokens that are substituted by the
            string.Template module:
            - $first_page: number of first reachable page
            - $last_page: number of last reachable page
            - $page: number of currently selected page
            - $page_count: number of reachable pages
            - $items_per_page: maximal number of items per page
            - $first_item: index of first item on the current page
            - $last_item: index of last item on the current page
            - $item_count: total number of items
            - $link_first: link to first page (unless this is first page)
            - $link_last: link to last page (unless this is last page)
            - $link_previous: link to previous page (unless this is first page)
            - $link_next: link to next page (unless this is last page)
            To render a range of pages the token '~3~' can be used. The
            number sets the radius of pages around the current page.
            Example for a range with radius 3:
            '1 .. 5 6 7 [8] 9 10 11 .. 50'
            Default: '~2~'
        url
            The URL that page links will point to. Make sure it contains the string
            $page which will be replaced by the actual page number.
            Must be given unless a url_maker is specified to __init__, in which
            case this parameter is ignored.
        symbol_first
            String to be displayed as the text for the $link_first link above.
            Default: '&lt;&lt;' (<<)
        symbol_last
            String to be displayed as the text for the $link_last link above.
            Default: '&gt;&gt;' (>>)
        symbol_previous
            String to be displayed as the text for the $link_previous link above.
            Default: '&lt;' (<)
        symbol_next
            String to be displayed as the text for the $link_next link above.
            Default: '&gt;' (>)
        separator:
            String that is used to separate page links/numbers in the above range of pages.
            Default: ' '
        show_if_single_page:
            if True the navigator will be shown even if there is only one page.
            Default: False
        link_attr (optional)
            A dictionary of attributes that get added to A-HREF links pointing to other pages. Can
            be used to define a CSS style or class to customize the look of links.
            Example: { 'style':'border: 1px solid green' }
            Example: { 'class':'pager_link' }
        curpage_attr (optional)
            A dictionary of attributes that get added to the current page number in the pager (which
            is obviously not a link). If this dictionary is not empty then the elements will be
            wrapped in a SPAN tag with the given attributes.
            Example: { 'style':'border: 3px solid blue' }
            Example: { 'class':'pager_curpage' }
        dotdot_attr (optional)
            A dictionary of attributes that get added to the '..' string in the pager (which is
            obviously not a link). If this dictionary is not empty then the elements will be wrapped
            in a SPAN tag with the given attributes.
            Example: { 'style':'color: #808080' }
            Example: { 'class':'pager_dotdot' }
        """
    @staticmethod
    def default_link_tag(item: _PageLink) -> str:
        """
        Create an A-HREF tag that points to another page.
        """

def make_html_tag(tag: str, text: str | None = None, **params: object) -> str:
    '''Create an HTML tag string.
    tag
        The HTML tag to use (e.g. \'a\', \'span\' or \'div\')
    text
        The text to enclose between opening and closing tag. If no text is specified then only
        the opening tag is returned.
    Example::
        make_html_tag(\'a\', text="Hello", href="/another/page")
        -> <a href="/another/page">Hello</a>
    To use reserved Python keywords like "class" as a parameter prepend it with
    an underscore. Instead of "class=\'green\'" use "_class=\'green\'".
    Warning: Quotes and apostrophes are not escaped.'''
