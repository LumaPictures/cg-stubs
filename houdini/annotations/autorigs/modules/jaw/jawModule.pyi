from typing import TypeAlias

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base import rootModule as Mod
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.jaw.autoRigsJawBuilder import AutoRigsJawBuilder
from autorigs.modules.jaw.buildJawGuide import JawGuide
from autorigs.modules.jaw.jawGuideOptions import ModuleOptionsWidget, _JawOptionsJson
from autorigs.modules.jaw.jawGuideParams import ModuleParamsWidget
from autorigs.ui.moduleTabsWidget import ModuleTabsWidget
from autorigs.utils.guideParamsHelper import _ParamsJson
from autorigs.modules.base.rootModule import _ModuleJson

_JawModuleJson: TypeAlias = _ModuleJson[_JawOptionsJson, _ParamsJson, _GuideNamesJson]

# The standalone jaw module never sets a model or controller.
class JawModule(
    Mod.Module[
        _JawOptionsJson,
        _ParamsJson,
        _GuideNamesJson,
        ModuleOptionsWidget,
        ModuleParamsWidget,
        JawGuide,
        None,
        None,
        None,
        "JawGuideTab",
    ]
):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _JawModuleJson
    assetnode: hou.ObjNode
    guidetab: "JawGuideTab | None"
    autorigsbuilder: AutoRigsJawBuilder
    buildguides: JawGuide
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _JawModuleJson, is_submodule: bool = ...) -> None: ...
    def buildFromJsonExisting(self, json: _JawModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class JawGuideTab(
    Mod.ModuleGuideTab[
        _JawOptionsJson, _ParamsJson, _GuideNamesJson, ModuleOptionsWidget, ModuleParamsWidget, JawGuide, ModuleTabsWidget
    ]
):
    tabswidget: ModuleTabsWidget
    buildguides: JawGuide
    optionswidget: ModuleOptionsWidget
    paramswidget: ModuleParamsWidget
    def __init__(self, buildguides: JawGuide) -> None: ...
