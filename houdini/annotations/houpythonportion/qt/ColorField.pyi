from PySide6 import QtCore, QtGui, QtWidgets

import hou

class ColorField(QtWidgets.QWidget):
    colorSwatchButton: hou.qt.ColorSwatchButton
    colorChanged: QtCore.SignalInstance
    inputField: hou.qt.InputField
    def __init__(self, label: str | None = ..., include_alpha: bool = ...) -> None: ...
    def color(self) -> QtGui.QColor: ...
    def setColor(self, color: QtGui.QColor) -> None: ...
