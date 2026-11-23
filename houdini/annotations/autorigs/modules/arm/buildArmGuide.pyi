
import hou

from autorigs.modules.limb import buildLimbGuide
from autorigs.modules.limb.limbModule import _LimbModuleJson

class ArmGuide(buildLimbGuide.LimbGuide):
    JSON_LABELS: dict[str, str]
    JSON_PARAM_LABELS: dict[str, str]
    has_rotation_end: bool
    def __init__(self, assetnode: hou.OpNode) -> None: ...

class ArmFactory(buildLimbGuide.LimbFactory):
    @classmethod
    def createFromJsonNew(cls, json: _LimbModuleJson, assetnode: hou.OpNode) -> ArmGuide: ...
    @classmethod
    def createFromJsonExisting(cls, json: _LimbModuleJson, assetnode: hou.OpNode) -> ArmGuide: ...
