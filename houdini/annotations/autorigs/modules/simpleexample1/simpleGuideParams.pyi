import collections
from typing import TypedDict

from PySide6 import QtWidgets
from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from autorigs.modules.simpleexample1.buildSimpleGuide import SimpleGuide
from autorigs.ui.uiParamFloat import UiParamFloat

class _SimpleParamsJson(TypedDict):
    simpleroot: _GuideXformJson
    simpleend: _GuideXformJson

class ModuleParamsWidget(QtWidgets.QWidget):
    null0widgets: dict[int, UiParamFloat]
    null1widgets: dict[int, UiParamFloat]
    def __init__(self, simpleguide: SimpleGuide) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, dict[str, list[float]]]: ...
    def fromJSON(self, json: _SimpleParamsJson) -> None: ...
