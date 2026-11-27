import datetime
import logging
import re
from bookish import compat as compat, functions as functions, paths as paths, util as util
from bookish.stores import ResourceNotFoundError as ResourceNotFoundError
from bookish.wiki.wikipages import WikiPages as WikiPages, _WikiBlock
from collections.abc import Container, Generator, Iterable, Mapping, Sequence
from concurrent import futures as futures
from houtypes import JSONValue
from typing import Any, TextIO
from typing_extensions import Required, TypedDict, Unpack
from whoosh import analysis, fields, query, reading, sorting
from whoosh.codec import codecs as codecs
from whoosh.index import Index as Index
from whoosh.results import Results
from whoosh.searching import SearcherType as SearcherType
from whoosh.writing import IndexWriter as IndexWriter, merging as merging, reporting as reporting

from typing import TypeAlias
from typing import TypeAlias
from whoosh.collectors import Collector
from whoosh.idsets import DocIdSet
_FacetSpec: TypeAlias = sorting.FacetType | str | Sequence[sorting.FacetType | str]
_FilterSpec: TypeAlias = Collector | Results | query.Query | DocIdSet | set[int]
_Query: TypeAlias = query.Query
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

class _IndexCache(TypedDict, total=False, extra_items=Any):  # type: ignore[call-arg]
    py_parent: dict[str, dict[str, str]]

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

class Searchables:
    index_page_name: str | None
    def schema(self) -> fields.Schema: ...
    def documents(self, pages: WikiPages, path: str, root: _WikiBlock, options: Mapping[str, object], cache: _IndexCache) -> list[_SearchDoc]: ...

def mkdir_p(path: str) -> None: ...

class WhooshIndexer:
    indexdir: str
    searchables: Searchables
    options: dict[str, object]
    cache: _IndexCache
    logger: logging.Logger
    index: Index
    def __init__(self, indexdir: str, searchables: Searchables, options: dict[str, object] | None = None, create: bool = True, indexname: str | None = None, logger: logging.Logger | None = None) -> None: ...
    @staticmethod
    def index_exists_in(indexdir: str, indexname: str | None = None) -> bool: ...
    def set_option(self, name: str, value: object) -> None: ...
    def close(self) -> None: ...
    def reader(self) -> reading.IndexReader: ...
    def searcher(self, overlay: bool = True) -> WhooshSearcher: ...
    def query(self) -> WhooshQuery: ...
    def dump(self, pages: WikiPages) -> None: ...
    def documents(self, pages: WikiPages, path: str) -> Generator[_SearchDoc, None, None]: ...
    def create(self) -> None: ...
    def writer(self, **kwargs: Unpack[_WriterKwargs]) -> IndexWriter: ...
    def update(self, pages: WikiPages, clean: bool = False, optimize: bool = False, **kwargs: Unpack[_UpdateWriterKwargs]) -> bool | set[str] | None: ...
    def update_with(self, writer: IndexWriter, pages: WikiPages, clean: bool = False, overlay: bool = False) -> tuple[bool | set[str] | None, float, int | None, int | None] | None: ...
    def index_paths_with(self, writer: IndexWriter, pages: WikiPages, pathlist: Iterable[str], needs_delete: Container[str] | None = None) -> tuple[bool, int, int] | tuple[None, None, None]: ...
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
    def query(self) -> WhooshQuery: ...
    def document(self, **fields: object) -> _SearchDoc | None: ...
    def tagged_documents(self, tagname: str, pagetype: str | None = None) -> list[_SearchDoc]: ...
    def documents(self, **fields: object) -> Iterable[_SearchDoc]: ...
    def search(self, *args: Unpack[tuple[_Query]], **kwargs: Unpack[_SearchKwargs]) -> Results: ...
    def all_stored_fields(self) -> Iterable[_SearchDoc]: ...
    def group_hits(self, docnums: Iterable[int]) -> list[_SearchDoc]: ...

class WhooshQuery:
    searcher: SearcherType
    q: query.Query | None
    limit: int | None
    sortedby: sorting.MultiFacet | None
    groupedby: sorting.FieldFacet | None
    shortcut_exp: re.Pattern[str]
    def __init__(self, searcher: SearcherType) -> None: ...
    def parse(self, qstring: str, field: str | None = None) -> query.Query: ...
    def make_query(self, qstring: str | None = None, field: str | None = None, **fields: object) -> query.Query: ...
    def set(self, qstring: str | None, **fields: Unpack[_QueryFields]) -> None: ...
    def set_limit(self, limit: int | None) -> None: ...
    def add_sort_field(self, fieldname: str, reverse: bool = False) -> None: ...
    def set_group_field(self, fieldname: str, overlap: bool) -> None: ...
    def search(self, lang: str | None = None) -> Results: ...
    def expand_shortcuts(self, qstring: str, shortcuts: Iterable[Mapping[str, str]]) -> tuple[str, bool]: ...
    def results(self, pages: WikiPages, qstring: str, cat_order: Sequence[str], category: str | None = None, shortcuts: Iterable[Mapping[str, str]] | None = None, limit: int | None = None, cat_limit: int = 5, require: str | None = None, lang: str | None = None, sequence: int = 0) -> _SearchResults: ...
