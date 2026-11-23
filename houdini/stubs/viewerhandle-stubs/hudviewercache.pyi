import hou
import typing
import viewerhandle.hudapi as hud
from collections.abc import Iterable, Mapping
from typing import Literal
from viewerhandle.hudapi import _HUDSettingValue

from typing import TypeAlias
from typing import TypeAlias
_IntWindowSetting: TypeAlias = Literal['hudx', 'hudy', 'hudwidth', 'hudheight', 'hudlocked', 'visible', 'hudtitlevisible', 'hudtoolbarvisible', 'hudplacingmode', 'handleindirectmouse']
_OptionalStrWindowSetting: TypeAlias = Literal['hudnodetype', 'hudhandlename', 'huddockee', 'huddocker', 'huddocking', 'hudtitle']
class HUDWindowSettings:
    """ The settings associated with a HUD handle window and its widget(s).

        Handle settings include window settings (position, width, title, etc.)
        and settings specific to each HUD widget type (HUD slider min/max,
        lock limits, etc.).

        Window settings are consistent across all HUD widget types. They are
        stored in the `_window_settings` mapping.

        Widget parameters vary dynamically. They are stored in the
        `_widget_settings` mapping.

        HUD handle settings are stored in the Houdini tables. When first entering
        a state, the settings are loaded from the associated table. The first HUD
        update occurs after the activation event, but since the activation is
        deferred, the HUD handle is provisioned with the settings before the
        activation takes place. When exiting the state, the settings are saved
        in the tables.

        When entering a volatile state, the settings are not saved in the tables
        but in the cache when the HUD is deactivated. The HUD is updated with
        the latest cache when re-activated by releasing the volatile state
        hotkey.

        The first time a window is created, the associated HUDWindowSettings
        has its `_is_new` flag set. At the end of post-activation
        (see `_postWindowActivate` in HUDWindowManager), it is toggled.
        `isNewWindow()` indicates whether the window is newly created, and
        `setAsNewWindow()` is used to change the flag.
    """
    def __init__(self, id: str) -> None: ...
    def isNewWindow(self) -> bool:
        """ Check whether the window is new.
        """
    def setAsNewWindow(self, value: bool) -> None:
        """ Set whether the window is new.
        """
    def hasWindowSetting(self, setting_name: str) -> bool:
        """ Check whether the setting exists.
        """
    @typing.overload
    def windowSetting(self, setting_name: Literal['hudid']) -> str: ...
    @typing.overload
    def windowSetting(self, setting_name: _OptionalStrWindowSetting) -> str | None: ...
    @typing.overload
    def windowSetting(self, setting_name: _IntWindowSetting) -> int: ...
    @typing.overload
    def windowSetting(self, setting_name: str) -> _HUDSettingValue | None: ...
    @typing.overload
    def setWindowSetting(self, setting_name: Literal['hudid'], value: str) -> None: ...
    @typing.overload
    def setWindowSetting(self, setting_name: _OptionalStrWindowSetting, value: str | None) -> None: ...
    @typing.overload
    def setWindowSetting(self, setting_name: _IntWindowSetting, value: int) -> None: ...
    @typing.overload
    def setWindowSetting(self, setting_name: str, value: _HUDSettingValue | None) -> None: ...
    def updateFromPreferences(self, prefs: Mapping[str, int]) -> None:
        """ Update the cache given a dictionary of new preference values.
        """
    def setPreferenceSnapshot(self, prefs: dict[str, int]) -> None:
        """ Set the preference snapshot.
        """
    def hasWidgetSetting(self, widget_key: str, setting_name: str) -> bool:
        """ Checks whether the window has the specified widget setting.
        """
    def widgetSetting(self, widget_key: str, setting_name: str) -> _HUDSettingValue | None:
        """ Retrieve a widget setting by widget key and name.
        """
    def setWidgetSetting(self, widget_key: str, setting_name: str, value: _HUDSettingValue | None) -> None:
        """ Set a widget setting by widget key and name.
        """
    def widgetSettingCache(self) -> dict[str, dict[str, _HUDSettingValue | None]]:
        """ Retrieve the widget setting cache.
        """
    def createWidgetSettingCacheEntry(self, widget_key: str, setting_names: Iterable[str]) -> dict[str, _HUDSettingValue | None]:
        """ Create an empty widget setting cache entry.

            Replaces the previous cache if it existed.
        """
    def copyWidgetSettingCacheEntry(self, widget_key: str, parms: Mapping[str, _HUDSettingValue | None]) -> None:
        """ Copies a widget setting cache entry.
        """
    def inspect(self, output: hou.EnumValue[hou.resourceType] | None = None) -> None: ...

