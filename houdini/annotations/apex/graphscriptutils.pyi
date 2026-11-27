from collections.abc import Iterable, Sequence
from typing import Generic, TypeAlias, TypeVar

import _apex
import apex
import hou
from houtypes import JSONValue

_T = TypeVar("_T", bound=_apex._ValueArg)

# An argument spec of FuncMapping: the name of both the script argument and the port,
# (name,), (argument name, port name) or (argument name, port name, default).
_FuncArgSpec: TypeAlias = str | tuple[str] | tuple[str, str] | tuple[str, str, _apex._ValueArg]

GRAPH_TYPE: str
VECTOR3_TYPE: str
INT_TYPE: str
FLOAT_TYPE: str
STRING_TYPE: str
VECTOR2_TYPE: str
VECTOR4_TYPE: str
MATRIX3_TYPE: str
MATRIX4_TYPE: str
GEOMETRY_TYPE: str
DICT_TYPE: str
BOOL_TYPE: str
NODEID_TYPE: str
PORTID_TYPE: str
FLOATRAMP_TYPE: str
COLORRAMP_TYPE: str
ARRAY_INDICATOR: str
VALUE_TYPES: set[str]
cb_load: str
VALUE_DEFAULTS: dict[str, bool | int | float | tuple[float, ...]]
SIMPLE_COPY_TYPES: set[str]
LOOP_CALLBACKS: tuple[str, str, str, str, str, str, str, str, str, str]
COND_CALLBACKS: tuple[str, str]
METADATA_SCOPE_FUNCTIONS: list[str]
METADATA_SUBNET_FUNCTIONS: list[str]
CUSTOM_FUNCS: list[str]
VERB_ALLOWED_ARG_TYPES: dict[str, list[str]]
TYPE_COMPATIBILITY: dict[str, str]

def matchAnyFuncName(func_name: str, test_names: Iterable[str], starts_with: bool = ...) -> bool: ...
def remapTypeCompatibility(type_name: str) -> str: ...

RAMP_BASIS_EQUIV: list[tuple[hou.EnumValue[hou.rampBasis], str]]
RAMP_STR_TO_BASIS: dict[str, hou.EnumValue[hou.rampBasis]]
RAMP_BASIS_TO_STR: dict[hou.EnumValue[hou.rampBasis], str]
RAMP_BASIS_TO_INT: dict[hou.EnumValue[hou.rampBasis], int]
RAMP_COLORTYPE_EQUIV: list[tuple[hou.EnumValue[hou.colorType], str]]
RAMP_COLORTYPE_TO_STR: dict[hou.EnumValue[hou.colorType], str]
RAMP_STR_TO_COLORTYPE: dict[str, hou.EnumValue[hou.colorType]]

def strToRampBasis(basis_str: str) -> hou.EnumValue[hou.rampBasis]: ...
def rampBasisToStr(basis: hou.EnumValue[hou.rampBasis]) -> str: ...
def rampBasisToInt(basis: hou.EnumValue[hou.rampBasis]) -> int: ...
def intToRampBasis(basis_int: int) -> hou.EnumValue[hou.rampBasis]: ...
def strListToRampBasisList(basis_str: Iterable[str]) -> list[hou.EnumValue[hou.rampBasis]]: ...
def rampBasisListToStrList(basis: Iterable[hou.EnumValue[hou.rampBasis]]) -> list[str]: ...
def intListToRampBasisList(basis_int: Iterable[int]) -> list[hou.EnumValue[hou.rampBasis]]: ...
def rampBasisListToIntList(basis: Iterable[hou.EnumValue[hou.rampBasis]]) -> list[int]: ...
def rampColorTypeToStr(colortype: hou.EnumValue[hou.colorType]) -> str: ...
def rampStrToColorType(colortype: str) -> hou.EnumValue[hou.colorType]: ...

class FuncArgMapping:
    index: int
    default: _apex._ValueArg | None
    arg: str | None
    port: str | None
    def __init__(
        self, argname: str | None = ..., portname: str | None = ..., index: int = ..., default: _apex._ValueArg | None = ...
    ) -> None: ...

class FuncMapping:
    func_name: str
    callback_name: str
    valuetype: str
    inplace: bool
    arg_mappings: list[FuncArgMapping]
    def __init__(
        self,
        func_name: str,
        callback_name: str,
        args: Iterable[_FuncArgSpec] | None = ...,
        valuetype: str = ...,
        inplace: bool = ...,
    ) -> None: ...
    def addArgs(self, args: Iterable[_FuncArgSpec]) -> None: ...
    def findArg(self, index: int) -> str | None: ...
    def findPort(self, index_or_name: int | str) -> str | None: ...
    def findDefault(self, index: int) -> _apex._ValueArg | None: ...

