from collections.abc import Callable

import _houqt
import hou
import statehud.window as shud
from apex.ui.animationhudwidgets import BaseHudWidget, _HudState
from houtypes import ViewerStateKwargs

INIT_GALLERY_SOURCE_CB: str

# Unused: nothing creates one.
class AnimationCatalogHUDPanel(BaseHudWidget[_HudState]):
    WIDGET_NAME: str
    callbacks: dict[str, Callable[[], object]]
    def __init__(
        self,
        state: _HudState,
        scene_viewer: hou.SceneViewer,
        name: str = ...,
        hud_window: shud.WidgetBundleWindow | None = ...,
        tab_widget_name: str | None = ...,
        tab_name: str | None = ...,
        help_button_path: str = ...,
    ) -> None: ...
    def showDragThumbnails(self, on: bool) -> None: ...
    def setCallback(self, callback: Callable[[], object], name: str) -> None: ...
    def activate(self, title: str | None = ...) -> None: ...
    def onExit(self, kwargs: ViewerStateKwargs) -> bool: ...

class AssetGalleryHUDView(_houqt.QT_AssetGallery):
    def __init__(self, scene_viewer: hou.SceneViewer | None, help_button_path: str = ...) -> None: ...
