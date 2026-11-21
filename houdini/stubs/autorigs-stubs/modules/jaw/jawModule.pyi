# Houdini stubs generated from Houdini 22.0.466

import hou
from . import buildJawGuide as buildJawGuide, jawGuideOptions as jawGuideOptions, jawGuideParams as jawGuideParams
from _typeshed import Incomplete
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base import rootModule as Mod
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.jaw.autoRigsJawBuilder import AutoRigsJawBuilder as AutoRigsJawBuilder
from autorigs.modules.jaw.buildJawGuide import JawGuide as JawGuide
from autorigs.modules.jaw.jawGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget, _JawOptionsJson
from autorigs.modules.jaw.jawGuideParams import ModuleParamsWidget as ModuleParamsWidget
from autorigs.ui import moduleTabsWidget as moduleTabsWidget
from autorigs.ui.moduleTabsWidget import ModuleTabsWidget as ModuleTabsWidget
from autorigs.utils.guideParamsHelper import _ParamsJson

from typing import TypeAlias
from autorigs.modules.base.rootModule import _ModuleJson
from typing import TypeAlias
_JawModuleJson: TypeAlias = _ModuleJson[_JawOptionsJson, _ParamsJson, _GuideNamesJson]
class JawModule(Mod.Module[_JawOptionsJson, _ParamsJson, _GuideNamesJson, ModuleOptionsWidget, ModuleParamsWidget, JawGuide, None, None, None]):
    assetnode: hou.ObjNode
    guidetab: JawGuideTab
    autorigsbuilder: AutoRigsJawBuilder
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _JawModuleJson
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    buildguides: Incomplete
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _JawModuleJson, is_submodule: bool = False) -> None: ...
    def buildFromJsonExisting(self, json: _JawModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class JawGuideTab(Mod.ModuleGuideTab[_JawOptionsJson, _ParamsJson, _GuideNamesJson, ModuleOptionsWidget, ModuleParamsWidget, JawGuide]):
    tabswidget: ModuleTabsWidget
    buildguides: Incomplete
    optionswidget: Incomplete
    paramswidget: Incomplete
    def __init__(self, buildguides: JawGuide) -> None: ...
