# Houdini stubs generated from Houdini 22.0.466

import hou

from typing import TypeAlias
from typing import TypeAlias
_Parms: TypeAlias = str | hou.Parm | hou.ParmTuple | list[str] | list[hou.Parm] | list[hou.ParmTuple] | list[str | hou.Parm | hou.ParmTuple]
def autoPlaceNodes(self: hou.NetworkEditor) -> bool:
    """
autoPlaceNodes(self) -> bool

    This method is deprecated in the new network editor and always
    returns False.

"""
def autoScrollNodes(self: hou.NetworkEditor) -> bool:
    """
autoScrollNodes(self) -> bool

    This method is deprecated in the new network editor and always
    returns False.

"""
def listMode(self: hou.NetworkEditor) -> bool:
    """
listMode(self) -> bool

    Return True if the network editor is in list mode and False
    otherwise.

"""
def setListMode(self: hou.NetworkEditor, list_mode: bool) -> None:
    """
setListMode(self, on)

    Set the network editor to enter list mode if on is True and to exit
    list mode if on is False.

"""
def selectPosition(self: hou.NetworkEditor, input_node: hou.NetworkMovableItem | None = None, output_index: int = 0, output_node: hou.NetworkMovableItem | None = None, input_index: int = 0) -> hou.Vector2 | None:
    '''
selectPosition(self, input_node=None, output_index=0, output_node=None,
input_index=0) -> hou.Vector2

    This method wraps a call to hou.NetworkEditor.pushEventContext, with
    the event context set to \'nodegraphselectpos\', and appropriate
    context data to give behavior similar to the old network editor.

    Prompt the user to select a position in the network editor for a new
    node to be placed. The network editor visualizes the position with a
    dotted outline of a node placeholder. The user can then move the
    mouse to change the position and [LMB] to confirm. The user can also
    press [Esc] instead to cancel the selection.

    You can optionally pass in hou.Node objects to the input_node and
    output_node arguments to visualize the node placeholder with
    connections to the specified input and output nodes.

    Return a hou.Vector2 containing the x,y coordinates of the selected
    position.

    Raise hou.OperationInterrupted if the user canceled the selection.
    Raise hou.OperationFailed if the network editor is in list mode.

    This method can be useful for scripts that create new nodes and
    prompts for node positions. Here is an example:

  > 
  > # Get the input and output nodes that the new node will connect to.
  > input_node = hou.node("/obj/myInput")
  > output_node = hou.node("/obj/myOutput")
  > 
  > # Set the new node to connect to the first output of the input node
  > # and the second input of the output node.
  > output_index = 0
  > input_index = 1
  > 
  > # Get the network editor.
  > network_editor = hou.ui.curDesktop().paneTabOfType(
  >     hou.paneTabType.NetworkEditor)
  > 
  > # Prompt the user to select a position for the new node.
  > position = network_editor.selectPosition(
  >     input_node, output_index, output_node, input_index)
  > 
  > # Create the new node.
  > new_node = hou.node("/obj").createNode("geo")
  > 
  > # Position the new node and wire it to the input and output nodes.
  > new_node.move(position)
  > new_node.setInput(0, input_node, output_index)
  > output_node.setInput(input_index, new_node, 0)
'''
def selectItems(self: hou.NetworkEditor, prompt_message: str, clear_selected: bool = True) -> tuple[hou.NetworkMovableItem, ...]: ...
def homeToSelection(self: hou.NetworkEditor) -> None:
    """
homeToSelection(self)

    Centers the nodes within the network editor to show the current
    selection. This method wraps a call to
    hou.NetworkEditor.setVisibleBounds.

"""
def frameSelection(self: hou.NetworkEditor) -> None:
    """
frameSelection(self)

    Centers the nodes within the network editor to show the current
    selection and zooms to its extents. This method wraps a call to
    hou.NetworkEditor.setVisibleBounds.

"""
def insertIntoUnderlyingConnections(self: hou.NetworkEditor, node: hou.Node, x: float, y: float) -> None:
    """
    insertIntoUnderlyingConnections(self, node, x, y)

        This method is deprecated in the new network editor and does
        nothing.

    """
def autoAddToNetbox(self: hou.NetworkEditor, node: hou.Node) -> None:
    """
autoAddToNetbox(self, node)

    This method is deprecated in the new network editor and does
    nothing.

"""
def modifyPositionForNode(self: hou.NetworkEditor, pos: hou.Vector2, node: hou.Node) -> hou.Vector2:
    """
modifyPositionForNode(self, vector2, node) -> Vector2

    This method is deprecated in the new network editor, and simply
    returns the position passed into the function.

"""
def parmScrollTo(self: hou.NetworkEditor, parms: _Parms, scroll_pos: hou.EnumValue[hou.scrollPosition] = ...) -> None:
    """
parmScrollTo(self, parms, scroll_pos)

    Adjust the Parameter Editor vertical scroll bar to align one or more
    parameters using hou.scrollPosition mode.

    The parms argument can be a list or a single str, hou.Parm or
    hou.ParmTuple. The types can also be mixed in the list. If an entry
    is a str, you can pass a comma seperated list of parameter names but
    wildcards are not supported.

    The scroll_pos argument defines how to align the vertical bounding
    box of the affected parameters. See hou.scrollPosition.

"""
def parmMoveFocusTo(self: hou.NetworkEditor, parm: str | hou.Parm | hou.ParmTuple) -> None:
    """
parmMoveFocusTo(self, parm)

    Try to move keyboard focus to the specified parameter in the
    Parameter Editor.

"""
