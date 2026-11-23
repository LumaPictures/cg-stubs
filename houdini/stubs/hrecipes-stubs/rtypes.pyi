import dataclasses
import enum
import hou
from . import utils as utils
from _typeshed import Incomplete
from collections.abc import Mapping
from houtypes import JSONLike, JSONValue
from hrecipes.utils import _UserDataContents
from typing import Any, Iterable, Never, NotRequired, Protocol, Self, Sequence, TypeAlias, Unpack
from typing_extensions import TypedDict

from typing import TypeAlias
from typing import Dict
from typing import List
from typing import Literal
from typing import Union
ParsingCallback: TypeAlias = _ParsingCallback
LiteralData: TypeAlias = int | float | str | bool | _GeometryValueData | _DictionaryValueData
ParmUnionData: TypeAlias = 'ParmValueData | ParmData | RampPointDataList | MultiParmInstanceDataList'
MultiParmInstanceDataList: TypeAlias = 'list[ParmDataDict]'
ParmValueType: TypeAlias = 'int | float | str | dict[str, str] | Sequence[int | float | str] | ParmValueData | None'
_RecipeDataPayload: TypeAlias = 'ParmUnionData | NetworkItemData | ClusterData | JSONValue'
ParmTemplateOptionType: TypeAlias = Literal['none', 'spare_only', 'all']
ParmOptionType: TypeAlias = Union[bool, List[hou.ParmTuple], List[str], set[str], tuple[str]]
NetworkMovableItemDict: TypeAlias = Dict[str, hou.NetworkMovableItem]
class _ParsingCallbackKwargs(TypedDict, total=False):
    parm_tuple: hou.ParmTuple
    parm_template: hou.ParmTemplate

class _ParsingCallback(Protocol):
    def __call__(self, **kwargs: Unpack[_ParsingCallbackKwargs]) -> object: ...


class _GeometryValueData(TypedDict):
    geometry: str

class _DictionaryValueData(TypedDict):
    dictionary: dict[str, str]


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

class _RecipeFileData(TypedDict, total=False):
    info: RecipeInfoData
    properties: RecipePropertiesData
    options: _RecipeOptionsData
    tool: RecipeToolData
    data: _RecipeDataPayload

class RecipeCategory(enum.Enum):
    parmPreset = 'parm_preset_recipe'
    parmTemplate = 'parm_template_recipe'
    nodePreset = 'node_preset_recipe'
    decoration = 'decoration_recipe'
    tool = 'tool_recipe'
    data = 'data_recipe'
    def text(self, plural: bool = False, short: bool = False) -> str: ...
    @classmethod
    def hasValue(cls, value: object) -> bool: ...

class ConnectDir(enum.Enum):
    incoming = enum.auto()
    outgoing = enum.auto()

class ClusterTagTypes(enum.Enum):
    target = 'target_tag'
    selected = 'selected_tag'
    dummy = 'dummy_tags'

class Patterns(enum.Enum):
    nodetype = 'nodetype_patterns'
    parmname = 'parmname_patterns'
    parmtype = 'parmtype_patterns'

class MultiParmOpType(enum.Enum):
    set = 'set'
    set_from_index = 'set_from_index'
    insert_at_index = 'insert_at_index'
    insert_first = 'insert_first'
    append = 'append'

class ToolType(enum.Enum):
    tab = 'tab'
    shelf = 'shelf'

class ToolPromptType(enum.Enum):
    position_selection = 'position_selection'
    node_selection = 'node_selection'

class ParmFilterMode(enum.Enum):
    none = ''
    captured = 'captured'
    all = 'all'
    parms_and_headings = ('parms_and_headings',)
    time_dependent = 'time_dependent'
    scoped = 'scoped'
    auto_scoped = 'auto_scoped'
    selected = 'selected'
    with_non_default_value = 'with_non_default_value'
    with_expression = 'with_expression'
    with_overwrite = 'with_overwrite'
    invisible = 'invisible'
    visible_and_invisible = 'visible_and_invisible'
    no_control_menu = 'no_control_menu'

class ParmFilterCriteria(enum.Enum):
    names_and_labels = 'names_and_labels'
    names = 'names'
    labels = 'labels'
    raw_values = 'raw_values'
    evaluated_values = 'evaluated_values'

class ExampleDict(TypedDict):
    doc_path: str
    file_path: str
    title: str

