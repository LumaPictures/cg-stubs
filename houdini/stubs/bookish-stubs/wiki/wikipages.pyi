import jinja2
import logging
import multiprocessing
import typing
from bookish import compat as compat, functions as functions, paths as paths, search as search, stores as stores, util as util
from bookish.parser import ParserContext as ParserContext, condition_string as condition_string
from bookish.parser.rules import Miss as Miss
from bookish.search import _IndexCache, _SearchDoc
from bookish.text.textify import TextifierBase as TextifierBase
from bookish.wiki import langpaths as langpaths, pipeline as pipeline, styles as styles
from collections.abc import Callable as Callable, Container, Generator, Iterable, Mapping, MutableMapping, Sequence
from datetime import datetime
from houtypes import JSONValue
from multiprocessing.queues import Queue
from typing import Any, Literal, Protocol
from typing_extensions import Required, TypedDict, Unpack

from typing import TypeAlias
from typing import TypeVar
from collections.abc import Hashable
from typing import TypeAlias
from typing import TypeVar
_HashableT = TypeVar('_HashableT', bound=Hashable)
_WikiText: TypeAlias = 'str | list[str | _WikiSpan]'
_WikiNode: TypeAlias = '_WikiBlock | _WikiSpan'
_WikiContent: TypeAlias = '_WikiNode | _WikiText | Sequence[_WikiNode] | None'
_StoredValue: TypeAlias = JSONValue | datetime
class _WikiSpan(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    type: Required[str]
    text: _WikiText | None
    scheme: str | None
    value: str
    tag: str
    attrs: dict[str, str]
    keys: list[str] | str
    alt_keys: tuple[str, ...] | list[str]
    name: str
    fullpath: str
    fragment: str
    exists: bool
    fields: _SearchDoc | None
    fallback_text: _WikiText

class _WikiBlock(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    type: Required[str]
    indent: int
    text: _WikiText
    role: str
    level: int
    body: list[_WikiBlock]
    attrs: dict[str, str | None]
    id: str | None
    container: bool
    is_container: bool
    extent: tuple[int, int] | list[int]
    blevel: int
    ext: str | None
    lang: str | None
    name: str | None
    value: str | None
    tag: str
    ref: str | None
    unwrap: bool | None
    retain: str | Container[str] | None
    remove: str | Container[str] | None
    newtype: str
    newid: str
    title: _WikiText | None
    summary: _WikiText | None
    included: list[str]
    from_cache: bool
    parents: list[_ParentInfo]
    path: str
    hits: list[_SearchDoc]
    groups: dict[str, list[_SearchDoc]]
    labels: dict[str, str]
    tagged: dict[str, list[_SearchDoc]]
    subclasses: list[dict[str, str | None]]
    superclasses: list[dict[str, str]]
    flow_title: _WikiText | None
    flow_links: list[_WikiSpan]
    flow_index: int
    previous: _WikiSpan
    next: _WikiSpan
    replaces: str
    usages: list[_WikiBlock]
    hotkeys: list[list[str]]
    thead: list[_WikiBlock]
    divider: bool
    error: str
    subtitle: str
    prefix: str
    super_path: str
    super_title: _WikiText | None

class _SpanOptions(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    scheme: str | None
    value: str
    tag: str
    attrs: dict[str, str]
    keys: list[str]
    name: str

class _BlockOptions(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    blevel: int
    level: int
    lang: str | None
    id: str | None
    container: bool
    ext: str | None
    name: str | None
    value: str | None
    tag: str
    attrs: dict[str, str | None]

class _ParentInfo(TypedDict):
    path: str
    basepath: str
    title: _WikiText | tuple[()] | None
    summary: _WikiText | tuple[()] | None
    attrs: dict[str, str | None]
    subtopics: _WikiBlock | None

class _MarkdownifierClass(Protocol):
    def __call__(self, root: _WikiBlock, path: str = ..., rel: Callable[[str], str] | None = ..., config: Mapping[str, Any] | None = ...) -> TextifierBase: ...

class Redirect(Exception):
    newpath: str
    def __init__(self, newpath: str) -> None: ...

class ParserError(Exception): ...

def span(typename: str, text: _WikiText | None, **kwargs: Unpack[_SpanOptions]) -> _WikiSpan: ...
def block(typename: str, indent: int, text: _WikiText | None, role: str | None = None, **kwargs: Unpack[_BlockOptions]) -> _WikiBlock: ...
def remove_duplicates(ls: Iterable[_HashableT]) -> list[_HashableT]: ...
def parse_to_blocklist(string: str) -> list[_WikiBlock]: ...
def parse_to_root(string: str) -> _WikiBlock: ...
def write_output(pages: WikiPages, path: str, output_dir: str | None, renderer: str = 'html', suffix: str = '.html', cache: bool = True, searcher: search.WhooshSearcher | None = None) -> None: ...
def write_html_output(pages: WikiPages, path: str, output_dir: str | None, cache: bool = True, searcher: search.WhooshSearcher | None = None) -> None: ...
def write_markdown_output(pages: WikiPages, path: str, output_dir: str | None, cache: bool = True, searcher: search.WhooshSearcher | None = None) -> None: ...
def write_outputs(pages: WikiPages, path: str, output_dir: str | None, cache: bool = True, searcher: search.WhooshSearcher | None = None) -> None: ...
def write_output_multi(pages: WikiPages, dirpath: str | None, procs: int, pathlist: Iterable[str], renderer: str = 'html', suffix: str = '.html', cache: bool = True) -> None: ...
def write_outputs_multi(pages: WikiPages, dirpath: str | None, procs: int, pathlist: Iterable[str], cache: bool = True) -> None: ...
def write_html_output_multi(pages: WikiPages, dirpath: str | None, procs: int, pathlist: Iterable[str], cache: bool = True) -> None: ...
def write_markdown_output_multi(pages: WikiPages, dirpath: str | None, procs: int, pathlist: Iterable[str], cache: bool = True) -> None: ...

class RenderGenProcess(multiprocessing.Process):
    pages: WikiPages
    indexer: search.WhooshIndexer
    searcher: search.WhooshSearcher
    dirpath: str | None
    queue: Queue[str | None]
    outputs: Sequence[tuple[str, str]]
    cache: bool
    error_queue: Queue[tuple[str, str | None, str | None, str]] | None
    def __init__(self, pages: WikiPages, dirpath: str | None, queue: Queue[str | None], outputs: Sequence[tuple[str, str]], cache: bool, error_queue: Queue[tuple[str, str | None, str | None, str]] | None = None) -> None: ...
    def run(self) -> None: ...

class HtmlGenProcess(RenderGenProcess):
    """Backward-compatible HTML-only worker process."""
    def __init__(self, pages: WikiPages, dirpath: str | None, queue: Queue[str | None]) -> None: ...

class PageCache:
    cachedir: str
    cachestore: stores.FileStore
    ext: str
    def __init__(self, cachedir: str | None) -> None: ...
    def cache_path(self, path: str) -> str: ...
    def get_cached_json(self, pages: WikiPages, sourcepath: str) -> _WikiBlock | None: ...
    def put_cache(self, path: str, jsondata: _WikiBlock) -> None: ...
    def delete_path(self, path: str) -> None: ...
    def empty(self) -> None: ...

def pages_from_config(config: Mapping[str, Any], cls: type['WikiPages'] | str | None = None, jinja_env: jinja2.Environment | None = None, logger: logging.Logger | None = None) -> WikiPages: ...
def logger_from_config(config: Mapping[str, Any], logger: logging.Logger | None = None) -> logging.Logger: ...
def store_from_config(config: Mapping[str, Any]) -> stores.Store: ...
def jinja_from_config(config: Mapping[str, Any], store: stores.Store, jinja_env: jinja2.Environment | None = None) -> jinja2.Environment: ...
def textifier_from_config(config: Mapping[str, Any]) -> type[TextifierBase]: ...

class WikiPages:
    store: stores.Store
    jinja_env: jinja2.Environment
    config: Mapping[str, Any]
    logger: logging.Logger
    index_page_name: str
    wiki_ext: str
    cache: PageCache | None
    cachedir: str | None
    def __init__(self, store: stores.Store, jinja_env: jinja2.Environment, config: Mapping[str, Any], logger: logging.Logger | None = None) -> None: ...
    def index_dirs(self) -> tuple[str, str | None, str]: ...
    def indexer(self) -> search.WhooshIndexer: ...
    def reindex(self, clean: bool = False) -> None: ...
    def textifier(self) -> type[TextifierBase]: ...
    def markdownifier(self) -> _MarkdownifierClass: ...
    def textify(self, jsondata: _WikiBlock, path: str = '', **kwargs: Any) -> str: ...
    def json_to_markdown(self, path: str, jsondata: _WikiBlock, **kwargs: Any) -> str: ...
    def style(self, templatename: str) -> styles.Stylesheet: ...
    def full_path(self, origin: str, relpath: str, ext: str = '.html') -> str: ...
    def source_path(self, path: str, locale: str | None = None) -> str: ...
    def is_wiki(self, path: str) -> bool: ...
    def is_wiki_source(self, path: str) -> bool: ...
    def is_index_page(self, path: str) -> bool: ...
    def find_source(self, path: str, locales: Iterable[str | None] | None = None) -> str | None: ...
    def file_path(self, path: str) -> str | None:
        '''
        Takes a virtual server path and translates it into a "real" file path,
        or None if the resource does not exist in a file.
        '''
    def exists(self, path: str) -> bool: ...
    def last_modified(self, path: str) -> datetime: ...
    def size(self, path: str) -> int: ...
    def etag(self, path: str, locale: str | None = None) -> str | None: ...
    @typing.overload
    def content(self, path: str, reformat: bool = ..., encoding: str = ...) -> str: ...
    @typing.overload
    def content(self, path: str, reformat: Literal[False], encoding: None) -> bytes: ...
    @typing.overload
    def content(self, path: str, reformat: Literal[False] = ..., *, encoding: None) -> bytes: ...
    def wiki_context(self, path: str, conditional: bool = True, save_to_cache: bool = True, searcher: search.WhooshSearcher | None = None, profiling: bool = False) -> util.Context: ...
    def context_from(self, wcontext: util.Context | None, path: str, conditional: bool = True, save_to_cache: bool = True, searcher: search.WhooshSearcher | None = None, extra_context: Mapping[str, object] | None = None) -> util.Context: ...
    def process_indexed_doc(self, block: _WikiBlock, doc: _SearchDoc, cache: _IndexCache) -> None: ...
    def available_languages(self, path: str) -> Generator[str, None, None]: ...
    def enlang(self, path: str, lang: str | None = None) -> str: ...
    def page_lang(self, path: str) -> str: ...
    def parent_info_list(self, path: str, context: util.Context, parent_getter: Callable[[WikiPages, str, _WikiBlock], str], seen: set[str] | None = None) -> list[_ParentInfo]: ...
    def parent_info(self, path: str, json: _WikiBlock) -> _ParentInfo: ...
    def json(self, path: str, wcontext: util.Context | None = None, conditional: bool = True, process: bool = True, postprocess: bool = True, save_to_cache: bool = True, extra_context: Mapping[str, object] | None = None, searcher: search.WhooshSearcher | None = None, allow_redirect: bool = False) -> _WikiBlock: ...
    def string_to_json(self, path: str, content: str, wcontext: util.Context | None = None, searcher: search.WhooshSearcher | None = None, extras: Mapping[str, object] | None = None, postprocess: bool = True, allow_redirect: bool = False) -> _WikiBlock: ...
    def json_to_html(self, path: str, jsondata: _WikiContent, stylename: str | None = None, templatename: str | None = None, extras: Mapping[str, object] | None = None, searcher: search.WhooshSearcher | None = None) -> str: ...
    def html(self, path: str, stylename: str | None = None, templatename: str | None = None, language: str | None = None, conditional: bool = True, save_to_cache: bool = True, searcher: search.WhooshSearcher | None = None, extras: Mapping[str, object] | None = None, allow_redirect: bool = False) -> str: ...
    def markdown(self, path: str, language: str | None = None, conditional: bool = True, save_to_cache: bool = True, searcher: search.WhooshSearcher | None = None, extras: Mapping[str, object] | None = None, allow_redirect: bool = False) -> str: ...
    def render_template(self, template_path: str, **kwargs: Any) -> str: ...
    def preview(self, path: str, content: str, stylename: str | None = None, templatename: str | None = None, language: str | None = None, searcher: search.WhooshSearcher | None = None, extras: MutableMapping[str, Any] | None = None) -> str: ...
