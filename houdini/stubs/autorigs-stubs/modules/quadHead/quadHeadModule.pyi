# Houdini stubs generated from Houdini 22.0.466

import hou
from . import buildQuadHeadGuide as buildQuadHeadGuide, quadHeadGuideOptions as quadHeadGuideOptions, quadHeadGuideParams as quadHeadGuideParams
from _typeshed import Incomplete
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base import moduleTabsWidget as moduleTabsWidget, rootModule as Mod
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.quadHead.autoRigsQuadHeadBuilder import AutoRigsQuadHeadBuilder as AutoRigsQuadHeadBuilder, _QuadHeadControls
from autorigs.modules.quadHead.quadHeadGuideOptions import _QuadHeadOptionsJson
from autorigs.modules.quadHead.quadHeadGuideParams import _QuadHeadParamsJson
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from collections.abc import Iterable, Mapping, Sequence

from typing import TypeAlias
from autorigs.modules.base.rootModule import _ModuleJson
from typing import TypeAlias
_QuadHeadModuleJson: TypeAlias = _ModuleJson[_QuadHeadOptionsJson, _QuadHeadParamsJson, _GuideNamesJson]
class QuadHeadModule(Mod.Module[_QuadHeadOptionsJson, _QuadHeadParamsJson, _GuideNamesJson, quadHeadGuideOptions.ModuleOptionsWidget, quadHeadGuideParams.ModuleParamsWidget, buildQuadHeadGuide.QuadHeadGuide, _QuadHeadControls | None, None, None]):
    mastermodule: MasterModule
    spinemodules: Sequence[SpineModule]
    autorig_asset: AutoRigsAsset
    guidetab: QuadHeadGuideTab
    autorigsbuilder: AutoRigsQuadHeadBuilder
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _QuadHeadModuleJson
    def __init__(self, autorig_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    buildguides: Incomplete
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _QuadHeadModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _QuadHeadModuleJson) -> None: ...
    builtrig: Incomplete
    def buildRig(self, index: int) -> None: ...

class QuadHeadGuideTab(Mod.ModuleGuideTab[_QuadHeadOptionsJson, _QuadHeadParamsJson, _GuideNamesJson, quadHeadGuideOptions.ModuleOptionsWidget, quadHeadGuideParams.ModuleParamsWidget, buildQuadHeadGuide.QuadHeadGuide]):
    tabswidget: moduleTabsWidget.ModuleTabsWidget
    PREFIX: str
    buildguides: Incomplete
    optionswidget: Incomplete
    paramswidget: Incomplete
    def __init__(self, buildguides: buildQuadHeadGuide.QuadHeadGuide, spinemodules: Iterable[SpineModule], mastermodule: MasterModule) -> None: ...
    def updateParent(self, spinemodules: Iterable[SpineModule]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | SpineModule, hou.ObjNode]: ...
