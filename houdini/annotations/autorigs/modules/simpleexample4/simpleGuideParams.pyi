from collections import OrderedDict
from collections.abc import Sequence
from typing import TypedDict

from PySide6 import QtWidgets

from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from autorigs.modules.simpleexample4.buildSimpleGuide import SimpleGuide
from autorigs.modules.simpleexample4.simpleGuideModel import SimpleModel
from autorigs.ui import moduleUiTab
from autorigs.ui.uiParamFloat import UiParamFloat

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
