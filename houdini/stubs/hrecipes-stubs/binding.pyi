from typing import Any
import hou
from . import rtypes as rtypes, storage as storage, utils as utils
from collections.abc import Mapping
from houtypes import JSONValue, NodeContextMenuKwargs
from typing import Generic, Sequence, TypedDict

from typing import TypeVar
from typing_extensions import TypeVar
_D = TypeVar('_D', default=rtypes._RecipeDataPayload)
class _RecipeDataEntry(TypedDict, Generic[_D]):
    name: str
    label: str
    data: _D

def recipeMenu(node_or_parm: hou.Node | hou.Parm | hou.ParmTuple, recipe_category: rtypes.RecipeCategory | Sequence[rtypes.RecipeCategory], legacy_presets: bool = False, examples_only: bool = False, submenu_filter: str = '', visible: bool = True, valid: bool = True, build_submenus: bool = False, show_last_invoked: bool = False, no_default_entry: bool = False) -> list[str]:
    """Returns menu entries for a node or parameter used to build XML or parameter menus, but in support with submenus
    that can display the last invoked recipe in the submenu. This also lets you set whenever to show parm and/or legacy presets
    alongside node presets.

    :param node_or_parm: The node or parameter tuple to check for menu entries.
    :param recipe_category: The recipe category in which to look for recipes belonging to the node or parameter
    tuple. This could be a single or a list of hrecipes.rtypes.RecipeCategory.
    :param legacy_presets: Whenever to include legacy presets belonging to the node.
    :param examples_only: Whenever to only include the examples belonging to the node.
    :param submenu_filter: Only include entries that are part of this submenu.
    :param visible: Only include recipes that are set visible.
    :param valid: Only include recipes that are passed the validity test for this session.
    :param build_submenus: Whenever to return the entries in a submenu like structure.
    :param show_last_invoked: When build_submenus is True, controls whenever to show the last invoked recipe next to
    the submenu title.
    :param no_default_entry: Adds a 'No Default' entry at the start that is used for permanent defaults.

    TODO: Build Submenus possibly needs to adjusted when we know how to deal with dynamic xml submenus.
    """
def hasRecipe(node_or_parm: hou.Node | hou.ParmTuple, recipe_category: rtypes.RecipeCategory | Sequence[rtypes.RecipeCategory], legacy_presets: bool = False, examples_only: bool = False, name_pattern: str | None = None, submenu_filter: str = '', visible: bool = True, valid: bool = True) -> bool:
    """Returns whenever the node or parameter has any associated Recipe. This will be faster to call than using
    recipeMenu() and check for its output.

    :param node_or_parm: The node or parameter tuple to check for menu entries.
    :param recipe_category: The recipe category in which to look for recipes belonging to the node or parameter
    tuple. This could be a single or a list of hrecipes.rtypes.RecipeCategory.
    :param legacy_presets: Whenever to include legacy presets belonging to the node.
    :param examples_only: Whenever to only include the examples belonging to the node.
    :param submenu_filter: Only include entries that are part of this submenu.
    :param name_pattern: Only include entries that have a matching name to this pattern. The pattern search is based
    on hou.text.patternMatch()
    :param visible: Only include recipes that are visible.
    :param valid: Only include recipes that are passed the validity test for this session.
    """
def canMakeTool(items: Sequence[hou.NetworkMovableItem]) -> bool: ...
def canMakeDecoration(items: Sequence[hou.NetworkMovableItem]) -> bool | Sequence[hou.NetworkMovableItem]: ...
def _showGenericNodeDialog(kind: rtypes.RecipeCategory = ..., items: Sequence[hou.NetworkMovableItem] = ..., central: hou.OpNode | None = None, editor: hou.NetworkEditor | None = None, kwargs: NodeContextMenuKwargs | None = None) -> None: ...
def showParmPresetDialog(parm: hou.Parm | hou.ParmTuple, kwargs: Mapping[str, object] | None = None) -> None: ...
def showNodePresetDialog(node: hou.OpNode, kwargs: Mapping[str, object] | None = None) -> None: ...
def showDecorationDialog(items: Sequence[hou.NetworkMovableItem] = ..., central: hou.OpNode | None = None, editor: hou.NetworkEditor | None = None, kwargs: NodeContextMenuKwargs | None = None) -> None: ...
def showToolDialog(items: Sequence[hou.NetworkMovableItem] = ..., central: hou.OpNode | None = None, editor: hou.NetworkEditor | None = None, kwargs: NodeContextMenuKwargs | None = None) -> None: ...
def showPermanentDefaultDialog(node: hou.OpNode) -> None: ...
def recipeExists(name_pattern: str, recipe_categories: rtypes.RecipeCategory | list[rtypes.RecipeCategory] | tuple[rtypes.RecipeCategory, ...]) -> bool:
    """Returns whenever a recipe is present in the current houdini session.

    :param name_pattern: The internal name of the recipe. Optionally, you can use a pattern
    similar to hou.text.patternMatch().
    :param recipe_categories: The recipe categories in which to look for the recipe.
    """