class ExpressionData(TypedDict, total=False):
    expression: str
    language: str

class KeyframeData(TypedDict, total=False):
    frame: float
    time: float
    value: float
    expression: str
    slope: float
    accel: float
    invalue: float
    inslope: float
    inaccel: float
    accelasratio: bool

class KeyframesData(TypedDict, total=True):
    keyframes: list[KeyframeData]
    extrapolation_before: str
    extrapolation_after: str
ParmValueComponentData = LiteralData | ExpressionData | KeyframesData
ParmValueComponentDataList = list[ParmValueComponentData]
ParmValueData = LiteralData | ExpressionData | KeyframesData | ParmValueComponentDataList | None

class ParmMetaData(TypedDict, total=True):
    type: str
    label: str
    spare: bool
    path: str

class RampPointData(TypedDict, total=False):
    pos: float | ExpressionData | KeyframesData
    value: float | ExpressionData | KeyframesData | Sequence[float | ExpressionData | KeyframesData]
    interp: str | ExpressionData | KeyframesData
RampPointDataList = list[RampPointData]
MultiParmLinksData = dict[str, str]

class ParmData(TypedDict, total=False):
    locked: bool | list[bool]
    multiparm_links: MultiParmLinksData
    range: list[float]
    value: ParmValueData
    points: RampPointDataList
    lock: Never
    visible: bool
    multiparms: MultiParmInstanceDataList
    multiparmlinks: Never
    metadata: ParmMetaData
ParmDataDict = dict[str, ParmUnionData]
RecipeData = dict[str, Any]

class ParmTemplateData(TypedDict, total=False):
    tab_disable_when: str
    tab_hide_when: str
    type: str
    label: str
    label_hidden: bool
    num_components: int
    help: str
    hidden: bool
    joins_with_next: bool
    disable_when: str
    hide_when: str
    no_cook_when: str
    tags: dict[str, str]
    script_callback: str
    script_callback_language: str
    default_value: ParmValueData
    default_points: RampPointDataList
    min_value: float
    max_value: float
    strict_min: bool
    strict_max: bool
    menu_items: list[dict[str, str]]
    icon_names: str
    item_generator_script: str
    item_generator_script_language: str
    menu_type: str
    menu_use_token: bool
    column_labels: list[str]
    show_controls: bool
    color_type: str
    folder_names: str
    tab_group_end: bool
    tab_conditionals: str
    ordering_index: int
    parmtemplates: ParmTemplateDataDict
ParmTemplateDataDict = dict[str, ParmTemplateData]

class ParmTemplateBundleData(TypedDict, total=False):
    insert_after: str
    insert_first: str
    parmtemplates: ParmTemplateDataDict
ParmTemplateBundleDataList = list[ParmTemplateBundleData]
NetworkItemInputData = TypedDict('NetworkItemInputData', {'from': str, 'from_index': int | str, 'to_index': int | str}, total=False)

class NetworkItemOutputData(TypedDict, total=False):
    from_index: int | str
    to_index: int | str
    to: str

ConnectionData = TypedDict('ConnectionData', {'from': str, 'to': str, 'from_index': int | str, 'to_index': int | str}, total=False)
NetworkItemInputDataList = list[NetworkItemInputData]
NetworkItemOutputDataList = list[NetworkItemOutputData]
ConnectionDataList = list[ConnectionData]

class NetworkItemMetadata(TypedDict, total=True):
    category: NotRequired[str]
    path: str
    parent: NotRequired[str]
NodeFlagData = dict[str, bool]

class NetworkItemData(TypedDict, total=False):
    shader_language: str
    inoutdetail: str
    title: str
    sidefx: _UserDataContents
    type: str
    inputs: NetworkItemInputDataList
    outputs: NetworkItemOutputDataList
    color: list[float]
    size: list[float]
    position: list[float]
    comment: str
    user_data: dict[str, str]
    parms: ParmDataDict
    parmtemplates: ParmTemplateDataDict | ParmTemplateBundleDataList
    parmfilter: ParmFilterDataDict
    flags: NodeFlagData
    children: NetworkItemDataDict
    editables: NetworkItemDataDict
    pinned: bool
    box_content: list[str]
    text: str
    text_color: list[float]
    text_size: list[float]
    draw_background: bool
    minimized: bool
    metadata: NetworkItemMetadata
