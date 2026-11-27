import apex.dynamicmotiontool_2 as dmt
import statehud.parmwidgetset as ws
from apex.dynamicmotionutils import DynamicMotionToolbox
from apex.ui.animationhudwidgets import ParameterWidget
from typing import type_check_only

from houtypes import ViewerStateKwargs
from statehud.baseconfig import AbstractConfig
from statehud.window import WidgetBundleWindow

PARMS_HUD_SET: dict[DynamicMotionToolbox, ws._HUDParmTemplate]
SETTINGS_HUD_SET: dict[DynamicMotionToolbox, ws._HUDParmTemplate]

class DynamicMotionParmsWidget(ParameterWidget[dmt._AnimateState, WidgetBundleWindow]):
    hud_window: WidgetBundleWindow
    # None once the widget has exited.
    parm_set: ws.ParmWidgetSet | None
    # The tool passes its activate kwargs' tab info, which defaults to (None, None, None), and whose
    # settings tab is None when the settings HUD uses folders; the base class makes a window for None.
    def __init__(
        self, tool: dmt.DynamicMotionTool, hud_window: WidgetBundleWindow | None, tab_widget_name: str | None, tab_name: str | None
    ) -> None: ...
    @property
    def tool(self) -> dmt.DynamicMotionTool | None: ...
    # Set in __init__: the base class's property, not an attribute.
    @type_check_only
    @property
    def widgethotkey(self) -> str: ...
    @type_check_only
    @widgethotkey.setter
    def widgethotkey(self, val: str) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    # The options are ignored.
    def loadFromConfig(self, the_config: AbstractConfig, **kwargs: object) -> None: ...
    def saveToConfig(self, the_config: AbstractConfig, **kwargs: object) -> None: ...

class DynamicMotionSettingsWidget(ParameterWidget[dmt._AnimateState, WidgetBundleWindow]):
    hud_window: WidgetBundleWindow
    # None once the widget has exited.
    parm_set: ws.ParmWidgetSet | None
    # The tool passes its activate kwargs' tab info, which defaults to (None, None, None), and whose
    # settings tab is None when the settings HUD uses folders; the base class makes a window for None.
    def __init__(
        self, tool: dmt.DynamicMotionTool, hud_window: WidgetBundleWindow | None, tab_widget_name: str | None, tab_name: str | None
    ) -> None: ...
    @property
    def tool(self) -> dmt.DynamicMotionTool | None: ...
    # Set in __init__: the base class's property, not an attribute.
    @type_check_only
    @property
    def widgethotkey(self) -> str: ...
    @type_check_only
    @widgethotkey.setter
    def widgethotkey(self, val: str) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    # The options are ignored.
    def loadFromConfig(self, the_config: AbstractConfig, **kwargs: object) -> None: ...
    def saveToConfig(self, the_config: AbstractConfig, **kwargs: object) -> None: ...
