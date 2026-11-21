# Houdini stubs generated from Houdini 22.0.466

import collections
import hou
from autorigs.modules.base import buildBaseGuide as buildBaseGuide
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.simpleexample1.simpleGuideParams import _SimpleParamsJson

class SimpleGuide(buildBaseGuide.BaseGuide[collections.OrderedDict[str, collections.OrderedDict[str, str]]]):
    assetnode: hou.ObjNode
    guidenodesdata: dict[str, tuple[hou.ObjNode | None, bool, bool]]
    def __init__(self, assetnode: hou.ObjNode) -> None: ...
    def buildFromJsonNew(self, json: _GuideNamesJson, paramjson: _SimpleParamsJson) -> None:
        """ paramjson is the transforms, which we don't use here
            but could use in other situations. However, since the
            parameters widgets are linked to the ndoes in the viewport,
            doing a fromJson call there will actually update the values
            of the transforms in the nodes to the values in the json
            (see simpleGuideParams.py). Hence, we don't actually need
            to do any transforming here. """
    def buildFromJsonExisting(self, json: _GuideNamesJson) -> None: ...
    def getGuideObject(self, guidename: str) -> hou.ObjNode | None: ...
    def toJSON(self) -> collections.OrderedDict[str, collections.OrderedDict[str, str]]: ...
