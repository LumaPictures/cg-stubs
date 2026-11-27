import _houqt
import hou
import statehud.window as shud
from apex.ui.animationhudwidgets import BaseHudWidget as BaseHudWidget, _HudState
from collections.abc import Callable as Callable
from houtypes import ViewerStateKwargs

INIT_GALLERY_SOURCE_CB: str

class AnimationCatalogHUDPanel(BaseHudWidget[_HudState]):
    """
    A HUD Panel for the Animation catalog.
    """
    callbacks: dict[str, Callable[[], object]]
    WIDGET_NAME: str
    def __init__(self, state: _HudState, scene_viewer: hou.SceneViewer, name: str = 'catalog_hud_widget', hud_window: shud.WidgetBundleWindow | None = None, tab_widget_name: str | None = None, tab_name: str | None = None, help_button_path: str = '/ref/panes/assetgallery') -> None: ...
    def showDragThumbnails(self, on: bool) -> None: ...
    def setCallback(self, callback: Callable[[], object], name: str) -> None: ...
    def activate(self, title: str | None = None) -> None:
        """
        We fully initialize the hudwindow outside the init function in order to
        pre configure the cls before showing it
        """
    def onExit(self, kwargs: ViewerStateKwargs) -> bool: ...

class AssetGalleryHUDView(_houqt.QT_AssetGallery):
    """
    The view used for the HUD Asset Gallery.
    """
    def __init__(self, scene_viewer: hou.SceneViewer | None, help_button_path: str = '/ref/panes/assetgallery') -> None: ...
