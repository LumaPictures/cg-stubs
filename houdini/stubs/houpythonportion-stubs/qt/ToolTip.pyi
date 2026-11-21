# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import PySide6.QtWidgets
import hou
from hutil.Qt import QtWidgets

class ToolTip(QtWidgets.QWidget):
    '''
hou.qt.ToolTip

A tooltip window with the Houdini look and feel that can be used for
hover tooltips.

This class inherits from Qt\'s QtWidgets.QWidget class.

EXAMPLES

    This example demonstrates creating a tooltip window and attaching it
    to a button:

  > 
  > tooltip = hou.qt.ToolTip()
  > tooltip.setTitle("Tooltip Example - SOP Torus Help")
  > tooltip.setText("This tooltip links to the SOP Torus help page.")
  > tooltip.setHotkey("Shift+H")
  > tooltip.setHelpUrl("/nodes/sop/torus")
  > 
  > btn = QtWidgets.QPushButton("Hover Me")
  > tooltip.setTargetWidget(btn)

'''
    targetWidget: PySide6.QtWidgets.QWidget | None
    titleWidget: PySide6.QtWidgets.QLabel
    separator: hou.qt.Separator
    textWidget: PySide6.QtWidgets.QLabel
    hotkeyWidget: PySide6.QtWidgets.QLabel
    extraHelpIconWidget: PySide6.QtWidgets.QLabel
    extraHelpTextWidget: PySide6.QtWidgets.QLabel
    helpHotkey: str
    helpUrl: str
    __module__: str
    def __init__(self) -> None:
        """
__init__(self)

    Create and return a new tooltip window.

"""
    def __del__(self) -> None: ...
    def setTitle(self, title: str) -> None:
        """
setTitle(self, title)

    Set the tooltip's title. The title appears at the top of the window.
    If no title is set then the tooltip window does not display the
    title area.

"""
    def setText(self, text: str) -> None:
        """
setText(self, text)

    Set the tooltip's main text.

"""
    def setHotkey(self, hotkey: str) -> None:
        """
setHotkey(self, hotkey)

    Sets a hotkey to display in the tooltip.

    hotkey must be a key sequence such as G, Shift+G or Cmd+G.

"""
    def setHelpUrl(self, help_url: str) -> None:
        """
setHelpUrl(self, help_url)

    Link the tooltip to the given help web page. When a help URL is set
    then the user can press F1 while the tooltip is visible to open the
    help web page.

    help_url can be either a fully qualified URL or a Houdini help path.
    For example, passing in /nodes/sop/torus as the help URL will cause
    the tooltip window to open the SOP Torus help page when F1 is
    pressed.

"""
    def setTargetWidget(self, widget: PySide6.QtWidgets.QWidget | None) -> None:
        """
setTargetWidget(self, widget)

    Sets the widget that the tooltip is attached to. When the cursor is
    hovered over the target widget then the tooltip window is opened.
    And when the cursor is moved outside of the target widget's area
    then the tooltip window is closed.

    Setting the target widget will cause the tooltip to detach itself
    from any previous target widget.

"""
    def eventFilter(self, obj: PySide6.QtCore.QObject, event: PySide6.QtCore.QEvent) -> bool: ...
