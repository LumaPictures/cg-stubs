from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget
from autorigs.modules.jaw.buildJawGuide import JawGuide
from autorigs.utils.guideParamsHelper import _ParamsJson

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, JawGuide]):
    def __init__(self, jawguide: JawGuide) -> None: ...
