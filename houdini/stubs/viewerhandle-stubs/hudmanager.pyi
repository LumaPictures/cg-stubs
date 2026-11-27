import PySide6.QtCore
import hou
import typing
import viewerhandle.hudapi as hud
import viewerhandle.hudviewercache as hudv
from collections.abc import Callable as Callable, Generator, Mapping
from houtypes import SceneViewerEventKwargs, ViewerHandleKwargs, ViewerHandleParmChangeKwargs, ViewerParmProperties
from types import TracebackType
from typing import Literal, Never, TypedDict, Unpack
from viewerhandle.hudapi import _CreateHUDWidgetOptions, _HUDHandle, _HUDSettingValue
from viewerhandle.hudviewercache import _IntWindowSetting, _OptionalStrWindowSetting

from typing import TypeVar
from typing import TypeVar
_W = TypeVar('_W', bound=hud.HUDWidgetBase)
class _HUDActiveViewerOptions(TypedDict, total=False):
    viewer_id: str | None

ACTIVATE_ACTION_ID: str
DEACTIVATE_ACTION_ID: str
DEFERINIT_ACTION_ID: str
NODE_EVENTS: tuple[hou.EnumValue[hou.nodeEventType], hou.EnumValue[hou.nodeEventType]]

class HUDWindowManager:
    """ HUD Handle window manager.
    """
    theWinMgr: HUDWindowManager | None
    @staticmethod
    def instance() -> HUDWindowManager: ...
    def __init__(self, *args: Never, **kwargs: Never) -> None: ...
    def __del__(self) -> None: ...
    def hudPrefHandler(self) -> HUDPrefHandler: ...
    def onWindowHoverEvent(self, event: PySide6.QtCore.QEvent) -> None:
        """ Callback called when the mouse is hovering over a
            scene viewer.
        """
    def setViewerCache(self, scene_viewer: hou.SceneViewer | None) -> str | None:
        """ Create a new cache holding the HUD windows for
            a scene viewer and make the new cache active.
            If a cache exists already make it active.

            If the viewer is not compatible, like a network viewer,
            the active viewer is reset to None.

            Returns the previous active cache ID.
        """
    def setActiveViewer(self, viewer_id: str | None) -> str | None:
        """ Make the viewer_id cache the active viewer cache.
            Returns the previous active viewer id.
        """
    def viewerCache(self) -> hudv.HUDViewerCache | None:
        """ Return the active HUD viewer cache.
        """
    def onDeferClearViewerCache(self, active_viewer_id: str) -> None:
        """ Remove a viewer cache entry
            Note: the window(s), if any, will be deleted when the
            state exits.
        """
    def onViewerEvent(self, **kwargs: Unpack[SceneViewerEventKwargs]) -> None:
        """ Track viewer and state events for the current viewer.
        """
    def setFreezeState(self, value: bool | int) -> None: ...
    def createHUDWidget(self, handle: _HUDHandle, **kwargs: Unpack[_CreateHUDWidgetOptions[_W]]) -> _W | None:
        """ Called by HUD handle plugins to create a new HUD handle
            widget of type hud_widget_type. A HUD window is also
            created the first time the widget is created as well as a
            HUDWindowSettings cache object.
        """
    def window(self, scene_viewer: hou.SceneViewer, key: str) -> hud.HUDWindow | None:
        """ Return a HUD window contained in scene_viewer.
        """
    def windows(self, scene_viewer: hou.SceneViewer, filter_func: Callable[[hud.HUDWindow], bool] | None = None) -> Generator[hud.HUDWindow, None, None]:
        """ Ensure the windows are generated from the scene_viewer
            cache.
        """
    def setWindowVisibleStateByHandleName(self, scene_viewer: hou.SceneViewer, handle_name: str, onoff: bool) -> bool: ...
    def windowCache(self, scene_viewer: hou.SceneViewer) -> dict[str, hud.HUDWindow]:
        """ Retrieve a reference to the window cache for the current
            viewer.
        """
    def toggleWindowsVisibleState(self, scene_viewer: hou.SceneViewer) -> None:
        """ Toggle the visibility of all windows.
        """
    def areWindowsVisibleState(self, scene_viewer: hou.SceneViewer) -> bool:
        """ Return True if any windows are visible, False otherwise.
        """
    def toggleWindowsLockedState(self, scene_viewer: hou.SceneViewer) -> None:
        """ Toggle the locking state of all windows contained in
            scene_viewer.
        """
    def createID(self, handle: _HUDHandle) -> tuple[str, str]:
        """ Create the unique IDs for the Handle window and widget.
        """
    def displayAllWindows(self, scene_viewer: hou.SceneViewer, value: bool | int, include_persistent: bool = True) -> None:
        """ Set the visibility of all windows to the provided state.
        """
    def clearStateWindowSettings(self, state_name: str) -> None:
        """ Remove the window settings from the cache for a given state.
        """
    def deleteWindow(self, win: hud.HUDWindow, single: bool = False) -> None:
        """ This method deletes `win` along with any other cached
            windows if they share the same handle and node type.

            NOTE: Deleting a non-persistent window will also
                  delete persistent windows if they share the
                  same handle and node type.

            `win`:
                HUD window to delete

            `single`:
                Delete `win` only and its cache if True.
        """
    def closeWindow(self, win: hud.HUDWindow) -> None:
        """ Called when QWidget.close() is called on the HUD window.
        """
    def clearWindowSettingsCache(self, win: hud.HUDWindow) -> None: ...
    def inspect(self, scene_viewer: hou.SceneViewer | None = None, compact: bool = True, output: hou.EnumValue[hou.resourceType] | None = None) -> None: ...
    def changeVisualSize(self, visual_size_index: int, defer: bool = True) -> None: ...
    def visualSize(self) -> int: ...
    def setPlacingMode(self, placing_mode_index: int) -> None: ...
    def placingMode(self) -> int: ...
    def setIndirectMouseManipLevel(self, value: int) -> None: ...
    def indirectMouseManipLevel(self) -> int: ...
    def changeCompactState(self, value: bool | int, defer: bool = True) -> None:
        """ Compact or uncompact all windows
        """
    def isCompact(self) -> bool | int: ...
    def isSceneLoading(self) -> bool: ...
    def onLoadSettings(self, hud_widget: hud.HUDWidgetBase, settings: Mapping[str, ViewerParmProperties | _HUDSettingValue]) -> None:
        """ Called when the handle settings are being loaded in Houdini.
            The settings are re-structured and passed to the HUD widget.
        """
    def onMouseIndirectUpdate(self, hud_widget: hud.HUDWidgetBase, mouse_pos: tuple[float, float] = (0, 0), index: int = 0) -> bool: ...
    def onMouseIndirectStart(self, hud_widget: hud.HUDWidgetBase, mouse_pos: tuple[float, float] = (0, 0)) -> bool | None: ...
    def activateWindow(self, hud_widget: hud.HUDWidgetBase) -> None:
        """ Delay the window activation.
        """
    def deactivateWindow(self, hud_widget: hud.HUDWidgetBase, kwargs: ViewerHandleKwargs) -> None:
        ''' Called when a HUD handle is being deactivated. The
            window associated to the handle is closed and the
            window cache entry is deleted. The deactivation is
            deferred for persistent HUD or if a scene is loading.

            An entry is created in the deactivated windows cache for
            reloading on future activations.

            kwargs may contain:
            "node_deleted": True if the handle is deactivated as
                            a result of a node deletion. In this
                            case we skip the operation as the
                            cleanup will be done on the node
                            delete event.
                            (see _onNodeChangeEvent, etc..)

                            If the handle is dynamic there is no
                            callback installed on the node and the
                            window needs to be deleted here.
        '''
    def parmChangeEvent(self, hud_widget: hud.HUDWidgetBase, kwargs: ViewerHandleParmChangeKwargs) -> None: ...
    def onDeferActivateWindow(self, scene_viewer: hou.SceneViewer) -> None:
        """ Activate existing windows
        """
    def onDeferInitWindow(self, scene_viewer: hou.SceneViewer) -> None:
        """ Post initialize existing windows. This is required when
            a volatile state is being activated in which case
            we want to activate the windows immediately and defer
            the initialization.
        """
    def onDeferDeactivateWindow(self, scene_viewer: hou.SceneViewer) -> None:
        """ Deactivate existing windows
        """
    def onInit(self) -> None:
        """ This is called from the event loop to initialize
            the manager with UI related stuff.
        """
    def onSceneEvent(self, event_type: hou.EnumValue[hou.hipFileEventType]) -> None: ...
    @typing.overload
    def windowSetting(self, win: hud.HUDWindow, setting_name: Literal['hudid'] | _OptionalStrWindowSetting) -> str | None: ...
    @typing.overload
    def windowSetting(self, win: hud.HUDWindow, setting_name: _IntWindowSetting) -> int | None: ...
    @typing.overload
    def windowSetting(self, win: hud.HUDWindow, setting_name: str) -> _HUDSettingValue | None: ...
    @typing.overload
    def setWindowSetting(self, win: hud.HUDWindow, setting_name: Literal['hudid'], value: str) -> None: ...
    @typing.overload
    def setWindowSetting(self, win: hud.HUDWindow, setting_name: _OptionalStrWindowSetting, value: str | None) -> None: ...
    @typing.overload
    def setWindowSetting(self, win: hud.HUDWindow, setting_name: _IntWindowSetting, value: int) -> None: ...
    @typing.overload
    def setWindowSetting(self, win: hud.HUDWindow, setting_name: str, value: _HUDSettingValue | None) -> None: ...
    def isActionDeferred(self, scene_viewer: hou.SceneViewer, window_key: str, action_id: str) -> bool: ...
    def setDeferredAction(self, scene_viewer: hou.SceneViewer, window_key: str, action_id: str) -> None:
        """ Deferred an action for a given window
        """
    def unsetDeferredAction(self, scene_viewer: hou.SceneViewer, window_key: str, action_id: str) -> None:
        """ Unset a deferred action previously set for a given window
        """

