from collections.abc import Iterable, Mapping, Sequence
from typing import TypeAlias

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base import moduleTabsWidget, rootModule as Mod
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.quadHead import buildQuadHeadGuide, quadHeadGuideOptions, quadHeadGuideParams
from autorigs.modules.quadHead.autoRigsQuadHeadBuilder import AutoRigsQuadHeadBuilder, _QuadHeadControls
from autorigs.modules.quadHead.quadHeadGuideOptions import _QuadHeadOptionsJson
from autorigs.modules.quadHead.quadHeadGuideParams import _QuadHeadParamsJson
from autorigs.modules.spine.spineModule import SpineModule
from autorigs.modules.base.rootModule import _ModuleJson

_QuadHeadModuleJson: TypeAlias = _ModuleJson[_QuadHeadOptionsJson, _QuadHeadParamsJson, _GuideNamesJson]

class QuadHeadModule(
    Mod.Module[
        _QuadHeadOptionsJson,
        _QuadHeadParamsJson,
        _GuideNamesJson,
        quadHeadGuideOptions.ModuleOptionsWidget,
        quadHeadGuideParams.ModuleParamsWidget,
        buildQuadHeadGuide.QuadHeadGuide,
        _QuadHeadControls | None,
        None,
        None,
        "QuadHeadGuideTab",
        AutoRigsAsset | None,
    ]
):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _QuadHeadModuleJson
    mastermodule: MasterModule
    spinemodules: Sequence[SpineModule]
    autorig_asset: AutoRigsAsset
    guidetab: "QuadHeadGuideTab | None"
    autorigsbuilder: AutoRigsQuadHeadBuilder
    buildguides: buildQuadHeadGuide.QuadHeadGuide
    builtrig: _QuadHeadControls | None
    def __init__(self, autorig_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _QuadHeadModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _QuadHeadModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class QuadHeadGuideTab(
    Mod.ModuleGuideTab[
        _QuadHeadOptionsJson,
        _QuadHeadParamsJson,
        _GuideNamesJson,
        quadHeadGuideOptions.ModuleOptionsWidget,
        quadHeadGuideParams.ModuleParamsWidget,
        buildQuadHeadGuide.QuadHeadGuide,
        moduleTabsWidget.ModuleTabsWidget,
    ]
):
    PREFIX: str
    tabswidget: moduleTabsWidget.ModuleTabsWidget
    buildguides: buildQuadHeadGuide.QuadHeadGuide
    optionswidget: quadHeadGuideOptions.ModuleOptionsWidget
    paramswidget: quadHeadGuideParams.ModuleParamsWidget
    def __init__(
        self,
        buildguides: buildQuadHeadGuide.QuadHeadGuide,
        spinemodules: Iterable[SpineModule],
        mastermodule: MasterModule,
    ) -> None: ...
    def updateParent(self, spinemodules: Iterable[SpineModule]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | SpineModule, hou.ObjNode]: ...
