from typing import Self
import hou
from PySide6 import QtWidgets
from houpythonportion.qt.__utils__ import wrapQtGuiObject as wrapQtGuiObject
from typing import SupportsInt

class _ParmDialogWidget(QtWidgets.QWidget):
    """The QWidget that ParmDialog() returns, with ParmDialog's methods bound onto it."""
    ptr: SupportsInt
    def setNode(self, node: hou.OpNode | None) -> None: ...
    def node(self) -> hou.OpNode | None: ...
    def _getValueNames(self) -> tuple[str, ...]: ...
    def _getValue(self, name: str) -> str: ...
    def _setValue(self, name: str, value: str) -> bool: ...
    def _pressButton(self, name: str) -> bool: ...
    def setScrollPosition(self, pos: hou.Vector2) -> None: ...
    def scrollPosition(self) -> hou.Vector2: ...
    def _scrollToParms(self, parms: str) -> None: ...
    def _filterParms(self, parms: str) -> None: ...
    def _filterParmFolders(self, parms: str) -> None: ...
    def setMultiParmTab(self, parm: str, index: int) -> None: ...
    def multiParmTab(self, parm: str) -> int: ...
    def visibleParms(self) -> tuple[hou.ParmTuple, ...]: ...

class ParmDialog(_ParmDialogWidget):
    """
hou.qt.ParmDialog

A Houdini parameters dialog.

This class inherits from Qt's QtWidgets.QWidget class.

"""
    __module__: str
    @staticmethod
    def __new__(cls, the_node: hou.OpNode | None, showTitleBar: bool = False, compact: bool = False, labelsize: float = -1.0) -> Self:
        """
__init__(self, node, showTitleBar, compact, labelsize)

    Create and return a Houdini parameters dialog.


    node
        Must be set to the hou.OpNode object from which to get the
        parameters.

    showTitleBar
        Show the Parameter Editor Title Bar. Defaults to False.

    compact
        Create a parameter editor with smaller trailing and leading
        space for parameters. Defaults to False.

    labelsize
        Override the parameter label size in inches. A value of -1.0
        means to use the default label size. Defaults to -1.0.

"""
