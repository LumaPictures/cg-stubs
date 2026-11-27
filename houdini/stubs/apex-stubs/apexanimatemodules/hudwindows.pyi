import abc
import apex.stateutils_2 as asu
import dbg
import hou
import statehud.utils as shu
import statehud.window as shs
from apex.apexanimatemodules.base import ApexAnimateBaseModule as ApexAnimateBaseModule, _AnimateState as _BaseState
from apex.ui.animationhudwidgets import CONSTRAINT_TAB as CONSTRAINT_TAB, TAB_WIDGET as TAB_WIDGET, TOOL_TAB as TOOL_TAB
from apex.ui.channelhudwidgets import _AnimateState as _ChannelHudState
from apex.ui.selectionmanager import hudpanel as hudpanel
from apex.ui.selectionmanager.hudpanel import SelectionSetHUDPanel as SelectionSetHUDPanel
from apex.ui.settingshudwidgets import AnimateSettingsWidget as AnimateSettingsWidget, _AnimateState as _SettingsState
from apex.ui.splitchannelwidget import SplitChannelWidgetHandler as SplitChannelWidgetHandler
from apex.xformgadget import KEY_ROTATES_CMD as KEY_ROTATES_CMD, KEY_SCALES_CMD as KEY_SCALES_CMD, KEY_TRANSLATES_CMD as KEY_TRANSLATES_CMD, _HandleSettingsUpdateKwargs
from houtypes import SceneViewerEventKwargs, ViewerStateCommandKwargs, ViewerStateEnterKwargs, ViewerStateEventKwargs, ViewerStateKwargs, ViewerStatePlaybackChangeKwargs, ViewerStateVolatileClientKwargs
from statehud.window import _ParmEventDict
from staterecordutils import RecordableViewerState

class _AnimateState(RecordableViewerState, _ChannelHudState, _SettingsState, _BaseState, metaclass=abc.ABCMeta):
    """The Animate viewer state (`viewer_states/apexanimate.py`), with the members this module uses."""
    def clearCustomBakeParms(self) -> None: ...

USRDATA_PARM_KEY: str
USRDATA_CHANNEL_KEY: str
USRDATA_SEL_KEY: str
USRDATA_MOUSE_SEL_KEY: str
PRIMARY_XFORM_INDEX: int

class ApexAnimateHUDWindows(ApexAnimateBaseModule):
    """
    This class is owned by the APEX Animate state and has access to
    all of its variables.

    It implements all of the functions necessary to manage cameras in the
    APEX Aniamte viewer state.
    """
    hud_channel_panel: SplitChannelWidgetHandler | None
    hud_parameter_panel: AnimateSettingsWidget | None
    hud_sel_panel: SelectionSetHUDPanel | None
    hud_mouse_sel_panel: SelectionSetHUDPanel | None
    hud_pin_mgr: shu.PinManager
    stashed_visible_huds: list[SelectionSetHUDPanel | SplitChannelWidgetHandler | AnimateSettingsWidget]
    def __init__(self, state: _AnimateState) -> None: ...
    def onEnter(self, kwargs: ViewerStateEnterKwargs) -> None:
        """ On viewer state enter event
        """
    def onExit(self, kwargs: ViewerStateKwargs) -> None:
        """ On viewer state exit event
        """
    @dbg.ZoneScopedDecorator
    def initHudWidgets(self) -> None:
        """
        Initializes the HUD panels
        """
    def updateParameters(self) -> None: ...
    def toggleAllHuds(self) -> None:
        """
        Toggle all the huds.
        If any is visible, stash whats visible, and hide all.
        If none are visible, and a stash exists, show only whats in
        the stash.
        If none are visible, and no stash exists, show all.
        """
    def onHUDParmEvent(self, kwargs: _ParmEventDict) -> None:
        """ Called whenever the parameter HUD window is interacted with by the user
        """
    def onHUDSettingEvent(self, kwargs: _ParmEventDict) -> None:
        """ Called whenever the settings HUD window is interacted with by the user
        """
    def onSelectionChanged(self, update_channel_widget: bool = True) -> None:
        """ Called when the selection changes
        """
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> None:
        """ Handles the viewer state's onMouseEvent
        """
    def onKeyEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Handles the viewer state's onKeyEvent
        """
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """ Handles the viewer state's onKeyTransitEivent
        """
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> None:
        """ Handles the viewer state's onVolatileClientEvent
        """
    def onPlaybackChangeEvent(self, kwargs: ViewerStatePlaybackChangeKwargs) -> None:
        """ Handles the viewer state's onPlaybackChangeEvent
        """
    def onXformGadgetSettingsEvent(self, kwargs: _HandleSettingsUpdateKwargs) -> None:
        """ Called when the settings for the xform gadget are changed
        """
    def onSceneViewerEvent(self, kwargs: SceneViewerEventKwargs) -> None:
        """Respond to viewer events relevant to the active Animate state."""
    def deactivateToolHUD(self) -> None:
        """ Saves the active tool's user data settings and
            deactivate's the tool's tab.
        """
    def activateToolHUD(self) -> None:
        """ Loads the newly activated tool's user data settings and
            activates the tool's tab.
        """
    def bindToolHuds(self, tool: asu._Tool | None = None) -> None:
        """
        Binds the tool hud widget handlers to the state's hud widget
        handlers.
        This ensures that event handlers are called on the tool's hud
        widget handlers.
        """
    def unbindToolHuds(self, tool: asu._Tool | None = None) -> None:
        """
        Unbinds the tool hud widget handlers from the state's hud widget
        handlers.
        This ensures that event handlers are no longer called on the
        tool's hud widget handlers.
        """
    def saveToolHUDSettings(self, node: hou.SopNode | None = None, tool: asu._Tool | None = None, settings_widget: bool = True, hud_widget: bool = True) -> None:
        """ Save the HUD settings for the settings widget and hud widget
            on the active tool.
        """
    def saveHUDSettings(self, node: hou.SopNode | None = None, sel_panel: bool = True, mouse_sel_panel: bool = True, parm_panel: bool = True, channel_panel: bool = True) -> None:
        """ Save the HUD settings for the selection set panels, the parm
            panel and the channel panels.
        """
    def loadToolHUDSettings(self, node: hou.SopNode | None = None, tool: asu._Tool | None = None, settings_widget: bool = True, hud_widget: bool = True) -> None:
        """ Load the HUD Settings for the settings widget and the hud widget
            on the active tool.
        """
    @dbg.ZoneScopedDecorator
    def loadHUDSettings(self, node: hou.SopNode | None = None, sel_panel: bool = True, mouse_sel_panel: bool = True, parm_panel: bool = True, channel_panel: bool = True) -> None:
        """ Load the HUD Settings for the selection set panels,
            the parm panel and the channel panels.
        """
    def onCommand(self, kwargs: ViewerStateCommandKwargs) -> bool:
        """ Implements the commands for managing the huds
        """
    def getHUDWindow(self, name: str) -> shs.WidgetBundleWindow | None: ...
    @property
    def state(self) -> _AnimateState: ...
