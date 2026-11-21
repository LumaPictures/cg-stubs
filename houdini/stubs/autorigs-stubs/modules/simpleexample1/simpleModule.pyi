# Houdini stubs generated from Houdini 22.0.466

import hou
from . import buildSimpleGuide as buildSimpleGuide, simpleGuideOptions as simpleGuideOptions, simpleGuideParams as simpleGuideParams
from _typeshed import Incomplete
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base import moduleTabsWidget as moduleTabsWidget, rootModule as Mod
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.simpleexample1.simpleGuideOptions import _SimpleOptionsJson
from autorigs.modules.simpleexample1.simpleGuideParams import _SimpleParamsJson

from typing import TypeAlias
from autorigs.modules.base.rootModule import _ModuleJson
from typing import TypeAlias
_SimpleModuleJson: TypeAlias = _ModuleJson[_SimpleOptionsJson, _SimpleParamsJson, _GuideNamesJson]
class SimpleModule(Mod.Module[_SimpleOptionsJson, _SimpleParamsJson, _GuideNamesJson, simpleGuideOptions.ModuleOptionsWidget, simpleGuideParams.ModuleParamsWidget, buildSimpleGuide.SimpleGuide, None, None, None]):
    assetnode: hou.ObjNode
    guidetab: SimpleGuideTab
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _SimpleModuleJson
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    buildguides: Incomplete
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _SimpleModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _SimpleModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class SimpleGuideTab(Mod.ModuleGuideTab[_SimpleOptionsJson, _SimpleParamsJson, _GuideNamesJson, simpleGuideOptions.ModuleOptionsWidget, simpleGuideParams.ModuleParamsWidget, buildSimpleGuide.SimpleGuide]):
    tabswidget: moduleTabsWidget.ModuleTabsWidget
    optionswidget: Incomplete
    paramswidget: Incomplete
    buildguides: Incomplete
    def __init__(self, buildguides: buildSimpleGuide.SimpleGuide) -> None:
        """ The widget for the options tab """
