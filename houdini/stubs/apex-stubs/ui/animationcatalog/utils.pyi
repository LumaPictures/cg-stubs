import _houqt
import hou
import logging
from .commands import addFolder as addFolder, sceneViewer as sceneViewer, setDefaultSceneViewer as setDefaultSceneViewer
from .undos import DeleteFoldersUndo as DeleteFoldersUndo
from apex.ui.animationcatalog.panel import Window as Window
from collections.abc import Sequence
from hutil.PySide import QtCore

GALLERY_SOURCE_IDENTIFIER: str
GALLERY_SOURCE_FILENAME: str
PANEL_INTERFACE_NAME: str
MAX_PREVIEW_LENGTH: int
SAVE_PREFERENCE_NAME: str
logger: logging.Logger

def saveGallerySource(path: str | None = None) -> None: ...
def getViewportImage(width: int = 512, height: int = 384) -> QtCore.QByteArray: ...
def getViewportGif(frame_start: float, frame_end: float, increment: int = 1, width: int = 512, height: int = 384) -> QtCore.QByteArray | None: ...
def getPreviewFrameIncrement(duration: int) -> int:
    """
    Returns the frame increment based on the duration in frames
    """
def resizeCatalogThumbnails(width: int = 512, height: int = 512) -> None:
    """
    Utility function which resizes all images in the currently loaded asset
    gallery to a given size.
    """
def createAnimationCatalogPane() -> hou.PaneTab:
    """
    Create a new floating Animation Catalog
    """
def getFirstCatalogPanel(set_current: bool = True, can_create: bool = False) -> Window | None: ...
def getPanelSelection(panel: Window | None = None) -> list[str]:
    """
    Returns the ids of all selected items in the Animation Catalog.
    If multiple Animation Catalogs are active, returns the ids in the first
    one.
    """
def createNewClip(pose: bool, panel: Window | None = None) -> bool: ...
def setSceneViewer(scene_viewer: hou.SceneViewer | None, panel: Window | None = None) -> None:
    """
    Sets the scene viewer to send animation catalog commands to.
    """
def updateControlSelection(scoped_controls: Sequence[str], panel: Window | None = None) -> None: ...
def resetBlendSlider(panel: Window | None = None) -> None: ...
def unload() -> None: ...
def promptToSave(message: str, allow_cancel: bool = True) -> bool:
    """
    Prompt to save the current catalog.
    Returns True if the catalog was saved or discarded, False if cancelled
    """
def expandCatalogPath(source_identifier: str) -> str: ...
def newCatalog() -> None: ...
def openCatalog(file: str | None = None) -> None: ...
def checkForNewerVersion(source_identifier: str) -> str: ...
def bumpCatalogFileName(source_identifier: str) -> str: ...
def createCatalogBackup(source_identifier: str) -> None: ...
def canSaveCatalog(source_identifier: str) -> bool: ...
def saveCatalog(use_current_path: bool = False) -> bool:
    """
    Save the current catalog to the provided path. If the path is none, prompt
    the user.
    """
def checkForUnsavedChanges() -> None: ...
def promptToSaveCatalogOnQuit() -> None:
    """Prompt to save the catalog at app quit."""
def createFolder(gallery: _houqt.QT_AssetGallery | None = None, edit: bool = True) -> None: ...
def exportSelectedFolders(gallery: _houqt.QT_AssetGallery | None = None) -> None:
    """
    Export the selected folders from the Animation Catalog to a new .bgeo file.
    """
def importCatalog() -> None:
    """
    Import items and folders from an external catalog file into the current
    Animation Catalog.
    """
def deleteFolders(folder_ids: list[str]) -> None:
    """
    Delete the specified folders from the Animation Catalog
    :param folder_ids: The ids of the folders to delete.
    """
