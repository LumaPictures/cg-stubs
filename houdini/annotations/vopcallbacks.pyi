from collections.abc import Sequence
from typing import TypeAlias

import hou

_GeneratedNodes: TypeAlias = tuple[hou.VopNode, tuple[hou.VopNode, ...]] | tuple[()]

class ShaderFxCallbacks:
    def generateNodes(
        self,
        target_node: hou.VopNode,
        input_index: int,
        parm: hou.ParmTuple | None,
        effect_type: str | None,
        common_source_nodes: Sequence[hou.VopNode],
    ) -> _GeneratedNodes: ...

class MyShaderFxCallbacks(ShaderFxCallbacks):
    def generateNodes(
        self,
        target_node: hou.VopNode,
        input_index: int,
        parm: hou.ParmTuple | None,
        effect_type: str | None,
        common_source_nodes: Sequence[hou.VopNode],
    ) -> _GeneratedNodes: ...
