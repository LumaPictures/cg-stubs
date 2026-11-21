from typing import Self
from PySide6 import QtGui as QtGui
from houpythonportion.qt.__utils__ import wrapQtGuiObject as wrapQtGuiObject

class Icon(QtGui.QIcon):
    """
hou.qt.Icon

An icon generated from a Houdini icon name.

This class inherits from Qt's QtGui.QIcon class.

"""
    __module__: str
    @staticmethod
    def __new__(cls, icon_name: str, width: int | None = None, height: int | None = None, device_pixel_ratio: float = 1.0, accent_color_name: str | None = None, tint_color_name: str | None = None) -> Self:
        """
__init__(self, icon_name, width=None, height=None)

    Create and return a new icon for the specified Houdini icon name.

    You can discover Houdini icons using the Houdini file chooser dialog
    and diving into the hicon:// path. The name of the icon file without
    the .svg extension is the icon's name. For example, the icon name
    for hicon://SVGIcons.index/BUTTONS_help.svg is BUTTONS_help.

"""
