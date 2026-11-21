from collections.abc import MutableMapping

import hou
from autorigs.modules.limb import buildLimbGuide
from autorigs.modules.limb.limbModule import _LimbModuleJson, _LimbParamsJson

class QuadLegGuide(buildLimbGuide.LimbGuide):
    JSON_LABELS: dict[str, str]
    JSON_PARAM_LABELS: dict[str, str]
    has_rotation_end: bool
    def __init__(self, assetnode: hou.ObjNode) -> None: ...
    def toJsonGuideTypeNames(self, jsonobj: MutableMapping[str, str], ismain: bool) -> None: ...

class QuadLegFactory(buildLimbGuide.LimbFactory):
    @classmethod
    def createFromJsonNew(
        cls, json: _LimbModuleJson, guidejson: _LimbParamsJson, assetnode: hou.ObjNode
    ) -> QuadLegGuide: ...
    @classmethod
    def createFromJsonExisting(cls, json: _LimbModuleJson, assetnode: hou.ObjNode) -> QuadLegGuide: ...
