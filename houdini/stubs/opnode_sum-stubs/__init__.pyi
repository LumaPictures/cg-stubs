import builtins
import hou
import optparse
from collections.abc import Iterable
from houtypes import JSONValue
from typing import Never, NotRequired, TypedDict

class _ParmDescription(TypedDict):
    label: str
    name: str
    type: NotRequired[str]
    size: NotRequired[int]
    namingscheme: NotRequired[str]
    default: NotRequired[tuple[float, ...] | tuple[int, ...] | tuple[str, ...] | int | bool]
    parms: NotRequired[builtins.dict[str, '_ParmDescription']]

class _TypeDescription(TypedDict, total=False):
    name: str
    label: str
    mininput: int
    maxinput: int
    parms: builtins.dict[str, _ParmDescription]

class _Summary(TypedDict, total=False):
    Nodes: builtins.dict[str, builtins.dict[str, _TypeDescription]]
    Shelves: builtins.dict[str, builtins.dict[str, str | builtins.dict[str, builtins.dict[str, str]]]]
    Vex: builtins.dict[str, JSONValue]
    hscript: builtins.dict[str, builtins.dict[str, Never]]
    EXPR: builtins.dict[str, builtins.dict[str, Never]]
    Verbs: builtins.dict[str, builtins.dict[str, builtins.dict[str, Never]]]
    hom: builtins.dict[str, builtins.dict[str, builtins.dict[str, list[str]]]]
    Libraries: builtins.dict[str, builtins.dict[str, str]]

options: optparse.Values
args: list[str]

def ismultiparm(parm: hou.ParmTemplate) -> bool: ...
def describeparm(type_name: str, parm: hou.ParmTemplate | None, brief: bool) -> tuple[None, None] | tuple[None, tuple[hou.ParmTemplate, ...]] | tuple[_ParmDescription, None]:
    """ Takes an indivdual ParmTemplate and returns a dictionary
        describing it.
        WIll return None if it is not describable.
    """
def describeparms(type_name: str, parms: Iterable[hou.ParmTemplate | None], brief: bool) -> builtins.dict[str, _ParmDescription]:
    """ Takes a tuple of ParmTemplates and describes it as
        a dictionary.
    """
def describetype(type: hou.NodeType, brief: bool) -> _TypeDescription:
    """ Takes  NodeType and returns a dictionary describing it
    """
def describealltypes(category: hou.OpNodeTypeCategory, printparms: bool, brief: bool) -> builtins.dict[str, _TypeDescription]:
    """ Takes a NodeTypeCategory and builds a dictionary of all nodetypes
        in that category
    """
def describenodes(printparms: bool, brief: bool) -> builtins.dict[str, builtins.dict[str, _TypeDescription]]:
    """ Describe all nodes and returns a dictionary of categories
    """
def describetool(tool: hou.Tool) -> builtins.dict[str, str]:
    """ Return a dict describing a tool
    """
def describeshelf(shelf: hou.Shelf) -> builtins.dict[str, str | builtins.dict[str, builtins.dict[str, str]]]:
    """ Returns a dict of all tools in a shelf
    """
def describeshelves() -> builtins.dict[str, builtins.dict[str, str | builtins.dict[str, builtins.dict[str, str]]]]:
    """ returns a dict of all shelves
    """
def describevex() -> builtins.dict[str, JSONValue]:
    """ Returns a dict of all vex functions
    """
def describehscript() -> builtins.dict[str, builtins.dict[str, Never]]:
    """ Returns dict of all hscript functions
    """
def describeEXPR() -> builtins.dict[str, builtins.dict[str, Never]]:
    """ Returns dict of all hscript functions
    """
def describeVerbs() -> builtins.dict[str, builtins.dict[str, builtins.dict[str, Never]]]:
    """ Return a dict of all verbs
    """
def describehom() -> builtins.dict[str, builtins.dict[str, builtins.dict[str, list[str]]]]: ...
def describeThirdPartyLibraries() -> builtins.dict[str, builtins.dict[str, str]]:
    """ Return a dict of all third party libraries being used.
    """

usage: str
parser: optparse.OptionParser
dict: _Summary
