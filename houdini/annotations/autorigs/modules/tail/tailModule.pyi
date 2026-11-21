from collections.abc import Iterable, Mapping, Sequence
from typing import TypeAlias

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base import moduleTabsWidget, rootModule
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.spineModule import SpineModule
from autorigs.modules.tail.autoRigsTailBuilder import AutoRigsTailBuilder
from autorigs.modules.tail.buildTailGuide import TailGuide
from autorigs.modules.tail.tailGuideOptions import ModuleOptions, _TailOptionsJson
from autorigs.modules.tail.tailGuideParams import ModuleParams, _TailParamsJson
from autorigs.modules.base.rootModule import _ModuleJson

_TailModuleJson: TypeAlias = _ModuleJson[_TailOptionsJson, _TailParamsJson, _GuideNamesJson]

class TailModule(
    rootModule.Module[
        _TailOptionsJson,
        _TailParamsJson,
        _GuideNamesJson,
        ModuleOptions,
        ModuleParams,
        TailGuide,
        dict[str, hou.OpNode | hou.NodeGroup] | None,
        None,
        None,
    ]
):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _TailModuleJson
    autorig_asset: AutoRigsAsset
    mastermodule: MasterModule
    spinemodules: list[SpineModule]
    guidetab: "TailGuideTab"
    autorigsbuilder: AutoRigsTailBuilder

    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[rootModule.Module]]) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _TailModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _TailModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class TailGuideTab(
    rootModule.ModuleGuideTab[_TailOptionsJson, _TailParamsJson, _GuideNamesJson, ModuleOptions, ModuleParams, TailGuide]
):
    PREFIX: str
    tabswidget: moduleTabsWidget.ModuleTabsWidget

    def __init__(self, buildguides: TailGuide, spinemodules: Iterable[SpineModule], mastermodule: MasterModule) -> None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | SpineModule, hou.ObjNode]: ...
    def updateParent(self, spinemodules: Iterable[SpineModule]) -> None: ...
