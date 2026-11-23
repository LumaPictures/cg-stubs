import logging

import hou
from pdg.hda.ropconfig import RopConfig, _RopConfigJson
from typing_extensions import TypedDict

# The ROP wrapper's .json file.
class _RopsJson(TypedDict):
    nodes: list[_RopConfigJson]

class RopWrapper:
    RootTop: str
    # /tasks always exists; the class body dereferences it immediately.
    trueroot: hou.OpNode
    RefExcludeType: list[hou.EnumValue[hou.parmTemplateType]]
    Remap: dict[str, str]
    OpParms: list[hou.EnumValue[hou.stringParmType]]
    SyncNodeVersion: str
    ShelfFormat: str
    config: RopConfig
    log: logging.Logger
    rop_node_group: hou.ParmTemplateGroup
    hda_node: hou.TopNode
    hda: hou.HDADefinition | None
    # Never None once __init__ returns: it dereferences both lookups.
    rop_fetch: hou.TopNode
    rop_node: hou.RopNode
    @classmethod
    def wrapRopsFile(
        cls,
        input_file: str,
        output_dir: str,
        working_dir: str | None,
        version: str,
        verbose: bool = ...,
    ) -> None: ...
    @classmethod
    def wrapRopsJson(
        cls,
        json_data: _RopsJson,
        output_dir: str,
        working_dir: str | None,
        version: str,
        verbose: bool = ...,
    ) -> None: ...
    def __init__(self, config: RopConfig) -> None: ...
