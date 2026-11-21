import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.quadHead.autoRigsQuadHeadBuilder import _QuadHeadControls
from autorigs.modules.quadHead.quadHeadGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget
from typing import ClassVar

class AutoRigsQuadHeadInterfaceBuilder:
    INTERFACE_NAME_LABEL: ClassVar[dict[str, tuple[str, str]]]
    DISPLAY_MENU: ClassVar[list[str]]
    @classmethod
    def buildRigInterface(cls, autorigs_asset: AutoRigsAsset, options: ModuleOptionsWidget, controls: _QuadHeadControls, index: int, modulename: str) -> None: ...
    @classmethod
    def linkRigInterfaceParms(cls, controls: _QuadHeadControls, assetnode: hou.ObjNode, prefix: str) -> None: ...
    @classmethod
    def buildRigInterfaceParms(cls, controls: _QuadHeadControls, assetnode: hou.ObjNode, prefix: str, modulename: str) -> hou.FolderParmTemplate: ...
