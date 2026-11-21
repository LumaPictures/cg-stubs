# Houdini stubs generated from Houdini 22.0.466

import hou

def createDefaultStateToolScript(state: hou.ViewerState, nodetypecategory: hou.NodeTypeCategory) -> str:
    """ Returns a string representing a default python script for a tool
        associated with a given state. Each tool has a python script that gets
        executed when the tool is invoked, and in this case the tool script
        will cause the appropriate viewer to enter the given state.
    """
def createDefaultStateTool(shelffile: str, nodetypecategory: hou.NodeTypeCategory, state: hou.ViewerState) -> None:
    """ Generates a default shelf tool for a given state and saves it into
        a given file name. 
    """
def createDefaultStateToolsForCategory(shelfdir: str, nodetypecategory: hou.OpNodeTypeCategory) -> None:
    """ Generates default shelf tools for all the viewer states that exist
        within a given nodetypecategory (i.e., OBJ, SOP, etc.). All these
        tools are saved into a file that corresponds to the category name and
        that is saved in a given directory.
    """
def createDefaultStateTools(shelfdir: str) -> None:
    """ Generates all the shelf tools that correspond to various viewer states.
        The viewer states are grouped according to the node type categories (ie,
        network types, such as OBJ, SOP, POP), and the state tools for all such
        categories are generated and saved in corresponding files within the
        given shelf dir.
        The shelf tools that get generated cause the viewers to enter various
        states, each of which correspons to one shelf tool. These tools can be
        invoked from the top level shelf or from the TAB menus.
    """
