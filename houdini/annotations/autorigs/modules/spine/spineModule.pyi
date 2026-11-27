from collections.abc import Mapping, Sequence
from typing import TypeAlias

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base import rootModule as Mod
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.base.moduleTabsWidget import ModuleTabsWidget
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.autoRigsSpineBuilder import AutoRigsSpineBuilder
from autorigs.modules.spine.autoRigsSpineInterfaceBuilder import _SpineControls
from autorigs.modules.spine.buildSpineGuide import SpineGuide
from autorigs.modules.spine.spineGuideOptions import ModuleOptions, _SpineOptionsJson
from autorigs.modules.spine.spineGuideParams import ModuleParams, _SpineParamsJson
from autorigs.modules.base.rootModule import _ModuleJson, _ModuleJsonWithNode

_SpineModuleJson: TypeAlias = _ModuleJson[_SpineOptionsJson, _SpineParamsJson, _GuideNamesJson]

class SpineModule(
    Mod.Module[
        _SpineOptionsJson,
        _SpineParamsJson,
        _GuideNamesJson,
        ModuleOptions,
        ModuleParams,
        SpineGuide,
        _SpineControls | None,
        None,
        None,
        "SpineGuideTab",
        AutoRigsAsset,
    ]
):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _ModuleJsonWithNode[_SpineOptionsJson, _SpineParamsJson, _GuideNamesJson]
    autorigs_asset: AutoRigsAsset
    mastermodule: MasterModule
    assetnode: hou.ObjNode
    builtRig: None
    hookrigmap: None
    guidetab: "SpineGuideTab | None"
    autorigsbuilder: AutoRigsSpineBuilder
    hookrigmapping: dict[str, hou.ObjNode | None]
    buildguides: SpineGuide
    builtrig: _SpineControls | None
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def buildFromDefault(self, modulestyle: int = ...) -> None: ...
    def buildFromJsonNew(self, json: _SpineModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _SpineModuleJson) -> None: ...
    def buildRig(self, orig_asset: AutoRigsAsset, index: int) -> None: ...
    def buildHookRigMapping(self) -> None: ...
    def getModuleHooks(self) -> list[hou.OpNode | None]: ...
    def getGuideTopHook(self) -> hou.OpNode | None: ...
    def getGuideBaseHook(self) -> hou.OpNode | None: ...
    def getBuiltShoulderCtrl(self) -> hou.ObjNode | None: ...
    def getBuiltCOGCtrl(self) -> hou.ObjNode | None: ...
    def getBuiltChestCtrl(self) -> hou.ObjNode | None: ...
    def getBuiltShoulderHook(self) -> hou.ObjNode | None: ...
    def getBuiltHipsHook(self) -> hou.ObjNode | None: ...
    def getBuiltLocalHook(self) -> hou.ObjNode | None: ...
    def getLastSpineBone(self) -> hou.ObjNode | None: ...

class SpineGuideTab(
    Mod.ModuleGuideTab[_SpineOptionsJson, _SpineParamsJson, _GuideNamesJson, ModuleOptions, ModuleParams, SpineGuide, ModuleTabsWidget]
):
    PREFIX: str
    assetnode: hou.ObjNode
    tabswidget: ModuleTabsWidget
    buildguides: SpineGuide
    optionswidget: ModuleOptions
    paramswidget: ModuleParams
    def __init__(self, assetnode: hou.ObjNode, buildguides: SpineGuide, mastermodule: MasterModule) -> None: ...
