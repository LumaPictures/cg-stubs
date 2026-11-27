import _apex
import apex
import apex.ui.apexparmdata as ap
import ast
import hou
import logging
import re
from _typeshed import StrPath as StrPath
from collections.abc import Callable as Callable, Collection, Container, Iterable, Mapping, MutableSet
from enum import Enum
from typing import Concatenate, Never, NoReturn

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_K = TypeVar('_K')
_V = TypeVar('_V')
_P = ParamSpec('_P')
_R = TypeVar('_R')
_VisitorT = TypeVar('_VisitorT', bound='ApexNodeVisitor')
TYPE_ID: str
METADATA_NAME: str
METADATA_COLOR: str
METADATA_POS: str
METADATA_PROPERTIES: str
METADATA_TAGS: str
METADATA_OFFSET: str
METADATA_RELATIVE: str
METADATA_RIGHT: str
METADATA_LEFT: str
METADATA_ABOVE: str
METADATA_BELOW: str
METADATA_KWARGS: list[str]
DEFAULT_METADATA_OFFSETS: dict[str, hou.Vector3]
VAR_OUT_SUFFIX: str
APEX_MODULE_ID: str
TEMP_INDICATOR: str
ANNOTATION_TUPLE: str
PROTECTED_AST_KEYWORDS: list[str]
PROP_CONTAINING_SCOPE: str
PROP_LINENO: str
PROP_SCOPES: str
PROP_CURRENT_SCOPE: str
SCRIPT_PROPERTIES: list[str]
GRAPH_ID_ARRAYS: list[str]
GRAPH_ID_TYPES: list[str]
PROTECTED_APEX_NAMESPACES: tuple[str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str, str]
VECTOR_TYPES: dict[str, type[hou.Vector2] | type[hou.Vector3] | type[hou.Vector4] | type[hou.Matrix3] | type[hou.Matrix4]]
VECTOR_COMP_TYPE: dict[str, str]
RAMP_TYPES: tuple[str, str]
SOP_INPLACE_VERSION: str

def vector_comp_get_callback(vec_type: str, has_second_index: bool) -> str:
    """ Get the callback used to go from the vector to its components. """
def vector_comp_set_callback(vec_type: str, has_second_index: bool) -> str:
    """ Get the callback used to go from components to the full vector. """
def vector_comp_type(vec_type: str, has_second_index: bool) -> str:
    """ Get the component type for vector[i], matrix[i], or matrix[i][j] """

NUMERICAL_TYPES: list[str]
UNDEFINED_VALUES: tuple[str, str]
MATH_NODES: dict[str, str]
COMPARE_NODES: dict[str, str]
GEO_ATTRS: list[str]
ARRAY_TYPES: dict[str, type[apex.BoolArray] | type[apex.IntArray] | type[apex.FloatArray] | type[apex.StringArray] | type[apex.DictArray] | type[apex.GeometryArray] | type[apex.Vector2Array] | type[apex.Vector3Array] | type[apex.Vector4Array] | type[apex.Matrix3Array] | type[apex.Matrix4Array]]
ALL_ARRAY_TYPES: list[str]
LOG_SEVERITY: list[str]
STRING_SUBSTITUTION_KEYS: list[str]
DEBUG_OUTPUT_NODE: str
DEBUG_OUTPUT_NAME: str
DEBUG_OUTPUT_PORT: str
DEFAULT_COLOR: hou.Vector3
SCOPE_COLOR: hou.Vector3
BIND_COLOR: hou.Vector3
COND_COLOR: hou.Vector3
LOOP_COLOR: hou.Vector3
GENERICS: set[str]
ARRAY_NODES: set[str]
IGNORED_STICKY_NOTE_PARMS: tuple[str]
STICKY_NOTE_DEFAULT_PARMS: dict[str, hou.Vector2 | bool | hou.Vector3 | float]
STICKY_NOTE_DEFAULT_METADATA: dict[str, hou.Vector3]
generic_start_token: int
cb_load: str

def check_operation_types(op_types: Iterable[str], valid_types: Collection[str], operation_name: str) -> None: ...
def is_protected_keyword(keyw: str) -> bool:
    """
    Whether keyw is a protected keyword which is either
    a special keyword for apex script or a python keyword.
    """
def guard_protected_keyword(keyw: str) -> str:
    """
    For any keyword that is not allowed to be used, we suffix it with
    an underscore, and remove the underscore as needed to keep names
    consistent.
    """
def unguard_protected_keyword(keyw: str) -> str:
    """ Undoes guard_protected_keyword. """
