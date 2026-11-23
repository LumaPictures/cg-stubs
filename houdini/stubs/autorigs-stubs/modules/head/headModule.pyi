import hou
from . import buildHeadGuide as buildHeadGuide, headGuideOptions as headGuideOptions, headGuideParams as headGuideParams
from _typeshed import Incomplete
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base import moduleTabsWidget as moduleTabsWidget, rootModule as Mod
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.base.moduleTabsWidget import ModuleTabsWidget as ModuleTabsWidget
from autorigs.modules.base.rootModule import _ModuleJsonWithNode
from autorigs.modules.head.autoRigsHeadBuilder import AutoRigsHeadBuilder as AutoRigsHeadBuilder
from autorigs.modules.head.autoRigsHeadInterfaceBuilder import _HeadControls
from autorigs.modules.head.buildHeadGuide import HeadGuide as HeadGuide
from autorigs.modules.head.headGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget, _HeadOptionsJson
from autorigs.modules.head.headGuideParams import ModuleParamsWidget as ModuleParamsWidget, _HeadParamsJson
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from collections.abc import Mapping, Sequence

from typing import TypeAlias
from autorigs.modules.base.rootModule import _ModuleJson
from typing import TypeAlias
_HeadModuleJson: TypeAlias = _ModuleJson[_HeadOptionsJson, _HeadParamsJson, _GuideNamesJson]
class HeadModule(Mod.Module[_HeadOptionsJson, _HeadParamsJson, _GuideNamesJson, ModuleOptionsWidget, ModuleParamsWidget, HeadGuide, _HeadControls | None, None, None]):
    autorigs_asset: AutoRigsAsset
    mastermodule: MasterModule
    spinemodules: Sequence[SpineModule]
    guidetab: HeadGuideTab
    autorigsbuilder: AutoRigsHeadBuilder
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _ModuleJsonWithNode[_HeadOptionsJson, _HeadParamsJson, _GuideNamesJson]
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    buildguides: Incomplete
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _HeadModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _HeadModuleJson) -> None: ...
    def getModuleHooks(self) -> list[hou.ObjNode | None]: ...
    builtrig: Incomplete
    def buildRig(self, orig_asset: AutoRigsAsset, index: int) -> None: ...
    def getMainHook(self) -> hou.ObjNode: ...
    def getHeadBone(self) -> hou.ObjNode: ...

class HeadGuideTab(Mod.ModuleGuideTab[_HeadOptionsJson, _HeadParamsJson, _GuideNamesJson, ModuleOptionsWidget, ModuleParamsWidget, HeadGuide]):
    tabswidget: ModuleTabsWidget
    PREFIX: str
    buildguides: Incomplete
    optionswidget: Incomplete
    paramswidget: Incomplete
    def __init__(self, buildguides: HeadGuide, spinemodules: Sequence[SpineModule], mastermodule: MasterModule) -> None: ...
    def updateParent(self, spinemodules: Sequence[SpineModule]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | SpineModule, hou.ObjNode]: ...
