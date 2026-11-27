from collections.abc import Iterable, Mapping, Sequence
from typing import Literal, TypeVar, overload

import apex
import hou
from houtypes import HDANodeEventKwargs, ParmCallbackKwargs
from typing_extensions import Required, TypedDict, Unpack

_T = TypeVar("_T")

class _DsCategory(TypedDict):
    """A folder of the dialog script `dsFromGraphInputs` builds: a `parmoptions` category, or a multiparm."""

    name: str
    parms: list[str]
    existing_parms: list[str]
    """Each parm's dialog script, or `"__NONE__"` for a parm not built (yet)."""
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

COMPONENTSCRIPT_PARM_BLACKLIST: list[str]
COMPONENTSCRIPT_SETUP_TUPLE: tuple[str, str]
COMPONENTSCRIPT_ANIM_PARMS: list[str]
type_info: dict[str, tuple[str, int]]

# Dead code: it keeps the lists among `parms` whose first item is a dict.
def getDictArrayKeys(parms: Iterable[_T]) -> list[_T]: ...
def getValueInfo(value: object) -> tuple[Literal["string", "multiparm", "vector", "int", "float"], int] | None: ...
def dsMenuTemplate(name: str, entries: Iterable[str], add_overrride_toggles: bool = ..., joinnext: str = ..., help: str = ...) -> str: ...
def dsParmTemplate(
    name: str,
    type_info: tuple[str, int],
    parm_options: _ParmOptions | None = ...,
    add_overrride_toggles: bool = ...,
    namespace: str | None = ...,
) -> str: ...
def addMultiparmCategory(
    parms: Mapping[str, hou._OptionValue],
    multi_name: str,
    all_names: list[str],
    all_categories: list[_DsCategory],
    parm_options: _ParmOptions,
    add_overrride_toggles: bool = ...,
    namespace: str | None = ...,
) -> None: ...
def addDsCategory(
    ds: str, category: _DsCategory, all_category_names: Sequence[str], all_categories: Sequence[_DsCategory], built_categories: list[str]
) -> tuple[str, list[str]]: ...
@overload
def dsFromGraphInputs(
    apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool = ..., namespace: str | None = ..., getParms: Literal[False] = ...
) -> str: ...
@overload
def dsFromGraphInputs(
    apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool = ..., namespace: str | None = ..., *, getParms: Literal[True]
) -> tuple[str, list[str]]: ...
@overload
def dsFromGraphInputs(
    apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool, namespace: str | None, getParms: Literal[True]
) -> tuple[str, list[str]]: ...
@overload
def dsFromGraphInputs(
    apexgraph: hou.Geometry, graph: apex.Graph, add_overrride_toggles: bool = ..., namespace: str | None = ..., getParms: bool = ...
) -> str | tuple[str, list[str]]: ...
def setParm(node: hou.OpNode, parm: str, value: hou._OptionValue) -> None: ...
def saveParmValues(node: hou.OpNode) -> tuple[hou._OptionDict, bytes | None]: ...
def restoreParmValues(
    node: hou.OpNode,
    attr_parms: Mapping[str, hou._OptionValue],
    data: bytes | None,
    parentfolder: str | None = ...,
    default_dict: Mapping[str, hou._OptionValue] | None = ...,
) -> None: ...
def rigParmsFromGraph(
    node: hou.OpNode, graph_geo: hou.Geometry, graph: apex.Graph, name: str, namespace: str = ..., parentfolder: str | None = ...
) -> list[str]: ...
def parms_from_graph(kwargs: ParmCallbackKwargs) -> None: ...
def componentParmsFromGraph(kwargs: ParmCallbackKwargs) -> None: ...
def clearComponentAnimationParms(node: hou.OpNode) -> None: ...
def updateComponentAnimationParms(kwargs: ParmCallbackKwargs) -> None: ...
def addUpdateRigNodeCallback(kwargs: HDANodeEventKwargs) -> None: ...
def removeUpdateRigNodeCallback(kwargs: HDANodeEventKwargs) -> None: ...
def updateRigNode(node: hou.OpNode, **kwargs: Unpack[_ParmTupleEventKwargs]) -> None: ...
