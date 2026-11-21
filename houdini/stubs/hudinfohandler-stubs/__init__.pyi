# Houdini stubs generated from Houdini 22.0.466

import hou
import re
from collections.abc import Callable as Callable, Iterable
from hutil.qt.data.HUDInfo import HUDInfo
from hutil.qt.data.panels import _HudTemplate, _HudUpdates
from hutil.qt.hud.sceneview import ViewerHud
from typing import Required, TypedDict, Unpack

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
class _HUDOptions(TypedDict, total=False):
    scene_viewer_path: str
    panel_layout: int
    hud_label_color: Iterable[float]
    hud_value_color: Iterable[float]
    hud_background_color: Iterable[float]
    hud_text_shadow: bool
    hud_background_visibility: bool
    hud_panel_size: int

class _HUDInfoHandlerKwargs(TypedDict, total=False):
    scene_viewer_path: Required[str]
    panel_layout: Required[int]
    hud_label_color: Iterable[float]
    hud_value_color: Iterable[float]
    hud_background_color: Iterable[float]
    hud_text_shadow: bool
    hud_background_visibility: bool
    hud_panel_size: int

class _ToolInfoHeaderKwargs(TypedDict, total=False):
    title: Required[str]
    description: Required[str]
    icon: Required[str]
    show_min_hint: bool
    force_default_update: bool

USE_HUD_TEXTURE: bool
TEXTURE_EXPR: re.Pattern[str]
IS_DARWIN: bool
USE_OLD_HUD: bool

class HUDInfoHandler:
    """ Class to drive and render hutil.qt.data.HUDInfo into an OpenGL
        texture in the current GL context.
    """
    enable_trace: bool
    @staticmethod
    def trace(func: Callable[_P, _R]) -> Callable[_P, _R]: ...
    @staticmethod
    def textureInfo(tid: int = -2, w: int = 0, h: int = 0) -> list[int]: ...
    def __init__(self, **kwargs: Unpack[_HUDInfoHandlerKwargs]) -> None: ...
    def close(self) -> None: ...
    def updateOverlay(self) -> list[int]:
        """ Create the hud overlay texture.
        """
    def setTemplate(self, hud_template: _HudTemplate) -> None: ...
    def updateContent(self, hud_values: _HudUpdates) -> bool: ...
    def clearContent(self) -> None: ...
    def updateHotkeyBindings(self) -> None: ...
    def minimize(self, minimize_state: bool) -> int: ...
    def toggle(self) -> int: ...
    def queryState(self) -> int:
        """ Return the current toolinfo state.
        """
    def setOptions(self, **kwargs: Unpack[_HUDOptions]) -> int:
        """
        Set HUD options such as label color, panel size and others.
        Options can be set in batch or individually.
        """
    def setToolInfoHeader(self, **kwargs: Unpack[_ToolInfoHeaderKwargs]) -> int: ...
    def log(self, value: object) -> None: ...

class HUDInfoWindow(HUDInfo):
    """ HUDInfo implementation used by HUDInfoHandler
    """
    def __init__(self, scene_viewer: hou.SceneViewer, panel_layout: int) -> None: ...
    def onWindowPlacement(self) -> None: ...
    def onInitWindow(self) -> None:
        """ Init the window as opaque. We just want the window to
            have a transparent background style.
        """

def viewerHud(viewer: hou.SceneViewer) -> ViewerHud | None: ...
def onHudSetTemplate(hud: ViewerHud | HUDInfoHandler, hud_template: _HudTemplate) -> None: ...
def onHudSetToolInfoHeader(hud: ViewerHud | HUDInfoHandler, title: str, description: str, icon: str, show_min_hint: bool, force_default_update: bool = False) -> int: ...
def onHudMinimize(hud: ViewerHud | HUDInfoHandler, minimize_value: bool = False) -> int:
    """ Minimize or maximize the HUD.
    """
def onHudToggle(hud: ViewerHud | HUDInfoHandler) -> int: ...
def onHudUpdate(hud: ViewerHud | HUDInfoHandler, hud_values: _HudUpdates) -> int: ...
def onHudClearContent(hud: ViewerHud | HUDInfoHandler) -> None: ...
def onHudUpdateHotkeyBindings(hud: ViewerHud | HUDInfoHandler) -> None: ...
def hudQueryState(hud: ViewerHud | HUDInfoHandler) -> int: ...
