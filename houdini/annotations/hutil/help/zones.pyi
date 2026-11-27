import pathlib
import re
from datetime import datetime
from collections.abc import Iterator, Mapping
from typing import Any, Unpack

from typing_extensions import TypedDict

from hutil.help import processing
from hutil.help.blocks import BlockType, Root, _WikiData
from hutil.help.config import Config
from hutil.help.paths import WikiPath
from hutil.help.search import indexing, searching
from hutil.help.stores import Store, _StoreObj

WIKI_EXT: str
DEFAULT_TEMPLATE_NAME: str
split_expr: re.Pattern[str]
ws_expr: re.Pattern[str]

class Redirect(Exception):
    newpath: str
    def __init__(self, newpath: str) -> None: ...

# WikiContext.copy() takes these fields' new values; any other keyword goes into the copy's env.
class _WikiContextCopyKwargs(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    path: WikiPath
    conditional: bool
    save_to_cache: bool
    including: bool
    depth: int

class WikiContext:
    def copy(self, **kwargs: Unpack[_WikiContextCopyKwargs]) -> WikiContext: ...

class Zone:
    store: Store
    db_path: pathlib.Path | str
    index_page_name: str
    index_source_name: str
    pre: processing.Processor
    post: processing.Processor
    def __init__(self, config: Config | None = ..., store: _StoreObj | None = ..., db_path: str | pathlib.Path | None = ..., create: bool = ..., caching: bool = ...) -> None: ...
    def cache_put(self, path: WikiPath, data: _WikiData) -> None: ...
    def cache_get(self, path: str | WikiPath) -> _WikiData | None: ...
    def source_path(self, path: str | WikiPath, lang: str | None = ...) -> WikiPath: ...
    def parse_to_block(self, source: str, path: str | WikiPath | None = ..., context: WikiContext | None = ..., processor: processing.Processor | None = ..., process: bool = ...) -> Root: ...
    def rebuild_search_index(self, clean: bool = ...) -> None: ...
    def searchables(self, path: str | WikiPath, searcher: searching.Searcher | None = ..., block: BlockType | None = ..., modified: datetime | None = ...) -> Iterator[indexing.Document]: ...
    def wiki_context(self, path: str | WikiPath, *, searcher: searching.Searcher | None = ..., conditional: bool = ..., save_to_cache: bool = ..., env: dict[str, Any] | None = ..., including: bool = ..., depth: int = ...) -> WikiContext: ...
    def load(self, path: str | WikiPath, *, context: WikiContext | None = ..., searcher: searching.Searcher | None = ..., conditional: bool = ..., process: bool = ..., post_process: bool = ..., save_to_cache: bool = ..., env: dict[str, Any] | None = ..., allow_redirect: bool = ..., including: bool = ..., depth: int = ...) -> Root: ...
    def html(self, path: str | WikiPath, template_name: str | None = ..., *, context: WikiContext | None = ..., searcher: searching.Searcher | None = ..., conditional: bool = ..., process: bool = ..., post_process: bool = ..., save_to_cache: bool = ..., env: dict[str, Any] | None = ..., template_vars: Mapping[str, object] | None = ..., allow_redirect: bool = ...) -> str: ...
    def render_template(self, template_name: str, variables: Mapping[str, object]) -> str: ...
