from collections.abc import Mapping, Sequence
from typing import TypeAlias

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base import rootModule as Mod
from autorigs.modules.basicFace import basicFaceGuideOptions, basicFaceGuideParams
from autorigs.modules.basicFace.autoRigsBasicFaceBuilder import AutoRigsBasicFaceBuilder
from autorigs.modules.basicFace.basicFaceGuideController import BasicFaceGuideController
from autorigs.modules.basicFace.basicFaceGuideModel import BasicFaceGuideModel
from autorigs.modules.basicFace.basicFaceGuideOptions import _BasicFaceOptionsJson
from autorigs.modules.basicFace.buildBasicFaceGuide import BasicFaceGuide, _BasicFaceGuideJson
from autorigs.ui import moduleTabsWidget
from autorigs.utils.guideParamsHelper import _ParamsJson
from autorigs.modules.base.rootModule import _ModuleJson

_BasicFaceModuleJson: TypeAlias = _ModuleJson[_BasicFaceOptionsJson, _ParamsJson, _BasicFaceGuideJson]

class BasicFaceModule(
    Mod.Module[
        _BasicFaceOptionsJson,
        _ParamsJson,
        _BasicFaceGuideJson,
        basicFaceGuideOptions.ModuleOptionsWidget,
        basicFaceGuideParams.ModuleParamsWidget,
        BasicFaceGuide,
        None,
        BasicFaceGuideModel,
        BasicFaceGuideController,
    ]
):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _BasicFaceModuleJson

    autorigs_asset: AutoRigsAsset
    assetnode: hou.ObjNode
    guidetab: "BasicFaceGuideTab"
    autorigsbuilder: AutoRigsBasicFaceBuilder

    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _BasicFaceModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _BasicFaceModuleJson) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def buildRig(self, index: int) -> None: ...

class BasicFaceGuideTab(
    Mod.ModuleGuideTab[
        _BasicFaceOptionsJson,
        _ParamsJson,
        _BasicFaceGuideJson,
        basicFaceGuideOptions.ModuleOptionsWidget,
        basicFaceGuideParams.ModuleParamsWidget,
        BasicFaceGuide,
    ]
):
    tabswidget: moduleTabsWidget.ModuleTabsWidget

    def __init__(
        self,
        buildguides: BasicFaceGuide,
        modulesdict: Mapping[str, Sequence[Mod.Module]],
        model: BasicFaceGuideModel,
        controller: BasicFaceGuideController,
    ) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[Mod.Module]]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[Mod.Module, hou.ObjNode]: ...
