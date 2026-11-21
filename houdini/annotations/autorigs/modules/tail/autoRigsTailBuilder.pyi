import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.spineModule import SpineModule
from autorigs.modules.tail.buildTailGuide import TailGuide
from autorigs.modules.tail.tailGuideOptions import ModuleOptions

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
    def makeRestAttribute(cls, node: hou.OpNode, guidepos: hou.Matrix4) -> None: ...
    @classmethod
    def layoutNodes(cls, nodegroup: hou.NodeGroup, modulename: str, prefix: str) -> None: ...
