# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.arm import armModule as armModule
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.extremity.autoRigsExtremityBuilder import AutoRigsExtremityBuilder as AutoRigsExtremityBuilder
from autorigs.modules.extremity.buildExtremityGuide import ExtremityGuide as ExtremityGuide
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel as ModuleOptionModel
from autorigs.modules.master.masterModule import MasterModule as MasterModule

class AutoRigsHandBuilder(AutoRigsExtremityBuilder):
    SUFFIX: dict[str, str]
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(cls, index: int, autorig_asset: AutoRigsAsset, optionsmodel: ModuleOptionModel, extremityguide: ExtremityGuide, mastermodule: MasterModule, parentinfo: tuple[Module, hou.ObjNode], modulename: str) -> None: ...
    @classmethod
    def hasAllDegreeBigDigitRoot(cls) -> bool: ...
