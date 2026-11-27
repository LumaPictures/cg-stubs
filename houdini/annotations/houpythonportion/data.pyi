from collections.abc import Iterable, Sequence
from typing import Literal, TypedDict, Unpack

import hou
from houpythonportion.OpNode import _ParmOption
from hrecipes import rtypes
from hrecipes.api import Ref

# The keyword options each function accepts: the init fields of the hrecipes.rtypes options
# dataclass it updates ("The given fields strictly represents the valid arguments").
class _Options(TypedDict, total=False):
    verbose: bool

class _ParmOptionsDictKwargs(_Options, total=False):
    values: bool
    spareparms: bool
    default_values: bool
    evaluate_values: bool
    locked: bool
    brief: bool
    multiparm_instances: bool
    metadata: bool
    callback: rtypes.ParsingCallback | None

class _ItemOptionsKwargs(_Options, total=False):
    nodes_only: bool
    children: bool
    editables: bool
    inputs: bool
    outputs: bool
    position: bool
    flags: bool
    parms: _ParmOption
    spareparms: bool
    parms_as_brief: bool
    default_parmvalues: bool
    evaluate_parmvalues: bool
    parmtemplates: rtypes.ParmTemplateOptionType
    parmtemplate_order: bool
    parmfilter: bool
    metadata: bool
    callback: rtypes.ParsingCallback | None

class _ItemOptionsListKwargs(_ItemOptionsKwargs, total=False):
    anchor_position: hou.Vector2

class _ItemOptionsSettingKwargs(TypedDict, total=False):
    clear_content: bool
    force_item_creation: bool
    parms: bool
    parmtemplates: bool
    children: bool
    editables: bool
    skip_notes: bool

class _ItemOptionsSettingListKwargs(_ItemOptionsSettingKwargs, total=False):
    external_connections: bool
    offset_position: hou.Vector2

class _ClusterOptionsKwargs(_ItemOptionsListKwargs, total=False):
    target_node: hou.OpNode | None
    dummy_nodes: list[str] | list[hou.Node] | None
    frame_nodes: list[str] | list[hou.Node] | str | None
    selected_nodes: list[str] | list[hou.Node] | str | None
    current_node: str | hou.Node | None
    selected_node: bool | hou.Node
    target_children: bool
    target_editables: bool
    target_parms: _ParmOption
    cluster_inputs: list[tuple[hou.Node, int]] | None
    cluster_outputs: list[tuple[hou.Node, int]] | None

class _ClusterOptionsSettingKwargs(_ItemOptionsSettingListKwargs, total=False):
    target_node: hou.OpNode | None
    dummy_nodes: list[hou.Node] | None
    drop_on_wire: bool
    click_to_place: bool
    avoid_overlap: bool
    frame: bool

class _RecipeOptionsKwargs(TypedDict, total=False):
    comment: str
    visible: bool
    record_data: bool
    prescript: str
    postscript: str
    oncreatedscript: str
    expand_to_dir: bool

class _ParmPresetRecipeOptionsKwargs(_Options, _RecipeOptionsKwargs, total=False):
    value: bool
    default_value: bool
    evaluate_value: bool
    locked: bool
    brief: bool
    multiparm_instances: bool
    multiparm_links: bool
    multiparm_default_values: bool
    multiparms_as_brief: bool
    metadata: bool
    parmtype_patterns: str
    parmname_patterns: str
    nodetype_patterns: str
    multiparm_operation: Literal["set", "set_from_index", "insert_at_index", "insert_first", "append"]
    multiparm_start_index: int
    multiparm_end_index: int
    submenu: str
    callback: rtypes.ParsingCallback | None

class _ParmPresetRecipeOptionsSettingKwargs(TypedDict, total=False):
    # "" applies the operation the recipe was saved with.
    multiparm_operation: Literal["", "set", "set_from_index", "insert_at_index", "insert_first", "append"]
    multiparm_start_index: int
    prescript: bool
    postscript: bool

class _NodePresetRecipeOptionsKwargs(_ItemOptionsKwargs, _RecipeOptionsKwargs, total=False):
    nodetype_patterns: str
    submenu: str

class _NodePresetRecipeOptionsSettingKwargs(_ItemOptionsSettingKwargs, total=False):
    prescript: bool
    postscript: bool

class _DecorationRecipeOptionsKwargs(_ClusterOptionsKwargs, _RecipeOptionsKwargs, total=False):
    nodetype_patterns: str
    submenu: str
    central_parms: _ParmOption
    central_children: bool
    central_editables: bool

class _DecorationRecipeOptionsSettingKwargs(_ClusterOptionsSettingKwargs, total=False):
    prescript: bool
    postscript: bool

