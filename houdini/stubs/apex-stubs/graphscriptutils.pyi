import _apex
import apex
import hou
from collections.abc import Iterable, Sequence
from houtypes import JSONValue
from typing import Generic

from typing import TypeAlias
from typing import TypeVar
from typing import TypeAlias
from typing import TypeVar
_T = TypeVar('_T', bound=_apex._ValueArg)
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
SPARE_PORT_NAME: str
VALUE_TYPES: set[str]
cb_load: str
VALUE_DEFAULTS: dict[str, bool | int | float | tuple[float, ...]]
SIMPLE_COPY_TYPES: set[str]
PROP_SCOPES: str
PROP_CONTAINING_SCOPE: str
PROP_LINENO: str
PROP_CURRENT_SCOPE: str
LOOP_CALLBACKS: tuple[str, str, str, str, str, str, str, str, str, str]
COND_CALLBACKS: tuple[str, str]
METADATA_FUNC_INPUT: str
METADATA_FUNC_OUTPUT: str
METADATA_FUNC_BEGIN: str
METADATA_FUNC_END: str
METADATA_SCOPE_FUNCTIONS: list[str]
METADATA_SUBNET_FUNCTIONS: list[str]
STICKY_NOTE_FUNC: str
HOUDINI_VERSION_FUNC: str
PORT_ALIAS_FUNCTION: str
FUNC_SETGRAPH: str
FUNC_LEN: str
FUNC_RANGE: str
FUNC_ENUMERATE: str
FUNC_INVOKE: str
FUNC_ISDEFAULT: str
FUNC_SETPRESET: str
FUNC_ADDTOFOLDER: str
FUNC_BINDMULTI: str
FUNC_ADDTOMULTI: str
FUNC_SETPROPERTIES: str
FUNC_PRINT: str
FUNC_WARN: str
FUNC_ERROR: str
FUNC_BINDINPUT: str
FUNC_BINDOUTPUT: str
PRESET_KWARG: str
PRESET_KWARGS_KWARG: str
SUBGRAPH_DECORATOR: str
NAMESPACE_DECORATOR: str
SAFEGUARD_INPUTS_DECORATOR: str
CUSTOM_FUNCS: list[str]
VERB_ALLOWED_ARG_TYPES: dict[str, list[str]]
TYPE_COMPATIBILITY: dict[str, str]

def nameLower(func_name: str) -> str: ...
def nameUpper(func_name: str) -> str: ...
def matchFuncName(func_name: str, test_name: str, starts_with: bool = False) -> bool: ...
def matchAnyFuncName(func_name: str, test_names: Iterable[str], starts_with: bool = False) -> bool: ...
def remapTypeCompatibility(type_name: str) -> str: ...

RAMP_BASIS_EQUIV: list[tuple[hou.EnumValue[hou.rampBasis], str]]
RAMP_STR_TO_BASIS: dict[str, hou.EnumValue[hou.rampBasis]]
RAMP_BASIS_TO_STR: dict[hou.EnumValue[hou.rampBasis], str]
RAMP_BASIS_TO_INT: dict[hou.EnumValue[hou.rampBasis], int]
RAMP_COLORTYPE_EQUIV: list[tuple[hou.EnumValue[hou.colorType], str]]
RAMP_COLORTYPE_TO_STR: dict[hou.EnumValue[hou.colorType], str]
RAMP_STR_TO_COLORTYPE: dict[str, hou.EnumValue[hou.colorType]]

def strToRampBasis(basis_str: str) -> hou.EnumValue[hou.rampBasis]:
    """ Convert string to hou.rampBasis """
def rampBasisToStr(basis: hou.EnumValue[hou.rampBasis]) -> str:
    """ Convert hou.rampBasis to string. """
def rampBasisToInt(basis: hou.EnumValue[hou.rampBasis]) -> int:
    """ Convert hou.rampBasis to int. """
def intToRampBasis(basis_int: int) -> hou.EnumValue[hou.rampBasis]:
    """ Convert int to hou.rampBasis. """
def strListToRampBasisList(basis_str: Iterable[str]) -> list[hou.EnumValue[hou.rampBasis]]:
    """ Convert a list of strings to a list of hou.rampBasis. """
def rampBasisListToStrList(basis: Iterable[hou.EnumValue[hou.rampBasis]]) -> list[str]:
    """ Convert a list of hou.rampBasis to a list of strings. """
def intListToRampBasisList(basis_int: Iterable[int]) -> list[hou.EnumValue[hou.rampBasis]]:
    """ Convert a list of int to a list of hou.rampBasis. """
def rampBasisListToIntList(basis: Iterable[hou.EnumValue[hou.rampBasis]]) -> list[int]:
    """ Convert a list of hou.rampBasis to a list of int. """
def rampColorTypeToStr(colortype: hou.EnumValue[hou.colorType]) -> str:
    """ Convert hou.colorType to string. """
