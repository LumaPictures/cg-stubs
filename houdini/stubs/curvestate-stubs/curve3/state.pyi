import hou
import statehud.window as shs
from collections.abc import Callable as Callable, Iterable, Mapping
from curvestate.curve3.adapters import SceneViewerAdapter as SceneViewerAdapter, get_viewer_adapter as get_viewer_adapter
from curvestate.curve3.channels import Curve3ChannelManager as Curve3ChannelManager
from curvestate.curve3.constants import TOOL_MODE_ITEMS as TOOL_MODE_ITEMS
from curvestate.curve3.controller import Curve3Controller as Curve3Controller
from curvestate.curve3.debug import log as log
from curvestate.curve3.dragger import Curve3Dragger as Curve3Dragger
from curvestate.curve3.drawables import Curve3DrawableManager as Curve3DrawableManager
from curvestate.curve3.handle_manager import Curve3HandleManager as Curve3HandleManager
from curvestate.curve3.pick_controller import PickController as PickController
from curvestate.curve3.selection_controller import SelectionController as SelectionController
from curvestate.curve3.tool_base import Curve3ToolBase as Curve3ToolBase
from curvestate.curve3.tool_draw import Curve3DrawTool as Curve3DrawTool
from curvestate.curve3.tool_edit import Curve3EditTool as Curve3EditTool
from curvestate.curve3.tool_helpers import node_handle_is_alive as node_handle_is_alive
from curvestate.curve3.tool_orient import Curve3OrientTool as Curve3OrientTool
from curvestate.curve3.tool_scale import Curve3ScaleTool as Curve3ScaleTool
from curvestate.curve3.undo_helpers import HUDParmUndoBlock as HUDParmUndoBlock, HUDParmUndoCache as HUDParmUndoCache, execute_with_undo as execute_with_undo
from frameworkstate.frameworkbase import FrameWorkParameterWidget, State as FrameworkState
from frameworkstate.hotkeymanager import HotkeyManager
from houtypes import ViewerParmProperties, ViewerStateCommandKwargs, ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateMenuActionKwargs, ViewerStateMenuPreOpenKwargs, ViewerStateNodeChangeKwargs, ViewerStateParmChangeKwargs, ViewerStateSelectionKwargs, ViewerStateVolatileClientKwargs
from hutil.qt.data.panels import _HudTemplate
from statehud.baseconfig import AbstractConfig
from statehud.parmutils import _HUDParmValue
from staterecordutils import RecordableViewerState
from typing import Any, Literal, Unpack, overload

class _Curve3SettingsHUDWindow(shs.WidgetBundleWindow):
    @overload
    def getParmValue(self, name: Literal['liveupdate', 'curve3_edit_show_handle', 'curve3_synchronize_keys', 'curve3_approx_shape_del', 'curve3_convert_match_poly', 'curve3_soft_transform_enabled', 'curve3_orient_scale_change_all_selected'], menus_as_int: bool = ...) -> bool: ...
    @overload
    def getParmValue(self, name: Literal['curve3_convert_divs', 'curve3_draw_order'], menus_as_int: bool = ...) -> int: ...
    @overload
    def getParmValue(self, name: Literal['curve3_soft_transform_radius', 'curve3_guide_scale'], menus_as_int: bool = ...) -> float: ...
    @overload
    def getParmValue(self, name: Literal['curve3_edit_plane', 'curve3_edit_preview_curve', 'curve3_draw_primtype', 'curve3_draw_new_anchortype', 'curve3_show_frame_guide', 'curve3_show_frame_guide_components'], menus_as_int: Literal[True] = ...) -> int | None: ...
    @overload
    def getParmValue(self, name: Literal['curve3_edit_plane', 'curve3_edit_preview_curve', 'curve3_draw_primtype', 'curve3_draw_new_anchortype', 'curve3_show_frame_guide'], menus_as_int: Literal[False]) -> str | None: ...
    @overload
    def getParmValue(self, name: Literal['curve3_show_frame_guide_components'], menus_as_int: Literal[False]) -> str | list[str] | None: ...
    @overload
    def getParmValue(self, name: str, menus_as_int: bool = ...) -> _HUDParmValue: ...