def recipeNames(recipe_categories: rtypes.RecipeCategory | list[rtypes.RecipeCategory] | tuple[rtypes.RecipeCategory, ...], name_pattern: str | None = None, nodetype_categories: hou.NodeTypeCategory | list[hou.NodeTypeCategory] | tuple[hou.NodeTypeCategory, ...] = ..., include_label: bool = True, pad: bool = True) -> list[str]:
    """Returns a list of available internal recipe names in the houdini session.

    :param recipe_categories: A single recipe category or a tuple of recipe categories in which to search for recipes.
    :param name_pattern: When this is none, it searches all recipes in the given category, otherwise use this to
    match the pattern similarly to hou.text.patternMatch().
    :param nodetype_categories: Provides another filter option as a single node type category or a tuple of node type
    categories. This is useful if you only want to return recipes related to a specific context. For example,
    use hou.sopNodeTypeCategory() for this option to return all recipes that are SOP context based.
    :param include_label: Whenever to include the label besides the internal name.
    :param pad: Whenever to pad the space between labels and internal names. When used with hutil.pprint.pprint
    function, this will print out the list of recipe names in a more human-readable column format.
    """
def submenus(node_or_parm: hou.Node | hou.ParmTuple, recipe_categories: rtypes.RecipeCategory | list[rtypes.RecipeCategory]) -> list[str]:
    """Returns a list of existing submenus declared by the recipes that apply to this node or parameter.

    :param node_or_parm: The node or parameter to check for submenus.
    :param recipe_categories: A single recipe category or a tuple of recipe categories that is searched for submenus.
    """
def submenuForRecipe(name_pattern: str, recipe_categories: rtypes.RecipeCategory | list[rtypes.RecipeCategory]) -> str:
    """Returns the submenu for this recipe.

    :param name_pattern: The internal name of the recipe. Optionally, you can use a pattern
    similar to hou.text.patternMatch().
    :param recipe_categories: A single recipe category or a tuple of recipe categories in which to look for the
    recipe. Use the RecipeCategory enum provided in this module.
    """
def setLastInvokedRecipeForNode(node: hou.Node, name: str) -> bool:
    """Sets the node's user data to store a recipe as first invoked without applying the recipe to the node. This is
    useful in an 'OnCreated' script where the node should display a recipe corresponding to the default values on
    creation, but want to avoid applying the recipe.

    NOTE: It will only set the node's user data without applying the recipe to the node.

    :param node: The node that sets its recipe as invoked.
    :param name: The internal name of the recipe to set as the invoked recipe
    """
def lastInvokedRecipeForNode(node: hou.Node, submenu: str = '', recipe_category: rtypes.RecipeCategory | None = None) -> str | None:
    """Returns the last invoked recipe for a node. Leave submenu and recipe_category empty, to return the last
    invoked recipe. Use submenu and recipe_category to filter which last invoked recipe to return. This is useful
    when multiple recipe categories use the same submenu.

    :param node: The node to check for invoked recipes.
    :param submenu: The submenu in which to look for the last invoked recipe. When no submenu is provided, it
    returns the last invoked recipe.
    :param recipe_category: The recipe category (currently, node or parmPreset) in which to look for the last invoked
    recipe. When no recipe category is provided, it returns the last invoked recipe.
    """