def rampStrToColorType(colortype: str) -> hou.EnumValue[hou.colorType]:
    """ Convert string to hou.colorType, default to RGB. """

class FuncArgMapping:
    """
    simple collector of the data relevant to map an arg from a graph script to a port on a callback. 
    """
    index: int
    default: _apex._ValueArg | None
    arg: str | None
    port: str | None
    def __init__(self, argname: str | None = None, portname: str | None = None, index: int = -1, default: _apex._ValueArg | None = None) -> None: ...

class FuncMapping:
    """
    contains all the mapping information necessary to alias an apex script function to a callback
    we allow 
    func name mappings, 
    arg name mappings, 
    a different arg index then port index
    different default parms
    """
    func_name: str
    callback_name: str
    valuetype: str
    inplace: bool
    arg_mappings: list[FuncArgMapping]
    def __init__(self, func_name: str, callback_name: str, args: Iterable[_FuncArgSpec] | None = None, valuetype: str = '', inplace: bool = False) -> None: ...
    @property
    def func_path(self) -> str: ...
    def addArgs(self, args: Iterable[_FuncArgSpec]) -> None:
        """add the args mappings based on a list of tuples"""
    def findArgMapping(self, index: int) -> FuncArgMapping: ...
    def findArg(self, index: int) -> str | None: ...
    def findPort(self, index_or_name: int | str) -> str | None: ...
    def findDefault(self, index: int) -> _apex._ValueArg | None: ...
    def buildDefaultsDict(self) -> apex.Dict: ...
    def mapObjectPortIndex(self, index: int) -> int: ...

class FuncMappingCollection:
    """
    contains all the function mappings we assemble, we can get the data either by searchy based on the function path
    aka the valuetype that the function is associated with plus its function name or by callback name
    """
    def __init__(self) -> None: ...
    def add(self, mapping: FuncMapping, valuetype: str | None = None) -> None: ...
    def extend(self, mapping_lst: Iterable[FuncMapping], valuetype: str | None = None) -> None: ...
    def findCallback(self, callback_name: str | None = None) -> list[FuncMapping]: ...
    def findFunc(self, func_path: str | None = None) -> list[FuncMapping]: ...
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
    def getTypename(self) -> str: ...
    def getName(self) -> str: ...
    def getValue(self) -> _T: ...

CONSTANT_DEFINITIONS: dict[str, ConstantId[float] | ConstantId[hou.Vector3]]

def lookupConstant(name: str) -> ConstantId[float] | ConstantId[hou.Vector3] | None:
    """ Lookup a predefined constant by name. """
def getTypeDefault(valuetype: str) -> bool | int | float | tuple[float, ...] | str: ...
def findPriorityCallback(callback_names: Sequence[str]) -> str | None:
    """
    Finds the callback from the list of provided callback names with the
    highest priority.

    If no entry in the list is listed in the priority list, return the first one.
    Otherwise, return the callback name that occurs in the priority list first.
    """
def isCallbackInplace(callback: str, registry: apex.Registry, mapping: FuncMapping | None = None, signature: apex.Signature | None = None, houdini_version: str = '') -> bool:
    """ Check if a callback is inplace. """
def callbackNameToFuncName(callback_name: str, strip_all_namespaces: bool = False) -> tuple[str | None, str]: ...
def callbackVerbInfo(callbackname: str) -> tuple[bool, list[str] | None]:
    """
    Given a callback name, return a tuple of whether the callback
    is a verb, and the allowed type to pass in as a regular arg
    or None if no type is allowed or it is not a verb.
    """
def getGraphNodeNestingLevel(node: int, graph: apex.Graph) -> int:
    """return the current nesting level of a given graph not as an integer 
    based on the number of scopes stored as a property for a given nodes. 
    this proerty is automatically managed by apex script
    """
def isGraphNodeInScope(node: int, scope_id: int, graph: apex.Graph) -> bool:
    """checks if a given apex node is part of a scope id. this scope
    id is being set by the apex graphs script as a node property
    """
def colorNodesFromLineno(graph: apex.Graph, color: hou.Vector3, lines: Iterable[int]) -> None:
    """Color as given section of the compiled graph nodes in a highlight color based on the annotated line number for better debugging or error raising"""

START_INDICATOR: str
END_INDICATOR: str
PROPERTIES_INDICATOR_TXT: str
HEADER_INDICATOR_TXT: str
FOOTER_INDICATOR_TXT: str
MODIFY_TEXT: str
HEADER_SETTINGS_TXT: str
SOURCE_SCRIPT_PROP: str
PYTHON_AUTOCOMPLETE_TXT: str

