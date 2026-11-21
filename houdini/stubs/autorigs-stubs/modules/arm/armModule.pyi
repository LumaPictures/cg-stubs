# Houdini stubs generated from Houdini 22.0.466

import hou
from . import buildArmGuide as buildArmGuide
from _typeshed import Incomplete
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.arm.autoRigsArmBuilder import AutoRigsArmBuilder as AutoRigsArmBuilder
from autorigs.modules.arm.buildArmGuide import ArmGuide as ArmGuide
from autorigs.modules.limb import limbGuideOptions as limbGuideOptions, limbGuideParams as limbGuideParams, limbModule as limbModule
from autorigs.modules.limb.limbGuideOptions import ArmOptionsWidget as ArmOptionsWidget
from autorigs.modules.limb.limbGuideParams import ArmParamsWidget as ArmParamsWidget
from autorigs.modules.limb.limbModule import _LimbModuleJson
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule

class ArmModule(limbModule.LimbModule[ArmOptionsWidget, ArmParamsWidget, ArmGuide]):
    modulestyle: int
    autorigsbuilder: AutoRigsArmBuilder
    mastermodule: MasterModule
    spinemodules: list[SpineModule]
    autorigs_asset: AutoRigsAsset | None
    builtparentinfo: tuple[MasterModule | SpineModule, hou.OpNode] | None
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    BIPED_STYLE: int
    QUAD_STYLE: int
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _LimbModuleJson
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    guidetab: Incomplete
    def buildFromDefault(self, modulestyle: int = ...) -> None: ...
    def buildFromJsonNew(self, json: _LimbModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _LimbModuleJson) -> None: ...
    builtrig: Incomplete
    def buildRig(self, orig_asset: AutoRigsAsset, index: int) -> None: ...
    def getWristHook(self) -> hou.OpNode | None: ...
    def getMirrorWristHook(self) -> hou.OpNode | None: ...
    def getModuleHooks(self) -> list[hou.OpNode | None]: ...

class ArmGuideTab(limbModule.LimbGuideTab[ArmOptionsWidget, ArmParamsWidget, ArmGuide]):
    PREFIX: str
    GUIDE_OPTIONS: type[ArmOptionsWidget]
    GUIDE_PARAMS: type[ArmParamsWidget]
