import hou
from collections.abc import Iterable, Mapping, Sequence
from typing import Any, Literal, Never, NotRequired, Protocol, Self, TypeAlias, TypedDict, Unpack

from houtypes import JSONLike, JSONValue
from hrecipes.utils import _UserDataContents

# utils.invokeCallback calls it with a single keyword: parm_tuple= from api.parm, parm_template=
# from api.parmtemplate.
class _ParsingCallbackKwargs(TypedDict, total=False):
    parm_tuple: hou.ParmTuple
    parm_template: hou.ParmTemplate

class _ParsingCallback(Protocol):
    def __call__(self, **kwargs: Unpack[_ParsingCallbackKwargs]) -> object: ...

ParsingCallback: TypeAlias = _ParsingCallback

# The values of a geometry data parm and a key-value dictionary parm (parmvalue._evalAsData).
class _GeometryValueData(TypedDict):
    geometry: str

class _DictionaryValueData(TypedDict):
    dictionary: dict[str, str]

ParmTemplateOptionType: TypeAlias = Literal["none", "spare_only", "all"]
LiteralData: TypeAlias = int | float | str | bool | _GeometryValueData | _DictionaryValueData

# A parm's brief data is its value alone, or the list of its ramp points or multiparm instances
# (`{"objpath#": ...}` per instance).
ParmUnionData: TypeAlias = "ParmValueData | ParmData | RampPointDataList | MultiParmInstanceDataList"
MultiParmInstanceDataList: TypeAlias = "list[ParmDataDict]"
# A parm value, including a key-value dictionary parm's (utils.parmDataValue).
ParmValueType: TypeAlias = "int | float | str | dict[str, str] | Sequence[int | float | str] | ParmValueData | None"

class RampPointData:
    # Each is the point's parm value data, so it can be an expression or keyframes.
    pos: float | ExpressionData | KeyframesData
    value: float | ExpressionData | KeyframesData | Sequence[float | ExpressionData | KeyframesData]
    interp: str | ExpressionData | KeyframesData

class ParmData:
    # Not keys of the data, which has `locked` and `multiparm_links`.
    lock: Never
    multiparmlinks: Never
    locked: bool | list[bool]
    multiparm_links: MultiParmLinksData
    range: list[float]

class RecipeCategory:
    def text(self, plural: bool = ..., short: bool = ...) -> str: ...
    @classmethod
    def hasValue(cls, value: object) -> bool: ...

class ParmTemplateData:
    # hou.ParmTemplate.tags()
    tags: dict[str, str]
    tab_disable_when: str
    tab_hide_when: str

class NetworkItemData:
    # hou.NetworkMovableItem.userDataDict(), less the private ___ keys
    user_data: dict[str, str]
    shader_language: str
    inoutdetail: str
    title: str
    # utils.UserData.attachTo()
    sidefx: _UserDataContents

class ClusterData:
    # utils.UserData.attachTo()
    sidefx: _UserDataContents

class NetworkItemMetadata:
    # Only a node's metadata has these.
    category: NotRequired[str]
    parent: NotRequired[str]

class BaseOptions:
    def asdict(self) -> dict[str, Any]: ...
    def replace(self, /, **changes: Any) -> Self: ...
    def update(self, data: Mapping[str, object], overwrite_existing: bool = ...) -> None: ...

class ParmOptions:
    def __post_init__(self) -> None: ...

class RampPointOptionsList:
    def __post_init__(self) -> None: ...

class MultiParmInstanceOptions:
    def __post_init__(self) -> None: ...

class ParmOptionsDict:
    callback: ParsingCallback | None
    def __post_init__(self) -> None: ...

class ParmTemplateOptions:
    callback: ParsingCallback | None

class ParmTemplateOptionsDict:
    callback: ParsingCallback | None

class ItemOptions:
    callback: ParsingCallback | None
    def __post_init__(self) -> None: ...

