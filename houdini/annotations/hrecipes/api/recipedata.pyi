from collections.abc import Sequence
from typing import Unpack

from houtypes import JSONLike

import hou
from hrecipes import rtypes
from hrecipes.api import recipebinding

typed_dict_chooser_for_properties: dict[
    rtypes.RecipeCategory,
    type[rtypes.ParmPresetOptionsData]
    | type[rtypes.NodePresetOptionsData]
    | type[rtypes.DecorationOptionsData]
    | type[rtypes.ToolOptionsData],
]

def recipeDataForParmPreset(parm: hou.ParmTuple, **opts: Unpack[recipebinding._SaveParmPresetRecipeKwargs]) -> rtypes.ParmPresetData: ...
def recipeDataForNodePreset(node: hou.OpNode, **opts: Unpack[recipebinding._SaveNodePresetRecipeKwargs]) -> rtypes.NodePresetData: ...
def recipeDataForDecoration(
    central_node: hou.OpNode, decorator_items: Sequence[hou.NetworkMovableItem], **opts: Unpack[recipebinding._SaveDecorationRecipeKwargs]
) -> rtypes.DecorationData: ...
def recipeDataForTool(anchor_node: hou.OpNode, label: str = ..., **opts: Unpack[recipebinding._SaveToolRecipeKwargs]) -> rtypes.ToolData: ...
def recipeDataForData(
    data: JSONLike, **opts: Unpack[recipebinding._SaveDataRecipeKwargs]
) -> rtypes.DataRecipeData: ...