def getSnippetIndictators(indicator: str) -> tuple[str, str]: ...
def extractFromIndicators(script: str, indicator: str, strip: bool = False) -> tuple[str, str]: ...
def saveSnippetAsText(path: str, snippet: str, properties: hou._OptionDict | None = None, header: str | None = None, header_mode: int | None = None, footer: str | None = None, sourcescript: bool = True) -> None:
    """stores a given snippet as text to disk. The parm options and the header and footer and optionally
    allso be added. they also get clearly split from the snippet code. that makes it easier to load the snippets bakc
    to nodes and and apply properties and header setting correctly

    :param path: the path to store the snippet as text 
    :param snippet: the main body of the text snippet
    :param properties: a properties dict of the given parm properties to be stored, defaults to None
    :param header: teh current header snippet, defaults to None
    :param header_mode: the header template setting, defaults to None
    :param footer: teh current footer snippet, defaults to None
    """
def loadSnippetFromText(path: str, extract_header: bool = True, apply_properties: bool = True, keep_properties_snippet: bool = False, script: str | None = None) -> tuple[str, int, str | None, str | None, str, None, str] | tuple[None, int, None, None, None, str, str] | None:
    """extracts from a given text file the according snippet sections. This can be use to apply the various bits 
    of that text snippet properly to a given node. Snippet sections are:
    
    snippet: the main body of the text snippet
    header_mode: the int mode of the header template - this info can be set on the header section of an apex script node
    header: if a custom header exists: the snippet of the custom header
    footer: the custom footer snippet txt
    properties_str: a string holding only the dict of the properties of the given nodes. we only check for properties 
    that have been automatically added to the script in order to store the parmoptions: we can do this for example with 
    the saveSnippetToText() function
    subgraph: if the given snippet contains subgraphs functions then the given snippet interpreted for that section. we d
    differentiate because subgraphs get usually applied in a different snippet

    :param path: the path and file name for the text file
    :param extract_header: defines if the headers are to be clipped and seperated, defaults to True
    :param apply_properties: defines if the properties are to be processed, defaults to True
    :param keep_properties_snippet: defines if the properties snippet is to be clipped or not, defaults to False
    :return: snippet, header_mode, header, footer, properties_str, subgraph
    """
def applyTextToNode(path: str, node: hou.OpNode, extract_header: bool = True, apply_properties: bool = True, keep_properties_snippet: bool = False, parmfolder: str | None = 'parameters', parmblacklist: Sequence[str] | None = None, snippet_parm: str = 'snippet', footer_parm: str | None = 'footer', header_parm: str | None = 'header', headertemplate_parm: str | None = 'headertemplate', useheader_parm: str | None = 'useheader', editheader_parm: str | None = 'editheader', usehoudiniversion_parm: str | None = 'addversion', houdiniversion_parm: str | None = 'applicationversion', subgraph_parm: str | None = None, usesubgraph_parm: str | None = 'usesubgraphs', snippet: str | None = None) -> dict[str, JSONValue] | None:
    """_summary_

    loads a snippet from a text file and applies the various parts of the snippet properly to the node parameters:
    if the text contains parm options that gotten automatically stored with the text then those properties can be reapplied
    to the interface as parm otiopn 
    
    NOTE: in this 
    """

class SubgraphLibCache:
    """
    Class to handle opening multiple subgraph libraries by name to allow writing
    to them. Once a subgraph has been opened, it is kept open and cached
    to allow other subgraphs to be added to it before being written out.

    Displays confirmation messages for overwriting subgraph library files,
    and a message after libraries have been written out to display any
    saved files.
    
    Comes with the option to generate a preview graph that can be used to
    interact with the subgraph for better debugging
    """
    default_path: str | None
    clear_existing: bool
    reload_existing: bool
    reload_subgraphs: bool
    pack_to_geo: hou.Geometry | None
    registry: apex.Registry
    cache_for_preview: bool
    def __init__(self, default_path: str | None = None, clear_existing: bool = False, reload_existing: bool = False, pack_to_geo: hou.Geometry | None = None, preview: bool = False, reload_subgraphs: bool = True) -> None: ...
    def addSubgraph(self, subgraph: apex.Graph, subgraphname: str, subgraphlibpath: str | None = None) -> None:
        """
        Add an APEX graph to the subgraph library using the given subgraph
        name, and the desired subgraph library path.
        """
    def getPackToGeo(self) -> hou.Geometry | None: ...
    def writeOut(self, show_message: bool = True, snippet: str | None = None) -> bool:
        """
        Write out any cached subgraph libraries to the specified paths.
        Prompts for confirmation before overwriting library files, and
        displays a message to show the saved files.
        """
    def createSubgraphPreview(self) -> apex.Graph:
        """
        creates a preview graph of the currently codes subgraphs. Each subgraphs gets represented as a singler
        unconnected subnet and the name of the subnet is representing the subgraph name to be stored
        """

graphexamples: dict[str, str]
hello_world: str
blend_pose: str
