# Houdini stubs generated from Houdini 22.0.466

from houtypes import JSONValue
from typing_extensions import NotRequired, Required, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_ExtraNode: TypeAlias = tuple[str, str, bool, dict[str, JSONValue], list['_ExtraNode'], str]
class _DiveToggleJson(TypedDict):
    name: str
    label: str
    default: bool

class _ScriptOverrideJson(TypedDict):
    parm: str
    script: str

class _SectionOverrideJson(TypedDict):
    name: str
    script: str

class _ExtraNodeJson(TypedDict):
    type: str
    name: str
    connect: NotRequired[bool]
    parms: NotRequired[dict[str, JSONValue]]
    children: NotRequired[list['_ExtraNodeJson']]
    target: NotRequired[str]

class _RopConfigJson(TypedDict, total=False):
    assetname: Required[str]
    assetlabel: Required[str]
    assetfile: Required[str]
    assetversion: str
    assetcategory: str
    assetdesc: str
    roptype: Required[str]
    ropexact: bool
    ropname: Required[str]
    ropexcludeparms: list[str]
    ropexcludespare: bool
    ropexcluderefs: list[str]
    ropkeepmenus: list[str]
    ropbackref: str
    sourceparm: str
    outputparm: str
    outputtag: str
    fetchdistribute: bool
    fetchbatch: bool
    fetchtiles: bool
    fetchdebug: bool
    divetarget: str
    divetoggle: _DiveToggleJson
    scriptoverrides: list[_ScriptOverrideJson]
    sectionoverrides: list[_SectionOverrideJson]
    editable: bool
    extranodes: list[_ExtraNodeJson]
    defaults: dict[str, JSONValue]
    hidden: list[str]
    expand: bool

class RopConfig:
    output_dir: str
    asset_name: str
    asset_label: str
    asset_file: str
    asset_version: str
    asset_category: str
    asset_desc: str
    rop_type: str
    rop_exact: bool
    rop_name: str
    rop_exclude: list[str]
    rop_exclude_spare: bool
    rop_exclude_ref: list[str]
    rop_keep_menu: list[str]
    rop_back_ref: str
    source_parm: str
    output_parm: str
    output_tag: str
    fetch_distribute: bool
    fetch_batch: bool
    fetch_tiles: bool
    fetch_debug: bool
    dive_target: str
    dive_toggle: tuple[str, str, bool] | None
    script_overrides: dict[str, str]
    section_overrides: dict[str, str]
    editable: bool
    extra_nodes: list[_ExtraNode]
    defaults: dict[str, JSONValue]
    hidden: list[str]
    expand: bool
    folders: list[tuple[str, str]]
    rop_parms: dict[str, list[str]]
    fetch_parms: dict[str, list[str]]
    fetch_exclude: list[str]
    SepParm: str
    FolderParm: str
    BatchParms: list[str]
    OutputParms: list[str]
    DistribParms: list[str]
    TileParms: list[str]
    MantraTileParms: dict[str, str]
    DebugParms: list[str]
    RopParms: list[str]
    RopScript: list[str]
    RopManual: list[str]
    def __init__(self, output_dir: str, working_dir: str | None, version: str, json_data: _RopConfigJson) -> None: ...
