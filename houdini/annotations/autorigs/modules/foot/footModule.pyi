from collections.abc import Mapping, Sequence

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.arm.armModule import ArmModule
from autorigs.modules.base.rootModule import Module
from autorigs.modules.extremity import extremityModule
from autorigs.modules.extremity.extremityGuideOptions import FootOptionsWidget
from autorigs.modules.extremity.extremityGuideParams import FootParamsWidget
from autorigs.modules.extremity.extremityModule import _ExtremityModuleJson
from autorigs.modules.foot.buildFootGuide import FootGuide
from autorigs.modules.foot.autoRigsFootBuilder import AutoRigsFootBuilder
from autorigs.modules.leg.legModule import LegModule
from autorigs.modules.limb.limbModule import LimbModule
from autorigs.modules.quadleg.quadLegModule import QuadLegModule

class FootModule(extremityModule.ExtremityModule[FootOptionsWidget, FootParamsWidget, FootGuide]):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _ExtremityModuleJson
    autorigs_asset: AutoRigsAsset
    limbmodules: Sequence[LimbModule]
    legmodules: Sequence[LegModule]
    armmodules: Sequence[ArmModule]
    quadlegmodules: Sequence[QuadLegModule]
    guidetab: "FootGuideTab"
    autorigsbuilder: AutoRigsFootBuilder
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset, arg2: object = ..., arg3: object = ...) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Module]]) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _ExtremityModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _ExtremityModuleJson) -> None: ...
    def buildRig(self, orig_asset: AutoRigsAsset, index: int) -> None: ...
    def getModuleHooks(self) -> list[hou.ObjNode | None]: ...

class FootGuideTab(extremityModule.ExtremityGuideTab[FootOptionsWidget, FootParamsWidget, FootGuide]):
    prefix: str
