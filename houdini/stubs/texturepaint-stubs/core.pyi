import _cop as COP
import dbg as DBG
import enum as ENUM
import hou as HOU
import numpy as NP
import re
import typing
import typing as TY
from collections.abc import Callable as Callable, Collection, Iterable, Mapping, MutableMapping, Sequence
from dataclasses import dataclass as DATACLASS
from houtypes import NodeEventKwargs, RadialMenuKwargs
from hrecipes import rtypes as rtypes
from numpy.typing import NDArray as NDArray
from types import TracebackType
from typing import Literal, Protocol, Required, TypedDict, Unpack

from typing import TypeAlias
from typing import TypeAlias
_CopOutput: TypeAlias = HOU.ImageLayer | HOU.NanoVDB | HOU.DetachedAttrib | HOU.Geometry
_VerbParmValue: TypeAlias = HOU.OptionMultiArgType | HOU.Ramp
_VerbParms: TypeAlias = Mapping[str, _VerbParmValue | Sequence[Mapping[str, _VerbParmValue]]]
class _CopInvoke(Protocol):
    def __call__(self, inputs: Mapping[str, _CopOutput | None] = ..., /) -> dict[str, _CopOutput]: ...

class _CopVerbFn(Protocol):
    def __call__(self, parms: _VerbParms = ..., /) -> _CopInvoke: ...

class _SopInvoke(Protocol):
    def __call__(self, inputs: Sequence[HOU.Geometry], output: HOU.Geometry | None = ..., /) -> HOU.Geometry: ...

class _SopVerbFn(Protocol):
    def __call__(self, parms: _VerbParms = ..., /) -> _SopInvoke: ...

class _SavedData(TypedDict, total=False):
    name: Required[str]
    is_visible: Required[bool]
    blend_mode: Required[str]
    opacity: float
    mask_active: bool | int
    child_nids: list[int] | tuple[int, ...]

class _RecipePrescriptKwargs(TypedDict):
    name: str
    HDADefinition: HOU.HDADefinition
    node: HOU.OpNode
    data: rtypes.RecipeData

class _RecipeCreatedKwargs(TypedDict):
    name: str
    HDADefinition: HOU.HDADefinition
    node: HOU.OpNode
    parm: HOU.ParmTuple | None

class _Invoke(Protocol):
    def __call__(self, *inputs: _CopOutput) -> list[_CopOutput]: ...

AddDynOut: type[COP.AddDynOut]
MultDynIn: type[COP.MultDynIn]
MultDynOut: type[COP.MultDynOut]

class ParmNames(ENUM.StrEnum):
    BLEND_TREE = 'blendtree'
    CANVAS_SELECT = 'canvasselect'
    GROUP = 'group'
    LAYERS = 'layers'
    LAYERS_UPDATED_SIGNAL = 'layersupdatedsignal'
    LAZY_MOUSE_RADIUS = 'lazymouseradius'
    MASK_VIS = 'maskvis'
    MASK_WRITE = 'maskwrite'
    PAINT_2D = 'paint2d'
    SIGNATURE = 'signature'
    STROKE_ALIGN = 'strokealign'
    TOOL = 'tool'
    USE_LAZY_MOUSE = 'uselazymouse'
    WRITING_LAYER_NAME = 'writinglayername'

class SavedDataFieldNames(ENUM.StrEnum):
    BLEND_MODE = 'blend_mode'
    CHILD_NIDS = 'child_nids'
    IS_VISIBLE = 'is_visible'
    MASK_ACTIVE = 'mask_active'
    NAME = 'name'
    OPACITY = 'opacity'

class Names(ENUM.StrEnum):
    ASCII = 'ascii'
    ALPHA = 'alpha'
    BASE_SIZE = 'basesize'
    BASE64 = 'base64'
    BLEND = 'blend'
    BRIGHT = 'bright'
    BG = 'bg'
    CAMERA_REF = 'camera_ref'
    COLOUR = 'colour'
    CROP = 'crop'
    DATATYPE = 'datatype'
    ID = 'id'
    INVOKE_BLOCK = 'invokeblock'
    INVOKE_GEO = 'invokegeo'
    FILE = 'file'
    FG = 'fg'
    GAMMA = 'gamma'
    LAYER = 'layer'
    MASK = 'mask'
    MODE = 'mode'
    NODE = 'node'
    PIXEL_SCALE = 'pixelscale'
    PREVIEW_RASTER_GENERATION_INHIBITOR = 'preview_raster_generation_inhibitor'
    RES = 'res'
    RESAMPLE = 'resample'
    RESOLUTION = 'resolution'
    RESULT = 'result'
    RGB = 'rgb'
    RGBA = 'rgba'
    SET_PIXEL_SCALE = 'setpixelscale'
    SET_RES = 'setres'
    SIGNATURE = 'signature'
    SIZE_REF = 'size_ref'
    SPACE = 'space'
    STAMP = 'stamp'
    SOURCE = 'source'
    VALUE = 'value'
    XFORMS = 'xforms'

