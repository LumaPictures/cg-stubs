# Houdini stubs generated from Houdini 22.0.466

import hou
from collections.abc import Generator

def createInputNode(self: hou.Node, input_index: int, node_type_name: str, node_name: str | None = None, run_init_scripts: bool = True, load_contents: bool = True, exact_type_name: bool = False) -> hou.Node:
    """
createInputNode(self, input_index, node_type_name, node_name=None,
run_init_scripts=True, load_contents=True, bool exact_type_name=False)

    Create a new node and connect it to one of this node's inputs.
    Return the new node.


    input_index
        The index of this node's input connector.

    node_type_name
        The name of the type of node to create. See the createNode
        method for more information.

    node_name
        See the createNode method for more information.

    run_init_scripts
        See the createNode method for more information.

    load_contents
        See the createNode method for more information.

    exact_type_name
        See the createNode method for more information.

    See also the createOutputNode method.

"""
def createOutputNode(self: hou.Node, node_type_name: str, node_name: str | None = None, run_init_scripts: bool = True, load_contents: bool = True, exact_type_name: bool = False) -> hou.Node:
    """
createOutputNode(self, node_type_name, node_name=None,
run_init_scripts=True, load_contents=True, bool exact_type_name=False)

    Create a new node and connect its first input to this node's (first)
    output. Return the new node.

    See the createNode method for more information on the parameters.

    See also the createInputNode method.

"""
def allNodes(self: hou.Node) -> Generator[hou.Node, None, None]:
    '''
allNodes(self) -> generator of hou.Node

    Recursively return a sequence of all nodes contained in this node
    including this node. This method differs from
    hou.Node.allSubChildren in the following ways:

  * It includes this node in the returned sequence.

  * It does not guarantee a top-down or bottom-up traversal order.

  * The method is a generator and does not return a tuple so it is not
    safe to create or delete nodes while looping through the return
    value.

    Here is an example of printing out the paths for all nodes under
    /obj:

  > root_node = hou.node("/obj")
  > for node in root_node.allNodes():
  >     print node.path()
'''
