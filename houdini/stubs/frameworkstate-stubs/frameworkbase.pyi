import hou
import statehud.utils as shu
import typing
from collections.abc import Mapping
from frameworkstate.hotkeymanager import HotkeyManager as HotkeyManager
from frameworkstate.parameterwidget import ParameterWidget as ParameterWidget
from houtypes import ViewerStateCommandKwargs, ViewerStateDrawKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateParmChangeKwargs, ViewerStateVolatileClientKwargs
from statehud.baseconfig import AbstractConfig
from typing import Any, Generic, Literal

from typing import TypeVar
from typing import TypeVar
import statehud.window as shud
_T = TypeVar('_T')
_W_co = TypeVar('_W_co', bound=shud.WidgetBundleWindow, default=shud.WidgetBundleWindow, covariant=True)
_P_co = TypeVar('_P_co', bound='FrameWorkParameterWidget[shud.WidgetBundleWindow]', default='FrameWorkParameterWidget[shud.WidgetBundleWindow]', covariant=True)
TOOL_MODE: str
ANIMATE_TOOL_ICON: str
SCENE_NODE_CONFIG: Literal['scene_node']
DISABLE_ANIM_TOOLS_CONFIG: Literal['disable_animation_tools']
DEFAULT_TOOL_CONFIG: Literal['default_tool']
TOOLS_CONFIG: Literal['tools']
RADIAL_TOOL_MENU: Literal['radial_tool_menu']
USRDATA_PARM_KEY: str
MY_FRAMEWORK_TOGGLE: str
TOOL_TAB: str
FRAMEWORK_TAB: str
TAB_WIDGET: str
TAB_NAMES: list[str]
TOOL_STANDARD: str
DEFAULT_PACKAGE_NAME: str

class FrameWorkParameterWidget(ParameterWidget['State[FrameWorkParameterWidget[shud.WidgetBundleWindow]]', _W_co]):
    """we build our basic settings parameter widget for our example frame work 
    we want to have a few Generic parameters that we want to have always available in one tab, 
    our tools can then add and remove tabs to that widgets for tool specific parameters."""
    include_framework_tab: bool
    DEFAULT_LABEL_WIDTH: int
    def __init__(self, state: State, scene_viewer: hou.SceneViewer, include_framework_tab: bool) -> None: ...
    def resetToolTabLabel(self, toolname: str) -> None: ...
    def setTitleFromCurrentTab(self) -> None: ...
    def onFrameworkToggle(self, name: str, v: bool) -> bool:
        """this is a silly double toggle showing that we can use the same callback on 
        2 different toggle
        to execture a little function"""
    def loadFromConfig(self, the_config: AbstractConfig, **kwargs: object) -> None:
        ''' 
        Load from userdata on entering tool. very handy if you dont want to 
        constantly loose your last settings
        the user data saving happens in the framework! 
        in the function state._loadToolHUDSettings for example"
        '''
    def saveToConfig(self, the_config: AbstractConfig, **kwargs: object) -> None:
        """ Save to userdata on exiting tool. the user data saving happens in the frame work! 
        in the function state._saveToolHUDSettings for example"""

