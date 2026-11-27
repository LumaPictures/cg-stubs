import PySide6.QtGui
import PySide6.QtWidgets
import apex
import hou
import statehud.utils as shutils
import statehud.window as shud
from collections.abc import Callable as Callable, Mapping
from houtypes import ViewerStateEventKwargs, ViewerStateKwargs, ViewerStatePlaybackChangeKwargs, ViewerStateVolatileClientKwargs
from hutil.PySide import QtWidgets
from statehud.parmutils import ButtonParm
from statehud.window import _ParmEventDict
from typing import Generic, Protocol

from typing import TypeVar
from typing import TypeVar
_S = TypeVar('_S', bound=_HudState, default=_HudState)
_W = TypeVar('_W', bound=shud.WidgetBundleWindow | None, default=shud.WidgetBundleWindow | None)
_C_co = TypeVar('_C_co', bound=apex.Control, default=apex.Control, covariant=True)
class _HudState(Protocol):
    @property
    def scene(self) -> apex.Scene: ...

SETKEY_MODIFIER: tuple[int, int]
DELKEY_MODIFIER: tuple[int, int]
DELKEY_ALL_MODIFIER: tuple[int, int]
SETKEY_ALL_MODIFIER: tuple[int, int]
RESET_MODIFIER: tuple[int, int]
SETKEY_SYMBOL: str
DELKEY_SYMBOL: str
RESET_SYMBOL: str
SETKEY_ALL_SYMBOL: str
DELKEY_ALL_SYMBOL: str
SLIDER_MOUSE_MODIFIERS: dict[tuple[int, int], str]
TOGGLE_MOUSE_MODIFIERS: dict[tuple[int, int], str]
PARMS_SUFFIX: str
SETTINGS_SUFFIX: str
TOOL_TAB_WIDGET: str
TAB_WIDGET: str
CONSTRAINT_TAB: str
TOOL_TAB: str

class BaseHudWidget(Generic[_S, _W, _C_co]):
    """
    A class that can be used as the base class for any floating hud window.
    """
    scene_viewer: hou.SceneViewer
    name: str
    hud_window: _W
    tab_widget_name: str | None
    tab_name: str | None
    is_visible: bool
    current_controls: list[_C_co]
    def __init__(self, state: _S, scene_viewer: hou.SceneViewer, name: str = 'hud_window', hud_window: shud.WidgetBundleWindow | None = None, tab_widget_name: str | None = None, tab_name: str | None = None) -> None: ...
    @property
    def state(self) -> _S | None: ...
    @property
    def scene(self) -> apex.Scene: ...
    @property
    def widgethotkey(self) -> str: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str) -> None: ...
    def setTitle(self, title: str | None) -> None: ...
    def setTitleFromControl(self, control: apex.Control, multi_selection: bool = False, use_namespace: bool = False) -> str: ...
    def initWindow(self, width: int = 400, callback: Callable[[_ParmEventDict], object] | None = None) -> None: ...
    def activateWindow(self, title: str = 'Control Parms', set_tab_text: bool = False) -> None: ...
    def onPlaybackChangeEvent(self, kwargs: ViewerStatePlaybackChangeKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def _updateFromControls(self) -> bool:
        """ Override to customize how to update the window from controls. """
    def hideWindow(self) -> None: ...
    def show(self, on: bool = True) -> None: ...
    def onWindowShown(self) -> bool | None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onSelectionChanged(self) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> bool: ...

class ParameterWidget(Generic[_S, _W]):
    """
    A base class to be used for any tool parameters or settings
    """
    name: str
    scene_viewer: hou.SceneViewer
    hud_window: _W
    tab_widget_name: str | None
    tab_name: str | None
    is_visible: bool
    mute_value_update: int
    def __init__(self, state: _S, scene_viewer: hou.SceneViewer, name: str | None = None, hud_window: shud.WidgetBundleWindow | None = None, tab_widget_name: str | None = None, tab_name: str | None = None) -> None: ...
    @property
    def state(self) -> _S | None: ...
    @property
    def scene(self) -> apex.Scene: ...
    @property
    def widgethotkey(self) -> str: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str) -> None: ...
    def initWindow(self, width: int = 400, callback: Callable[[_ParmEventDict], object] | None = None) -> None: ...
    def activateWindow(self, title: str = 'Settings', set_tab_text: bool = False) -> None: ...
    def show(self, on: bool = True) -> None: ...
    def hideWindow(self) -> None: ...
    def isVisible(self) -> bool: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> bool: ...

class ToolbarButtonParm(ButtonParm):
    """
    A class for managing the parameter corresponding to a toolbar button.
    """
    button_name: str
    toolbar_name: str
    def __init__(self, parm_name: str, tab_widget_name: str | None, tab_name: str | None, button_name: str, toolbar_name: str) -> None: ...
    @staticmethod
    def typeName() -> str: ...
    def triggerChangedEvent(self, hud_window: shud.WidgetBundleWindow) -> None: ...

def createCrossIcon(size: int | None = None, color: PySide6.QtGui.QColor | None = None, margin_factor: int = 3) -> PySide6.QtGui.QIcon:
    """Create a small 'x' cross icon for reset buttons.
    margin_factor: higher = smaller cross (3 = default inline, 4 = bigger for toolbar)."""

class ToolbarWidget(QtWidgets.QWidget):
    has_copy: bool
    has_snap: bool
    has_reset: bool
    component_buttonstrip: None
    reset_btn: shutils.ToolButton | None
    snap_btn: shutils.ToolButton | None
    copy_btn: shutils.ToolButton | None
    paste_btn: shutils.ToolButton | None
    use_transparency: bool
    core_buttons: dict[str, shutils.ToolButton]
    extra_buttons: Mapping[str, PySide6.QtWidgets.QAbstractButton]
    _hbox: PySide6.QtWidgets.QHBoxLayout
    def __init__(self, copypaste: bool = True, snap: bool = True, reset: bool = True, extra_buttons: Mapping[str, PySide6.QtWidgets.QAbstractButton] | None = None) -> None: ...
    def getButton(self, name: str) -> PySide6.QtWidgets.QAbstractButton | None: ...
    def addParameters(self, hud_window: shud.WidgetBundleWindow, name: str, tab_widget_name: str | None, tab_name: str | None) -> None: ...
