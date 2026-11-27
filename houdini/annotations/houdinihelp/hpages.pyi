import logging
import re
from collections.abc import Mapping
from typing import Any, TypeVar, overload, type_check_only

import jinja2
from bookish.search import _IndexCache, _SearchDoc
from bookish.stores import Store
from bookish.util import Context
from bookish.wiki import pipeline, wikipages
from bookish.wiki.wikipages import WikiPages, _WikiBlock, _WikiNode, _WikiText
from typing_extensions import Never, TypedDict, Unpack
from whoosh.results import Hit

_PagesT = TypeVar("_PagesT", bound=WikiPages)
_WikiTextT = TypeVar("_WikiTextT", bound=_WikiText)

@type_check_only
class _WikiPagesKwargs(TypedDict, total=False):
    logger: logging.Logger | None

table_to_dir: dict[str, str]
shelves_file_path: str

@overload
def pages_from_config(
    config: Mapping[str, Any],
    cls: type[_PagesT],
    jinja_env: jinja2.Environment | None = ...,
    logger: logging.Logger | None = ...,
) -> _PagesT: ...
@overload
def pages_from_config(
    config: Mapping[str, Any],
    cls: str | None = ...,
    jinja_env: jinja2.Environment | None = ...,
    logger: logging.Logger | None = ...,
) -> WikiPages: ...
def pages_from_config(
    config: Mapping[str, Any],
    cls: type[WikiPages] | str | None = ...,
    jinja_env: jinja2.Environment | None = ...,
    logger: logging.Logger | None = ...,
) -> WikiPages: ...
def jinja_from_config(
    config: Mapping[str, Any], store: Store, jinja_env: jinja2.Environment | None = ...
) -> jinja2.Environment: ...

class HoudiniPages(wikipages.WikiPages):
    use_hou: bool
    @overload
    def __init__(
        self, *args: Unpack[tuple[Store, jinja2.Environment, Mapping[str, Any]]], **kwargs: Unpack[_WikiPagesKwargs]
    ) -> None: ...
    @overload
    def __init__(
        self, *args: Unpack[tuple[Store, jinja2.Environment, Mapping[str, Any], logging.Logger | None]], **kwargs: Never
    ) -> None: ...

class HoudiniPagesWithoutHou(HoudiniPages):
    use_hou: bool
    @overload
    def __init__(
        self, *args: Unpack[tuple[Store, jinja2.Environment, Mapping[str, Any]]], **kwargs: Unpack[_WikiPagesKwargs]
    ) -> None: ...
    @overload
    def __init__(
        self, *args: Unpack[tuple[Store, jinja2.Environment, Mapping[str, Any], logging.Logger | None]], **kwargs: Never
    ) -> None: ...

scheme_map: dict[str, str]

def get_shortcut(scheme: str, value: str) -> str: ...
def parse_shortcut(path: str) -> str: ...
def url_to_path(url: str) -> str | None: ...

class HoudiniNodes(pipeline.Processor):
    name: str
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class HoudiniShelves(pipeline.Processor):
    name: str
    def __init__(self) -> None: ...
    def apply(
        self, block: _WikiBlock, context: Context, level: int = ..., root: _WikiBlock | None = ...
    ) -> None: ...

class VexPages(pipeline.Processor):
    name: str
    before: tuple[str, ...]
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class HoudiniShortcuts(pipeline.TextModifier):
    name: str
    before: tuple[str, ...]
    do_properties: tuple[str, ...]
    opdef_exp: re.Pattern[str]
    use_hou: bool
    def __init__(self, use_hou: bool = ...) -> None: ...
    def apply(self, block: _WikiBlock, context: Context) -> None: ...
    def text(self, text: _WikiTextT, context: Context) -> _WikiTextT: ...

class ContentFroms(pipeline.Modifier):
    name: str
    after: tuple[str, ...]
    before: tuple[str, ...]
    def modify(self, block: _WikiBlock, context: Context) -> None: ...

class HoudiniIds(pipeline.Processor):
    name: str
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class HomTitles(pipeline.Processor):
    name: str
    after: tuple[str, ...]
    before: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class HomClasses(pipeline.Processor):
    name: str
    before: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Itemize(pipeline.Processor):
    name: str
    after: tuple[str, ...]
    before: tuple[str, ...]
    sections: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class ExampleFiles(pipeline.Processor):
    name: str
    before: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class NodeMetadata(pipeline.Processor):
    name: str
    use_hou: bool
    def __init__(self, use_hou: bool = ...) -> None: ...
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class ExampleSearches(pipeline.Processor):
    def apply(self, block: _WikiBlock, context: Context, root: _WikiBlock | None = ...) -> None: ...
    @staticmethod
    def make_load_example(
        hit: _SearchDoc | Hit, context: Context, root: _WikiBlock
    ) -> _WikiBlock: ...

class RewriteReplaces(pipeline.Processor):
    name: str
    split_expr: re.Pattern[str]
    fields: tuple[str, ...]
    def apply(
        self, block: _WikiBlock, context: Context, root: _WikiBlock | None = ..., in_replaces: bool = ...
    ) -> None: ...

class Replacements(pipeline.Processor):
    name: str
    prefixes: tuple[str, ...]
    fields: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Actions(pipeline.Processor):
    name: str
    before: tuple[str, ...]
    use_hou: bool
    def __init__(self, use_hou: bool = ...) -> None: ...
    def apply(self, block: _WikiBlock, context: Context, action_context: str = ...) -> None: ...

class Suites(pipeline.Processor):
    name: str
    retain: dict[str, list[str]]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class IconAliases(pipeline.Processor):
    name: str
    after: tuple[str, ...]
    line_expr: re.Pattern[str]
    path_expr: re.Pattern[str]
    def apply(self, block: _WikiNode, context: Context) -> None: ...
    def process_indexed(self, pages: WikiPages, block: _WikiBlock, doc: _SearchDoc, cache: _IndexCache) -> None: ...
