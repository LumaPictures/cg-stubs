# Houdini stubs generated from Houdini 22.0.466

import hou
from . import basicFaceGuideOptions as basicFaceGuideOptions, basicFaceGuideParams as basicFaceGuideParams, buildBasicFaceGuide as buildBasicFaceGuide
from .basicFaceGuideController import BasicFaceGuideController as BasicFaceGuideController
from .basicFaceGuideModel import BasicFaceGuideModel as BasicFaceGuideModel
from _typeshed import Incomplete
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base import rootModule as Mod
from autorigs.modules.basicFace.autoRigsBasicFaceBuilder import AutoRigsBasicFaceBuilder as AutoRigsBasicFaceBuilder
from autorigs.modules.basicFace.basicFaceGuideOptions import _BasicFaceOptionsJson
from autorigs.modules.basicFace.buildBasicFaceGuide import BasicFaceGuide as BasicFaceGuide, _BasicFaceGuideJson
from autorigs.modules.jaw.jawModule import JawModule as JawModule
from autorigs.ui import moduleTabsWidget as moduleTabsWidget
from autorigs.utils.guideParamsHelper import _ParamsJson
from collections.abc import Mapping, Sequence

from typing import TypeAlias
from autorigs.modules.base.rootModule import _ModuleJson
from typing import TypeAlias
_BasicFaceModuleJson: TypeAlias = _ModuleJson[_BasicFaceOptionsJson, _ParamsJson, _BasicFaceGuideJson]
class BasicFaceModule(Mod.Module[_BasicFaceOptionsJson, _ParamsJson, _BasicFaceGuideJson, basicFaceGuideOptions.ModuleOptionsWidget, basicFaceGuideParams.ModuleParamsWidget, BasicFaceGuide, None, BasicFaceGuideModel, BasicFaceGuideController]):
    autorigs_asset: AutoRigsAsset
    assetnode: hou.ObjNode
    guidetab: BasicFaceGuideTab
    autorigsbuilder: AutoRigsBasicFaceBuilder
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _BasicFaceModuleJson
    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    model: Incomplete
    controller: Incomplete
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    buildguides: Incomplete
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _BasicFaceModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _BasicFaceModuleJson) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def buildRig(self, index: int) -> None: ...

class BasicFaceGuideTab(Mod.ModuleGuideTab[_BasicFaceOptionsJson, _ParamsJson, _BasicFaceGuideJson, basicFaceGuideOptions.ModuleOptionsWidget, basicFaceGuideParams.ModuleParamsWidget, BasicFaceGuide]):
    tabswidget: moduleTabsWidget.ModuleTabsWidget
    optionswidget: Incomplete
    paramswidget: Incomplete
    buildguides: Incomplete
    def __init__(self, buildguides: BasicFaceGuide, modulesdict: Mapping[str, Sequence[Mod.Module]], model: BasicFaceGuideModel, controller: BasicFaceGuideController) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[Mod.Module, hou.ObjNode]: ...
