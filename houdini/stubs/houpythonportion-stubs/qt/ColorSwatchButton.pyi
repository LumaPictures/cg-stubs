import hou
from hutil.Qt import QtCore, QtGui, QtWidgets
from typing import ClassVar

class ColorSwatchButton(QtWidgets.QPushButton):
    '''
hou.qt.ColorSwatchButton

A button used for selecting colors with the Houdini look and feel.

When clicked, the button opens a Houdini color picker dialog.

This class inherits from Qt\'s QtWidgets.QPushButton class.

ENUMS

    POSITION

        This enumeration specifies where on the colour swatch to show
        the secondary color.


        PositionOff
            Don\'t show on the swatch.

        PositionTop
            Show at the top of the swatch.

        PositionBottom
            Show at the bottom of the swatch.

        PositionLeft
            Show at the left of the swatch.

        PositionRight
            Show at the right of the swatch.

        PositionAll
            Fille the whole sdwatch.

SIGNALS


    colorChanged(QtGui.QColor)
        This signal is emitted when the color in the swatch button has
        changed.

EXAMPLES

    This example demonstrates creating a color swatch button and hooking
    it to a callback function that is invoked when the color changes in
    the Houdini color picker dialog:

  > 
  > def onColorSelected(color):
  >     print("Selected color:", color)
  > 
  > color_chooser_btn = hou.qt.ColorSwatchButton()
  > color_chooser_btn.setSecondaryColorPosition(color_chooser_btn.PositionBottom)
  > color_chooser_btn.colorSelected.connect(onColorSelected)

'''
    includeAlpha: bool
    COLOR_BOX_MARGIN_SIZE: int
    COLOR_BOX_COIRNER_RADIUS: int
    HIGHLIGHT_BOX_OUTSET_SIZE: int
    selectColorDragMode: bool
    colorBoxRect: QtCore.QRect
    selectedColorBoxRect: QtCore.QRect
    secondaryColorBoxRect: QtCore.QRect
    selectedColorBoxPath: QtGui.QPainterPath
    secondaryColorBoxPath: QtGui.QPainterPath
    highlightBoxPath: QtGui.QPainterPath
    __module__: str
    PositionOff: int
    PositionTop: int
    PositionBottom: int
    PositionLeft: int
    PositionRight: int
    PositionAll: int
    colorChanged: ClassVar[QtCore.Signal]
    def __init__(self, include_alpha: bool = False) -> None:
        """
__init__(self, include_alpha=False)

    Create and return a new ColorSwatchButton object.


    include_alpha
        If True, then an alpha component is added to the color swatch
        button.

"""
    def color(self) -> QtGui.QColor:
        """
color(self) -> QtGui.QColor

    Return the button's current color.

"""
    def setColor(self, color: QtGui.QColor) -> None:
        """
setColor(self, color)

    Set the button's current color.


    color
        QtGui.QColor object of the desired color.

"""
    def secondaryColor(self) -> QtGui.QColor: ...
    def setSecondaryColor(self, color: QtGui.QColor) -> None: ...
    def secondaryColorPosition(self) -> int: ...
    def setSecondaryColorPosition(self, position: int) -> None: ...
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None: ...
    def hasAlpha(self) -> bool: ...
    def paintEvent(self, e: QtGui.QPaintEvent) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None: ...