def portname_strip_leading_symbol(portname: str) -> str:
    """
    Inplace ports have an extra * at the start.
    Spare ports have an extra + at the start.
    These need to be removed before setting the portname:value pair
    in the parameters dictionary for the node.
    """
def convert_version(version_pre: str) -> str | None: ...
def validateTypeName(type_name: ast.Name | str) -> str: ...
def findVersionSuffix(callbackname: str) -> str | None: ...
def callbackTypeInfo(callbackname: str) -> tuple[str, list[str] | None]:
    """
    Parse a callback name (after it has been processed by
    processCallbackName) to extract the type name(s).
    Return the parsed types as a list or None if no type info.
    NOTE: For cases like Add_Float_Int_ we need to support
    multi-types.
    """
def process_special_argname(argname: str) -> str:
    """
    Process an argument name, replacing special syntax with symbols
    that usually cannot be in the name.

    Replace '__dot__' with '.'
    """

class SignatureMatchLevel(Enum):
    NO_MATCH = 0
    ALLOW = 1
    MATCH = 2

class SurjectiveMap(dict[_K, _V]):
    """ Many to One invertible map. The inverse is a one to many relation. """
    inverse: dict[_V, list[_K]]
    def __init__(self) -> None: ...
    def __setitem__(self, key: _K, value: _V) -> None: ...
    def __delitem__(self, key: _K) -> None: ...
    def getFirstInverse(self, val: _V) -> _K | None: ...
    def getLastInverse(self, val: _V) -> _K | None: ...

SHOW_TRACEBACK: bool

class ApexCodeError(Exception):
    """
    Custom exception that automatically shows the correct line number for the given ast node that errors.
    """
    line_offset: int
    lineno: int
    msg: str
    source: str | None
    node: ast.AST
    traceback: str | None
    show_traceback: bool
    def __init__(self, node: ast.AST, msg: str, line_offset: int = 0, source: str | None = None) -> None: ...
    def format_traceback(self) -> str: ...
    def line_info(self, use_multiline_highlight: bool = False) -> str:
        """
        creates the error message that we print out of the user. the given error section is either highlighted with quotes 
        or on a multiline string with a highlight line. this requires a monospaced font though
        """
    def print_text(self) -> str: ...
    def text(self) -> str: ...

class ApexNodeVisitorScope:
    def __eq__(self, other: object) -> bool: ...
    start_id: int
    end_id: int
    parent: ApexNodeVisitorScope | None
    id: int
    element_binding: str | None
    array_binding: str | None
    index_binding: str | None

class ApexGraphIdManager:
    graphname: str | None
    name: str
    ports: dict[str, int]
    def __init__(self, name: str, graphname: str | None = None) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def getPort(self, portname: str) -> int | None: ...
    def addPort(self, portname: str, port: int) -> None: ...

