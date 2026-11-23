from collections.abc import Mapping, Sequence
from typing import TypeAlias

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base import rootModule as Mod
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.base.moduleTabsWidget import ModuleTabsWidget
from autorigs.modules.head.autoRigsHeadBuilder import AutoRigsHeadBuilder
from autorigs.modules.head.autoRigsHeadInterfaceBuilder import _HeadControls
from autorigs.modules.head.buildHeadGuide import HeadGuide
from autorigs.modules.head.headGuideOptions import ModuleOptionsWidget, _HeadOptionsJson
from autorigs.modules.head.headGuideParams import ModuleParamsWidget, _HeadParamsJson
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.spineModule import SpineModule
from autorigs.modules.base.rootModule import _ModuleJson, _ModuleJsonWithNode

_HeadModuleJson: TypeAlias = _ModuleJson[_HeadOptionsJson, _HeadParamsJson, _GuideNamesJson]

class HeadModule(
    Mod.Module[
        _HeadOptionsJson,
        _HeadParamsJson,
        _GuideNamesJson,
        ModuleOptionsWidget,
        ModuleParamsWidget,
        HeadGuide,
        _HeadControls | None,
        None,
        None,
    ]
):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _ModuleJsonWithNode[_HeadOptionsJson, _HeadParamsJson, _GuideNamesJson]
    autorigs_asset: AutoRigsAsset
    mastermodule: MasterModule
    spinemodules: Sequence[SpineModule]
    guidetab: "HeadGuideTab"
    autorigsbuilder: AutoRigsHeadBuilder
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _HeadModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _HeadModuleJson) -> None: ...
    def getModuleHooks(self) -> list[hou.ObjNode | None]: ...
    def buildRig(self, orig_asset: AutoRigsAsset, index: int) -> None: ...
    def getMainHook(self) -> hou.ObjNode: ...
    def getHeadBone(self) -> hou.ObjNode: ...

class HeadGuideTab(
    Mod.ModuleGuideTab[
        _HeadOptionsJson, _HeadParamsJson, _GuideNamesJson, ModuleOptionsWidget, ModuleParamsWidget, HeadGuide
    ]
):
    PREFIX: str
    tabswidget: ModuleTabsWidget
    def __init__(self, buildguides: HeadGuide, spinemodules: Sequence[SpineModule], mastermodule: MasterModule) -> None: ...
    def updateParent(self, spinemodules: Sequence[SpineModule]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | SpineModule, hou.ObjNode]: ...
