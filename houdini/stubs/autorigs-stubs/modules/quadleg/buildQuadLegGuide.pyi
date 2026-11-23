import hou
from autorigs.modules.limb import buildLimbGuide as buildLimbGuide
from autorigs.modules.limb.limbGuideParams import QuadLegParamsWidget as QuadLegParamsWidget
from autorigs.modules.limb.limbModule import _LimbModuleJson, _LimbParamsJson
from collections.abc import MutableMapping

class QuadLegGuide(buildLimbGuide.LimbGuide):
    has_rotation_end: bool
    JSON_LABELS: dict[str, str]
    JSON_PARAM_LABELS: dict[str, str]
    def __init__(self, assetnode: hou.ObjNode) -> None: ...
    def toJsonGuideTypeNames(self, jsonobj: MutableMapping[str, str], ismain: bool) -> None: ...

class QuadLegFactory(buildLimbGuide.LimbFactory):
    @classmethod
    def createFromJsonNew(cls, json: _LimbModuleJson, guidejson: _LimbParamsJson, assetnode: hou.ObjNode) -> QuadLegGuide: ...
    @classmethod
    def createFromJsonExisting(cls, json: _LimbModuleJson, assetnode: hou.ObjNode) -> QuadLegGuide: ...
