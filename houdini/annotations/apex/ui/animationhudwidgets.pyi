from collections.abc import Callable, Mapping
from typing import Generic, Protocol, TypeVar

import apex
import hou
import statehud.utils as shutils
import statehud.window as shud
from houtypes import ViewerStateEventKwargs, ViewerStateKwargs, ViewerStatePlaybackChangeKwargs, ViewerStateVolatileClientKwargs
import PySide6.QtGui
import PySide6.QtWidgets
from statehud.parmutils import ButtonParm
from statehud.window import _ParmEventDict

# The viewer state that owns the widget (the Animate state, which tools pass on). The widgets only
# use its scene (and probe it for `hud_parm_hk`); subclasses that use more of it say which state
# they take (`BaseHudWidget[_AnimateState]`).
class _HudState(Protocol):
    @property
    def scene(self) -> apex.Scene: ...

_S = TypeVar("_S", bound=_HudState, default=_HudState)
# The HUD window: `None` until `initWindow`; subclasses that call it in `__init__` take a
# `WidgetBundleWindow`.
_W = TypeVar("_W", bound=shud.WidgetBundleWindow | None, default=shud.WidgetBundleWindow | None)
# The controls the widget shows (`current_controls`); a subclass may only pick some kinds.
_C_co = TypeVar("_C_co", bound=apex.Control, default=apex.Control, covariant=True)

# (Qt mouse button, Qt keyboard modifiers) -> hotkey symbol.
SETKEY_MODIFIER: tuple[int, int]
DELKEY_MODIFIER: tuple[int, int]
DELKEY_ALL_MODIFIER: tuple[int, int]
SETKEY_ALL_MODIFIER: tuple[int, int]
RESET_MODIFIER: tuple[int, int]
SLIDER_MOUSE_MODIFIERS: dict[tuple[int, int], str]
TOGGLE_MOUSE_MODIFIERS: dict[tuple[int, int], str]

class BaseHudWidget(Generic[_S, _W, _C_co]):
    scene_viewer: hou.SceneViewer
    name: str
    hud_window: _W
    tab_widget_name: str | None
    tab_name: str | None
    is_visible: bool
    current_controls: list[_C_co]
    def __init__(
        self,
        state: _S,
        scene_viewer: hou.SceneViewer,
        name: str = ...,
        hud_window: shud.WidgetBundleWindow | None = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
    ) -> None: ...
    @property
    def state(self) -> _S | None: ...
    @property
    def scene(self) -> apex.Scene: ...
    @property
    def widgethotkey(self) -> str: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str) -> None: ...
    def setTitle(self, title: str | None) -> None: ...
    def setTitleFromControl(self, control: apex.Control, multi_selection: bool = ..., use_namespace: bool = ...) -> str: ...
    def initWindow(self, width: int = ..., callback: Callable[[_ParmEventDict], object] | None = ...) -> None: ...
    def activateWindow(self, title: str = ..., set_tab_text: bool = ...) -> None: ...
    def onPlaybackChangeEvent(self, kwargs: ViewerStatePlaybackChangeKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def _updateFromControls(self) -> bool: ...
    def hideWindow(self) -> None: ...
    def show(self, on: bool = ...) -> None: ...
    def onWindowShown(self) -> bool | None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onMouseEvent(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onSelectionChanged(self) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> bool: ...

class ParameterWidget(Generic[_S, _W]):
    name: str
    scene_viewer: hou.SceneViewer
    hud_window: _W
    tab_widget_name: str | None
    tab_name: str | None
    is_visible: bool
    mute_value_update: int
    def __init__(
        self,
        state: _S,
        scene_viewer: hou.SceneViewer,
        name: str | None = ...,
        hud_window: shud.WidgetBundleWindow | None = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
    ) -> None: ...
    @property
    def state(self) -> _S | None: ...
    @property
    def scene(self) -> apex.Scene: ...
    @property
    def widgethotkey(self) -> str: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str) -> None: ...
    def initWindow(self, width: int = ..., callback: Callable[[_ParmEventDict], object] | None = ...) -> None: ...
    def activateWindow(self, title: str = ..., set_tab_text: bool = ...) -> None: ...
    def show(self, on: bool = ...) -> None: ...
    def hideWindow(self) -> None: ...
    def isVisible(self) -> bool: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> bool: ...

class ToolbarButtonParm(ButtonParm):
    button_name: str
    toolbar_name: str
    def __init__(self, parm_name: str, tab_widget_name: str | None, tab_name: str | None, button_name: str, toolbar_name: str) -> None: ...
    @staticmethod
    def typeName() -> str: ...
    def triggerChangedEvent(self, hud_window: shud.WidgetBundleWindow) -> None: ...

def createCrossIcon(size: int | None = ..., color: PySide6.QtGui.QColor | None = ..., margin_factor: int = ...) -> PySide6.QtGui.QIcon: ...

class ToolbarWidget(PySide6.QtWidgets.QWidget):
    has_copy: bool
    has_snap: bool
    has_reset: bool
    # Never set.
    component_buttonstrip: None
    reset_btn: shutils.ToolButton | None
    snap_btn: shutils.ToolButton | None
    copy_btn: shutils.ToolButton | None
    paste_btn: shutils.ToolButton | None
    use_transparency: bool
    core_buttons: dict[str, shutils.ToolButton]
    extra_buttons: Mapping[str, PySide6.QtWidgets.QAbstractButton]
    _hbox: PySide6.QtWidgets.QHBoxLayout
    def __init__(
        self, copypaste: bool = ..., snap: bool = ..., reset: bool = ..., extra_buttons: Mapping[str, PySide6.QtWidgets.QAbstractButton] | None = ...
    ) -> None: ...
    def getButton(self, name: str) -> PySide6.QtWidgets.QAbstractButton | None: ...
    def addParameters(self, hud_window: shud.WidgetBundleWindow, name: str, tab_widget_name: str | None, tab_name: str | None) -> None: ...