class StampAttribName(ENUM.StrEnum):
    SPACE = 'stamp_space'
    IS_PERSP = 'stamp_is_persp'
    RIGHT = 'stamp_right'
    UP = 'stamp_up'
    BACK = 'stamp_back'
    CLIP = 'stamp_clip'
    FLOW = 'stamp_flow'

class Space(ENUM.IntEnum):
    SURFACE = 0
    SCREEN = 1
    COUNT = 2

@DATACLASS
class SpaceDesc:
    short_name: str
    label: str

SPACE_DESCS: tuple[SpaceDesc, SpaceDesc]
EVAL_INTERMEDIATE_CHAN_C: int
FILEPATH_OPDEF_PREFIX: str
IS_VISUALLY_REVERSED: bool
DEFAULT_BLEND_MODE: str
DEFAULT_OPACITY: float
DEFAULT_INT_ATTR_VAL: int
ROOT_NID: int
NAME_REGEX: re.Pattern[str]
DATATYPE_NAMES: tuple[str, str, str]
SHOULD_DEBUG_CRASH: bool

class OpNodeInputs(ENUM.IntEnum):
    CANVAS = 0
    UV_GEO = 1

class AlphaType(ENUM.IntEnum):
    SQUARE = 0
    CIRCLE = 1
    FILE = 2
    CATALOGUE = 3

class CatalogueAlphaType(ENUM.IntEnum):
    SQUARE = 0
    CIRCLE = 1
    FILE = 2

class Orient(ENUM.IntEnum):
    TAN_DURING_STROKE = 0
    UP_DIR_ALWAYS = 1

@DATACLASS
class ToolProps:
    name: str | None
    label: str
    modifies_layer: bool

class Tool(ENUM.IntEnum):
    PAINT = 0
    ERASE = 1
    SMOOTH = 2
    SAMPLE = 3
    FILL = 4
    ADJUST_BRUSH_RADIUS = 5
    ADJUST_LM_RADIUS = 6
    def props(self: TY.Self) -> ToolProps: ...

TOOL_PROPS: tuple[ToolProps, ToolProps, ToolProps, ToolProps, ToolProps, ToolProps, ToolProps]
BRUSH_TOOLS: tuple[Tool, Tool, Tool]
ADJUST_TOOLS: tuple[Tool, Tool]
BRUSH_PREVIEW_HDA_SXN_NAME: str

@DATACLASS
class RecipeTypeProps:
    plural_label: str
    alpha_raster_hda_sxn_name: str

RECIPE_TYPE_PROPS: tuple[RecipeTypeProps, RecipeTypeProps]

class RecipeType(ENUM.IntEnum):
    ALPHA = 0
    BRUSH = 1
    def props(self: TY.Self) -> RecipeTypeProps: ...

@DATACLASS
class Dynamics:
    flow: COP.MultDynOut | None
    radius: COP.MultDynOut | None
    rotation: COP.AddDynOut | None
    def quote(self: TY.Self, ns_expr: str) -> str: ...
    def to_parm_dict(self: TY.Self, tool_name: str | None) -> dict[str, float | bool]: ...

def quote_add_dyn_out(ns_expr: str, dyn_out: COP.AddDynOut | None) -> str: ...
def quote_mult_dyn_in(ns_expr: str, dyn_in: COP.MultDynIn | None) -> str: ...
def quote_mult_dyn_out(ns_expr: str, dyn_out: COP.MultDynOut | None) -> str: ...
def opnode_get_dynamics(paint_node: HOU.OpNode, tool: Tool) -> Dynamics: ...
@DBG.ZoneScopedDecorator
def opnode_get_common_stroke_parms(paint_node: HOU.OpNode, tool: Tool) -> COP.CommonStrokeParms: ...

