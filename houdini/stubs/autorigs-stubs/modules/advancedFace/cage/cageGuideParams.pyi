# Houdini stubs generated from Houdini 22.0.466

from autorigs.modules.advancedFace.cage.buildCageGuide import CageGuide as CageGuide
from autorigs.modules.advancedFace.cage.cageGuideModel import CageGuideModel as CageGuideModel
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget as BaseParamWidget
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.utils.guideParamsHelper import _ParamsJson
from collections.abc import Iterable
from hutil.Qt import QtWidgets

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, CageGuide]):
    model: CageGuideModel
    guide_tab: QtWidgets.QTabWidget
    primary_tab: QtWidgets.QWidget
    secondary_tab: QtWidgets.QWidget
    def __init__(self, cageguide: CageGuide, model: CageGuideModel) -> None: ...
    def createGuidesLayout(self, guides: Iterable[str]) -> QtWidgets.QVBoxLayout: ...
