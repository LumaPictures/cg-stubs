import apex.glidetool as agt
import statehud.parmwidgetset as ws
from apex.glideutils import GlideToolbox
from apex.ui.animationhudwidgets import ParameterWidget
from typing import type_check_only

from houtypes import ViewerStateKwargs
from statehud.baseconfig import AbstractConfig
from statehud.window import WidgetBundleWindow

PARMS_HUD_SET: dict[GlideToolbox, ws._HUDParmTemplate]
SETTINGS_HUD_SET: dict[GlideToolbox, ws._HUDParmTemplate]

class GlideParmsWidget(ParameterWidget[agt._AnimateState, WidgetBundleWindow]):
    hud_window: WidgetBundleWindow
    # None once the widget has exited.
    parm_set: ws.ParmWidgetSet | None
    # The tool passes its activate kwargs' tab info, which defaults to (None, None, None), and whose
    # settings tab is None when the settings HUD uses folders; the base class makes a window for None.
    def __init__(
        self, tool: agt.GlideTool, hud_window: WidgetBundleWindow | None, tab_widget_name: str | None, tab_name: str | None
    ) -> None: ...
    @property
    def tool(self) -> agt.GlideTool | None: ...
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

class GlideSettingsWidget(ParameterWidget[agt._AnimateState, WidgetBundleWindow]):
    hud_window: WidgetBundleWindow
    # None once the widget has exited.
    parm_set: ws.ParmWidgetSet | None
    # The tool passes its activate kwargs' tab info, which defaults to (None, None, None), and whose
    # settings tab is None when the settings HUD uses folders; the base class makes a window for None.
    def __init__(
        self, tool: agt.GlideTool, hud_window: WidgetBundleWindow | None, tab_widget_name: str | None, tab_name: str | None
    ) -> None: ...
    @property
    def tool(self) -> agt.GlideTool | None: ...
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
