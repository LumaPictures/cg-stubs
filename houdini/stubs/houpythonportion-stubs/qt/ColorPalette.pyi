# Houdini stubs generated from Houdini 22.0.466

import hou
import layout
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
from collections.abc import Sequence
from hutil.PySide import QtWidgets
from typing import ClassVar

default_colors: tuple[PySide6.QtGui.QColor, ...]

class ColorPalette(QtWidgets.QFrame):
    '''
hou.qt.ColorPalette

A convenient widget for quick olor selection from a small palette of
colors.

OVERVIEW

    Sometimes, you want to allow users to choose a color from a list of
    predefined colors, without burdening them with the requirement to
    specify their own custom color each time. For example, when tagging
    items in a user interface with different colors to keep them
    organized.

    This widget lets you specify a list of colors, and have the user
    select from that list, with the optional ability to edit the colors.

    This object works two ways:

  * You can use it as a pop-up window, where a palette window pops open,
    the user clicks a color, and the palette window disappears.

  * Or, you can embed it as a regular Qt widget in a widget layout. This
    would be useful, for example, in a preferences window, where you
    want to provide a palette from which to pick a color for something.

USING COLORPALETTE AS A POPUP

    The color palette is non-modal. Once you open it, your script
    continues to run, and you have to use signals to get feedback on how
    the user interacts with the palette.

  > class MyWindow(QtWidgets.QDialog):
  >     def __init__(self, parent=None):
  >         super(MyWindow, self).__init__(parent)
  > 
  >         self._colors = [
  >             QtGui.QColor(255, 0, 0),
  >             QtGui.QColor(0, 255, 0),
  >             QtGui.QColor(0, 0, 255),
  >             QtGui.QColor(255, 255, 0),
  >             QtGui.QColor(255, 0, 255),
  >             QtGui.QColor(0, 255, 255),
  >             QtGui.QColor(255, 128, 0),
  >             QtGui.QColor(255, 255, 255),
  >             QtGui.QColor(0, 0, 0),
  >         ]
  > 
  >         self._palette = ColorPalette(self._colors)
  >         self._palette.colorSelected.connect(self._chose_color)
  > 
  >         layout = QtWidgets.QVBoxLayout()
  >         self.setLayout(layout)
  > 
  >         self._label = QtWidgets.QLabel("No color")
  >         layout.addWidget(self._label)
  >         self._button = QtWidgets.QPushButton("Choose")
  >         self._button.clicked.connect(self._palette.show)
  >         layout.addWidget(self._button)
  > 
  >     def _chose_color(self, ix, color):
  >         msg = "Color #{}, R: {}, G: {}, B: {}".format(
  >             ix, color.red(), color.green(), color.blue()
  >         )
  >         self._label.setText(msg)

    NOTE
        Remember that you must have at least one persistent reference to
        the widget, otherwise the window will be garbage collected and
        immediately close.

EMBEDDING COLORPALETTE AS A WIDGET IN A QT LAYOUT

    You can simply use ListEditor as a widget, and use signals to react
    when users interact with the palette.

  > class MyWindow(QtWidgets.QDialog):
  >     def __init__(self, parent=None):
  >         super(MyWindow, self).__init__(parent)
  > 
  >         self._colors = [
  >             QtGui.QColor(255, 0, 0),
  >             QtGui.QColor(0, 255, 0),
  >             QtGui.QColor(0, 0, 255),
  >             QtGui.QColor(255, 255, 0),
  >             QtGui.QColor(255, 0, 255),
  >             QtGui.QColor(0, 255, 255),
  >             QtGui.QColor(255, 128, 0),
  >             QtGui.QColor(255, 255, 255),
  >             QtGui.QColor(0, 0, 0),
  >         ]
  > 
  >         layout = QtWidgets.QVBoxLayout()
  >         self.setLayout(layout)
  > 
  >         self._label = QtWidgets.QLabel("No color")
  >         layout.addWidget(self._label)
  > 
  >         self._palette = ColorPalette(self._colors, size=24)
  >         self._palette.colorSelected.connect(self._chose_color)
  >         self._palette.colorEdited.connect(self._edited_color)
  >         layout.addWidget(self._palette)
  > 
  >     def _chose_color(self, ix, color):
  >         msg = "Color #{}, R: {}, G: {}, B: {}".format(
  >             ix, color.red(), color.green(), color.blue()
  >         )
  >         self._label.setText(msg)

SWATCH LAYOUT

  * The size of the widget is derived from the swatch size (the size
    argument to the initializer) and the number of colors in the
    palette.

  * By default, the palette will try to lay out the swatches in as close
    to a square as possible.

  * If there aren\'t enough colors to fill the layout, swatches can be
    empty.

  * If you specify a columns argument to the initializer, the widget
    will only allow that number of columns, with swatches going down to
    create more rows.

  * If you specify a rows argument to the initializer, the widget will
    only allow that number of rows, with swatches going across to create
    more columns.

  * If you specify both rows and columns, the layout will have exactly
    that number of rows and columns, even if this means you can\'t see
    all the colors in the color list.

  * By default colors in the list are ordered by filling up the first
    row left to right, then second row, and so on. If you pass
    by_column=True to the initializer, the widget will instead order the
    colors by filling in the first column top to bottom, then the second
    column, and so on.

ALLOWING THE USER TO EDIT COLORS

    By default, the user can Alt-click a color in the palette to edit
    that swatch\'s color value. When the user accepts the edited color
    (that is, doesn\'t cancel the edit operation), the widget emits a
    colorEdited signal.

    Note that the edited palette is kept in the ColorPalette object. If
    you want to persist the palette between uses of different
    ColorPalette objects, or across sessions, you will need to do that
    yourself.

    To prevent the user from editing colors, pass allow_editing=False
    when you create the widget, or call setEditingAllowed(False) on the
    widget.

BACKGROUND COLORS

  * By default, the background of the widget is filled with the default
    window background from the current palette. You can pass a bg_color
    to the initializer to specify a custom color (or brush).

  * Empty swatches are painted with a special brush. The default brush
    draws dark or light diagonal lines. You can pass an empty_color to
    the initializer to specify a custom color (or brush) for empty
    squares.

TIPS AND NOTES

  * The colors in the list may be QBrush objects, not just QColor
    objects. You could use QBrush objects to set gradients, patterns,
    and textures as swatches in the palette instead of or alongside
    plain colors.

SIGNALS


    paletteChanged()
        Triggered when the entire palette is replaced by setColorList().

    colorEdited(index: int, old: QColor, new: QColor)
        Triggered when the user manually edits one of the colors (see
        color editing above).

    colorSelected(index: int, color: QColor)
        Triggered when the user selects a color in the palette. The
        signal can be triggered multiple times by the user dragging over
        different colors, or if you have embedded the widget in a layout
        so users can change the color selection as many times as they
        want. If you only want to react when the user chooses a color
        from a popup and the popup closes, use the colorAccepted signal
        instead.

    colorAccepted(index: int, color: QColor)
        Only triggered when the user releases the mouse button on a
        color in a popup and the popup closes.

    colorCancelled()
        Triggered if the user closes the popup without choosing a valid
        color, for example by clicking outside the popup, or clicking an
        empty space.

'''
    __module__: str
    paletteChanged: ClassVar[PySide6.QtCore.Signal]
    colorEdited: ClassVar[PySide6.QtCore.Signal]
    colorSelected: ClassVar[PySide6.QtCore.Signal]
    colorAccepted: ClassVar[PySide6.QtCore.Signal]
    colorCancelled: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, colors: Sequence[PySide6.QtGui.QColor] | None = None, size: int = 32, by_column: bool = False, show_at_pointer: bool = True, columns: int | None = None, rows: int | None = None, allow_editing: bool = True, selected_index: int = -1, bg_color: PySide6.QtGui.QColor | None = None, empty_color: PySide6.QtGui.QColor | None = None, parent: PySide6.QtWidgets.QWidget | None = None) -> None:
        """
__init__(self, colors=None, size=32, by_column=False,
show_at_pointer=True, columns=None, rows=None, allow_editing=True,
selected_index=-1, bg_color=None, empty_color=None, parent=None)


    colors
        A list of QColor (or QBrush) objects that the user can choose
        from. If you don't supply this argument, the widget uses a
        default 16-color palette.

    size
        The size, in pixels, or individual swatches (color squares) in
        the palette.

    by_column
        If True, lay out the colors column-by-column, instead of row-by-
        row.

    show_at_pointer
        If this is True (the default), when you call show() the popup
        window will automatically center itself under the mouse pointer.

    columns
        The maximum number of columns of swatches to show.

    rows
        The maximum number of rows of swatches to show.


    NOTE
        If you specify both rows and columns, the layout will have a
        fixed number of squares, and if the fixed count is less than the
        number of colors in the color list, some colors will not be
        shown.


    allow_editing
        Allow the user to Alt-click a color swatch to change the color
        value in that space.

    selected_index
        If you pass this integer argument, the color at this position in
        the color list will already be selected when the widget appears.

    bg_color
        Allows you to specify a custom background color (or brush) for
        the widget.

    empty_color
        Allows you to specify a custom color (or brush) for empty
        squares in the palette.

    parent
        A QWidget to set as this widget's parent. If you don't supply
        this argument, the widget automatically uses Houdini's main
        window as the parent.

"""
    def colorCount(self) -> int: ...
    def colorList(self) -> list[PySide6.QtGui.QColor]:
        """
colorList() -> list

    Returns the list of colors used to create the palette.

"""
    def setColorList(self, colors: Sequence[PySide6.QtGui.QColor]) -> None:
        """
setColorList(colors)

    Replaces the current color list with a new list. The items in the
    list must be QColor or QBrush objects.

"""
    def setColor(self, ix: int, color: PySide6.QtGui.QColor) -> None:
        """
setColor(n, color)

    Sets the nth color in the color list to the given QColor (or
    QBrush).

"""
    def color(self, ix: int) -> PySide6.QtGui.QColor: ...
    def swatchSize(self) -> int:
        """
swatchSize() -> int

    The size (in pixels) of the individual swatches (color squares) in
    the palette. The overall size of the palette is computed from this
    value and the colorCount().

"""
    def setSwatchSize(self, size: int) -> None:
        """
setSwatchSize(size)

    Sets the size (in pixels) of the individual swatches (color squares)
    in the palette.

"""
    def isEditingAllowed(self) -> bool:
        """
isEditingAllowed() -> bool

    Returns True if the user can alt-click a color to edit it.

"""
    def setEditingAllowed(self, allowed: bool) -> None:
        """
setEditingAllowed(allow)

    Pass True to allow the user to alt-click a color to edit it, or
    False to prevent the user from editing colors.

"""
    def selectedIndex(self) -> int:
        """
selectedIndex() -> int

    Returns the index of the selected color in the current color list.

"""
    def setSelectedIndex(self, ix: int) -> None:
        """
setSelectedIndex(ix)

    Selects the color at the given index.

"""
    def selectedColor(self) -> PySide6.QtGui.QColor | None:
        """
selectedColor() -> QtGui.QColor

    Returns the currently selected color.

"""
    def sizeHint(self) -> PySide6.QtCore.QSize: ...
    def changeEvent(self, event: PySide6.QtCore.QEvent) -> None: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...
    def showEvent(self, event: PySide6.QtGui.QShowEvent) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...
