from collections.abc import Collection, Iterable
from typing import Protocol, TypeAlias

import hou
from husd.assetutils import _AssetDataSourceInfo, _AssetInfo

class _AssetGeneratorSig(Protocol):
    def __call__(
        self,
        container: hou.Node,
        asset_info: _AssetInfo | _AssetDataSourceInfo,
        primpath: str,
        prev_item: hou.NetworkMovableItem | None,
        next_node: hou.Node | None,
        force_gen: bool = ...,
    ) -> hou.Node | None: ...

AssetGeneratorSig: TypeAlias = _AssetGeneratorSig

DARK_GREY: hou.Color

def selectBrushByType(brush_type_name: str) -> None: ...
def requestHUDUpdate() -> None: ...
def currentBrushNode() -> hou.SopNode | None: ...
def getInstancerPath(node: hou.OpNode | None) -> str | None: ...
def deleteEdits(delta: hou.Geometry | None, indices: Collection[int], instancer_path: str) -> hou.Geometry | None: ...
def applyParmSet(node: hou.OpNode, parmlist: Iterable[tuple[str, int | float | str]]) -> None: ...
def createMouseEventHandler(container: hou.OpNode) -> hou.OpNode: ...
def generateBrushTemplate(brush: hou.OpNode) -> None: ...
def generateBrushPythonModule(definition: hou.HDADefinition) -> None: ...
def generateBrushDebugger(
    existing_points: hou.Geometry,
    static_geo: hou.Geometry,
    asset_geo: hou.Geometry,
    stroke: hou.Geometry,
    working_set: hou.Geometry,
) -> None: ...
