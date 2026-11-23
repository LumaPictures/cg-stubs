import collections
import hou
from autorigs.modules.base import buildBaseGuide as buildBaseGuide
from autorigs.modules.master.masterModule import _MasterModuleJson
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from typing import Any

class MasterGuide(buildBaseGuide.BaseGuide[collections.OrderedDict[str, collections.OrderedDict[str, str]]]):
    assetnode: hou.ObjNode
    assetnodecontents: hou.ObjNode | None
    module_master: hou.ObjNode
    modulenode: hou.ObjNode | None
    master_null: hou.ObjNode | None
    guidenodesdata: dict[str, list[Any]]
    JSON_LABEL: dict[str, str]
    JSON_LABELS: dict[str, str]
    def __init__(self, assetnode: hou.ObjNode) -> None: ...
    def createFromJson(self, json: _MasterModuleJson) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, collections.OrderedDict[str, str]]: ...
    def existingFromJson(self, json: _MasterModuleJson) -> None: ...
    def getMasterGuide(self) -> hou.ObjNode | None: ...
    def getGuideObject(self, guidename: str) -> hou.ObjNode | None: ...

class MasterFactory(buildBaseGuide.BaseFactory):
    @classmethod
    def createFromDefault(cls, json: _MasterModuleJson, autorigs_asset: hou.ObjNode) -> MasterGuide: ...
    @classmethod
    def createFromJsonNew(cls, autorigs_asset: hou.ObjNode, json: _MasterModuleJson) -> MasterGuide: ...
    @classmethod
    def createFromJsonExisting(cls, autorigs_asset: hou.ObjNode, json: _MasterModuleJson) -> MasterGuide: ...
