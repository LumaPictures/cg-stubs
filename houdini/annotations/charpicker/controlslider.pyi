from typing import TypedDict

import hou
from PySide6 import QtCore, QtGui, QtWidgets

from .tabview import TabView

# A slider in the picker file; the keys are the cpglobals._JSON_* constants. Files from older
# versions can lack keys, which setSliderFromMap() fills in.
_SliderMap = TypedDict("_SliderMap", {
    "Parameter": str,
    "Character Path": str,
    "x": int,
    "y": int,
    "Label": str,
    "Minimum": float,
    "Maximum": float,
    "Show Value": bool,
    "Show Slider": bool,
    "Show Label": bool,
}, total=False)

class ControlSlider:
    csTriggeredSignal: QtCore.Signal
    csDeleteSignal: QtCore.Signal
    myId: int
    myMinimum: float
    myMaximum: float
    myNode: hou.OpNode | None
    myParameter: hou.Parm | None
    myCharPath: str
    myParmPath: str
    myLayout: QtWidgets.QHBoxLayout
    myEditMode: bool
    myLabel: str
    myLabelWidget: QtWidgets.QLabel
    mySlider: QtWidgets.QSlider
    mySpinBox: QtWidgets.QDoubleSpinBox
    myButton: QtWidgets.QToolButton
    myButtonMenu: QtWidgets.QMenu
    def __init__(self, parent: TabView, is_horizontal: bool, myId: int) -> None: ...
    def setLabel(self) -> None: ...
    def setParameter(self, set_from_update: bool = ...) -> None: ...
    def updateValueFromSpinbox(self, value: float, from_playbar_update: bool = ...) -> None: ...
    def updateValueFromSlider(self, value: int) -> None: ...
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def setRange(self) -> None: ...
    def setSliderFromMap(self, input_map: _SliderMap) -> None: ...
    def delete(self) -> None: ...
    def cleanUpUponClose(self) -> None: ...
