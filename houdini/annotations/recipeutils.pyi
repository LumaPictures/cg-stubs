from collections.abc import Mapping, Sequence
from typing import Literal, TypedDict, overload

import hou
import recipedatamerger as rdmerger
from houtypes import JSONValue, ParmCallbackKwargs, ParmMenuScriptKwargs
from hrecipes import RecipeCategory
from hrecipes.binding import _RecipeDataEntry
from hrecipes.rtypes import _RecipeDataPayload
from typing_extensions import ReadOnly, Required

# The keys networkEditorForMenuEntry reads from the kwargs of an OPmenu.xml script
# (houtypes.NodeContextMenuKwargs) or a ParmDonutMenu.xml one.
class _MenuEntryKwargs(TypedDict, total=False):
    node: Required[ReadOnly[hou.OpNode]]
    toolname: ReadOnly[str]
    networkeditor: ReadOnly[hou.NetworkEditor]

# Each parameter preset recipe's data, then its label.
def buildSnippetMenuFromRecipes(kwargs: ParmMenuScriptKwargs) -> list[_RecipeDataPayload]: ...
def buildPresetMenu(
    kwargs: ParmMenuScriptKwargs,
    submenu: str = ...,
    revert: bool = ...,
    revert_token: str = ...,
    revert_label: str = ...,
) -> list[str]: ...
def setPresetMenu(kwargs: ParmCallbackKwargs, revert: bool = ...) -> None: ...
def submenusForNode(node: hou.Node, recipe_categories: RecipeCategory | list[RecipeCategory]) -> list[str]: ...
def submenusForParm(
    parm: hou.Parm | hou.ParmTuple, recipe_categories: RecipeCategory | list[RecipeCategory]
) -> list[str]: ...
def submenuForRecipe(name_pattern: str, recipe_categories: RecipeCategory | list[RecipeCategory]) -> str: ...
def setLastInvokedRecipeForNode(node: hou.Node, name: str) -> bool: ...
def lastInvokedRecipe(
    node: hou.Node, submenu: str = ..., recipe_category: RecipeCategory | None = ...
) -> str | None: ...
def removeLastInvokedRecipe(node: hou.Node) -> None: ...
def hasRecipe(
    node_or_parm: hou.Node | hou.ParmTuple,
    recipe_category: RecipeCategory | Sequence[RecipeCategory],
    submenu_filter: str = ...,
    visible: bool = ...,
    valid: bool = ...,
) -> bool: ...
def recipeExists(
    name_pattern: str, recipe_categories: RecipeCategory | list[RecipeCategory] | tuple[RecipeCategory, ...]
) -> bool: ...
def recipeNames(
    recipe_categories: RecipeCategory | list[RecipeCategory] | tuple[RecipeCategory, ...],
    name_pattern: str | None = ...,
    nodetype_categories: hou.NodeTypeCategory | list[hou.NodeTypeCategory] | tuple[hou.NodeTypeCategory, ...] = ...,
    include_label: bool = ...,
    pad: bool = ...,
) -> list[str]: ...
def recipeNamesForProperties(
    recipe_categories: RecipeCategory | list[RecipeCategory] = ...,
    nodetype_category: str = ...,
    nodetype_name: str = ...,
    parmname: str = ...,
    parmtype_name: str = ...,
    nodetype_pattern: str = ...,
    parmtype_pattern: str = ...,
    parmname_pattern: str = ...,
    visible: bool = ...,
    valid: bool = ...,
) -> list[str]: ...
def missingNodeTypesForRecipe(
    name: str, recipe_category: RecipeCategory
) -> dict[str, dict[str, list[str]]] | None: ...
def updateRecipeBuilder(node: hou.Node) -> None: ...
def updateAllRecipeBuilders(node: hou.OpNode) -> None: ...
def networkEditorForMenuEntry(kwargs: _MenuEntryKwargs) -> hou.NetworkEditor | None: ...
def dataFromRecipe(name: str) -> _RecipeDataPayload: ...
def dataFromRecipes(
    recipe_categories: RecipeCategory | list[RecipeCategory] | tuple[RecipeCategory, ...],
    nodetype_category: str | None = ...,
    nodetype_name: str | None = ...,
    parmname: str | None = ...,
    parmtype_name: str | None = ...,
    nodetype_patterns: str | None = ...,
    parmtype_patterns: str | None = ...,
    parmname_patterns: str | None = ...,
    visible: bool = ...,
    valid: bool = ...,
    under_hfs: bool | None = ...,
) -> list[_RecipeDataEntry[_RecipeDataPayload]]: ...
def isRecipeUnderHFS(name: str, recipe_category: RecipeCategory) -> bool: ...
@overload
def dataFromDataCategory(
    data_category: str,
    merge: Literal[False] = ...,
    merge_rules: list[rdmerger.MergeRule] = ...,
    visible: bool = ...,
    valid: bool = ...,
    under_hfs: bool | None = ...,
) -> list[_RecipeDataEntry[JSONValue]] | dict[str, JSONValue]: ...
@overload
def dataFromDataCategory(
    data_category: str,
    merge: Literal[True],
    merge_rules: list[rdmerger.MergeRule] = ...,
    visible: bool = ...,
    valid: bool = ...,
    under_hfs: bool | None = ...,
) -> JSONValue: ...
@overload
def dataFromDataCategory(
    data_category: str,
    merge: bool,
    merge_rules: list[rdmerger.MergeRule] = ...,
    visible: bool = ...,
    valid: bool = ...,
    under_hfs: bool | None = ...,
) -> list[_RecipeDataEntry[JSONValue]] | JSONValue: ...
def dataFromDataCategory(
    data_category: str,
    merge: bool = ...,
    merge_rules: list[rdmerger.MergeRule] = ...,
    visible: bool = ...,
    valid: bool = ...,
    under_hfs: bool | None = ...,
) -> list[_RecipeDataEntry[JSONValue]] | JSONValue: ...
def iconNameForRecipe(name: str) -> str: ...
def labelForRecipe(name: str) -> str: ...
def pprint(data: object) -> None: ...
