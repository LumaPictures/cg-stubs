from collections.abc import Mapping, MutableMapping

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.tail.tailGuideOptions import ModuleOptions

class AutoRigsTailInterfaceBuilder:
    INTERFACE_NAME_LABEL: dict[str, tuple[str, str]]
    CONTROL_DISPLAY_MENU: list[str]
    BONE_DISPLAY_MENU: list[str]
    MATCH_FK_IK_POSTFIX: str
    @classmethod
    def buildRigInterface(cls, autorig_asset: AutoRigsAsset, options: ModuleOptions, controls: MutableMapping[str, hou.OpNode | hou.NodeGroup], index: int, modulename: str) -> None: ...
    @classmethod
    def linkRigInterfaceParms(cls, controls: MutableMapping[str, hou.OpNode | hou.NodeGroup], autorig_asset: hou.ObjNode, prefix: str) -> None: ...
    @classmethod
    def buildRigInterfaceParms(cls, controls: MutableMapping[str, hou.OpNode | hou.NodeGroup], autorig_asset: hou.ObjNode, prefix: str, modulename: str) -> hou.FolderParmTemplate: ...
    @classmethod
    def getMatchTailFKtoIKStr(cls, assetnode: hou.ObjNode, controls: Mapping[str, hou.OpNode | hou.NodeGroup], prefix: str) -> str: ...
