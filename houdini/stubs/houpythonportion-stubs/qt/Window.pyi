from typing import Self
import PySide6.QtWidgets
from houpythonportion.qt.__utils__ import wrapQtGuiObject as wrapQtGuiObject

class Window(PySide6.QtWidgets.QWidget):
    """
hou.qt.Window

A generic window with the Houdini look and feel.

This class inherits from Qt's QtWidgets.QWidget class.

"""
    __module__: str
    @staticmethod
    def __new__(cls) -> Self:
        """
__init__(self)

    Create and return a new window.

"""
