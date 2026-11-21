import jinja2
from . import functions as functions, includes as includes, indexing as indexing, zones as zones
from .blocks import BlockType as BlockType, Root as Root, SpanType as SpanType, Text as Text, WikiType as WikiType
from .config import Config as Config
from .paths import WikiPath as WikiPath
from collections.abc import Iterator
from typing import Generic, Iterable, Self, Sequence

from typing import TypeVar
from collections.abc import Hashable
from typing import TypeVar
_H = TypeVar('_H', bound=Hashable)
PRE_PROC_KEY: str
POST_PROC_KEY: str

class Processor:
    name: str
    before: Sequence[str]
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...
    def process_indexed(self, zone: zones.Zone, block: BlockType, doc: indexing.Document) -> None: ...

class Modifier(Processor):
    """
    A type of Processor that only modifies a single block at a time (that is,
    that doesn't care about hierarchy). This allows them to be grouped together
    in a MultiModifier.
    """
    def modify(self, block: BlockType, context: zones.WikiContext) -> None: ...
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class MultiModifier(Modifier):
    """
    Processor that wraps multiple Modifier objects. This object walks the
    document tree and calls each modifier on each block.
    """
    modifiers: list[Modifier]
    def __init__(self, modifiers: Sequence[Modifier] = ...) -> None: ...
    def add(self, modifier: Modifier) -> None: ...
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

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
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class SortHeadings(Processor):
    '''
    Implements "linear" header style, where blocks simply come after headers at
    the same indent, instead of being indented under the heading. This processor
    looks for headings without bodies and pulls any subsequent blocks into them.
    '''
    name: str
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class Groups(Processor):
    '''
    Groups blocks of the same type "N" under "group_N" superblocks.
    '''
    types: frozenset[str]
    blacklist: frozenset[str]
    name: str
    after: Sequence[str]
    def __init__(self, types: Iterable[str] = ('bullet', 'ord', 'dt', 'item'), blacklist: Iterable[str] = ('billboard', 'null', 'include')) -> None: ...
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class Properties(Processor):
    '''
    Changes "property" blocks into attributes on the parent block.
    Make sure this runs after Hierarchy.
    '''
    name: str
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class EmptyBlocks(Processor):
    """
    Removes blocks without any content. Ignores certain things.
    """
    name: str
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class Promote(Processor):
    '''
    Finds blocks where a bit of xml or an include is the only thing in the
    block, and "promotes" that span up to block level.
    '''
    name: str
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class Sections(Processor):
    '''
    Sets the "text" on sections if it wasn\'t given, and changes the "type" of
    plain items inside a section to a type based on the section name. For
    example, a plain item inside a `@properties` section becomes type
    `properties_item`.
    '''
    name: str
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext, itemtype: str | None = None) -> None: ...

class Includes(Processor):
    """
    Finds include directives and replaces them with the included wiki content.
    """
    name: str
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class Templates(Modifier):
    name: str
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext, parent_defs: dict[str, jinja2.Template] | None = None) -> None: ...

class Tables(Processor):
    """
    Because of the way simple tables are marked up, you end up with a cell block
    for each row, where each rightward cell is the only child of the cell to its
    left. This processor re-organizes this into a more render-friendly
    structure.
    """
    name: str
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class RenumberHeadings(Processor):
    '''
    Adds "level" keys to headings indicating their level in the heading
    hierarchy.
    '''
    name: str
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext, level: int = 2) -> None: ...

class LinkProcessor(Modifier):
    """
    Base class for processors of links.
    """
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...
    def text(self, context: zones.WikiContext, text: Text) -> None: ...
    def link(self, context: zones.WikiContext, span: SpanType) -> None: ...

class FullPaths(LinkProcessor):
    """
    Finds links in the content, and annotates them with the absolute path to the
    linked page.
    """
    name: str
    def link(self, context: zones.WikiContext, span: SpanType) -> None: ...

class TextModifier(Modifier):
    """
    Special subclass of Modifier that only modifies text nodes.
    """
    def modify(self, block: BlockType, context: zones.WikiContext) -> None: ...
    def text(self, text: Text, context: zones.WikiContext) -> Text: ...

class JoinKeys(TextModifier):
    """
    Coalesces consecutive keys spans.
    """
    name: str
    def text(self, text: Text, context: zones.WikiContext) -> Text: ...

class Shortcuts(TextModifier):
    """
    Finds shortcuts and looks for a method corresponding to the shortcut's
    scheme to process it. You must subclass this to get it to do anything.
    """
    name: str
    def text(self, text: Text, context: zones.WikiContext) -> Text: ...

class AnnoteteLinks(LinkProcessor):
    def link(self, context: zones.WikiContext, span: SpanType) -> None: ...
    @staticmethod
    def annotate(context: zones.WikiContext, span: SpanType, path: WikiPath) -> None: ...

class RunSearches(Modifier):
    """
    Finds various items that run searches and replaces them with the search
    results.
    """
    name: str
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class Parents(Processor):
    """
    Annotates the current document with information about its parent documents,
    including their subtopics, allowing the template to display things like
    breadcrumbs and a tree view.
    """
    name: str
    @classmethod
    def parent_page(cls, zone: zones.Zone, path: WikiPath, block: BlockType) -> WikiPath: ...
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class Flow(Processor):
    name: str
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class DeleteNotImplemented(Processor):
    name: str
    after: Sequence[str]
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...

class DependencyGraph(Generic[_H]):
    def __init__(self, values: Sequence[_H] = ...) -> None: ...
    def add(self, value: _H) -> None: ...
    def dependency(self, value: _H, prereq: _H) -> None: ...
    def resolve(self, values: Sequence[_H] = ...) -> Iterator[_H]: ...

class Pipeline(Processor):
    procs: list[Processor]
    def __init__(self, procs: Sequence[Processor] = ...) -> None: ...
    @classmethod
    def with_procs(cls, procs: Sequence[Processor]) -> Self: ...
    def add(self, proc: Processor) -> None: ...
    def apply(self, block: BlockType, context: zones.WikiContext) -> None: ...
    def process_indexed(self, zone: zones.Zone, block: BlockType, doc: indexing.Document) -> None: ...

def default_pre_list() -> Sequence[Processor]: ...
def default_post_list() -> Sequence[Processor]: ...
def pipelines_from_config(config: Config) -> tuple[Processor, Processor]: ...
