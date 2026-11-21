# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import hou
from collections.abc import Sequence
from hutil.Qt import QtWidgets
from typing import ClassVar

class ParmTupleChooserButton(QtWidgets.QToolButton):
    '''
hou.qt.ParmTupleChooserButton

A button with the Houdini look and feel that opens the Houdini node
chooser dialog when clicked.

This class inherits from Qt\'s QtWidgets.QToolButton class.

SIGNALS


    parmTupleSelected(str)
        This signal is emitted when a selection is made in the node
        chooser dialog.

EXAMPLES

    This example demonstrates creating a chooser button for parm tuples
    and hooking it to a callback function that is invoked when a
    parameter is selected from the chooser dialog:

  > 
  > def onSelected(parmtuple_path):
  >     print("Selected parm tuple:", parmtuple_path)
  > 
  > node_chooser_btn = hou.qt.ParmTupleChooserButton()
  > node_chooser_btn.parmTupleSelected.connect(onSelected)

'''
    relative_to_node: hou.OpNode | None
    initial_selection: Sequence[str]
    category_filter: hou.NodeTypeCategory | None
    select_multiple: bool
    __module__: str
    parmTupleSelected: ClassVar[PySide6.QtCore.Signal]
    def __init__(self) -> None:
        """
__init__(self)

    Create and return a new ParmTupleChooserButton object.

"""
    def setRelativeToNode(self, relative_to_node: hou.OpNode | None) -> None:
        """
setRelativeToNode(self, relative_to_node)

    Set the reference node to use in the node chooser dialog. This will
    cause the Use Relative Paths checkbox in the dialog to be set. Node
    paths returned by the node chooser dialog will be relative to the
    reference node when the checkbox is set.

    relative_to_node must be a hou.OpNode object.

    If no reference node is set or if the Use Relative Paths checkbox is
    not set then returned paths will be absolute.

"""
    def setInitialSelection(self, initial_selection: Sequence[str]) -> None:
        """
setInitialSelection(self, initial_selection)

    Set the node that is initially selected when the node chooser dialog
    is opened.

    initial_selection must be a hou.OpNode object.

"""
    def setCategoryFilter(self, category_filter: hou.NodeTypeCategory | None) -> None:
        """
setCategoryFilter(self, category_filter)

    Set the node type filter used by the node chooser dialog.

    category_filter must be a hou.NodeTypeCategory.

"""
    def setSelectMultiple(self, value: bool) -> None:
        """
setSelectMultiple(self, value)

    Set if multiple nodes should be selectable with the chooser dialog.

"""
