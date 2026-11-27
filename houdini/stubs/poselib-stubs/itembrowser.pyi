import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
from . import capturewidget as capturewidget, infowindow as infowindow, itemgrid as itemgrid, itemlibrary as itemlibrary, itemnavigator as itemnavigator, plglobals as plglobals, poselibundos as poselibundos, posemodel as posemodel
from collections.abc import Sequence
from hutil.PySide import QtCore, QtWidgets
from typing import Any, Generic

from typing import TypeVar
from typing import TypeVar
_ItemModelT_co = TypeVar('_ItemModelT_co', bound=itemlibrary.ItemModel, covariant=True, default=itemlibrary.ItemModel)
_GridViewT_co = TypeVar('_GridViewT_co', bound=itemgrid.GridView, covariant=True, default=itemgrid.GridView)
DELETE_POSE: str
ADD_POSE: str
DELETE_FOLDER: str
ADD_FOLDER: str

class ItemBrowser(QtWidgets.QWidget, Generic[_ItemModelT_co, _GridViewT_co]):
    """Contains generic interface for navigating and modifying an item 
       library."""
    newLibraryDialog: NewLibraryDialog
    infoWindow: infowindow.InfoWindow
    itemModel: _ItemModelT_co
    treeView: itemnavigator.TreeView
    gridView: _GridViewT_co
    libraryPathLabel: QtWidgets.QLabel
    toolTip: ToolTip
    contextMenu: QtWidgets.QMenu
    showItemInfoAction: PySide6.QtGui.QAction
    newFolderAction: PySide6.QtGui.QAction
    copyAction: PySide6.QtGui.QAction
    cutAction: PySide6.QtGui.QAction
    pasteAction: PySide6.QtGui.QAction
    renameAction: PySide6.QtGui.QAction
    renameAction2: PySide6.QtGui.QAction
    changeThumbnailFileAction: PySide6.QtGui.QAction
    changeThumbnailViewportAction: PySide6.QtGui.QAction
    thumbnailMenu: QtWidgets.QMenu
    exportToHDANodeAction: PySide6.QtGui.QAction
    exportToHDAFileAction: PySide6.QtGui.QAction
    exportToDirectoryAction: PySide6.QtGui.QAction
    exportToFileAction: PySide6.QtGui.QAction
    exportMenu: QtWidgets.QMenu
    deleteAction: PySide6.QtGui.QAction
    separatorAction1: PySide6.QtGui.QAction
    separatorAction2: PySide6.QtGui.QAction
    separatorAction3: PySide6.QtGui.QAction
    separatorAction4: PySide6.QtGui.QAction
    separatorAction5: PySide6.QtGui.QAction
    separatorAction6: PySide6.QtGui.QAction
    separatorAction7: PySide6.QtGui.QAction
    libraryStateChanged: QtCore.Signal
    newLibraryCreated: QtCore.Signal
    librarySourceChanged: QtCore.Signal
    changeThumbnailFileRequested: QtCore.Signal
    changeThumbnailViewportRequested: QtCore.Signal
    def __init__(self, parent: PySide6.QtWidgets.QWidget, item_type: str) -> None: ...
    def cleanup(self) -> None:
        """This is called when the library interface is about to be
           destroyed."""
    def reset(self) -> None: ...
    def setDefaultLibraryName(self, name: str) -> None:
        """Sets default name of new libraries."""
    def setDefaultFolderName(self, name: str) -> None:
        """Sets default name of new folders."""
    def setEntryIconSize(self, width: int, height: int) -> None:
        """Set the entry icon size to the given width and height."""
    def setAutosave(self, save_format: str, path: str) -> None:
        """Set the location and format for autosaving this library."""
    def setAutosaveEnabled(self, enabled: bool) -> None:
        """Set whether library will be autosaved periodically."""
    def setInfoWindowEnabled(self, enabled: bool) -> None: ...
    def resetLibrarySource(self) -> None:
        """Sets source of pose library to None."""
    def isInitialized(self) -> bool:
        """Returns True if the library is either loaded from an existing source
           or the library is not currently empty."""
    def addItem(self, item: itemlibrary.Item[Any], row: int = -1, undo: bool = True, item_id: int | None = None, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex | None = None) -> None:
        """Adds item to currently selected/active folder."""
    def addFolder(self) -> None:
        """Adds folder of default name to currently selected/active folder."""
    def findIndex(self, root: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, item: itemlibrary.Item[Any]) -> PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex | None: ...
    def deleteItem(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, child: itemlibrary.Item[Any], item_id: int, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...
    def deleteFolder(self, folder_index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> None: ...
    def newLibrary(self) -> None:
        """Prompts user to create a new library."""
    def saveTo(self, save_format: str, path: str | None = None, copy: bool = False) -> bool:
        """Saves the library to the given format."""
    def save(self) -> bool:
        """Saves the current library to its source location.

        If the current library does not have a source then prompt the user
        for a save location.
        """
    def openLibrary(self, load_format: str, path: str | None = None) -> bool:
        """Open library of given format from given path."""
    def importLibrary(self, load_format: str, path: str | None = None) -> bool:
        """Open library of given format from given path."""
    def mergeLastAutosave(self) -> None:
        """Open library from the last autosave."""
    def promptToSave(self) -> None:
        """Prompt the user to save if there are unsaved changes.
            
        If there are no unsaved changes then do nothing.
        """
    def saveIfNeeded(self) -> bool:
        """Prompt the user to save the library if there are unsaved changes.

        Return True if the library was saved successfully or if there are no
        unsaved changes.  Return False otherwise.
        """
    def promptOverwrite(self, save_format: str, path: str) -> bool:
        """Prompt user to choose whether to overwrite an existing library,
           if necessary."""
    def ensureSourceValid(self, save_format: str, path: str) -> bool:
        """Ensure the given library save destination is valid.

        Return True if valid, return False otherwise.
        """
    def chooseLibrarySavePath(self, save_format: str, name: str | None, prompt_title: str, validate_source: bool = True, prompt_overwrite: bool = True) -> str | None:
        """Prompt user to choose the save location of their library with 
           the given save format."""

class _ViewportOptionsDialog(QtWidgets.QDialog):
    """Modal dialog containing options for capturing viewport animations."""
    frameRangeWidget: capturewidget.CaptureFrameRangeWidget
    includeAllObjectsBox: QtWidgets.QCheckBox
    def __init__(self) -> None: ...
    def startFrame(self) -> float:
        """Return the start frame set in the dialog."""
    def endFrame(self) -> float:
        """Return the end frame set in the dialog."""
    def includeAllObjects(self) -> bool:
        """Return True if the Include All Objects box is checked on and False
           otherwise."""

class NewLibraryDialog(QtCore.QObject):
    """Contains interface for initializing a new pose/clip library."""
    MIN_WIDTH: int
    def __init__(self, owner_browser: ItemBrowser, accepted_formats: Sequence[str], default_library_name: str) -> None: ...
    def cleanup(self) -> None: ...
    def exec_(self) -> int: ...
    def setCenter(self, global_pos: PySide6.QtCore.QPoint) -> None:
        """Center dialog relative to the given point."""
    def bringToFocus(self) -> None:
        """Opens dialog if not already open, then brings it into focus."""
    def reset(self) -> None:
        """Resets dialog to its default state."""
    def close(self) -> None: ...
    def saveName(self) -> str:
        """Return inputted name of new library."""
    def saveFormat(self) -> str:
        """Return selected format of new library."""
    def saveDest(self) -> str:
        """Returns selected save destination of new library."""

class ToolTip(QtWidgets.QWidget):
    """Custom tool tip used for displaying item information and 
       animated thumbnails."""
    titleWidget: QtWidgets.QLabel
    bodyWidget: QtWidgets.QLabel
    def __init__(self) -> None: ...
    def setTitle(self, title: str) -> None: ...
    def setText(self, text: str) -> None: ...
    def setPixmap(self, pixmap: PySide6.QtGui.QPixmap | None) -> None: ...
    def setMovie(self, movie: PySide6.QtGui.QMovie | None) -> None: ...
    def hide(self) -> None: ...
