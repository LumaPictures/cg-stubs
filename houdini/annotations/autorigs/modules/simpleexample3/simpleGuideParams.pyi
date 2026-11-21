from collections import OrderedDict
from typing import TypedDict

from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from autorigs.modules.simpleexample3.buildSimpleGuide import SimpleGuide
from autorigs.ui import moduleUiTab
from autorigs.ui.uiParamFloat import UiParamFloat

class _SimpleParamsJson(TypedDict):
    rootnode: _GuideXformJson
    simpleroot: _GuideXformJson
    simpleend: _GuideXformJson

class ModuleParamsWidget(moduleUiTab.ModuleUiTab):
    rootwidgets: dict[int, UiParamFloat]
    null0widgets: dict[int, UiParamFloat]
    null1widgets: dict[int, UiParamFloat]
    def __init__(self, simpleguide: SimpleGuide) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def toJSON(self) -> OrderedDict[str, dict[str, list[float]]]: ...
    def fromJSON(self, json: _SimpleParamsJson) -> None: ...
