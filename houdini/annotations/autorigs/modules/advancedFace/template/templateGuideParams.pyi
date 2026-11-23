from autorigs.modules.advancedFace.template.buildTemplateGuide import TemplateGuide
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget
from autorigs.utils.guideParamsHelper import _ParamsJson

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, TemplateGuide]):
    def __init__(self, templateguide: TemplateGuide) -> None: ...
