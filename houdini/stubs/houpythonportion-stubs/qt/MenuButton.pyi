# Houdini stubs generated from Houdini 22.0.466

from hutil.Qt import QtWidgets

class MenuButton(QtWidgets.QPushButton):
    """
hou.qt.MenuButton

A button with the Houdini look and feel that opens a drop-down menu when
clicked.

This class inherits from Qt's QtWidgets.QPushButton class.

"""
    __module__: str
    def __init__(self, menu: QtWidgets.QMenu) -> None:
        """
__init__(self, menu)

    Create and return a new button with the given menu attached to the
    button.

    menu must be a QtWidgets.QMenu object.

"""
