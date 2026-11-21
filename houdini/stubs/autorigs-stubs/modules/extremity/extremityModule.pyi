# Houdini stubs generated from Houdini 22.0.466

import hou
from . import extremityGuideController as extremityGuideController, extremityGuideModel as extremityGuideModel
from _typeshed import Incomplete
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base import moduleTabsWidget as moduleTabsWidget, rootModule as Mod
from autorigs.modules.base.moduleTabsWidget import ModuleTabsWidget as ModuleTabsWidget
from autorigs.modules.extremity.buildExtremityGuide import ExtremityGuide as ExtremityGuide, _ExtremityGuideJson
from autorigs.modules.extremity.extremityGuideController import ModuleOptionController as ModuleOptionController
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel as ModuleOptionModel
from autorigs.modules.extremity.extremityGuideOptions import ModuleOptionsWidget as ModuleOptionsWidget, _ExtremityOptionsJson
from autorigs.modules.extremity.extremityGuideParams import ModuleParamsWidget as ModuleParamsWidget, _ExtremityParamsJson
from autorigs.modules.foot.buildFootGuide import FootGuide as FootGuide
from autorigs.modules.hand.buildHandGuide import HandGuide as HandGuide
from autorigs.modules.limb.limbModule import LimbModule as LimbModule
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.quadFoot.buildQuadFootGuide import QuadFootGuide as QuadFootGuide
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from collections.abc import Sequence
from typing import Generic, Protocol

from typing import TypeAlias
from typing import TypeVar
from autorigs.modules.base.rootModule import _ModuleJson
from typing import Any
from typing import TypeAlias
from typing_extensions import TypeVar
_ExtremityModuleJson: TypeAlias = _ModuleJson[_ExtremityOptionsJson, _ExtremityParamsJson, _ExtremityGuideJson]
_ExtremityOptions = TypeVar('_ExtremityOptions', bound=ModuleOptionsWidget, default=Any)
_ExtremityParams = TypeVar('_ExtremityParams', bound=ModuleParamsWidget, default=Any)
_ExtremityGuideT = TypeVar('_ExtremityGuideT', bound=HandGuide | FootGuide | QuadFootGuide, default=Any)
_Guide_co = TypeVar('_Guide_co', bound=ExtremityGuide, covariant=True, default=ExtremityGuide)
class _GuidesFactory(Protocol[_Guide_co]):
    def createFromDefault(self, json: _ExtremityModuleJson, assetnode: hou.ObjNode, model: ModuleOptionModel, parent: hou.ObjNode | None = ...) -> _Guide_co: ...
    def createFromJsonNew(self, json: _ExtremityModuleJson, assetnode: hou.ObjNode, model: ModuleOptionModel, parent: hou.ObjNode | None = ...) -> _Guide_co: ...
    def createFromJsonExisting(self, json: _ExtremityModuleJson, assetnode: hou.ObjNode, model: ModuleOptionModel, parent: hou.ObjNode | None = ...) -> _Guide_co: ...

class ExtremityModule(Mod.Module[_ExtremityOptionsJson, _ExtremityParamsJson, _ExtremityGuideJson, _ExtremityOptions, _ExtremityParams, _ExtremityGuideT, None, ModuleOptionModel, ModuleOptionController], Generic[_ExtremityOptions, _ExtremityParams, _ExtremityGuideT]):
    limbmodules: Sequence[LimbModule]
    guidesfactory: _GuidesFactory[_ExtremityGuideT]
    assetnode: hou.ObjNode
    mastermodule: MasterModule
    spinemodules: Sequence[SpineModule]
    model: Incomplete
    controller: Incomplete
    def __init__(self, autorigs_asset: AutoRigsAsset, limbmodules: Sequence[LimbModule], guidesfactory: _GuidesFactory[_ExtremityGuideT]) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset, arg2: object = None, arg3: object = None) -> None: ...
    buildguides: Incomplete
    def buildFromDefault(self, json: _ExtremityModuleJson) -> None: ...
    def buildFromJsonNew(self, json: _ExtremityModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _ExtremityModuleJson) -> None: ...
    def getBUiltObject(self, builtkey: str) -> None: ...
    def getBuiltObjectSide(self, builtkey: str, ismain: bool) -> None: ...
    def getLimbModuleIfExists(self) -> LimbModule | None: ...
    def buildRig(self, index: int) -> None: ...
    def canBeMirrored(self) -> bool: ...

class ExtremityGuideTab(Mod.ModuleGuideTab[_ExtremityOptionsJson, _ExtremityParamsJson, _ExtremityGuideJson, _ExtremityOptions, _ExtremityParams, _ExtremityGuideT], Generic[_ExtremityOptions, _ExtremityParams, _ExtremityGuideT]):
    GUIDE_OPTIONS: type[_ExtremityOptions]
    GUIDE_PARAMS: type[_ExtremityParams]
    tabswidget: ModuleTabsWidget
    PREFIX: str
    buildguides: Incomplete
    optionswidget: Incomplete
    paramswidget: Incomplete
    def __init__(self, buildguides: _ExtremityGuideT, assetnode: hou.ObjNode, mastermodule: MasterModule, limbmodules: Sequence[LimbModule], spinemodules: Sequence[SpineModule], model: ModuleOptionModel, controller: ModuleOptionController) -> None: ...
    def updateParent(self, limbmodules: Sequence[LimbModule], spinemodules: Sequence[SpineModule]) -> None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | LimbModule | SpineModule, hou.ObjNode]: ...
