# Houdini stubs generated from Houdini 22.0.466

import hou
from . import buildFootGuide as buildFootGuide
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.arm import armModule as armModule
from autorigs.modules.arm.armModule import ArmModule as ArmModule
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.extremity import extremityGuideOptions as extremityGuideOptions, extremityGuideParams as extremityGuideParams, extremityModule as extremityModule
from autorigs.modules.extremity.extremityGuideOptions import FootOptionsWidget as FootOptionsWidget
from autorigs.modules.extremity.extremityGuideParams import FootParamsWidget as FootParamsWidget
from autorigs.modules.extremity.extremityModule import _ExtremityModuleJson
from autorigs.modules.foot.autoRigsFootBuilder import AutoRigsFootBuilder as AutoRigsFootBuilder
from autorigs.modules.foot.buildFootGuide import FootGuide as FootGuide
from autorigs.modules.leg import legModule as legModule
from autorigs.modules.leg.legModule import LegModule as LegModule
from autorigs.modules.limb.limbModule import LimbModule as LimbModule
from autorigs.modules.quadleg import quadLegModule as quadLegModule
from autorigs.modules.quadleg.quadLegModule import QuadLegModule as QuadLegModule
from autorigs.modules.spine import spineModule as spineModule
from collections.abc import Mapping, Sequence

class FootModule(extremityModule.ExtremityModule[FootOptionsWidget, FootParamsWidget, FootGuide]):
    autorigs_asset: AutoRigsAsset
    limbmodules: Sequence[LimbModule]
    legmodules: Sequence[LegModule]
    armmodules: Sequence[ArmModule]
    quadlegmodules: Sequence[QuadLegModule]
    guidetab: FootGuideTab
    autorigsbuilder: AutoRigsFootBuilder
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _ExtremityModuleJson
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset, arg2: object = None, arg3: object = None) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Module]]) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _ExtremityModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _ExtremityModuleJson) -> None: ...
    def buildRig(self, orig_asset: AutoRigsAsset, index: int) -> None: ...
    def getModuleHooks(self) -> list[hou.ObjNode | None]: ...

class FootGuideTab(extremityModule.ExtremityGuideTab[FootOptionsWidget, FootParamsWidget, FootGuide]):
    prefix: str
    GUIDE_OPTIONS = extremityGuideOptions.FootOptionsWidget
    GUIDE_PARAMS = extremityGuideParams.FootParamsWidget
