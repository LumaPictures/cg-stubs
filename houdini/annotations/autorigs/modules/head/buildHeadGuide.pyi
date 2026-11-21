import collections
from typing import Literal, overload

import hou
from autorigs.modules.base import buildBaseGuide
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.head.headModule import _HeadModuleJson

class HeadGuide(buildBaseGuide.BaseGuide[collections.OrderedDict[str, collections.OrderedDict[str, str]]]):
    JSON_LABEL: dict[str, str]
    parent: hou.OpNode | None
    assetnode: hou.ObjNode
    assetnodecontents: hou.OpNode | None
    guidenodesdata: dict[str, tuple[hou.OpNode | None, bool, bool]]
    module_head: hou.ObjNode | None
    modulenode: hou.ObjNode
    def __init__(self, assetnode: hou.ObjNode, parent: hou.OpNode | None = ...) -> None: ...
    def updateToMasterParent(self, masternode: hou.ObjNode) -> None: ...
    def updateToSpineHookParent(self, node: hou.ObjNode) -> None: ...
    def existingFromJson(self, json: _GuideNamesJson) -> None: ...
    def createFromJson(self, json: _HeadModuleJson) -> None: ...
    def deleteGuides(self) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, collections.OrderedDict[str, str]]: ...
    def updateParent(self, parenttext: str) -> None: ...
    def getChosenParentNode(self) -> str | None: ...
    @overload
    def getGuideObject(
        self,
        guidename: Literal[
            "modulenode",
            "neckroot",
            "neckblend",
            "neck1",
            "headroot",
            "head1",
            "guidecurve",
            "neckroothook",
            "headroothook",
        ],
    ) -> hou.ObjNode | None: ...
    @overload
    def getGuideObject(
        self,
        guidename: Literal["guidecurve_merge", "guidecurve_add", "guidecurve_polywire", "guidecurve_out"],
    ) -> hou.SopNode | None: ...
    @overload
    def getGuideObject(self, guidename: str) -> hou.OpNode | None: ...

class HeadFactory(buildBaseGuide.BaseFactory):
    @classmethod
    def createFromDefault(
        cls, json: _HeadModuleJson, assetnode: hou.ObjNode, parent: hou.OpNode | None = ...
    ) -> HeadGuide: ...
    @classmethod
    def createFromJsonNew(
        cls, json: _HeadModuleJson, assetnode: hou.ObjNode, parent: hou.OpNode | None = ...
    ) -> HeadGuide: ...
    @classmethod
    def createFromJsonExisting(
        cls, json: _HeadModuleJson, assetnode: hou.ObjNode, parent: hou.OpNode | None = ...
    ) -> HeadGuide: ...