PROCEDURAL_ALPHA_TYPES: tuple[AlphaType, AlphaType]

@DATACLASS
class ProceduralAlphaParms:
    xy_falloff: float

@DATACLASS
class AlphaRecipe:
    type: CatalogueAlphaType
    parms: ProceduralAlphaParms | None

@DATACLASS
class UniformBrushParms:
    opacity: float
    flow_static: float
    spacing: float
    flow_comp: bool
    rot_static: float
    orient_screen: Orient
    orient_surf: Orient
    squish: float
    z_falloff: float

class UniformBrushParm(ENUM.StrEnum):
    OPACITY = 'opacity'
    FLOW_STATIC = 'flowstatic'
    SPACING = 'spacing'
    FLOW_COMP = 'flowcomp'
    ROT_STATIC = 'rotstatic'
    ORIENT_SCREEN = 'orientscreen'
    ORIENT_SURF = 'orientsurf'
    SQUISH = 'alphasquish'
    Z_FALLOFF = 'alphazfalloff'

BRUSH_PARM_NAMES: tuple[UniformBrushParm, UniformBrushParm, UniformBrushParm, UniformBrushParm, UniformBrushParm, UniformBrushParm, UniformBrushParm, UniformBrushParm, UniformBrushParm]

@DATACLASS
class BrushRecipe:
    alpha: AlphaRecipe
    uniform: UniformBrushParms
    dynamics: Dynamics

class RecipeAPIParmName:
    DATA: str
    HDA_DEFINITION: str
    NAME: str
    NODE: str
    PARMS: str

def recipe_to_internal_filepath_prefix(recipe_name: str) -> str: ...
def recipe_to_alpha_raster_filepath(recipe_type: RecipeType, recipe_name: str) -> str: ...
def recipe_to_brush_filepath(recipe_name: str) -> str: ...
def recipe_prescript_parms_inject_parm_data(recipe_prescript_kwargs: _RecipePrescriptKwargs) -> rtypes.ParmDataDict: ...
def make_recipe_assign_parm(parm_data: MutableMapping[str, rtypes.ParmUnionData], recipe_prescript_kwargs: _RecipePrescriptKwargs) -> Callable[[str, rtypes.ParmUnionData], None]: ...
def apply_recipe_alpha(recipe_prescript_kwargs: _RecipePrescriptKwargs, parm_data: MutableMapping[str, rtypes.ParmUnionData], recipe_type: RecipeType, recipe_alpha: AlphaRecipe) -> None: ...
def apply_alpha_recipe(recipe_prescript_kwargs: _RecipePrescriptKwargs, recipe: AlphaRecipe) -> None: ...
def apply_brush_recipe(recipe_prescript_kwargs: _RecipePrescriptKwargs, recipe: BrushRecipe) -> None: ...
def hda_insert_mono_layer_as_section(hda: HOU.HDADefinition, sxn_name: str, layer: HOU.ImageLayer) -> None: ...
def on_recipe_created(recipe_type: RecipeType, kwargs: _RecipeCreatedKwargs) -> None: ...

class FlowCompensationBlendMode(ENUM.IntEnum):
    NONE = 0
    ADD = 1
    OVER = 2

@DATACLASS
class BrushToolProps:
    blend_mode: int | None

BRUSH_TOOL_PROPS: tuple[BrushToolProps, BrushToolProps, BrushToolProps]

def match_grid_to_layer(grid_geo: HOU.Geometry, layer: HOU.ImageLayer, should_tile_3x3: bool) -> None: ...

class StampPointWrapMode(ENUM.IntEnum):
    OFF = 1
    ON = 2

class StampPointSpace(ENUM.IntEnum):
    IMAGE = 0
    WORLD = 1

class StampPointBlendMode(ENUM.IntEnum):
    ORDERED_OVER = 0
    ORDER_INDEPENDENT_OVER = 1
    ADD = 2
    SUBTRACT = 3
    MULTIPLY = 4
    MAXIMUM = 5
    MINIMUM = 6

def invoke_stamp_points(signature: str, blend_mode: StampPointBlendMode, xforms: HOU.Geometry, pos: HOU.ImageLayer, stamp: HOU.ImageLayer, alpha_type: int, xy_falloff: float, z_falloff: float, is_geo: bool, is_tile_wrap: bool, tile_img_space_size: Sequence[float]) -> HOU.ImageLayer: ...

@DATACLASS
class ParentPtr:
    parent_nid: int
    idx_in_parent: int

