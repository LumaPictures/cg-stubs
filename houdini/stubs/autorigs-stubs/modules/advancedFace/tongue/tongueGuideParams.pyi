from autorigs.modules.advancedFace.tongue.buildTongueGuide import TongueGuide as TongueGuide
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget as BaseParamWidget
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.utils.guideParamsHelper import _ParamsJson

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, TongueGuide]):
    def __init__(self, buildguide: TongueGuide) -> None: ...
