import logging
from bookish import functions as functions, paths as paths, util as util
from bookish.compat import StringIO as StringIO, iteritems as iteritems, string_type as string_type
from bookish.search import _IndexCache, _SearchDoc
from bookish.util import Context as Context, join_text as join_text
from bookish.wiki import includes as includes, langpaths as langpaths
from bookish.wiki.wikipages import WikiPages as WikiPages, _WikiBlock, _WikiSpan
from collections.abc import Generator, Iterable, Sequence
from whoosh.results import Results as Results

from typing import TypeVar
from typing import TypeVar
_P = TypeVar('_P', bound='Processor')
logger: logging.Logger

class Processor:
    """
    Base class for objects that walk a document tree modifying the blocks in
    place.
    """
    name: str
    def __or__(self, other: Processor) -> Pipe: ...
    def add(self, other: Processor) -> Pipe: ...
    def apply(self, block: _WikiBlock, context: Context) -> None: ...
    def process_indexed(self, pages: WikiPages, block: _WikiBlock, doc: _SearchDoc, cache: _IndexCache) -> None: ...

class Pipe(Processor):
    """
    Processor that wraps multiple processor objects and calls them each in turn.
    """
    processors: list[Processor]
    def __init__(self, processors: Iterable[Processor]) -> None: ...
    def add(self, other: Processor) -> None: ...
    def processor_by_class(self, cls: type[_P]) -> _P | None: ...
    def apply(self, block: _WikiBlock, context: Context, profile: bool = False, threshold: float = 0.1) -> None: ...
    def process_indexed(self, pages: WikiPages, block: _WikiBlock, doc: _SearchDoc, cache: _IndexCache) -> None: ...

class TreeProcessor(Processor):
    """
    Middle-ware for processors that might have to process every block in the
    tree. Does the work of traversing the tree, calling `modify(block, context)`
    at each block. If the `modify` method returns `True`, the processor
    recursively processes each child of the block.
    """
    def apply(self, block: _WikiBlock, context: Context) -> None: ...
    def modify(self, block: _WikiBlock, context: Context) -> bool: ...

class MultiModifier(Processor):
    """
    Processor that wraps multiple Modifier objects. This object walks the document
    tree and calls each modifier on each block.
    """
    modifiers: list['Modifier']
    def __init__(self, modifiers: list['Modifier']) -> None: ...
    def add(self, modifier: Modifier) -> None: ...
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Modifier(Processor):
    """
    A type of Processor that only modifies a single block at a time (that is,
    that doesn't care about hierarchy). This allows them to be grouped together
    in a MultiModifier.
    """
    def modify(self, block: _WikiBlock, context: Context) -> None: ...
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Title(Processor):
    """
    Finds the page title and summary blocks and copies their text up to the root
    for easier access by other code.
    """
    name: str
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Hierarchy(Processor):
    '''
    Organizes a linear list of blocks into a hierarchy based on the relative
    values of a key (usually "indent").
    '''
    attr: str
    default: int
    name: str
    def __init__(self, attr: str = 'indent', default: int = 0) -> None:
        """
        :param attr: The key to use to determine the hierarchical level of
            a given block.
        :param default: The value to use for blocks that don't have the
            attribute key.
        """
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class SortHeadings(Processor):
    '''
    Implements "linear" header style, where blocks simply come after headers at
    the same indent, instead of being indented under the heading. This processor
    looks for headings without bodies and pulls any subsequent blocks into them.
    '''
    name: str
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Groups(Processor):
    '''
    Groups blocks of the same type "N" under "group_N" superblocks.
    '''
    types: frozenset[str]
    blacklist: frozenset[str]
    name: str
    after: tuple[str, ...]
    def __init__(self, types: Iterable[str] = ('bullet', 'ord', 'dt', 'item'), blacklist: Iterable[str] = ('billboard', 'null')) -> None:
        """
        :param whitelist: if not empty, only type names in this collection
            will be grouped.
        :param blacklist: if not empty, no type names in this collection will
            be grouped.
        """
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Properties(Processor):
    '''
    Changes "property" blocks into attributes on the parent block.
    Make sure this runs after Hierarchy.
    '''
    name: str
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class EmptyBlocks(Processor):
    """
    Removes blocks without any content. Ignores certain things.
    """
    name: str
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Promote(Processor):
    '''
    Finds blocks where a bit of xml or an include is the only thing in the
    block, and "promotes" that span up to block level.
    '''
    name: str
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Sections(Processor):
    '''
    Sets the "text" on sections if it wasn\'t given, and changes the "type" of
    plain items inside a section to a type based on the section name. For
    example, a plain item inside a `@properties` section becomes type
    `properties_item`.
    '''
    name: str
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context, itemtype: str | None = None) -> None: ...

