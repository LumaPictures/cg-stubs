from collections.abc import Sequence
from typing import Any

import hou
from houtypes import JSONLike, ShelfToolKwargs
from hrecipes import rtypes
from hrecipes.api.reciperef import Ref

def saveParmPresetRecipe(name: str, label: str, location: str, parm: hou.ParmTuple, **opts: Any) -> Ref | None: ...
def saveNodePresetRecipe(name: str, label: str, location: str, node: hou.OpNode, **opts: Any) -> Ref | None: ...
def saveDecorationRecipe(
    name: str,
    label: str,
    location: str,
    central_node: hou.OpNode,
    decorator_items: Sequence[hou.NetworkMovableItem],
    **opts: Any,
) -> Ref | None: ...
def saveToolRecipe(
    name: str, label: str, location: str, anchor_node: hou.OpNode | None = ..., **opts: Any
) -> Ref | None: ...
def saveDataRecipe(
    name: str,
    label: str,
    location: str,
    data: JSONLike,
    **opts: Any,
) -> Ref | None: ...
def applyParmPresetRecipe(
    name: str, parm: hou.Parm | hou.ParmTuple | None = ..., **opts: Any
) -> rtypes.ParmPresetOutputData | None: ...
def applyNodePresetRecipe(
    name: str, node: hou.OpNode | None = ..., **opts: Any
) -> rtypes.NodePresetOutputData | tuple[str, str] | None: ...
def applyPermanentDefault(name: str, nodetype_name: str, kwargs: ShelfToolKwargs, **opts: Any) -> tuple[str, str]: ...
def applyPresetRecipe(
    name: str, node: hou.OpNode | None = ..., **opts: Any
) -> rtypes.NodePresetOutputData | rtypes.ParmPresetOutputData | tuple[str, str] | None: ...
def applyDecorationRecipe(
    name: str, central_node: hou.OpNode | None = ..., **opts: Any
) -> rtypes.DecorationOutputData | None: ...
def applyToolRecipe(name: str, **opts: Any) -> rtypes.ToolOutputData | None: ...
def applyExample(name: str, **opts: Any) -> rtypes.ToolOutputData | None: ...
def applyToSubnet(
    name: str,
    recipe_category: rtypes.RecipeCategory,
    subnet: hou.OpNode,
    update_interface: bool = ...,
    update_content: bool = ...,
) -> None: ...
def dataFromRecipe(name: str) -> rtypes._RecipeDataPayload: ...
