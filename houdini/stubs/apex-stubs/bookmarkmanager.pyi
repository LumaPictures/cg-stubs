import hou
import typing
from apex.utils import addAnimateStateUndo as addAnimateStateUndo
from collections.abc import Callable as Callable, Mapping as Mapping, Sequence as Sequence
from enum import Enum
from typing import ClassVar, Final, Literal, Protocol, Required, TypedDict

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
class _MethodDecorator(Protocol):
    def __call__(self, func: Callable[_P, _R], /) -> Callable[_P, _R]: ...

class _BookmarkMetadata(TypedDict, total=False):
    label: str
    start: int
    end: int
    color: hou.Vector3

class _BookmarkData(TypedDict, total=False):
    label: Required[str]
    start: Required[int]
    end: Required[int]
    color: hou.Vector3
    dirty: bool
    prim: int
    name: str | None
    path: str

BOOKMARK_LABEL: Final[str]
BOOKMARK_START: Final[str]
BOOKMARK_END: Final[str]
BOOKMARK_COLOR: Final[str]
BOOKMARK_METADATA_KEYS: tuple[Literal['label'], Literal['start'], Literal['end'], Literal['color']]
BOOKMARK_DIRTY: Final[str]
BOOKMARK_COLOR_DEFAULT: hou.Vector3

class BookmarkChangedEvent(Enum):
    Start = 0
    End = 1
    Label = 2
    Color = 3
    Deleted = 4

class UpdateBookmarkUndo:
    manager: BookmarkManager
    data_id: int | None
    prev_metadata: _BookmarkMetadata | None
    metadata: _BookmarkMetadata
    def __init__(self, manager: BookmarkManager, data_id: int | None, prev_metadata: _BookmarkMetadata | None, metadata: _BookmarkMetadata) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class DeleteBookmarkUndo:
    manager: BookmarkManager
    data: _BookmarkData
    data_id: int | None
    def __init__(self, manager: BookmarkManager, data: _BookmarkData) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class BookmarkManager:
    _bookmark_data: dict[int, _BookmarkData]
    bookmarkChangedEventBlocker: ClassVar[_MethodDecorator]
    def __init__(self) -> None: ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def addCallbacks(self) -> None: ...
    def removeCallbacks(self) -> None: ...
    @property
    def bookmarks(self) -> list[hou.Bookmark]: ...
    def bookmark(self, bookmark_id: int) -> hou.Bookmark | None: ...
    def findBookmarks(self, frame: float) -> list[hou.Bookmark]: ...
    def getDataId(self, bookmark: int | hou.Bookmark) -> int | None:
        """
        Returns the data id corresponding to a bookmark id
        """
    def getBookmarkId(self, data_id: int | None) -> int | None:
        """
        Returns the bookmark id corresponding to a dataid
        """
    @typing.overload
    def bookmarkData(self, bookmark: int | hou.Bookmark, metadata_only: Literal[False] = ...) -> _BookmarkData | None: ...
    @typing.overload
    def bookmarkData(self, bookmark: int | hou.Bookmark, metadata_only: Literal[True]) -> _BookmarkMetadata | None: ...
    @typing.overload
    def bookmarkData(self, bookmark: int | hou.Bookmark, metadata_only: bool = ...) -> _BookmarkData | _BookmarkMetadata | None: ...
    def updateBookmarkData(self, bookmark: int | hou.Bookmark, data: _BookmarkMetadata) -> bool:
        """
        Updates stashed bookmark data from a dictionary
        """
    def deleteBookmarkData(self, bookmark: int | hou.Bookmark) -> bool:
        """
        Deletes bookmark data from the manager.
        """
    def bookmarkMetaData(self, bookmark: hou.Bookmark) -> _BookmarkMetadata:
        """
        Collect the data relevant for bookmarks in a dictionary.
        """
    @bookmarkChangedEventBlocker
    def setBookmarkMetaData(self, bookmark_id: int | hou.Bookmark | None, metadata: _BookmarkMetadata) -> hou.Bookmark | None:
        """
        Writes data relavent for bookmarks from a dictionary.
        """
    def onBookmarkInteractionStartedEvent(self, bookmark_id: int) -> bool:
        """
        An event callback that responds when interaction with a bookmark starts.
        """
    def onBookmarkInteractionFinishedEvent(self, bookmark_id: int) -> bool | None:
        """
        An event callback that responds when interaction with a bookmark finises.
        """
    def onBookmarkModifiedEvent(self, bookmark_id: int) -> bool | None:
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
    def getUniqueDataId(self) -> int:
        """
        Gets a unique data id for the bookmark data
        """
    @bookmarkChangedEventBlocker
    def createBookmark(self, data: _BookmarkData) -> int | None:
        """
        Creates a new bookmark given a bookmark data dictionary
        """
    @bookmarkChangedEventBlocker
    def addBookmark(self, data_id: int, data: _BookmarkData) -> hou.Bookmark:
        """
        Adds a new bookmark
        """
    @bookmarkChangedEventBlocker
    def removeBookmark(self, data_id: int) -> bool:
        """
        Deletes a tracked bookmark
        """
    @bookmarkChangedEventBlocker
    def clearBookmarks(self) -> None:
        """
        Clears the bookmarks
        """
    def setBookmarkColorByName(self, name: str | None, color: hou.Vector3) -> None: ...
    def getBookmarkColorByName(self, name: str | None) -> hou.Vector3: ...
    def generateRandomBookmarkColor(self) -> hou.Vector3: ...
