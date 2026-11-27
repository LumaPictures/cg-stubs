import PySide6.QtWidgets
import apex
import apex.ui.controlhudwidgets as cu
import hou
import statehud.window as shud
from collections.abc import Callable as Callable, Mapping, Sequence
from houtypes import ViewerStateEventKwargs, ViewerStateKwargs, ViewerStatePlaybackChangeKwargs, ViewerStateVolatileClientKwargs
from statehud.window import HUDConfig, _ParmEventDict
from typing import Protocol

class _AnimateState(cu._AnimateState, Protocol):
    """The members of the Animate viewer state this module uses: those of the state it hands to
    `controlhudwidgets.ControlChannelWidget`."""

class _ToolHud(Protocol):
    @property
    def hud_window(self) -> shud.WidgetBundleWindow | None: ...

_USE_NEW_UI: bool
TRANSFORM_TAB: str

class ChannelWidgetHandler:
    scene_viewer: hou.SceneViewer
    show_transforms: bool
    show_abstracts: bool
    show_controlgroup: bool
    channel_parm_widget: cu.ControlChannelWidget
    controlgroup_slider: None
    active_sliders: list[cu.ControlChannelWidget]
    active_tool_huds: list[_ToolHud]
    current_selection_names: list[str]
    is_visible: bool
    hud_window: shud.WidgetBundleWindow
    tab_widget: None
    def __init__(self, state: _AnimateState, scene_viewer: hou.SceneViewer, callback: Callable[[_ParmEventDict], object] | None = None, tab_position: PySide6.QtWidgets.QTabWidget.TabPosition | None = None) -> None: ...
    @property
    def state(self) -> _AnimateState | None: ...
    def initWindow(self, width: int = 200, callback: Callable[[_ParmEventDict], object] | None = None) -> None: ...
    def initSliders(self) -> None: ...
    def bindHud(self, hud_widget: _ToolHud) -> None: ...
    def unbindHud(self, hud_widget: _ToolHud) -> None: ...
    def resetToolTabLabel(self) -> None: ...
    def setTitleFromCurrentTab(self) -> None: ...
    def currentTabChangedCallback(self, index: int) -> None: ...
    def activateWindow(self, title: str = 'Control Parms') -> None: ...
    @property
    def scene(self) -> apex.Scene: ...
    @property
    def widgethotkey(self) -> str | None: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def onPlaybackChangeEvent(self, kwargs: ViewerStatePlaybackChangeKwargs) -> bool: ...
    def onParmChangedEvent(self, kwargs: Mapping[str, object]) -> bool: ...
    def contextMenuCallback(self, action: str, slider_names: Sequence[str]) -> None: ...
    def setActiveSliders(self) -> None: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def isVisible(self) -> bool:
        """ Whether the hud window is visible. """
    def hideWindows(self) -> None:
        """ Hide the window. """
    def show(self, on: bool = True) -> None:
        """ Show or hide the window. """
    def activeWidget(self) -> cu.ControlChannelWidget | None:
        """ Return the first active tab. """
    def onSelectionChanged(self) -> None:
        """
        Called when the state changes its current selection.
        Here we should update the panels to reflect the current
        selection, and possibly change which panel is visible if
        we have changed what we are working with.
        """
    def loadFromConfig(self, config: HUDConfig) -> None:
        """ Load the window from the passed in config. """
    def saveToConfig(self, config: HUDConfig) -> None:
        """ Save the hud window to the passed in config. """
