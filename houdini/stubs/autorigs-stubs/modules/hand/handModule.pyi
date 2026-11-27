import hou
from . import buildHandGuide as buildHandGuide
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.arm import armModule as armModule
from autorigs.modules.arm.armModule import ArmModule as ArmModule
from autorigs.modules.base.rootModule import Module as Module
from autorigs.modules.extremity import extremityGuideOptions as extremityGuideOptions, extremityGuideParams as extremityGuideParams, extremityModule as extremityModule
from autorigs.modules.extremity.extremityGuideOptions import HandOptionsWidget as HandOptionsWidget
from autorigs.modules.extremity.extremityGuideParams import HandParamsWidget as HandParamsWidget
from autorigs.modules.extremity.extremityModule import _ExtremityModuleJson
from autorigs.modules.hand.autoRigsHandBuilder import AutoRigsHandBuilder as AutoRigsHandBuilder
from autorigs.modules.hand.buildHandGuide import HandGuide as HandGuide
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from collections.abc import Mapping, Sequence

class HandModule(extremityModule.ExtremityModule[HandOptionsWidget, HandParamsWidget, HandGuide, 'HandGuideTab', AutoRigsAsset]):
    autorigs_asset: AutoRigsAsset
    armmodules: Sequence[ArmModule]
    spinemodules: Sequence[SpineModule]
    guidetab: HandGuideTab | None
    autorigsbuilder: AutoRigsHandBuilder
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

class HandGuideTab(extremityModule.ExtremityGuideTab[HandOptionsWidget, HandParamsWidget, HandGuide]):
    PREFIX: str
    GUIDE_OPTIONS = extremityGuideOptions.HandOptionsWidget
    GUIDE_PARAMS = extremityGuideParams.HandParamsWidget
