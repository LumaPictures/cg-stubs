from collections.abc import Mapping, Sequence

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.arm.armModule import ArmModule
from autorigs.modules.base.rootModule import Module
from autorigs.modules.extremity import extremityGuideOptions, extremityGuideParams, extremityModule
from autorigs.modules.extremity.extremityModule import _ExtremityModuleJson
from autorigs.modules.quadFoot.buildQuadFootGuide import QuadFootGuide
from autorigs.modules.leg.legModule import LegModule
from autorigs.modules.limb.limbModule import LimbModule
from autorigs.modules.quadFoot.autoRigsQuadFootBuilder import AutoRigsQuadFootBuilder
from autorigs.modules.quadleg.quadLegModule import QuadLegModule

class QuadFootModule(
    extremityModule.ExtremityModule[
        extremityGuideOptions.QuadFootOptionsWidget, extremityGuideParams.QuadFootParamsWidget, QuadFootGuide
    ]
):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _ExtremityModuleJson
    autorig_asset: AutoRigsAsset
    limbmodules: Sequence[LimbModule]
    legmodules: Sequence[LegModule]
    armmodules: Sequence[ArmModule]
    quadlegmodules: Sequence[QuadLegModule]
    guidetab: "QuadFootGuideTab"
    autorigsbuilder: AutoRigsQuadFootBuilder
    def __init__(self, autorig_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Module]]) -> None: ...
    def buildFromDefault(self, modulestyle: int = ...) -> None: ...
    def buildFromJsonNew(self, json: _ExtremityModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _ExtremityModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class QuadFootGuideTab(
    extremityModule.ExtremityGuideTab[
        extremityGuideOptions.QuadFootOptionsWidget, extremityGuideParams.QuadFootParamsWidget, QuadFootGuide
    ]
):
    prefix: str