@DATACLASS
class EphData:
    pp: ParentPtr | None

make_cop_verb: Callable[[str], HOU.OpVerb | None]
make_sop_verb: Callable[[str], HOU.OpVerb | None]

def cop_verb(name: str) -> _CopVerbFn: ...
def sop_verb(name: str) -> _SopVerbFn: ...

class InvokeType:
    MONO: int
    UV: int
    RGB: int
    RGBA: int
    ID: int
    GEO: int
    IVDB: int
    FVDB: int
    VVDB: int
    CABLE: int

def make_invoke(program_geo: HOU.Geometry, input_specs: Iterable[tuple[str, int]], output_specs: Collection[tuple[str, int]]) -> _Invoke: ...
def make_geo_invoke(program_geo: HOU.Geometry, input_labels: Iterable[str], output_labels: Iterable[str]) -> _Invoke: ...
def radial_menu_set_tool(tool: Tool, kwargs: RadialMenuKwargs) -> None: ...

COP_VERB_BLEND: _CopVerbFn
COP_VERB_BRIGHT: _CopVerbFn
COP_VERB_FILE: _CopVerbFn
COP_VERB_LAYER: _CopVerbFn
COP_VERB_RESAMPLE: _CopVerbFn
COP_VERB_XFORM_2D: _CopVerbFn

def chan_c_to_sig(chan_c: int) -> str: ...
def layer_to_sig(layer: HOU.ImageLayer) -> str: ...
def constant_layer(res: tuple[int, int] | None, size_ref: HOU.ImageLayer | None, value: Sequence[float]) -> HOU.ImageLayer: ...
def size_ref_layer(res: tuple[int, int]) -> HOU.ImageLayer: ...
def densify_layer(layer: HOU.ImageLayer) -> HOU.ImageLayer: ...
def load_layer_from_file(filepath: str) -> HOU.ImageLayer: ...
def flip_layer(layer: HOU.ImageLayer) -> HOU.ImageLayer: ...
def resample_layer(layer: HOU.ImageLayer, res: tuple[int, int]) -> HOU.ImageLayer: ...
def numpy_encode_gamma(arr: NDArray[NP.uint8]) -> None: ...
def clear_layer(layer: HOU.ImageLayer, value: float) -> HOU.ImageLayer: ...
def zero_layer(layer: HOU.ImageLayer) -> HOU.ImageLayer: ...
def get_input_layer_image_space_size() -> list[float]: ...

UNDO_GROUP_LABEL_PREFIX: str
undo_group: Callable[[str], HOU.UndosGroup]

def saved_data_is_folder(sd: _SavedData) -> bool: ...
def saved_data_child_c(sd: _SavedData) -> int | None: ...
def saved_data_flip_child_idx_excl(sd: _SavedData, child_idx: int) -> int: ...
def saved_data_flip_child_idx_incl(sd: _SavedData, child_idx: int) -> int: ...

class ImageUsage(ENUM.IntEnum):
    COLOUR = 0
    ALPHA = 1
    MASK = 2

USAGE_STRS: tuple[str, str, str]

@DATACLASS
class ImageId:
    name: str
    usage: ImageUsage

class BadCableFieldName(Exception): ...

