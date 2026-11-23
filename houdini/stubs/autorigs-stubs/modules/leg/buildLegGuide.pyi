import hou
from autorigs.modules.limb import buildLimbGuide as buildLimbGuide
from autorigs.modules.limb.limbGuideParams import LegParamsWidget as LegParamsWidget
from autorigs.modules.limb.limbModule import _LimbModuleJson

class LegGuide(buildLimbGuide.LimbGuide):
    has_rotation_end: bool
    JSON_LABELS: dict[str, str]
    JSON_PARAM_LABELS: dict[str, str]
    def __init__(self, assetnode: hou.ObjNode) -> None: ...

class LegFactory(buildLimbGuide.LimbFactory):
    @classmethod
    def createFromJsonNew(cls, json: _LimbModuleJson, assetnode: hou.ObjNode) -> LegGuide: ...
    @classmethod
    def createFromJsonExisting(cls, json: _LimbModuleJson, assetnode: hou.ObjNode) -> LegGuide: ...
