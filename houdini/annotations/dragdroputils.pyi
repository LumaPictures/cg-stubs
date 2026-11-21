import hou
from collections.abc import Callable, Iterator
from typing import Any

class Source:
    def hasData(self, token: str) -> bool: ...
    def data(self, token: str) -> Iterator[Any]: ...

def findOrCreateSop(
    target_node: hou.ObjNode | hou.SopNode,
    node_type_name: str,
    exact_node_type: bool,
    new_node_name: str | None,
    test_func: Callable[[hou.SopNode], bool] | None = ...,
) -> hou.SopNode: ...
def assignPrimGroupMaterial(node: hou.ObjNode | hou.SopNode, group_name: str, material_node: hou.Node) -> None: ...
