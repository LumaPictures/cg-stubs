import collections
from typing import TypedDict

from autorigs.modules.base.buildBaseGuide import _GuideXformJson
import hou
from PySide6 import QtWidgets

from autorigs.modules.master.buildMasterGuide import MasterGuide
from autorigs.ui.uiParamColor import UiParamColor
from autorigs.ui.uiParamFloat import UiParamFloat
from autorigs.ui.uiParamInt import UiParamInt

class _MasterParamsJson(TypedDict):
    master: _GuideXformJson

class ModuleParamsWidget(QtWidgets.QWidget):
    JSON_LABELS: dict[str, str]
    widget: QtWidgets.QWidget
    mainlayout: QtWidgets.QVBoxLayout
    master_null: hou.ObjNode | None
    buildguides: MasterGuide
    modulenode: hou.ObjNode | None
    masterwidgets: dict[int, UiParamFloat | UiParamColor | UiParamInt]
    scroll: QtWidgets.QScrollArea
    vLayout: QtWidgets.QVBoxLayout

    def __init__(self, masterguide: MasterGuide) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def getSizeParameter(self) -> float: ...
    def getControlColor(self) -> UiParamColor: ...
    def getTranslate(self) -> tuple[float, float, float]: ...
    def getRotate(self) -> tuple[float, float, float]: ...
    def toJSON(self) -> collections.OrderedDict[str, _GuideXformJson]: ...
    def fromJSON(self, json: _MasterParamsJson) -> bool: ...
