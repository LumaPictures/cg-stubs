# Houdini stubs generated from Houdini 22.0.466

from PySide6 import QtGui as QtGui
from hutil.Qt import QtWidgets

class ComboBox(QtWidgets.QComboBox):
    """
hou.qt.ComboBox

A non-scrollable combo box (menu button and menu) with the Houdini look
and feel.

This class inherits from Qt's QtWidgets.QComboBox class.

"""
    __module__: str
    def __init__(self) -> None:
        """
__init__(self)

    Create and return a new ComboBox object.

"""
    def wheelEvent(self, event: QtGui.QWheelEvent) -> None: ...
