from typing import TypeAlias

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.advancedFace.eye.autoRigsEyeBuilder import AutoRigsEyeBuilder
from autorigs.modules.advancedFace.eye.buildEyeGuide import EyeGuide, _EyeGuideJson
from autorigs.modules.advancedFace.eye.eyeGuideOptions import ModuleOptionsWidget, _EyeOptionsJson
from autorigs.modules.advancedFace.eye.eyeGuideParams import ModuleParamsWidget
from autorigs.modules.base import rootModule as Mod
from autorigs.ui.moduleTabsWidget import ModuleTabsWidget
from autorigs.utils.guideParamsHelper import _ParamsJson
from autorigs.modules.base.rootModule import _ModuleJson

_EyeModuleJson: TypeAlias = _ModuleJson[_EyeOptionsJson, _ParamsJson, _EyeGuideJson]

# The standalone eye module never sets a model or controller.
class EyeModule(
    Mod.Module[
        _EyeOptionsJson,
        _ParamsJson,
        _EyeGuideJson,
        ModuleOptionsWidget,
        ModuleParamsWidget,
        EyeGuide,
        None,
        None,
        None,
        "EyeGuideTab",
    ]
):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _EyeModuleJson
    assetnode: hou.ObjNode
    guidetab: "EyeGuideTab | None"
    autorigsbuilder: AutoRigsEyeBuilder

    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _EyeModuleJson, is_submodule: bool = ...) -> None: ...
    def buildFromJsonExisting(self, json: _EyeModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class EyeGuideTab(
    Mod.ModuleGuideTab[
        _EyeOptionsJson, _ParamsJson, _EyeGuideJson, ModuleOptionsWidget, ModuleParamsWidget, EyeGuide, ModuleTabsWidget
    ]
):
    tabswidget: ModuleTabsWidget

    def __init__(self, buildguides: EyeGuide) -> None: ...