class FuncMappingCollection:
    def __init__(self) -> None: ...
    def add(self, mapping: FuncMapping, valuetype: str | None = ...) -> None: ...
    def extend(self, mapping_lst: Iterable[FuncMapping], valuetype: str | None = ...) -> None: ...
    def findCallback(self, callback_name: str | None = ...) -> list[FuncMapping]: ...
    def findFunc(self, func_path: str | None = ...) -> list[FuncMapping]: ...
    def filterFuncs(self, pattern: str) -> list[FuncMapping]: ...
    def filterCallbacks(self, pattern: str) -> list[None]: ...

GRAPH_CALLBACK_MAPPING: tuple[FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping]
DICT_CALLBACK_MAPPING: tuple[FuncMapping]
GEO_CALLBACK_MAPPING: tuple[FuncMapping, FuncMapping]
VECTOR3_CALLBACK_MAPPING: tuple[FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping]
VECTOR_COMPONENTS: tuple[str, str, str, str]
VECTOR_NUM_COMPONENTS: dict[str, int]
VECTOR_COMP_CALLBACK_MAPPINGS: dict[str, list[FuncMapping]]
MATRIX4_CALLBACK_MAPPING: tuple[FuncMapping]
APEX_PORTID_CALLBACK_MAPPING: tuple[FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping]
APEX_NODEID_CALLBACK_MAPPING: tuple[FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping, FuncMapping]
FUNC_MAPPINGS: FuncMappingCollection
CALLBACK_PRIORITY: dict[str, int]

class ConstantId(Generic[_T]):
    name: str
    typename: str
    val: _T
    def __init__(self, name: str, typename: str, val: _T) -> None: ...
    def getValue(self) -> _T: ...

CONSTANT_DEFINITIONS: dict[str, ConstantId[float] | ConstantId[hou.Vector3]]

def lookupConstant(name: str) -> ConstantId[float] | ConstantId[hou.Vector3] | None: ...
def getTypeDefault(valuetype: str) -> bool | int | float | tuple[float, ...] | str: ...
def findPriorityCallback(callback_names: Sequence[str]) -> str | None: ...
def callbackNameToFuncName(callback_name: str, strip_all_namespaces: bool = ...) -> tuple[str | None, str]: ...
def getGraphNodeNestingLevel(node: int, graph: apex.Graph) -> int: ...
def isGraphNodeInScope(node: int, scope_id: int, graph: apex.Graph) -> bool: ...
def colorNodesFromLineno(graph: apex.Graph, color: hou.Vector3, lines: Iterable[int]) -> None: ...
def getSnippetIndictators(indicator: str) -> tuple[str, str]: ...
def extractFromIndicators(script: str, indicator: str, strip: bool = ...) -> tuple[str, str]: ...
def saveSnippetAsText(
    path: str,
    snippet: str,
    properties: hou._OptionDict | None = ...,
    header: str | None = ...,
    header_mode: int | None = ...,
    footer: str | None = ...,
    sourcescript: bool = ...,
) -> None: ...
def loadSnippetFromText(
    path: str,
    extract_header: bool = ...,
    apply_properties: bool = ...,
    keep_properties_snippet: bool = ...,
    script: str | None = ...,
) -> (
    tuple[str, int, str | None, str | None, str, None, str]
    | tuple[None, int, None, None, None, str, str]
    | None
): ...
def applyTextToNode(
    path: str,
    # Sets its parameters (a SOP's, from its parameter callbacks).
    node: hou.OpNode,
    extract_header: bool = ...,
    apply_properties: bool = ...,
    keep_properties_snippet: bool = ...,
    parmfolder: str | None = ...,
    parmblacklist: Sequence[str] | None = ...,
    snippet_parm: str = ...,
    footer_parm: str | None = ...,
    header_parm: str | None = ...,
    headertemplate_parm: str | None = ...,
    useheader_parm: str | None = ...,
    editheader_parm: str | None = ...,
    usehoudiniversion_parm: str | None = ...,
    houdiniversion_parm: str | None = ...,
    subgraph_parm: str | None = ...,
    usesubgraph_parm: str | None = ...,
    snippet: str | None = ...,
) -> dict[str, JSONValue] | None: ...

class SubgraphLibCache:
    default_path: str | None
    clear_existing: bool
    reload_existing: bool
    reload_subgraphs: bool
    pack_to_geo: hou.Geometry | None
    registry: apex.Registry
    cache_for_preview: bool
    def __init__(
        self,
        default_path: str | None = ...,
        clear_existing: bool = ...,
        reload_existing: bool = ...,
        pack_to_geo: hou.Geometry | None = ...,
        preview: bool = ...,
        reload_subgraphs: bool = ...,
    ) -> None: ...
    def addSubgraph(self, subgraph: apex.Graph, subgraphname: str, subgraphlibpath: str | None = ...) -> None: ...
    def writeOut(self, show_message: bool = ..., snippet: str | None = ...) -> bool: ...
    def createSubgraphPreview(self) -> apex.Graph: ...

graphexamples: dict[str, str]
