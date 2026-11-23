import collections
import hou
from autorigs.modules.base import buildBaseGuide as buildBaseGuide
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson

class JawGuide(buildBaseGuide.BaseGuide[collections.OrderedDict[str, collections.OrderedDict[str, str]]]):
    assetnode: hou.ObjNode
    guidenodesdata: dict[str, tuple[hou.OpNode | None, bool, bool]]
    JAW_ROOT: str
    JAW_END: str
    JAW_CURVE: str
    CURVE_OBJ_MERGE: str
    CURVE_ADD: str
    CURVE_POLYWIRE: str
    CURVE_OUT: str
    CURVE_SPHERE: str
    CURVE_CARVE1: str
    CURVE_CARVE2: str
    CURVE_MERGE: str
    def __init__(self, assetnode: hou.ObjNode) -> None: ...
    def buildFromJsonNew(self, json: _GuideNamesJson, parent: hou.ObjNode | None = None) -> dict[str, tuple[hou.OpNode | None, bool, bool]]: ...
    def createJawCurveSOP(self, parent: hou.ObjNode, jaw_root: hou.ObjNode, jaw_end: hou.ObjNode) -> None:
        """Creates the guide curve SOP for the Jaw"""
    def buildFromJsonExisting(self, json: _GuideNamesJson) -> dict[str, tuple[hou.OpNode | None, bool, bool]]: ...
    def toJSON(self) -> collections.OrderedDict[str, collections.OrderedDict[str, str]]: ...
