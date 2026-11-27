import hou
from enum import Enum
from hutil.PySide import QtCore, QtGui, QtWidgets
from typing import ClassVar


class ChangeType:
    STARTED: int
    UPDATED: int
    FINISHED: int

class SliderValue(hou.qt.InputField):
    BG_STYLE_SHEET: str
    def __init__(self, data_type: int) -> None: ...
    def setBackgroundColor(self, color: QtGui.QColor) -> None: ...
    def clearFocus(self) -> None: ...

class SimpleSlider(QtWidgets.QWidget):
    """Custom slider with input field"""
    class SliderStyle(QtWidgets.QProxyStyle):
        def styleHint(self, hint: QtWidgets.QStyle.StyleHint, option: QtWidgets.QStyleOption | None, widget: QtWidgets.QWidget | None, returndata: QtWidgets.QStyleHintReturn | None) -> int: ...
    valueChanged: ClassVar[QtCore.Signal]
    H_SPACE: int
    DEFAULT_FIELD_WIDTH: int
    DECIMALS: int
    def __init__(self, parent: QtWidgets.QWidget | None, default_value: float = 0.0, show_slider: bool = True, value_field_type: type[SliderValue] = ..., field_width: int = ...) -> None: ...
    def clearFocus(self) -> None: ...
    def value(self) -> float: ...
    def ignoreUpdates(self) -> bool: ...
    def setIgnoreUpdates(self, ignore: bool) -> None: ...
    def setBackgroundColor(self, color: QtGui.QColor) -> None: ...
    def setValue(self, value: float, notify: bool = True) -> None:
        """
        Programmatically set the value and ensure widgets are updated.
        """

class KeyableSliderValue(SliderValue):
    valueKeyed: ClassVar[QtCore.Signal]
    valueKeyRemoved: ClassVar[QtCore.Signal]
    valueKeyReset: ClassVar[QtCore.Signal]
    animationRemoved: ClassVar[QtCore.Signal]
    addedToChannelList: ClassVar[QtCore.Signal]
    def onMousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...

class KeyableSlider(SimpleSlider):
    """
    Variant of the SimpleSlider which emits signals for mouse events related to
    keying
    """
    valueKeyed: ClassVar[QtCore.Signal]
    valueKeyRemoved: ClassVar[QtCore.Signal]
    valueKeyReset: ClassVar[QtCore.Signal]
    animationRemoved: ClassVar[QtCore.Signal]
    addedToChannelList: ClassVar[QtCore.Signal]
    def __init__(self, parent: QtWidgets.QWidget | None, show_slider: bool = True) -> None: ...