class Includes(Processor):
    """
    Finds include directives and replaces them with the included wiki content.
    """
    name: str
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Templates(Modifier):
    name: str
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context, defns: Context | None = None) -> None: ...

class Tables(Processor):
    """
    Because of the way simple tables are marked up, you end up with a cell block
    for each row, where each rightward cell is the only child of the cell to its
    left. This processor re-organizes this into a more render-friendly
    structure.
    """
    name: str
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class RenumberHeadings(Processor):
    '''
    Adds "level" keys to headings indicating their level in the heading
    hierarchy.
    '''
    name: str
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context, level: int = 2) -> None: ...

class LinkProcessor(Processor):
    """
    Base class for processors of links.
    """
    def apply(self, block: _WikiBlock, context: Context, basepath: str | None = None) -> None: ...
    def text(self, context: Context, text: Iterable[str | _WikiSpan], basepath: str) -> None: ...
    def link(self, context: Context, span: _WikiSpan, basepath: str) -> None: ...

class FullPaths(LinkProcessor):
    """
    Finds links in the content, and annotates them with the absolute path to the
    linked page.
    """
    name: str
    def link(self, context: Context, span: _WikiSpan, basepath: str) -> None: ...

class TextModifier(Modifier):
    """
    Special subclass of Modifier that only modifies text nodes.
    """
    def modify(self, block: _WikiBlock, context: Context) -> None: ...
    def text(self, text: list[str | _WikiSpan], context: Context) -> list[str | _WikiSpan]: ...

class JoinText(TextModifier):
    '''
    Joins adjacent runs of text together, so `["foo", "bar"]` becomes
    `["foobar"]`.
    '''
    name: str
    def text(self, text: list[str | _WikiSpan], context: Context) -> list[str | _WikiSpan]: ...

class JoinKeys(TextModifier):
    """
    Coalesces consecutive keys spans.
    """
    name: str
    def text(self, text: list[str | _WikiSpan], context: Context) -> list[str | _WikiSpan]: ...

class Shortcuts(TextModifier):
    """
    Finds shortcuts and looks for a method corresponding to the shortcut's
    scheme to process it. You must subclass this to get it to do anything.
    """
    name: str
    def text(self, text: list[str | _WikiSpan], context: Context) -> list[str | _WikiSpan]: ...

class Metadata(Processor):
    """
    Adds some simple metadata to the JSON after it's generated.
    """
    name: str
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class AnnotateLinks(LinkProcessor):
    """
    Finds links in the content, looks up the linked document in the search
    index, and adds annotations to the link based on the linked document's
    search fields.
    """
    attrs: list[str]
    name: str
    default_attrs: list[str]
    def __init__(self, attrs: str | Iterable[str] | None = None) -> None: ...
    def add_attrs(self, *attrs: str) -> None: ...
    def link(self, context: Context, span: _WikiSpan, basepath: str) -> None: ...

class RunSearches(Processor):
    """
    Finds various items that run searches and replaces them with the search
    results.
    """
    name: str
    default_fields: list[str]
    @staticmethod
    def get_results(block: _WikiBlock, context: Context) -> Results | None: ...
    def apply(self, block: _WikiBlock, context: Context, root: _WikiBlock | None = None) -> None: ...

class Parents(Processor):
    """
    Annotates the current document with information about its parent documents,
    including their subtopics, allowing the template to display things like
    breadcrumbs and a tree view.
    """
    name: str
    @staticmethod
    def get_parent_path(pages: WikiPages, path: str, block: _WikiBlock) -> str: ...
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Toc(Processor):
    name: str
    before: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class BackLinks(Processor):
    name: str
    before: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class Flow(Processor):
    name: str
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...

class DeleteNotImplemented(Processor):
    name: str
    after: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context, root: bool = True) -> None: ...

class PythonAPI(Processor):
    name: str
    before: tuple[str, ...]
    def apply(self, block: _WikiBlock, context: Context) -> None: ...
    def process_indexed(self, pages: WikiPages, block: _WikiBlock, doc: _SearchDoc, cache: _IndexCache) -> None: ...

default_preprocessor_classes: tuple[type[Processor], ...]
default_postprocessor_classes: tuple[type[Processor], ...]

class CircularDependencyError(Exception): ...

class DependencyGraph:
    def __init__(self, vs: list[str] | None = None) -> None: ...
    def add(self, v: str) -> None: ...
    def depends_on(self, v: str, prereq: str) -> None: ...
    def resolve(self, vs: Iterable[str] | None = None) -> Generator[str, None, None]: ...

def make_pipeline(objs: Sequence[Processor]) -> Pipe: ...
def default_pre_pipeline() -> Pipe: ...
def default_post_pipeline() -> Pipe: ...
