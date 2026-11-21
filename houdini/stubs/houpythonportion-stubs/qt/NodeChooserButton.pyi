# Houdini stubs generated from Houdini 22.0.466

import hou
from hutil.Qt import QtCore, QtWidgets
from typing import ClassVar

class NodeChooserButton(QtWidgets.QToolButton):
    '''
hou.qt.NodeChooserButton

A button with the Houdini look and feel that opens the Houdini node
chooser dialog when clicked.

This class inherits from Qt\'s QtWidgets.QToolButton class.

SIGNALS


    nodeSelected(hou.Node)
        This signal is emitted when a selection is made in the node
        chooser dialog.

    nodePathsSelected(str)
        This signal is emitted when a selection is made in the node
        chooser dialog. The signal\'s argument is a string of semi-column
        separated paths. The paths can be relative paths if the button
        has a valid relative_to_node and the user turns on Export
        Relative Paths in the dialog. Otherwise, the paths are absolute.

    chooserStarted()
        This signal is emitted before the chooser dialog is opened.

EXAMPLES

    This example demonstrates creating a chooser button for SOP nodes
    and hooking it to a callback function that is invoked when a node is
    selected from the chooser dialog:

  > 
  > def onNodeSelected(node_path):
  >     print("Selected node:", node_path)
  > 
  > node_chooser_btn = hou.qt.NodeChooserButton()
  > node_chooser_btn.setNodeChooserFilter(hou.nodeTypeFilter.Sop)
  > node_chooser_btn.nodeSelected.connect(onNodeSelected)

'''
    relative_to_node: hou.Node | None
    initial_node: hou.Node | None
    node_filter: hou.EnumValue[hou.nodeTypeFilter]
    select_multiple: bool
    __module__: str
    nodeSelected: ClassVar[QtCore.Signal]
    nodePathsSelected: ClassVar[QtCore.Signal]
    chooserStarted: ClassVar[QtCore.Signal]
    def __init__(self) -> None:
        """
__init__(self)

    Create and return a new NodeChooserButton object.

"""
    def setNodeChooserRelativeToNode(self, relative_to_node: hou.Node | None) -> None:
        """
setNodeChooserRelativeToNode(self, relative_to_node)

    Set the reference node to use in the node chooser dialog. This will
    cause the Use Relative Paths checkbox in the dialog to be set. Node
    paths returned by the node chooser dialog will be relative to the
    reference node when the checkbox is set.

    relative_to_node must be a hou.OpNode object.

    If no reference node is set or if the Use Relative Paths checkbox is
    not set then returned paths will be absolute.

"""
    def setNodeChooserInitialNode(self, initial_node: hou.Node | None) -> None:
        """
setNodeChooserInitialNode(self, initial_node)

    Set the node that is initially selected when the node chooser dialog
    is opened.

    initial_node must be a hou.OpNode object.

"""
    def setNodeChooserFilter(self, node_filter: hou.EnumValue[hou.nodeTypeFilter]) -> None:
        """
setNodeChooserFilter(self, node_filter)

    Set the node type filter used by the node chooser dialog.

    node_filter must be a hou.nodeTypeFilter enumerated value.

"""
    def setSelectMultiple(self, value: bool) -> None:
        """
setSelectMultiple(self, value)

    Set if multiple nodes should be selectable with the chooser dialog.

"""
