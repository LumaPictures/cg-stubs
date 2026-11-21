from collections.abc import Sequence
from typing import Any

from houtypes import JSONLike

import hou
from hrecipes import rtypes

typed_dict_chooser_for_properties: dict[
    rtypes.RecipeCategory,
    type[rtypes.ParmPresetOptionsData]
    | type[rtypes.NodePresetOptionsData]
    | type[rtypes.DecorationOptionsData]
    | type[rtypes.ToolOptionsData],
]

def recipeDataForParmPreset(parm: hou.ParmTuple, **opts: Any) -> rtypes.ParmPresetData: ...
def recipeDataForNodePreset(node: hou.OpNode, **opts: Any) -> rtypes.NodePresetData: ...
def recipeDataForDecoration(
    central_node: hou.OpNode, decorator_items: Sequence[hou.NetworkMovableItem], **opts: Any
) -> rtypes.DecorationData: ...
def recipeDataForTool(anchor_node: hou.OpNode, label: str = ..., **opts: Any) -> rtypes.ToolData: ...
def recipeDataForData(
    data: JSONLike, **opts: Any
) -> rtypes.DataRecipeData: ...