class State(Generic[_P_co]):
    state_name: str
    scene_viewer: hou.SceneViewer
    scene_node: hou.OpNode | None
    tools: dict[str, Any]
    active_tool: Any
    prev_active_tool: Any
    prev_active_tool_module_name: str | None
    radial_menu: hou.RadialMenu | None
    tool_is_active: bool | None
    load_tool_name: str | None
    hud_menu_rows: list[dict[str, str]]
    hud_template: dict[str, str | list[dict[str, str]]]
    hud_pin_mgr: shu.PinManager
    hud_parameter_panel: _P_co | None
    include_framework_tab: bool
    hud_initialized: bool
    DEFAULT_TOOLS: list[str]
    DEFAULT_TOOLS_STR_TO_LABEL: dict[str, str]
    DEFAULT_TOOLS_STR_TO_RADIAL_LOCATION: dict[str, hou.EnumValue[hou.radialItemLocation]]
    DEFAULT_TOOLS_ITEMS: list[tuple[str, str | None, str]]
    hotkeys: HotkeyManager
    def __init__(self, state_name: str, scene_viewer: hou.SceneViewer, hotkeys: HotkeyManager) -> None: ...
    @property
    def category(self) -> str: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """
        the default frame work event when entering the state via a specific node. we initialize all
        the widgets here
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """small example for the mouse event handling"""
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> None: ...
    def onInterrupt(self, kwargs: ViewerStateKwargs) -> bool | None: ...
    def onResume(self, kwargs: ViewerStateKwargs) -> bool | None: ...
    def onDraw(self, kwargs: ViewerStateDrawKwargs) -> bool | None: ...
    def onMouseWheelEvent(self, kwargs: ViewerStateEventKwargs) -> bool | None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool | None: ...
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """shows how to use the hotkeys of the framework key event
        """
    def onParmChangeEvent(self, kwargs: ViewerStateParmChangeKwargs) -> None:
        """here we use the tool bar button strip to switch our active frame work tool. 
        In addition to the buttons we also use in our example """
    def onExit(self, kwargs: ViewerStateKwargs) -> None:
        """closes the active tool and saves all the current hud parm values to the node userdata
        """
    def showSopGeometry(self, on: bool = True, force: bool = True, redraw: bool = True) -> None:
        """shows or hides the visible geometry output of the sop node. this is quite handy if you need 
        to show something completely else in the viewport to interact with. your sop node can for example output
        only an abstract could of delta points but the viewport can show a drawable that actually applies the data 
        for visualisation properly to a given input geometry. We do this a lot in the animat state simply because 
        the resulting scene geometry is not invoked at all
        """
    @typing.overload
    def getConfigValue(self, key: Literal['scene_node', 'default_tool'], default: None = ...) -> str | None: ...
    @typing.overload
    def getConfigValue(self, key: Literal['scene_node', 'default_tool'], default: _T) -> str | _T: ...
    @typing.overload
    def getConfigValue(self, key: Literal['disable_animation_tools'], default: None = ...) -> bool | None: ...
    @typing.overload
    def getConfigValue(self, key: Literal['disable_animation_tools'], default: _T) -> bool | _T: ...
    @typing.overload
    def getConfigValue(self, key: Literal['tools'], default: None = ...) -> dict[str, str] | None: ...
    @typing.overload
    def getConfigValue(self, key: Literal['tools'], default: _T) -> dict[str, str] | _T: ...
    @typing.overload
    def getConfigValue(self, key: Literal['radial_tool_menu'], default: None = ...) -> dict[str, hou.EnumValue[hou.radialItemLocation]] | None: ...
    @typing.overload
    def getConfigValue(self, key: Literal['radial_tool_menu'], default: _T) -> dict[str, hou.EnumValue[hou.radialItemLocation]] | _T: ...
    @typing.overload
    def getConfigValue(self, key: str, default: Any = ...) -> Any: ...
    def updateHUD(self) -> None:
        """ Update HUD Info for the state. """
    def toolEvent(self, eventname: str, *args: object, **kwargs: object) -> Any:
        """
        this is our generic tool event wrapper. if if finds an event it runs it from the current active
        subtool otherwise it simly does noting and returns False
        """
    def loadAndSwitchToTool(self, module_name: str | None, on_activate_kwargs: dict[str, object] | None) -> None:
        """we can use this to trigger a tool module load and switch via a command
        """
    def loadTool(self, module_name: str, do_reload: bool) -> None:
        """loads and instanciates the a tool object for the frame work based on a module path. this allows us
        to load custom tools from any path if we want to
        """
    def setActiveTool(self, toolname: str, on_activate_kwargs: dict[str, object] | None = None) -> None:
        """ Change the active tool to toolname. Pass toolname=None to
            swap to the main animate tool.

            Handles the transfer of HUD settings from one tool to another,
            as well as the saving and loading of HUD settings from user data.
        """
    def createRadialMenuCommandScript(self, command_name: str, args: Mapping[str, object]) -> str:
        """
        Create a script that directly runs a state command for the animate state.
        :param command_name: The command name to provide to the state's onCommand handler.
        :param args: The command arguments to provide to the state's onCommand handler.
        """
    def createRadialMenuSetToolScript(self, toolname: str) -> str:
        """
        Create a script to change to a different tool.
        :param toolname: The name of the tool to swap to when activating the script.
        """
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool: ...
