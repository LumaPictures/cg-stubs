import collections
from typing import Literal, TypedDict

import hou
from PySide6 import QtCore, QtWidgets

from autorigs.ui.uiParamComboBox import UiParamComboBox
from autorigs.ui.uiParamFile import UiParamOperator
from autorigs.ui.uiParamFloat import UiParamFloat

class _LocatorValues(TypedDict):
    locator: str
    uv: list[float]
    parent: str
    parent_type: int

class UiParamLocatorWidget(QtWidgets.QWidget):
    PARENT_TYPE_ITEMS: list[str]
    PARENT_TYPE_NONE: int
    PARENT_TYPE_NURBS: int
    PARENT_TYPE_CUSTOM: int

    locatorChanged: QtCore.Signal
    locatorPlaced: QtCore.Signal
    uvwChanged: QtCore.Signal
    updatePressed: QtCore.Signal

    PATH: Literal["locator"]
    UVW: Literal["uv"]
    PARENT_PATH: Literal["parent"]
    PARENT_TYPE: Literal["parent_type"]

    widgets: collections.OrderedDict[str, UiParamOperator | UiParamFloat | UiParamComboBox]

    def __init__(self, relative_node: hou.OpNode | None = ...) -> None: ...
    def toggleParentVisibility(self, index: int, widget: QtWidgets.QWidget) -> None: ...
    def getPathWidget(self) -> UiParamOperator: ...
    def getUvwWidget(self) -> UiParamFloat: ...
    def getParentPathWidget(self) -> UiParamOperator: ...
    def getParentTypeWidget(self) -> UiParamComboBox: ...
    def unlinkParms(self) -> None: ...
    def getValues(self) -> collections.OrderedDict[str, str | list[float] | int]: ...
    def setValues(self, json: _LocatorValues) -> None: ...
