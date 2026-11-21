# Houdini stubs generated from Houdini 22.0.466

from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget as BaseParamWidget
from autorigs.modules.jaw.buildJawGuide import JawGuide as JawGuide
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.utils import guideParamsHelper as guideParamsHelper
from autorigs.utils.guideParamsHelper import _ParamsJson

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, JawGuide]):
    def __init__(self, jawguide: JawGuide) -> None: ...