class Curve3SettingsHUD(FrameWorkParameterWidget):
    """Curve3 settings HUD window and mode-scoped settings UI."""
    curve_state: CurveState
    controller: Curve3Controller
    active_tool_name: str
    hud_window: _Curve3SettingsHUDWindow
    PRIMTYPE_WIDGET: Literal['curve3_draw_primtype']
    ORDER_WIDGET: Literal['curve3_draw_order']
    NEW_ANCHORTYPE_WIDGET: Literal['curve3_draw_new_anchortype']
    EDIT_PLANE_WIDGET: Literal['curve3_edit_plane']
    EDIT_SHOW_HANDLE_WIDGET: Literal['curve3_edit_show_handle']
    EDIT_PREVIEW_CURVE_WIDGET: Literal['curve3_edit_preview_curve']
    SYNCHRONIZE_KEYS_WIDGET: Literal['curve3_synchronize_keys']
    SOFT_TRANSFORM_RADIUS_WIDGET: Literal['curve3_soft_transform_radius']
    SOFT_TRANSFORM_TOGGLE_WIDGET: Literal['curve3_soft_transform_enabled']
    APPROX_SHAPE_DEL_WIDGET: Literal['curve3_approx_shape_del']
    CONVERT_MATCH_POLY_WIDGET: Literal['curve3_convert_match_poly']
    CONVERT_DIVS_WIDGET: Literal['curve3_convert_divs']
    PRIMTYPE_LABELS: list[str]
    MODE_TABS: Literal['curve3_mode_tabs']
    TAB_GENERAL: str
    TAB_EDIT: str
    TAB_DRAW: str
    TAB_ORIENT_SCALE: str
    TAB_NAMES: list[str]
    TAB_LABELS: list[str]
    SHOW_FRAME_GUIDE_WIDGET: Literal['curve3_show_frame_guide']
    SHOW_FRAME_GUIDE_COMPONENTS_WIDGET: Literal['curve3_show_frame_guide_components']
    GUIDE_SCALE_WIDGET: Literal['curve3_guide_scale']
    ORIENT_SCALE_CHANGE_ALL_SELECTED_WIDGET: Literal['curve3_orient_scale_change_all_selected']
    LIVE_UPDATE_MODE_WIDGET: Literal['liveupdate']
    FRAME_GUIDE_COMPONENT_NAMES: list[str]
    FRAME_GUIDE_COMPONENT_LABELS: list[str]
    STORAGE_PARMS: tuple[str, ...]
    def __init__(self, curve_state: CurveState, scene_viewer: hou.SceneViewer, include_framework_tab: bool) -> None: ...
    def initWindow(self, width: float = 400) -> None: ...
    def set_setting_value(self, widget_name: str, value: object, *, state_parms: dict[str, ViewerParmProperties] | None = None) -> None:
        """
        Set one settings HUD value through the full synchronized path.

        This updates the viewer-state parm dictionary when available, mirrors
        node-owned settings to the node parm, updates the HUD widget without
        recursively reapplying callbacks, and applies the runtime controller
        value from the setting binding.
        """
    def handle_node_setting_parm_changes(self, parm_names: Iterable[str]) -> None: ...
    def loadParmsFromStorage(self) -> None: ...
    def saveParmsToStorage(self) -> None: ...
    def apply_runtime_values(self) -> None:
        """
        Push current HUD values into controller/backend runtime state.

        The settings HUD owns both persisted widget state and node-owned widget
        mirroring, so CurveState should only ask the panel to apply itself
        instead of reaching into individual setting callbacks.
        """
    def loadFromConfig(self, _the_config: AbstractConfig, **_kwargs: object) -> None: ...
    def saveToConfig(self, _the_config: AbstractConfig, **_kwargs: object) -> None: ...
    def resetToolTabLabel(self, toolname: str) -> None: ...
    def set_active_tool_name(self, tool_name: str) -> None: ...
    def sync_show_handle_widget(self) -> None: ...

class Curve3FrameworkState(FrameworkState, RecordableViewerState):
    """Curve3-specific framework state variant with custom parameter panel."""
    DEFAULT_TOOLS: list[str]
    DEFAULT_TOOLS_STR_TO_LABEL: dict[str, str]
    DEFAULT_TOOLS_STR_TO_RADIAL_LOCATION: dict[str, hou.EnumValue[hou.radialItemLocation]]
    scene_node: hou.OpNode | None
    hud_parameter_panel: Curve3SettingsHUD | None
    active_tool: Curve3ToolBase | None
    def __init__(self, *args: Unpack[tuple[str, hou.SceneViewer | hou.CompositorViewer, HotkeyManager]], **kwargs: object) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None: ...
    def setActiveTool(self, toolname: str, on_activate_kwargs: ViewerStateKwargs | dict[str, Any] | None = None) -> None:
        """
        Curve3 policy: tool switches must not mutate HUD window state.
        No HUD save/load/clear/tab/visibility operations here.

        NOTE: The Curve3 tools can be registered with another framework state,
        but this settings HUD is still CurveState-specific. A standalone tool
        host must either provide compatible HUD panel APIs or skip Curve3 HUD
        synchronization.
        """
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """Handle settings HUD hotkeys without resizing the settings window every key event."""
    def onExit(self, kwargs: ViewerStateKwargs) -> None:
        """Persist HUD + tool settings on state exit even without framework tab."""
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool: ...
    def isPlayingBackTest(self) -> bool: ...

