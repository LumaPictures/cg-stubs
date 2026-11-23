import hou
from houtypes import ParmCallbackKwargs
from typing import Protocol

class _QuickMaterialFunc(Protocol):
    def __call__(self, quick_material_node: hou.LopNode, file_path: str = ..., directory: str | None = ..., node_name: str | None = ..., ref_prim_path: str = ..., linker_node: hou.LopNode | None = ..., linker_idx: int | None = ...) -> None: ...

theQuickMaterialBaseFilePath: str
theQuickMaterialCloudVolumeLimitExpression: str
theQuickMaterialDefaultRefPrimPaths: dict[str, str]
theQuickMaterialCreatorState: str

def createQuickSurfaceMaterial(quick_material_node: hou.LopNode, file_path: str = ..., directory: str | None = None, node_name: str | None = None, ref_prim_path: str = ..., linker_node: hou.LopNode | None = None, linker_idx: int | None = None) -> None: ...
def createQuickOpenPBRSurfaceMaterial(quick_material_node: hou.LopNode, file_path: str = ..., directory: str | None = None, node_name: str | None = None, ref_prim_path: str = ..., linker_node: hou.LopNode | None = None, linker_idx: int | None = None) -> None: ...
def createQuickCloudMaterial(quick_material_node: hou.LopNode, file_path: str = ..., directory: str | None = None, node_name: str | None = None, ref_prim_path: str = ..., linker_node: hou.LopNode | None = None, linker_idx: int | None = None) -> None: ...

_quick_mat_funcs: dict[str, _QuickMaterialFunc]

def createQuickMaterialsMenu() -> list[str]:
    """
    Generates the drop-down menu for populating a Quick Materials menu
    """

theQuickMaterialBaseParmDS: str
theLinkerQuickMaterialBaseParmDS: str

def createUsdMaterialCopMenu() -> list[str]:
    """ Returns the menu entries containing known USD materials
        that a USD Material COP can be configured to use.
    """
def setupUsdMaterialCop(node: hou.CopNode, material_name: str = '') -> None:
    """ Add spare parameters to the COP node to configure it as a 
        USD Material COP for a particular material.
    """
def importGeometryToCopNetwork(kwargs: ParmCallbackKwargs | None = None) -> None:
    """
    Shortcut to import the unpacked USD prims into a SOP Import COP. Used by
    nodes like the Texture Material Library LOP.
    """
