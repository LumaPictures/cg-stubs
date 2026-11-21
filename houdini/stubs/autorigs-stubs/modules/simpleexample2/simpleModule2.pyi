# Houdini stubs generated from Houdini 22.0.466

from . import buildSimpleGuide as buildSimpleGuide, simpleGuideOptions as simpleGuideOptions, simpleGuideParams as simpleGuideParams
from _typeshed import Incomplete
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base import rootModule as Mod
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.simpleexample2.buildSimpleGuide import SimpleGuide as SimpleGuide
from autorigs.modules.simpleexample2.simpleGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget, _SimpleOptionsJson
from autorigs.modules.simpleexample2.simpleGuideParams import ModuleParamsWidget as ModuleParamsWidget, _SimpleParamsJson
from autorigs.ui import moduleTabsWidget as moduleTabsWidget
from autorigs.ui.moduleTabsWidget import ModuleTabsWidget as ModuleTabsWidget
from collections.abc import Mapping, Sequence

from typing import TypeAlias
from autorigs.modules.base.rootModule import _ModuleJson
from typing import TypeAlias
_SimpleModuleJson: TypeAlias = _ModuleJson[_SimpleOptionsJson, _SimpleParamsJson, _GuideNamesJson]
class SimpleModule2(Mod.Module[_SimpleOptionsJson, _SimpleParamsJson, _GuideNamesJson, ModuleOptionsWidget, ModuleParamsWidget, SimpleGuide, None, None, None]):
    autorigs_asset: AutoRigsAsset
    guidetab: SimpleGuideTab
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _SimpleModuleJson
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    buildguides: Incomplete
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _SimpleModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _SimpleModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class SimpleGuideTab(Mod.ModuleGuideTab[_SimpleOptionsJson, _SimpleParamsJson, _GuideNamesJson, ModuleOptionsWidget, ModuleParamsWidget, SimpleGuide]):
    tabswidget: ModuleTabsWidget
    buildguides: Incomplete
    optionswidget: Incomplete
    paramswidget: Incomplete
    def __init__(self, modulesdict: Mapping[str, Sequence[Mod.Module]], buildguides: SimpleGuide) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
