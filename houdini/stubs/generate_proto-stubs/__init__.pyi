# Houdini stubs generated from Houdini 22.0.466

import optparse
from _typeshed import SupportsWrite
from collections.abc import Iterable, Mapping, Sequence
from typing import NoReturn, NotRequired, TextIO, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_ProtoStatement: TypeAlias = list['str | list[_ProtoStatement]']
_DsBlock: TypeAlias = list['str | _DsBlock']
_Defn: TypeAlias = tuple[str, str, str, list['_Defn'], str, str | None, dict[str, str], str | None, str | None]
class _DsParm(TypedDict):
    type: str | None
    name: str
    default: str | _DsBlock | None
    size: int
    disablewhen: str
    disablewhenkey: str
    menu: list[str]
    prototext: str
    cppname: NotRequired[str]
    includeraw: NotRequired[str]
    rangemin: NotRequired[str]
    rangemax: NotRequired[str]
    rampdefault: NotRequired[str | _DsBlock]
    multistartoffset: NotRequired[str]
    childparms: NotRequired['list[_DsParm]']

class _AllEnums(TypedDict):
    byname: dict[str, str]
    text: str
    using: str
    namespace: str

options: optparse.Values
args: list[str]
statements: list[_ProtoStatement]
glb_protodocs: str
global_output_simquery: bool
global_output_oploader: bool
global_derive_from_nodeparms: bool
global_derive_from_opnodeparms: bool
parser: optparse.OptionParser
cpp_keywords: set[str]
cpp_keywords_uppercase: set[str]
ds_scalartags: set[str]
ds_integertags: set[str]
ds_stringtags: set[str]

def error(msg: str) -> NoReturn:
    """ Reports an error message
    """
def replacetext(text: str, dictionary: Mapping[str, str]) -> str:
    """ Uses dictionary to replace all elements of the text
    """
def indenttext(text: str, indent: int) -> str:
    """ Indent the given text by the specified spacing.
    """
def toctype(srctype: str) -> str:
    """ Converts a proto type to a C++ type.
    """
def toctype_ref(srctype: str) -> str:
    """ Converts a proto type to a C++ type const reference.
    """
def touttype(srctype: str) -> str:
    """ Converts a proto type to a UT_OptionEntry
    """
def touttypeenum(srctype: str) -> str:
    """ Converts a proto type to a UT_OptionType
    """
def toparmtypeenum(srctype: str) -> str:
    """ Converts a proto type to a UT_OptionType
    """
def tocinit(srctype: str) -> str:
    """ Converts a proto type to a C++ initializer.
    """
def tocdefault(defvalue: str, srctype: str) -> str:
    """ Converts a normal default into a C++ default
    """
def parseblock(tokens: list[str], inblock: bool) -> tuple[list[_ProtoStatement], list[str]]:
    """ Returns ( [statements], [tokens] ) where statements
        is a list of semicolon separated statements
        and tokens is the unconsumed tokens up to a }
    """
def parsedsblock(tokens: list[str], inblock: bool) -> tuple[_DsBlock, list[str]]:
    """ Returns ( [statements], [tokens] ) where statements
        is a list of tokens grouped into sub-lists wherever
        a {} block occurs.
    """
def buildStructBlock(replace: Mapping[str, str]) -> str:
    """ Returns code for the structure definitions defined by a
        multiparm definition
    """
def buildCreateString(mdefn: _Defn, memberreplace: Mapping[str, str]) -> str:
    """ createString text for a multiparm parameter
    """
def buildMultiparmReplacement(defn: _Defn, depth: int, arrayname: str, opaccessor: str, parmidxcorrection: str) -> dict[str, str]:
    """ Given a defintion line for a multparm, build the required
        access boilerplate
    """
def outputDefinition(outfile: SupportsWrite[str], version: int, apiname: str, classname: str, defnlist: Sequence[_Defn], allenums: _AllEnums) -> None:
    """ Constructs the boiler plate for class name and the
        set of triples in the defn list (type, optionname, C++Name)
        and writes it to outfile.
    """
def dsexecute(statements: Sequence[str | _DsBlock], toplevel: bool, allparms: list[_DsParm], allenums: _AllEnums, parentdisablewhen: str) -> None:
    """ Given a statement list break into separate commands,
        apply each, and return the total
    """
def stripquote(word: str) -> str:
    """ If word is quoted, remove it.
    """
def harden_ds_default(d: str) -> str:
    """ Takes a default and ensures the result is a number.
        Converts expressions into a simple 0.
    """
def parseds_default(parm: _DsParm) -> str:
    """ Takes a map specifying the parameter and extracts the
        string to initialize the default.
    """
def upperfirst(x: str) -> str: ...
def accessorName(parm: _DsParm) -> str: ...
def collapse_rangelist(rangelist: Sequence[str]) -> list[str]:
    """ Takes a tokenized sequence and returns two tokens that
        are the two ranges by collapsing numbers that were falsely
        split up.

        Note this will be confused by
        3 .3
        which is ambiguous with
        3. 3
        We need to re-tokenize the {} block with a less aggressive
        tokenizer to fix that.
    """
def dsparm(statements: Sequence[str | _DsBlock], toplevel: bool, allparms: list[_DsParm], allenums: _AllEnums, parentdisablewhen: str) -> str | None:
    """ Given a tokenized series of statements, with 
 seperators,
        build a line for a protofile to represent it.
    """
def dsmultiparm(statements: Sequence[str | _DsBlock], allparms: list[_DsParm], allenums: _AllEnums, parentdisablewhen: str) -> None:
    """ Parses a multiparm into from ds commands into proto text
    """
def dsgroupradio(statements: Sequence[str | _DsBlock], toplevel: bool, allparms: list[_DsParm], allenums: _AllEnums, parentdisablewhen: str) -> None:
    """ Parses a multiparm into from ds commands into proto text
    """
def dscommand(command: str | _DsBlock, args: Sequence[str | _DsBlock], toplevel: bool, allparms: list[_DsParm], allenums: _AllEnums, parentdisablewhen: str) -> str | None:
    """ Returns the update to protofile required for
        the given command
    """
def dsprocessparms(allparms: Sequence[_DsParm], globalparms: list[_DsParm], iscopnode: bool) -> str:
    """ Takes a list of parameters and generates the .proto file
        that corresponds with them. Handles expanding disablewhens
        and sorting according to evaulation order
    """

sourcefile: bool
classname: str | None
dsfile: bool
filetext: str
apiname: str
baselib: str
allenums: _AllEnums
tokens: list[str]
inbrace: bool

def processParmList(defnlist: list[_Defn], statements: Iterable[_ProtoStatement], conditional: str, toplevel: bool) -> list[_Defn]:
    """ Process a series of statements and applies them to the
        given definition.  Returns the augmented definition list.
    """

version: int
outfile: TextIO
underscore: int
libname: str
dest_dir: str
parmlist: str | list[_ProtoStatement]
defnlist: list[_Defn]