class ApexNodeVisitor(ast.NodeVisitor):
    graph: apex.Graph
    registry: apex.Registry
    source: str | None
    id_to_port: SurjectiveMap[str, int]
    graph_id_objects: dict[str, ApexGraphIdManager]
    graph_ids: list[str]
    awaiting_graph: list[int]
    id_to_scope: dict[str, ApexNodeVisitorScope | None]
    visited: list[Never]
    scopes: list[ApexNodeVisitorScope]
    annotated_ids: dict[str, str]
    cur_scopes: list[ApexNodeVisitorScope]
    graph_path: str
    line_offset: int
    subvisitors: list['ApexNodeVisitor']
    function_references: dict[str, int]
    warnings: list[str | ApexCodeError | hou.Error]
    subgraphs: dict[str, apex.Graph]
    graph_templates: dict[str, int]
    logger: logging.Logger
    print_to_console: bool
    positioned_node_ids: set[int]
    colored_node_ids: set[int]
    relative_pos_list: list[tuple[int, int, hou.Vector3]]
    houdini_version: str | None
    properties: dict[str, _apex._ValueArg]
    properties_manager: ap.GraphParmdataManager
    cur_line: int
    show_traceback: bool
    def __init__(self, graph: apex.Graph, registry: apex.Registry, line_offset: int = 0, graph_path: str = '', source: str | None = None, subgraphs: Mapping[str, apex.Graph] | None = None, houdini_version: str | None = None, print_to_console: bool = False) -> None: ...
    def setScriptHoudiniVersionString(self, version_string: str) -> None:
        """
        Set the script houdini version from a string. When creating callbacks
        if is are more than one version, this is used to find the last version
        available at the time of that houdini version.
        """
    def clearScriptHoudiniVersion(self) -> None:
        """
        Clear the houdini version string. This results in
        callbackVersionLookup always just returning the same
        callback_name as was provided and does not do any mapping.
        """
    @staticmethod
    def exceptionHandler(func: Callable[Concatenate[_VisitorT, _P], _R]) -> Callable[Concatenate[_VisitorT, _P], _R]:
        """
        raises any given error using the apex code error class that also shows an indication about the corresponding error line, error line content plus highlighing
        in addition to the error message
        """
    @staticmethod
    def lineHandler(func: Callable[Concatenate[_VisitorT, _P], _R]) -> Callable[Concatenate[_VisitorT, _P], _R]:
        """
        keeps track of the code line correlating to the current node in the syntax tree. this can be used to associated created graph nodes with 
        the line number they are associated with or for error handling
        """
    @property
    def cur_scope(self) -> ApexNodeVisitorScope | None: ...
    def addWarning(self, warning: str | ApexCodeError | hou.Error) -> None:
        """
        Add a warning to the list of warnings generated while
        compiling. These can be retrieved from self.warnings for the
        full list, or from self.generateWarning() which will take all
        warnings in the list, and format it as a single hou.NodeWarning
        to be raised in a python sop.
        """
    def collectWarnings(self) -> list[str | ApexCodeError | hou.Error]:
        """
        Collect all the warnings from this visitor and any subvisitors,
        adding any warnings from a subvisitor before the warnings from
        this visitor class.
        """
    def generateWarning(self) -> str | None:
        """
        Generate a hou.NodeWarning that can be raised at the end
        of a python sop to add the warnings generated while compiling
        to the node.

        This takes all generated warnings in self.warnings and creates
        a single hou.NodeWarning for all of them.
        """
    def getInputName(self, callback: str, index: int, add_suffix: bool = True) -> str:
        """
        the the input name of tha given callback at a given position name based on its signature.
        """
    def getOutputName(self, callback: str, index: int, add_suffix: bool = True) -> str | None:
        """
        the the input name of tha given callback at a given position name based on its signature.
        """
    def getCallbackOutputs(self, callback: str) -> tuple[apex.Parm, ...]:
        """
        returns the outputs of a given callback or subgraph
        """
    def getOutputTypeName(self, callback: str, index: int) -> str | None: ...
    def isVariadic(self, callback: str, portname: str) -> bool:
        """
        determines if a given port of a callback is variadic or not
        """
    def variableScope(self, var_id: str) -> ApexNodeVisitorScope | None: ...
    def scopeContains(self, outer_scope: ApexNodeVisitorScope | None, inner_scope: ApexNodeVisitorScope | None) -> bool: ...
    def getPathToScope(self, scope: ApexNodeVisitorScope | None) -> list[ApexNodeVisitorScope]: ...
    def createScope(self, start_node: int, end_node: int) -> None: ...
    def endScope(self) -> None: ...
    def findValueTypeSpec(self, func_node: ast.Call) -> list[str] | None:
        """
        Given a function call, try to find the valuetype kwarg in the arguments
        if it exists, and return that type. Or None if not found.

        Can raise an error if the valuetype specification is not of the valid form.
        """
    def generic_visit(self, node: ast.AST) -> None: ...
    def colorNodesFromLineno(self, color: hou.Vector3, lines: Iterable[int]) -> None:
        """Color as given section of the compiled graph nodes in a highlight color based on the annotated line number for better debugging or error raising"""
    def layoutUnpositionedNodes(self, node_width: float = 1.8) -> None: ...
    @exceptionHandler
    def visit_Assign(self, node: ast.Assign) -> None: ...
    @exceptionHandler
    def visit_AnnAssign(self, node: ast.AnnAssign) -> None: ...
    @exceptionHandler
    def visit_AugAssign(self, node: ast.AugAssign) -> None: ...
    @exceptionHandler
    def visit_Dict(self, node: ast.Dict) -> None: ...
    def visit_For(self, node: ast.For) -> None: ...
    @exceptionHandler
    def visit_Call(self, node: ast.Call) -> None: ...
    def visit_If(self, node: ast.If) -> None: ...
    @exceptionHandler
    def visit_Return(self, node: ast.Return) -> None: ...
    @exceptionHandler
    def visit_FunctionDef(self, node: ast.FunctionDef) -> None: ...
    @exceptionHandler
    def offloadSubgraphs(self, node: ast.Module, default_path: str | None = None, clear_existing: bool = False, header_node: ast.Module | None = None, snippet: str | None = None, reload_subgraphs: bool = True) -> None:
        """
        Given an ast.Module as returned by ast.parse(), go through top
        level functions in the body of the module and either error
        if they are not decorated as subgraphs or save the subgraph
        to disk to either the default path or a path specified
        in the subgraph decorator.
        """
    @exceptionHandler
    def getSubgraphsPreviewGraph(self, node: ast.Module, header_node: ast.Module | None = None) -> apex.Graph:
        """_summary_

        :param node: _description_
        :param default_path: _description_, defaults to None
        :param clear_existing: _description_, defaults to False
        :param header_node: _description_, defaults to None
        :return: _description_
        """
    @exceptionHandler
    def offloadSubgraphsToGeo(self, node: ast.Module, offload_lib: hou.Geometry, header_node: ast.Module | None = None, reload_subgraphs: bool = True) -> hou.Geometry: ...
    def visit_Import(self, node: ast.Import) -> None: ...
    def visit_ImportFrom(self, node: ast.ImportFrom) -> None: ...
    def visit_Yield(self, node: ast.Yield) -> NoReturn: ...
    def visit_Global(self, node: ast.Global) -> NoReturn: ...
    def visit_ClassDef(self, node: ast.ClassDef) -> NoReturn: ...
    def visit_While(self, node: ast.While) -> NoReturn: ...
    def visit_Match(self, node: ast.Match) -> NoReturn: ...
    def visit_With(self, node: ast.With) -> NoReturn: ...
    def visit_Try(self, node: ast.Try) -> NoReturn: ...
    def visit_Pass(self, node: ast.Pass) -> None: ...
    def visit_Break(self, node: ast.Break) -> NoReturn: ...
    def visit_Continue(self, node: ast.Continue) -> NoReturn: ...
    def visit_Assert(self, node: ast.Assert) -> NoReturn: ...
    def visit_Raise(self, node: ast.Raise) -> None: ...
    def visit_Delete(self, node: ast.Delete) -> NoReturn: ...
    def visit_NonLocal(self, node: ast.Nonlocal) -> NoReturn: ...
    def visitAndLayout(self, node: ast.AST) -> None: ...

