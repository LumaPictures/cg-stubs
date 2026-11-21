# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Iterable

def endsWithAnyOf(file_path: str, extension_list: Iterable[str]) -> bool: ...
def equalWithAnyOf(file_ext: str, extension_list: Iterable[str]) -> bool: ...
def digitalAssetExtensions() -> list[str]:
    """ Supported extensions for Digital Assets """
def isSupportedAssetPath(file_path: str) -> bool:
    """ Returns whether the asset is supported based on 
        the extension."""
def isSupportedAssetExt(file_ext: str) -> bool:
    """ Returns whether the asset is supported based on 
        the extension."""
def create_instance(node_type: hou.NodeType) -> tuple[hou.Node, hou.Node | None]:
    """
    Create an instance (i.e. a node) of the given node type, finding the
    proper parent node to hold it.
    """
