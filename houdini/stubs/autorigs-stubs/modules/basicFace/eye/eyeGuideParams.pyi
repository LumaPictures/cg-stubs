from .eyeGuideModel import EyeGuideModel as EyeGuideModel
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget as BaseParamWidget
from autorigs.modules.basicFace.eye.buildEyeGuide import EyeGuide as EyeGuide
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.utils.guideParamsHelper import _ParamsJson
from hutil.Qt import QtWidgets
from typing import Literal

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, EyeGuide]):
    main_box: QtWidgets.QVBoxLayout
    eyeguide: EyeGuide
    centertab: QtWidgets.QWidget
    innertab: QtWidgets.QWidget
    outertab: QtWidgets.QWidget
    tab: QtWidgets.QTabWidget
    EYELID_CENTER_GUIDE_NAME: str
    EYELID_INNER_GUIDE_NAME: str
    EYELID_OUTER_GUIDE_NAME: str
    def __init__(self, eyeguide: EyeGuide) -> None: ...
    def createEyelidGuideTab(self, guide_name: Literal['eyelid_center', 'eyelid_inner', 'eyelid_outer']) -> QtWidgets.QWidget:
        """Creates the widget of the eyelid guide tab"""
    def flipTabs(self, value: int) -> None: ...
