import hou
from . import advancedFaceGuideOptions as advancedFaceGuideOptions, advancedFaceGuideParams as advancedFaceGuideParams, buildAdvancedFaceGuide as buildAdvancedFaceGuide
from .advancedFaceGuideController import AdvancedFaceGuideController as AdvancedFaceGuideController
from .advancedFaceGuideModel import AdvancedFaceGuideModel as AdvancedFaceGuideModel
from _typeshed import Incomplete
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.advancedFace.advancedFaceGuideOptions import _AdvancedFaceOptionsJson
from autorigs.modules.advancedFace.autoRigsAdvancedFaceBuilder import AutoRigsAdvancedFaceBuilder as AutoRigsAdvancedFaceBuilder
from autorigs.modules.advancedFace.buildAdvancedFaceGuide import AdvancedFaceGuide as AdvancedFaceGuide, _AdvancedFaceGuideJson
from autorigs.modules.base import rootModule as Mod
from autorigs.ui import moduleTabsWidget as moduleTabsWidget
from autorigs.utils.guideParamsHelper import _ParamsJson
from collections.abc import Mapping, Sequence

from typing import TypeAlias
from autorigs.modules.base.rootModule import _ModuleJson
from typing import TypeAlias
_AdvancedFaceModuleJson: TypeAlias = _ModuleJson[_AdvancedFaceOptionsJson, _ParamsJson, _AdvancedFaceGuideJson]
class AdvancedFaceModule(Mod.Module[_AdvancedFaceOptionsJson, _ParamsJson, _AdvancedFaceGuideJson, advancedFaceGuideOptions.ModuleOptionsWidget, advancedFaceGuideParams.ModuleParamsWidget, AdvancedFaceGuide, None, AdvancedFaceGuideModel, AdvancedFaceGuideController]):
    autorigs_asset: AutoRigsAsset
    assetnode: hou.ObjNode
    guidetab: AdvancedFaceGuideTab
    autorigsbuilder: AutoRigsAdvancedFaceBuilder
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _AdvancedFaceModuleJson
    model: Incomplete
    controller: Incomplete
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    buildguides: Incomplete
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _AdvancedFaceModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _AdvancedFaceModuleJson) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def buildRig(self, index: int) -> None: ...

class AdvancedFaceGuideTab(Mod.ModuleGuideTab[_AdvancedFaceOptionsJson, _ParamsJson, _AdvancedFaceGuideJson, advancedFaceGuideOptions.ModuleOptionsWidget, advancedFaceGuideParams.ModuleParamsWidget, AdvancedFaceGuide]):
    tabswidget: moduleTabsWidget.ModuleTabsWidget
    optionswidget: Incomplete
    paramswidget: Incomplete
    buildguides: Incomplete
    def __init__(self, buildguides: AdvancedFaceGuide, modulesdict: Mapping[str, Sequence[Mod.Module]], model: AdvancedFaceGuideModel, controller: AdvancedFaceGuideController) -> None: ...
    def setTab(self, index: int) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[Mod.Module, hou.ObjNode]: ...
