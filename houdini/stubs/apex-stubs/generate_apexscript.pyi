import _apex
import apex
from apex import graphscriptutils as graphscriptutils, helputils as helputils
from apex.graphscriptutils import FuncMappingCollection as FuncMappingCollection
from bookish.wiki.wikipages import WikiPages

VECTOR3_TYPE: str
GRAPH_TYPE: str
FUNC_MAPPINGS: FuncMappingCollection
GENERIC_NAMESPACE: str
GENERIC_ARGS: str
DOC_LINE_WIDTH: int
TYPE_DOCS: dict[str, str]
FUTURE_DOCS: str

def getTypeDocString(valuetype: str) -> str: ...

DOC_LIB: dict[str, str]
DOC_DIR: str
QUIET: bool

def getCallbackDocString(callback_name: str) -> str: ...

class HoudiniHelpCache:
    pages: WikiPages
    def __init__(self) -> None: ...
    def getHelp(self, callback_name: str) -> str | None: ...

HELP_CACHE: HoudiniHelpCache | None

def getCallbackDocString_hhelp(callback_name: str) -> str: ...
def indentMultiLineTxt(txt: str, indent_level: int = 0) -> str: ...

class FuncData:
    """
    collects and assembles all the data necessary to create a proxy python function for documentation and auto completion
    """
    name: str
    callback_name: str
    input_args: dict[str, list[str | None]]
    input_defaults: dict[str, _apex._ValueArg]
    output_args: dict[str, list[str]]
    template: str
    indent_level: int
    line_with: int
    parent_name: str
    doc_template: str
    standard_template: str
    doc_string: str
    is_inplace: bool
    generic_args: bool
    class_name: str
    code: str
    use_hhelp: bool
    def __init__(self, name: str, callback_name: str, indent_level: int) -> None: ...
    def addInput(self, name: str, ann_type: str | None, default: _apex._ValueArg | None = None) -> None:
        """
        this will update or add a new input arg. if a given input arg has been already specified then only the given type will be added
        """
    def addOutput(self, name: str, ann_type: str) -> None:
        """
        this will update or add a new out arg. if a given input arg has been already specified then only the given type will be added
        """
    def writeInputArgs(self, use_annotation: bool = True) -> str:
        """
        formats the input arg dict to the python annotation style: 
        name: type 
        or in case of multiple types store in the input arg dict:
        name: type | type
        """
    def writeOutputArgs(self, use_annotation: bool = True) -> str:
        """ formats the given out arg names for the function return based on the keys in the collect out arg names in the dictionary"""
    def writOutputAnnotation(self) -> str:
        """formates the given annotation for the return type based on the stored type data in the output args dictionary"""
    def generateDocString(self, template: str | None = None) -> str:
        """
        format the doc string associated with a given function
        """
    def generateCode(self, template: str | None = None, doc_template: str | None = None) -> None:
        """
        based on a string template we will out the according func data collected to the function string: mandatory args for the template are
        name
        input_args
        output_annotation
        doc
        output_args
        """

class ObjectData:
    name: str
    cls_name: str
    registry: apex.Registry
    functions: dict[str, FuncData]
    doc_string: str
    cls_template: str
    init_template: str
    method_template: str
    doc_template: str
    code: str
    use_hhelp: bool
    def __init__(self, name: str, registry: apex.Registry) -> None: ...
    def __eq__(self, __value: object) -> bool: ...
    def generateDocString(self) -> str:
        """
        format the doc string for the __init__() function
        """
    def addFunc(self, callback_name: str, signature: apex.Signature, func_name: str | None = None) -> None:
        """
        process a given cal
        """
    def generateCode(self) -> None: ...

class NamespaceData:
    name: str
    cls_name: str
    registry: apex.Registry
    functions: dict[str, FuncData]
    namespaces: dict[str, 'NamespaceData']
    objects: dict[str, ObjectData]
    cls_template: str
    add_namespace_template: str
    method_template: str
    doc_template: str
    code: str
    use_hhelp: bool
    def __init__(self, name: str, registry: apex.Registry) -> None: ...
    def __eq__(self, __value: object) -> bool: ...
    def addFunc(self, callback_name: str, signature: apex.Signature, func_name: str | None = None) -> None:
        """
        add a FuncData object for the given function of the namespace. should the function have a nested namespace
        then handle add the according nested namespace recursively
        """
    def addObjectFunc(self, obj_name: str, callback_name: str, signature: apex.Signature) -> None: ...
    def generateCode(self) -> None:
        """
        generates the code for the current namespace class and all its collected methods it also recursively traverses through
        any sub namespaces and writes the according classes as well
        """

class DocHelper:
    registry: apex.Registry
    objects: dict[str, ObjectData]
    namespaces: dict[str, 'NamespaceData']
    cls_template: str
    add_namespace_template: str
    code: str
    use_hhelp: bool
    def __init__(self, registry: apex.Registry) -> None: ...
    def addNamespaceFunctions(self, pattern: str = '*') -> None: ...
    def addObjectDocFunctions(self, object_pattern: str = '*', function_pattern: str = '*') -> None: ...
    def generateCode(self) -> None: ...
    def writeCodeToFile(self, filepath: str) -> None: ...

def generateDoc(filepath: str, apex_module_docs: bool = True, use_hhelp: bool = True) -> None: ...
