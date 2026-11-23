import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base.rootModule import Module
from autorigs.modules.extremity.autoRigsExtremityBuilder import AutoRigsExtremityBuilder
from autorigs.modules.extremity.buildExtremityGuide import ExtremityGuide
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel
from autorigs.modules.master.masterModule import MasterModule

class AutoRigsFootBuilder(AutoRigsExtremityBuilder):
    SUFFIX: dict[str, str]
    def __init__(self) -> None: ...
    @classmethod
    def buildRig(
        cls,
        index: int,
        autorig_asset: AutoRigsAsset,
        optionsmodel: ModuleOptionModel,
        extremityguide: ExtremityGuide,
        mastermodule: MasterModule,
        parentinfo: tuple[Module, hou.ObjNode],
        modulename: str,
    ) -> None: ...
    @classmethod
    def hasAllDegreeBigDigitRoot(cls) -> bool: ...
