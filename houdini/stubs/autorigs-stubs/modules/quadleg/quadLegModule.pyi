import hou
from . import buildQuadLegGuide as buildQuadLegGuide
from _typeshed import Incomplete
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.limb import limbGuideOptions as limbGuideOptions, limbGuideParams as limbGuideParams, limbModule as limbModule
from autorigs.modules.limb.limbModule import _LimbModuleJson
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.quadleg.autoRigsQuadLegBuilder import AutoRigsQuadLegBuilder as AutoRigsQuadLegBuilder
from autorigs.modules.quadleg.buildQuadLegGuide import QuadLegGuide as QuadLegGuide
from autorigs.modules.spine.spineModule import SpineModule as SpineModule

class QuadLegModule(limbModule.LimbModule[limbGuideOptions.QuadLegOptionsWidget, limbGuideParams.QuadLegParamsWidget, QuadLegGuide]):
    guidetab: QuadLegGuideTab
    builtparentinfo: tuple[MasterModule | SpineModule, hou.OpNode] | None
    autorigsbuilder: AutoRigsQuadLegBuilder
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _LimbModuleJson
    def __init__(self, autorig_asset: AutoRigsAsset) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _LimbModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _LimbModuleJson) -> None: ...
    builtrig: Incomplete
    def buildRig(self, index: int) -> None: ...
    def getAnkleHook(self) -> hou.OpNode | None: ...
    def getFootHook(self) -> hou.OpNode | None: ...
    def getMirrorAnkleHook(self) -> hou.OpNode | None: ...
    def getMirrorFootHook(self) -> hou.OpNode | None: ...

class QuadLegGuideTab(limbModule.LimbGuideTab[limbGuideOptions.QuadLegOptionsWidget, limbGuideParams.QuadLegParamsWidget, QuadLegGuide]):
    PREFIX: str
    GUIDE_OPTIONS: type[limbGuideOptions.QuadLegOptionsWidget]
    GUIDE_PARAMS: type[limbGuideParams.QuadLegParamsWidget]
