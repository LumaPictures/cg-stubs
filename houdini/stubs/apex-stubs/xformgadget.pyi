import apex.xformgadgetutils as xgu
import hou
import kinefx.stateutils as ksu
import logging
import statehud.config as config
import typing
from apex.ui.statecommandutils import SWITCH_HANDLE_TOOL_CMD as SWITCH_HANDLE_TOOL_CMD
from apex.utils import timing as timing
from collections.abc import Collection, Iterable, Mapping, Sequence
from enum import Enum
from houtypes import SceneViewerEventKwargs, ViewerParmProperties, ViewerStateCommandKwargs, ViewerStateDrawKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs, ViewerStateParmChangeKwargs, ViewerStateVolatileClientKwargs
from typing import Final, Literal, NotRequired, ReadOnly, TypeAlias, Unpack
from typing_extensions import TypedDict

from typing import TypeAlias
from collections.abc import Callable
from typing import Never
_XformMode: TypeAlias = Literal['x', 't', 'r', 's', 'c']
_AlignMode: TypeAlias = Literal['world', 'local', 'c-plane', 'view', 'parent']
_IntSettingKey: TypeAlias = Literal['rOrd', 'xOrd', 'pre_rOrd', 'pre_xOrd', 'separate_align', 'gimbal_mode', 'pivot_mode', 'visible']
_AlignSettingKey: TypeAlias = Literal['t_alignment', 'r_alignment', 's_alignment']
_StrSettingKey: TypeAlias = Literal['name', 'label']
_HandleSettingValue: TypeAlias = int | str | dict[str, int] | dict[_XformMode, bool] | hou.Vector3
_MetadataLimitKey: TypeAlias = Literal['rot_limit_lower', 'rot_limit_upper', 'trans_limit_lower', 'trans_limit_upper', 'scale_limit_lower', 'scale_limit_upper', 'base_rotations', 'ds']
_EventKwargs: TypeAlias = ViewerStateKwargs | dict[str, Never]
_HandleUpdateCallback: TypeAlias = Callable[[_HandleUpdateKwargs], object]
_HandleStartUpdateCallback: TypeAlias = Callable[[_HandleStartUpdateKwargs], object]
_HandleSettingsUpdateCallback: TypeAlias = Callable[[_HandleSettingsUpdateKwargs], object]
_HandleSettingsEventCallback: TypeAlias = Callable[[_HandleSettingsEventKwargs], object]
_HandleHoverCallback: TypeAlias = Callable[[str | None, int, hou.EnumValue[hou.uiEventReason]], object]
_HandleCustomActionCallback: TypeAlias = Callable[[_HandleCustomActionKwargs], object]
_ExternalPickCallback: TypeAlias = Callable[[ViewerStateEventKwargs], _ExternalPick | None]
_HandleVisCallback: TypeAlias = Callable[[_HandleVisEvent], object]
DragInfoTuple: TypeAlias = tuple[str | None, int]
class _HandleSettings(TypedDict):
    rOrd: int
    xOrd: int
    pre_rOrd: int
    pre_xOrd: int
    xform_mode: _XformMode
    t_alignment: _AlignMode
    r_alignment: _AlignMode
    s_alignment: _AlignMode
    separate_align: int
    name: str
    label: str
    gimbal_mode: int
    pivot_mode: int
    enabled_components: dict[str, int]
    visible: int
    enabled_modes: dict[_XformMode, bool]
    reflection_hint: hou.Vector3
    has_reflection_hint: bool

class _HandleSettingsUpdate(TypedDict, total=False):
    rOrd: ReadOnly[int]
    xOrd: ReadOnly[int]
    pre_rOrd: ReadOnly[int]
    pre_xOrd: ReadOnly[int]
    xform_mode: ReadOnly[_XformMode]
    t_alignment: ReadOnly[_AlignMode]
    r_alignment: ReadOnly[_AlignMode]
    s_alignment: ReadOnly[_AlignMode]
    separate_align: ReadOnly[int]
    name: ReadOnly[str]
    label: ReadOnly[str]
    gimbal_mode: ReadOnly[int]
    pivot_mode: ReadOnly[int]
    enabled_components: ReadOnly[dict[str, int]]
    visible: ReadOnly[int]
    enabled_modes: ReadOnly[dict[_XformMode, bool]]
    reflection_hint: ReadOnly[hou.Vector3]
    has_reflection_hint: ReadOnly[bool]

