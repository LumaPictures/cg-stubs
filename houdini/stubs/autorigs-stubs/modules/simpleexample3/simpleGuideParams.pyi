# Houdini stubs generated from Houdini 22.0.466

from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from autorigs.modules.simpleexample3.buildSimpleGuide import SimpleGuide as SimpleGuide
from autorigs.ui import moduleUiTab as moduleUiTab
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.utils import guideParamsHelper as guideParamsHelper
from collections import OrderedDict
from typing import TypedDict

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
