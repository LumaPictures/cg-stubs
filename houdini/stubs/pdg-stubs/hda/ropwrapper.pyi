# Houdini stubs generated from Houdini 22.0.466

import hou
import logging
from pdg.hda.ropconfig import RopConfig as RopConfig, _RopConfigJson
from typing_extensions import TypedDict

class _RopsJson(TypedDict):
    nodes: list[_RopConfigJson]

class RopWrapper:
    config: RopConfig
    log: logging.Logger
    rop_node_group: hou.ParmTemplateGroup
    hda_node: hou.TopNode
    hda: hou.HDADefinition | None
    rop_fetch: hou.TopNode
    rop_node: hou.RopNode
    RootTop: str
    trueroot: hou.OpNode
    RefExcludeType: list[hou.EnumValue[hou.parmTemplateType]]
    Remap: dict[str, str]
    OpParms: list[hou.EnumValue[hou.stringParmType]]
    SyncNodeVersion: str
    ShelfFormat: str
    @classmethod
    def wrapRopsFile(cls, input_file: str, output_dir: str, working_dir: str | None, version: str, verbose: bool = False) -> None: ...
    @classmethod
    def wrapRopsJson(cls, json_data: _RopsJson, output_dir: str, working_dir: str | None, version: str, verbose: bool = False) -> None: ...
    def __init__(self, config: RopConfig) -> None: ...