def missingNodeTypesForRecipe(name: str, recipe_category: rtypes.RecipeCategory) -> dict[str, dict[str, list[str]]] | None:
    """Returns a dictionary containing information about node types that the recipe needs, but missing from the
    current houdini session. This only validates against the items recorded in the data. It will not validate for any
    missing type that is part of a locked digital asset.

    The output is a dictionary containing the node type category, the name of that node type that is missing,
    and the list of relative paths in the data where the missing node type is recorded, in the following fashion:

    {
        'category_name': {
            'type_name': [path_in_data1, ]
        }
    }

    For example,
    {
        'Sop': {
            'pyrosolver': [pyrosolver1, pyrosolver2, ],
            'bulletsolver': [subnet1/bulletsolver1, ],
        }
        'Lop': {
            'sopimport': [sopimport1, ],
        }
    }

    :param name: The internal name of the recipe to investigate.
    :param recipe_category: The recipe category in which to search for recipes. Use the RecipeCategory enum provided
    in this module.
    """
def isRecipeUnderHFS(name: str, recipe_category: rtypes.RecipeCategory) -> bool:
    """Returns True if the recipe name is under HFS path."""
def recipeNamesWithProperties(recipe_categories: rtypes.RecipeCategory | list[rtypes.RecipeCategory] = ..., nodetype_category: str = '', nodetype_name: str = '', parmname: str = '', parmtype_name: str = '', nodetype_pattern: str = '', parmtype_pattern: str = '', parmname_pattern: str = '', visible: bool = True, valid: bool = True) -> list[str]: ...
def dataFromRecipes(recipe_categories: rtypes.RecipeCategory | list[rtypes.RecipeCategory] | tuple[rtypes.RecipeCategory, ...] = ..., nodetype_category: str | None = None, nodetype_name: str | None = None, parmname: str | None = None, parmtype_name: str | None = None, nodetype_patterns: str | None = None, parmtype_patterns: str | None = None, parmname_patterns: str | None = None, visible: bool = True, valid: bool = True, under_hfs: bool | None = None) -> list[_RecipeDataEntry[rtypes._RecipeDataPayload]]:
    '''
    Returns the data for all recipes fitting the criteria. The returned data structure is grouped into a list of
    dictionaries to easily differentiate which data belongs to which recipe as follows:
    [
        { \'name\': \'the name of the recipe\',
          \'label\': \'the label of the recipe\',
          \'data\': \'the data stored in the recipe\',
        },
    ]

    Any option set to None is ignored during search. Recipes always save information about the node or parameter
    that was used to generate the recipe using nodetype_category, nodetype_name. In case of Decoration and Tool recipes
    these keys refer to the anchor/central node. Similarly, parmname and parmtype_name refer to the parameter
    that was used to create the Parm Preset Recipe.

    The pattern options on the other hand, nodetype_pattern, parmtype_pattern, parmname_pattern can specify a range
    of nodes and parameters that the recipe is valid for.

    For example a Node Preset recipe generated from SOP Box could have the following keys:
    {
        \'nodetype_category\':\'SOP\',
        \'nodetype_name\': \'box\',
        "nodetype_patterns": [
            "Sop/box",
            "Sop/sphere"
        ]
    }

    This means that the recipe was generated from a SOP box nodetype, but it is available for both SOP box and sphere nodetype.

    :param recipe_categories: The recipe categories to search for recipes.
    :param nodetype_category: Node Preset/Decoration/Tool Recipes with the given node type category will be returned.
    :param nodetype_name: Node Preset/Decoration/Tool Recipes generated from the given node type name will be returned.
    :param parmname: Parm Preset Recipes generated from the given parameter name will be returned.
    :param parmtype_name: Parm Preset Recipes with the given parm type will be returned.
    :param nodetype_patterns: Parm/Node Preset and Decoration Recipes with the given node type pattern will be returned.
    :param parmtype_patterns: Parm Preset Recipes with the given parm type pattern will be returned.
    :param parmname_patterns:  Parm Preset Recipes with the given parm name pattern will be returned.
    :param visible: Whether to return visible recipes.
    :param valid: Whether to return validated recipes.
    :param under_hfs: Whether to return recipes under the Houdini File System path. Use False to return recipes that
    are not under the Houdini File System path. When it is set to default None, all recipes will be returned.
    '''
def dataFromDataCategory(data_category: str = 'Untitled', visible: bool = True, valid: bool = True, under_hfs: bool | None = None) -> list[_RecipeDataEntry[JSONValue]]: ...
