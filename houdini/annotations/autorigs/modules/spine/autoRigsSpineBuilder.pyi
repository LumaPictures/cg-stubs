import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.spine.autoRigsSpineInterfaceBuilder import _SpineControls
from autorigs.modules.spine.buildSpineGuide import SpineGuide
from autorigs.modules.spine.spineGuideOptions import ModuleOptions

class AutoRigsSpineBuilder:
    SUFFIX: dict[str, str]
    DEFAULT_SPINE_PREFIX: str
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(cls, index: int, autorig_asset: AutoRigsAsset, options: ModuleOptions, spineguide: SpineGuide, parent: hou.ObjNode | None, modulename: str) -> _SpineControls: ...
    @classmethod
    def buildRigControls(cls, index: int, autorig_asset: AutoRigsAsset, options: ModuleOptions, spineguide: SpineGuide, parent: hou.ObjNode | None, modulename: str) -> _SpineControls: ...
    @classmethod
    def getPrefix(cls, index: int) -> str: ...
    @classmethod
    def layoutNodes(cls, nodegroup: hou.NodeGroup, prefix: str) -> None: ...
