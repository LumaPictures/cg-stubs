# Houdini stubs generated from Houdini 22.0.466

import hou
from PySide6 import QtCore, QtWidgets as QtWidgets

def qtScreenGeometry(self: hou.Pane) -> QtCore.QRect:
    """
qtScreenGeometry(self) -> QRect

    Return the geometry of the pane as a PySide6.QtCore.QRect object.
    The x and y properties of the returned QRect object point to the
    top-left corner of the pane in screen coordinates.

"""
def qtParentWindow(self: hou.Pane) -> QtWidgets.QWidget | None:
    """
qtParentWindow(self) -> QWidget

    Return a PySide6.QtWidgets.QWidget instance that represents the
    window containing the pane.

"""
