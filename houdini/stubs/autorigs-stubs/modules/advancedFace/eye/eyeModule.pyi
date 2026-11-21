import hou
from . import buildEyeGuide as buildEyeGuide, eyeGuideOptions as eyeGuideOptions, eyeGuideParams as eyeGuideParams
from _typeshed import Incomplete
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.advancedFace.eye.autoRigsEyeBuilder import AutoRigsEyeBuilder as AutoRigsEyeBuilder
from autorigs.modules.advancedFace.eye.buildEyeGuide import EyeGuide as EyeGuide, _EyeGuideJson
from autorigs.modules.advancedFace.eye.eyeGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget, _EyeOptionsJson
from autorigs.modules.advancedFace.eye.eyeGuideParams import ModuleParamsWidget as ModuleParamsWidget
from autorigs.modules.base import rootModule as Mod
from autorigs.ui import moduleTabsWidget as moduleTabsWidget
from autorigs.ui.moduleTabsWidget import ModuleTabsWidget as ModuleTabsWidget
from autorigs.utils.guideParamsHelper import _ParamsJson

from typing import TypeAlias
from autorigs.modules.base.rootModule import _ModuleJson
from typing import TypeAlias
_EyeModuleJson: TypeAlias = _ModuleJson[_EyeOptionsJson, _ParamsJson, _EyeGuideJson]
class EyeModule(Mod.Module[_EyeOptionsJson, _ParamsJson, _EyeGuideJson, ModuleOptionsWidget, ModuleParamsWidget, EyeGuide, None, None, None]):
    assetnode: hou.ObjNode
    guidetab: EyeGuideTab
    autorigsbuilder: AutoRigsEyeBuilder
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _EyeModuleJson
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    buildguides: Incomplete
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _EyeModuleJson, is_submodule: bool = False) -> None: ...
    def buildFromJsonExisting(self, json: _EyeModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...

class EyeGuideTab(Mod.ModuleGuideTab[_EyeOptionsJson, _ParamsJson, _EyeGuideJson, ModuleOptionsWidget, ModuleParamsWidget, EyeGuide]):
    tabswidget: ModuleTabsWidget
    buildguides: Incomplete
    optionswidget: Incomplete
    paramswidget: Incomplete
    def __init__(self, buildguides: EyeGuide) -> None: ...
