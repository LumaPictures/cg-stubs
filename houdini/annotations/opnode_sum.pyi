import builtins
import optparse
from collections.abc import Iterable
from typing import Never, NotRequired, TypedDict

import hou
from houtypes import JSONValue

# Which keys describeparm fills in depends on `brief` and on the template type.
class _ParmDescription(TypedDict):
    label: str
    name: str
    type: NotRequired[str]
    size: NotRequired[int]
    namingscheme: NotRequired[str]
    default: NotRequired[tuple[float, ...] | tuple[int, ...] | tuple[str, ...] | int | bool]
    parms: NotRequired[builtins.dict[str, "_ParmDescription"]]

# describealltypes leaves a type's entry empty when parameters aren't asked for.
class _TypeDescription(TypedDict, total=False):
    name: str
    label: str
    mininput: int
    maxinput: int
    parms: builtins.dict[str, _ParmDescription]

# The JSON summary the script prints, filled in one key at a time.
class _Summary(TypedDict, total=False):
    Nodes: builtins.dict[str, builtins.dict[str, _TypeDescription]]
    Shelves: builtins.dict[str, builtins.dict[str, str | builtins.dict[str, builtins.dict[str, str]]]]
    Vex: builtins.dict[str, JSONValue]
    hscript: builtins.dict[str, builtins.dict[str, Never]]
    EXPR: builtins.dict[str, builtins.dict[str, Never]]
    Verbs: builtins.dict[str, builtins.dict[str, builtins.dict[str, Never]]]
    hom: builtins.dict[str, builtins.dict[str, builtins.dict[str, list[str]]]]
    Libraries: builtins.dict[str, builtins.dict[str, str]]

def ismultiparm(parm: hou.ParmTemplate) -> bool: ...
def describeparm(
    type_name: str, parm: hou.ParmTemplate | None, brief: bool
) -> tuple[None, None] | tuple[None, tuple[hou.ParmTemplate, ...]] | tuple[_ParmDescription, None]: ...
def describeparms(
    type_name: str, parms: Iterable[hou.ParmTemplate | None], brief: bool
) -> builtins.dict[str, _ParmDescription]: ...
def describetype(type: hou.NodeType, brief: bool) -> _TypeDescription: ...
def describealltypes(
    category: hou.OpNodeTypeCategory, printparms: bool, brief: bool
) -> builtins.dict[str, _TypeDescription]: ...
def describenodes(printparms: bool, brief: bool) -> builtins.dict[str, builtins.dict[str, _TypeDescription]]: ...
def describetool(tool: hou.Tool) -> builtins.dict[str, str]: ...
def describeshelf(
    shelf: hou.Shelf,
) -> builtins.dict[str, str | builtins.dict[str, builtins.dict[str, str]]]: ...
def describeshelves() -> builtins.dict[
    str, builtins.dict[str, str | builtins.dict[str, builtins.dict[str, str]]]
]: ...
# vcc's --list-context-json output, under "cvex".
def describevex() -> builtins.dict[str, JSONValue]: ...
# The command and verb names, each with an empty placeholder dict.
def describehscript() -> builtins.dict[str, builtins.dict[str, Never]]: ...
def describeEXPR() -> builtins.dict[str, builtins.dict[str, Never]]: ...
def describeVerbs() -> builtins.dict[str, builtins.dict[str, builtins.dict[str, Never]]]: ...
def describehom() -> builtins.dict[str, builtins.dict[str, builtins.dict[str, list[str]]]]: ...
def describeThirdPartyLibraries() -> builtins.dict[str, builtins.dict[str, str]]: ...

usage: str
parser: optparse.OptionParser
options: optparse.Values
args: list[str]
dict: _Summary
