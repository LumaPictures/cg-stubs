# Houdini stubs generated from Houdini 22.0.466

from . import buildSimpleGuide as buildSimpleGuide, simpleGuideController as simpleGuideController, simpleGuideModel as simpleGuideModel, simpleGuideOptions as simpleGuideOptions, simpleGuideParams as simpleGuideParams
from _typeshed import Incomplete
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base import rootModule as Mod
from autorigs.modules.simpleexample4.buildSimpleGuide import SimpleGuide as SimpleGuide, _SimpleGuideJson
from autorigs.modules.simpleexample4.simpleGuideController import SimpleController as SimpleController
from autorigs.modules.simpleexample4.simpleGuideModel import SimpleModel as SimpleModel
from autorigs.modules.simpleexample4.simpleGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget, _SimpleOptionsJson
from autorigs.modules.simpleexample4.simpleGuideParams import ModuleParamsWidget as ModuleParamsWidget, _SimpleParamsJson
from autorigs.ui import moduleTabsWidget as moduleTabsWidget
from autorigs.ui.moduleTabsWidget import ModuleTabsWidget as ModuleTabsWidget
from collections.abc import Mapping, Sequence

from typing import TypeAlias
from autorigs.modules.base.rootModule import _ModuleJson
from typing import TypeAlias
_SimpleModuleJson: TypeAlias = _ModuleJson[_SimpleOptionsJson, _SimpleParamsJson, _SimpleGuideJson]
class SimpleModule4(Mod.Module[_SimpleOptionsJson, _SimpleParamsJson, _SimpleGuideJson, ModuleOptionsWidget, ModuleParamsWidget, SimpleGuide, None, SimpleModel, SimpleController]):
    autorigs_asset: AutoRigsAsset
    guidetab: SimpleGuideTab
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _SimpleModuleJson
    model: Incomplete
    controller: Incomplete
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    buildguides: Incomplete
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _SimpleModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _SimpleModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class SimpleGuideTab(Mod.ModuleGuideTab[_SimpleOptionsJson, _SimpleParamsJson, _SimpleGuideJson, ModuleOptionsWidget, ModuleParamsWidget, SimpleGuide]):
    tabswidget: ModuleTabsWidget
    buildguides: Incomplete
    optionswidget: Incomplete
    paramswidget: Incomplete
    def __init__(self, modulesdict: Mapping[str, Sequence[Mod.Module]], buildguides: SimpleGuide, controller: SimpleController, model: SimpleModel) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
