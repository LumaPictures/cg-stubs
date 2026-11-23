from typing import TypeAlias

import hou

from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.asset.geometry.buildGeometryGuide import GeometryGuide
from autorigs.modules.base import moduleTabsWidget, rootModule
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.master import masterGuideOptions, masterGuideParams
from autorigs.modules.master.autoRigsMasterBuilder import AutoRigsMasterBuilder
from autorigs.modules.master.buildMasterGuide import MasterGuide
from autorigs.modules.master.masterGuideOptions import _MasterOptionsJson
from autorigs.modules.master.masterGuideParams import _MasterParamsJson
from autorigs.modules.base.rootModule import _ModuleJson, _ModuleJsonWithNode

_MasterModuleJson: TypeAlias = _ModuleJson[_MasterOptionsJson, _MasterParamsJson, _GuideNamesJson]

class MasterModule(
    rootModule.Module[
        _MasterOptionsJson,
        _MasterParamsJson,
        _GuideNamesJson,
        masterGuideOptions.ModuleOptionsWidget,
        masterGuideParams.ModuleParamsWidget,
        MasterGuide,
        dict[str, hou.ObjNode] | None,
        None,
        None,
    ]
):
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _ModuleJsonWithNode[_MasterOptionsJson, _MasterParamsJson, _GuideNamesJson]
    hookrigmap: None
    autorigs_asset: AutoRigsAsset | None
    hookrigmapping: dict[str, hou.ObjNode | None]
    geoguide: GeometryGuide | hou.ObjNode
    guidetab: "MasterGuideTab"
    geoskin: hou.ObjNode | None
    autorigsbuilder: AutoRigsMasterBuilder

    def __init__(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def initialize(self, autorigs_asset: AutoRigsAsset) -> None: ...
    def getModuleHooks(self) -> list[hou.ObjNode | None]: ...
    def getMasterGuide(self) -> hou.ObjNode | None: ...
    def buildFromDefault(self) -> None: ...
    def buildFromJsonNew(self, json: _MasterModuleJson) -> None: ...
    def buildFromJsonExisting(self, json: _MasterModuleJson) -> None: ...
    def buildRig(self, orig_asset: AutoRigsAsset, index: int) -> None: ...
    def buildHookRigMapping(self) -> None: ...
    def getBuiltMasterCtrl(self) -> hou.ObjNode | None: ...
    def getMainHook(self) -> hou.ObjNode | None: ...
    def postRigBuild(self) -> None: ...
    def updateMasterLocation(self) -> None: ...
    def toJSON(self) -> _ModuleJsonWithNode[_MasterOptionsJson, _MasterParamsJson, _GuideNamesJson]: ...

class MasterGuideTab(
    rootModule.ModuleGuideTab[
        _MasterOptionsJson,
        _MasterParamsJson,
        _GuideNamesJson,
        masterGuideOptions.ModuleOptionsWidget,
        masterGuideParams.ModuleParamsWidget,
        MasterGuide,
    ]
):
    PREFIX: str
    tabswidget: moduleTabsWidget.ModuleTabsWidget

    def __init__(self, autorigs_asset: AutoRigsAsset, buildguides: MasterGuide) -> None: ...
