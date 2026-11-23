from typing import Literal

from PySide6 import QtWidgets

from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget
from autorigs.modules.basicFace.eye.buildEyeGuide import EyeGuide
from autorigs.utils.guideParamsHelper import _ParamsJson

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, EyeGuide]):
    EYELID_CENTER_GUIDE_NAME: str
    EYELID_INNER_GUIDE_NAME: str
    EYELID_OUTER_GUIDE_NAME: str

    main_box: QtWidgets.QVBoxLayout
    eyeguide: EyeGuide
    centertab: QtWidgets.QWidget
    innertab: QtWidgets.QWidget
    outertab: QtWidgets.QWidget
    tab: QtWidgets.QTabWidget

    def __init__(self, eyeguide: EyeGuide) -> None: ...
    def createEyelidGuideTab(
        self, guide_name: Literal["eyelid_center", "eyelid_inner", "eyelid_outer"]
    ) -> QtWidgets.QWidget: ...
    def flipTabs(self, value: int) -> None: ...
