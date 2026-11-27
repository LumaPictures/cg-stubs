from collections.abc import Mapping, Sequence
from typing import TypeAlias

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base import rootModule as Mod
from autorigs.modules.simpleexample4.buildSimpleGuide import SimpleGuide, _SimpleGuideJson
from autorigs.modules.simpleexample4.simpleGuideController import SimpleController
from autorigs.modules.simpleexample4.simpleGuideModel import SimpleModel
from autorigs.modules.simpleexample4.simpleGuideOptions import ModuleOptionsWidget, _SimpleOptionsJson
from autorigs.modules.simpleexample4.simpleGuideParams import ModuleParamsWidget, _SimpleParamsJson
from autorigs.ui.moduleTabsWidget import ModuleTabsWidget
from autorigs.modules.base.rootModule import _ModuleJson

_SimpleModuleJson: TypeAlias = _ModuleJson[_SimpleOptionsJson, _SimpleParamsJson, _SimpleGuideJson]

class SimpleModule4(
    Mod.Module[
        _SimpleOptionsJson,
        _SimpleParamsJson,
        _SimpleGuideJson,
        ModuleOptionsWidget,
        ModuleParamsWidget,
        SimpleGuide,
        None,
        SimpleModel,
        SimpleController,
        "SimpleGuideTab",
        AutoRigsAsset,
    ]
):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _SimpleModuleJson
    autorigs_asset: AutoRigsAsset
    guidetab: "SimpleGuideTab | None"
    model: SimpleModel
    controller: SimpleController
    buildguides: SimpleGuide
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _SimpleModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _SimpleModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class SimpleGuideTab(
    Mod.ModuleGuideTab[
        _SimpleOptionsJson, _SimpleParamsJson, _SimpleGuideJson, ModuleOptionsWidget, ModuleParamsWidget, SimpleGuide, ModuleTabsWidget
    ]
):
    tabswidget: ModuleTabsWidget
    buildguides: SimpleGuide
    optionswidget: ModuleOptionsWidget
    paramswidget: ModuleParamsWidget
    def __init__(
        self,
        modulesdict: Mapping[str, Sequence[Mod.Module]],
        buildguides: SimpleGuide,
        controller: SimpleController,
        model: SimpleModel,
    ) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
