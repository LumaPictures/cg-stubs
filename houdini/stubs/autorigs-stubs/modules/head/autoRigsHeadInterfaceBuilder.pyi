import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.head.headGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget
from typing import TypedDict

class _HeadControls(TypedDict):
    headneckroot: hou.ObjNode
    headneckchopnet: hou.ObjNode
    neckatlastspine: hou.ObjNode
    neckatcog: hou.ObjNode
    neckblend: hou.ObjNode
    neckroot: hou.ObjNode
    neckbone1: hou.ObjNode
    neckbone2: hou.ObjNode
    headroot: hou.ObjNode
    headbone: hou.ObjNode
    headweighthelperroot: hou.ObjNode
    headweighthelper: hou.ObjNode
    headatchest: hou.ObjNode
    headatcog: hou.ObjNode
    headblend: hou.ObjNode
    headctrl: hou.ObjNode
    neckatchest: hou.ObjNode
    neckaathead: hou.ObjNode
    neckablend: hou.ObjNode
    neckactrl: hou.ObjNode
    neckbctrl: hou.ObjNode
    headactrlptr: hou.ObjNode
    headactrl: hou.ObjNode
    neckup: hou.ObjNode
    headup: hou.ObjNode
    headhook: hou.ObjNode
    nodegroup: hou.NodeGroup
    bonegroup: hou.NodeGroup
    controlgroup: hou.NodeGroup
    visiblenodegroup: hou.NodeGroup
    ikcontrols: hou.NodeGroup

class AutoRigsHeadInterfaceBuilder:
    INTERFACE_NAME_LABEL: dict[str, tuple[str, str]]
    DISPLAY_MENU: list[str]
    @classmethod
    def buildRigInterface(cls, autorigs_asset: AutoRigsAsset, options: ModuleOptionsWidget, controls: _HeadControls, index: int, modulename: str) -> None: ...
    @classmethod
    def linkRigInterfaceParms(cls, controls: _HeadControls, assetnode: hou.OpNode, prefix: str) -> None: ...
    @classmethod
    def buildRigInterfaceParms(cls, controls: _HeadControls, assetnode: hou.OpNode, prefix: str, modulename: str) -> hou.FolderParmTemplate: ...
