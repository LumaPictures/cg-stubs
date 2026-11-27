from typing import Any
import hou
import recipedatamerger as rdmerger
import typing
from collections.abc import Mapping as Mapping, Sequence
from houtypes import JSONValue, ParmCallbackKwargs, ParmMenuScriptKwargs
from hrecipes import RecipeCategory, ToolPromptType as ToolPromptType, ToolType as ToolType
from hrecipes.binding import _RecipeDataEntry as _RecipeDataEntry
from hrecipes.rtypes import _RecipeDataPayload
from typing import Literal, TypedDict
from typing_extensions import ReadOnly, Required

class _MenuEntryKwargs(TypedDict, total=False):
    node: Required[ReadOnly[hou.OpNode]]
    toolname: ReadOnly[str]
    networkeditor: ReadOnly[hou.NetworkEditor]

def buildSnippetMenuFromRecipes(kwargs: ParmMenuScriptKwargs) -> list[_RecipeDataPayload]:
    """Builds dynamic menu for snippet like parameters that will apply the data of the recipe. This should not be
    called directly from parameters, instead this is used in files such as pythonscriptmenu.py and others.

    :param kwargs: The global variable of the same name that is available in the Menu Script context.
    :returns: A list of menu entries used to populate snippet expressions.
    """
def buildPresetMenu(kwargs: ParmMenuScriptKwargs, submenu: str = '', revert: bool = False, revert_token: str = 'menu', revert_label: str = 'Preset') -> list[str]:
    """Builds dynamic menu for menu parameters containing the available preset for a node.
    Call this function directly from the Menu Script of an ordered-menu parameter.

    :param kwargs: The global variable of the same name that is available in the Menu Script context.
    :param submenu: When it is left empty, it returns all presets recipes for the node otherwise provide
    the submenu to only return a recipe presets for that submenu.
    :param revert: Reverts the menu to its first element, which only displays a label with the last invoked recipe.
    :param revert_token: When revert is set to True, set the token of the first entry.
    :param revert_label: When revert is set to True, set the label of the first entry.
    :returns: A list of menu entries used to populate menu parameters.
    """
def setPresetMenu(kwargs: ParmCallbackKwargs, revert: bool = False) -> None:
    """Callback Script for menu parameters that were built using the buildPresetMenu function.
    :param kwargs: The global variable of the same name that is available in the Menu Script context.
    :param revert: Reverts the menu to the first element. Set this the same as in buildPresetMenu function.
    """
def submenusForNode(node: hou.Node, recipe_categories: RecipeCategory | list[RecipeCategory]) -> list[str]:
    """Returns a list of existing submenus declared by the recipes that apply to node.

    :param node: The node to check for submenus.
    :param recipe_categories: A single recipe category or a tuple of recipe categories that is searched for submenus.
    Currently, nodePreset and parmPreset use submenus. Use the RecipeCategory enum provided in this module.
    """
def submenusForParm(parm: hou.Parm | hou.ParmTuple, recipe_categories: RecipeCategory | list[RecipeCategory]) -> list[str]:
    """Returns a list of existing submenus declared by the recipes that apply to parm.

    :param parm: The parm or parm tuple to check for submenus.
    :param recipe_categories: A single recipe category or a tuple of recipe categories that is searched for submenus.
    Currently, nodePreset and parmPreset use submenus. Use the RecipeCategory enum provided in this module.
    """
def submenuForRecipe(name_pattern: str, recipe_categories: RecipeCategory | list[RecipeCategory]) -> str:
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
def lastInvokedRecipe(node: hou.Node, submenu: str = '', recipe_category: RecipeCategory | None = None) -> str | None:
    """Returns the last invoked recipe for a node. Leave submenu and recipe_category empty, to return the last
    invoked recipe. Use submenu and recipe_category to filter which last invoked recipe to return. This is useful
    when multiple recipe categories use the same submenu.

    :param node: The node to check for invoked recipes.
    :param submenu: The submenu in which to look for the last invoked recipe. When no submenu is provided, it
    returns the last invoked recipe.
    :param recipe_category: The recipe category (currently, nodePreset or parmPreset) in which to look for the last
    invoked recipe. Use the RecipeCategory enum provided in this module. When no recipe category is provided,
    it returns the last invoked recipe.
    """
def removeLastInvokedRecipe(node: hou.Node) -> None:
    """Removes the __last_invoked_recipes__ user data from this node.

    :param node: The node from witch to remove the user data related to invoked recipes.
    """
def hasRecipe(node_or_parm: hou.Node | hou.ParmTuple, recipe_category: RecipeCategory | Sequence[RecipeCategory], submenu_filter: str = '', visible: bool = True, valid: bool = True) -> bool:
    """Returns whenever the node or parameter has any associated Recipe. This will be faster to call than using
    recipeMenu() and check for its output.

    :param node_or_parm: The node or parameter tuple to check for menu entries.
    :param recipe_category: A single recipe category or a tuple of recipe categories in which to look for recipes
    belonging to the node or parameter tuple. Use the RecipeCategory enum provided in this module.
    :param submenu_filter: Only include entries that are part of this submenu.
    :param visible: Only include recipes that are set visible.
    :param valid: Only include recipes that are passed the validity test for this session.
    """
def recipeExists(name_pattern: str, recipe_categories: RecipeCategory | list[RecipeCategory] | tuple[RecipeCategory, ...]) -> bool:
    """Returns whenever a recipe is present in the current houdini session.

    :param name_pattern: The internal name of the recipe. Optionally, you can use a pattern
    similar to hou.text.patternMatch().
    :param recipe_categories: A single recipe category or a tuple of recipe categories in which to look for the
    recipe. Use the RecipeCategory enum provided in this module.
    """
