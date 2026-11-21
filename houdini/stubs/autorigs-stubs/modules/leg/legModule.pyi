# Houdini stubs generated from Houdini 22.0.466

import hou
from . import buildLegGuide as buildLegGuide
from _typeshed import Incomplete
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.leg.autoRigsLegBuilder import AutoRigsLegBuilder as AutoRigsLegBuilder
from autorigs.modules.leg.buildLegGuide import LegGuide as LegGuide
from autorigs.modules.limb import limbGuideOptions as limbGuideOptions, limbGuideParams as limbGuideParams, limbModule as limbModule
from autorigs.modules.limb.limbGuideOptions import LegOptionsWidget as LegOptionsWidget
from autorigs.modules.limb.limbGuideParams import LegParamsWidget as LegParamsWidget
from autorigs.modules.limb.limbModule import _LimbModuleJson
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule

class LegModule(limbModule.LimbModule[LegOptionsWidget, LegParamsWidget, LegGuide]):
    mastermodule: MasterModule
    autorigs_asset: AutoRigsAsset | None
    spinemodules: list[SpineModule]
    builtparentinfo: tuple[MasterModule | SpineModule, hou.OpNode] | None
    autorigsbuilder: AutoRigsLegBuilder
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _LimbModuleJson
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    guidetab: Incomplete
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _LimbModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _LimbModuleJson) -> None: ...
    builtrig: Incomplete
    def buildRig(self, orig_asset: AutoRigsAsset, index: int) -> None: ...
    def getAnkleHook(self) -> hou.OpNode | None: ...
    def getMirrorAnkleHook(self) -> hou.OpNode | None: ...
    def getModuleHooks(self) -> list[hou.OpNode | None]: ...

class LegGuideTab(limbModule.LimbGuideTab[LegOptionsWidget, LegParamsWidget, LegGuide]):
    PREFIX: str
    GUIDE_OPTIONS = limbGuideOptions.LegOptionsWidget
    GUIDE_PARAMS = limbGuideParams.LegParamsWidget