class HUDActiveViewer:
    """ A context manager used for scoping HUD windows operations.
        Use this manager to ensure the proper viewer cache is set
        for the public API.
    """
    def __init__(self, hud_mgr: HUDWindowManager, scene_viewer: hou.SceneViewer | None, **kwargs: Unpack[_HUDActiveViewerOptions]) -> None: ...
    def __enter__(self) -> hudv.HUDViewerCache | None: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...

class HUDPrefHandler:
    """ Handle the setting of HUD preferences on HUD windows
    """
    APPLY: int
    UPDATE: int
    def __init__(self, hud_mgr: HUDWindowManager) -> None: ...
    def windowSettingPrefs(self) -> dict[str, int]:
        """ Retrieve a dictionary of all window setting preferences. """
    def applyPref(self, pref_name: str, win: hud.HUDWindow) -> None:
        """ Apply a preference called pref_name to a specific HUD window.

            `pref_name`: The HUD preference name.

            `win`: The window to apply the preference to.
        """
    def applyPrefs(self, win: hud.HUDWindow) -> None:
        """ Apply all supported pref values on win.

            `pref_name`: The HUD preference name.

            `win`: The window to apply the preferences to.
        """
    def updatePref(self, pref_name: str, win: hud.HUDWindow) -> None:
        """ Helper to update the preference called pref_name
            with the current HUD value.

            `pref_name`: The HUD preference name.

            `value`: The new preference value.

            `action`: The action to perform with the window and preference.
        """
    def updatePrefs(self, win: hud.HUDWindow) -> None:
        """ Update all supported pref values from the win settings.

            `pref_name`: The HUD preference name.

            `win`: The window used to update the preferences.

            `action`: The action to perform with the window and preference.
        """

def windowManager() -> HUDWindowManager: ...
def clearStateWindowSettings(state_name: str) -> None: ...
def displayAllWindows(scene_viewer: hou.SceneViewer, value: bool | int, include_persistent: bool = True) -> None: ...
def areWindowsVisibleState(scene_viewer: hou.SceneViewer) -> bool: ...
