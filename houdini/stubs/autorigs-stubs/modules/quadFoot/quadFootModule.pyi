# Houdini stubs generated from Houdini 22.0.466

from . import buildQuadFootGuide as buildQuadFootGuide
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.arm import armModule as armModule
from autorigs.modules.arm.armModule import ArmModule as ArmModule
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.extremity import extremityGuideOptions as extremityGuideOptions, extremityGuideParams as extremityGuideParams, extremityModule as extremityModule
from autorigs.modules.extremity.extremityModule import _ExtremityModuleJson
from autorigs.modules.leg import legModule as legModule
from autorigs.modules.leg.legModule import LegModule as LegModule
from autorigs.modules.limb.limbModule import LimbModule as LimbModule
from autorigs.modules.quadFoot.autoRigsQuadFootBuilder import AutoRigsQuadFootBuilder as AutoRigsQuadFootBuilder
from autorigs.modules.quadFoot.buildQuadFootGuide import QuadFootGuide as QuadFootGuide
from autorigs.modules.quadleg import quadLegModule as quadLegModule
from autorigs.modules.quadleg.quadLegModule import QuadLegModule as QuadLegModule
from autorigs.modules.spine import spineModule as spineModule
from collections.abc import Mapping, Sequence

class QuadFootModule(extremityModule.ExtremityModule[extremityGuideOptions.QuadFootOptionsWidget, extremityGuideParams.QuadFootParamsWidget, QuadFootGuide]):
    autorig_asset: AutoRigsAsset
    limbmodules: Sequence[LimbModule]
    legmodules: Sequence[LegModule]
    armmodules: Sequence[ArmModule]
    quadlegmodules: Sequence[QuadLegModule]
    guidetab: QuadFootGuideTab
    autorigsbuilder: AutoRigsQuadFootBuilder
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _ExtremityModuleJson
    def __init__(self, autorig_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Module]]) -> None: ...
    def buildFromDefault(self, modulestyle: int = 0) -> None: ...
    def buildFromJsonNew(self, json: _ExtremityModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _ExtremityModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class QuadFootGuideTab(extremityModule.ExtremityGuideTab[extremityGuideOptions.QuadFootOptionsWidget, extremityGuideParams.QuadFootParamsWidget, QuadFootGuide]):
    prefix: str
    GUIDE_OPTIONS = extremityGuideOptions.QuadFootOptionsWidget
    GUIDE_PARAMS = extremityGuideParams.QuadFootParamsWidget
