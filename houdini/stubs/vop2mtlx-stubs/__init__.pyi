# Houdini stubs generated from Houdini 22.0.466

import MaterialX as mx
import hou
from collections.abc import Set as AbstractSet
from typing import ClassVar

from typing import TypeAlias
from typing import TypeAlias
_MtlxValue: TypeAlias = int | float | bool | str | mx.Vector2 | mx.Vector3 | mx.Vector4 | mx.Color3 | mx.Color4 | mx.Matrix33 | mx.Matrix44 | list['_MtlxValue | None']
def defaultPath() -> str: ...

class VOPConverter:
    """Wrapper class for the functions and constants used in converting a VOP
    into a MaterialX nodegraph/nodedef
    """
    std_doc: mx.Document
    all_nodes: bool
    graph_only: bool
    hda_only: bool
    tool_menu: str
    verbose: int
    doc: mx.Document | None
    subnet_nodedefs: dict[str, mx.NodeDef]
    signature_set: AbstractSet[str]
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
        """Data structure to hold some relevant input data including input name
        and type of input found in the VOP for that input
        """
        port_name: str
        port_type: str | None
        default_value: _MtlxValue | None
        def __init__(self, port_name: str, port_type: str | None, default_value: _MtlxValue | None) -> None: ...
    class Output:
        """Data structure to hold some relevant output data including output
        name, type of output and the VOP that the output comes from
        """
        port_name: str
        port_type: str
        vop: hou.VopNode
        def __init__(self, port_name: str, port_type: str, vop: hou.VopNode) -> None: ...
    subnet_inputs: dict[str, VOPConverter.Input] | None
    subnet_outputs: dict[str, VOPConverter.Output] | None
    def __init__(self, library_path: str | None, all_nodes: bool, graph_only: bool, hda_only: bool, tool_menu: str, verbose: int) -> None: ...
    def setSignatureSet(self, signatures: AbstractSet[str]) -> None: ...
    def convert(self, doc: mx.Document, node: hou.VopNode, node_name: str) -> None:
        """ Main function to call when attempting to convert an arbitrary node
        """

def validateShaderNetwork(vop: hou.VopNode, verbose: int) -> bool:
    """Full validation of shader network to see if it can be saved as a
    MaterialX file
    """
def canSaveMaterialX(node: hou.VopNode) -> bool:
    """Function used by OPMenu to estimate if the shader network can be saved as
    a MaterialX file
    """
def saveShaderNetwork(filepath: str, vop: hou.VopNode, mtlx_search_path: str | None = None) -> None: ...
def main() -> None:
    """ Main function. Parses the command line arguments and calls
        appropriate functions to execute it.
    """
