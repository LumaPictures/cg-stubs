from collections.abc import Sequence
from typing import Any, Generic, Protocol, TypeAlias

from typing_extensions import TypeVar

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base import rootModule as Mod
from autorigs.modules.base.moduleTabsWidget import ModuleTabsWidget
from autorigs.modules.extremity.buildExtremityGuide import ExtremityGuide, _ExtremityGuideJson
from autorigs.modules.extremity.extremityGuideController import ModuleOptionController
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel
from autorigs.modules.extremity.extremityGuideOptions import ModuleOptionsWidget, _ExtremityOptionsJson
from autorigs.modules.extremity.extremityGuideParams import ModuleParamsWidget, _ExtremityParamsJson
from autorigs.modules.foot.buildFootGuide import FootGuide
from autorigs.modules.hand.buildHandGuide import HandGuide
from autorigs.modules.limb.limbModule import LimbModule
from autorigs.modules.quadFoot.buildQuadFootGuide import QuadFootGuide
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.spineModule import SpineModule
from autorigs.modules.base.rootModule import _ModuleJson

_ExtremityModuleJson: TypeAlias = _ModuleJson[_ExtremityOptionsJson, _ExtremityParamsJson, _ExtremityGuideJson]

# The hand, foot and quadfoot modules each have their own widgets and guide; a bare
# ExtremityModule is any of them.
_ExtremityOptions = TypeVar("_ExtremityOptions", bound=ModuleOptionsWidget, default=Any)
_ExtremityParams = TypeVar("_ExtremityParams", bound=ModuleParamsWidget, default=Any)
_ExtremityGuideT = TypeVar("_ExtremityGuideT", bound=HandGuide | FootGuide | QuadFootGuide, default=Any)
_Guide_co = TypeVar("_Guide_co", bound=ExtremityGuide, covariant=True, default=ExtremityGuide)

class _GuidesFactory(Protocol[_Guide_co]):
    def createFromDefault(
        self,
        json: _ExtremityModuleJson,
        assetnode: hou.ObjNode,
        model: ModuleOptionModel,
        parent: hou.ObjNode | None = ...,
    ) -> _Guide_co: ...
    def createFromJsonNew(
        self,
        json: _ExtremityModuleJson,
        assetnode: hou.ObjNode,
        model: ModuleOptionModel,
        parent: hou.ObjNode | None = ...,
    ) -> _Guide_co: ...
    def createFromJsonExisting(
        self,
        json: _ExtremityModuleJson,
        assetnode: hou.ObjNode,
        model: ModuleOptionModel,
        parent: hou.ObjNode | None = ...,
    ) -> _Guide_co: ...

class ExtremityModule(
    Mod.Module[
        _ExtremityOptionsJson,
        _ExtremityParamsJson,
        _ExtremityGuideJson,
        _ExtremityOptions,
        _ExtremityParams,
        _ExtremityGuideT,
        None,
        ModuleOptionModel,
        ModuleOptionController,
    ],
    Generic[_ExtremityOptions, _ExtremityParams, _ExtremityGuideT],
):
    limbmodules: Sequence[LimbModule]
    guidesfactory: _GuidesFactory[_ExtremityGuideT]
    assetnode: hou.ObjNode
    mastermodule: MasterModule
    spinemodules: Sequence[SpineModule]
    def __init__(
        self,
        autorigs_asset: AutoRigsAsset,
        limbmodules: Sequence[LimbModule],
        guidesfactory: _GuidesFactory[_ExtremityGuideT],
    ) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset, arg2: object = ..., arg3: object = ...) -> None: ...
    def buildFromDefault(self, json: _ExtremityModuleJson) -> None: ...
    def buildFromJsonNew(self, json: _ExtremityModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _ExtremityModuleJson) -> None: ...
    def getBUiltObject(self, builtkey: str) -> None: ...
    def getBuiltObjectSide(self, builtkey: str, ismain: bool) -> None: ...
    def getLimbModuleIfExists(self) -> LimbModule | None: ...
    def buildRig(self, index: int) -> None: ...
    def canBeMirrored(self) -> bool: ...

class ExtremityGuideTab(
    Mod.ModuleGuideTab[
        _ExtremityOptionsJson,
        _ExtremityParamsJson,
        _ExtremityGuideJson,
        _ExtremityOptions,
        _ExtremityParams,
        _ExtremityGuideT,
    ],
    Generic[_ExtremityOptions, _ExtremityParams, _ExtremityGuideT],
):
    PREFIX: str
    GUIDE_OPTIONS: type[_ExtremityOptions]
    GUIDE_PARAMS: type[_ExtremityParams]
    tabswidget: ModuleTabsWidget
    def __init__(
        self,
        buildguides: _ExtremityGuideT,
        assetnode: hou.ObjNode,
        mastermodule: MasterModule,
        limbmodules: Sequence[LimbModule],
        spinemodules: Sequence[SpineModule],
        model: ModuleOptionModel,
        controller: ModuleOptionController,
    ) -> None: ...
    def updateParent(self, limbmodules: Sequence[LimbModule], spinemodules: Sequence[SpineModule]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | LimbModule | SpineModule, hou.ObjNode]: ...
