import logging
import re
from collections.abc import Container, Generator, Iterable, Mapping, Sequence
import datetime
from concurrent import futures
from typing import Any, TextIO, TypeAlias

from houtypes import JSONValue
from typing_extensions import Required, TypedDict, Unpack

from bookish.wiki.wikipages import WikiPages, _WikiBlock
from whoosh import analysis, fields, query, reading, sorting
from whoosh.codec import codecs
from whoosh.collectors import Collector
from whoosh.idsets import DocIdSet
from whoosh.index import Index
from whoosh.results import Results
from whoosh.searching import SearcherType
from whoosh.writing import IndexWriter, merging, reporting

# A document in the search index, as Searchables makes it, and its stored fields, as the
# searcher gives them back. Houdini's Searchables and the stores' extra_fields() add fields of
# their own, which hold strings (or None).
class _SearchDoc(TypedDict, total=False, extra_items=JSONValue):  # type: ignore[call-arg]
    path: Required[str]
    status: str | None
    category: str
    content: str
    title: str
    sortkey: str
    summary: str
    grams: str
    type: str | None
    tags: str | None
    icon: str | None
    links: str
    container: bool | None
    parent: str | None
    isindex: bool
    lang: str
    anchor: str | None
    modified: datetime.datetime
    py_anchor: str
    py_parent: str
    instant_doc: _WikiBlock

# The caches that the pipeline's process_indexed() methods keep while a whole index is built:
# PythonAPI's maps a directory to the python packages its settings name.
class _IndexCache(TypedDict, total=False, extra_items=Any):  # type: ignore[call-arg]
    py_parent: dict[str, dict[str, str]]

# The keywords Index.writer() takes, and passes on to the IndexWriter it makes; update() sets
# the writer's optimize flag itself.
class _UpdateWriterKwargs(TypedDict, total=False):
    executor: futures.Executor | None
    multiproc: bool
    multithreaded: bool
    procs: int | None
    threads: int | None
    codec: codecs.Codec | None
    schema: fields.Schema | None
    doc_limit: int
    post_limit: int
    merge_strategy: merging.MergeStrategy | None
    reporter: reporting.Reporter | None
    merge: bool

class _WriterKwargs(_UpdateWriterKwargs, total=False):
    optimize: bool

# A facet, or a field name or a list of them, which FacetType.from_sortedby() turns into one.
_FacetSpec: TypeAlias = sorting.FacetType | str | Sequence[sorting.FacetType | str]
_FilterSpec: TypeAlias = Collector | Results | query.Query | DocIdSet | set[int]

# WhooshSearcher's query() method hides the query module inside its class.
_Query: TypeAlias = query.Query

# The keywords SearcherType.search() takes after the query.
class _SearchKwargs(TypedDict, total=False):
    limit: int | None
    sortedby: _FacetSpec | None
    reverse: bool
    groupedby: _FacetSpec | None
    collapse: _FacetSpec | None
    collapse_limit: int
    collapse_order: _FacetSpec | None
    optimize: bool
    filter: _FilterSpec | None
    mask: _FilterSpec | None
    terms: bool
    maptype: type[sorting.FacetMap] | None
    scored: bool
    spans: bool

