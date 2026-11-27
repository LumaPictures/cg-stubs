import apex.dynamicmotiontool_2 as dmt
import statehud.parmwidgetset as ws
from apex.dynamicmotionutils import DynamicMotionToolbox as DynamicMotionToolbox, Mode as Mode, TargetingMethod as TargetingMethod, VisibleControls as VisibleControls
from apex.ui.animationhudwidgets import ParameterWidget as ParameterWidget
from houtypes import ViewerStateKwargs
from statehud.baseconfig import AbstractConfig
from statehud.window import WidgetBundleWindow

PARMS_HUD_SET: dict[DynamicMotionToolbox, ws._HUDParmTemplate]

class DynamicMotionParmsWidget(ParameterWidget[dmt._AnimateState, WidgetBundleWindow]):
    hud_window: WidgetBundleWindow
    NAME: str
    WINDOW_TITLE: str
    WINDOW_WIDTH: int
    WINDOW_LABEL_WIDTH: int
    parm_set: ws.ParmWidgetSet | None
    def __init__(self, tool: dmt.DynamicMotionTool, hud_window: WidgetBundleWindow | None, tab_widget_name: str | None, tab_name: str | None) -> None: ...
    @property
    def tool(self) -> dmt.DynamicMotionTool | None: ...
    def setMotionNum(self, motion_num: int) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def loadFromConfig(self, the_config: AbstractConfig, **kwargs: object) -> None:
        """Load from userdata on entering tool."""
    def saveToConfig(self, the_config: AbstractConfig, **kwargs: object) -> None:
        """Save to userdata on exiting tool."""
    @property
    def widgethotkey(self) -> str: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str) -> None: ...

SETTINGS_HUD_SET: dict[DynamicMotionToolbox, ws._HUDParmTemplate]

class DynamicMotionSettingsWidget(ParameterWidget[dmt._AnimateState, WidgetBundleWindow]):
    hud_window: WidgetBundleWindow
    NAME: str
    WINDOW_TITLE: str
    WINDOW_WIDTH: int
    WINDOW_LABEL_WIDTH: int
    parm_set: ws.ParmWidgetSet | None
    def __init__(self, tool: dmt.DynamicMotionTool, hud_window: WidgetBundleWindow | None, tab_widget_name: str | None, tab_name: str | None) -> None: ...
    @property
    def tool(self) -> dmt.DynamicMotionTool | None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def loadFromConfig(self, the_config: AbstractConfig, **kwargs: object) -> None:
        """Load from userdata on entering tool."""
    def saveToConfig(self, the_config: AbstractConfig, **kwargs: object) -> None:
        """Save to userdata on exiting tool."""
    @property
    def widgethotkey(self) -> str: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str) -> None: ...