class ItemOptionsSettingList:
    target_node: hou.OpNode | None
    def __post_init__(self) -> None: ...

class NodeOptionsList:
    def __post_init__(self) -> None: ...

class NetworkBoxOptions:
    def __post_init__(self) -> None: ...

class NetworkDotOptions:
    def __post_init__(self) -> None: ...

class StickyNoteOptions:
    def __post_init__(self) -> None: ...

class ClusterOptions:
    target_node: hou.OpNode | None
    dummy_nodes: list[str] | list[hou.Node] | None
    frame_nodes: list[str] | list[hou.Node] | str | None
    selected_nodes: list[str] | list[hou.Node] | str | None
    current_node: str | hou.Node | None
    cluster_inputs: list[tuple[hou.Node, int]] | None
    cluster_outputs: list[tuple[hou.Node, int]] | None

class ClusterOptionsSetting:
    target_node: hou.OpNode | None
    dummy_nodes: list[hou.Node] | None

class ParmPresetRecipeOptions:
    callback: ParsingCallback | None
    def __post_init__(self) -> None: ...

class NodePresetRecipeOptions:
    callback: ParsingCallback | None

class DecorationRecipeOptions:
    callback: ParsingCallback | None
    def __post_init__(self) -> None: ...

class ToolRecipeOptions:
    items: list[hou.NetworkMovableItem] | None
    prompt_messages: list[str] | None
    prompt_input_nodes: list[hou.Node] | None
    prompt_posparms: list[str | None] | None
    prompt_bboxes: list[hou.BoundingBox | None] | None
    callback: ParsingCallback | None
    def __post_init__(self) -> None: ...

class ToolRecipeOptionsSetting:
    pane: hou.Pane | None
    network_editor: hou.NetworkEditor | None
    scene_viewer: hou.SceneViewer | None
    parent: hou.OpNode | None
    tool_inputs: Sequence[tuple[str, int]]
    tool_outputs: Sequence[tuple[str, int]]

class ParmUIOptions:
    parms: list[str] | None

class DataRecipeData:
    # The data a data recipe is saved with; it is written out as JSON.
    data: JSONLike

class RecipePropertiesData:
    # recipedata._buildProperties() writes the 'submenu' option, a parm preset's parm name and type.
    submenu: str | None
    parmname: str
    parmtype_name: str

class RecipeToolData:
    # What recipedata._buildTool() writes, and recipeassetio.AssetIO.loadMetadata() reads.
    tool_types: list[str]
    tool_labels: list[str] | None
    prompt_bboxes: list[list[float]]
    prompt_posparms: list[str]

# The 'data' of a recipe of any category, as loaded from its JSON section: a parm preset's parm
# data, a node preset's node data, a decoration's or tool's cluster data, or a data recipe's data.
_RecipeDataPayload: TypeAlias = "ParmUnionData | NetworkItemData | ClusterData | JSONValue"

# The 'options' of a recipe of any category (recipedata._buildOptions()); old recipes may lack any.
class _RecipeOptionsData(TypedDict, total=False):
    evaluate_value: bool
    locked: bool
    brief: bool
    multiparm_instances: bool
    multiparm_links: bool
    multiparm_default_values: bool
    multiparms_as_brief: bool
    multiparm_operation: str
    nodes_only: bool
    children: bool
    central_children: bool
    anchor_children: bool
    editables: bool
    central_editables: bool
    anchor_editables: bool
    flags: bool
    parmfilter: bool
    parms: bool
    parms_as_brief: bool
    default_parmvalues: bool
    evaluate_parmvalues: bool
    parmtemplates: ParmTemplateOptionType
    metadata: bool
    verbose: bool

# A recipe's whole data section (data.recipe.json), of any category and data version: the keys
# are read with .get() and defaults.
class _RecipeFileData(TypedDict, total=False):
    info: RecipeInfoData
    properties: RecipePropertiesData
    options: _RecipeOptionsData
    tool: RecipeToolData
    data: _RecipeDataPayload
