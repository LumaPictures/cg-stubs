# Houdini stubs generated from Houdini 22.0.466

import hou
from .quadHeadNodePositions import POS_DICT_HEAD as POS_DICT_HEAD
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.master import masterModule as masterModule
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.quadHead.buildQuadHeadGuide import QuadHeadGuide as QuadHeadGuide
from autorigs.modules.quadHead.quadHeadGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from autorigs.utils import geometryutils as geometryutils, rigutils as rigutils
from typing import ClassVar, TypedDict

class _QuadHeadControls(TypedDict):
    headneckroot: hou.ObjNode
    headneckchop: hou.ObjNode
    neckatlastspine: hou.ObjNode
    neckatcog: hou.ObjNode
    neckblend: hou.ObjNode
    neckroot: hou.ObjNode
    neckbone1: hou.ObjNode
    neckbone2: hou.ObjNode
    neckbone3: hou.ObjNode
    neckbone4: hou.ObjNode
    headroot: hou.ObjNode
    headbone: hou.ObjNode
    headboneblend: hou.ObjNode
    headatchest: hou.ObjNode
    headatcog: hou.ObjNode
    headblend: hou.ObjNode
    headsoloblend: hou.ObjNode
    headsoloctrlblend: hou.ObjNode
    headneckctrl: hou.ObjNode
    headsoloctrl: hou.ObjNode
    neckatchest: hou.ObjNode
    neckaathead: hou.ObjNode
    neckablend: hou.ObjNode
    neckactrl: hou.ObjNode
    neckbctrl: hou.ObjNode
    neckcctrl: hou.ObjNode
    neckdctrl: hou.ObjNode
    headactrlptr: hou.ObjNode
    headactrl: hou.ObjNode
    neckup: hou.ObjNode
    neckupblend: hou.ObjNode
    headup: hou.ObjNode
    headhook: hou.ObjNode
    neckctrl: hou.ObjNode
    neckbctrlathead: hou.ObjNode
    neckbctrlatchest: hou.ObjNode
    neckcctrlathead: hou.ObjNode
    neckcctrlatneckctrl: hou.ObjNode
    neckctrlblend: hou.ObjNode
    neckcblend: hou.ObjNode
    nodegroup: hou.NodeGroup
    bonegroup: hou.NodeGroup
    controlgroup: hou.NodeGroup
    visiblenodegroup: hou.NodeGroup

class AutoRigsQuadHeadBuilder:
    SUFFIX: ClassVar[dict[str, str]]
    DEFAULT_HEAD_PREFIX: ClassVar[str]
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(cls, index: int, autorigs_asset: AutoRigsAsset, options: ModuleOptionsWidget, headguide: QuadHeadGuide, parentinfo: tuple[MasterModule | SpineModule, hou.ObjNode], modulename: str) -> _QuadHeadControls: ...
    @classmethod
    def buildRigControls(cls, index: int, autorigs_asset: AutoRigsAsset, options: ModuleOptionsWidget, headguide: QuadHeadGuide, parentinfo: tuple[MasterModule | SpineModule, hou.ObjNode], modulename: str) -> _QuadHeadControls: ...
    @classmethod
    def boneLengthStr(cls, bone: hou.ObjNode, obj1: hou.ObjNode, obj2: hou.ObjNode) -> str: ...
    @classmethod
    def cleanupMainViewport(cls, controls: _QuadHeadControls, bonegroup: hou.NodeGroup) -> None: ...
    @classmethod
    def getPrefix(cls, index: int) -> str: ...
    @classmethod
    def layoutNodes(cls, nodegroup: hou.NodeGroup, modulename: str, prefix: str) -> None: ...
