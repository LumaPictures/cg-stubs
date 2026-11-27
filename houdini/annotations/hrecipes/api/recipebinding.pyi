from collections.abc import Sequence
from typing import TypedDict, Unpack, type_check_only

import hou
from houtypes import JSONLike, ShelfToolKwargs
from hrecipes import rtypes
from hrecipes.api.reciperef import Ref

# The _save_recipe() wrapper saves a given recipe_data instead of building it from the options.
@type_check_only
class _SaveParmPresetRecipeKwargs(hou._ParmPresetRecipeOpts, total=False):
    recipe_data: rtypes.ParmPresetData | None

@type_check_only
class _SaveNodePresetRecipeKwargs(hou._NodePresetRecipeOpts, total=False):
    recipe_data: rtypes.NodePresetData | None

@type_check_only
class _SaveDecorationRecipeKwargs(hou._DecorationRecipeOpts, total=False):
    recipe_data: rtypes.DecorationData | None

@type_check_only
class _SaveToolRecipeKwargs(hou._ToolRecipeOpts, total=False):
    recipe_data: rtypes.ToolData | None

# The fields of rtypes.DataRecipeOptions.
@type_check_only
class _SaveDataRecipeKwargs(TypedDict, total=False):
    verbose: bool
    data_category: str
    process_order: float
    expand_to_dir: bool
    comment: str
    recipe_data: rtypes.DataRecipeData | None

# applyPresetRecipe() applies a node preset or a parm preset recipe.
@type_check_only
class _PresetRecipeOptionsSettingKwargs(
    hou._NodePresetRecipeSetOpts, hou._ParmPresetRecipeSetOpts, total=False
): ...

# networkcluster.setCluster() reads network_editor from the options.
@type_check_only
class _ApplyDecorationRecipeKwargs(hou._DecorationRecipeSetOpts, total=False):
    network_editor: hou.NetworkEditor | None

# ToolRecipeRef.applyRecipe() also reads jump.
@type_check_only
class _ApplyToolRecipeKwargs(hou._ToolRecipeSetOpts, total=False):
    jump: bool

def saveParmPresetRecipe(*, name: str, label: str, location: str, parm: hou.ParmTuple, **opts: Unpack[_SaveParmPresetRecipeKwargs]) -> Ref | None: ...
def saveNodePresetRecipe(*, name: str, label: str, location: str, node: hou.OpNode, **opts: Unpack[_SaveNodePresetRecipeKwargs]) -> Ref | None: ...
def saveDecorationRecipe(
    *,
    name: str,
    label: str,
    location: str,
    central_node: hou.OpNode,
    decorator_items: Sequence[hou.NetworkMovableItem],
    **opts: Unpack[_SaveDecorationRecipeKwargs],
) -> Ref | None: ...
def saveToolRecipe(
    *, name: str, label: str, location: str, anchor_node: hou.OpNode | None = ..., **opts: Unpack[_SaveToolRecipeKwargs]
) -> Ref | None: ...
def saveDataRecipe(
    *,
    name: str,
    label: str,
    location: str,
    data: JSONLike,
    **opts: Unpack[_SaveDataRecipeKwargs],
) -> Ref | None: ...
def applyParmPresetRecipe(
    name: str, parm: hou.Parm | hou.ParmTuple | None = ..., **opts: Unpack[hou._ParmPresetRecipeSetOpts]
) -> rtypes.ParmPresetOutputData | None: ...
def applyNodePresetRecipe(
    name: str, node: hou.OpNode | None = ..., **opts: Unpack[hou._NodePresetRecipeSetOpts]
) -> rtypes.NodePresetOutputData | tuple[str, str] | None: ...
def applyPermanentDefault(name: str, nodetype_name: str, kwargs: ShelfToolKwargs, **opts: Unpack[hou._NodePresetRecipeSetOpts]) -> tuple[str, str]: ...
def applyPresetRecipe(
    name: str, node: hou.OpNode | None = ..., **opts: Unpack[_PresetRecipeOptionsSettingKwargs]
) -> rtypes.NodePresetOutputData | rtypes.ParmPresetOutputData | tuple[str, str] | None: ...
def applyDecorationRecipe(
    name: str, central_node: hou.OpNode | None = ..., **opts: Unpack[_ApplyDecorationRecipeKwargs]
) -> rtypes.DecorationOutputData | None: ...
def applyToolRecipe(name: str, **opts: Unpack[_ApplyToolRecipeKwargs]) -> rtypes.ToolOutputData | None: ...
def applyExample(name: str, **opts: Unpack[_ApplyToolRecipeKwargs]) -> rtypes.ToolOutputData | None: ...
def applyToSubnet(
    name: str,
    recipe_category: rtypes.RecipeCategory,
    subnet: hou.OpNode,
    update_interface: bool = ...,
    update_content: bool = ...,
) -> None: ...
def dataFromRecipe(name: str) -> rtypes._RecipeDataPayload: ...
