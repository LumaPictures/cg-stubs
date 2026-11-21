from collections.abc import Callable, Iterable, Mapping, Sequence
from typing import Any, Generic, TypeAlias

from typing_extensions import TypeVar

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base import moduleTabsWidget, rootModule
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson, _GuideXformJson
from autorigs.modules.limb.autoRigsLimbInterfaceBuilder import _LimbControls
from autorigs.modules.limb.buildLimbGuide import LimbFactory, LimbGuide
from autorigs.modules.limb.limbGuideOptions import ModuleOptionsWidget, _LimbOptionsJson
from autorigs.modules.limb.limbGuideParams import ModuleParamsWidget
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.spine.spineModule import SpineModule
from autorigs.modules.base.rootModule import _ModuleJson

# {guide label: its transform params}, as limbGuideParams.ModuleParamsWidget writes and reads it
_LimbParamsJson: TypeAlias = Mapping[str, _GuideXformJson]
_LimbModuleJson: TypeAlias = _ModuleJson[_LimbOptionsJson, _LimbParamsJson, _GuideNamesJson]
_LimbRig: TypeAlias = tuple[_LimbControls, _LimbControls | None]

# The arm, leg and quadleg modules each have their own widgets and guide; a bare LimbModule is any.
_LimbOptions = TypeVar("_LimbOptions", bound=ModuleOptionsWidget, default=Any)
_LimbParams = TypeVar("_LimbParams", bound=ModuleParamsWidget, default=Any)
_LimbGuide = TypeVar("_LimbGuide", bound=LimbGuide, default=Any)

class LimbModule(
    rootModule.Module[
        _LimbOptionsJson,
        _LimbParamsJson,
        _GuideNamesJson,
        _LimbOptions,
        _LimbParams,
        _LimbGuide,
        _LimbRig | None,
        None,
        None,
    ],
    Generic[_LimbOptions, _LimbParams, _LimbGuide],
):
    guidesfactory: type[LimbFactory]
    builtparentinfo: tuple[MasterModule | SpineModule, hou.OpNode] | None
    mastermodule: MasterModule
    autorigs_asset: AutoRigsAsset | None
    spinemodules: list[SpineModule]
    guidetab: "LimbGuideTab[_LimbOptions, _LimbParams, _LimbGuide]"

    def __init__(self, autorigs_asset: AutoRigsAsset, guidesfactory: type[LimbFactory]) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def updateParent(self, modulesdict: Mapping[str, Sequence[rootModule.Module]]) -> None: ...
    def buildFromDefault(self, json: _LimbModuleJson) -> None: ...
    def buildFromJsonNew(self, json: _LimbModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _LimbModuleJson) -> None: ...
    def buildRig(self, index: int) -> None: ...
    def getBuiltRig(self) -> _LimbRig | None: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | SpineModule, hou.OpNode] | None: ...
    def getBUiltObject(self, builtkey: str) -> None: ...
    def getBuiltObjectSide(self, builtkey: str, ismain: bool) -> None: ...
    def getSide(self) -> int: ...
    def linkSide(self, callback_fcn: Callable[[int], object]) -> None: ...
    def unlinkSide(self, callback_fcn: Callable[[int], object]) -> None: ...
    def canBeMirrored(self) -> bool: ...

class LimbGuideTab(
    rootModule.ModuleGuideTab[
        _LimbOptionsJson, _LimbParamsJson, _GuideNamesJson, _LimbOptions, _LimbParams, _LimbGuide
    ],
    Generic[_LimbOptions, _LimbParams, _LimbGuide],
):
    PREFIX: str
    GUIDE_OPTIONS: type[_LimbOptions]
    GUIDE_PARAMS: type[_LimbParams]
    tabswidget: moduleTabsWidget.ModuleTabsWidget

    def __init__(self, buildguides: _LimbGuide, spinemodules: Iterable[SpineModule], mastermodule: MasterModule) -> None: ...
    def updateParent(self, spinemodules: Iterable[SpineModule]) -> None: ...
    def getSide(self) -> int: ...
    def getBuiltParentInfo(self) -> tuple[MasterModule | SpineModule, hou.ObjNode]: ...
    def linkSide(self, callback_fcn: Callable[[int], object]) -> None: ...
    def unlinkSide(self, callback_fcn: Callable[[int], object]) -> None: ...
