import hou
from . import masterGuideOptions as masterGuideOptions, masterGuideParams as masterGuideParams
from .buildMasterGuide import MasterFactory as MasterFactory
from autorigs.asset import defaultProperties as defaultProperties
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.asset.geometry.buildGeometryGuide import GeometryGuide as GeometryGuide
from autorigs.modules.base import moduleTabsWidget as moduleTabsWidget, rootModule as Mod
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.base.rootModule import _ModuleJsonWithNode
from autorigs.modules.master.autoRigsMasterBuilder import AutoRigsMasterBuilder as AutoRigsMasterBuilder
from autorigs.modules.master.buildMasterGuide import MasterGuide as MasterGuide
from autorigs.modules.master.masterGuideOptions import _MasterOptionsJson
from autorigs.modules.master.masterGuideParams import _MasterParamsJson
from autorigs.utils import geometryutils as geometryutils

from typing import TypeAlias
from autorigs.modules.base.rootModule import _ModuleJson
from typing import TypeAlias
_MasterModuleJson: TypeAlias = _ModuleJson[_MasterOptionsJson, _MasterParamsJson, _GuideNamesJson]
class MasterModule(Mod.Module[_MasterOptionsJson, _MasterParamsJson, _GuideNamesJson, masterGuideOptions.ModuleOptionsWidget, masterGuideParams.ModuleParamsWidget, MasterGuide, dict[str, hou.ObjNode] | None, None, None, 'MasterGuideTab']):
    hookrigmap: None
    autorigs_asset: AutoRigsAsset | None
    hookrigmapping: dict[str, hou.ObjNode | None]
    geoguide: GeometryGuide | hou.ObjNode
    guidetab: MasterGuideTab | None
    geoskin: hou.ObjNode | None
    autorigsbuilder: AutoRigsMasterBuilder
    builtrig: dict[str, hou.ObjNode] | None
    buildguides: MasterGuide
    MODULE_TYPE: str
    MODULE_DEFAULT_NAME: str
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: _ModuleJsonWithNode[_MasterOptionsJson, _MasterParamsJson, _GuideNamesJson]
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
    def updateMasterLocation(self) -> None:
        """Autoplace the master control if needed"""
    def toJSON(self) -> _ModuleJsonWithNode[_MasterOptionsJson, _MasterParamsJson, _GuideNamesJson]: ...

class MasterGuideTab(Mod.ModuleGuideTab[_MasterOptionsJson, _MasterParamsJson, _GuideNamesJson, masterGuideOptions.ModuleOptionsWidget, masterGuideParams.ModuleParamsWidget, MasterGuide, moduleTabsWidget.ModuleTabsWidget]):
    tabswidget: moduleTabsWidget.ModuleTabsWidget
    buildguides: MasterGuide
    optionswidget: masterGuideOptions.ModuleOptionsWidget
    paramswidget: masterGuideParams.ModuleParamsWidget
    PREFIX: str
    def __init__(self, autorigs_asset: AutoRigsAsset, buildguides: MasterGuide) -> None: ...
