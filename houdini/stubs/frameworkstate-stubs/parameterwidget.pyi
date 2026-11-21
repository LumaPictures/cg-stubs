# Houdini stubs generated from Houdini 22.0.466

import hou
import statehud.window as shud
from frameworkstate.storageinterface import StorageInterface as StorageInterface
from houtypes import ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateVolatileClientKwargs
from typing import Generic

from typing import TypeVar
from typing import TypeVar
_S = TypeVar('_S', default=object)
class ParameterWidget(Generic[_S]):
    """ 
    this is a basic class for a hud window that can bundle various commonly used 
    settings in a frame work. tools can easily add additional tabs to that widget. 
    so hud window can be context dependent. We use this heavily in the animate state 
    to have one unified settings widget for all our tools the cool thing about this class:
    if it can be used to create your initial hud window for the frame work. but if 
    you already have a framework hud window, the same class can be used as a base class!!! 
    to create a tab on that existing hud window and simply extend the functionality of 
    the existing one :D
    """
    name: str
    scene_viewer: hou.SceneViewer
    state: _S
    storage_interface: StorageInterface | None
    hud_window: shud.WidgetBundleWindow | None
    tab_widget_name: str | None
    tab_name: str | None
    is_visible: bool
    mute_value_update: int
    def __init__(self, state: _S, scene_viewer: hou.SceneViewer, name: str | None = None, hud_window: shud.WidgetBundleWindow | None = None, storage_interface: StorageInterface | None = None, tab_widget_name: str | None = None, tab_name: str | None = None) -> None: ...
    @property
    def widgethotkey(self) -> str | None: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str | None) -> None:
        """our widget is managed from the frame work state. Since the framework is 
        in charge of the hotkeys
        is alos needs to actively set the hotkey that we will use to toggle the widgets 
        visibility on or off
        """
    def initWindow(self, width: int = 400) -> None:
        """makes sure that our actual hud window we want to how is properly prepped 
        """
    def activateWindow(self, title: str = 'Settings', set_tab_text: bool = False) -> None:
        """
        finishes setting up the window ui
        """
    def setupUI(self, width: int = 400, title: str = 'Settings', set_tab_text: bool = False) -> None:
        """initializes the overall widget"""
    def show(self, on: bool = True) -> None: ...
    def hideWindow(self) -> None: ...
    def isVisible(self) -> bool: ...
    def toggleSettingsWidget(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool:
        """we open or close the our hud window with the dedicated hotkey"""
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool:
        """needed for that toggle on of behavior that we want from our hud window"""
    def onExit(self, kwargs: ViewerStateKwargs) -> bool:
        """closes the window if a new hud window was created"""
