# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.modules.base import buildBaseGuide as buildBaseGuide
from autorigs.modules.base.buildBaseGuide import _BaseGuideJson, _GuideNamesJson

class TongueGuide(buildBaseGuide.BaseGuide[_BaseGuideJson]):
    assetnode: hou.ObjNode
    guidenodesdata: dict[str, list[hou.OpNode | bool | None]]
    TONGUE_ROOT: str
    TONGUE_1: str
    TONGUE_2: str
    TONGUE_3: str
    TONGUE_TIP: str
    GUIDE_CURVE: str
    NUM_GUIDES: int
    def __init__(self, assetnode: hou.ObjNode) -> None: ...
    def buildFromJsonNew(self, json: _GuideNamesJson, parent: hou.ObjNode | None = None) -> None: ...
    def buildFromJsonExisting(self, json: _GuideNamesJson) -> None: ...
