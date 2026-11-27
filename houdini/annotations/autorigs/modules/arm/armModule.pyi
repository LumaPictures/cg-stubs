import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.arm.autoRigsArmBuilder import AutoRigsArmBuilder
from autorigs.modules.arm.buildArmGuide import ArmGuide
from autorigs.modules.limb import limbModule
from autorigs.modules.limb.limbGuideOptions import ArmOptionsWidget
from autorigs.modules.limb.limbGuideParams import ArmParamsWidget
from autorigs.modules.limb.limbModule import _LimbModuleJson, _LimbRig
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.spineModule import SpineModule

class ArmModule(limbModule.LimbModule[ArmOptionsWidget, ArmParamsWidget, ArmGuide, "ArmGuideTab"]):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    BIPED_STYLE: int
    QUAD_STYLE: int
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _LimbModuleJson
    modulestyle: int
    autorigsbuilder: AutoRigsArmBuilder
    mastermodule: MasterModule
    spinemodules: list[SpineModule]
    autorigs_asset: AutoRigsAsset | None
    builtparentinfo: tuple[MasterModule | SpineModule, hou.OpNode] | None
    guidetab: "ArmGuideTab | None"
    builtrig: _LimbRig | None
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def buildFromDefault(self, modulestyle: int = ...) -> None: ...
    def buildFromJsonNew(self, json: _LimbModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _LimbModuleJson) -> None: ...
    def buildRig(self, orig_asset: AutoRigsAsset, index: int) -> None: ...
    def getWristHook(self) -> hou.OpNode | None: ...
    def getMirrorWristHook(self) -> hou.OpNode | None: ...
    def getModuleHooks(self) -> list[hou.OpNode | None]: ...

class ArmGuideTab(limbModule.LimbGuideTab[ArmOptionsWidget, ArmParamsWidget, ArmGuide]):
    PREFIX: str
    GUIDE_OPTIONS: type[ArmOptionsWidget]
    GUIDE_PARAMS: type[ArmParamsWidget]
