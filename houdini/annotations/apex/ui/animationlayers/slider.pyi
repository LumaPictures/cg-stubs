from typing import ClassVar

import hou
from PySide6 import QtCore, QtGui, QtWidgets

class SliderValue(hou.qt.InputField):
    # data_type is a hou.qt.InputField data type (IntegerType, FloatType, StringType).
    def __init__(self, data_type: int) -> None: ...
    def setBackgroundColor(self, color: QtGui.QColor) -> None: ...
    def clearFocus(self) -> None: ...

class SimpleSlider(QtWidgets.QWidget):
    class SliderStyle(QtWidgets.QProxyStyle):
        def styleHint(
            self,
            hint: QtWidgets.QStyle.StyleHint,
            option: QtWidgets.QStyleOption | None,
            widget: QtWidgets.QWidget | None,
            returndata: QtWidgets.QStyleHintReturn | None,
        ) -> int: ...

    # Emits a ChangeType.
    valueChanged: ClassVar[QtCore.Signal]
    H_SPACE: int
    DEFAULT_FIELD_WIDTH: int
    def __init__(
        self,
        parent: QtWidgets.QWidget | None,
        default_value: float = ...,
        show_slider: bool = ...,
        value_field_type: type[SliderValue] = ...,
        field_width: int = ...,
    ) -> None: ...
    def clearFocus(self) -> None: ...
    def value(self) -> float: ...
    def ignoreUpdates(self) -> bool: ...
    def setIgnoreUpdates(self, ignore: bool) -> None: ...
    def setBackgroundColor(self, color: QtGui.QColor) -> None: ...
    def setValue(self, value: float, notify: bool = ...) -> None: ...

class KeyableSliderValue(SliderValue):
    valueKeyed: ClassVar[QtCore.Signal]
    valueKeyRemoved: ClassVar[QtCore.Signal]
    valueKeyReset: ClassVar[QtCore.Signal]
    animationRemoved: ClassVar[QtCore.Signal]
    addedToChannelList: ClassVar[QtCore.Signal]
    def onMousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...

class KeyableSlider(SimpleSlider):
    valueKeyed: ClassVar[QtCore.Signal]
    valueKeyRemoved: ClassVar[QtCore.Signal]
    valueKeyReset: ClassVar[QtCore.Signal]
    animationRemoved: ClassVar[QtCore.Signal]
    addedToChannelList: ClassVar[QtCore.Signal]
    def __init__(self, parent: QtWidgets.QWidget | None, show_slider: bool = ...) -> None: ...
