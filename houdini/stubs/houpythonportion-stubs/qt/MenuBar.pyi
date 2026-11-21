from hutil.Qt import QtWidgets

IS_NEW_UI: bool

class MenuBar(QtWidgets.QMenuBar):
    """
hou.qt.MenuBar

A menubar with the Houdini look and feel.

This class inherits from Qt's QtWidgets.QMenuBar class.

"""
    __module__: str
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        """
__init__(self, parent=None)

    Create and return a new menubar.

    If parent is None, then the menu bar is parentless and becomes a
    window. If parent is a QWidget object, then the menu bar becomes a
    child of the object.

"""
