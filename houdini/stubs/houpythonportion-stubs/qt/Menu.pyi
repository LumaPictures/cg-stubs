from typing import Self
from PySide6 import QtWidgets as QtWidgets
from houpythonportion.qt.__utils__ import wrapQtGuiObject as wrapQtGuiObject

class Menu(QtWidgets.QMenu):
    """
hou.qt.Menu

A menu with the Houdini look and feel.

This class inherits from Qt's QtWidgets.QMenu class.

"""
    __module__: str
    @staticmethod
    def __new__(cls) -> Self:
        """
__init__(self)

    Create and return a new menu.

"""
