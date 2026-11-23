import typing
from . import helpers as helpers, infowindow as infowindow, plglobals as plglobals
from collections.abc import Generator as Generator, Sequence
from houtypes import JSONValue
from hutil.Qt import QtCore
from poselib import itembrowser as itembrowser
from typing import Any, Generic, Literal, NotRequired, Self, TypedDict

from typing import TypeVar
from typing import TypeVar
_D_co = TypeVar('_D_co', covariant=True)
class _ItemJson(TypedDict):
    name: str
    type: str
    itemid: NotRequired[int | None]
    data: Any
    datatype: str | None
    datapath: str | None
    image: str | bytes | None
    imagetype: str | None
    imagepath: str | None
    metadata: dict[str, JSONValue]
    parent_tmp_id: NotRequired[int | None]
    children: NotRequired[list['_ItemJson']]
    full_data_path: NotRequired[str]
    full_image_data_path: NotRequired[str]

NAME: int
TYPE: int
DATA: int
DATA_TYPE: int
DATA_PATH: int
IMAGE: int
IMAGE_TYPE: int
IMAGE_PATH: int
METADATA: int
PATH: int
ICON: int
PIXMAP: int
MOVIE: int
TOOL_TIP: int
INFO_JSON: int
HOVERED: int
EXPANDED: int
VIEW_MODE: int
SHOW_ITEMS: int
ZOOM_LEVEL: int
THUMBNAIL_SIZE_HINT: int
CELL_SIZE_HINT: int
SAVED_SIZE: int
ZOOM_IN: int
ZOOM_OUT: int
ZOOM_RESET: int
CHANGED_ROLE: int
OLD_NAME: int
ROOT: str
LIBRARY_DIRECTORY: str
LIBRARY_HDA_NODE: str
LIBRARY_HDA_FILE: str
LIBRARY_FILE: str
ROW_HEIGHT: int
LABEL_HEIGHT: int
TEXT_MARGIN: int
GRID_MARGIN: int
GRID_BORDER: int
GRID_THUMBNAIL_WIDTH: int
GRID_THUMBNAIL_HEIGHT: int
ROW_PADDING: int
ROW_THUMBNAIL_WIDTH: int
ROW_THUMBNAIL_HEIGHT: int
ZOOM_MULTIPLIERS: tuple[float, ...]
MIN_ZOOM: float
MAX_ZOOM: float
DEFAULT_ZOOM_INDEX: int
LIST_VIEW: int
GRID_VIEW: int
TYPE_FOLDER: str
TYPE_ITEM: str
NUM_USER_ROLES: int
JSON_NAME: Literal['name']
JSON_TYPE: Literal['type']
JSON_DATA: Literal['data']
JSON_DATA_TYPE: Literal['datatype']
JSON_DATA_PATH: Literal['datapath']
JSON_IMAGE: Literal['image']
JSON_IMAGE_TYPE: Literal['imagetype']
JSON_IMAGE_PATH: Literal['imagepath']
JSON_METADATA: Literal['metadata']
JSON_CHILDREN: Literal['children']
JSON_VIEW_MODE: Literal['viewmode']
JSON_ZOOM_LEVEL: Literal['zoomlevel']
JSON_SHOW_ITEMS: Literal['showitems']
JSON_ITEM_ID: Literal['itemid']
JSON_LIB_NAME: Literal['name']
JSON_LIB_VERSION: Literal['hversion']
JSON_LIB_DATE: Literal['save_date']
JSON_LIB_TIME: Literal['save_time']
JSON_LIB_ITEMS: Literal['contents']
JSON_PARENT_ID: Literal['parent_tmp_id']
JSON_FULL_DATA_PATH: Literal['full_data_path']
JSON_FULL_IMAGE_DATA_PATH: Literal['full_image_data_path']