NodeData = NetworkItemData
NetworkBoxData = NetworkItemData
NetworkDotData = NetworkItemData
StickyNoteData = NetworkItemData
IndirectInputData = NetworkItemData
NetworkItemDataDict = dict[str, NetworkItemData]

class ParmFilterDataDict(TypedDict, total=False):
    mode: str
    criteria: str
    pattern: str
    exact_match: bool

class ClusterTagData(TypedDict, total=False):
    target_tag: str
    frame_tags: list[str] | str
    selected_tags: list[str] | str
    current_tag: str
    dummy_tags: list[str]

class ClusterData(TypedDict, total=False):
    sidefx: _UserDataContents
    tags: ClusterTagData
    children: NetworkItemDataDict
    cluster_inputs: ConnectionDataList
    cluster_outputs: ConnectionDataList

class ClusterOutputData(TypedDict, total=False):
    target_node: hou.Node
    target_parms: list[hou.ParmTuple]
    frame_nodes: list[hou.Node]
    selected_nodes: list[hou.Node]
    current_node: hou.Node
    items: NetworkMovableItemDict

class RecipeInfoData(TypedDict, total=True):
    author: str
    created: str
    houdini_version: str
    data_version: str
    comment: str

class RecipePropertiesData(TypedDict, total=False):
    parmname: str
    parmtype_name: str
    name: str
    label: str
    recipe_category: str
    data_category: str
    data_process_order: float
    visible: bool
    submenu: str | None
    nodetype_category: str
    nodetype_name: str
    vop_containertype: str
    parmtype_patterns: list[str]
    parmname_patterns: list[str]
    nodetype_patterns: list[str]

class ParmPresetOptionsData(TypedDict, total=True):
    evaluate_value: bool
    locked: bool
    brief: bool
    multiparm_instances: bool
    multiparm_links: bool
    multiparm_default_values: bool
    multiparms_as_brief: bool
    multiparm_operation: str
    metadata: bool
    verbose: bool

class NodePresetOptionsData(TypedDict, total=True):
    nodes_only: bool
    children: bool
    editables: bool
    flags: bool
    parmfilter: bool
    parms_as_brief: bool
    default_parmvalues: bool
    evaluate_parmvalues: bool
    parmtemplates: ParmTemplateOptionType
    metadata: bool
    verbose: bool

class DecorationOptionsData(TypedDict, total=True):
    nodes_only: bool
    central_children: bool
    children: bool
    central_editables: bool
    editables: bool
    flags: bool
    parmfilter: bool
    parms: bool
    parms_as_brief: bool
    default_parmvalues: bool
    evaluate_parmvalues: bool
    parmtemplates: ParmTemplateOptionType
    metadata: bool
    verbose: bool

class ToolOptionsData(TypedDict, total=True):
    nodes_only: bool
    anchor_children: bool
    children: bool
    anchor_editables: bool
    editables: bool
    flags: bool
    parmfilter: bool
    parms: bool
    parms_as_brief: bool
    default_parmvalues: bool
    evaluate_parmvalues: bool
    parmtemplates: ParmTemplateOptionType
    metadata: bool
    verbose: bool

class RecipeToolData(TypedDict, total=False):
    tool_types: list[str]
    tool_labels: list[str] | None
    prompt_bboxes: list[list[float]]
    icon: str
    tab_tool: bool
    tab_label: str
    tab_submenus: list[str]
    shelf_tool: bool
    shelf_label: str
    shelf_tab: str
    shelf_ordering_index: int
    help_url: str
    example: bool
    example_label: str
    network_categories: list[str]
    prompt_type: str
    prompt_messages: list[str]
    prompt_input_nodes: list[str]
    prompt_bbox: list[float]
    prompt_posparms: list[str]

class BaseRecipeData(TypedDict, total=True):
    info: RecipeInfoData
    properties: RecipePropertiesData

class ParmPresetData(BaseRecipeData):
    data: ParmUnionData
    options: ParmPresetOptionsData

class NodePresetData(BaseRecipeData):
    data: NetworkItemData
    options: NodePresetOptionsData

class DecorationData(BaseRecipeData):
    data: ClusterData
    options: DecorationOptionsData

class ToolData(BaseRecipeData):
    data: ClusterData
    options: ToolOptionsData
    tool: RecipeToolData