def make_cable_field_name(name: str, usage: ImageUsage) -> str: ...
@typing.overload
def make_cable_field_names(name: str, include_mask: Literal[False]) -> tuple[str, str]: ...
@typing.overload
def make_cable_field_names(name: str, include_mask: Literal[True]) -> tuple[str, str, str]: ...
@typing.overload
def make_cable_field_names(name: str, include_mask: bool) -> tuple[str, str] | tuple[str, str, str]: ...
def destruct_cable_field_name(name: str) -> ImageId: ...
def cable_has_field_name(cable: HOU.CopCable, fname: str) -> bool: ...
def opnode_get_alpha_scale_x(paint_node: HOU.OpNode, tool: Tool) -> float: ...
def opnode_get_static_rotation(paint_node: HOU.OpNode, tool: Tool) -> float: ...
def opnode_get_curr_alpha_parm(paint_node: HOU.OpNode, parm_name_suffix: str) -> int | float | str: ...
def opnode_get_blend_mode_parm(paint_node: HOU.OpNode) -> HOU.Parm | None: ...
def opnode_get_blend_mode_names(paint_node: HOU.OpNode) -> tuple[str, ...]: ...
def opnode_get_writing_layer_name(paint_node: HOU.OpNode) -> str: ...
def opnode_set_writing_layer_name(paint_node: HOU.OpNode, new_lname: str) -> None: ...
def opnode_get_layers(paint_node: HOU.OpNode) -> HOU.CopCable: ...
def opnode_set_layers(paint_node: HOU.OpNode, new_layers: HOU.CopCable | None) -> None: ...
def opnode_get_writing_colour(paint_node: HOU.OpNode) -> HOU.ImageLayer | None: ...
def opnode_get_writing_chan_c(paint_node: HOU.OpNode) -> int | None: ...
def opnode_get_out_chan_c(paint_node: HOU.OpNode) -> int: ...
def opnode_get_internals(paint_node: HOU.OpNode, chan_c: int) -> HOU.OpNode | None: ...
def opnode_get_blank_mono(paint_node: HOU.OpNode) -> HOU.ImageLayer | None: ...
def opnode_get_blank_colour(paint_node: HOU.OpNode, chan_c: int) -> HOU.ImageLayer | None: ...
def chan_c_to_invoke_type(chan_c: int) -> int: ...
def opnode_get_convert(paint_node: HOU.OpNode, in_chan_c: int, out_chan_c: int) -> Callable[[HOU.ImageLayer], HOU.ImageLayer]: ...
def opnode_get_lmb_tool(paint_node: HOU.OpNode) -> Tool: ...
def opnode_get_lmb_tool_name(paint_node: HOU.OpNode) -> str | None: ...
def opnode_get_lmb_brush_or_paint(paint_node: HOU.OpNode) -> Tool: ...
def opnode_get_blend_tree(paint_node: HOU.OpNode) -> dict[str, _SavedData] | None: ...

@DATACLASS
class ColourAlpha:
    colour: HOU.ImageLayer
    alpha: HOU.ImageLayer

@DATACLASS
class PaintLayer:
    colour_alpha: ColourAlpha
    mask: HOU.ImageLayer | None

@DATACLASS
class PaintLayerDesc:
    value: PaintLayer | None

@DATACLASS
class PendingNewNodeSrc:
    name: str | None
    value: PaintLayerDesc | None

@DATACLASS
class NewNodesSrc:
    nids: tuple[int, ...]

@DATACLASS
class PrefixedRange:
    parent_nid: int
    start_i: int
    end_i: int
    def rows(self: TY.Self, model: Model) -> tuple[int, int]: ...

@DATACLASS
class NullDst: ...

NULL_DST: NullDst

@DATACLASS
class InternalDst:
    parent_nid: int
    i: int
MoveSrc = NewNodesSrc | PrefixedRange
MoveDst = NullDst | InternalDst

class ModelListener:
    def before_reset(self: TY.Self) -> None: ...
    def after_reset(self: TY.Self) -> None: ...
    def on_layers_changed(self: TY.Self) -> None: ...
    def on_canvas_select_changed(self: TY.Self) -> None: ...
    def on_writing_layer_changed(self: TY.Self) -> None: ...
    def on_datatype_changed(self: TY.Self) -> None: ...
    def on_res_changed(self: TY.Self) -> None: ...
    def on_blend_mode_changed(self: TY.Self) -> None: ...

def blend_tree_get_saved_data(blend_tree: Mapping[str, _SavedData], nid: int) -> _SavedData: ...
def blend_tree_get_nid_range(blend_tree: Mapping[str, _SavedData], nid: int) -> PrefixedRange: ...
def opnode_get_root_range(paint_node: HOU.OpNode) -> PrefixedRange: ...
def layers_get_colour_alpha(layers: HOU.CopCable, lname: str) -> ColourAlpha: ...
def layers_get_paint_layer(layers: HOU.CopCable, lname: str) -> PaintLayer: ...
def opnode_partial_eval(paint_node: HOU.OpNode, pr: PrefixedRange, canvas: HOU.ImageLayer) -> HOU.ImageLayer: ...
def opnode_partial_eval_and_split(paint_node: HOU.OpNode, pr: PrefixedRange, canvas: HOU.ImageLayer) -> ColourAlpha: ...

