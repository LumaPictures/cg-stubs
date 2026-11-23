from collections.abc import Iterable, MutableSequence
from typing import Literal, TypedDict, Unpack, overload

import hou

class _FindFiltersBase(TypedDict, total=False):
    node_type: str | None
    node_types: Iterable[str] | None
    node_name: str | None
    node_names: Iterable[str] | None
    node_category: hou.NodeTypeCategory | None
    node_categories: Iterable[hou.NodeTypeCategory] | None
    node_creator: str | None
    node_creators: Iterable[str] | None
    skip_name: str | None
    skip_names: Iterable[str] | None
    skip_type: str | None
    skip_types: Iterable[str] | None
    skip_creator: str | None
    skip_creators: Iterable[str] | None
    skip_bypassed: bool
    skip_first_node: bool
    limit_type: str | None
    limit_types: Iterable[str] | None
    depth_first: bool

class _FindFilters(_FindFiltersBase, total=False):
    skip_not_displayed: bool

class _FindFiltersRecursive(_FindFilters, total=False):
    recursive: bool | hou.NodeType | None

class _FindDisplayedFilters(_FindFiltersBase, total=False):
    recursive: bool | hou.NodeType | None

FIND_CHILD: int
FIND_UPSTREAM: int
FIND_DOWNSTREAM: int
FIND_CONNECTED: int
JUMP_TO_HOME_SUBNET_TIMEOUT: int

class RestoreSelectionAfter:
    selected: tuple[hou.NetworkMovableItem, ...]
    def activate(self) -> None: ...
    def restore_(self) -> None: ...

restoreSelectionAfter: RestoreSelectionAfter

