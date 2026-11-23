from collections.abc import Mapping, Sequence
from typing import Generic, TypedDict

import hou
from houtypes import JSONValue, NodeContextMenuKwargs
from hrecipes import rtypes
from typing_extensions import TypeVar

_D = TypeVar("_D", default=rtypes._RecipeDataPayload)

# The data is Ref.loadData()'s.
class _RecipeDataEntry(TypedDict, Generic[_D]):
    name: str
    label: str
    data: _D

def hasRecipe(
    node_or_parm: hou.Node | hou.ParmTuple,
    recipe_category: rtypes.RecipeCategory | Sequence[rtypes.RecipeCategory],
    legacy_presets: bool = ...,
    examples_only: bool = ...,
    name_pattern: str | None = ...,
    submenu_filter: str = ...,
    visible: bool = ...,
    valid: bool = ...,
) -> bool: ...
def canMakeTool(items: Sequence[hou.NetworkMovableItem]) -> bool: ...
def canMakeDecoration(items: Sequence[hou.NetworkMovableItem]) -> bool | Sequence[hou.NetworkMovableItem]: ...
# kwargs is unused.
def showParmPresetDialog(parm: hou.Parm | hou.ParmTuple, kwargs: Mapping[str, object] | None = ...) -> None: ...
def showNodePresetDialog(node: hou.Node, kwargs: Mapping[str, object] | None = ...) -> None: ...
def _showGenericNodeDialog(
    kind: rtypes.RecipeCategory = ...,
    items: Sequence[hou.NetworkMovableItem] = ...,
    central: hou.Node | None = ...,
    editor: hou.NetworkEditor | None = ...,
    kwargs: NodeContextMenuKwargs | None = ...,
) -> None: ...
def showDecorationDialog(
    items: Sequence[hou.NetworkMovableItem] = ...,
    central: hou.Node | None = ...,
    editor: hou.NetworkEditor | None = ...,
    kwargs: NodeContextMenuKwargs | None = ...,
) -> None: ...
def showToolDialog(
    items: Sequence[hou.NetworkMovableItem] = ...,
    central: hou.Node | None = ...,
    editor: hou.NetworkEditor | None = ...,
    kwargs: NodeContextMenuKwargs | None = ...,
) -> None: ...
def showPermanentDefaultDialog(node: hou.Node) -> None: ...
def recipeExists(
    name_pattern: str, recipe_categories: rtypes.RecipeCategory | list[rtypes.RecipeCategory] | tuple[rtypes.RecipeCategory, ...]
) -> bool: ...
def recipeNames(
    recipe_categories: rtypes.RecipeCategory | list[rtypes.RecipeCategory] | tuple[rtypes.RecipeCategory, ...],
    name_pattern: str | None = ...,
    nodetype_categories: hou.NodeTypeCategory | list[hou.NodeTypeCategory] | tuple[hou.NodeTypeCategory, ...] = ...,
    include_label: bool = ...,
    pad: bool = ...,
) -> list[str]: ...
def lastInvokedRecipeForNode(
    node: hou.Node, submenu: str = ..., recipe_category: rtypes.RecipeCategory | None = ...
) -> str | None: ...
def missingNodeTypesForRecipe(
    name: str, recipe_category: rtypes.RecipeCategory
) -> dict[str, dict[str, list[str]]] | None: ...
def dataFromRecipes(
    recipe_categories: rtypes.RecipeCategory | list[rtypes.RecipeCategory] | tuple[rtypes.RecipeCategory, ...] = ...,
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
) -> list[_RecipeDataEntry[rtypes._RecipeDataPayload]]: ...
def dataFromDataCategory(
    data_category: str = ..., visible: bool = ..., valid: bool = ..., under_hfs: bool | None = ...
) -> list[_RecipeDataEntry[JSONValue]]: ...
