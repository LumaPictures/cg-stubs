from collections.abc import Generator
from typing import overload

import hou

# Not Self: the new node is a sibling, whose class can differ (a lopnet among ObjNodes).
@overload
def createInputNode(
    self: hou.OpNode,
    input_index: int,
    node_type_name: str,
    node_name: str | None = ...,
    run_init_scripts: bool = ...,
    load_contents: bool = ...,
    exact_type_name: bool = ...,
) -> hou.OpNode: ...
@overload
def createInputNode(
    self: hou.Node,
    input_index: int,
    node_type_name: str,
    node_name: str | None = ...,
    run_init_scripts: bool = ...,
    load_contents: bool = ...,
    exact_type_name: bool = ...,
) -> hou.Node: ...
def createInputNode(
    self: hou.Node,
    input_index: int,
    node_type_name: str,
    node_name: str | None = ...,
    run_init_scripts: bool = ...,
    load_contents: bool = ...,
    exact_type_name: bool = ...,
) -> hou.Node: ...
@overload
def createOutputNode(
    self: hou.OpNode,
    node_type_name: str,
    node_name: str | None = ...,
    run_init_scripts: bool = ...,
    load_contents: bool = ...,
    exact_type_name: bool = ...,
) -> hou.OpNode: ...
@overload
def createOutputNode(
    self: hou.Node,
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
@overload
def allNodes(self: hou.OpNode) -> Generator[hou.OpNode, None, None]: ...
@overload
def allNodes(self: hou.Node) -> Generator[hou.Node, None, None]: ...
def allNodes(self: hou.Node) -> Generator[hou.Node, None, None]: ...
