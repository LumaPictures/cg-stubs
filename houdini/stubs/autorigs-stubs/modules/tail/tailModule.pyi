# Houdini stubs generated from Houdini 22.0.466

import hou
from . import buildTailGuide as buildTailGuide, tailGuideOptions as tailGuideOptions, tailGuideParams as tailGuideParams
from _typeshed import Incomplete
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base import moduleTabsWidget as moduleTabsWidget, rootModule as Mod, rootModule as rootModule
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from autorigs.modules.tail.autoRigsTailBuilder import AutoRigsTailBuilder as AutoRigsTailBuilder
from autorigs.modules.tail.buildTailGuide import TailGuide as TailGuide
from autorigs.modules.tail.tailGuideOptions import ModuleOptions as ModuleOptions
from autorigs.modules.tail.tailGuideParams import ModuleParams as ModuleParams
from collections.abc import Iterable, Mapping, Sequence

from typing import TypeAlias
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.base.rootModule import _ModuleJson
from autorigs.modules.tail.tailGuideOptions import _TailOptionsJson
from autorigs.modules.tail.tailGuideParams import _TailParamsJson
from typing import TypeAlias
_TailModuleJson: TypeAlias = _ModuleJson[_TailOptionsJson, _TailParamsJson, _GuideNamesJson]
class TailModule(Mod.Module):
    autorig_asset: AutoRigsAsset
    mastermodule: MasterModule
    spinemodules: list[SpineModule]
    guidetab: TailGuideTab
    autorigsbuilder: AutoRigsTailBuilder
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _TailModuleJson
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[rootModule.Module]]) -> None: ...
    buildguides: Incomplete
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _TailModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _TailModuleJson) -> None: ...
    builtrig: Incomplete
    def buildRig(self, index: int) -> None: ...

class TailGuideTab(Mod.ModuleGuideTab):
    tabswidget: moduleTabsWidget.ModuleTabsWidget
    PREFIX: str
    buildguides: Incomplete
    optionswidget: Incomplete
    paramswidget: Incomplete
    def __init__(self, buildguides: TailGuide, spinemodules: Iterable[SpineModule], mastermodule: MasterModule) -> None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | SpineModule, hou.ObjNode]: ...
    def updateParent(self, spinemodules: Iterable[SpineModule]) -> None: ...