class Model:
    opnode: HOU.OpNode | None
    is_pushing_update: bool
    listeners: list[ModelListener]
    def __init__(self: TY.Self, opnode: HOU.OpNode | None = None) -> None: ...
    def set_opnode(self: TY.Self, opnode: HOU.OpNode | None) -> None: ...
    def on_deleting_opnode(self: TY.Self, **kwargs: Unpack[NodeEventKwargs]) -> None: ...
    def destroy(self: TY.Self) -> None: ...
    def __enter__(self: TY.Self) -> TY.Self: ...
    def __exit__(self: TY.Self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
    id_to_eph_data: dict[int, EphData]
    lname_to_nid: dict[str, int]
    next_nid: int
    def init_empty(self: TY.Self) -> None: ...
    def nid_to_saved_data(self: TY.Self, nid: int) -> _SavedData: ...
    def root_saved_data(self: TY.Self) -> _SavedData: ...
    def is_empty(self: TY.Self) -> bool: ...
    def delete_all(self: TY.Self) -> None: ...
    def push_blend_tree(self: TY.Self) -> None: ...
    def saved_to_eph(self: TY.Self, saved_data: _SavedData) -> EphData: ...
    def debug_print(self: TY.Self) -> None: ...
    def add_listener(self: TY.Self, listener: ModelListener) -> None: ...
    def remove_listener(self: TY.Self, listener: ModelListener) -> None: ...
    def add_layer(self: TY.Self, lname: str, value: PaintLayer | None) -> None: ...
    def pull_blend_tree(self: TY.Self) -> bool: ...
    def writing_nid(self: TY.Self) -> int | None: ...
    def set_mask_write(self: TY.Self, is_mask_write: bool) -> None: ...
    def select_canvas(self: TY.Self) -> None: ...
    def write_to_nid(self: TY.Self, nid: int, is_mask_write: bool | None, signal: bool) -> None: ...
    def node_colour(self: TY.Self, nid: int) -> HOU.ImageLayer: ...
    def node_name(self: TY.Self, nid: int) -> str: ...
    def set_node_name(self: TY.Self, nid: int, new_name: str) -> None: ...
    def node_vis(self: TY.Self, nid: int) -> bool: ...
    def set_node_vis(self: TY.Self, nid: int, is_vis: bool) -> None: ...
    def node_chan_c(self: TY.Self, nid: int) -> int: ...
    def set_node_chan_c(self: TY.Self, nid: int, value: int) -> None: ...
    def node_res(self: TY.Self, nid: int) -> tuple[int, int]: ...
    def on_update_res(self: TY.Self) -> None: ...
    def set_node_res(self: TY.Self, nid: int, res: tuple[int, int]) -> None: ...
    def set_all_nodes_res(self: TY.Self, res: tuple[int, int]) -> None: ...
    def node_blend_mode(self: TY.Self, nid: int) -> str: ...
    def set_node_blend_mode(self: TY.Self, nid: int, blend_mode: str) -> None: ...
    def node_opacity(self: TY.Self, nid: int) -> float: ...
    def set_node_opacity(self: TY.Self, nid: int, value: float) -> None: ...
    def has_mask(self: TY.Self, nid: int) -> bool: ...
    def add_mask(self: TY.Self, nid: int, is_white: bool) -> bool: ...
    def toggle_mask(self: TY.Self, nid: int) -> None: ...
    def delete_mask(self: TY.Self, nid: int) -> None: ...
    def merge(self: TY.Self, pr: PrefixedRange) -> None: ...
    def duplicate(self: TY.Self, pr: PrefixedRange) -> None: ...
    def notify_before_reset(self: TY.Self) -> None: ...
    def notify_after_reset(self: TY.Self) -> None: ...
    def notify_writing_layer_changed(self: TY.Self) -> None: ...
    def on_parm_changed(self: TY.Self, **kwargs: Unpack[NodeEventKwargs]) -> None: ...
    def find_unused_layer_name(self: TY.Self, lname: str) -> str: ...
    def make_new_nodes(self: TY.Self, srcs: Iterable[PendingNewNodeSrc]) -> NewNodesSrc: ...
    def add_new_created(self: TY.Self, dst: InternalDst, src: MoveSrc) -> bool: ...
    def add_new(self: TY.Self, dst: InternalDst, src: Collection[PendingNewNodeSrc]) -> bool: ...
    def delete(self: TY.Self, pr: PrefixedRange) -> bool: ...
    def move_nodes(self: TY.Self, src: MoveSrc, dst: MoveDst) -> bool: ...
    def move_nodes_impl(self: TY.Self, src: MoveSrc, dst: MoveDst) -> bool: ...
