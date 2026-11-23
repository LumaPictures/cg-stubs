import hou
from hutil.Qt import QtCore as QtCore, QtGui, QtWidgets

class ColorField(QtWidgets.QWidget):
    """
hou.qt.ColorField

A widget for color input.

The widget contains a color swatch button and an input field for RGBA
values.

This class inherits from Qt's QtWidgets.QWidget class.

"""
    colorSwatchButton: hou.qt.ColorSwatchButton
    colorChanged: QtCore.SignalInstance
    inputField: hou.qt.InputField
    __module__: str
    def __init__(self, label: str | None = '', include_alpha: bool = False) -> None:
        '''
__init__(self, label="", include_alpha=False)

    Create and return a new ColorField object.


    label
        If set to a non-empty string then a label is added to the color
        field.

    include_alpha
        If True, then an alpha component is added to the color field.

'''
    def color(self) -> QtGui.QColor:
        """
color() -> QtGui.QColor

    Return the field's current color.

"""
    def setColor(self, color: QtGui.QColor) -> None:
        """
setColor(color)

    Set the field's current color. color must be a QtGui.QColor object.

"""
