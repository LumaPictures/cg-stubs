from apex.bookmarkmanager import BOOKMARK_END as BOOKMARK_END, BOOKMARK_LABEL as BOOKMARK_LABEL, BOOKMARK_START as BOOKMARK_START, BookmarkManager as BookmarkManager
from apex.utils import addAnimateStateUndo as addAnimateStateUndo
from collections.abc import Callable as Callable

class RangeChangedUndo:
    """
    An undo that is added to the undo stack whenever the range is changed.
    """
    manager: RangeBookmarkManager
    pre_range: tuple[int, int] | None
    post_range: tuple[int, int] | None
    def __init__(self, manager: RangeBookmarkManager, pre_range: tuple[int, int] | None, post_range: tuple[int, int] | None) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class RangeBookmarkManager(BookmarkManager):
    """
    A bookmark manager class for a frame range.
    """
    name: str
    frame_range: tuple[int, int] | None
    callback: Callable[[], object] | None
    def __init__(self, name: str) -> None: ...
    def activate(self, callback: Callable[[], object] | None = None) -> None: ...
    def deactivate(self) -> None: ...
    def setFrameRange(self, frame_range: tuple[int, int] | None) -> bool:
        """
        Sets the frame range for the manager
        """
    def getRangeFromData(self, bookmark_id: int) -> tuple[int, int]: ...
    def updateRange(self, post_range: tuple[int, int] | None) -> None: ...
    def onRangeChanged(self) -> None: ...
    def onBookmarkModifiedEvent(self, bookmark_id: int) -> bool:
        """
        An event callback that responds when a bookmark is modified by the
        bookmark editor.
        """
    def onBookmarkDeletedEvent(self, bookmark_id: int) -> bool:
        """
        An event callback that responds when a bookmark is delete.
        """
