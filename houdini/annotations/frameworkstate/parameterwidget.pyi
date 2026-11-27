from typing import Generic, TypeVar

import hou
import statehud.window as shud
from frameworkstate.storageinterface import StorageInterface
from houtypes import ViewerStateEventKwargs, ViewerStateKwargs, ViewerStateVolatileClientKwargs

# The viewer state that manages the widget. ParameterWidget only probes it for `hud_parm_hk`, so
# any state will do; subclasses that use more of it say which (ParameterWidget[State]).
_S = TypeVar("_S", default=object)
# The HUD window: `None` until `initWindow`; subclasses that call it in `__init__` take a
# `WidgetBundleWindow`. Only the widget's own `initWindow` sets it, so it is covariant.
_W_co = TypeVar(
    "_W_co", bound=shud.WidgetBundleWindow | None, default=shud.WidgetBundleWindow | None, covariant=True
)

class ParameterWidget(Generic[_S, _W_co]):
    name: str
    scene_viewer: hou.SceneViewer
    state: _S
    storage_interface: StorageInterface | None
    hud_window: _W_co
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
        storage_interface: StorageInterface | None = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
    ) -> None: ...
    @property
    def widgethotkey(self) -> str | None: ...
    @widgethotkey.setter
    def widgethotkey(self, val: str | None) -> None: ...
    def initWindow(self, width: int = ...) -> None: ...
    def activateWindow(self, title: str = ..., set_tab_text: bool = ...) -> None: ...
    def setupUI(self, width: int = ..., title: str = ..., set_tab_text: bool = ...) -> None: ...
    def show(self, on: bool = ...) -> None: ...
    def hideWindow(self) -> None: ...
    def isVisible(self) -> bool: ...
    def toggleSettingsWidget(self, kwargs: ViewerStateEventKwargs) -> None: ...
    def onKeyTransitEvent(self, kwargs: ViewerStateEventKwargs) -> bool: ...
    def onVolatileClientEvent(self, kwargs: ViewerStateVolatileClientKwargs) -> bool: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> bool: ...
