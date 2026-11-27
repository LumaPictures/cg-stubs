import hou
from . import recipedata as recipedata, utils as utils
from .. import rtypes as rtypes, storage as storage
from houtypes import JSONLike, ShelfToolKwargs
from hrecipes.api.reciperef import Ref as Ref
from typing import Sequence, TypedDict, Unpack

class _SaveParmPresetRecipeKwargs(hou._ParmPresetRecipeOpts, total=False):
    recipe_data: rtypes.ParmPresetData | None

class _SaveNodePresetRecipeKwargs(hou._NodePresetRecipeOpts, total=False):
    recipe_data: rtypes.NodePresetData | None

class _SaveDecorationRecipeKwargs(hou._DecorationRecipeOpts, total=False):
    recipe_data: rtypes.DecorationData | None

class _SaveToolRecipeKwargs(hou._ToolRecipeOpts, total=False):
    recipe_data: rtypes.ToolData | None

class _SaveDataRecipeKwargs(TypedDict, total=False):
    verbose: bool
    data_category: str
    process_order: float
    expand_to_dir: bool
    comment: str
    recipe_data: rtypes.DataRecipeData | None

class _PresetRecipeOptionsSettingKwargs(hou._NodePresetRecipeSetOpts, hou._ParmPresetRecipeSetOpts, total=False): ...

class _ApplyDecorationRecipeKwargs(hou._DecorationRecipeSetOpts, total=False):
    network_editor: hou.NetworkEditor | None

class _ApplyToolRecipeKwargs(hou._ToolRecipeSetOpts, total=False):
    jump: bool

def saveParmPresetRecipe(name: str, label: str, location: str, parm: hou.ParmTuple, **opts: Unpack[_SaveParmPresetRecipeKwargs]) -> Ref | None: ...
def saveNodePresetRecipe(name: str, label: str, location: str, node: hou.OpNode, **opts: Unpack[_SaveNodePresetRecipeKwargs]) -> Ref | None: ...
def saveDecorationRecipe(name: str, label: str, location: str, central_node: hou.OpNode, decorator_items: Sequence[hou.NetworkMovableItem], **opts: Unpack[_SaveDecorationRecipeKwargs]) -> Ref | None: ...
def saveToolRecipe(name: str, label: str, location: str, anchor_node: hou.OpNode | None = None, **opts: Unpack[_SaveToolRecipeKwargs]) -> Ref | None: ...
def saveDataRecipe(name: str, label: str, location: str, data: JSONLike, **opts: Unpack[_SaveDataRecipeKwargs]) -> Ref | None: ...
def applyParmPresetRecipe(name: str, parm: hou.Parm | hou.ParmTuple | None = None, **opts: Unpack[hou._ParmPresetRecipeSetOpts]) -> rtypes.ParmPresetOutputData | None: ...
def applyNodePresetRecipe(name: str, node: hou.OpNode | None = None, **opts: Unpack[hou._NodePresetRecipeSetOpts]) -> rtypes.NodePresetOutputData | tuple[str, str] | None: ...
def applyPermanentDefault(name: str, nodetype_name: str, kwargs: ShelfToolKwargs, **opts: Unpack[hou._NodePresetRecipeSetOpts]) -> tuple[str, str]: ...
def applyPresetRecipe(name: str, node: hou.OpNode | None = None, **opts: Unpack[_PresetRecipeOptionsSettingKwargs]) -> rtypes.NodePresetOutputData | rtypes.ParmPresetOutputData | tuple[str, str] | None:
    """Used to apply presets from XML menus. This works on Node and Parm Preset Recipes, as well as Legacy Presets.
    Legacy presets are prefix with 'legacy::'. Otherwise, when a parm preset is given, the parameter is decided based
    on the parmname_patterns key stored inside the recipe data. We only look at the first pattern in the list, and
    the pattern must be an exact parm name to find the corresponding parm object.
    """
def applyDecorationRecipe(name: str, central_node: hou.OpNode | None = None, **opts: Unpack[_ApplyDecorationRecipeKwargs]) -> rtypes.DecorationOutputData | None: ...
def applyToolRecipe(name: str, **opts: Unpack[_ApplyToolRecipeKwargs]) -> rtypes.ToolOutputData | None: ...
def applyExample(name: str, **opts: Unpack[_ApplyToolRecipeKwargs]) -> rtypes.ToolOutputData | None:
    """Applies the example listed in XML menus."""
def applyToSubnet(name: str, recipe_category: rtypes.RecipeCategory, subnet: hou.OpNode, update_interface: bool = True, update_content: bool = True) -> None:
    """Loads the recipe into a Recipe Builder subnet.

    :param name: The name of the recipe to load.
    :param recipe_category: The recipe category of the recipe to load.
    :param subnet: The recipe builder subnet.
    :param update_interface: Whether to update the Recipe Builder's parameter interface.
    :param update_content: Whether to update to inside content of the Recipe Builder.
    """
def dataFromRecipe(name: str) -> rtypes._RecipeDataPayload: ...
def iconNameForRecipe(name: str) -> str: ...
def labelForRecipe(name: str) -> str: ...
