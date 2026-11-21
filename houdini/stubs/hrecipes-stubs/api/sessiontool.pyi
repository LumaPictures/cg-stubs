# Houdini stubs generated from Houdini 22.0.466

import hou
from .. import rtypes as rtypes
from hrecipes.api.reciperef import ToolRef as ToolRef

class SessionTool:
    """
    A class to handle session tool generation for recipes.

    Tool Recipe contains tool information under 'tool' key inside the recipe_data, and
    they use that to create their own session tools.

    Node Recipes by design do not store their own tool in the recipe_data. They do not need to launch from
    a session tool, they are presets, and their place is in the OPMenu and the ParmDonutMenu.

    However, you can set a node or param preset recipe to be the permanent default. This will 'ophide' the original
    tool for the node type from the tab menu, and replaces it with a new tool that places down the node type
    with the properties given in the recipe.

    For example, you have a Node Preset Recipe for a Box Sop, called 'Large Box' that has the Uniform Scale set to 10.
    When you pick this Node Preset to be the permanent default, 'Box (Large Box)' will replace the 'Box' tab entry.
    Any new box you create with this tool will be set to have its Uniform Scale to 10.
    """
    def __init__(self) -> None: ...
    def destroyTool(self) -> None: ...
    def destroyClones(self) -> None: ...
    def hasTool(self) -> bool: ...
    def hasClones(self) -> bool: ...
    def __bool__(self) -> bool: ...

class TabSessionTool(SessionTool):
    """
    Handles session tools created for the TAB menu.
    """
    tool_type: rtypes.ToolType
    def __init__(self) -> None: ...
    def cloneTool(self, node_type: hou.NodeType, name: str, title: str) -> bool:
        """Find an existing session tool and clone it for a node or parameter preset recipe.
        Several of our tools, like hou.shelves.tool('sop_box') for Sop/box node type are used in different contexts,
        in SOP and OBJ. In those cases, one we must clone one tool for the SOP context that uses the recipe tool,
        and we must clone one tool identical to the original that only applies to OBJ context. """
    def createTool(self, ref: ToolRef) -> None:
        """
        Creates a tool that will be placed on the TAB menu.
        """

class ShelfSessionTool(SessionTool):
    """
    Handles session tools created for the TAB menu.
    """
    tool_type: rtypes.ToolType
    def __init__(self) -> None: ...
    def placeToolOnShelf(self, shelf_tab: str, ordering_index: float) -> None:
        """
        This will rebuild the tools in order on a shelf so that this tool can be inserted given by the ordering index.
        """
    def createTool(self, ref: ToolRef) -> None:
        """
        Creates a tool that will be placed on the shelf tab.
        """
