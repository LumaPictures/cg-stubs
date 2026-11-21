from collections.abc import Iterable

from PySide6 import QtWidgets
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget
from autorigs.modules.advancedFace.cage.buildCageGuide import CageGuide
from autorigs.modules.advancedFace.cage.cageGuideModel import CageGuideModel
from autorigs.utils.guideParamsHelper import _ParamsJson

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, CageGuide]):
    model: CageGuideModel
    guide_tab: QtWidgets.QTabWidget
    primary_tab: QtWidgets.QWidget
    secondary_tab: QtWidgets.QWidget
    def __init__(self, cageguide: CageGuide, model: CageGuideModel) -> None: ...
    def createGuidesLayout(self, guides: Iterable[str]) -> QtWidgets.QVBoxLayout: ...
