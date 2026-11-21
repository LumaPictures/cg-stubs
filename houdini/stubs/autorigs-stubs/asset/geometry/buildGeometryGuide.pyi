import collections
import hou
from autorigs.asset import defaultProperties as defaultProperties
from collections.abc import Mapping

class GeometryFactory:
    DEFAULT_JSON_FILE: str
    DEFAULT_JSON: dict[str, dict[str, str]]
    @classmethod
    def createFromJsonExisting(self, assetnode: hou.ObjNode, json: Mapping[str, Mapping[str, str]]) -> GeometryGuide: ...
    @classmethod
    def createFromDefault(cls, assetnode: hou.ObjNode) -> GeometryGuide: ...
    @classmethod
    def createFromJsonNew(cls, assetnode: hou.ObjNode, json: Mapping[str, Mapping[str, str]]) -> GeometryGuide: ...
    @classmethod
    def createFromJsonBuild(cls, assetnode: hou.ObjNode, json: Mapping[str, Mapping[str, str]]) -> GeometryGuide: ...

class GeometryGuide:
    assetnode: hou.ObjNode
    guidenodes: dict[str, hou.OpNode | None]
    GEOSKIN_DEFAULT_NAME: str
    GUIDENAMES: dict[str, str]
    OBJFILE_SWITCH_OPERATOR: int
    OBJFILE_SWITCH_FILE: int
    PLACEMENT_SWITCH_OBJFILE: int
    PLACEMENT_SWITCH_PLACEGEO: int
    PLACEMENT_SWITCH_STANDIN: int
    PLACEMENT_TRANS_SWITCH_AS_IS: int
    PLACEMENT_TRANS_SWITCH_AUTOPLACE: int
    OPERATOR_OFFSET_TRANSLATE: tuple[int, int, int]
    OPERATOR_OFFSET_ROTATE: tuple[int, int, int]
    OPERATOR_OFFSET_SCALE: tuple[int, int, int]
    FILE_OFFSET_TRANSLATE: tuple[int, int, int]
    FILE_OFFSET_ROTATE: tuple[int, int, int]
    FILE_OFFSET_SCALE: tuple[int, int, int]
    STANDIN_OFFSET_TRANSLATE: tuple[int, int, int]
    STANDIN_OFFSET_ROTATE: tuple[int, int, int]
    STANDIN_OFFSET_SCALE: tuple[int, int, int]
    AUTOPLACEMENT_TRANSLATE: tuple[int, int, int]
    AUTOPLACEMENT_ROTATE: tuple[int, int, int]
    def __init__(self, assetnode: hou.ObjNode) -> None: ...
    def createNewFromJson(self, json: Mapping[str, Mapping[str, str]]) -> None: ...
    def createFromJson(self, json: Mapping[str, Mapping[str, str]]) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, dict[str, str]]: ...
    def existingFromJson(self, json: Mapping[str, Mapping[str, str]]) -> None: ...
    def getBuiltGuideNodes(self) -> dict[str, hou.OpNode | None]: ...
    def destroyGuides(self) -> None: ...
    def getStandIn(self) -> hou.ObjNode: ...
    def getGeoSkin(self) -> hou.ObjNode | None: ...
