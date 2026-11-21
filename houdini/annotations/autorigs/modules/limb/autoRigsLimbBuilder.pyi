import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.limb.autoRigsLimbInterfaceBuilder import (
    AutoRigsLimbInterfaceBuilder,
    _LimbControls,
    _LimbNoodleControls,
)
from autorigs.modules.limb.buildLimbGuide import LimbGuide
from autorigs.modules.limb.limbGuideOptions import ModuleOptionsWidget
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.spineModule import SpineModule

class AutoRigsLimbBuilder:
    SUFFIX: dict[str, str]
    NUM_NOODLE_BONES: int
    BEFORE_LIMB_CONTROL_RATIO: float
    LEFT_SIDE_NAME: int
    RIGHT_SIDE_NAME: int
    CENTER_SIDE_NAME: int
    LEFT_LIMB_PREFIX: str
    RIGHT_LIMB_PREFIX: str
    DEFAULT_LIMB_PREFIX: str
    LIMBTYPE: str
    modulename: str

    def __init__(self) -> None: ...
    @classmethod
    def buildLimbRig(
        cls,
        index: int,
        autorigs_asset: AutoRigsAsset,
        options: ModuleOptionsWidget,
        limbguide: LimbGuide,
        parentinfo: tuple[MasterModule | SpineModule, hou.OpNode],
        interfacebuilder: type[AutoRigsLimbInterfaceBuilder],
        modulename: str,
    ) -> tuple[_LimbControls, _LimbControls | None]: ...
    @classmethod
    def buildParmLinks(cls, rigcontrols: _LimbControls) -> None: ...
    @classmethod
    def buildRigSide(
        cls,
        prefix: str,
        autorigs_asset: AutoRigsAsset,
        options: ModuleOptionsWidget,
        limbguide: LimbGuide,
        ismain: bool,
        parent: hou.OpNode,
        modulename: str,
    ) -> _LimbControls: ...
    @classmethod
    def cleanupMainViewport(cls, maincontrols: _LimbControls, rigscale: float) -> None: ...
    @classmethod
    def buildNoodleSide(cls, maincontrols: _LimbControls, prefix: str, rigscale: float) -> _LimbNoodleControls: ...
    @classmethod
    def cleanupNoodleViewport(cls, noodlecontrols: _LimbNoodleControls, rigscale: float) -> None: ...
    @classmethod
    def getPrefix(cls, index: int, side: int) -> str: ...
    @classmethod
    def layoutNodes(cls, nodegroup: hou.NodeGroup, modulename: str, prefix: str) -> None: ...