# The keywords make_query() takes: the field to parse a query string in, or the field values
# to match.
class _QueryFields(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    field: str | None

class _SearchResults(TypedDict):
    qstring: str
    instants: list[_SearchDoc]
    category: str | None
    categories: list[tuple[str, list[_SearchDoc], int]]
    length: int
    limit: int | None
    hitobj: Results
    hits: list[_SearchDoc]
    sequence: int
    runtime: float

HOST_EXITING: bool
IS_WHOOSH3: bool
default_logger: logging.Logger
sh: logging.StreamHandler[TextIO]
formatter: logging.Formatter
text_ana: analysis.CompositeAnalyzer
default_fields: dict[str, fields.FieldType | type[fields.FieldType]]
dynamic_fields: dict[str, type[fields.FieldType]]

def become_instant(andq: Iterable[query.Query]) -> query.And: ...
def combine_readers(readers: Iterable[reading.IndexReader]) -> reading.IndexReader: ...
def mkdir_p(path: str) -> None: ...

class Searchables:
    index_page_name: str | None
    def schema(self) -> fields.Schema: ...
    def documents(
        self,
        pages: WikiPages,
        path: str,
        root: _WikiBlock,
        options: Mapping[str, object],
        cache: _IndexCache,
    ) -> list[_SearchDoc]: ...

class WhooshIndexer:
    indexdir: str
    searchables: Searchables
    options: dict[str, object]
    cache: _IndexCache
    logger: logging.Logger
    index: Index
    def __init__(
        self,
        indexdir: str,
        searchables: Searchables,
        options: dict[str, object] | None = ...,
        create: bool = ...,
        indexname: str | None = ...,
        logger: logging.Logger | None = ...,
    ) -> None: ...
    @staticmethod
    def index_exists_in(indexdir: str, indexname: str | None = ...) -> bool: ...
    def set_option(self, name: str, value: object) -> None: ...
    def close(self) -> None: ...
    def reader(self) -> reading.IndexReader: ...
    def searcher(self, overlay: bool = ...) -> "WhooshSearcher": ...
    def query(self) -> "WhooshQuery": ...
    def dump(self, pages: WikiPages) -> None: ...
    def documents(self, pages: WikiPages, path: str) -> Generator[_SearchDoc, None, None]: ...
    def create(self) -> None: ...
    def writer(self, **kwargs: Unpack[_WriterKwargs]) -> IndexWriter: ...
    def update(
        self, pages: WikiPages, clean: bool = ..., optimize: bool = ..., **kwargs: Unpack[_UpdateWriterKwargs]
    ) -> bool | set[str] | None: ...
    def update_with(
        self, writer: IndexWriter, pages: WikiPages, clean: bool = ..., overlay: bool = ...
    ) -> tuple[bool | set[str] | None, float, int | None, int | None] | None: ...
    def index_paths_with(
        self,
        writer: IndexWriter,
        pages: WikiPages,
        pathlist: Iterable[str],
        needs_delete: Container[str] | None = ...,
    ) -> tuple[bool, int, int] | tuple[None, None, None]: ...
    def delete_paths_with(self, writer: IndexWriter, pathlist: Iterable[str]) -> tuple[None, None, None] | None: ...

class WhooshSearcher:
    searcher: SearcherType
    limit: int | None
    sortedby: sorting.MultiFacet | None
    def __init__(self, searcher: SearcherType) -> None: ...
    def up_to_date(self) -> bool: ...
    def has_field(self, fieldname: str) -> bool: ...
    def lexicon(self, fieldname: str) -> Generator[str | bool | int | float | datetime.datetime, None, None]: ...
    def term_exists(self, fieldname: str, text: str) -> bool: ...
    def query(self) -> "WhooshQuery": ...
    def document(self, **fields: object) -> _SearchDoc | None: ...
    def tagged_documents(self, tagname: str, pagetype: str | None = ...) -> list[_SearchDoc]: ...
    def documents(self, **fields: object) -> Iterable[_SearchDoc]: ...
    def search(self, *args: Unpack[tuple[_Query]], **kwargs: Unpack[_SearchKwargs]) -> Results: ...
    def all_stored_fields(self) -> Iterable[_SearchDoc]: ...
    def group_hits(self, docnums: Iterable[int]) -> list[_SearchDoc]: ...

class WhooshQuery:
    shortcut_exp: re.Pattern[str]
    searcher: SearcherType
    q: query.Query | None
    limit: int | None
    sortedby: sorting.MultiFacet | None
    groupedby: sorting.FieldFacet | None
    def __init__(self, searcher: SearcherType) -> None: ...
    def __repr__(self) -> str: ...
    def parse(self, qstring: str, field: str | None = ...) -> query.Query: ...
    def make_query(self, qstring: str | None = ..., field: str | None = ..., **fields: object) -> query.Query: ...
    def set(self, qstring: str | None, **fields: Unpack[_QueryFields]) -> None: ...
    def set_limit(self, limit: int | None) -> None: ...
    def add_sort_field(self, fieldname: str, reverse: bool = ...) -> None: ...
    def set_group_field(self, fieldname: str, overlap: bool) -> None: ...
    def search(self, lang: str | None = ...) -> Results: ...
    def expand_shortcuts(self, qstring: str, shortcuts: Iterable[Mapping[str, str]]) -> tuple[str, bool]: ...
    def results(
        self,
        pages: WikiPages,
        qstring: str,
        cat_order: Sequence[str],
        category: str | None = ...,
        shortcuts: Iterable[Mapping[str, str]] | None = ...,
        limit: int | None = ...,
        cat_limit: int = ...,
        require: str | None = ...,
        lang: str | None = ...,
        sequence: int = ...,
    ) -> _SearchResults: ...