def jumpAllEditorsToNode(node: hou.Node, siblings: MutableSequence[hou.NetworkMovableItem]) -> None: ...
def diveAllEditorsIntoSubnet(node: hou.Node) -> hou.Node: ...
def diveAllEditorsIntoSubnetAndSelectNode(
    node: hou.Node, node_type: str | None = ..., node_name: str | None = ...
) -> None: ...
def findChildNode(
    node: hou.OpNode, recursive: bool | hou.NodeType | None = ..., **kwargs: Unpack[_FindFilters]
) -> hou.OpNode | None: ...
def findChildNodes(
    node: hou.OpNode, recursive: bool | hou.NodeType | None = ..., **kwargs: Unpack[_FindFilters]
) -> list[hou.OpNode]: ...
def findOrCreateChildNode(
    parent_node: hou.OpNode,
    node_type: str,
    new_node_name: str,
    new_node_creator: str | None = ...,
    recursive: bool | hou.NodeType | None = ...,
) -> hou.OpNode: ...
def findUpstreamNode(node: hou.OpNode, **kwargs: Unpack[_FindFiltersRecursive]) -> hou.OpNode | None: ...
def findUpstreamNodes(node: hou.OpNode, **kwargs: Unpack[_FindFiltersRecursive]) -> list[hou.OpNode]: ...
def findUpstreamNodeFromDisplayedNode(
    parent_node: hou.OpNode, **kwargs: Unpack[_FindFiltersRecursive]
) -> hou.OpNode | None: ...
def findDownstreamNode(node: hou.OpNode, **kwargs: Unpack[_FindFiltersRecursive]) -> hou.OpNode | None: ...
def findDownstreamNodes(node: hou.OpNode, **kwargs: Unpack[_FindFiltersRecursive]) -> list[hou.OpNode]: ...
def findDownstreamDisplayedNode(node: hou.OpNode, **kwargs: Unpack[_FindDisplayedFilters]) -> hou.OpNode | None: ...
def findOrCreateDownstreamNode(
    root_node: hou.OpNode,
    node_type: str,
    new_node_name: str,
    new_node_creator: str | None = ...,
    recursive: bool | hou.NodeType | None = ...,
) -> hou.OpNode: ...
def findConnectedNode(node: hou.OpNode, **kwargs: Unpack[_FindFiltersRecursive]) -> hou.OpNode | None: ...
def findConnectedNodes(node: hou.OpNode, **kwargs: Unpack[_FindFiltersRecursive]) -> list[hou.OpNode]: ...
@overload
def findNodes(
    findir: int,
    node: hou.OpNode,
    node_type: str | None = ...,
    node_types: Iterable[str] | None = ...,
    node_name: str | None = ...,
    node_names: Iterable[str] | None = ...,
    node_category: hou.NodeTypeCategory | None = ...,
    node_categories: Iterable[hou.NodeTypeCategory] | None = ...,
    node_creator: str | None = ...,
    node_creators: Iterable[str] | None = ...,
    skip_name: str | None = ...,
    skip_names: Iterable[str] | None = ...,
    skip_type: str | None = ...,
    skip_types: Iterable[str] | None = ...,
    skip_creator: str | None = ...,
    skip_creators: Iterable[str] | None = ...,
    skip_bypassed: bool = ...,
    skip_not_displayed: bool = ...,
    skip_first_node: bool = ...,
    limit_type: str | None = ...,
    limit_types: Iterable[str] | None = ...,
    depth_first: bool = ...,
    find_one: Literal[False] = ...,
    recursive: bool | hou.NodeType | None = ...,
) -> list[hou.OpNode]: ...
@overload
def findNodes(
    findir: int,
    node: hou.OpNode,
    node_type: str | None = ...,
    node_types: Iterable[str] | None = ...,
    node_name: str | None = ...,
    node_names: Iterable[str] | None = ...,
    node_category: hou.NodeTypeCategory | None = ...,
    node_categories: Iterable[hou.NodeTypeCategory] | None = ...,
    node_creator: str | None = ...,
    node_creators: Iterable[str] | None = ...,
    skip_name: str | None = ...,
    skip_names: Iterable[str] | None = ...,
    skip_type: str | None = ...,
    skip_types: Iterable[str] | None = ...,
    skip_creator: str | None = ...,
    skip_creators: Iterable[str] | None = ...,
    skip_bypassed: bool = ...,
    skip_not_displayed: bool = ...,
    skip_first_node: bool = ...,
    limit_type: str | None = ...,
    limit_types: Iterable[str] | None = ...,
    depth_first: bool = ...,
    *,
    find_one: Literal[True],
    recursive: bool | hou.NodeType | None = ...,
) -> hou.OpNode | None: ...
@overload
def findNodes(
    findir: int,
    node: hou.OpNode,
    node_type: str | None = ...,
    node_types: Iterable[str] | None = ...,
    node_name: str | None = ...,
    node_names: Iterable[str] | None = ...,
    node_category: hou.NodeTypeCategory | None = ...,
    node_categories: Iterable[hou.NodeTypeCategory] | None = ...,
    node_creator: str | None = ...,
    node_creators: Iterable[str] | None = ...,
    skip_name: str | None = ...,
    skip_names: Iterable[str] | None = ...,
    skip_type: str | None = ...,
    skip_types: Iterable[str] | None = ...,
    skip_creator: str | None = ...,
    skip_creators: Iterable[str] | None = ...,
    skip_bypassed: bool = ...,
    skip_not_displayed: bool = ...,
    skip_first_node: bool = ...,
    limit_type: str | None = ...,
    limit_types: Iterable[str] | None = ...,
    depth_first: bool = ...,
    find_one: bool = ...,
    recursive: bool | hou.NodeType | None = ...,
) -> list[hou.OpNode] | hou.OpNode | None: ...
def findNodes(
    findir: int,
    node: hou.OpNode,
    node_type: str | None = ...,
    node_types: Iterable[str] | None = ...,
    node_name: str | None = ...,
    node_names: Iterable[str] | None = ...,
    node_category: hou.NodeTypeCategory | None = ...,
    node_categories: Iterable[hou.NodeTypeCategory] | None = ...,
    node_creator: str | None = ...,
    node_creators: Iterable[str] | None = ...,
    skip_name: str | None = ...,
    skip_names: Iterable[str] | None = ...,
    skip_type: str | None = ...,
    skip_types: Iterable[str] | None = ...,
    skip_creator: str | None = ...,
    skip_creators: Iterable[str] | None = ...,
    skip_bypassed: bool = ...,
    skip_not_displayed: bool = ...,
    skip_first_node: bool = ...,
    limit_type: str | None = ...,
    limit_types: Iterable[str] | None = ...,
    depth_first: bool = ...,
    find_one: bool = ...,
    recursive: bool | hou.NodeType | None = ...,
) -> list[hou.OpNode] | hou.OpNode | None: ...
def createChildNode(
    parent_node: hou.OpNode, node_type: str, node_name: str, node_creator: str | None = ...
) -> hou.OpNode: ...
def copyChildNode(parent_node: hou.OpNode, child_node: hou.OpNode, node_creator: str | None = ...) -> hou.OpNode: ...