class Item(Generic[_D_co]):
    """Represents a single entry in the item library model.

    Can either be a Folder or an Item.
    """
    isRootFolder: bool
    TOOL_TIP_ICON_WIDTH: int
    TOOL_TIP_ICON_HEIGHT: int
    showItems: bool
    zoomLevel: int
    viewMode: int
    def __init__(self, parent: Item[Any] | None, name: str | None, item_type: str | None, data: _D_co | None, data_type: str | None, data_path: str | None, image_data: QtCore.QByteArray | None, image_type: str | None, image_path: str | None, item_id: int | None = None, full_data_path: str | None = None, **metadata: JSONValue) -> None: ...
    def copyForExport(self) -> Item[_D_co | JSONValue | bytes]:
        """
        Returns a copy of this item to use when exporting.
        """
    def cleanup(self) -> None: ...
    @classmethod
    def placeholder(cls, parent: Item[Any] | None) -> Self: ...
    @classmethod
    def folder(cls, name: str) -> Self: ...
    @classmethod
    def resetViewSettings(cls) -> None:
        """Resets view settings to default."""
    def setSaved(self, saved: bool) -> None: ...
    def hasUnsavedChanges(self) -> bool: ...
    def dataFile(self, item_name: str | None = None) -> str:
        """Returns the file name of the data file."""
    def imageFile(self, item_name: str | None = None) -> str:
        """Returns the file name of the image file."""
    def saveData(self, path: str) -> str | None:
        """Save item data file to the given path."""
    def saveImage(self, path: str) -> str | None:
        """Save item image file to the given path."""
    def serializeData(self, to_string: bool = False) -> _D_co | JSONValue | bytes:
        """Return a JSON serializable representation of this item's data."""
    def serializeImage(self) -> bytes | None:
        """Return a JSON serializable representation of this item's image."""
    def serializeMetadata(self) -> dict[str, JSONValue]:
        """Return a JSON serializable representation of this item's metadata."""
    @typing.overload
    def toJSON(self, recursive: Literal[False], external_references: bool, store_parent_id: bool = ..., separate_data_section: Literal[False] = ..., ignore_data_for_saved_items: bool = ..., save_item_id: bool = ...) -> _ItemJson: ...
    @typing.overload
    def toJSON(self, recursive: Literal[False], external_references: bool, store_parent_id: bool = ..., *, separate_data_section: Literal[True], ignore_data_for_saved_items: bool = ..., save_item_id: bool = ...) -> tuple[_ItemJson, Any]: ...
    @typing.overload
    def toJSON(self, recursive: Literal[True], external_references: bool, store_parent_id: bool = ..., separate_data_section: bool = ..., ignore_data_for_saved_items: bool = ..., save_item_id: bool = ...) -> _ItemJson: ...
    @typing.overload
    def toJSON(self, recursive: bool, external_references: bool, store_parent_id: bool = ..., separate_data_section: bool = ..., ignore_data_for_saved_items: bool = ..., save_item_id: bool = ...) -> _ItemJson | tuple[_ItemJson, Any]: ...
    def getId(self) -> int:
        """ Returns the id for this item as a long. """
    def hasData(self) -> bool: ...
    def hasImage(self) -> bool: ...
    def getData(self) -> _D_co | JSONValue | bytes:
        """
        All read access to self._data should use this method to
        ensure data is lazy-loaded.
        """
    def isFolder(self) -> bool: ...
    def getZoomMultiplier(self) -> float: ...
    def getViewMode(self) -> int: ...
    def path(self, pretty: bool = False) -> str: ...
    def parent(self) -> Item[Any] | None: ...
    def child(self, row: int) -> Item[Any] | None: ...
    def childItem(self, row: int) -> Item[Any] | None: ...
    def childFolder(self, row: int) -> Item[Any] | None: ...
    def childNumberByName(self, name: str) -> int: ...
    def childCount(self) -> int: ...
    def childItemCount(self) -> int: ...
    def childFolderCount(self) -> int: ...
    def childNumber(self) -> int: ...
    def childItemNumber(self) -> int: ...
    def childFolderNumber(self) -> int: ...
    def data(self, role: int) -> Any: ...
    def setId(self, id_val: int) -> None:
        """A hack to force the ID from this class. Don't use this unless
           it's necessary."""
    def setParent(self, parent_item: Item[Any] | None, keep_item_name: bool = False) -> None:
        """
        Sets this item's parent to the given parent item.
        :param parent_item: The new parent item for this item
        :param keep_item_name: Whether this items should keep its name even
            if the parent already contains an item with the same name.
            This should only be used with items being moved to the same parent
            folder.
        :return:
        """
    def setData(self, value: Any, role: int) -> bool: ...
    def actionRequested(self, action: int) -> bool:
        """Perform requested action on this item.

        Return True if action succeeded. Return False if action failed, or
        specified action does not exist.
        """
    def setChild(self, position: int, child_item: Item[Any], keep_item_name: bool = False) -> bool:
        """
        Sets the given item as a child of this item at
        the given position.

        :param position: Position at which the child should be added.
        :param child_item: The child item to add.
        :param keep_item_name: Whether the added child should keep its
            name even if a duplicate name exists.
            This should really only be used with items that are being moved
            into the same parent folder.
        :return:
        """
    def appendChild(self, child_item: Item[Any]) -> bool: ...
    def insertChildren(self, position: int, rows: int) -> bool: ...
    def removeChildren(self, position: int, count: int) -> bool: ...
    def swapChildren(self, other_item: Item[Any]) -> None:
        """Swaps self's children with children of other_item."""

