import weakref
from collections.abc import Callable, Iterable, Mapping
from enum import StrEnum
from typing import ClassVar, Literal, Protocol, Required, TypeAlias, TypedDict, Unpack, type_check_only

import _apex
import apex
import apex.bake as apexbake
import apex.stateutils_2 as asu
import hou
from apex.autorigtool import _ToolActivateKwargs
from apex.bake import _CtrlParms
from apex.channelutils import ChannelData, SceneChannelManager, _ScopeChannelsKwargs
from apex.effecttool import (
    EffectParmHudWidget,
    EffectParmSelectable,
    EffectSubtool,
    EffectTool,
    _AnimatedParmActionKwargs,
    _AnimateState as _EffectState,
    _BakeKwargs,
    _CollectionNamesKwargs,
    _ParmChangeKwargs,
    _ParmValue,
    _TabInfo,
    _WidgetValue,
)
from apex.ui.sceneparmwidgetset import SceneParmWidgetSet
from apex.ui.statecommandutils import _ToolboxParmUpdate
from houtypes import (
    ViewerParmProperties,
    ViewerStateEventKwargs,
    ViewerStateMenuActionKwargs,
    ViewerStateMenuPreOpenKwargs,
    ViewerStateParmChangeKwargs,
)
from statehud.parmutils import _HUDParmValue
from statehud.parmwidgetset import ParmWidgetSet, _MenuItem
from statehud.window import WidgetBundleWindow

