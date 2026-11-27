from collections.abc import Mapping, Sequence
from typing import TypeAlias

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base import rootModule as Mod
from autorigs.ui import moduleTabsWidget
from autorigs.modules.advancedFace import advancedFaceGuideOptions, advancedFaceGuideParams
from autorigs.modules.advancedFace.advancedFaceGuideController import AdvancedFaceGuideController
from autorigs.modules.advancedFace.advancedFaceGuideModel import AdvancedFaceGuideModel
from autorigs.modules.advancedFace.advancedFaceGuideOptions import _AdvancedFaceOptionsJson
from autorigs.modules.advancedFace.autoRigsAdvancedFaceBuilder import AutoRigsAdvancedFaceBuilder
from autorigs.modules.advancedFace.buildAdvancedFaceGuide import AdvancedFaceGuide, _AdvancedFaceGuideJson
from autorigs.utils.guideParamsHelper import _ParamsJson
from autorigs.modules.base.rootModule import _ModuleJson

_AdvancedFaceModuleJson: TypeAlias = _ModuleJson[_AdvancedFaceOptionsJson, _ParamsJson, _AdvancedFaceGuideJson]

class AdvancedFaceModule(
    Mod.Module[
        _AdvancedFaceOptionsJson,
        _ParamsJson,
        _AdvancedFaceGuideJson,
        advancedFaceGuideOptions.ModuleOptionsWidget,
        advancedFaceGuideParams.ModuleParamsWidget,
        AdvancedFaceGuide,
        None,
        AdvancedFaceGuideModel,
        AdvancedFaceGuideController,
        "AdvancedFaceGuideTab",
        AutoRigsAsset,
    ]
):
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _AdvancedFaceModuleJson
    autorigs_asset: AutoRigsAsset
    assetnode: hou.ObjNode
    guidetab: "AdvancedFaceGuideTab | None"
    autorigsbuilder: AutoRigsAdvancedFaceBuilder
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _AdvancedFaceModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _AdvancedFaceModuleJson) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def buildRig(self, index: int) -> None: ...

class AdvancedFaceGuideTab(
    Mod.ModuleGuideTab[
        _AdvancedFaceOptionsJson,
        _ParamsJson,
        _AdvancedFaceGuideJson,
        advancedFaceGuideOptions.ModuleOptionsWidget,
        advancedFaceGuideParams.ModuleParamsWidget,
        AdvancedFaceGuide,
        moduleTabsWidget.ModuleTabsWidget,
    ]
):
    tabswidget: moduleTabsWidget.ModuleTabsWidget
    def __init__(
        self,
        buildguides: AdvancedFaceGuide,
        modulesdict: Mapping[str, Sequence[Mod.Module]],
        model: AdvancedFaceGuideModel,
        controller: AdvancedFaceGuideController,
    ) -> None: ...
    def setTab(self, index: int) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[Mod.Module, hou.ObjNode]: ...