INPUT_PORT_KIND: int
OUTPUT_PORT_KIND: int
WRAP_ARR_TYPES: list[str]

def isParmsCallback(cbname: str) -> bool: ...
def isRangeCallback(cbname: str) -> bool: ...
def isOutputCallback(cbname: str) -> bool: ...
def isForBeginCallback(cbname: str) -> bool: ...
def isForRangeBeginCallback(cbname: str) -> bool: ...
def isIfBeginCallback(cbname: str) -> bool: ...
def isForEachBeginCallback(cbname: str) -> bool: ...
def isPointForEachBeginCallback(cbname: str) -> bool: ...
def isPrimForEachBeginCallback(cbname: str) -> bool: ...
def isGeoForEachBeginCallback(cbname: str) -> bool: ...
def isPointForEachEndCallback(cbname: str) -> bool: ...
def isPrimForEachEndCallback(cbname: str) -> bool: ...
def isGeoForEachEndCallback(cbname: str) -> bool: ...
def isForEndCallback(cbname: str) -> bool: ...
def isForRangeEndCallback(cbname: str) -> bool: ...
def isIfEndCallback(cbname: str) -> bool: ...
def isForEachEndCallback(cbname: str) -> bool: ...
def isScopeBeginCallback(cbname: str) -> bool: ...
def isScopeEndCallback(cbname: str) -> bool: ...
def isSpecialArgNameCallback(cbname: str) -> bool: ...
def isGraphTemplateCallback(cbname: str) -> bool: ...
def isSubnetCallback(cbname: str) -> bool: ...
def isStickyNoteCallback(cbname: str) -> bool: ...
def isUntypedNullCallback(cbname: str) -> bool: ...

POS_PRECISION: int
COL_PRECISION: int

def subnetPathToName(subnet_path: str) -> str: ...
def subnetPath(cur_path: str, subnet_name: str) -> str: ...
def subnetEncodedName(cur_path: str, subnet_name: str) -> str: ...
def indentSpaces(level: int) -> str: ...
def matchVersion(test_str: str) -> re.Match[str] | None:
    """ Check if 'test_str' matches a regular expression that checks for a version string. """
