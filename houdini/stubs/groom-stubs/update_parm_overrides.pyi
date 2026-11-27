import hou
from collections.abc import Iterable, Iterator
from os import PathLike
from typing import TypedDict
from typing_extensions import NotRequired

class _OverrideParm(TypedDict):
    name: str
    default_attrib_name: str
    allowcurveattrib: NotRequired[bool]
    allowclumpattrib: NotRequired[bool]
    curve_is_clump: NotRequired[bool]
    barbramptoggle: NotRequired[bool]
    uvmodes: NotRequired[int]

class _TypeOverrides(TypedDict):
    parms: list[_OverrideParm]
    core: NotRequired[str]
    loop_iteration_expr: NotRequired[str]
    skininput: NotRequired[int]
    texturepriminput: NotRequired[int]

support_dir: str
loadedfiles: set[str]
cattypemaps: dict[hou.NodeTypeCategory, dict[str, object]]

def allParmTemplates(group_or_folder: hou.ParmTemplateGroup | hou.FolderParmTemplate) -> Iterator[hou.ParmTemplate]: ...
def find(name: str, path: str) -> list[str]: ...
def hdaUseSourceDefinition(nodetype: hou.OpNodeType) -> hou.HDADefinition | None: ...
def replace_ds_in_source(source_file: str | PathLike[str], ds: str) -> None: ...
def break_up_ds(ds: str) -> str: ...
def link_ramp(targetnodepath: str, source: str, target: str) -> None: ...
def update_overrides(typename: str, parmdicts: Iterable[_OverrideParm], core: str | None = None, skininput: int = 1, texturepriminput: int = 2, loop_iteration_expr: str | None = None) -> None: ...

parms: dict[str, _TypeOverrides]

def main(do_core: bool, typepatterns: Iterable[str]) -> None: ...
