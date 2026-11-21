from autorigs.modules.advancedFace.tongue.buildTongueGuide import TongueGuide
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget
from autorigs.utils.guideParamsHelper import _ParamsJson

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, TongueGuide]):
    def __init__(self, buildguide: TongueGuide) -> None: ...
