from typing import Protocol

import hou
from houtypes import ParmCallbackKwargs

theQuickMaterialBaseFilePath: str
theQuickMaterialCloudVolumeLimitExpression: str
theQuickMaterialDefaultRefPrimPaths: dict[str, str]
theQuickMaterialCreatorState: str
theQuickMaterialBaseParmDS: str
theLinkerQuickMaterialBaseParmDS: str


def createQuickSurfaceMaterial(
    quick_material_node: hou.LopNode,
    file_path: str = ...,
    directory: str | None = ...,
    node_name: str | None = ...,
    ref_prim_path: str = ...,
    linker_node: hou.LopNode | None = ...,
    linker_idx: int | None = ...,
) -> None: ...
def createQuickOpenPBRSurfaceMaterial(
    quick_material_node: hou.LopNode,
    file_path: str = ...,
    directory: str | None = ...,
    node_name: str | None = ...,
    ref_prim_path: str = ...,
    linker_node: hou.LopNode | None = ...,
    linker_idx: int | None = ...,
) -> None: ...
def createQuickCloudMaterial(
    quick_material_node: hou.LopNode,
    file_path: str = ...,
    directory: str | None = ...,
    node_name: str | None = ...,
    ref_prim_path: str = ...,
    linker_node: hou.LopNode | None = ...,
    linker_idx: int | None = ...,
) -> None: ...
class _QuickMaterialFunc(Protocol):
    def __call__(
        self,
        quick_material_node: hou.LopNode,
        file_path: str = ...,
        directory: str | None = ...,
        node_name: str | None = ...,
        ref_prim_path: str = ...,
        linker_node: hou.LopNode | None = ...,
        linker_idx: int | None = ...,
    ) -> None: ...

_quick_mat_funcs: dict[str, _QuickMaterialFunc]
def createQuickMaterialsMenu() -> list[str]: ...
def createUsdMaterialCopMenu() -> list[str]: ...
def setupUsdMaterialCop(node: hou.CopNode, material_name: str = ...) -> None: ...
def importGeometryToCopNetwork(kwargs: ParmCallbackKwargs | None = ...) -> None: ...