class _ToolRecipeOptionsKwargs(_ClusterOptionsKwargs, _RecipeOptionsKwargs, total=False):
    items: list[hou.NetworkMovableItem] | None
    anchor_parms: _ParmOption
    anchor_children: bool
    anchor_editables: bool
    tool_types: Iterable[rtypes.ToolType]
    tool_labels: Iterable[str]
    tab_submenu: str
    shelf_tab: str
    shelf_ordering_index: float
    help_url: str
    example: bool
    icon: str
    # recipedata keeps the prompt type only when it is one of the ToolPromptType values.
    prompt_type: Literal["position_selection", "node_selection"]
    prompt_messages: list[str] | None
    prompt_input_nodes: list[hou.Node] | None
    prompt_posparms: list[str | None] | None
    prompt_bboxes: list[hou.BoundingBox | None] | None

class _ToolRecipeOptionsSettingKwargs(_ClusterOptionsSettingKwargs, total=False):
    pane: hou.Pane | None
    network_editor: hou.NetworkEditor | None
    scene_viewer: hou.SceneViewer | None
    parent: hou.OpNode | None
    tool_inputs: Sequence[tuple[str, int]]
    tool_outputs: Sequence[tuple[str, int]]
    prompt: bool
    prescript: bool
    postscript: bool

def dataFromParms(
    parms: Sequence[hou.ParmTuple], **parms_opts: Unpack[_ParmOptionsDictKwargs]
) -> rtypes.ParmDataDict: ...
def selectedItemsAsData(**items_opts: Unpack[_ItemOptionsListKwargs]) -> rtypes.NetworkItemDataDict | None: ...
def itemsAsData(
    items: list[hou.NetworkMovableItem], **items_opts: Unpack[_ItemOptionsListKwargs]
) -> rtypes.NetworkItemDataDict | None: ...
def createItemsFromData(
    parent: hou.OpNode, data: rtypes.NetworkItemDataDict, **items_set_opts: Unpack[_ItemOptionsSettingListKwargs]
) -> dict[str, hou.NetworkMovableItem]: ...
def clusterItemsAsData(
    items: Sequence[hou.NetworkMovableItem], **cluster_opts: Unpack[_ClusterOptionsKwargs]
) -> rtypes.ClusterData: ...
def createClusterItemsFromData(
    parent: hou.OpNode, data: rtypes.ClusterData, **cluster_set_opts: Unpack[_ClusterOptionsSettingKwargs]
) -> rtypes.ClusterOutputData: ...
def dataFromRecipe(name: str) -> rtypes._RecipeDataPayload: ...
def saveParmPresetRecipe(
    name: str,
    label: str,
    location: str,
    parm: hou.ParmTuple,
    **parmpresetrecipe_opts: Unpack[_ParmPresetRecipeOptionsKwargs],
) -> Ref | None: ...
def applyParmPresetRecipe(
    name: str,
    parm: hou.Parm | hou.ParmTuple | None = ...,
    **parmpresetrecipe_set_opts: Unpack[_ParmPresetRecipeOptionsSettingKwargs],
) -> rtypes.ParmPresetOutputData | None: ...
def saveNodePresetRecipe(
    name: str, label: str, location: str, node: hou.OpNode, **nodepresetrecipe_opts: Unpack[_NodePresetRecipeOptionsKwargs]
) -> Ref | None: ...
def applyNodePresetRecipe(
    name: str, node: hou.OpNode, **nodepresetrecipe_set_opts: Unpack[_NodePresetRecipeOptionsSettingKwargs]
) -> rtypes.NodePresetOutputData | tuple[str, str] | None: ...
def saveDecorationRecipe(
    name: str,
    label: str,
    location: str,
    central_node: hou.OpNode,
    decorator_items: Sequence[hou.NetworkMovableItem],
    **decoratorrecipe_opts: Unpack[_DecorationRecipeOptionsKwargs],
) -> Ref | None: ...
# hrecipes.applyDecorationRecipe reads these options as a DecorationRecipeOptionsSetting.
def applyDecorationRecipe(
    name: str,
    central_node: hou.OpNode | None = ...,
    **decoratorrecipe_set_opts: Unpack[_DecorationRecipeOptionsSettingKwargs],
) -> rtypes.DecorationOutputData | None: ...
def saveToolRecipe(
    name: str, label: str, location: str, anchor_node: hou.OpNode, **toolrecipe_opts: Unpack[_ToolRecipeOptionsKwargs]
) -> Ref | None: ...
def applyToolRecipe(
    name: str, **toolrecipe_set_opts: Unpack[_ToolRecipeOptionsSettingKwargs]
) -> rtypes.ToolOutputData | None: ...
def saveTabToolRecipe(
    name: str, label: str, location: str, anchor_node: hou.OpNode, **toolrecipe_opts: Unpack[_ToolRecipeOptionsKwargs]
) -> Ref | None: ...
def applyTabToolRecipe(
    name: str, **toolrecipe_set_opts: Unpack[_ToolRecipeOptionsSettingKwargs]
) -> rtypes.ToolOutputData | None: ...
