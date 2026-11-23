import jinja2
import logging
import re
import typing
from bookish.search import _IndexCache, _SearchDoc
from bookish.stores import Store
from bookish.util import Context
from bookish.wiki import pipeline, wikipages
from bookish.wiki.wikipages import WikiPages, _WikiBlock, _WikiNode
from collections.abc import Mapping
from typing import Any
from whoosh.results import Hit as Hit

from typing import TypeVar
from bookish.wiki.wikipages import _WikiText
from typing import TypeVar
_PagesT = TypeVar('_PagesT', bound=WikiPages)
_WikiTextT = TypeVar('_WikiTextT', bound=_WikiText)
table_to_dir: dict[str, str]
shelves_file_path: str

@typing.overload
def pages_from_config(config: Mapping[str, Any], cls: type[_PagesT], jinja_env: jinja2.Environment | None = ..., logger: logging.Logger | None = ...) -> _PagesT: ...
@typing.overload
def pages_from_config(config: Mapping[str, Any], cls: str | None = ..., jinja_env: jinja2.Environment | None = ..., logger: logging.Logger | None = ...) -> WikiPages: ...
def jinja_from_config(config: Mapping[str, Any], store: Store, jinja_env: jinja2.Environment | None = None) -> jinja2.Environment: ...

class HoudiniPages(wikipages.WikiPages):
    use_hou: bool
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class HoudiniPagesWithoutHou(HoudiniPages):
    use_hou: bool
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

scheme_map: dict[str, str]

def get_shortcut(scheme: str, value: str) -> str: ...
def parse_shortcut(path: str) -> str: ...
def url_to_path(url: str) -> str | None: ...

class HoudiniNodes(pipeline.Processor):
    """
    Sets any missing node-specific information based on HOM calls.
    """
    name: str
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class HoudiniShelves(pipeline.Processor):
    name: str
    def __init__(self) -> None: ...
    def apply(self, block: _WikiBlock, context: Context, level: int = 0, root: _WikiBlock | None = None) -> None: ...

class VexPages(pipeline.Processor):
    name: str
    before: tuple[str, ...]
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class HoudiniShortcuts(pipeline.TextModifier):
    '''
    Implements Houdini-specific link features such as "opdef:" syntax and
    convenience schemes such as "Node:" and "Hom:".
    '''
    use_hou: bool
    name: str
    before: tuple[str, ...]
    do_properties: tuple[str, ...]
    opdef_exp: re.Pattern[str]
    def __init__(self, use_hou: bool = True) -> None: ...
    def apply(self, block: _WikiBlock, context: Context) -> None: ...
    def text(self, text: _WikiTextT, context: Context) -> _WikiTextT: ...

class ContentFroms(pipeline.Modifier):
    '''
    Finds the "#contentfrom:" property and replaces it with an include.
    '''
    name: str
    after: tuple[str, ...]
    before: tuple[str, ...]
    def modify(self, block: _WikiBlock, context: Context) -> None: ...

class HoudiniIds(pipeline.Processor):
    """
    Pre-processor for converting names of methods etc. into IDs.
    """
    name: str
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class HomTitles(pipeline.Processor):
    """
    Aesthetic processor that just takes the dotted prefix of a class/function
    name (e.g. hou.Node) and puts the part up to the last dot in the pre-title.
    """
    name: str
    after: tuple[str, ...]
    before: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class HomClasses(pipeline.Processor):
    """
    Post-processor for several features related to HOM pages, such as listing
    subclasses and methods inherited from superclasses.
    """
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
    """
    For example files, computes the nodes and example files and adds them as
    annotations on the document.

    For node docs, searches for examples related to the node.

    For everything else, looks for example loader markup.
    """
    name: str
    before: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class NodeMetadata(pipeline.Processor):
    """
    Uses HOM to attach additional metadata to node docs after they're parsed.
    """
    use_hou: bool
    name: str
    def __init__(self, use_hou: bool = True) -> None: ...
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class ExampleSearches(pipeline.Processor):
    def apply(self, block: _WikiBlock, context: Context, root: _WikiBlock | None = None) -> None: ...
    @staticmethod
    def make_load_example(hit: _SearchDoc | Hit, context: Context, root: _WikiBlock) -> _WikiBlock: ...

class RewriteReplaces(pipeline.Processor):
    '''
    A long time ago, instead of putting /commands/ophide as the path in a
    replaces property, someone wrote Cmd:ophide somehow assuming that would
    work. I should really go back and just replace them all, but rewriting
    them at runtime isn\'t so bad, and who knows who might try the same thing
    again someday, so I might as well make it work.

    Also, someone else decided they wanted that instead of using a page
    property, they wanted to write a @replaces section with links inside, so
    I have to support that too. This processor looks for such a section and
    translates it into a page property.

    This has to run as a preprocessor (so the results are visible to the
    indexer, which currently skips postprocessing), so it\'s split from the
    "Replacments" post-processor which does the reverse lookup on "replaced"
    pages.
    '''
    name: str
    split_expr: re.Pattern[str]
    fields: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context, root: _WikiBlock | None = None, in_replaces: bool = False) -> None: ...

class Replacements(pipeline.Processor):
    '''
    If a searcher is available, this processor finds any documents that
    "replace" the current path, and adds information about them to a
    "replacedby" list on the document root, making them available to display
    in the document. This is to support linking from HScript commands to the
    replacement HOM equivalents.
    '''
    name: str
    prefixes: tuple[str, ...]
    fields: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Actions(pipeline.Processor):
    use_hou: bool
    name: str
    before: tuple[str, ...]
    def __init__(self, use_hou: bool = True) -> None: ...
    def apply(self, block: _WikiBlock, context: Context, action_context: str = '') -> None: ...

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
