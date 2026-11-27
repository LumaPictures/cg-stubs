import hou
from apex.bookmarkmanager import BOOKMARK_COLOR as BOOKMARK_COLOR, BOOKMARK_END as BOOKMARK_END, BOOKMARK_LABEL as BOOKMARK_LABEL, BOOKMARK_START as BOOKMARK_START, BookmarkChangedEvent as BookmarkChangedEvent, BookmarkManager as BookmarkManager, _BookmarkData
from apex.utils import addAnimateStateUndo as addAnimateStateUndo
from collections.abc import Callable as Callable, Sequence
from typing import TypedDict

class _ChannelBookmarkChangedKwargs(TypedDict, total=False):
    event: BookmarkChangedEvent
    data: _BookmarkData

class _PrimBookmarkData(TypedDict, total=False):
    label: str
    start: int
    end: int
    color: hou.Vector3
    dirty: bool
    name: str | None
    path: str

class ChannelsChangedUndo:
    """
    An undo that is added to the undo stack whenever the channels in the
    bookmark manager are updated
    """
    manager: ChannelBookmarkManager
    prev_channels: hou.Geometry
    channels: hou.Geometry
    def __init__(self, manager: ChannelBookmarkManager, prev_channels: hou.Geometry, channels: hou.Geometry) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class ChannelBookmarkManager(BookmarkManager):
    """
    A bookmark manager class that associates bookmarks with periods of channel
    primitives that are greater than 0.
    """
    geo: hou.Geometry | None
    prev_data_ids: tuple[int, ...] | None
    prims: Sequence[int]
    prim_data: Sequence[_PrimBookmarkData]
    scope_channels: bool
    callback: Callable[[_ChannelBookmarkChangedKwargs], object] | None
    def __init__(self, scope_channels: bool = False) -> None: ...
    def activate(self, callback: Callable[[_ChannelBookmarkChangedKwargs], object] | None = None) -> None: ...
    def deactivate(self) -> None: ...
    def bindGeometryChannels(self, geo: hou.Geometry | None, prims: str | Sequence[int] | None = None, prim_data: Sequence[_PrimBookmarkData] = ...) -> None:
        """
        Binds a set of geometry channel primitives to the bookmark manager
        """
    def syncBookmarks(self, force: bool = False) -> bool:
        """
        Checks to see if the bookmarks need updating and updates them if
        necessary.
        """
    def createBookmarks(self) -> None:
        """
        Creates bookmarks to track the periods during which the listed channels
        are greater than 0.
        """
    def _updateChannel(self, old_data: _BookmarkData) -> None:
        """
        Updates the channel primitive to key on the channel during the
        tracked regions.
        This clears all keys within the regions
        """
    def onChannelsChanged(self) -> None: ...
    def primBookmarks(self, prim_idx: int | None) -> list[hou.Bookmark]:
        """
        Return all bookmarks with the matching primitive
        """
    def onBookmarkModifiedEvent(self, bookmark_id: int) -> bool | None:
        """
        An event callback that responds when a bookmark is modified by the
        bookmark editor.
        """
    def onBookmarkDeletedEvent(self, bookmark_id: int) -> bool:
        """
        An event callback that responds when a bookmark is deleted.
        This function is used to remove the transient entry in the scene that
        corresponds to this bookmark.
        """