class _HandleMetadata(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    centroid_xform: hou.Matrix4
    rot_limit_lower: hou.Vector3 | None
    rot_limit_upper: hou.Vector3 | None
    trans_limit_lower: hou.Vector3 | None
    trans_limit_upper: hou.Vector3 | None
    scale_limit_lower: hou.Vector3 | None
    scale_limit_upper: hou.Vector3 | None
    base_rotations: hou.Vector3 | None
    ds: hou.Vector3 | None

class _HandleUpdateKwargs(TypedDict):
    index: int
    name: str
    parms: dict[str, hou.Vector3]
    event_kwargs: _EventKwargs | None
    in_undo: bool
    interactive: bool

class _HandleStartUpdateKwargs(_HandleUpdateKwargs):
    component: str
    pivot_mode: int

class _HandleSettingsEventKwargs(TypedDict):
    index: int
    name: str
    event_kwargs: _EventKwargs | None
    in_undo: bool

class _HandleSettingsUpdateKwargs(_HandleSettingsEventKwargs):
    settings: _HandleSettings

class _HandleCustomActionKwargs(TypedDict):
    index: int
    menu_item: str
    event_kwargs: ViewerStateMenuActionKwargs | None

class _HandleVisEvent(TypedDict, total=False):
    index: int

class _ExternalPick(TypedDict, total=False):
    pos0: hou.Vector3
    pos1: hou.Vector3
    name: str
    xform: hou.Matrix4

class _CustomMenuItem(TypedDict):
    item: str
    broadcast: NotRequired[bool]
XFORM_HANDLE_SUBGRAPH_NAME: str
SNAPPING_SUBGRAPH_NAME: str
HK_INCREASE_HANDLE_SIZE: str
HK_DECREASE_HANDLE_SIZE: str
XAXIS_COLOR_NAME: str
YAXIS_COLOR_NAME: str
ZAXIS_COLOR_NAME: str
PIVOT_COLOR_NAME: str
VIEWRING_COLOR_NAME: str
ROTSPHERE_COLOR_NAME: str
HLGLOW_COLOR_NAME: str
HLSELGLOW_COLOR_NAME: str
MENU_NAME: tuple[str, str]
CENTER_COMP: str
CENTER_PIVOT_COMP: str
CENTER_SPHERE_COMP: str
CENTER_ALIGNED_COMP: str
XAXIS_COMP: str
YAXIS_COMP: str
ZAXIS_COMP: str
BASE_AXES: list[str]
XAXIS_ARROW_COMP: str
YAXIS_ARROW_COMP: str
ZAXIS_ARROW_COMP: str
XAXIS_PIVOT_COMP: str
YAXIS_PIVOT_COMP: str
ZAXIS_PIVOT_COMP: str
XAXIS_ARROW_PIVOT_COMP: str
YAXIS_ARROW_PIVOT_COMP: str
ZAXIS_ARROW_PIVOT_COMP: str
XAXIS_INSIDE_COMP: str
YAXIS_INSIDE_COMP: str
ZAXIS_INSIDE_COMP: str
XAXIS_ARROW_INSIDE_COMP: str
YAXIS_ARROW_INSIDE_COMP: str
ZAXIS_ARROW_INSIDE_COMP: str
XAXIS_SCALE_COMP: str
YAXIS_SCALE_COMP: str
ZAXIS_SCALE_COMP: str
XAXIS_SPHERE_COMP: str
YAXIS_SPHERE_COMP: str
ZAXIS_SPHERE_COMP: str
XAXIS_SPHERE_INV_COMP: str
YAXIS_SPHERE_INV_COMP: str
ZAXIS_SPHERE_INV_COMP: str
XAXIS_RING_COMP: str
YAXIS_RING_COMP: str
ZAXIS_RING_COMP: str
XAXIS_SPHERE_PIV_COMP: str
YAXIS_SPHERE_PIV_COMP: str
ZAXIS_SPHERE_PIV_COMP: str
XAXIS_RING_PIV_COMP: str
YAXIS_RING_PIV_COMP: str
ZAXIS_RING_PIV_COMP: str
HIDDEN_ROTATE_SPHERE_COMP: str
HIDDEN_ROTATE_BORDER_COMP: str
VIEW_RING_COMP: str
XY_PLANE_COMP: str
XZ_PLANE_COMP: str
YZ_PLANE_COMP: str
XY_PLANE_INSIDE_COMP: str
XZ_PLANE_INSIDE_COMP: str
YZ_PLANE_INSIDE_COMP: str
HIDDEN_XY_PLANE_COMP: str
HIDDEN_XZ_PLANE_COMP: str
HIDDEN_YZ_PLANE_COMP: str
AXIS_NAMES: dict[str, list[str]]
HIGHLIGHT_EXPAND_GROUPS: list[list[str]]
SELECTION_EXPAND_GROUPS: list[list[str]]
NO_HIGHLIGHT_COMPONENTS: list[str]
HIDDEN_COMPONENTS: list[str]
ROT_ORDERS: list[ksu._RotateOrder]
XFORM_ORDERS: list[ksu._TransformOrder]
XFORM_MODE_X: str
XFORM_MODE_T: str
XFORM_MODE_R: str
XFORM_MODE_S: str
XFORM_MODE_C: str
XFORM_MODES: list[_XformMode]
TOOL_MODE_MAP: dict[str, _XformMode]
ALIGN_MODE_WORLD: str
ALIGN_MODE_LOCAL: str
ALIGN_MODE_CPLANE: str
ALIGN_MODE_VIEW: str
ALIGN_MODE_PARENT: str
ALIGNMENT_MODES: dict[_AlignMode, str]
ALIGNMENT_KEYS: list[_AlignMode]
PARM_TX: str
PARM_TY: str
PARM_TZ: str
TRANSLATE_PARMS: list[str]
PARM_RX: str
PARM_RY: str
PARM_RZ: str
ROTATE_PARMS: list[str]
PARM_SX: str
PARM_SY: str
PARM_SZ: str
SCALE_PARMS: list[str]
PARM_RVIEW: str
ENABLE_COMPONENTS: list[str]
ROT_ORDER_RADIO: str
XFORM_ORDER_RADIO: str
XFORM_MODE_RADIO: str
ALIGN_MODE_RADIO: str
ALIGN_R_MODE_RADIO: str
ALIGN_T_MODE_RADIO: str
ALIGN_S_MODE_RADIO: str
CYCLE_XFORM_MODE_ACTION: str
CYCLE_XFORM_MODE_BACKWARD_SYMBOL: str
MINIMIZE_ALL_ACTION: str
ALIGN_WORLD_AXES_ACTION: str
ALIGN_VIEW_AXES_ACTION: str
ALIGN_CPLANE_AXES_ACTION: str
ALIGN_OTHER_XFORM_ACTION: str
START_ORIENT_PICK_ACTION: str
CANCEL_ORIENT_PICK_ACTION: str
MOVE_PIVOT_WORLD_ORIGIN_ACTION: str
MOVE_PIVOT_CPLANE_ORIGIN_ACTION: str
MOVE_PIVOT_PROJECT_CPLANE_ACTION: str
MOVE_OTHER_XFORM_ACTION: str
SNAP_OTHER_XFORM_ACTION: str
REVERT_DEFAULT_ACTION: str
REVERT_CTRLS_DEFAULTS_ACTION: str
SNAP_TO_CENTROID_ACTION: str
SNAP_TO_PIVOT_ACTION: str
ALT_ROTATE_MODE_SYMBOL: str
CYCLE_ALIGN_MODE_SYMBOL: str
SWITCH_ALIGN_MODE_SYMBOL: str
TOGGLE_HANDLE_VIS_SYMBOL: str
KEY_COMP_T_ACTION: str
KEY_COMP_R_ACTION: str
KEY_COMP_S_ACTION: str
XFORM_MODE_MENU: str
ALIGN_MODE_MENU: str
ALIGN_R_MENU: str
ALIGN_T_MENU: str
ALIGN_S_MENU: str
MOVE_PIVOT_MENU: str
CONFIG_MENU: str
ROTATE_ORD_MENU: str
XFORM_ORD_MENU: str
ENABLE_COMP_MENU: str
SNAP_TO_MENU: str
KEY_COMP_MENU: str
REVERT_MENU: str
SEPARATE_ALIGN_TOGGLE: Final[str]
GIMBAL_MODE_TOGGLE: Final[str]
PIVOT_MODE_TOGGLE: Final[str]
MENU_ITEMS: list[str]
MENU_ITEMS_SET: set[str]
BROADCAST_MENU_ITEMS: list[str]
SINGLE_BROADCAST_MENU_ITEMS: list[str]
NON_BROADCAST_ITEMS: list[str]
PARM_UNDO_NAME: tuple[str, str]
SETTING_UNDO_NAME: tuple[str, str]
FACES_GEO_OUTPUT: str
LINES_GEO_OUTPUT: str
TRANSLATE_STEP_STATEPARM: str
ROTATE_STEP_STATEPARM: str
SCALE_STEP_STATEPARM: str
HANDLE_PREF_BTN_STATEPARM: str
CONFIG_STATE_PARMS_LIST: list[str]
ROT_ORD_PARM: Final[str]
XFORM_ORD_PARM: Final[str]
PRE_ROT_ORD_PARM: Final[str]
PRE_XFORM_ORD_PARM: Final[str]
XFORM_MODE_PARM: Final[str]
T_ALIGN_PARM: Final[str]
R_ALIGN_PARM: Final[str]
S_ALIGN_PARM: Final[str]
ALIGN_PARMS: tuple[str, str, str]
NAME_PARM: Final[str]
LABEL_PARM: Final[str]
ENABLED_COMPS_PARM: Final[str]
ENABLED_MODES_PARM: Final[str]
VISIBLE_PARM: Final[str]
REFLECTION_HINT_PARM: Final[str]
HAS_REFLECTION_HINT_PARM: Final[str]
TRANSLATE_PARM: str
ROTATE_PARM: str
SCALE_PARM: str
SHEAR_PARM: str
DELTA_SCALE_PARM: str
PIVOT_PARM: str
PIVOT_ROT_PARM: str
PRE_TRANSLATE_PARM: str
PRE_ROTATE_PARM: str
PRE_SCALE_PARM: str
PRE_SHEAR_PARM: str
HANDLE_PARMS_CONFIG_KEY: str
HANDLE_SETTINGS_CONFIG_KEY: str
HANDLE_METADATA_CONFIG_KEY: str
HANDLE_STATEPARMS_CONFIG_KEY: str
HANDLE_VERSION_CONFIG_KEY: str
HANDLE_CONFIG_VERSION: int
HANDLE_CONFIG_PREFIX: str
KEY_TRANSLATES_CMD: str
KEY_ROTATES_CMD: str
KEY_SCALES_CMD: str
CENTROID_KEY: str
ROT_LIMIT_LOWER_KEY: str
ROT_LIMIT_UPPER_KEY: str
TRANS_LIMIT_LOWER_KEY: str
TRANS_LIMIT_UPPER_KEY: str
SCALE_LIMIT_LOWER_KEY: str
SCALE_LIMIT_UPPER_KEY: str
BASE_ROT_KEY: str
DEFAULT_HANDLE_SCALE: float
DEFAULT_HANDLE_MIN_SCALE: float
DEFAULT_RADIUS_SCALE: float
DEFAULT_SHOW_PLANES: int
DEFAULT_SHOW_HIDDEN_PLANES: int
DEFAULT_SHOW_TUMBLE_SPHERE: int
DEFAULT_SHOW_TUMBLE_SPHERE_COMBINED: int
DEFAULT_SHOW_TUMBLE_BORDER: int
DEFAULT_CENTER_VIEW_ALIGNED: int
DEFAULT_HIDE_RINGS_VIEW_DIR: int
DEFAULT_SHOW_VIEW_RING: int
DEFAULT_AXES_OUTSIDE: int
DEFAULT_PLANES_OUTSIDE: int
DEFAULT_SHOW_NEGATIVE_AXES: int
DEFAULT_SHOW_ROT_SPHERES: int
DEFAULT_VIEW_RING_SCALE: float
DEFAULT_LINE_WIDTH: float
DEFAULT_TUMBLE_SPHERE_RADIUS_SCALE: float
DEFAULT_ARROW_TIP_SCALE: float
DEFAULT_ARROW_TIP_RADIUS_SCALE: float
DEFAULT_AXIS_BOX_SCALE: float
DEFAULT_PLANE_SCALE: float
DEFAULT_ROT_SPHERE_SCALE: float
DEFAULT_CENTER_XFORM_SCALE: float
DEFAULT_PIVOT_RADIUS_SCALE: float
DEFAULT_AXIS_LENGTH_SCALE: float
DEFAULT_CENTER_BOX_SCALE: float
DEFAULT_PLANE_OFFSET: float
DEFAULT_PLANE_OFFSET_OUTSIDE: float
DEFAULT_CLIP_DIST: float
DEFAULT_AXIS_OFFSET: float
DEFAULT_OUTSIDE_AXIS_LENGTH_SCALE: float
DEFAULT_OUTSIDE_AXIS_OFFSET: float
DEFAULT_HIDE_RINGS_VIEW_TOL: float
GRAPH_PARM_VP_MINVERTED: str
GRAPH_PARM_VP_SCALE: str
GRAPH_PARM_VP_VIEWDIR: str
GRAPH_PARM_VP_VIEWROT: str
GRAPH_PARM_VP_WORLDROT: str
GRAPH_PARM_VP_CPLANEROT: str
GRAPH_PARM_VP_RAYDIR_ARRAY: str
GRAPH_PARM_SHOW_PLANES: str
GRAPH_PARM_SHOW_HIDDEN_PLANES: str
GRAPH_PARM_LINE_WIDTH: str
GRAPH_PARM_AXES_OUTSIDE: str
GRAPH_PARM_PLANES_OUTSIDE: str
GRAPH_PARM_SHOW_NEGATIVE_AXES: str
GRAPH_PARM_VIEW_RING_SCALE: str
GRAPH_PARM_SHOW_TUMBLE_SPHERE: str
GRAPH_PARM_SHOW_TUMBLE_SPHERE_COMBINED: str
GRAPH_PARM_SHOW_TUMBLE_BORDER: str
GRAPH_PARM_CENTER_VIEW_ALIGNED: str
GRAPH_PARM_HIDE_RINGS_VIEW_DIR: str
GRAPH_PARM_SHOW_VIEW_RING: str
GRAPH_PARM_TUMBLE_SPHERE_SCALE: str
GRAPH_PARM_ARROW_TIP_SCALE: str
GRAPH_PARM_ARROW_TIP_RADIUS_SCALE: str
GRAPH_PARM_AXIS_BOX_SCALE: str
GRAPH_PARM_PLANE_SCALE: str
GRAPH_PARM_ROT_SPHERE_SCALE: str
GRAPH_PARM_CENTER_XFORM_SCALE: str
GRAPH_PARM_PIVOT_RADIUS_SCALE: str
GRAPH_PARM_AXIS_LENGTH_SCALE: str
GRAPH_PARM_CENTER_BOX_SCALE: str
GRAPH_PARM_PLANE_OFFSET: str
GRAPH_PARM_PLANE_OFFSET_OUTSIDE: str
GRAPH_PARM_CLIP_DIST: str
GRAPH_PARM_HIDE_RINGS_VIEW_TOL: str
GRAPH_PARM_SHOW_ROT_SPHERES: str
GRAPH_PARM_AXIS_OFFSET: str
GRAPH_PARM_OUTSIDE_AXIS_OFFSET: str
GRAPH_PARM_OUTSIDE_AXIS_LENGTH_SCALE: str
GRAPH_PARM_DEFAULTS: dict[str, float]
FLOAT_GRAPH_PARMS: list[str]
BOOL_GRAPH_PARMS: list[str]
CACHED_FLOAT_PARM_TOL: float
VECTOR_AND_MATRIX_GRAPH_PARMS: list[str]
IGNORE_CACHE_CHECK_GRAPH_PARMS: list[str]
GRAPH_PARM_HANDLE_SETTINGS: str
GRAPH_PARM_HANDLE_PARMS: str
GRAPH_PARM_CD_X: str
GRAPH_PARM_CD_Y: str
GRAPH_PARM_CD_Z: str
GRAPH_PARM_CD_C: str
GRAPH_PARM_CD_VIEW: str
GRAPH_PARM_CD_TUMBLE: str
GRAPH_PARM_CD_BORDER: str
GRAPH_PARM_CD_HL_FACES: str
GRAPH_PARM_CD_HL_LINES: str
GRAPH_PARM_CD_SEL_FACES: str
GRAPH_PARM_CD_SEL_LINES: str
GRAPH_PARM_LOCATE_NAME: str
GRAPH_PARM_LOCATE_INDEX: str
GRAPH_PARM_SELECT_NAME: str
GRAPH_PARM_SELECT_INDEX: str
GRAPH_PARM_IS_DRAGGING: str
GLOBAL_VARIABLE_PARMS: list[str]
PRIO_FACES_DRAWABLE: str
PRIO_LINES_DRAWABLE: str
FACES_DRAWABLE: str
LINES_DRAWABLE: str
HIDDEN_FACES_DRAWABLE: str
TRANSPARENT_FACES_DRAWABLE: str

def remap_gadget_params(params: hou._DrawableParams, is_handle: bool) -> hou._DrawableParams:
    """ Turn params for Geometry drawables into Gadget drawable params. """

class HandleMode(Enum):
    default_mode = 0
    orient_picking = 1
    copy_orient = 2
    copy_pivot = 3
    copy_all = 4

def getTRSFromXformMode(xform_mode: str) -> tuple[bool, bool, bool]:
    """ Get whether the xform mode has rotate, scales and translate components. """

INVALID_DRAG_INFO: DragInfoTuple

def addHotkeyActionItem(hotkey_definitions: hou.PluginHotkeyDefinitions, template: hou.ViewerStateTemplate | hou.ViewerHandleTemplate, menu: hou.ViewerStateMenu, code: str, label: str, state_cat: hou.NodeTypeCategory, key: str | Sequence[str] | None = None, hotkey_label: str | None = None, hk: str | None = None) -> None:
    """ Add a hotkey action menu item to the template. """
def addHotkeyToggleItem(hotkey_definitions: hou.PluginHotkeyDefinitions, template: hou.ViewerStateTemplate | hou.ViewerHandleTemplate, menu: hou.ViewerStateMenu, code: str, label: str, default_val: bool, state_cat: hou.NodeTypeCategory, key: str | Sequence[str] | None = None, hotkey_label: str | None = None) -> None:
    """ Add a hotkey toggle menu item to the template. """
def buildXformMenu(template: hou.ViewerStateTemplate | hou.ViewerHandleTemplate, main_menu: hou.ViewerStateMenu | None = None, main_hotkey_definitions: hou.PluginHotkeyDefinitions | None = None) -> None:
    """ Build the context menu for the xform handles."""
def bindXformGadgets(template: hou.ViewerStateTemplate) -> None:
    """ Bind the GadgetDrawables for the xform handles. """
def bindXformStateParms(template: hou.ViewerStateTemplate, toolbox: bool = False) -> None:
    """ Bind the state parms used for the xform handles. """
def registerXformHandle(template: hou.ViewerStateTemplate, main_menu: hou.ViewerStateMenu | None = None, toolbox: bool = False, main_hotkey_definitions: hou.PluginHotkeyDefinitions | None = None) -> None:
    """ Register the xform handles to the given template."""

HANDLE_XYZ_PARMS: list[str]
HANDLE_123_PARMS: list[str]
HANDLE_INT_PARMS: list[str]

def bindHandleParms(template: hou.ViewerHandleTemplate) -> None:
    """ Bind the python handle parms. """
def remapToHandleParms(parms: Mapping[str, hou.Vector3], settings: _HandleSettings) -> dict[str, float]:
    """
    Remap the gadget's parms and settings into the parms for the
    python handle.
    """
def remapFromHandleParms(handle_parms: Mapping[str, ViewerParmProperties]) -> tuple[dict[str, hou.Vector3], dict[str, int]]:
    """
    Remap python handle parms into the parms and settings for the
    gadget.
    """
def registerViewerHandle(template: hou.ViewerHandleTemplate) -> None:
    """ Registry the python handle. """
def isAxisComponent(component: str) -> bool:
    """ Check whether the given component is an axis component,
        which is one of an axis line, arrow, or scale box.
    """
def isRotateRingComponent(component: str) -> bool:
    """ Check whether the given component is a rotate ring
        component, which is one of a rotate ring, the view ring,
        a hidden rotate ring, or a pivot rotate ring.
    """
def isRotateSphereComponent(component: str) -> bool:
    """ Check whether the given component is a rotate sphere component,
        which is one of a rotate sphere, a pivot rotate sphere,
        or the hidden rotate sphere.
    """
def isCenterComponent(component: str) -> bool:
    """ Check if the given component is a center component,
        which is one of a center box, the pivot center box,
        of the rotate center sphere.
    """
def isPlaneComponent(component: str) -> bool:
    """ Check if the given component is a plane component,
        which is defined as one of the drag or scale planes.
    """
def isRotateComponent(component: str) -> bool:
    """ Whether it is a rotate ring, dot or tumble sphere. """
def isTranslateComponent(component: str) -> bool:
    """ Whether it is an axis, center, or plane. """
def getAlignmentParm(component: str, xform_mode: str, separate_aligns: int) -> _AlignSettingKey:
    """
    Get the appropriate alignment parameter given the component name,
    the transform mode and whether we have separate alignments.
    """

class SingleGadgetSettingsConfig(config.UserDataConfig):
    gadget_index: int
    def __init__(self, node: hou.SopNode, gadget_index: int = 0, prefix: str | None = None) -> None: ...
    def loadHandleSettings(self, handle_obj: ApexXformHandle, kwargs: ViewerStateKwargs) -> None: ...
    def storeHandleSettings(self, handle_obj: ApexXformHandle, kwargs: ViewerStateKwargs) -> None: ...

class GadgetConfig(config.UserDataConfig):
    """ Encapsulate storing and loading of handles from configs. """
    def storeHandles(self, handle_obj: ApexXformHandle, kwargs: ViewerStateKwargs) -> None:
        """ Store the handle instances given a kwargs dict, and the
            handles object.

            The kwargs dict is used to store the state parms.
        """
    def loadHandles(self, handle_obj: ApexXformHandle, kwargs: ViewerStateKwargs) -> None:
        """ Load the handles instances and state parms from the
            config.

            The loaded handle instances are stored in handle_obj,
            and are appended to the existing instances.

            The loaded state parms are set in the kwargs dictionary.
        """

class ApexXformHandle:
    """Class to allow creation and management of multiple transform gadgets."""
    disable_parm_undo: bool
    logger: logging.Logger
    class ParmUndo:
        """ Undo object for xform handle parm updates. """
        def __init__(self, parent: ApexXformHandle, index: int, pre_parms: Mapping[str, hou.Vector3], new_parms: Mapping[str, hou.Vector3]) -> None: ...
        def undo(self) -> None: ...
        def redo(self) -> None: ...
    class SettingUndo:
        """ Undo object for Xform handle setting updates. """
        def __init__(self, parent: ApexXformHandle, index: int, pre_settings: _HandleSettingsUpdate, post_settings: _HandleSettingsUpdate) -> None: ...
        def undo(self) -> None: ...
        def redo(self) -> None: ...
    class ParmUpdateBlock:
        """ Allows collecting parm updates into a
            'with ParmUpdateBlock(...):' block.
        """
        def __init__(self, parent: ApexXformHandle, index: int, name: str, kwargs: _EventKwargs, in_undo: bool = False) -> None: ...
        def __enter__(self) -> None: ...
        def __exit__(self, *args: object) -> None: ...
    class SettingUpdateBlock:
        """ Allows collecting settings updates into a
            'with SettingUpdateBlock(...):' block.
        """
        def __init__(self, parent: ApexXformHandle, index: int, kwargs: _EventKwargs, in_undo: bool = False) -> None: ...
        def __enter__(self) -> None: ...
        def __exit__(self, *args: object) -> None: ...
    def __init__(self, scene_viewer: hou.SceneViewer, state: object, hidden_menu_items: Iterable[str] | None = None, custom_menu_items: Iterable[_CustomMenuItem] | None = None, hotkey_context: str | None = None, handle_gadgets: Mapping[str, hou.GadgetDrawable] | None = None) -> None: ...
    def setCustomAxesSnapping(self, val: bool) -> None:
        """ Set whether the handle uses the custom axes snapping behaviour. """
    def setToggleVisShowAll(self, val: bool) -> None:
        """
        Set whether the hotkey to toggle the visibility of handles to affect the
        visibility of individual handle instances.

        When this is enabled, if any handles are visible it will hide the full
        drawable, but keep the instances internally visible.

        If none are visible, then it will show the drawables, and if NO instance
        is visible, it will then show them all.
        """
    def setHandlesOwnPrompt(self, val: bool) -> None:
        """
        Set whether the handle draws its own prompt.
        This is for more complicated set ups with conflicting
        prompts from the handle and other tools that we need to
        sort out at a higher level.
        """
    def show(self, value: bool) -> None:
        """ Show or hide all the handles."""
    def onActivate(self, kwargs: ViewerStateKwargs) -> None:
        """ Call from onEnter or onGenerate to initialize handles. """
    def updateFromPrefs(self) -> None:
        """ Refresh all settings from preferences. """
    def prefChanged(self, pref_name: str) -> None:
        """ Respond to a single preference change. """
    def onSceneViewerEvent(self, **kwargs: Unpack[SceneViewerEventKwargs]) -> None:
        """ Respond to a scene viewer event (like a preference change.) """
    def onDeactivate(self, kwargs: ViewerStateKwargs) -> None:
        """ Call from onExit. """
    def onInterrupt(self, kwargs: ViewerStateKwargs) -> None:
        """ Call from onInterrupt. """
    def onResume(self, kwargs: ViewerStateKwargs) -> None:
        """ Call from onResume. """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Call from onMouseEvent, returns True if the handles
            consume the event, or False otherwise.
        """
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> None:
        """ Call from onMenuPreOpen. Shows and hides menu items
            based on what is hovered over.
        """
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> None:
        """ Call from onMenuAction. Triggers the menu actions. """
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Called on onKeyTransitEvent from the state. Return True
            to consume.
        """
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Called from onKeyEvent in the state. Return True to
            consume.
        """
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> None:
        """ Called from onVolatileClientEvent in the state.
        """
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> None:
        """ Called from onCommand by the state. """
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None:
        """ Call from onParmChangeEvent. Called when state parms change.
        """
    def onDrawInterruptSetup(self, kwargs: ViewerStateKwargs) -> None:
        """ Call from onDrawInterrupt. Must be called before onDraw. """
    def onDrawSetup(self, kwargs: ViewerStateKwargs) -> None:
        """ Call from onDraw or onDrawSetup. Must be called before onDraw. """
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None:
        """ Call from onDraw. Note that onDrawSetup must be called first. """
    def numInstances(self) -> int:
        """ Return the number of active handles."""
    def getHandleIndex(self, handle_name: str) -> int:
        """ Get the index of a handle from its name."""
    def getHandleName(self, index: int) -> str:
        """ Get a handle name from its index."""
    def getDragFlags(self) -> xgu.DragGuide.DragFlags:
        """
        Get a collection of flags that can be used to alter the
        visibility of parts of the drag guide.
        """
    def getHandleLabel(self, index: int, default_to_name: bool = True) -> str:
        """ Get the handle label given the index. """
    def getHandleLabelFromName(self, name: str, default_to_name: bool = True) -> str | None:
        """ Get the handle label given the handle name. """
    def setHandleLabel(self, index: int, label: str) -> None:
        """ Set the handle label by index. """
    def setHandleLabelByName(self, name: str, label: str) -> None:
        """ Set the handle label by name. """
    def addInstance(self, name: str | None = None, label: str | None = None, default_parms: Mapping[str, hou.Vector3] | None = None, default_settings: _HandleSettingsUpdate | None = None, default_metadata: _HandleMetadata | None = None, default_parm_values: Mapping[str, hou.Vector3] | None = None) -> int:
        """
        Add a new instance with the given name.

        Returns the index of the created handle instance. This should be
        used where ever you need to provide an index or transform id.
        """
    def removeInstance(self, transform_id: int = -1, name: str | None = None) -> None:
        """ Remove an instance given either its index or name.
            If both are given, the index is given priority.
        """
    def isVisible(self) -> bool:
        """ Whether the handles are visible."""
    def updateFromXformMatrixPre(self, index: int, xform: hou.Matrix4) -> None:
        """ Update the pre-transform parameters for a handle from a matrix. """
    def updateFromXformMatrix(self, index: int, xform: hou.Matrix4, base_rotations: hou.Vector3 | None = None) -> None:
        """ Update the transform parameters for a handle from a matrix."""
    def updatePreXform(self, index: int, pre_xform: hou.Matrix4) -> None:
        """ Update the pre-transform parms from the matrix representation. """
    def snapXformToLimits(self, index: int) -> None:
        """
        Reset with the same xform to force it to apply the limits to it.
        This is helpful if the limits change and we just want to snap the
        handle to them.
        """
    def updateLimitsGuide(self, index: int) -> None:
        """
        Refresh the transform limits guide with updated parameters
        and visibility.
        """
    def updateFromXformMatrixByName(self, name: str, xform: hou.Matrix4) -> None:
        """ Update the transform parameters for the handle with given
            name from the given matrix.
        """
    def updatePivotXform(self, index: int, pivot_xform: hou.Matrix4, maintain_xform: bool = True) -> None:
        """ Update the pivot xform matrix for a specific instance. """
    def updatePivotXformByName(self, name: str, pivot_xform: hou.Matrix4, maintain_xform: bool = True) -> None:
        """ Update the pivot xform matrix for a specific instance by name.
            If maintain_xform is True, then the full xform specified by
            this instance will be kept the same after the pivot has
            been changed.
        """
    def updateFullXform(self, index: int, xform: hou.Matrix4, pivot_xform: hou.Matrix4, pre_xform: hou.Matrix4 | None = None, base_rotations: hou.Vector3 | None = None, set_centroid: bool = True) -> None:
        """
        Update the xform and the pivot xform at the same time, and if provided
        also update the internal base rotations used for transform limits.
        If set_centroid is true, store the pivot_xform as the centroid xform
        in the metadata.
        """
    def updateFullXformByName(self, name: str, xform: hou.Matrix4, pivot_xform: hou.Matrix4, pre_xform: hou.Matrix4 | None = None, base_rotations: hou.Vector3 | None = None, set_centroid: bool = True) -> None:
        """
        Update the xform and the pivot xform at the same time, and if provided
        also update the internal base rotations used for transform limits.
        If set_centroid is true, store the pivot_xform as the centroid xform
        in the metadata.
        """
    def setCentroidXform(self, index: int, centroid_xform: hou.Matrix4) -> None:
        """ Set the transform stored for the centroid. """
    def getCentroidXform(self, index: int) -> hou.Matrix4:
        """ Get the transform stored for the centroid. """
    def setRotationLimits(self, index: int, lower_limit: hou.Vector3 | None = None, upper_limit: hou.Vector3 | None = None) -> None:
        """
        Set the rotation transform limits. If set to None, they will
        not be used.
        """
    def getRotationLimits(self, index: int) -> tuple[hou.Vector3 | None, hou.Vector3 | None]:
        """
        Get the rotation transform limits. If None, they are not used.
        """
    def setTranslateLimits(self, index: int, lower_limit: hou.Vector3 | None = None, upper_limit: hou.Vector3 | None = None) -> None:
        """
        Set the translation transform limits. If set to None, they will not
        be used.
        """
    def getTranslateLimits(self, index: int) -> tuple[hou.Vector3 | None, hou.Vector3 | None]:
        """
        Get the translation transform limits. If None, they are not used.
        """
    def setScaleLimits(self, index: int, lower_limit: hou.Vector3 | None = None, upper_limit: hou.Vector3 | None = None) -> None:
        """
        Set the scale transform limits. If set to None, they will not
        be used.
        """
    def getScaleLimits(self, index: int) -> tuple[hou.Vector3 | None, hou.Vector3 | None]:
        """
        Get the scale transform limits. If None, they are not used.

        """
    def clearTransformLimits(self, index: int) -> None:
        """ Reset all transform limits to None. """
    def hideComponentsFromLimits(self, index: int) -> None:
        """ Update hidden components using the transform limits. """
    def getLimitBaseRotation(self, index: int) -> hou.Vector3 | None:
        """
        Get the base rotations used for the rotation limits, but
        clamped to within the rotation limits.
        """
    def setLimitBaseRotations(self, index: int, base_rot: hou.Vector3, apply_limits: bool = True) -> None:
        """
        Set the base rotations used for transform limits.
        If apply_limits is true, these base rotations are first clamped
        to the stored rotation limits if present.
        """
    def applyTransformLimits(self, index: int, xform: hou.Matrix4) -> hou.Matrix4:
        """
        Pull apart xform into local transform components, then apply
        transform limits to the components, and return the resulting
        transform.
        """
    def snapPivotCentroid(self, index: int) -> None:
        """ Moves the placement of the handle to the centroid. """
    def snapCentroidPivot(self, index: int) -> None:
        """ Moves the control (the centroid) to the placement position of the
            handle.
        """
    def resetPivot(self, transform_id: int, reset_pivot_rot: bool = False, maintain_xform: bool = True) -> None:
        """ Reset the pivot parameters for the given instance.
            The resultant transform will not change, but individual
            values t/r/s will change to account for the different
            pivot.
        """
    def updateParms(self, transform_id: int, parms: Mapping[str, hou.Vector3]) -> None:
        """ Update the parms for a handle."""
    def updateParm(self, transform_id: int, key: str, value: hou.Vector3, add: bool = False, snap_zero: bool = False) -> None:
        """ Update an individual parm for a handle."""
    def resetSetting(self, transform_id: int, key: str) -> None:
        """ Reset the setting with name key to the default value. """
    def resetSettings(self, transform_id: int, keys: Sequence[str] | None = None) -> None:
        """ Reset the settings with names in keys to defaults. """
    def resetParm(self, transform_id: int, key: str) -> None:
        """ Reset the parm with name key to the default. """
    def resetParms(self, transform_id: int, keys: Sequence[str] | None = None) -> None:
        """ Reset the parms with keys in keys to default. """
    def setHandleVisible(self, transform_id: int, show_val: bool, send_to_callback: bool = True) -> None:
        """ Update the visibility for a handle. """
    def sendHandleVisibilityEvent(self, index: int | None = None) -> None:
        """
        If you have changed the visibility on handles with
        send_to_callback=False and still wish to get an event on the
        callback for the visiblity change, call this once after
        batch changing the visibilities.
        """
    def getHandleVisible(self, transform_id: int) -> int:
        """ Get whether this instance is visible. """
    def anyHandleVisible(self) -> bool:
        """
        Whether any handle instance is visible. Does not look at whether the
        drawables are visible. Use .isVisible() for that.
        """
    def setAllVisible(self, val: bool) -> None:
        """
        Set the visibility on all the handle instances.
        Note that this does not affect whether the drawable is visible.
        """
    @typing.overload
    def updateSetting(self, transform_id: int, key: _IntSettingKey, value: int) -> None: ...
    @typing.overload
    def updateSetting(self, transform_id: int, key: Literal['xform_mode'], value: _XformMode) -> None: ...
    @typing.overload
    def updateSetting(self, transform_id: int, key: _AlignSettingKey, value: _AlignMode) -> None: ...
    @typing.overload
    def updateSetting(self, transform_id: int, key: _StrSettingKey, value: str) -> None: ...
    @typing.overload
    def updateSetting(self, transform_id: int, key: Literal['enabled_components'], value: dict[str, int]) -> None: ...
    @typing.overload
    def updateSetting(self, transform_id: int, key: Literal['enabled_modes'], value: dict[_XformMode, bool]) -> None: ...
    @typing.overload
    def updateSetting(self, transform_id: int, key: Literal['reflection_hint'], value: hou.Vector3) -> None: ...
    @typing.overload
    def updateSetting(self, transform_id: int, key: Literal['has_reflection_hint'], value: bool) -> None: ...
    @typing.overload
    def updateSetting(self, transform_id: int, key: str, value: _HandleSettingValue) -> None: ...
    def updateSettings(self, transform_id: int, settings: _HandleSettingsUpdate) -> None:
        """ Update multiple settings on the instance with index
            'transform_id' using the dictionary 'settings'.
        """
    def updateMetadata(self, transform_id: int, update_dict: _HandleMetadata) -> None:
        """ Update the metadata for the instance with index
            'transform_id' using the dictionary 'update_dict'.
        """
    @typing.overload
    def updateMetadataEntry(self, transform_id: int, key: Literal['centroid_xform'], value: hou.Matrix4) -> None: ...
    @typing.overload
    def updateMetadataEntry(self, transform_id: int, key: _MetadataLimitKey, value: hou.Vector3 | None) -> None: ...
    @typing.overload
    def updateMetadataEntry(self, transform_id: int, key: str, value: object) -> None: ...
    def updateEnabledComponent(self, transform_id: int, key: str, value: bool) -> None:
        """ Update whether the component 'key' is enabled or disabled
            ('value'), on the instance 'transform_id'.
        """
    def getEnabledComponents(self, transform_id: int) -> dict[str, int]:
        """ Get the enabled components dictionary for 'transform_id'. """
    def setModeEnabled(self, transform_id: int, mode_key: str, enabled_val: bool = True) -> None:
        """ Update whether the mode 'mode_key' is enabled or disabled. """
    def getEnabledModes(self, transform_id: int) -> list[_XformMode]:
        """
        Get the enabled modes. This returns them in the order they
        occur in the radio menu.
        """
    def getModeEnabled(self, transform_id: int, mode_key: str) -> bool:
        """ Get whether the given mode is enabled. """
    def setReflectionHint(self, transform_id: int, reflection_hint: hou.Vector3) -> None:
        """
        Set the reflection hint, which sets whether each axis should have
        its direction reversed.
        """
    def clearReflectionHint(self, transform_id: int) -> None:
        """ Clear out the reflection hint so that it is no longer used for this instance. """
    def updateReflectionHint(self, transform_id: int) -> hou.Vector3:
        """ Compute the new reflection hint from the delta scale. """
    def getLocalDeltaScaleHint(self, transform_id: int) -> hou.Vector3: ...
    def updateXformModeIfDisabled(self, transform_id: int) -> None:
        """ Change to the first enabled mode if the current mode is not enabled. """
    def setEnabledModes(self, transform_id: int, mode_list: Collection[str]) -> None:
        """ Set the enabled modes from the given list. """
    def getXformMode(self, transform_id: int) -> _XformMode:
        """ Get the transform mode (x,t,r,s,c) for a given instance. """
    def setXformMode(self, transform_id: int, the_mode: _XformMode, check_enabled: bool = True) -> bool:
        """
        Set the transform mode for a given instance.

        Return True if successful or False if the mode is not enabled.
        """
    def getParms(self, transform_id: int) -> dict[str, hou.Vector3]:
        """ Get the parameter dictionary for a given instance. """
    def getParm(self, transform_id: int, parm: str) -> hou.Vector3 | None:
        """ Get the parameter 'parm' for the instance 'transform_id'."""
    def getSettings(self, transform_id: int) -> _HandleSettings:
        """ Get the full settings dictionary for the instance
            'transform_id'.
        """
    @typing.overload
    def getSetting(self, transform_id: int, setting: _IntSettingKey) -> int: ...
    @typing.overload
    def getSetting(self, transform_id: int, setting: Literal['xform_mode']) -> _XformMode: ...
    @typing.overload
    def getSetting(self, transform_id: int, setting: _AlignSettingKey) -> _AlignMode: ...
    @typing.overload
    def getSetting(self, transform_id: int, setting: _StrSettingKey) -> str: ...
    @typing.overload
    def getSetting(self, transform_id: int, setting: Literal['enabled_components']) -> dict[str, int]: ...
    @typing.overload
    def getSetting(self, transform_id: int, setting: Literal['enabled_modes']) -> dict[_XformMode, bool]: ...
    @typing.overload
    def getSetting(self, transform_id: int, setting: Literal['reflection_hint']) -> hou.Vector3: ...
    @typing.overload
    def getSetting(self, transform_id: int, setting: Literal['has_reflection_hint']) -> bool: ...
    @typing.overload
    def getSetting(self, transform_id: int, setting: str) -> _HandleSettingValue | None: ...
    def getMetadata(self, transform_id: int) -> _HandleMetadata:
        """ Get the full metadata dictionary for the instance
            'transform_id'.
        """
    @typing.overload
    def getMetadataEntry(self, transform_id: int, key: Literal['centroid_xform']) -> hou.Matrix4 | None: ...
    @typing.overload
    def getMetadataEntry(self, transform_id: int, key: _MetadataLimitKey) -> hou.Vector3 | None: ...
    @typing.overload
    def getMetadataEntry(self, transform_id: int, key: str) -> object: ...
    def getAllParms(self) -> list[dict[str, hou.Vector3]]:
        """ Get the full list of parm dicts."""
    def getAllSettings(self) -> list[_HandleSettings]:
        """ Get the full list of settings dicts. """
    def getAllMetadata(self) -> list[_HandleMetadata]:
        """ Get the full list of metadata dicts. """
    def getRotOrder(self, index: int) -> ksu._RotateOrder:
        """ Get the rotate order for the instance 'index'. """
    def getXformOrder(self, index: int) -> ksu._TransformOrder:
        """ Get the transform order for the instance 'index'. """
    def getPreRotOrder(self, index: int) -> ksu._RotateOrder:
        """ Get the rotate order for the instance 'index'. """
    def getPreXformOrder(self, index: int) -> ksu._TransformOrder:
        """ Get the transform order for the instance 'index'. """
    def getPivotMode(self, index: int) -> int:
        """ Get whether the instance 'index' is in pivot mode. """
    def updatePivotMode(self, index: int, val: bool) -> None:
        """ Update pivot mode. """
    def getTranslateAlignment(self, index: int) -> _AlignMode:
        """
        Get the alignment used for translating. If separate alignment
        if disabled, then this will grab the single alignment.
        """
    def getRotateAlignment(self, index: int) -> _AlignMode:
        """
        Get the alignment used for rotating. If separate alignment
        if disabled, then this will grab the single alignment.
        """
    def getScaleAlignment(self, index: int) -> _AlignMode:
        """
        Get the alignment used for scaling. If separate alignment
        if disabled, then this will grab the single alignment.
        """
    def updateTranslateAlignment(self, index: int, val: _AlignMode) -> None:
        """
        Update the alignment used for translating. If separate alignment
        if disabled, then this will update the single alignment.
        """
    def updateRotateAlignment(self, index: int, val: _AlignMode) -> None:
        """
        Update the alignment used for rotating. If separate alignment
        if disabled, then this will update the single alignment.
        """
    def updateScaleAlignment(self, index: int, val: _AlignMode) -> None:
        """
        Update the alignment used for scaling. If separate alignment
        if disabled, then this will update the single alignment.
        """
    def getGimbalMode(self, index: int) -> int:
        """ Get whether the handle is gimbal mode. """
    def updateGimbalMode(self, index: int, v: bool) -> None:
        """ Update whether the handle is in gimbal mode. """
    def setHandleUpdateCallback(self, cb: _HandleUpdateCallback | None) -> None:
        """ Set the callback that is called whenever a handle updates. """
    def setHandleStartUpdateCallback(self, cb: _HandleStartUpdateCallback | None) -> None:
        """ Set the callback that is called whenever a handle update
            event start.
        """
    def setHandleEndUpdateCallback(self, cb: _HandleUpdateCallback | None) -> None:
        """ Set the callback that is called whenever a handle update
            event is finished.
        """
    def setHandleSettingsUpdateCallback(self, cb: _HandleSettingsUpdateCallback | None) -> None:
        """ Set the callback that is called whenever a handle's settings
            are updated.
        """
    def setHandleSettingsStartUpdateCallback(self, cb: _HandleSettingsEventCallback | None) -> None:
        """ Set the callback that is called when beginning an update to
            a handle's settings.
        """
    def setHandleSettingsEndUpdateCallback(self, cb: _HandleSettingsEventCallback | None) -> None:
        """ Set the callback that is called when ending an update to a
            handle's settings.
        """
    def setHandleHoverCallback(self, cb: _HandleHoverCallback | None) -> None:
        """ Set the callback that is called whenever a mouse event is
            over a handle.
        """
    def setHandleCustomActionCallback(self, cb: _HandleCustomActionCallback | None) -> None:
        """ Set the callback that is called whenever a custom context
            menu action on the handle is triggered.
        """
    def setExternalPickCallback(self, cb: _ExternalPickCallback | None) -> None:
        """ Set the callback that is called whenever the handle is waiting
            for a pick of a component.

            Can be used to allow orientation picking and moving handle to
            picked position to be aware of state objects defined outside
            of the handle, such as controls.
        """
    def setHandleVisibilityCallback(self, cb: _HandleVisCallback | None) -> None:
        """
        Set the callback that is called when a handle instance visibility changes
        or the full handle drawables' visibility changes.

        :cb: The callback.
        """
    def isCtrlKey(self) -> bool:
        """ Whether the ctrl key was pressed on the last interaction start. """
    def isShiftKey(self) -> bool:
        """ Whether the shift key was pressed on the last interaction start. """
    def getCenterPos(self, transform_id: int) -> hou.Vector3:
        """ Get the center postion for a handle."""
    def pickDrawables(self, ui_event: hou.ViewerEvent | None = None, mx: int = 0, my: int = 0) -> DragInfoTuple:
        """ Pick drawables on the handle in order of priority. """
    def getIndirectDragInfo(self) -> DragInfoTuple:
        """
        When performing an indirect drag, get the component
        and index of the handle, if we are allowed to do the
        indirect drag.
        """
    def getSelectedInstance(self) -> int | None:
        """
        Get the index of the last interacted instance,
        or None if it doesn't exist.
        """
    def getSelectedName(self) -> str | None:
        """ Get the name of the last interacted component, or None. """
    def getSelectedCompInfo(self) -> tuple[str | None, int | None]: ...
    def getMode(self) -> HandleMode:
        """ Get the handle mode. """
    def setMode(self, mode: HandleMode) -> None:
        """ Set the handle mode to one of the values in the
            HandleMode enum class.
        """
    def clearMode(self) -> None:
        """ Reset the handle mode to the default. """
    def isTranslateComponent(self, transform_id: int, comp: str) -> bool:
        """
        Whether the component on the given transform handle instance is
        a translate component in the current xform mode.
        """
    def isRotateComponent(self, transform_id: int, comp: str) -> bool:
        """
        Whether the component on the given transform handle instance is
        a rotate component in the current xform mode.
        """
    def isScaleComponent(self, transform_id: int, comp: str) -> bool:
        """
        Whether the component on the given transform handle instance is
        a scale component in the current xform mode.
        """
    def isComponentVisible(self, transform_id: int, comp: str) -> bool:
        """ Whether the given component is currently visible on the handle. """
    def getPostTransformMatrix(self, transform_id: int, pivots: bool = True) -> hou.Matrix4:
        """
        Get the transform matrix taking into account the TRS parms and the pivot.
        This DOES NOT take the pre-transform into account yet.
        """
    def getTransformMatrix(self, transform_id: int) -> hou.Matrix4:
        """
        Get the transform matrix for a given instance, including the pre-transform,
        the pivot and the post-transform.
        """
    def getTransformMatrixByName(self, name: str) -> hou.Matrix4:
        """ Get the transform matrix for a given instance by name. """
    def getPivotTransformMatrix(self, transform_id: int) -> hou.Matrix4:
        """ Get a matrix4 representing the pivot transform for a handle. """
    def getPivotRotateMatrix(self, transform_id: int) -> hou.Matrix3:
        """ Get a matrix3 representing the pivot rotation of the handle. """
    def getPreTransformMatrix(self, transform_id: int) -> hou.Matrix4:
        """ Get a matrix4 representing the pre-transform of the handle. """
    def getPlacementTransformMatrix(self, transform_id: int, alignment_parm: str | None = None) -> hou.Matrix4:
        """ Get a matrix4 representing the full transform for a handle. """
    def getPlacementRotateMatrix(self, transform_id: int, alignment_parm: str | None = None) -> hou.Matrix3:
        """ Get a matrix3 representing the full rotation of the handle. """
    def getParentSpaceTransformMatrix(self, transform_id: int) -> hou.Matrix4:
        """ Get a matrix4 representing transform of parent space. """
    def getParentSpaceRotateMatrix(self, transform_id: int) -> hou.Matrix3:
        """ Get a matrix3 representing rotation of parent space. """
    def saveForUndo(self, index: int) -> None:
        """ Save the current parms for undo. """
    def commitUndo(self) -> None:
        """ Send the stored undo parms as a new undo. """
    def clearSelectedComps(self) -> None:
        """ Clear the selected components or revert to defaults. """
    def setSelectedComp(self, name: str, index: int) -> None:
        """ Set a selected component. """
    def refreshSelectedComps(self) -> None:
        """
        Check if the currently selected component is still visible and if not
        reset it to nothing.
        """
    def allowSelectComponents(self) -> bool:
        """ Whether we allow selecting components. """
    def isDragging(self) -> bool:
        """ Whether the handle is being dragged. """
    def setHandlesOwnCursorLabel(self, val: bool) -> None:
        """ Set whether we should draw our own cursor label. """
    def getHandlesOwnCursorLabel(self) -> bool:
        """ Whether we draw our own cursor label. """
    def cursorLabel(self) -> str | None:
        """ Get the cursor label text. """
    def getSeparateAlignment(self, index: int) -> int:
        """ Get whether there are separate alignments. """
    def updateSeparateAlignment(self, index: int, val: bool) -> None:
        """ Update whether there are separate alignments. """
    def updateSeparateAlignments(self, val: bool) -> None: ...
    def getHandleScale(self, index: int = -1, pos: hou.Vector3 | None = None) -> float:
        """ Get the handle scale amount (radius) for the instance
            'index', at the position 'pos'.

            If index == -1, it uses the 'pos' as the reference position.

            If index >= 0, it uses the center position of this instance
            as the reference position.
        """
    def displayPrompt(self) -> bool:
        """ Display stored prompt message. """
    def drawSetup(self, kwargs: ViewerStateKwargs, interrupt: bool = False, world_m: hou.Matrix4 | None = None) -> None:
        """ Setup the handles to draw."""
    def drawOpaqueComponents(self, kwargs: ViewerStateDrawKwargs) -> None:
        """ Draw the handles."""
    def drawTransparentComponents(self, kwargs: ViewerStateDrawKwargs) -> None:
        """ Draw the handles."""