class DataRecipeData(BaseRecipeData):
    data: JSONLike

class ParmPresetEditData(TypedDict, total=False):
    edit_container: hou.Node
    node: hou.Node
    parm: hou.ParmTuple

class ParmPresetOutputData(TypedDict, total=False):
    node: hou.Node
    parm: hou.ParmTuple

class NodePresetEditData(TypedDict, total=True):
    info: RecipeInfoData
    properties: RecipePropertiesData
    options: NodePresetOptionsData
    edit_container: hou.Node
    node: hou.Node
    parms: list[hou.ParmTuple]

class NodePresetOutputData(TypedDict, total=True):
    node: hou.Node
    parms: list[hou.ParmTuple]

class DecorationEditData(TypedDict, total=False):
    info: RecipeInfoData
    properties: RecipePropertiesData
    options: DecorationOptionsData
    edit_container: hou.Node
    target_node: hou.Node
    target_parms: list[hou.ParmTuple]
    frame_nodes: list[hou.ParmTuple]
    selected_nodes: list[hou.ParmTuple]
    current_node: hou.Node
    items: list[hou.Node]

class DecorationOutputData(TypedDict, total=True):
    central_node: hou.Node
    central_parms: list[hou.ParmTuple]
    frame_nodes: list[hou.Node]
    selected_nodes: list[hou.Node]
    current_node: hou.Node
    items: NetworkMovableItemDict

class ToolEditData(TypedDict, total=False):
    info: RecipeInfoData
    properties: RecipePropertiesData
    options: ToolOptionsData
    edit_container: hou.Node
    target_node: hou.Node
    target_parms: list[hou.ParmTuple]
    frame_nodes: list[hou.ParmTuple]
    selected_nodes: list[hou.ParmTuple]
    current_node: hou.Node
    items: list[hou.Node]

class ToolOutputData(TypedDict, total=False):
    anchor_node: hou.Node
    anchor_parms: list[hou.ParmTuple]
    frame_nodes: list[hou.Node]
    selected_nodes: list[hou.Node]
    current_node: hou.Node
    items: NetworkMovableItemDict

@dataclasses.dataclass
class BaseOptions:
    def asdict(self) -> dict[str, Any]: ...
    def replace(self, /, **changes: Any) -> Self:
        """ Replaces existing class attribs.
        """
    def update(self, data: Mapping[str, Any], overwrite_existing: bool = True) -> None:
        """
        Update the instance attribs with values from a dictionary,
        adding new keys if they don't exist.

        NOTE: this method doesn't update the class representation.

        Args:
            data: A dictionary containing key-value pairs to 
                  update BaseOptions.

            overwrite_existing: Do not update Base Options if key already exists.

        Returns:
            None
        """

@dataclasses.dataclass
class Options(BaseOptions):
    verbose: bool = ...

@dataclasses.dataclass
class ParmValueOptions(Options):
    evaluate: bool = ...

@dataclasses.dataclass
class ParmOptions(Options):
    value: bool = ...
    default_value: bool = ...
    evaluate_value: bool = ...
    locked: bool = ...
    brief: bool = ...
    multiparm_instances: bool = ...
    multiparm_links: bool = ...
    multiparm_default_values: bool = ...
    multiparms_as_brief: bool = ...
    metadata: bool = ...
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class ParmOptionsSetting(BaseOptions): ...

@dataclasses.dataclass
class RampPointOptionsList(Options):
    evaluate: bool = ...
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class MultiParmInstanceOptions(Options):
    value: bool = ...
    default_value: bool = ...
    evaluate_value: bool = ...
    links: bool = ...
    locked: bool = ...
    brief: bool = ...
    metadata: bool = ...
    multiparm_instances = ...
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class ParmOptionsDict(Options):
    values: bool = ...
    parms: ParmOptionType = ...
    spareparms: bool = ...
    default_values: bool = ...
    evaluate_values: bool = ...
    locked: bool = ...
    brief: bool = ...
    multiparm_instances: bool = ...
    metadata: bool = ...
    callback: ParsingCallback | None = ...
    def __post_init__(self) -> None: ...

class ParmTemplateOptions(Options):
    callback: ParsingCallback | None

class ParmTemplateOptionsDict(Options):
    callback: ParsingCallback | None
    parmtemplate_order: bool

