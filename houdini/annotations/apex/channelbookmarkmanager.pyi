from collections.abc import Callable, Sequence
from typing import TypedDict

import hou
from apex.bookmarkmanager import BookmarkChangedEvent, BookmarkManager, _BookmarkData

# What ChannelBookmarkManager passes its callback: empty when the channels change.
class _ChannelBookmarkChangedKwargs(TypedDict, total=False):
    event: BookmarkChangedEvent
    data: _BookmarkData

# Bookmark data that bindGeometryChannels() merges into each channel primitive's bookmarks.
class _PrimBookmarkData(TypedDict, total=False):
    label: str
    start: int
    end: int
    color: hou.Vector3
    dirty: bool
    name: str | None
    path: str

class ChannelsChangedUndo:
    manager: "ChannelBookmarkManager"
    prev_channels: hou.Geometry
    channels: hou.Geometry
    def __init__(self, manager: "ChannelBookmarkManager", prev_channels: hou.Geometry, channels: hou.Geometry) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class ChannelBookmarkManager(BookmarkManager):
    geo: hou.Geometry | None
    prev_data_ids: tuple[int, ...] | None
    prims: Sequence[int]
    prim_data: Sequence[_PrimBookmarkData]
    scope_channels: bool
    callback: Callable[[_ChannelBookmarkChangedKwargs], object] | None
    def __init__(self, scope_channels: bool = ...) -> None: ...
    def activate(self, callback: Callable[[_ChannelBookmarkChangedKwargs], object] | None = ...) -> None: ...
    def deactivate(self) -> None: ...
    def bindGeometryChannels(self, geo: hou.Geometry | None, prims: str | Sequence[int] | None = ..., prim_data: Sequence[_PrimBookmarkData] = ...) -> None: ...
    def syncBookmarks(self, force: bool = ...) -> bool: ...
    def createBookmarks(self) -> None: ...
    def _updateChannel(self, old_data: _BookmarkData) -> None: ...
    def onChannelsChanged(self) -> None: ...
    def primBookmarks(self, prim_idx: int | None) -> list[hou.Bookmark]: ...
    def onBookmarkModifiedEvent(self, bookmark_id: int) -> bool | None: ...
    def onBookmarkDeletedEvent(self, bookmark_id: int) -> bool: ...
