import flask
import hou
import re
import threading
import whoosh.index
from bookish import util as util
from bookish.search import WhooshSearcher
from bookish.wiki.wikipages import WikiPages, _WikiBlock
from collections import namedtuple as namedtuple
from collections.abc import Callable as Callable, MutableSet, Sequence
from houdinihelp.htextify import HoudiniTextifier as HoudiniTextifier
from typing import Literal, NamedTuple
from typing_extensions import TypedDict, Unpack
from urllib.parse import ParseResult as ParseResult, quote as quote

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
class _AssetIndexingKwargs(TypedDict, total=False):
    asset_definition: hou.HDADefinition
    asset_name: str
    library_path: str
    node_type_category: hou.OpNodeTypeCategory

initialized: bool
bookish_app: flask.Flask | None
bookish_searcher: WhooshSearcher | None
ram_index: whoosh.index.Index
indexing_work_queue: list[tuple[hou.EnumValue[hou.hdaEventType] | None, _AssetIndexingKwargs]]
table_to_dir: dict[str, str]
url_schemes: list[str]
dir_to_table: dict[str, str]
load_script_path: str
tooltip_regex: re.Pattern[str]

def memoize(func: Callable[..., _T]) -> Callable[..., _T]: ...

class FastExitException(Exception): ...

def patch_socket_server_error_handler() -> None: ...
def initialize(*args: object, **kwargs: object) -> None: ...
def getHelpForId(helpid: str) -> str | None: ...
def getParmTooltipFromPath(path: str, parm_token: str, parm_label: str, is_spare: bool, pages: WikiPages | None = None) -> str | None: ...
def getParmTooltip(op_table_name: str, op_type: str, version: str | None, namespace: str | None, scopeop: str | None, parm_token: str, parm_label: str, is_spare: bool) -> str | None: ...

class ParmSpec(NamedTuple):
    table: str
    scopeop: str
    namespace: str
    corename: str
    version: str
    nodepath: str
    name: str
    label: str
    path: str

def decodeParmUrl(parsed: ParseResult) -> ParmSpec: ...
def urlToPath(url: str, snap_version: bool = True, maybe_manager: bool = True) -> str | Literal[False]:
    '''
    Translates a URL from Houdini (e.g. "op:Sop/copy") and translates it into
    a help server path (e.g. "/nodes/sop/copy").
    '''
def hasHelp(url: str) -> bool:
    '''
    Returns True if the URL is something the help system can handle, e.g.
    "op:Object/geo".
    '''
def nodeHasHelp(pages: WikiPages, nodetype: hou.OpNodeType) -> bool: ...
def load_json(path: str, pages: WikiPages | None = None, follow_redirects: bool = False, history: tuple[str, ...] = ...) -> _WikiBlock | None: ...
def getTooltip(url: str) -> str | None: ...
def getFormattedTooltip(url: str) -> str | None: ...
def getTextHelp(url: str) -> str | None: ...
def get_textified(path: str) -> str | None: ...
def commandTextHelp(command_name: str) -> str | None: ...
def expressionTextHelp(function_name: str) -> str | None: ...
def commandKeywordSearch(kw: str) -> list[str]: ...
def expressionKeywordSearch(kw: str) -> list[str]: ...
def configTextHelp(var_name: str) -> str | None: ...
def getParsedHtmlHelp(url: str, content: str | bytes) -> str | None: ...
def getParsedTooltip(url: str, content: str | bytes) -> str | None: ...
def startHelpServer(port_callback: Callable[[int], object] | None = None, address: str = '0.0.0.0', port: int = 48626, use_ipv6: bool = False, threads: int = 1) -> int: ...
def start_hwebserver(app: flask.Flask, address: str = '0.0.0.0', port: int = 48626, allow_system_port: bool = False, use_ipv6: bool = False, port_cb: Callable[[str, int], object] | None = None, port_name: str = 'help', in_background: bool = False, threads: int = 1) -> int: ...

asset_indexer_threads: list['AssetIndexer']

def async_raise(thread_obj: threading.Thread, exception: type[BaseException] | BaseException) -> None: ...
def cleanup_asset_indexer_threads() -> None:
    """
    Clean up asset indexer threads.
    """
def setup_asset_indexing() -> None: ...
def asset_indexing_event(event_type: hou.EnumValue[hou.hdaEventType] | None, **kwargs: Unpack[_AssetIndexingKwargs]) -> None: ...

class AssetIndexer(threading.Thread):
    indexer: None
    def __init__(self) -> None: ...
    def run(self) -> None: ...

def nodeHelpTemplate(table: str, namespace: str | None, name: str, version: str | None) -> str: ...
def gather_node_paths(node: hou.Node, pathset: MutableSet[str]) -> None: ...
def open_wiki_preview(baseurl: str, path: str, content: str) -> None: ...
def get_pages(app: flask.Flask | None = None) -> WikiPages: ...
def get_searcher() -> WhooshSearcher: ...
def hstring(text: object) -> str: ...
def find_parm(root: _WikiBlock | Sequence[_WikiBlock], parmid: str, label: str) -> _WikiBlock | None:
    """
    Tries to find a parameter in a help document, based on the parameter ID and
    its label.
    """
def load_example(source: str, launch: bool = False) -> str | None: ...
def components_to_path(table: str | None, scopeop: str | None, ns: str | None, name: str, version: str | None, snap_version: bool = True, maybe_manager: bool = False, pages: WikiPages | None = None) -> str: ...
def components_to_nodetype(table: str, scopeop: str | None, namespace: str | None, corename: str, version: str | None) -> hou.NodeType | None: ...
def nodetype_to_path(nodetype: hou.NodeType, snap_version: bool = False, pages: WikiPages | None = None) -> str:
    """
    Takes a ``hou.NodeType`` object and returns the equivalent help path.
    """

node_path_exp: re.Pattern[str]
node_filename_exp: re.Pattern[str]

class NodeInfo(NamedTuple):
    table: str
    scopeop: str | None
    namespace: str | None
    corename: str
    version: str | None
    ext: str
    section: str | None
    fragment: str | None

def path_to_components(path: str) -> NodeInfo | None:
    '''
    Takes a help path and returns a named tuple of the following components:

    * ``table`` - the node category name, e.g. ``Object``.
    * ``scopeop`` - if the node has a scope, the name of the scope node,
        otherwise an empty string.
    * ``namespace`` - the node\'s namespace, or an empty string.
    * ``name`` - the node\'s "core" name.
    * ``version`` - the node\'s version string.
    * ``ext`` - the filename extension given in the path (if any).
    * ``section`` - an asset section name, or an empty string.
    '''
def path_to_nodetype(path: str) -> hou.NodeType | None: ...
def load_module_from_houdini(module_name: str, search_distro: bool = True, search_houdini_modules: bool = True) -> None: ...
