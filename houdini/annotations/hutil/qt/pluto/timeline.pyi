import enum
from collections.abc import Iterable, Iterator, Sequence
from typing import NamedTuple

from PySide6 import QtCore, QtGui
from PySide6.QtCore import Qt

class CacheType(enum.IntEnum):
    memory = 0
    disk = 1

class KeyType(enum.IntEnum):
    normal = 0
    pending = 1
    partial = 2
    error = 3
    disabled = 4
    selected = 5
    selecting = 6
    overlay = 7
    multi_overlay = 8

class BookmarkHandle(enum.IntEnum):
    left = 0
    middle = 1
    right = 2
    none = 3

def clamp(v: float, min_v: float, max_v: float) -> float: ...
def drawTimelinePanel(painter: QtGui.QPainter, palette: QtGui.QPalette, rect: QtCore.QRectF, scale: float) -> None: ...
def drawAudio(
    painter: QtGui.QPainter,
    palette: QtGui.QPalette,
    timeline_rect: QtCore.QRectF,
    start: int,
    end: int,
    min_values: Sequence[float],
    max_values: Sequence[float],
    start_index: float,
    end_index: float,
    scale: float,
    *,
    level: float = ...,
    alpha: float = ...,
    compact: bool = ...,
) -> None: ...
def drawFrameRange(
    painter: QtGui.QPainter,
    rect: QtCore.QRectF,
    scale: float,
    frame_width: float,
    *,
    rounded: bool = ...,
    frame_lines: bool = ...,
) -> None: ...
def drawFrameRanges(
    painter: QtGui.QPainter,
    rect: QtCore.QRectF,
    scale: float,
    start: int,
    end: int,
    frames: Iterable[int],
    brush: QtGui.QBrush | Qt.BrushStyle | QtGui.QColor,
    *,
    rounded: bool = ...,
    frame_lines: bool = ...,
) -> None: ...
def drawFrameRects(
    painter: QtGui.QPainter,
    rect: QtCore.QRectF,
    scale: float,
    start: int,
    end: int,
    frames: Iterable[int],
    brush: QtGui.QBrush | Qt.BrushStyle | QtGui.QColor,
) -> None: ...
def cacheBarRect(timeline_rect: QtCore.QRectF, scale: float, compact: bool = ...) -> QtCore.QRectF: ...
def drawCached(
    painter: QtGui.QPainter,
    palette: QtGui.QPalette,
    timeline_rect: QtCore.QRectF,
    scale: float,
    start: int,
    end: int,
    cache_type: CacheType,
    frames: Iterable[int],
    is_disabled: bool,
    needs_reset: bool,
    is_playing: bool,
    compact: bool = ...,
) -> None: ...
def keyframeBarRect(timeline_rect: QtCore.QRectF, scale: float, compact: bool = ...) -> QtCore.QRectF: ...
def drawKeys(
    painter: QtGui.QPainter,
    palette: QtGui.QPalette,
    timeline_rect: QtCore.QRectF,
    scale: float,
    start: int,
    end: int,
    key_type: KeyType,
    frames: Iterable[int],
    is_dope_sheet: bool = ...,
    compact: bool = ...,
) -> None: ...
def bookmarkBarRect(timeline_rect: QtCore.QRectF, scale: float, compact: bool = ...) -> QtCore.QRectF: ...

class Bmark(NamedTuple):
    name: str
    start: int
    end: int
    color: QtGui.QColor

def drawBookmarks(
    painter: QtGui.QPainter,
    palette: QtGui.QPalette,
    timeline_rect: QtCore.QRectF,
    scale: float,
    start: int,
    end: int,
    bookmarks: Sequence[Bmark],
    bookmark_rects: Sequence[QtCore.QRect],
    compact: bool = ...,
    hovered_index: int = ...,
    handle: BookmarkHandle = ...,
    interactive: bool = ...,
) -> None: ...
def drawBookmark(
    painter: QtGui.QPainter,
    palette: QtGui.QPalette,
    scale: float,
    rect: QtCore.QRectF,
    name: str,
    color: QtGui.QColor,
    frame_width: float,
    baseline_offset: float,
    interactive: bool = ...,
    hovered: bool = ...,
    handle: BookmarkHandle = ...,
) -> None: ...
def drawPlayhead(
    painter: QtGui.QPainter,
    palette: QtGui.QPalette,
    timeline_rect: QtCore.QRectF,
    scale: float,
    start: int,
    end: int,
    frame: float,
    compact: bool = ...,
) -> None: ...
def selectionBarRect(timeline_rect: QtCore.QRectF, scale: float, compact: bool = ...) -> QtCore.QRectF: ...
def drawSelection(
    painter: QtGui.QPainter,
    palette: QtGui.QPalette,
    rect: QtCore.QRectF,
    select_rect: QtCore.QRectF,
    left_handle: QtCore.QRectF,
    right_handle: QtCore.QRectF,
    scale: float,
    select_start: int,
    select_end: int,
    frame_width: float,
    border_width: float = ...,
    compact: bool = ...,
) -> None: ...
def drawHover(
    painter: QtGui.QPainter,
    palette: QtGui.QPalette,
    timeline_rect: QtCore.QRectF,
    scale: float,
    frame_x: int,
    line_width: float = ...,
    compact: bool = ...,
) -> None: ...
def drawHoverFrame(
    painter: QtGui.QPainter,
    palette: QtGui.QPalette,
    timeline_rect: QtCore.QRectF,
    scale: float,
    start: int,
    end: int,
    frame: int,
    compact: bool = ...,
) -> None: ...

super_ticks: tuple[int, int, int, int, int, int, int, int, int, int, int, int]

def bigDivision(fps: int, initial_sep: float, minimum_sep: int) -> float: ...
def whichMultiple(inc: float) -> int: ...
def smallDivision(fps: int, frame_width: float, big_inc: float, min_width: float = ...) -> float: ...
def drawTicks(
    painter: QtGui.QPainter,
    palette: QtGui.QPalette,
    timeline_rect: QtCore.QRectF,
    scale: float,
    start: int,
    end: int,
    fps: int,
    pen_width: float = ...,
    compact: bool = ...,
) -> None: ...
def drawSheetSeparators(
    painter: QtGui.QPainter,
    palette: QtGui.QPalette,
    timeline_rect: QtCore.QRectF,
    scale: float,
    start: int,
    end: int,
    tick_positions: Iterable[int],
    pen_width: float = ...,
) -> None: ...
