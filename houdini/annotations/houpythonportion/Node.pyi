from collections.abc import Generator

import hou

def createInputNode(
    self: hou.Node,
    input_index: int,
    node_type_name: str,
    node_name: str | None = ...,
    run_init_scripts: bool = ...,
    load_contents: bool = ...,
    exact_type_name: bool = ...,
) -> hou.Node: ...
def createOutputNode(
    self: hou.Node,
    node_type_name: str,
    node_name: str | None = ...,
    run_init_scripts: bool = ...,
    load_contents: bool = ...,
    exact_type_name: bool = ...,
) -> hou.Node: ...
def allNodes(self: hou.Node) -> Generator[hou.Node, None, None]: ...
