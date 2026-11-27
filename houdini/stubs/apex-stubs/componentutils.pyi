import apex
import hou
import typing
from collections.abc import Iterable, Mapping, Sequence
from houtypes import HDANodeEventKwargs, ParmCallbackKwargs
from typing import Literal
from typing_extensions import Required, TypedDict, Unpack

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
class _DsCategory(TypedDict):
    """A folder of the dialog script `dsFromGraphInputs` builds: a `parmoptions` category, or a multiparm."""
    name: str
    parms: list[str]
    existing_parms: list[str]
    type: str

class _ParmMetadata(TypedDict, total=False):
    """A parm's entry in the `metadata` of a graph's (deprecated) `parmoptions`: only some keys' presence matters."""
    joinnext: hou._OptionValue
    isLabelHidden: hou._OptionValue
    disableWhen: str
    help: str
    ramp: str

class _ParmTypeHint(TypedDict, total=False):
    parms: Required[tuple[str, ...]]
    type: Required[str]
    defaults: tuple[str, ...]

class _ParmCategory(TypedDict):
    name: str
    parms: tuple[str, ...]

class _ParmOptions(TypedDict, total=False):
    """The (deprecated) `parmoptions` dictionary of a graph's `properties` (or its own detail attribute)."""
    metadata: dict[str, _ParmMetadata]
    typehints: tuple[_ParmTypeHint, ...]
    hidden: tuple[str, ...]
    categories: tuple[_ParmCategory, ...]

class _ParmTupleEventKwargs(TypedDict):
    event_type: hou.EnumValue[hou.nodeEventType]
    parm_tuple: hou.ParmTuple | None

COMPONENTSCRIPT_TXT_WARNING: str
COMPONENTSCRIPT_TITLE_WARNING: str
COMPONENTSCRIPT_DETAILS_WARNING: str
COMPONENTSCRIPT_NULL: str
COMPONENTSCRIPT_PARMNODE: str
COMPONENTSTRIPT_SOURCE_PARM: str
COMPONENTSCRIPT_PARM_BLACKLIST: list[str]
COMPONENTSCRIPT_SETUP_FOLDER: str
COMPONENTSCRIPT_SETUP_TUPLE: tuple[str, str]
COMPONENTSCRIPT_PARM_FOLDER: str
COMPONENTSCRIPT_ANIM_FOLDER: str
COMPONENTSCRIPT_SETUP_MULTI: str
COMPONENTSCRIPT_ANIM_PARMS: list[str]
GRAPH_NULL: str
GRAPH_PARMNODE: str
GRAPH_SETUP_FOLDER: str
type_info: dict[str, tuple[str, int]]
begin_templ: str
end_templ: str
entry_templ: str
begin_tab_templ: str
end_tab_templ: str
menu_templ: str
menu_entry_temp: str
toggle_templ: str
TOGGLE_MENU_TEMPL: str
FLOAT_RAMP_TEMPL: str
COLOR_RAMP_TEMPL: str

def getDictArrayKeys(parms: Iterable[_T]) -> list[_T]:
    """returns the keys containing a dict array of a dict. This is needed for filtering out multiparm entries of the attribform parm style dict"""
def getValueInfo(value: object) -> tuple[Literal['string', 'multiparm', 'vector', 'int', 'float'], int] | None:
    """returns the value info of a given value formatted in the the ds style """
def dsMenuTemplate(name: str, entries: Iterable[str], add_overrride_toggles: bool = False, joinnext: str = '', help: str = '') -> str:
    """create ds menu template for a menu with the given name and entries"""
def dsParmTemplate(name: str, type_info: tuple[str, int], parm_options: _ParmOptions | None = None, add_overrride_toggles: bool = False, namespace: str | None = None) -> str: ...
def addMultiparmCategory(parms: Mapping[str, hou._OptionValue], multi_name: str, all_names: list[str], all_categories: list[_DsCategory], parm_options: _ParmOptions, add_overrride_toggles: bool = False, namespace: str | None = None) -> None: ...
def addDsCategory(ds: str, category: _DsCategory, all_category_names: Sequence[str], all_categories: Sequence[_DsCategory], built_categories: list[str]) -> tuple[str, list[str]]: ...
@typing.overload
def dsFromGraphInputs(apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool = ..., namespace: str | None = ..., getParms: Literal[False] = ...) -> str: ...
@typing.overload
def dsFromGraphInputs(apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool = ..., namespace: str | None = ..., *, getParms: Literal[True]) -> tuple[str, list[str]]: ...
@typing.overload
def dsFromGraphInputs(apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool, namespace: str | None, getParms: Literal[True]) -> tuple[str, list[str]]: ...
@typing.overload
def dsFromGraphInputs(apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool = ..., namespace: str | None = ..., getParms: bool = ...) -> str | tuple[str, list[str]]: ...
def setParm(node: hou.OpNode, parm: str, value: hou._OptionValue) -> None:
    """Sets the parm value for a node. Multiparms and parm tuples will automatically detected and the values will be 
    accordingly set for those types as well. Only existing parms will be set. 
    :param node: the hou.Node 
    :param parm: the name of the parm to be set
    :param value: the value of the parm to be set. 
    """
def saveParmValues(node: hou.OpNode) -> tuple[hou._OptionDict, bytes | None]:
    """stores the current values based on an attrib from parm format plus the clip data of a given set of parms. This will be in the future replaces by the node.asData() api. """
def restoreParmValues(node: hou.OpNode, attr_parms: Mapping[str, hou._OptionValue], data: bytes | None, parentfolder: str | None = None, default_dict: Mapping[str, hou._OptionValue] | None = None) -> None:
    """reapllies values plus keyed clip data to a given set of parms. This will be in the future replaces by the node.asData() api. """
def rigParmsFromGraph(node: hou.OpNode, graph_geo: hou.Geometry, graph: apex.Graph, name: str, namespace: str = '', parentfolder: str | None = None) -> list[str]: ...
def parms_from_graph(kwargs: ParmCallbackKwargs) -> None: ...
def componentParmsFromGraph(kwargs: ParmCallbackKwargs) -> None: ...
def clearComponentAnimationParms(node: hou.OpNode) -> None: ...
def updateComponentAnimationParms(kwargs: ParmCallbackKwargs) -> None: ...
def addUpdateRigNodeCallback(kwargs: HDANodeEventKwargs) -> None: ...
def removeUpdateRigNodeCallback(kwargs: HDANodeEventKwargs) -> None: ...
def updateRigNode(node: hou.OpNode, **kwargs: Unpack[_ParmTupleEventKwargs]) -> None: ...