class HUDViewerCache:
    """ Holds a set of caches associated with a single scene viewer.

        Each scene viewer has its own HUDViewerCache. The HUDWindowManager
        singleton manages the lifecycle of all instances of HUDViewerCache and
        their association with scene viewers.

        The settings associated with a handle are first constructed on drag-and-drop
        or when an OPBinding handle is created on state entry. If the settings exist
        in the scene file, they are loaded as this point, and saved whenever leaving
        a state.

        The cache is cleared when the scene is closed. Individual entries are
        deleted when the associated node is deleted.
    """
    def __init__(self, **kwargs: str) -> None: ...
    def viewerID(self) -> str:
        """ Retrieve the current viewer ID.
        """
    def windowCache(self) -> dict[str, hud.HUDWindow]:
        """ Retrieve a reference to the HUDWindow cache.
        """
    def settingCache(self) -> dict[str, HUDWindowSettings]:
        """ Retrieve a reference to the HUDWindowSettings cache.
        """
    def stateWindowCache(self) -> dict[str, list[str]]:
        """ Retrieve a reference to the state-to-windows mapping cache.
        """
    def deferActionCache(self) -> dict[str, list[str]]:
        """ Retrieve a reference to the deferred actions cache.
        """
    def dockingCache(self) -> dict[str, tuple[str, list[str]]]:
        """ Retrieve a reference to the docking groups cache.
        """
    def windows(self) -> list[hud.HUDWindow]:
        """ Retrieve the list of HUDWindow objects stored in this cache.
        """
    def windowKeys(self) -> list[str]:
        """ Retrieve the list of HUDWindow keys stored in this cache. Note
            these are retrieved from the settings cache instead of the windows
            cache.
        """
    def window(self, window_key: str | None) -> hud.HUDWindow | None:
        """ Retrieve the window with the specified key.
        """
    def hasWindowSettingCache(self, window_key: str) -> bool:
        """ Check whether the HUDWindowSettings cache contains an entry for the
            specified key.
        """
    def windowSettingCache(self, window_key: str) -> HUDWindowSettings | None:
        """ Retrieve the HUDWindowSettings object for the specified key.
        """
    def createWindowSettingCache(self, window_key: str) -> HUDWindowSettings | None:
        """ Create a new HUDWindowSettings entry in the cache.
        """
    def deleteWindowSettingCache(self, window_key: str) -> None:
        """ Delete a HUDWindowSettings entry from the cache.
        """
    def saveWindowSettingCacheToScene(self, win: hud.HUDWindow, update_handle: bool = False) -> None:
        """ Save all window settings to the hou.Handle object's
            parameters dictionary.
        """
    def loadWindowSettingCacheFromScene(self, win: hud.HUDWindow) -> None:
        """ Load all window settings from the hou.Handle object's
            parameters dictionary.
        """
    def populateWindowSettingCache(self, hud_widget: hud.HUDWidgetBase, parms: Mapping[str, _HUDSettingValue | None]) -> None:
        ''' Populates the window setting cache dictionary of parms.
        
            Widget parms should have been flattened. I.e., instead of
            needing to access the parm with `parms[parm]["value"]`,
            `parms[parm]` should work.
        '''
    def setPreferenceSnapshot(self, window_key: str, prefs: dict[str, int]) -> None:
        """ Attach a snapshot of preferences to this window's settings.
        """
    def getDecodedCacheValues(self, hud_widget: hud.HUDWidgetBase) -> dict[str, int | float]:
        """ Decodes the cache values for a given HUD widget.
        """
    def clear(self) -> None:
        """ Close all windows and clear caches for the active viewer.
        """
    def clearWindowSettingsByState(self, state_name: str) -> None:
        """ Delete all HUDWindowSettings in the specified state.
        """
    def clearWindowCache(self, window_key: str, remove_setting_cache: bool = True) -> None:
        """ Clear the cache for a given window. Optionally remove the associated
            settings cache.
        """
    def clearWindowSettingsCache(self, window_key: str) -> None:
        """ Clear the HUDWindowSettings cache and clean the state-to-windows
            mapping for the specified window.
        """
    def clearWindowSettingsCacheByNode(self, node: hou.Node) -> None:
        """ Remove all HUD settings cache entries for a given node.
        """
    def clearStateWindowsCacheByKey(self, window_key: str) -> None:
        """Clean the state-to-windows mapping of the specified window key."""
    def sanitizeWindowSettingCache(self) -> None:
        """ Remove dead entries from the HUD settings cache.
        """
    def isActionDeferred(self, window_key: str, action_id: str) -> bool:
        """ Checks whether the deferred action exists for the specified window.
        """
    def setDeferredAction(self, window_key: str, action_id: str) -> None:
        """ Sets a deferred action for the specified window.
        """
    def unsetDeferredAction(self, window_key: str, action_id: str) -> None:
        """ Unsets a deferred action for the specified window.
        """
    def clearDeferredActions(self, window_key: str) -> None:
        """ Clears all deferred actions for the specified window.
        """
    def findWindowsByDeferredAction(self, action_id: str) -> list[hud.HUDWindow]:
        """ Finds all windows that have the specified action ID deferred.
        """
    def firstWindowWithDeferredAction(self, action_id: str) -> hud.HUDWindow | None:
        """ Finds the first window with the specified action ID deferred.
        """
    def inspect(self, output: hou.EnumValue[hou.resourceType] | None = None) -> None: ...