def filterApexDict(d: apex.Dict | Mapping[str, hou._OptionValue], filter_set: Container[str], exclude: bool = False) -> apex.Dict:
    """
    Filter the apex.Dict 'd' by filter_set.
    If exclude is False, only items in filter_set are kept.
    If exclude is True, only items not in filter_set are kept.
    """

class VarAssign:
    """
    Convenience class for writing down an assignment to a single variable
    with a type string to also record the target in the list of vars.
    """
    target_name: str
    typestr: str
    rhs: str
    def __init__(self, target_name: str, typestr: str | None, rhs: str) -> None: ...
    def write(self, scope_variables: MutableSet[str]) -> str: ...

class GraphDecompiler:
    graph: apex.Graph
    geo: hou.Geometry
    registry: apex.Registry
    identifier_map: dict[str, str]
    target_names: dict[str, str | None]
    subnet_names: list[str]
    subnet_sig_cache: dict[Never, Never]
    port_name_cache: dict[int, str]
    use_object_oriented: bool
    code: str
    def __init__(self, geo: hou.Geometry | None = None, graph: apex.Graph | None = None, subnet_names: list[str] | None = None, use_object_oriented: bool = True) -> None: ...
    def isCallbackSubgraph(self, callback_name: str) -> bool:
        """ Check whether a callback with the given name is a subgraph. """
    def isPortInput(self, portid: int) -> bool: ...
    def isPortOutput(self, portid: int) -> bool: ...
    def isPortRundata(self, portid: int) -> bool: ...
    def isPortNext(self, portid: int) -> bool: ...
    def isPortSpare(self, portid: int) -> bool: ...
    def findInputPort(self, nodeid: int, portname: str) -> int | None: ...
    def findOutputPort(self, nodeid: int, portname: str) -> int | None: ...
    def findSpareOuterPort(self, nodeid: int, get_input_port: bool) -> int: ...
    def findSpareSubports(self, nodeid: int, get_input_ports: bool) -> list[int]: ...
    def portToUniqueName(self, portid: int) -> str:
        """ Get a unique name from a port by using the port name and nodeid. """
    def portToPrettyName(self, portid: int) -> str:
        """ Get a prettier (though not necessarily unique) name for the port. """
    def portToTargetName(self, portid: int, enforce_unique: bool = True, track_uniques: bool = True) -> str:
        """ Get the target name from a port, if not unique, append an integer. """
    def portIsWired(self, portid: int) -> bool:
        """ Whether the port is connected to anything. """
    def subportToPort(self, subportid: int) -> int:
        """ Find the outer port from a subport. """
    def connectedPorts(self, portid: int, traverse_begin_scope: bool = True, traverse_end_scope: bool = False, depth: int = 0) -> list[int]:
        """ Get connected ports list, optionally traversing begin and end scopes. """
    def portIsConnected(self, portid: int, traverse_begin_scope: bool = True, traverse_end_scope: bool = False) -> bool:
        """ Whether the port is connected to some other port that we care about. """
    def portWireEnds(self, portid: int, traverse_begin_scope: bool = True, traverse_end_scope: bool = False) -> list[int]:
        """ Get the connected input ports to this output port. """
    def portWireStart(self, portid: int, traverse_begin_scope: bool = False, traverse_end_scope: bool = False) -> int | None:
        """ Get the connected output port connected to this input port. """
    def findMatchingInputPort(self, output_portid: int) -> int | None:
        """
        Given an output port on a node, find an input port on the node
        with the same name and type and return it, or return None if
        not possible.
        """
    def findOutputToReuseName(self, output_portid: int) -> int | None:
        """
        Given an output port on a node, first find a matching input port
        with the same name and type, if this exists, and this input port
        is connected to an output port with only one wire coming from it,
        then the identifier for the found output port can be reused for
        the given output port. In this case we return the found output
        port.

        Otherwise, if no such output port can be found, return None.
        """
    def findObjectOrientedReusePortid(self, nodeid: int) -> tuple[int, int] | tuple[None, None]:
        """
        Given a nodeid, check if the first output port is an inplace port with
        a matching input port with the same name and type, and if so also check
        if the input port is connected to an output port with exactly one wire
        connected to it. If this is the case then check if the output port on
        the previous node and the current node can be given the same name using
        portToVariableId. If they can be given the same names, then return
        these two output ports which we can reuse the identifier for.

        Otherwise return (None,None) if no ports can be found to reuse the idenfier.
        """
    def findScopeBegin(self, nodeid: int) -> int:
        """ Given a scope end node, find the corresponding scope begin node. """
    def findScopeEnd(self, nodeid: int) -> int: ...
    def spareEndPortToMatchingStartPort(self, portid: int) -> int | None:
        """
        Given a spare port (input or outut) on a scope end node,
        find the matching spare input port on the scope begin node
        or None if it cannot be found.
        """
    def spareStartPortToMatchingEndPort(self, portid: int) -> int | None: ...
    def portToVariableId(self, portid: int) -> str:
        """ This is used as caching layer for the results of _portToVariableId. """
    def portToOutputBindings(self, portid: int) -> list[int]:
        """
        Get the output ports connected to this port, or if this is
        an input, follow back to the port we get the name from
        and get the outputs bound to that node.
        This grabs the listof outputs to create output binding
        aliases for.
        """
    def processCallbackName(self, callback_raw_name: str) -> str:
        """ Process callback name to include the namespace infront. """
    def processCallbackNameObjectOriented(self, callback_raw_name: str, object_oriented_varid: str) -> str:
        """ Process the callback name to include 'object_oriented_varid' infront. """
    def nodeCallbackName(self, pt: hou.Point) -> str: ...
    def nodeName(self, pt: hou.Point) -> str: ...
    def nodeParms(self, pt: hou.Point) -> hou._OptionDict: ...
    def nodeColor(self, pt: hou.Point) -> hou.Vector3: ...
    def nodePosition(self, pt: hou.Point) -> hou.Vector3: ...
    def nodeProperties(self, pt: hou.Point) -> hou._OptionDict: ...
    def nodeTags(self, pt: hou.Point) -> tuple[str, ...]: ...
    def nodeSubnetGeo(self, pt: hou.Point) -> hou.Geometry | None: ...
    def findSubnetNode(self, subnet_name: str) -> hou.Point | None: ...
    def subnetGeo(self, subnet_name: str) -> hou.Geometry | None: ...
    def arrayTypeName(self, arr: object) -> str | None: ...
    def formatParm(self, v: object, wrap_lines: bool = False, indent_level: int = 0) -> str:
        """
        Format a value as a string that when parsed will generate the
        same value on the compile side.
        """
    def formatVariadicArgDict(self, the_dict: Mapping[str, str], wrap_lines: bool = False, indent_level: int = 0) -> str:
        """
        Format a dictionary for the variadic input args to map input
        variadic port names as string literals to variable names
        representing output ports wired to these spare inputs.
        """
    def nodeMetadata(self, pt: hou.Point, pos: bool = True, col: bool = True, name: bool = True, tags: bool = True, properties: bool = True) -> dict[str, str]:
        """ Get the metadata for the node as a dictionary. """
    def graphNodeMetadata(self, nodeid: int, pos: bool = True, col: bool = True, name: bool = True, tags: bool = True, properties: bool = True) -> dict[str, str]:
        """ Get the metadata for the node as a dictionary. """
    def generateStickyNotesCode(self, indent_level: int = 0, metadata_pos: bool = True, metadata_col: bool = True, metadata_name: bool = True, metadata_tags: bool = True, metadata_properties: bool = True) -> str:
        """ Generate the special code for making sticky notes. """
    def gatherSubnets(self, subnet_path: str | None = None) -> list[str]:
        """
        Return a list of all subnet names generated in this subnet and
        all recursive subnets.
        """
    def generateSubnetCode(self, subnet_path: str, nodeid: int, annotations: bool = False, metadata_pos: bool = True, metadata_col: bool = True, metadata_name: bool = True, metadata_tags: bool = True, metadata_properties: bool = True, wrap_lines: bool = True) -> tuple[str, str]:
        """ Generate code for a subnet. """
    header: str
    def generateCode(self, subnet_path: str | None = None, subnet_nodeid: int | None = None, annotations: bool = False, metadata_pos: bool = True, metadata_col: bool = True, metadata_name: bool = True, metadata_tags: bool = True, metadata_properties: bool = True, wrap_lines: bool = True) -> str:
        """ Generate code for the graph. """
    def writeCodeToFile(self, filepath: StrPath) -> None: ...

def roundTripGraphGeo(geo: hou.Geometry, annotations: bool = True, metadata_pos: bool = True, metadata_col: bool = True, metadata_name: bool = True, metadata_tags: bool = True, metadata_properties: bool = True, wrap_lines: bool = True) -> tuple[str, hou.Geometry]:
    """
    Used for testing.

    Take a graph representation of a geometry, decompile it,
    then recompile it.

    Return the decompiled code and recompiled graph geometry.
    """