def recipeNames(recipe_categories: RecipeCategory | list[RecipeCategory] | tuple[RecipeCategory, ...], name_pattern: str | None = None, nodetype_categories: hou.NodeTypeCategory | list[hou.NodeTypeCategory] | tuple[hou.NodeTypeCategory, ...] = ..., include_label: bool = True, pad: bool = True) -> list[str]:
    """Returns a list of available internal recipe names in the houdini session.

    :param recipe_categories: A single recipe category or a tuple of recipe categories in which to search for recipes.
    Use the RecipeCategory enum provided in this module.
    :param name_pattern: When this is none, it searches all recipes in the given category, otherwise use this to
    match the pattern similarly to hou.text.patternMatch().
    :param nodetype_categories: Provides another filter option as a single node type category or a tuple of node type
    categories. This is useful if you only want to return recipes related to a specific context. For example,
    use hou.sopNodeTypeCategory() for this option to return all recipes that are SOP context based.
    :param include_label: Whenever to include the label besides the internal name.
    :param pad: Whenever to pad the space between labels and internal names. When used with hutil.pprint.pprint
    function, this will print out the list of recipe names in a more human-readable column format.
    """
def recipeNamesForProperties(recipe_categories: RecipeCategory | list[RecipeCategory] = ..., nodetype_category: str = '', nodetype_name: str = '', parmname: str = '', parmtype_name: str = '', nodetype_pattern: str = '', parmtype_pattern: str = '', parmname_pattern: str = '', visible: bool = True, valid: bool = True) -> list[str]:
    """Returns a list of available internal recipe names in the houdini session for recipes that match the given
    properties.

    :param recipe_categories: A single recipe category or a tuple of recipe categories in which to search for recipes.
    Use the RecipeCategory enum provided in this module.
    :param name_pattern: When this is none, it searches all recipes in the given category, otherwise use this to
    match the pattern similarly to hou.text.patternMatch().
    :param nodetype_categories: Provides another filter option as a single node type category or a tuple of node type
    categories. This is useful if you only want to return recipes related to a specific context. For example,
    use hou.sopNodeTypeCategory() for this option to return all recipes that are SOP context based.
    :param include_label: Whenever to include the label besides the internal name.
    :param pad: Whenever to pad the space between labels and internal names. When used with hutil.pprint.pprint
    function, this will print out the list of recipe names in a more human-readable column format.
    """
def missingNodeTypesForRecipe(name: str, recipe_category: RecipeCategory) -> dict[str, dict[str, list[str]]] | None:
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
def updateRecipeBuilder(node: hou.OpNode) -> None:
    """Updates the spare parameter interface of a recipe builder subnetwork.

    :param node: The recipe generator subnetwork to update.
    """
def updateAllRecipeBuilders(node: hou.OpNode) -> None:
    """Updates the parameter interface of all recipe builder subnetworks inside the user defined node.

    :param node: The parent node that contains recipe builder subnetworks to update.
    """
def networkEditorForMenuEntry(kwargs: _MenuEntryKwargs) -> hou.NetworkEditor | None:
    """
    Finds the network editor for recipes invoked from the XML menus. This is used for decoration recipes that
    require the user to click and place them in the most relevant network editor.

    :param kwargs: The global variable of the same name that is available in the Menu Script context.
    """
def dataFromRecipe(name: str) -> _RecipeDataPayload:
    """Returns the data structure from the named recipe.

    :param name: The internal name of the recipe from which to extract the data.
    """
def dataFromRecipes(recipe_categories: RecipeCategory | list[RecipeCategory] | tuple[RecipeCategory, ...], nodetype_category: str | None = None, nodetype_name: str | None = None, parmname: str | None = None, parmtype_name: str | None = None, nodetype_patterns: str | None = None, parmtype_patterns: str | None = None, parmname_patterns: str | None = None, visible: bool = True, valid: bool = True, under_hfs: bool | None = None) -> list[_RecipeDataEntry[_RecipeDataPayload]]:
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
def isRecipeUnderHFS(name: str, recipe_category: RecipeCategory) -> bool:
    """Returns True if the recipe with the given name is under the Houdini File System path.

    :param name: The internal name of the recipe to check.
    :param recipe_category: The recipe category of the recipe to check.
    """
@typing.overload
def dataFromDataCategory(data_category: str, merge: Literal[False] = ..., merge_rules: list[rdmerger.MergeRule] = ..., visible: bool = ..., valid: bool = ..., under_hfs: bool | None = ...) -> list[_RecipeDataEntry[JSONValue]] | dict[str, JSONValue]: ...
@typing.overload
def dataFromDataCategory(data_category: str, merge: Literal[True], merge_rules: list[rdmerger.MergeRule] = ..., visible: bool = ..., valid: bool = ..., under_hfs: bool | None = ...) -> JSONValue: ...
@typing.overload
def dataFromDataCategory(data_category: str, merge: bool, merge_rules: list[rdmerger.MergeRule] = ..., visible: bool = ..., valid: bool = ..., under_hfs: bool | None = ...) -> list[_RecipeDataEntry[JSONValue]] | JSONValue: ...
def iconNameForRecipe(name: str) -> str:
    """Returns the icon name from the named recipe.

    :param name: The internal name of the recipe from which to extract the data.
    :return: The name of the icon representing the named recipe.
    """
def labelForRecipe(name: str) -> str:
    """
    Returns the label from the named recipe.
    :param name: The internal name of the recipe from which to extract the data.
    :return: The label of the recipe.
    """
def pprint(data: object) -> None:
    """Pretty prints the incoming dictionary data structure. Use this to display the data you work with more human-readable.

    :param data: The data to print in a human-readable format.
    """
