# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.spine.spineGuideOptions import ModuleOptions as ModuleOptions
from typing import TypedDict

class _SpineControls(TypedDict):
    chesthook: hou.ObjNode
    hipshook: hou.ObjNode
    lastspinebone: hou.ObjNode
    shoulderctrl: hou.ObjNode
    localhook: hou.ObjNode
    spinecurve: hou.ObjNode
    coghook: hou.ObjNode
    chestatlocal: hou.ObjNode
    chestatcog: hou.ObjNode
    chestfollowcog: hou.ObjNode
    spinecv3: hou.ObjNode
    chestn: hou.ObjNode
    hipsn: hou.ObjNode
    chestatchesta: hou.ObjNode
    hipsatchesta: hou.ObjNode
    chestablend: hou.ObjNode
    spinecv2: hou.ObjNode
    chestatbelly: hou.ObjNode
    hipsatbelly: hou.ObjNode
    bellyblend: hou.ObjNode
    spinecv1: hou.ObjNode
    spineroot: hou.ObjNode
    spinebonesblend: hou.ObjNode
    pelvisptr: hou.ObjNode
    spinecv0: hou.ObjNode
    spinechopnet: hou.OpNode
    pelvisbone: hou.ObjNode
    chestctrl: hou.ObjNode
    chestactrl: hou.ObjNode
    bellyctrl: hou.ObjNode
    cogctrl: hou.ObjNode
    hipsctrl: hou.ObjNode
    localctrl: hou.ObjNode
    pelvisctrl: hou.ObjNode
    nodegroup: hou.NodeGroup
    bonegroup: hou.NodeGroup
    controlgroup: hou.NodeGroup
    visiblegroup: hou.NodeGroup
    ikcontrols: hou.NodeGroup

class AutoRigsSpineInterfaceBuilder:
    INTERFACE_NAME_LABEL: dict[str, tuple[str, str]]
    CONTROL_DISPLAY_MENU: list[str]
    BONE_DISPLAY_MENU: list[str]
    @classmethod
    def buildRigInterface(cls, autorig_asset: AutoRigsAsset, options: ModuleOptions, controls: _SpineControls, index: int, modulename: str) -> None: ...
    @classmethod
    def linkRigInterfaceParms(cls, controls: _SpineControls, autorig_asset: hou.ObjNode, prefix: str) -> None: ...
    @classmethod
    def buildRigInterfaceParms(cls, controls: _SpineControls, autorig_asset: hou.ObjNode, prefix: str, modulename: str) -> hou.FolderParmTemplate: ...
