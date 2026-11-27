import apex.glidetool as agt
import statehud.parmwidgetset as ws
from apex.glideutils import BrushKind as BrushKind, GlideToolbox as GlideToolbox, ModeKind as ModeKind, RetimeRange as RetimeRange, modeFromButtonStripMask as modeFromButtonStripMask
from apex.ui.animationhudwidgets import ParameterWidget as ParameterWidget
from houtypes import ViewerStateKwargs
from statehud.baseconfig import AbstractConfig
from statehud.window import WidgetBundleWindow

PARMS_HUD_SET: dict[GlideToolbox, ws._HUDParmTemplate]

class GlideParmsWidget(ParameterWidget[agt._AnimateState, WidgetBundleWindow]):
    hud_window: WidgetBundleWindow
    NAME: str
    WINDOW_TITLE: str
    WINDOW_WIDTH: int
    WINDOW_LABEL_WIDTH: int
    parm_set: ws.ParmWidgetSet | None
    def __init__(self, tool: agt.GlideTool, hud_window: WidgetBundleWindow | None, tab_widget_name: str | None, tab_name: str | None) -> None: ...
    @property
    def tool(self) -> agt.GlideTool | None: ...
    def setIsComSelected(self, on: bool) -> None: ...
    def setIsRigCtrlSelected(self, on: bool) -> None: ...
    def setIsPathCtrlSelected(self, on: bool) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def loadFromConfig(self, the_config: AbstractConfig, **kwargs: object) -> None:
        """Load from userdata on entering tool."""
    def saveToConfig(self, the_config: AbstractConfig, **kwargs: object) -> None:
        """Save to userdata on exiting tool."""
    @property
    def widgethotkey(self) -> str: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str) -> None: ...

SETTINGS_HUD_SET: dict[GlideToolbox, ws._HUDParmTemplate]

class GlideSettingsWidget(ParameterWidget[agt._AnimateState, WidgetBundleWindow]):
    hud_window: WidgetBundleWindow
    NAME: str
    WINDOW_TITLE: str
    WINDOW_WIDTH: int
    WINDOW_LABEL_WIDTH: int
    parm_set: ws.ParmWidgetSet | None
    def __init__(self, tool: agt.GlideTool, hud_window: WidgetBundleWindow | None, tab_widget_name: str | None, tab_name: str | None) -> None: ...
    @property
    def tool(self) -> agt.GlideTool | None: ...
    def setIsComSelected(self, on: bool) -> None: ...
    def setModeKind(self, mode_kind: ModeKind) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def loadFromConfig(self, the_config: AbstractConfig, **kwargs: object) -> None:
        """Load from userdata on entering tool."""
    def saveToConfig(self, the_config: AbstractConfig, **kwargs: object) -> None:
        """Save to userdata on exiting tool."""
    @property
    def widgethotkey(self) -> str: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str) -> None: ...