class CurveState(Curve3FrameworkState):
    state_category: hou.OpNodeTypeCategory
    hotkeys: HotkeyManager
    include_framework_tab: bool
    adapter: SceneViewerAdapter
    controller: Curve3Controller
    tools: dict[str, Curve3ToolBase]
    channel_manager: Curve3ChannelManager
    hk_create_mode_point: str
    hk_toggle_settings_hud: str
    hk_delete_mode_action: str
    hk_cycle_tool_forward: str
    hk_cycle_tool_backward: str
    hk_create_channels: str
    hk_scale_increase_selected: str
    hk_scale_decrease_selected: str
    scene_node: hou.OpNode | None
    HUD_TEMPLATE: _HudTemplate
    def __init__(self, state_name: str, scene_viewer: hou.SceneViewer | hou.CompositorViewer, category: hou.OpNodeTypeCategory | None = None) -> None: ...
    def active_tool_prompt_message(self, kwargs: ViewerStateEventKwargs | None = None) -> str: ...
    def set_prompt_message(self, message: str) -> None: ...
    def refresh_prompt_message(self, kwargs: ViewerStateEventKwargs | None = None) -> None: ...
    def cycle_tool(self, kwargs: ViewerStateEventKwargs | None = None, *, forward: bool) -> None: ...
    def toggle_settings_hud_window(self) -> bool: ...
    def showActiveHUD(self, node: hou.OpNode | None, val: bool) -> None:
        """ Show/hide the HUD and update the values. """
    def set_settings_hud_value(self, widget_name: str, value: object, *, state_parms: dict[str, ViewerParmProperties] | None = None) -> bool:
        """Set one settings HUD value through the synchronized settings path."""
    def setActiveTool(self, toolname: str, on_activate_kwargs: ViewerStateKwargs | dict[str, Any] | None = None) -> None:
        """Set the active tool and keep the tool-mode state parm in sync."""
    def hud_hints_for_tool(self, tool_name: str) -> list[dict[str, str]]: ...
    def show(self, visible: bool) -> None:
        """ Display or hide drawables/gadgets. """
    def onGenerate(self, kwargs: ViewerStateKwargs) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """ Set up gadgets, callbacks, show drawables.
        """
    def onExit(self, kwargs: ViewerStateKwargs) -> None:
        """ Called when the state is exited. """
    def _guard_deleted_scene_node(self, kwargs: Mapping[str, object]) -> bool:
        """Return True and block dispatch if the viewer state's node was deleted."""
    @RecordableViewerState.recordableEvent
    def onResume(self, kwargs: ViewerStateKwargs) -> None:
        """ Called when the state is resumed. """
    @RecordableViewerState.recordableEvent
    def onInterrupt(self, kwargs: ViewerStateKwargs) -> None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> None: ...
    @RecordableViewerState.recordableEvent
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    @RecordableViewerState.recordableEvent
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def _on_key_event_after_tool(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    @RecordableViewerState.recordableEvent
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    @RecordableViewerState.recordableEvent
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool | None: ...
    def onSelection(self, kwargs: ViewerStateSelectionKwargs[hou.GeometrySelection]) -> bool: ...
    @RecordableViewerState.recordableEvent
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> bool | None: ...
    def onNodeChangeEvent(self, kwargs: ViewerStateNodeChangeKwargs) -> bool: ...
    @RecordableViewerState.recordableEvent
    def onMenuAction(self, kwargs: ViewerStateMenuActionKwargs) -> bool | None: ...
    def onMenuPreOpen(self, kwargs: ViewerStateMenuPreOpenKwargs) -> bool: ...
    @RecordableViewerState.recordableEvent
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool | None: ...
    def onUndoOrRedo(self) -> None: ...
    def handleSelectionUndoOrRedo(self, group: str | None) -> None: ...
    def savePlaybackOutputGeometry(self, geo: hou.Geometry) -> None: ...

def createContextMenu(state_typename: str, state_category: hou.NodeTypeCategory, hotkey_definitions: hou.PluginHotkeyDefinitions) -> hou.ViewerStateMenu: ...
def bindCurveStateHotkeys(hotkeys: hou.PluginHotkeyDefinitions, state_typename: str, state_cat: hou.OpNodeTypeCategory) -> None: ...
def bindCurveStateParameters(template: hou.ViewerStateTemplate) -> None: ...
def bindCurveStateTemplate(template: hou.ViewerStateTemplate, state_typename: str, state_category: hou.OpNodeTypeCategory) -> hou.ViewerStateTemplate: ...
def createCurveStateTemplate(state_typename: str, state_label: str, icon_name: str, state_category: hou.OpNodeTypeCategory, state_class_type: Callable[[str, hou.SceneViewer | hou.CompositorViewer], object]) -> hou.ViewerStateTemplate: ...
def createViewerStateTemplate() -> hou.ViewerStateTemplate:
    """ Mandatory entry point to create and return the viewer state
        template to register. """
