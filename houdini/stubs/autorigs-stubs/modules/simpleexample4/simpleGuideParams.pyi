# Houdini stubs generated from Houdini 22.0.466

from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from autorigs.modules.simpleexample4.buildSimpleGuide import SimpleGuide as SimpleGuide
from autorigs.modules.simpleexample4.simpleGuideModel import SimpleModel as SimpleModel
from autorigs.ui import moduleUiTab as moduleUiTab
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.utils import guideParamsHelper as guideParamsHelper
from collections import OrderedDict
from collections.abc import Sequence
from hutil.Qt import QtWidgets
from typing import TypedDict

class _SimpleParamsJson(TypedDict):
    simpleguides: Sequence[_GuideXformJson]

class ModuleParamsWidget(moduleUiTab.ModuleUiTab):
    simpleguide: SimpleGuide
    coollabel: QtWidgets.QLabel
    tabswidgets: list[dict[int, UiParamFloat]]
    tabs: QtWidgets.QTabWidget
    def __init__(self, simpleguide: SimpleGuide, model: SimpleModel) -> None: ...
    def syncTabsWithGuides(self, simpleguide: SimpleGuide) -> None: ...
    def onNumBonesChanged(self, numbones: int) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def toJSON(self) -> OrderedDict[str, list[dict[str, list[float]]]]: ...
    def fromJSON(self, json: _SimpleParamsJson) -> None: ...