class _AnimateState(_EffectState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only the members of the states it extends."""

# The keywords ParmWidgetSet.__init__ takes, which LinkedParmWidgetSet passes on.
class _ParmWidgetSetKwargs(TypedDict, total=False):
    hud_window: Required[WidgetBundleWindow]
    label_width: Required[int]
    tab_widget: Required[str]
    tab_name: Required[str | None]
    prefix: str
    folder_name: str | None
    folder_collapsible: bool
    folder_collapsed: bool
    folder_label: str | None
    callback: Callable[[str], object] | None
    expand_vectors: bool
    slider_start_callback: Callable[[str], object] | None
    slider_end_callback: Callable[[str], object] | None
    action_button_callback: Callable[[str], object] | None
    hotkey_callback: Callable[[str, str], object] | None
    disable_parm_conditionals: bool

class SecondaryMotionToolbox(StrEnum):
    # enable is a bool, or an int used as one.
    @classmethod
    def getParmsEnabledDict(cls, enable: bool | int) -> dict[str, _ToolboxParmUpdate]: ...
    @classmethod
    def getParmsValueDict(
        cls, toolbox_name: str, value: bool | int | float | str | list[int] | list[float]
    ) -> dict[str, _ToolboxParmUpdate]: ...

class LinkedParmWidgetSet(SceneParmWidgetSet):
    widget_set_refs: list[weakref.ref[ParmWidgetSet]]
    # SceneParmWidgetSet's scene, then ParmWidgetSet's arguments.
    def __init__(self, *args: *tuple[apex.Scene], **kwargs: Unpack[_ParmWidgetSetKwargs]) -> None: ...
    def addRef(self, widget_sets: Iterable[ParmWidgetSet]) -> None: ...

class SecondaryMotionSettingsWidget(EffectParmHudWidget[LinkedParmWidgetSet]):
    parm_widget_set: LinkedParmWidgetSet
    effect_widget_set: LinkedParmWidgetSet | None
    transform_widget_set: LinkedParmWidgetSet | None
    def __init__(
        self,
        tool: "SecondaryMotionTool",
        hud_window: WidgetBundleWindow | None = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
    ) -> None: ...
    @type_check_only
    @property
    def tool(self) -> "SecondaryMotionTool | None": ...
    @type_check_only
    @property
    def focused_subtool(self) -> "SecondaryMotionSubtool | None": ...
    def createParmWidgetSet(self, tool: EffectTool) -> LinkedParmWidgetSet: ...
    def getParmKeys(self) -> list[str]: ...
    # val is a bool for the effect enable, debug and select_desc parameters.
    def updateParmValue(self, parm_name: str, val: _WidgetValue, refresh_hide_disable: bool = ...) -> bool: ...

TRANSFORM_COMPONENTS: list[str]
FILTER_PARM_DEFAULT: int
MULT_PARM_DEFAULT: float
# The filter parameters' (bit masks of the axes) and the multipliers' defaults.
CONFIG_PARM_DEFAULTS: dict[str, int | float]
XYZ_MENU_ITEMS: list[_MenuItem]

class SecondaryMotionParmWidget(EffectParmHudWidget):
    filter_widget: ParmWidgetSet | None
    parm_widget_set: SceneParmWidgetSet
    def __init__(
        self,
        tool: "SecondaryMotionTool",
        hud_window: WidgetBundleWindow | None = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
    ) -> None: ...
    @type_check_only
    @property
    def tool(self) -> "SecondaryMotionTool | None": ...
    @type_check_only
    @property
    def focused_subtool(self) -> "SecondaryMotionSubtool | None": ...
    # graph is ignored.
    def initBindings(self, graph: apex.Graph | None = ...) -> None: ...
    def getParmKeys(self) -> list[str]: ...
    def getParmDict(self) -> dict[str, _HUDParmValue]: ...
    def getParmValue(self, parm_name: str) -> _HUDParmValue: ...
    def updateParmValue(self, parm_name: str, val: _WidgetValue, refresh_hide_disable: bool = ...) -> bool: ...

class SecondaryMotionSelectable(EffectParmSelectable[SecondaryMotionParmWidget, SecondaryMotionSettingsWidget]):
    hud_widget: SecondaryMotionParmWidget | None
    settings_widget: SecondaryMotionSettingsWidget | None
    add_driven_hk: str
    remove_driven_hk: str
    select_desc: bool
    double_click_started: bool
    last_select_time: float
    last_control_selection: tuple[str, ...] | None
    selected: set[str]
    @type_check_only
    @property
    def subtool(self) -> "SecondaryMotionSubtool | None": ...
    @type_check_only
    @property
    def state(self) -> _AnimateState | None: ...
    @property
    def prompt_message(self) -> str | None: ...
    def onSelectionChanged(self, control_selection: tuple[str, ...]) -> None: ...
    def onActivate(self, parms: Iterable[str]) -> None: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...

class SecondaryMotionTool(EffectTool["SecondaryMotionSubtool", SecondaryMotionParmWidget, SecondaryMotionSettingsWidget]):
    subtools: list["SecondaryMotionSubtool"]
    focused_subtool: "SecondaryMotionSubtool | None"
    add_driven_hk: str
    remove_driven_hk: str
    confirm_selection_hk: str
    default_hud_rows: list[hou._HudRow]
    parm_widget: SecondaryMotionParmWidget | None
    sett_widget: SecondaryMotionSettingsWidget | None
    def __init__(self, state: _AnimateState, solver_graph: apex.Graph | None = ...) -> None: ...
    @type_check_only
    @property
    def state(self) -> _AnimateState | None: ...
    def setupWidgets(self, channel_hud_tab_info: _TabInfo, settings_hud_tab_info: _TabInfo) -> None: ...
    # lag and overshoot are floats, made Vector2s here.
    def onParmValueChange(
        self,
        parm_name: str,
        val: _ParmValue,
        active: bool = ...,
        start_slider: bool = ...,
        end_slider: bool = ...,
        focused_subtool_only: bool = ...,
    ) -> None: ...
    def createSubtool(
        self, char_path: str, rest_skel: hou.Geometry, node_name: str, skel_name: str, rest_ctrl_skel: hou.Geometry | None
    ) -> "SecondaryMotionSubtool": ...

# Each control's filter config: a Dict of its filter_t, filter_r and filter_s bit masks.
_FilterConfig: TypeAlias = apex.Dict | dict[str, apex.Dict]

class ControlConfigData(ChannelData):
    filter_config: _FilterConfig
    def __init__(
        self, geo: hou.Geometry, filter_config: _FilterConfig, pending_channels: dict[str, float] | None = ...
    ) -> None: ...

class SecondaryMotionControlConfig(SceneChannelManager):
    MULT_PARMS: ClassVar[tuple[str, str, str]]
    filter_config: _FilterConfig
    # Set in setData: the base class's property, not an attribute.
    @type_check_only
    @property
    def channel_geo(self) -> hou.Geometry: ...
    @type_check_only
    @channel_geo.setter
    def channel_geo(self, geo: hou.Geometry) -> None: ...
    @property
    def subtool(self) -> "SecondaryMotionSubtool | None": ...
    @property
    def state(self) -> _AnimateState | None: ...
    @property
    def scene(self) -> apex.Scene: ...
    def channelNames(self, ctrls: Iterable[str], parm: str) -> set[str]: ...
    def getFilterConfig(self, ctrl: str) -> apex.Dict: ...
    # The filter parameters' values, and the multipliers' channels evaluated at frame.
    def getConfigValue(self, ctrl: str, frame: float | None = ...) -> dict[str, float | None]: ...
    def setValue(
        self, parm_name: str, controls: Iterable[str], value: float, start_undo: bool = ..., apply_undo: bool = ...
    ) -> None: ...
    def onAnimatedParmAction(
        self, parm_name: str, controls: Iterable[str], action: str, value: float | None = ..., frame: float | None = ...
    ) -> bool: ...
    # extract_xform is a bit mask of the translate (1), rotate (2) and scale (4) components.
    def getScopedMultChannels(self, selected_controls: Iterable[str], extract_xform: int) -> dict[str, list[str]] | Literal[False]: ...

UNIFORM_WORLD_TRANSFORM: int
DYNAMIC_WORLD_TRANSFORM: int

class SecondaryMotionSubtool(EffectSubtool[SecondaryMotionSelectable]):
    selectable_parm: SecondaryMotionSelectable | None
    select_target: EffectParmSelectable.SELECT_TARGET
    joint_group: str
    debug: bool
    orig_control_skel: hou.Geometry | None
    ignore_root: bool
    control_config: SecondaryMotionControlConfig
    # The translation weight of each driven control (or joint) in dynamic world transform mode.
    trans_weights: dict[str, float]
    skel_diag_len: float
    use_custom_regularizer: bool
    regularizer_factor: float
    def __init__(
        self,
        tool: SecondaryMotionTool,
        driven_char_path: str,
        rest_skel: hou.Geometry,
        node_name: str,
        skel_name: str,
        rest_ctrl_skel: hou.Geometry | None,
    ) -> None: ...
    @type_check_only
    @property
    def tool(self) -> SecondaryMotionTool | None: ...
    @type_check_only
    @property
    def state(self) -> _AnimateState | None: ...
    def setSolverGraph(self, graph: apex.Graph, graph_name: str | None = ...) -> None: ...
    def getSolverGraphParms(self) -> apex.Dict: ...
    def setSolverGraphParms(self, parms: apex.Dict | Mapping[str, _apex._ValueArg]) -> None: ...
    # solve_controls is ignored: the select target decides.
    def solve(self, frame: float | None = ..., solve_controls: bool = ...) -> None: ...
    def createSolveCtrlBakeMap(self, solver_out: hou.Geometry | None = ...) -> dict[str, apexbake.BakeSourceXform]: ...
    def createSolveJointTRS(self, solver_out: hou.Geometry | None = ...) -> dict[str, _CtrlParms]: ...
    def createParmSelectable(self) -> SecondaryMotionSelectable: ...
    def onActivate(self, kwargs: _ToolActivateKwargs) -> None: ...
    def onSelectionChanged(self, control_selection: tuple[str, ...]) -> None: ...
    def onParmWidgetValueChangeToGraph(self, kwargs: _ParmChangeKwargs) -> None: ...
    def onAnimatedParmAction(self, kwargs: _AnimatedParmActionKwargs) -> bool: ...
    # The tool events below get an (ignored) dictionary from EffectTool.
    def getScopedChannels(self, kwargs: Mapping[str, object]) -> dict[str, list[str]] | Literal[False]: ...
    def pushChannels(self, kwargs: Mapping[str, object]) -> None: ...
    def scopeChannels(self, kwargs: _ScopeChannelsKwargs) -> None: ...
    def addGeometryChannelCallbacks(self, kwargs: _CollectionNamesKwargs) -> None: ...
    def removeGeometryChannelCallbacks(self, kwargs: Mapping[str, object] | None = ...) -> None: ...
    def onDeactivate(self) -> Literal[False]: ...
    # Does nothing.
    def updateStateParms(self, state_parms: Mapping[str, ViewerParmProperties]) -> None: ...
    def getDrivers(self) -> set[str]: ...
    def getDriven(self) -> set[str]: ...
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None: ...
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> None: ...
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> None: ...
    def onBakeEvent(self, kwargs: _BakeKwargs) -> Literal[True]: ...

def load(viewer_state: _AnimateState) -> SecondaryMotionTool: ...
def bindParametersToTemplate(template: hou.ViewerStateTemplate) -> None: ...
def bindActionsToMenu(menu: hou.ViewerStateMenu, hotkeys: asu.Hotkeys) -> None: ...
