import apex
import apex.stateutils_2 as asu
import hou
import typing
from apex.bookmarkmanager import _BookmarkMetadata, _MethodDecorator
from apex.utils import addAnimateStateUndo as addAnimateStateUndo
from collections.abc import Callable as Callable
from enum import Enum as Enum
from functools import wraps as wraps
from typing import ClassVar, Final, Literal, Protocol

from typing import TypeAlias
from typing import TypeAlias
_DataId: TypeAlias = int | str
class _AnimateState(asu._AnimateState, Protocol):
    """The Animate viewer state (`viewer_states/apexanimate.py`): this module uses only the members `apex.stateutils_2._AnimateState` declares."""

BOOKMARK_LABEL: Final[str]
BOOKMARK_START: Final[str]
BOOKMARK_END: Final[str]
BOOKMARK_COLOR: Final[str]

class UpdateBookmarkUndo:
    manager: SceneBookmarkManager
    bookmark_id: int
    prev_metadata: _BookmarkMetadata | None
    metadata: _BookmarkMetadata
    def __init__(self, manager: SceneBookmarkManager, bookmark_id: int, prev_metadata: _BookmarkMetadata | None, metadata: _BookmarkMetadata) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class DeleteBookmarkUndo:
    manager: SceneBookmarkManager
    entry: apex.Dict | None
    layer: str
    data_id: int | None
    def __init__(self, manager: SceneBookmarkManager, entry: apex.Dict | None, layer: str) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class SceneBookmarkManager:
    is_active: bool
    type_name: str
    auto_select: bool
    show_all_bookmarks: bool
    prev_metadata: _BookmarkMetadata | None
    copied_transient_data: list[apex.Dict]
    follow_colors: dict[str, hou.Color]
    _bookmarkid_to_dataid: dict[int, _DataId]
    bookmarkChangedEventBlocker: ClassVar[_MethodDecorator]
    def __init__(self, state: _AnimateState, type_name: str) -> None: ...
    @property
    def state(self) -> _AnimateState | None: ...
    @property
    def scene(self) -> apex.Scene: ...
    def onActivate(self) -> None: ...
    def onDeactivate(self) -> None: ...
    def addCallbacks(self) -> None: ...
    def removeCallbacks(self) -> None: ...
    @property
    def bookmarks(self) -> list[hou.Bookmark]: ...
    def bookmark(self, bookmark_id: int) -> hou.Bookmark | None: ...
    def findBookmarkID(self, target_id: _DataId) -> int | None: ...
    def findBookmarks(self, frame: float) -> list[hou.Bookmark]: ...
    @typing.overload
    def transientData(self, include_path: Literal[False] = ..., layer: str | None = ...) -> apex.Dict | None: ...
    @typing.overload
    def transientData(self, include_path: Literal[True], layer: str | None = ...) -> tuple[str | None, apex.Dict | None]: ...
    @typing.overload
    def transientData(self, include_path: bool = ..., layer: str | None = ...) -> apex.Dict | None | tuple[str | None, apex.Dict | None]: ...
    def findTransientEntries(self, frame: float, visible: bool = False, layer: str | None = None) -> dict[_DataId, apex.Dict]: ...
    def bookmarkMetaDataID(self, bookmark: int | hou.Bookmark) -> _DataId | None: ...
    def setBookmarkMetaDataID(self, bookmark: int | hou.Bookmark, data_id: _DataId | None) -> None: ...
    def bookmarkMetaData(self, bookmark: hou.Bookmark) -> _BookmarkMetadata:
        """
        Collect the data relevant for bookmarks in a dictionary.
        """
    @bookmarkChangedEventBlocker
    def setBookmarkMetaData(self, bookmark_id: int, metadata: _BookmarkMetadata) -> hou.Bookmark | None:
        """
        Writes data relavent for bookmarks from a dictionary.
        """
    def onBookmarkInteractionStartedEvent(self, bookmark_id: int) -> bool:
        """
        An event callback that responds when interaction with a bookmark starts.
        This function is used to backup all of the relavent metadata for the
        bookmark so that an undo block can be added.
        """
    def onBookmarkInteractionFinishedEvent(self, bookmark_id: int) -> bool:
        """
        An event callback that responds when interaction with a bookmark finises.
        This function is used to update the transient entry in the scene that
        corresponds to this bookmark.
        """
    def onBookmarkModifiedEvent(self, bookmark_id: int) -> bool:
        """
        An event callback that responds when a bookmark is modified by the
        bookmark editor.
        """
    @bookmarkChangedEventBlocker
    def onBookmarkDeletedEvent(self, bookmark_id: int) -> bool:
        """
        An event callback that responds when a bookmark is deleted.
        This function is used to remove the transient entry in the scene that
        corresponds to this bookmark.
        """
    @bookmarkChangedEventBlocker
    def updateBookmarks(self) -> None: ...
    @bookmarkChangedEventBlocker
    def createBookmark(self, entry: apex.Dict, layer: str | None) -> int: ...
    @bookmarkChangedEventBlocker
    def addBookmark(self, data_id: _DataId) -> hou.Bookmark | None:
        """
        Adds a new bookmark linked to transient data in the scene
        """
    @bookmarkChangedEventBlocker
    def addBookmarks(self, filter_fn: Callable[[apex.Dict], object] | None = None) -> None:
        """
        Adds bookmarks for each transient data entry that matches the
        filter function.
        """
    @bookmarkChangedEventBlocker
    def clearBookmarks(self) -> None:
        """
        Removes a given selection fo follow bookmarks.
        """
    @bookmarkChangedEventBlocker
    def removeBookmark(self, data_id: _DataId, layer: str | None) -> None: ...
    def copyBookmarks(self) -> None:
        """
        Copy the bookmarks of the current layer
        """
    def pasteBookmarks(self) -> None:
        """
        Paste the bookmarks onto the the current layer
        """
    def getBookmarkColor(self, key: str) -> hou.Color: ...
    def setBookmarkColor(self, key: str, color: hou.Color) -> None: ...
    def generateRandomBookmarkColor(self) -> hou.Color: ...
    def findBookmarkByName(self, name: str) -> hou.Bookmark | None: ...
    def hideAllBookmarks(self) -> None: ...
