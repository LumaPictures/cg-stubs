import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.leg.autoRigsLegBuilder import AutoRigsLegBuilder
from autorigs.modules.leg.buildLegGuide import LegGuide
from autorigs.modules.limb import limbModule
from autorigs.modules.limb.limbGuideOptions import LegOptionsWidget
from autorigs.modules.limb.limbGuideParams import LegParamsWidget
from autorigs.modules.limb.limbModule import _LimbModuleJson, _LimbRig
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.spineModule import SpineModule

class LegModule(limbModule.LimbModule[LegOptionsWidget, LegParamsWidget, LegGuide, "LegGuideTab"]):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _LimbModuleJson
    mastermodule: MasterModule
    autorigs_asset: AutoRigsAsset | None
    spinemodules: list[SpineModule]
    builtparentinfo: tuple[MasterModule | SpineModule, hou.OpNode] | None
    autorigsbuilder: AutoRigsLegBuilder
    guidetab: "LegGuideTab | None"
    builtrig: _LimbRig | None

    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _LimbModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _LimbModuleJson) -> None: ...
    def buildRig(self, orig_asset: AutoRigsAsset, index: int) -> None: ...
    def getAnkleHook(self) -> hou.OpNode | None: ...
    def getMirrorAnkleHook(self) -> hou.OpNode | None: ...
    def getModuleHooks(self) -> list[hou.OpNode | None]: ...

class LegGuideTab(limbModule.LimbGuideTab[LegOptionsWidget, LegParamsWidget, LegGuide]):
    PREFIX: str
    GUIDE_OPTIONS: type[LegOptionsWidget]
    GUIDE_PARAMS: type[LegParamsWidget]