@dataclasses.dataclass
class ItemOptions(Options):
    nodes_only: bool = ...
    children: bool = ...
    editables: bool = ...
    inputs: bool = ...
    outputs: bool = ...
    position: bool = ...
    flags: bool = ...
    parms: ParmOptionType = ...
    spareparms: bool = ...
    parms_as_brief: bool = ...
    default_parmvalues: bool = ...
    evaluate_parmvalues: bool = ...
    parmtemplates: ParmTemplateOptionType = ...
    parmtemplate_order: bool = ...
    parmfilter: bool = ...
    metadata: bool = ...
    callback: ParsingCallback | None = ...
    multiparm_instances = ...
    multiparm_links = ...
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class ItemOptionsSetting(BaseOptions):
    clear_content: bool = ...
    force_item_creation: bool = ...
    parms: bool = ...
    parmtemplates: bool = ...
    children: bool = ...
    editables: bool = ...
    skip_notes: bool = ...

@dataclasses.dataclass
class ItemOptionsList(ItemOptions):
    nodes_only: bool = ...
    children: bool = ...
    editables: bool = ...
    inputs: bool = ...
    position: bool = ...
    flags: bool = ...
    parms: bool = ...
    anchor_position: hou.Vector2 = dataclasses.field(default_factory=hou.Vector2)

@dataclasses.dataclass
class ItemOptionsSettingList(ItemOptionsSetting):
    target_node: hou.Node | None = dataclasses.field(init=False)
    target_name_in_data: str = dataclasses.field(init=False)
    external_connections: bool = ...
    start_position: hou.Vector2 = dataclasses.field(init=False, default_factory=hou.Vector2)
    offset_position: hou.Vector2 = dataclasses.field(default_factory=hou.Vector2)
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class ChildrenOptionsSettingList(ItemOptionsSettingList):
    clear_content: bool = ...

@dataclasses.dataclass
class EditablesOptionsSettingList(ItemOptionsSettingList):
    clear_content: bool = ...

@dataclasses.dataclass
class NodeOptionsList(ItemOptionsList):
    nodes_only: bool = dataclasses.field(init=False)
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class NetworkBoxOptions(Options):
    nodes_only: bool = ...
    box_content: bool = ...
    position: bool = ...
    metadata: bool = ...
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class NetworkDotOptions(Options):
    inputs: bool = ...
    position: bool = ...
    metadata: bool = ...
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class StickyNoteOptions(Options):
    position: bool = ...
    metadata: bool = ...
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class ClusterOptions(ItemOptionsList):
    target_node: hou.Node | None = ...
    dummy_nodes: list[str] | list[hou.Node] | None = ...
    frame_nodes: list[str] | list[hou.Node] | str | None = ...
    selected_nodes: list[str] | list[hou.Node] | str | None = ...
    current_node: str | hou.Node | None = ...
    selected_node: bool | hou.Node = ...
    target_children: bool = ...
    target_editables: bool = ...
    target_parms: ParmOptionType = ...
    cluster_inputs: list[tuple[hou.Node, int]] | None = ...
    cluster_outputs: list[tuple[hou.Node, int]] | None = ...

@dataclasses.dataclass
class ClusterOptionsSetting(ItemOptionsSettingList):
    target_node: hou.Node | None = ...
    dummy_nodes: list[hou.Node] | None = ...
    clear_content: bool = ...
    external_connections: bool = ...
    drop_on_wire: bool = ...
    click_to_place: bool = ...
    avoid_overlap: bool = ...
    frame: bool = ...

@dataclasses.dataclass
class DescendantItemOptionsSettingList(ItemOptionsSettingList):
    clear_content: bool = ...

@dataclasses.dataclass
class ParmPresetRecipeOptions(ParmOptions):
    parmtype_patterns: str = ...
    parmname_patterns: str = ...
    nodetype_patterns: str = ...
    multiparm_operation: str = ...
    multiparm_start_index: int = ...
    multiparm_end_index: int = ...
    comment: str = ...
    visible: bool = ...
    submenu: str = ...
    record_data: bool = ...
    prescript: str = ...
    postscript: str = ...
    oncreatedscript: str = ...
    expand_to_dir: bool = ...
    callback: ParsingCallback | None = ...
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class ParmPresetRecipeOptionsSetting(ParmOptionsSetting):
    multiparm_operation: str = ...
    multiparm_start_index: int = ...
    prescript: bool = ...
    postscript: bool = ...

