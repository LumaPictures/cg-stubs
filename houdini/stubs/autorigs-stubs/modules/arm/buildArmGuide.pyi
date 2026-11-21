import hou
from autorigs.modules.limb import buildLimbGuide as buildLimbGuide
from autorigs.modules.limb.limbGuideParams import ArmParamsWidget as ArmParamsWidget
from autorigs.modules.limb.limbModule import _LimbModuleJson

class ArmGuide(buildLimbGuide.LimbGuide):
    has_rotation_end: bool
    JSON_LABELS: dict[str, str]
    JSON_PARAM_LABELS: dict[str, str]
    def __init__(self, assetnode: hou.OpNode) -> None: ...

class ArmFactory(buildLimbGuide.LimbFactory):
    @classmethod
    def createFromJsonNew(cls, json: _LimbModuleJson, assetnode: hou.OpNode) -> ArmGuide: ...
    @classmethod
    def createFromJsonExisting(cls, json: _LimbModuleJson, assetnode: hou.OpNode) -> ArmGuide: ...
