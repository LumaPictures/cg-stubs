# Houdini stubs generated from Houdini 22.0.466

import collections
from autorigs.modules.base.buildBaseGuide import _GuideXformJson
from autorigs.modules.simpleexample1.buildSimpleGuide import SimpleGuide as SimpleGuide
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.utils import guideParamsHelper as guideParamsHelper
from hutil.Qt import QtWidgets
from typing import TypedDict

class _SimpleParamsJson(TypedDict):
    simpleroot: _GuideXformJson
    simpleend: _GuideXformJson

class ModuleParamsWidget(QtWidgets.QWidget):
    """ Constructor of the guide parameters. The simpleguide
        is a class that contains all of the guides that are built """
    null0widgets: dict[int, UiParamFloat]
    null1widgets: dict[int, UiParamFloat]
    def __init__(self, simpleguide: SimpleGuide) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, dict[str, list[float]]]: ...
    def fromJSON(self, json: _SimpleParamsJson) -> None: ...
