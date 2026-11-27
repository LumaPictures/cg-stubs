import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.limb import limbGuideOptions, limbGuideParams, limbModule
from autorigs.modules.limb.limbModule import _LimbModuleJson, _LimbRig
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.spineModule import SpineModule
from autorigs.modules.quadleg.autoRigsQuadLegBuilder import AutoRigsQuadLegBuilder
from autorigs.modules.quadleg.buildQuadLegGuide import QuadLegGuide

class QuadLegModule(
    limbModule.LimbModule[
        limbGuideOptions.QuadLegOptionsWidget, limbGuideParams.QuadLegParamsWidget, QuadLegGuide, "QuadLegGuideTab"
    ]
):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _LimbModuleJson
    guidetab: "QuadLegGuideTab | None"
    builtparentinfo: tuple[MasterModule | SpineModule, hou.OpNode] | None
    autorigsbuilder: AutoRigsQuadLegBuilder
    builtrig: _LimbRig | None
    def __init__(self, autorig_asset: AutoRigsAsset) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _LimbModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _LimbModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...
    def getAnkleHook(self) -> hou.OpNode | None: ...
    def getFootHook(self) -> hou.OpNode | None: ...
    def getMirrorAnkleHook(self) -> hou.OpNode | None: ...
    def getMirrorFootHook(self) -> hou.OpNode | None: ...

class QuadLegGuideTab(
    limbModule.LimbGuideTab[limbGuideOptions.QuadLegOptionsWidget, limbGuideParams.QuadLegParamsWidget, QuadLegGuide]
):
    PREFIX: str
    GUIDE_OPTIONS: type[limbGuideOptions.QuadLegOptionsWidget]
    GUIDE_PARAMS: type[limbGuideParams.QuadLegParamsWidget]