class IdentityProxyModel(QtCore.QAbstractProxyModel):
    """Proxy model which does not modify data from source model.

    Note QIdentityProxyModel exists in Qt, but is not implemented in PySide.
    """
    def __init__(self, parent: QtCore.QObject | None, model: ItemModel) -> None: ...
    def cleanup(self) -> None: ...
    def reset(self) -> None: ...
    def setSourceModel(self, model: QtCore.QAbstractItemModel) -> None: ...
    def mapFromSource(self, source_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, filtered: bool = True) -> QtCore.QModelIndex: ...
    def mapToSource(self, proxy_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex: ...
    def index(self, row: int, column: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> QtCore.QModelIndex: ...
    def parent(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex: ...
    def hasChildren(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> bool: ...
    def rowCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> int: ...
    def columnCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> int: ...
    def data(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, role: int) -> Any: ...
    def setData(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, value: Any, role: int = ...) -> bool: ...
    def flags(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.Qt.ItemFlag: ...
    def dropMimeData(self, data: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool: ...
    def removeRows(self, position: int, rows: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> bool: ...
    def getItem(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> Item[Any]: ...
    def assertSourceIndex(self, source_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...
    def assertProxyIndex(self, proxy_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...
    def actionRequested(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, action: int) -> bool: ...

class GridModel(IdentityProxyModel):
    """Proxy model which presents items of a tree model (excluding folders)
       as a grid."""
    columns: int
    def __init__(self, parent: QtCore.QObject | None, model: ItemModel) -> None: ...
    def mapFromSource(self, source_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, filtered: bool = True) -> QtCore.QModelIndex: ...
    def mapToSource(self, proxy_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex: ...
    def index(self, row: int, column: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> QtCore.QModelIndex: ...
    def rowCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> int: ...
    def columnCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> int: ...

class TreeModel(QtCore.QSortFilterProxyModel):
    """Model that can optionally filter out (leaf) items."""
    showOnlyFolders: bool
    def __init__(self, parent: QtCore.QObject | None, model: ItemModel) -> None: ...
    def setShowItems(self, show: bool) -> None:
        """Set the filtering so that only folders are shown or both folders and
           items are shown."""
    def showItems(self) -> bool: ...
    def assertSourceIndex(self, source_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None:
        """Assert that the specified source index is valid and belongs to this
           proxy model's source model."""
    def assertProxyIndex(self, proxy_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None:
        """Assert that the specified proxy index is valid and belongs to this
           proxy model."""
    def filterAcceptsRow(self, source_row: int, source_parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool:
        """Overrides QSortFilterProxyModel::filterAcceptsRow."""

class ItemModel(QtCore.QAbstractItemModel):
    """Generic tree-structure model.
    
    Includes functionality for saving and loading this model to and from 
    HDAs and disk.
    """
    invisibleRootItem: Item[Any]
    rootItem: Item[Any]
    def __init__(self, parent: itembrowser.ItemBrowser, item_type: str, hda_section_name: str) -> None: ...
    def cleanup(self) -> None: ...
    def reset(self) -> None: ...
    def clear(self) -> None: ...
    def resetItemEditTracking(self) -> None:
        """
        Resets all variables associated with tracking item changes
        (e.g. deletion, renaming, etc.).
        """
    def setupForNewLibrary(self, library_name: str, save_path: str, save_format: str) -> None: ...
    def itemFromJSON(self, json: _ItemJson, recursive: bool = False) -> Item[Any]: ...
    def loadJSON(self, json: _ItemJson, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ..., force_load_data: bool = False, ignore_view_settings: bool = False) -> bool:
        """
        Creates and adds Item objects from the given JSON dictionary as
        children of the given parent index.
        :param json: The json dictionary to load from
        :param parent: The parent of the newly loaded items
        :param force_load_data: If True, forces all data to be loaded on
            item creation rather than being lazy loaded.
        :param ignore_view_settings: If True, ignores loading of view settings
            from the root folder (if any) in the given json.
        """
    def mimeTypes(self) -> list[str]: ...
    def mimeData(self, indexes: Sequence[QtCore.QModelIndex]) -> QtCore.QMimeData: ...
    def canDropMimeData(self, data: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool: ...
    def supportedDropActions(self) -> QtCore.Qt.DropAction: ...
    def dropMimeData(self, data: QtCore.QMimeData | str, action: QtCore.Qt.DropAction, row: int, column: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex, force_row: bool = False) -> bool: ...
    def findIndex(self, root: QtCore.QModelIndex | QtCore.QPersistentModelIndex, item_id: int) -> QtCore.QModelIndex | QtCore.QPersistentModelIndex | None: ...
    def insertRows(self, position: int, rows: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> bool: ...
    def removeRows(self, position: int, rows: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> bool: ...
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int) -> None: ...
    def setData(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, value: Any, role: int = ...) -> bool: ...
    def data(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, role: int) -> Any: ...
    def flags(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.Qt.ItemFlag: ...
    def index(self, row: int, column: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> QtCore.QModelIndex: ...
    def parent(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex: ...
    def rowCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> int: ...
    def columnCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> int: ...
    def isEmpty(self) -> bool:
        """Returns True if there are no items or subdirectories in this
           library."""
    def actionRequested(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, action: int) -> bool: ...
    def addItem(self, item: Item[Any], parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex, row: int = -1, keep_item_name: bool = False) -> QtCore.QModelIndex:
        """
        Adds the given item at the given `row` of the `parent`.
        :param item: The Item to add
        :param parent: The index of the parent
        :param row: The row to add the item at. -1 means at the end
            of the existing items under `parent`
        :param keep_item_name: Whether the added item should keep its name if
            there is a conflict.
        """
    def hasUnsavedChanges(self) -> bool: ...
    def setSaved(self, saved: bool) -> None: ...
    def exportTo(self, save_format: str, indexes: Sequence[QtCore.QModelIndex | QtCore.QPersistentModelIndex], name: str, path: str) -> bool | None:
        """Exports object at given path as a standalone JSON file.

        Return True if save was successful.  Return False otherwise.
        """
    def saveTo(self, save_format: str, name: str, path: str, copy: bool = False, item: Item[Any] | None = None) -> bool | None:
        """Save library to given path as given format.

        :param name: name of the library to save.
        :param copy: True means what's being saved should be a copy and not an
            original. False means what's being saved should be the original.
            This is used for temp saves.

        Return True if save was successful, or False otherwise.
        """
    def saveItem(self, path: str, copy: bool = False, item: Item[Any] | None = None) -> tuple[_ItemJson | None, list[str]]:
        """Saves given item or folder to a directory recursively.

        Return 2-tuple containing a JSON representation of saved folder and a list
        of files which failed to save.
        """
    def loadFrom(self, load_format: str, path: str, importing: bool = False) -> str | None:
        """Load library of given format and path.

        Return name of loaded library if load was successful, or None otherwise.
        """
    def nodeHasLibrary(self, path: str) -> bool:
        """Return True if the specified node has an item library stored in its 
           HDA definition and False otherwise."""
    def fileHasLibrary(self, path: str) -> bool:
        """Return True if the specified file has an item library stored in its 
           HDA definition and False otherwise."""
    @typing.overload
    def loadImage(self, image_file_path: str, image_type: str | None = ..., serialize: Literal[True] = ...) -> tuple[str, str | bytes] | tuple[None, None]: ...
    @typing.overload
    def loadImage(self, image_file_path: str, image_type: str | None = ..., *, serialize: Literal[False]) -> tuple[QtCore.QByteArray, str | bytes] | tuple[None, None]: ...
    @typing.overload
    def loadImage(self, image_file_path: str, image_type: str | None, serialize: Literal[False]) -> tuple[QtCore.QByteArray, str | bytes] | tuple[None, None]: ...
    @typing.overload
    def loadImage(self, image_file_path: str, image_type: str | None = ..., serialize: bool = ...) -> tuple[str | QtCore.QByteArray, str | bytes] | tuple[None, None]: ...
    def getItem(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> Item[Any]: ...
    def joinPaths(self, path1: str, path2: str) -> str:
        """Joins two library paths."""
