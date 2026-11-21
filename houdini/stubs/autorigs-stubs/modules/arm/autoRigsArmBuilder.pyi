# Houdini stubs generated from Houdini 22.0.466

import hou
from .autoRigsArmInterfaceBuilder import AutoRigsArmInterfaceBuilder as AutoRigsArmInterfaceBuilder
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.limb.autoRigsLimbBuilder import AutoRigsLimbBuilder as AutoRigsLimbBuilder
from autorigs.modules.limb.autoRigsLimbInterfaceBuilder import _LimbControls
from autorigs.modules.limb.buildLimbGuide import LimbGuide as LimbGuide
from autorigs.modules.limb.limbGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule

class AutoRigsArmBuilder(AutoRigsLimbBuilder):
    SUFFIX: dict[str, str]
    LEFT_SIDE_NAME: int
    RIGHT_SIDE_NAME: int
    CENTER_SIDE_NAME: int
    LEFT_LIMB_PREFIX: str
    RIGHT_LIMB_PREFIX: str
    DEFAULT_LIMB_PREFIX: str
    LIMBTYPE: str
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(cls, index: int, autorigs_asset: AutoRigsAsset, options: ModuleOptionsWidget, armguide: LimbGuide, parent: tuple[MasterModule | SpineModule, hou.OpNode], modulename: str) -> tuple[_LimbControls, _LimbControls | None]: ...
