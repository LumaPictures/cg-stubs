from collections.abc import Set as AbstractSet
from typing import ClassVar, TypeAlias

import hou
import MaterialX as mx

_MtlxValue: TypeAlias = (
    int
    | float
    | bool
    | str
    | mx.Vector2
    | mx.Vector3
    | mx.Vector4
    | mx.Color3
    | mx.Color4
    | mx.Matrix33
    | mx.Matrix44
    | list["_MtlxValue | None"]
)

def defaultPath() -> str: ...

class VOPConverter:
    NODE_SIGNATURE_PATH: ClassVar[str]
    DEFAULT_SIGNATURE: ClassVar[str]
    SUBNET_TYPE: ClassVar[str]
    SUBINPUT_TYPE: ClassVar[str]
    SUBOUTPUT_TYPE: ClassVar[str]
    SUBNETWORKCONNECTOR_TYPE: ClassVar[str]
    SUBNETWORKCONNECTOR_KIND: ClassVar[str]
    PARAMETER_TYPE: ClassVar[str]
    VERBOSE_QUIET: ClassVar[int]
    VERBOSE_WARNING: ClassVar[int]
    VERBOSE_INFO: ClassVar[int]
    SUBNET_INPUTS: ClassVar[set[str]]
    SUBNET_NODES: ClassVar[set[str]]
    TYPE_PATH: ClassVar[str]
    NAME_PATH: ClassVar[str]
    MTLX_RENDERMASK: ClassVar[str]
    CURRENT_MAX_VERSION: ClassVar[tuple[int, int]]

    class Input:
        port_name: str
        port_type: str | None
        default_value: _MtlxValue | None
        def __init__(self, port_name: str, port_type: str | None, default_value: _MtlxValue | None) -> None: ...

    class Output:
        port_name: str
        port_type: str
        vop: hou.VopNode
        def __init__(self, port_name: str, port_type: str, vop: hou.VopNode) -> None: ...

    std_doc: mx.Document
    all_nodes: bool
    graph_only: bool
    hda_only: bool
    tool_menu: str
    verbose: int
    doc: mx.Document | None
    subnet_inputs: "dict[str, VOPConverter.Input] | None"
    subnet_outputs: "dict[str, VOPConverter.Output] | None"
    subnet_nodedefs: dict[str, mx.NodeDef]
    signature_set: AbstractSet[str]
    def __init__(
        self,
        library_path: str | None,
        all_nodes: bool,
        graph_only: bool,
        hda_only: bool,
        tool_menu: str,
        verbose: int,
    ) -> None: ...
    def setSignatureSet(self, signatures: AbstractSet[str]) -> None: ...
    def convert(self, doc: mx.Document, node: hou.VopNode, node_name: str) -> None: ...

def validateShaderNetwork(vop: hou.VopNode, verbose: int) -> bool: ...
def canSaveMaterialX(node: hou.VopNode) -> bool: ...
def saveShaderNetwork(filepath: str, vop: hou.VopNode, mtlx_search_path: str | None = ...) -> None: ...
def main() -> None: ...
