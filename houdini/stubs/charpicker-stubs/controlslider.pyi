# Houdini stubs generated from Houdini 22.0.466

import hou
from . import cpglobals as cpglobals
from .tabview import TabView as TabView
from PySide6 import QtGui as QtGui
from hutil.Qt import QtCore, QtWidgets
from typing import TypedDict

_SliderMap = TypedDict('_SliderMap', {'Parameter': str, 'Character Path': str, 'x': int, 'y': int, 'Label': str, 'Minimum': float, 'Maximum': float, 'Show Value': bool, 'Show Slider': bool, 'Show Label': bool}, total=False)

class ControlSlider(QtWidgets.QWidget):
    """Custom signals for control button class """
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
    csTriggeredSignal: QtCore.Signal
    csDeleteSignal: QtCore.Signal
    def __init__(self, parent: TabView, is_horizontal: bool, myId: int) -> None: ...
    def setLabel(self) -> None:
        '''"Sets the text of the label widget. If it is currently invisible, shows it.
        '''
    def setParameter(self, set_from_update: bool = False) -> None:
        """Opens the tree menu to select the parameter to link to. Optionally
        sets the parameter from update which will not open the menu and will
        use myParmPath as the parameter. This is useful when myParmPath is changed
        outside of this widget. Updates the tooltip display text.
        """
    def updateValueFromSpinbox(self, value: float, from_playbar_update: bool = False) -> None:
        """Updates the value of the parameter.
        """
    def updateValueFromSlider(self, value: int) -> None:
        """Updates the value of the spinbox based on the value of the slider.
        Since sliders can only have integer values, divides the slider's value.
        """
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """Handles drag and drop for repositioning the button
        with absolute positioning. Only accepts right mouse button
        """
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """Handles mouse press on button, depending on mode and
        modifiers, sends process to helper functions. Only accepts
        left mouse button for all actions.
        Needs to emit a tuple for the tabview to handle correctly. This is because
        controlbutton will use modifiers.
        """
    def setRange(self) -> None:
        """Opens an input dialog and sets the range of the slider values.
        """
    def setSliderFromMap(self, input_map: _SliderMap) -> None:
        """Sets the slider's parameters based on the map loaded from a file or HDA.
        """
    def delete(self) -> None: ...
    def cleanUpUponClose(self) -> None:
        """Removes parent and signal-slot connections to allow for complete
        cleanup upon garbage collection.
        """
