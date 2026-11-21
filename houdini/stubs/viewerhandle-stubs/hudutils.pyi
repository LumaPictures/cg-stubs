# Houdini stubs generated from Houdini 22.0.466

import hou
import typing
from collections.abc import Callable, Collection, Mapping
from hutil.PySide import QtCore
from hutil.undo import Command as Command
from viewerhandle.hudapi import HUDWidgetBase, _HUDHandle
from viewerhandle.hudwindow import HUDWindow

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
__all__ = ['Command', 'parmLabels', 'valueToList', 'HUDDockable', 'listToString', 'formatSettings', 'convertSettings', 'bindHandleSettings']

def valueToList(value: object, count: int) -> str:
    """ Encodes a value repeated count times into a string.
    """
def listToString(item_list: Collection[object]) -> str:
    """ Helper for encoding a list into a string. The list items
        are comma separated.
    """
@typing.overload
def stringToList(encoded_string: str, to_type: None = ...) -> list[str]: ...
@typing.overload
def stringToList(encoded_string: str, to_type: Callable[[str], _T]) -> list[_T]: ...
def formatSettings(setting_dict: Mapping[str, int | float | str | list[str] | None]) -> str:
    ''' Builds a setting string usable with hou.ViewerStateState.bindHandle,
        hou.ViewerStateState.bindHandleStatic or hou.Handle.applySettings.

        setting_dict: Dictionary containing the setting info for
                      creating the setting string:

                      key: Setting name such hudc.BTN_TYPE and hudc.PARM_MIN.
                      value: Value for a given setting. Value type
                             must match the setting type: int, string,
                             float. List of values is supported for
                             button hud handle setting (i.e. BTN_xxx).

        e.g.
        settings = {hudc.PARM_MIN : 10, hudc.PARM_MAX: 200, hudc.PARM_DEFAULT: 20}
        print( formatSettings(settings) )
        > hudrangemin(10) hudrangemax(200) huddefval(20

        # Create a setting for a button strip
        settings = {hudc.BTN_TEXT : ["A", "B", "C"]}
        print( formatSettings(settings) )
        > hudbtntext(\'A,B,C\')

        settings = {hudc.BTN_TEXT : ["A", "B", "C"],
            hudc.BTN_TOOLTIP: ["Create A", "Create B", "Create C"]}
        print( formatSettings(settings) )
        > hudbtntext(\'A,B,C\') hudbtntooltip(\'A,B,C\')

        settings = {hudc.BTN_TEXT : ["A", "B", "C"], hudc.BTN_TOOLTIP: None}
        print( formatSettings(settings) )
        > hudbtntext(\'A,B,C\') hudbtntooltip(\'A,B,C\')

        # Create a setting for a radio button strip
        btn_settings = formatSettings({
            hudc.WIN_TITLE: "My Radio Buttons",
            hudc.BTN_TEXT: ["Radio A", "Radio B", "Radio C"],
            hudc.BTN_TYPE: [hudc.BTN_TYPE_TOGGLE, hudc.BTN_TYPE_TOGGLE, hudc.BTN_TYPE_TOGGLE],
            hudc.BTN_RADIO_STRIP: 1,
            hudc.BTN_RADIO_STRIP_DEFAULT: 1
        })

    '''
def convertSettings(settings: object) -> list[str]:
    """ Convert a comma separated setting string to a list of strings.
    """
def parmLabels(parm_template: hou.ParmTemplate) -> list[str]:
    """ Build a list of label names for a parm template using the template
        naming scheme. The last element of the list is the base name used
        for bulding the labels. If the template has only one component,
        the list will contain the base name only.

        return: [name1, name2, ..., nameN, basename]
    """
def isValidHOM(hom_obj: object) -> bool: ...
def isValidViewer(scene_viewer: hou.SceneViewer) -> bool: ...
def isValidHudWidget(hud_widget: HUDWidgetBase | None) -> bool: ...

class HUDDockable:
    """ Helper to perform docking operations with HUDWindow
        objects
    """
    def __init__(self, win: HUDWindow) -> None: ...
    def window(self) -> HUDWindow: ...
    def key(self) -> str: ...
    def isDocked(self) -> bool: ...
    def dockee(self) -> HUDWindow | None: ...
    def docker(self) -> HUDWindow | None: ...
    def isDockee(self) -> bool: ...
    def isDocker(self) -> bool: ...
    def isTopDocker(self) -> bool: ...
    def dockees(self) -> list[HUDWindow]: ...
    def topDocker(self) -> HUDWindow:
        """ Return the very top docker window of the underlying
            window or itself if it has no docker.
        """
    def lastDockee(self) -> HUDWindow | None: ...
    def bottomWindow(self) -> HUDWindow:
        """ Return the bottom window or the underlying window if
            there are no dockees.
        """
    def topWindow(self) -> HUDWindow:
        """ Return the underlying window.
        """
    def dockTo(self, docker_win: HUDWindow) -> None:
        """ Dock to a docker window.
        """
    def refresh(self) -> None:
        """ Refresh the docking for this HUD.
        """
    def pos(self) -> QtCore.QPoint: ...
    def height(self) -> int: ...
    def width(self) -> int: ...
    def rect(self) -> QtCore.QRect: ...
    def size(self) -> QtCore.QSize: ...
    def update(self) -> None:
        """ Update all docked windows
        """
    def align(self) -> None:
        """ Align the dockees position to the docker.
        """
    def move(self, pt: QtCore.QPoint) -> None:
        """ Move the underlying window and its dockees to 'pt'.
        """
    def moveBy(self, delta_pt: QtCore.QPoint) -> None:
        """ Move the underlying window and its dockees by 'delta'.
        """

def bindHandleSettings(template: hou.ViewerHandleTemplate) -> None:
    """ Bind the mandatory settings to the hud handle template. These
        settings are mostly for internal use and should not be edited.
    """
def indirectMouseIsSupported(hud_handle: _HUDHandle | None) -> bool:
    """ Return True if the given HUD handle supports indirect
        mouse handling.

        This checks the HUD handle's parameters for HINDIRECTMOUSE.
        If the parameter exists, its value is returned; otherwise,
        False is returned.
    """