@dataclasses.dataclass
class NodePresetRecipeOptions(ItemOptions):
    nodetype_patterns: str = ...
    comment: str = ...
    visible: bool = ...
    submenu: str = ...
    record_data: bool = ...
    prescript: str = ...
    postscript: str = ...
    oncreatedscript: str = ...
    expand_to_dir: bool = ...
    callback: ParsingCallback | None = ...

@dataclasses.dataclass
class NodePresetRecipeOptionsSetting(ItemOptionsSetting):
    prescript: bool = ...
    postscript: bool = ...
    clear_content: bool = ...

@dataclasses.dataclass
class DecorationRecipeOptions(ClusterOptions):
    nodetype_patterns: str = ...
    comment: str = ...
    visible: bool = ...
    submenu: str = ...
    central_parms: ParmOptionType = ...
    central_children: bool = ...
    central_editables: bool = ...
    record_data: bool = ...
    prescript: str = ...
    postscript: str = ...
    oncreatedscript: str = ...
    expand_to_dir: bool = ...
    callback: ParsingCallback | None = ...
    target_name_in_data = ...
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class DecorationRecipeOptionsSetting(ClusterOptionsSetting):
    drop_on_wire: bool = ...
    click_to_place: bool = ...
    avoid_overlap: bool = ...
    frame: bool = ...
    prescript: bool = ...
    postscript: bool = ...

@dataclasses.dataclass
class ToolRecipeOptions(ClusterOptions):
    items: list[hou.NetworkMovableItem] | None = ...
    anchor_parms: ParmOptionType = ...
    anchor_children: bool = ...
    anchor_editables: bool = ...
    tool_types: Iterable[ToolType] = ...
    tool_labels: Iterable[str] = ...
    tab_submenu: str = ...
    shelf_tab: str = ...
    shelf_ordering_index: float = ...
    help_url: str = ...
    example: bool = ...
    icon: str = ...
    visible: bool = ...
    comment: str = ...
    record_data: bool = ...
    prescript: str = ...
    postscript: str = ...
    oncreatedscript: str = ...
    prompt_type: ToolPromptType = ...
    prompt_messages: list[str] | None = ...
    prompt_input_nodes: list[hou.Node] | None = ...
    prompt_posparms: list[str | None] | None = ...
    prompt_bboxes: list[hou.BoundingBox | None] | None = ...
    expand_to_dir: bool = ...
    callback: ParsingCallback | None = ...
    target_name_in_data = ...
    def __post_init__(self) -> None: ...

@dataclasses.dataclass
class ToolRecipeOptionsSetting(ClusterOptionsSetting):
    pane: hou.Pane | None = ...
    network_editor: hou.NetworkEditor | None = ...
    scene_viewer: hou.SceneViewer | None = ...
    parent: hou.Node | None = ...
    tool_inputs: Sequence[tuple[str, int]] = ...
    tool_outputs: Sequence[tuple[str, int]] = ...
    external_connections: bool = ...
    drop_on_wire: bool = ...
    click_to_place: bool = ...
    avoid_overlap: bool = ...
    frame: bool = ...
    prompt: bool = ...
    prescript: bool = ...
    postscript: bool = ...

@dataclasses.dataclass
class DataRecipeOptions(Options):
    data_category: str = ...
    process_order: float = ...
    expand_to_dir: bool = ...
    comment: str = ...

@dataclasses.dataclass
class ParmUIOptions(BaseOptions):
    recipecategory: str = ...
    internalname: str = ...
    file: str = ...
    label: str = ...
    visible: bool = ...
    dosubmenu: bool = ...
    submenu: str = ...
    icon: str = ...
    comment: str = ...
    usenodetypepatterns: bool = ...
    nodetypepatterns: str = ...
    useparmnamepatterns: bool = ...
    parmnamepatterns: str = ...
    parmtypepatterns: str = ...
    parmtemplates: ParmTemplateOptionType = ...
    parms: list[str] | None = ...
    briefparms: bool = ...
    children: bool = ...
    editables: bool = ...
    nodes_only: bool = ...
    flags: bool = ...
    parmfilter: bool = ...
    metadata: bool = ...
    verbose: bool = ...
    recorddata: bool = ...
    evaluate: bool = ...
    prescript: str = ...
    postscript: str = ...
    oncreatedscript: str = ...
