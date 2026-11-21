import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.limb.autoRigsLimbBuilder import AutoRigsLimbBuilder
from autorigs.modules.limb.autoRigsLimbInterfaceBuilder import _LimbControls
from autorigs.modules.limb.buildLimbGuide import LimbGuide
from autorigs.modules.limb.limbGuideOptions import ModuleOptionsWidget
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.spineModule import SpineModule

class AutoRigsLegBuilder(AutoRigsLimbBuilder):
    SUFFIX: dict[str, str]
    LEFT_LIMB_PREFIX: str
    RIGHT_LIMB_PREFIX: str
    DEFAULT_LIMB_PREFIX: str
    LIMBTYPE: str
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(
        cls,
        index: int,
        autorigs_asset: AutoRigsAsset,
        options: ModuleOptionsWidget,
        legguide: LimbGuide,
        spineparent: tuple[MasterModule | SpineModule, hou.OpNode],
        modulename: str,
    ) -> tuple[_LimbControls, _LimbControls | None]: ...
