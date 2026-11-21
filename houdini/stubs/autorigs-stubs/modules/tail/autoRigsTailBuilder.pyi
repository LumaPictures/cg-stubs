# Houdini stubs generated from Houdini 22.0.466

import hou
from .tailNodePositions import POS_DICT_TAIL as POS_DICT_TAIL
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.master import masterModule as masterModule
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from autorigs.modules.tail.buildTailGuide import TailGuide as TailGuide
from autorigs.modules.tail.tailGuideOptions import ModuleOptions as ModuleOptions
from autorigs.utils import geometryutils as geometryutils, rigutils as rigutils

class AutoRigsTailBuilder:
    SUFFIX: dict[str, str]
    DEFAULT_TAIL_PREFIX: str
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(cls, index: int, autorig_asset: AutoRigsAsset, options: ModuleOptions, tailguide: TailGuide, parentinfo: tuple[MasterModule | SpineModule, hou.ObjNode], modulename: str) -> dict[str, hou.OpNode | hou.NodeGroup]: ...
    @classmethod
    def buildRigControls(cls, index: int, autorig_asset: AutoRigsAsset, options: ModuleOptions, tailguide: TailGuide, parentnode: tuple[MasterModule | SpineModule, hou.ObjNode], modulename: str) -> dict[str, hou.OpNode | hou.NodeGroup]: ...
    @classmethod
    def getPrefix(cls, index: int) -> str: ...
    @classmethod
    def makeRestAttribute(cls, node: hou.OpNode, guidepos: hou.Matrix4) -> None:
        """ this function will create a rest position attribute on a null"""
    @classmethod
    def layoutNodes(cls, nodegroup: hou.NodeGroup, modulename: str, prefix: str) -> None: ...
