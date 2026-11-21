import hou
from .headNodePositions import POS_DICT_HEAD as POS_DICT_HEAD
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.head.autoRigsHeadInterfaceBuilder import _HeadControls
from autorigs.modules.head.buildHeadGuide import HeadGuide as HeadGuide
from autorigs.modules.head.headGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget
from autorigs.modules.master import masterModule as masterModule
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from autorigs.utils import geometryutils as geometryutils, rigutils as rigutils

class AutoRigsHeadBuilder:
    SUFFIX: dict[str, tuple[str, tuple[float, float] | None]]
    DEFAULT_HEAD_PREFIX: str
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(cls, index: int, autorigs_asset: AutoRigsAsset, options: ModuleOptionsWidget, headguide: HeadGuide, parentinfo: tuple[MasterModule | SpineModule, hou.ObjNode], modulename: str) -> _HeadControls: ...
    @classmethod
    def buildRigControls(cls, index: int, autorigs_asset: AutoRigsAsset, options: ModuleOptionsWidget, headguide: HeadGuide, parentinfo: tuple[MasterModule | SpineModule, hou.ObjNode]) -> _HeadControls: ...
    @classmethod
    def cleanupMainViewport(cls, controls: _HeadControls, bonegroup: hou.NodeGroup) -> None: ...
    @classmethod
    def getPrefix(cls, index: int) -> str: ...
    @classmethod
    def layoutNodes(cls, nodegroup: hou.NodeGroup, prefix: str) -> None: ...
