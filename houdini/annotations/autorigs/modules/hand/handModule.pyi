from collections.abc import Mapping, Sequence

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.arm.armModule import ArmModule
from autorigs.modules.base.rootModule import Module
from autorigs.modules.extremity import extremityModule
from autorigs.modules.extremity.extremityGuideOptions import HandOptionsWidget
from autorigs.modules.extremity.extremityGuideParams import HandParamsWidget
from autorigs.modules.extremity.extremityModule import _ExtremityModuleJson
from autorigs.modules.hand.autoRigsHandBuilder import AutoRigsHandBuilder
from autorigs.modules.hand.buildHandGuide import HandGuide
from autorigs.modules.spine.spineModule import SpineModule

class HandModule(extremityModule.ExtremityModule[HandOptionsWidget, HandParamsWidget, HandGuide]):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _ExtremityModuleJson
    autorigs_asset: AutoRigsAsset
    armmodules: Sequence[ArmModule]
    spinemodules: Sequence[SpineModule]
    guidetab: "HandGuideTab"
    autorigsbuilder: AutoRigsHandBuilder
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset, arg2: object = ..., arg3: object = ...) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Module]]) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _ExtremityModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _ExtremityModuleJson) -> None: ...
    def buildRig(self, orig_asset: AutoRigsAsset, index: int) -> None: ...
    def getModuleHooks(self) -> list[hou.ObjNode | None]: ...

class HandGuideTab(extremityModule.ExtremityGuideTab[HandOptionsWidget, HandParamsWidget, HandGuide]):
    PREFIX: str
