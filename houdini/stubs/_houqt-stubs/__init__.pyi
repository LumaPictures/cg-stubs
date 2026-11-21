# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Sequence
from typing import Never, TypeAlias, Unpack, overload

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import shiboken6
import typing

# The hou.qt.NLE_* classes these methods take and return live in _houqt, but report their
# module as hou.qt, so no stub declares them; their common base stands in for them.
_NLEObject: TypeAlias = shiboken6.Shiboken.Object
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import Shiboken
import enum
import functools
from _typeshed import Incomplete
from typing import Callable, ClassVar

class NLE_AnimValue(Shiboken.Object):
    myFrames: list[float]
    myTimes: list[float]
    myValue: float
    myValueState: NLE_AnimValueState
    myValues: list[float]
    def __init__(self) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addKey(self, *args: Unpack[tuple[float]], **kwargs: Never) -> None: ...
    def animValueMapper(self, *args: Never, **kwargs: Never) -> _NLEObject | None: ...
    def bumpChangeCount(self, *args: Never, **kwargs: Never) -> None: ...
    def copyFrom(self, *args: Unpack[tuple[NLE_AnimValue]], **kwargs: Never) -> None: ...
    def evalValue(self, *args: Unpack[tuple[float]], **kwargs: Never) -> float: ...
    def evalValues(self, *args: Unpack[tuple[Sequence[float]]], **kwargs: Never) -> list[float]: ...
    def findFrame(self, *args: Unpack[tuple[float]], **kwargs: Never) -> int: ...
    def findTime(self, *args: Unpack[tuple[float]], **kwargs: Never) -> int: ...
    def getChangeCount(self, *args: Never, **kwargs: Never) -> int: ...
    def getFps(self, *args: Never, **kwargs: Never) -> float: ...
    def getKeyFrames(self, *args: Never, **kwargs: Never) -> list[float]: ...
    def getKeyTimes(self, *args: Never, **kwargs: Never) -> list[float]: ...
    def getKeyValues(self, *args: Never, **kwargs: Never) -> list[float]: ...
    def getValue(self, *args: Never, **kwargs: Never) -> float: ...
    def getValueState(self, *args: Never, **kwargs: Never) -> NLE_AnimValueState: ...
    def isUndoPushed(self, *args: Never, **kwargs: Never) -> bool: ...
    def moveKeys(self, *args: Unpack[tuple[Sequence[float], Sequence[float], Sequence[float]]], **kwargs: Never) -> bool: ...
    def popUndo(self, *args: Never, **kwargs: Never) -> None: ...
    def pushUndo(self, *args: Unpack[tuple[str]], **kwargs: Never) -> None: ...
    def removeKeys(self, *args: Unpack[tuple[Sequence[float]]], **kwargs: Never) -> None: ...
    def saveUndoState(self, *args: Never, **kwargs: Never) -> None: ...
    def setAnimValueMapper(self, *args: Unpack[tuple[_NLEObject | None]], **kwargs: Never) -> None: ...
    def setKey(self, *args: Unpack[tuple[float, float]], **kwargs: Never) -> None: ...
    def setValue(self, *args: Unpack[tuple[float]], **kwargs: Never) -> None: ...
    def update(self, *args: Never, **kwargs: Never) -> None: ...
    def __delattr__(self, name: str) -> None:
        """Implement delattr(self, name)."""
    def __setattr__(self, name: str, value: object) -> None:
        """Implement setattr(self, name, value)."""

class NLE_AnimValueMapper(Shiboken.Object):
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_AnimValueState(enum.IntEnum):
    NLE_AVS_AT_KEY = 1
    NLE_AVS_NO_KEYS = 0
    NLE_AVS_OFF_KEY = 2
    NLE_AVS_PENDING = 3
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class NLE_DropType(enum.IntEnum):
    NLE_DROP_TYPE_CLIP = 1
    NLE_DROP_TYPE_NONE = 0
    NLE_DROP_TYPE_TRACK = 2
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class NLE_Event(Shiboken.Object):
    def __init__(self, *, no_constructor: Never) -> None: ...
    @staticmethod
    def clipSourceEvent(*args: Unpack[tuple[NLE_EventType, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    def count(self, *args: Never, **kwargs: Never) -> int: ...
    def destination(self, *args: Never, **kwargs: Never) -> int: ...
    def destinationA(self, *args: Never, **kwargs: Never) -> list[int]: ...
    def fx(self, *args: Never, **kwargs: Never) -> _NLEObject | None: ...
    @staticmethod
    def fxAddedEvent(*args: Unpack[tuple[_NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def fxEvent(*args: Unpack[tuple[NLE_EventType, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def fxMovedEvent(*args: Unpack[tuple[_NLEObject | None, Sequence[int], int, Sequence[int]]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def fxRemovedEvent(*args: Unpack[tuple[_NLEObject | None, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    def index(self, *args: Never, **kwargs: Never) -> int: ...
    def indexA(self, *args: Never, **kwargs: Never) -> list[int]: ...
    def item(self, *args: Never, **kwargs: Never) -> _NLEObject | None: ...
    @staticmethod
    def itemAddedEvent(*args: Unpack[tuple[_NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def itemEvent(*args: Unpack[tuple[NLE_EventType, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def itemRemovedEvent(*args: Unpack[tuple[_NLEObject | None, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def itemSourceChangeEvent(*args: Unpack[tuple[_NLEObject | None, _NLEObject | None, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def keyframeAddedEvent(*args: Unpack[tuple[_NLEObject | None, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def keyframeSetEvent(*args: Unpack[tuple[_NLEObject | None, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    def marker(self, *args: Never, **kwargs: Never) -> _NLEObject | None: ...
    @staticmethod
    def markerAddedEvent(*args: Unpack[tuple[_NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def markerEvent(*args: Unpack[tuple[NLE_EventType, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def markerRemovedEvent(*args: Unpack[tuple[_NLEObject | None, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    def note(self, *args: Never, **kwargs: Never) -> _NLEObject | None: ...
    @staticmethod
    def noteAddedEvent(*args: Unpack[tuple[_NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def noteEvent(*args: Unpack[tuple[NLE_EventType, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def noteRemovedEvent(*args: Unpack[tuple[_NLEObject | None, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    def oldSource(self, *args: Never, **kwargs: Never) -> _NLEObject | None: ...
    @staticmethod
    def redrawAllEvent(*args: Never, **kwargs: Never) -> NLE_Event: ...
    def source(self, *args: Never, **kwargs: Never) -> _NLEObject | None: ...
    @staticmethod
    def styleEvent(*args: Unpack[tuple[NLE_EventType]], **kwargs: Never) -> NLE_Event: ...
    def timeline(self, *args: Never, **kwargs: Never) -> _NLEObject | None: ...
    @staticmethod
    def timelineEvent(*args: Unpack[tuple[NLE_EventType, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    def track(self, *args: Never, **kwargs: Never) -> _NLEObject | None: ...
    @staticmethod
    def trackAddedEvent(*args: Unpack[tuple[_NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def trackEvent(*args: Unpack[tuple[NLE_EventType, _NLEObject | None]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def trackRemovedEvent(*args: Unpack[tuple[_NLEObject | None, _NLEObject | None, int]], **kwargs: Never) -> NLE_Event: ...
    @staticmethod
    def tracksMovedEvent(*args: Unpack[tuple[_NLEObject | None, int, int, int]], **kwargs: Never) -> NLE_Event: ...
    def type(self, *args: Never, **kwargs: Never) -> NLE_EventType: ...

class NLE_EventType(enum.IntEnum):
    NLE_CLIP_KEYFRAME_ADDED = 79
    NLE_CLIP_KEYFRAME_SET = 78
    NLE_CLIP_SOURCE_ADDED = 1
    NLE_CLIP_SOURCE_FPS_CHANGED = 3
    NLE_CLIP_SOURCE_IN_CHANGED = 4
    NLE_CLIP_SOURCE_NAME_CHANGED = 5
    NLE_CLIP_SOURCE_OUT_CHANGED = 6
    NLE_CLIP_SOURCE_REMOVED = 2
    NLE_EVENT_NONE = 0
    NLE_MARKER_ADDED = 7
    NLE_MARKER_COLOR_CHANGED = 9
    NLE_MARKER_DURATION_CHANGED = 10
    NLE_MARKER_LABEL_CHANGED = 11
    NLE_MARKER_NOTE_CHANGED = 12
    NLE_MARKER_POSITION_CHANGED = 13
    NLE_MARKER_RANGE_CHANGED = 14
    NLE_MARKER_REMOVED = 8
    NLE_NOTE_ADDED = 15
    NLE_NOTE_COLOR_CHANGED = 17
    NLE_NOTE_HEIGHT_CHANGED = 18
    NLE_NOTE_LABEL_CHANGED = 19
    NLE_NOTE_MESSAGE_CHANGED = 20
    NLE_NOTE_POSITION_CHANGED = 21
    NLE_NOTE_REMOVED = 16
    NLE_NOTE_WIDTH_CHANGED = 22
    NLE_NOTE_Y_CHANGED = 23
    NLE_REDRAW_ALL = 77
    NLE_STYLE_CHANGED = 24
    NLE_STYLE_UPDATED = 25
    NLE_TIMELINE_END_FRAME_CHANGED = 29
    NLE_TIMELINE_HAS_FRAME_RANGE_CHANGED = 27
    NLE_TIMELINE_NAME_CHANGED = 26
    NLE_TIMELINE_START_FRAME_CHANGED = 28
    NLE_TRACKS_GATHERED = 76
    NLE_TRACKS_MOVED = 75
    NLE_TRACK_ADDED = 30
    NLE_TRACK_COLOR_CHANGE = 32
    NLE_TRACK_ERROR_CHANGE = 36
    NLE_TRACK_FX_ADDED = 66
    NLE_TRACK_FX_BLEND_CHANGED = 72
    NLE_TRACK_FX_DISABLE_CHANGED = 73
    NLE_TRACK_FX_KEYS_CHANGED = 74
    NLE_TRACK_FX_MODE_CHANGED = 71
    NLE_TRACK_FX_MOVED = 68
    NLE_TRACK_FX_NAME_CHANGED = 69
    NLE_TRACK_FX_REMOVED = 67
    NLE_TRACK_FX_TYPE_CHANGED = 70
    NLE_TRACK_GEOTYPE_CHANGE = 38
    NLE_TRACK_ITEM_ADDED = 43
    NLE_TRACK_ITEM_CLIP_IN_CHANGED = 45
    NLE_TRACK_ITEM_CLIP_IN_OUT_CHANGED = 46
    NLE_TRACK_ITEM_CLIP_OUT_CHANGED = 47
    NLE_TRACK_ITEM_COLOR_CHANGED = 48
    NLE_TRACK_ITEM_CUT_IN_CHANGED = 49
    NLE_TRACK_ITEM_CUT_IN_OUT_CHANGED = 50
    NLE_TRACK_ITEM_CUT_OUT_CHANGED = 51
    NLE_TRACK_ITEM_DISSOLVE_IN_CHANGED = 53
    NLE_TRACK_ITEM_DISSOLVE_IN_OUT_CHANGED = 54
    NLE_TRACK_ITEM_DISSOLVE_OUT_CHANGED = 55
    NLE_TRACK_ITEM_ENABLED_CHANGED = 56
    NLE_TRACK_ITEM_FPS_CHANGED = 57
    NLE_TRACK_ITEM_KEYFRAME_CHANGED = 52
    NLE_TRACK_ITEM_NAME_CHANGED = 58
    NLE_TRACK_ITEM_OPACITY_CHANGED = 59
    NLE_TRACK_ITEM_POSITION_CHANGED = 60
    NLE_TRACK_ITEM_RECORD_IN_CHANGED = 63
    NLE_TRACK_ITEM_RECORD_IN_OUT_CHANGED = 65
    NLE_TRACK_ITEM_RECORD_OUT_CHANGED = 64
    NLE_TRACK_ITEM_REMOVED = 44
    NLE_TRACK_ITEM_SOURCE_CHANGED = 61
    NLE_TRACK_ITEM_SPEED_CHANGED = 62
    NLE_TRACK_LOCK_CHANGE = 33
    NLE_TRACK_MODE_CHANGE = 41
    NLE_TRACK_MUTE_CHANGE = 34
    NLE_TRACK_NAME_CHANGE = 35
    NLE_TRACK_OPACITY_CHANGE = 39
    NLE_TRACK_REMOVED = 31
    NLE_TRACK_SELECTION_CHANGE = 42
    NLE_TRACK_SOLO_CHANGE = 40
    NLE_TRACK_TYPE_CHANGE = 37
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class NLE_Flag(enum.IntEnum):
    NLE_ACTIVE_FLAG = 0
    NLE_BLOCK_UPDATES_FLAG = 1
    NLE_BUTTON_TRIGGER = 8
    NLE_INTERACTIVE_FLAG = 2
    NLE_INTERSECT_FLAG = 3
    NLE_RESERVED_FLAGS = 7
    NLE_SELECTION_RECT_OVER = 5
    NLE_SELECTION_STATE_FLAG = 4
    NLE_SNAPSHOT_FLAG = 7
    NLE_SNAP_FLAG = 6
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class NLE_Handle(enum.IntEnum):
    NLE_HANDLE_ALL = 383
    NLE_HANDLE_ANIM_VALUE = 128
    NLE_HANDLE_CUTS = 36
    NLE_HANDLE_DISSOLVES = 3
    NLE_HANDLE_DISSOLVE_IN = 1
    NLE_HANDLE_DISSOLVE_OUT = 2
    NLE_HANDLE_EDGES = 108
    NLE_HANDLE_ITEM = 16
    NLE_HANDLE_KEYFRAME = 256
    NLE_HANDLE_LEFT = 8
    NLE_HANDLE_LEFT_CUT = 4
    NLE_HANDLE_LEFT_RIGHT = 72
    NLE_HANDLE_NONE = 0
    NLE_HANDLE_RIGHT = 64
    NLE_HANDLE_RIGHT_CUT = 32
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class NLE_NoteStateFlag(enum.IntEnum):
    NLE_NOTE_NONE = 0
    NLE_NOTE_RESIZE_BOTTOM = 8
    NLE_NOTE_RESIZE_LEFT = 1
    NLE_NOTE_RESIZE_RIGHT = 2
    NLE_NOTE_RESIZE_TOP = 4
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class NLE_QtAnimValue(Shiboken.Object):
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtAnimValueHeader(PySide6.QtWidgets.QWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtAnimValueTail(PySide6.QtWidgets.QWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtColorChip(PySide6.QtWidgets.QPushButton):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ..., /) -> None: ...
    @typing.overload
    def __init__(self, color: PySide6.QtGui.QColor | PySide6.QtCore.Qt.GlobalColor | str, parent: PySide6.QtWidgets.QWidget | None = ..., /) -> None: ...

class NLE_QtCommonTimelineStyle(NLE_QtTimelineStyle):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtExpandButton(PySide6.QtWidgets.QPushButton):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class NLE_QtHeaderPushButton(PySide6.QtWidgets.QPushButton):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Unpack[tuple[str | None, str | None, bool]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtHitTest(Shiboken.Object):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint, arg1: PySide6.QtCore.QPointF | PySide6.QtCore.QPoint, arg2: int, /) -> None: ...

class NLE_QtLineEdit(PySide6.QtWidgets.QLineEdit):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtMotionMixer(NLE_QtTimelineWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class NLE_QtMotionMixerPathGadget(PySide6.QtWidgets.QWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class NLE_QtPushButton(PySide6.QtWidgets.QPushButton):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class NLE_QtShotsculpt(NLE_QtTimelineWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class NLE_QtStackedWidget(PySide6.QtWidgets.QStackedWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtTimelineFx(Shiboken.Object):
    def __init__(self, *args: Unpack[tuple[NLE_QtTimelineTrack, NLE_TimelineFx]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtTimelineItem(Shiboken.Object):
    def __init__(self, *args: Unpack[tuple[NLE_QtTimelineTrack, NLE_TimelineItem]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __eq__(self, other: object) -> bool:
        """Return self==value."""
    def __ge__(self, other: object) -> bool:
        """Return self>=value."""
    def __gt__(self, other: object) -> bool:
        """Return self>value."""
    def __le__(self, other: object) -> bool:
        """Return self<=value."""
    def __lt__(self, other: object) -> bool:
        """Return self<value."""
    def __ne__(self, other: object) -> bool:
        """Return self!=value."""

class NLE_QtTimelineKeyframe(Shiboken.Object):
    def __init__(self, *args: Unpack[tuple[NLE_TimelineKeyframe, NLE_TimelineItem, NLE_QtTimelineItem, NLE_QtTimelineWidget]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtTimelineNote(PySide6.QtWidgets.QWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtTimelineOverlayWidget(PySide6.QtWidgets.QWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: bool, /) -> None: ...

class NLE_QtTimelinePlayhead(PySide6.QtWidgets.QWidget, NLE_TimelinePlayhead):
    class StateFlag(enum.IntEnum):
        MARKERS_DURATION_TRANSLATE = 2
        MARKERS_TRANSLATE = 4
        MARKER_INSERT = 1
        PLAYHEAD_FOLLOW = 8
        PLAYHEAD_TRANSLATE = 16
        RANGE_TRANSLATE = 128
        TIMELINE_TRANSLATE = 32
        TIMELINE_ZOOM = 64
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Unpack[tuple[NLE_QtTimelineWidget]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtTimelineSelectionModel(PySide6.QtCore.QObject):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, timeline: NLE_QtTimelineWidget | None, /) -> None: ...

class NLE_QtTimelineStyle(PySide6.QtCore.QObject):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...

class NLE_QtTimelineTrack(Shiboken.Object):
    def __init__(self, *args: Unpack[tuple[NLE_QtTimelineWidget, NLE_QtTimelineTrackHeader, NLE_QtTimelineTrackTail]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtTimelineTrackArea(PySide6.QtWidgets.QWidget, NLE_AnimValueMapper):
    class StateFlag(enum.IntEnum):
        SELECT = 1
        SELECTION_BBOX = 2
        SELECTION_MOVE = 4
        TIMELINE_ZOOM = 8
        TRACK_AREA_RESIZE = 16
        TRACK_RESIZE = 32
        TRACK_RESIZE_PROXY = 64
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Unpack[tuple[NLE_QtTimelineTrackTail | None]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtTimelineTrackHeader(PySide6.QtWidgets.QWidget):
    class StateFlag(enum.IntEnum):
        TRACK_MOVE = 16
        TRACK_MOVE_PENDING = 8
        TRACK_RESIZE = 1
        TRACK_RESIZE_PROXY = 2
        TRACK_RESIZE_RESIZING = 5
        TRACK_RESIZE_RESIZING_PROXY = 7
        TRACK_RESIZING = 4
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Unpack[tuple[NLE_QtTimelineTrack | None]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_QtTimelineTrackTail(PySide6.QtWidgets.QWidget):
    class StateFlag(enum.IntEnum):
        TRACK_RESIZE = 1
        TRACK_RESIZE_PROXY = 2
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self, track: NLE_QtTimelineTrack | None, /) -> None: ...
    @typing.overload
    def __init__(self, track: NLE_QtTimelineTrack | None, area: NLE_QtTimelineTrackArea | None, /) -> None: ...

class NLE_QtTimelineWidget(PySide6.QtWidgets.QWidget, NLE_TimelineViewport):
    class AutoPanFlag(enum.IntEnum):
        ALL_AUTO_PAN = 3
        HORIZONTAL_AUTO_PAN = 1
        VERTICAL_AUTO_PAN = 2
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""

    class ZoomMode(enum.IntEnum):
        ZOOM_CENTERED = 0
        ZOOM_POINTER = 1
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class NLE_SnapFlag(enum.IntEnum):
    NLE_SNAP_CLIP = 63
    NLE_SNAP_CLIP_CUT_IN = 1
    NLE_SNAP_CLIP_CUT_OUT = 2
    NLE_SNAP_CLIP_DISSOLVE_IN = 4
    NLE_SNAP_CLIP_DISSOLVE_OUT = 8
    NLE_SNAP_CLIP_RECORD_IN = 16
    NLE_SNAP_CLIP_RECORD_OUT = 32
    NLE_SNAP_DEFAULT_MASK = 30527
    NLE_SNAP_FLAGGED = 64
    NLE_SNAP_IGNORE_LOCKED = 128
    NLE_SNAP_IGNORE_MUTED = 256
    NLE_SNAP_IGNORE_SOLO_MUTED = 512
    NLE_SNAP_MARKER = 1024
    NLE_SNAP_NONE = 0
    NLE_SNAP_NOT_FLAGGED = 2048
    NLE_SNAP_PLAYHEAD = 4096
    NLE_SNAP_SELECTED = 8192
    NLE_SNAP_UNSELECTED = 16384
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class NLE_StyleHint(enum.IntEnum):
    NLE_SH_CLIP_MOUSE_OVER_HIGHTLIGHT = 0
    NLE_SH_CLIP_ROUNDNESS = 1
    NLE_SH_CLIP_SELECTION_WIDTH = 2
    NLE_SH_CURSOR_POSITION = 3
    NLE_SH_CURSOR_POSITION_WIDTH = 4
    NLE_SH_ROUNDNESS = 5
    NLE_SH_SELECTION_RECT_INFO = 6
    NLE_SH_SELECTION_RECT_ROUNDNESS = 7
    NLE_SH_SELECTION_RECT_WIDTH = 8
    NLE_SH_SNAP_DISTANCE = 9
    NLE_SH_TRACK_HORIZONTAL_MARGIN = 10
    NLE_SH_TRACK_MOUSE_OVER_HIGHTLIGHT = 11
    NLE_SH_TRACK_RESIZE_HANDLE = 12
    NLE_SH_TRACK_SOLO_MUTED_DESATURATE = 13
    NLE_SH_TRACK_VERTICAL_MARGIN = 14
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class NLE_Timeline(Shiboken.Object):
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_TimelineClipLibrary(Shiboken.Object):
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_TimelineClipSource(Shiboken.Object):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, name: str | None, arg1: float, arg2: float, arg3: float, /) -> None: ...

class NLE_TimelineClipSourceRef(Shiboken.Object):
    def __init__(self, *args: Unpack[tuple[NLE_TimelineClipSource | None]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_TimelineFx(Shiboken.Object):
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_TimelineItem(NLE_TimelineClipSourceRef):
    def __init__(self, *args: Unpack[tuple[NLE_TimelineClipSource | None]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_TimelineKeyframe(Shiboken.Object):
    def __init__(self, *args: Unpack[tuple[NLE_TimelineItem | None]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_TimelineMarker(Shiboken.Object):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: float, /) -> None: ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, /) -> None: ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, arg2: int, /) -> None: ...

class NLE_TimelineNote(Shiboken.Object):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, arg0: float, arg1: float, text: str | None, arg3: int = ..., /) -> None: ...

class NLE_TimelinePlayhead(Shiboken.Object):
    def __init__(self, *args: Unpack[tuple[NLE_TimelineViewport | None]], **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_TimelineTrack(Shiboken.Object):
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_TimelineViewport(Shiboken.Object):
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class NLE_ValueReason(enum.IntEnum):
    NLE_VALUE_ACTIVE = 2
    NLE_VALUE_CHANGED = 1
    NLE_VALUE_NO_REASON = 0
    NLE_VALUE_START = 3
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class QIntList:
    __opaque_container__: ClassVar[bool] = ...
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def append(self, *args: Unpack[tuple[int]], **kwargs: Never) -> None:
        """append"""
    def capacity(self, *args: Never, **kwargs: Never) -> int:
        """capacity"""
    def clear(self, *args: Never, **kwargs: Never) -> None:
        """clear"""
    def constData(self, *args: Never, **kwargs: Never) -> memoryview:
        """constData"""
    def data(self, *args: Never, **kwargs: Never) -> memoryview:
        """data"""
    def pop_back(self, *args: Never, **kwargs: Never) -> None:
        """pop_back"""
    def pop_front(self, *args: Never, **kwargs: Never) -> None:
        """pop_front"""
    def prepend(self, *args: Unpack[tuple[int]], **kwargs: Never) -> None:
        """prepend"""
    def push_back(self, *args: Unpack[tuple[int]], **kwargs: Never) -> None:
        """push_back"""
    def push_front(self, *args: Unpack[tuple[int]], **kwargs: Never) -> None:
        """push_front"""
    def removeFirst(self, *args: Unpack[tuple[object]], **kwargs: Never) -> None:
        """removeFirst"""
    def removeLast(self, *args: Never, **kwargs: Never) -> None:
        """removeLast"""
    def reserve(self, *args: Unpack[tuple[int]], **kwargs: Never) -> None:
        """reserve"""
    def __delitem__(self, other: int) -> None:
        """Delete self[key]."""
    def __getitem__(self, index: int) -> int:
        """Return self[key]."""
    def __len__(self) -> int:
        """Return len(self)."""
    def __setitem__(self, index: int, object: int) -> None:
        """Set self[key] to value."""

class QT_AbstractAttributeModel(QT_AbstractAttributeModelAPI, PySide6.QtCore.QAbstractItemModel):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None, /) -> None: ...

class QT_AbstractAttributeModelAPI(Shiboken.Object):
    class CustomRoles(enum.IntEnum):
        EditExRole = 271
        ExcludesRole = 259
        FullPathRole = 257
        IncludesRole = 258
        InputRole = 266
        InternalItemRole = 262
        OverriddenRole = 261
        PostColorRole = 260
        RangeMaximumRole = 273
        RangeMinimumRole = 272
        RangeRole = 263
        RgbRole = 267
        ShowExpressionRole = 269
        StateColorRole = 265
        StateRole = 264
        TintedRgbRole = 268
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""

    class StateFlags(enum.IntEnum):
        KeyframeState = 2
        LockedState = 1
        PendingState = 4
        TimeDependentState = 8
        ValueSetState = 16
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class QT_AssetGallery(QT_Gallery):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, name: str | None, delegate: QT_GalleryItemDelegate | None = ..., view: QT_GalleryView | None = ..., parent: PySide6.QtWidgets.QWidget | None = ..., show_info_html: bool = ..., help_path: str | None = ..., arg6: bool = ..., /) -> None: ...

class QT_AssetGalleryModel(QT_GalleryModel):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None, /) -> None: ...

class QT_AssetGalleryRole(enum.IntEnum):
    AssetIdRole = 270
    AssetPathRole = 271
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class QT_ColorPalette(PySide6.QtWidgets.QDialog):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, pos: PySide6.QtCore.QPoint, parent: PySide6.QtWidgets.QWidget | None = ..., arg2: bool = ..., /) -> None: ...

class QT_Dialog(PySide6.QtWidgets.QDialog):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class QT_EnumObject(PySide6.QtCore.QObject):
    class MyEnum(enum.IntEnum):
        Enum = 4
        For = 2
        Some = 0
        The = 3
        Values = 1
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None, /) -> None: ...

class QT_FileLineEdit(PySide6.QtWidgets.QLineEdit):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, text: str | None, arg1: str | None = ..., arg2: int = ..., arg3: int = ..., parent: PySide6.QtWidgets.QWidget | None = ..., /) -> None: ...
    @typing.overload
    def __init__(self, text: str | None, arg1: int, arg2: int = ..., parent: PySide6.QtWidgets.QWidget | None = ..., /) -> None: ...
    @typing.overload
    def __init__(self, icon: PySide6.QtGui.QIcon, arg1: str | None = ..., arg2: int = ..., arg3: int = ..., parent: PySide6.QtWidgets.QWidget | None = ..., /) -> None: ...

class QT_Gallery(PySide6.QtWidgets.QWidget):
    class GalleryViewMode(enum.IntEnum):
        GridMode = 1
        ListMode = 3
        SplitMode = 4
        StripMode = 0
        TreeMode = 2
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""

    class ThumbnailPreset(enum.IntEnum):
        Large = 2
        Medium = 1
        Small = 0
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *, no_constructor: Never) -> None: ...

class QT_GalleryColumnProxy(PySide6.QtCore.QIdentityProxyModel):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None, /) -> None: ...

class QT_GalleryItemDelegate(PySide6.QtWidgets.QStyledItemDelegate):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self, arg0: float, /) -> None: ...
    @typing.overload
    def __init__(self, arg0: float, parent: PySide6.QtCore.QObject | None, /) -> None: ...

class QT_GalleryModel(PySide6.QtGui.QStandardItemModel):
    class LayoutMode(enum.IntEnum):
        FlatLayoutMode = 0
        TreeLayoutMode = 1
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None, /) -> None: ...

class QT_GalleryRole(enum.IntEnum):
    Color = 260
    CreationDate = 256
    DiffMarker = 259
    IsReadOnly = 269
    ItemType = 268
    Metadata = 265
    ModificationDate = 257
    Name = 0
    ParentId = 267
    ReservedForDerived = 270
    SizeHint = 13
    Star = 258
    Tags = 261
    TagsAdd = 262
    TagsRemove = 263
    Thumb = 1
    ThumbValid = 264
    Uuid = 266
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class QT_GalleryView(PySide6.QtWidgets.QListView):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class QT_HSlider(PySide6.QtWidgets.QSlider):
    class LabelPosition(enum.IntEnum):
        LabelsAbove = 1
        LabelsBelow = 2
        LabelsBothSides = 3
        LabelsLeft = 1
        LabelsRight = 2
        NoLabels = 0
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""

    class ValueBoxPosition(enum.IntEnum):
        NoValueBox = 0
        ValueBoxAbove = 1
        ValueBoxBelow = 2
        ValueBoxLeft = 1
        ValueBoxRight = 2
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class QT_HelpButton(PySide6.QtWidgets.QToolButton):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self, help_path: str | None, /) -> None: ...
    @typing.overload
    def __init__(self, help_path: str | None, tooltip: str | None, /) -> None: ...

class QT_HighlightTreeView(PySide6.QtWidgets.QTreeView):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class QT_HighlightTreeViewDelegate(PySide6.QtWidgets.QStyledItemDelegate):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None, /) -> None: ...

class QT_LinkRuleCardDelegate(PySide6.QtWidgets.QStyledItemDelegate):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None, /) -> None: ...

class QT_LinkRuleCardView(PySide6.QtWidgets.QAbstractItemView):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class QT_LopXformItem(PySide6.QtGui.QStandardItem):
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class QT_LopXformItemModel(PySide6.QtGui.QStandardItemModel):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class QT_Menu(PySide6.QtWidgets.QMenu):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = ..., /) -> None: ...
    @typing.overload
    def __init__(self, title: str | None, parent: PySide6.QtWidgets.QWidget | None = ..., /) -> None: ...

class QT_MixerFilterProxyModel(PySide6.QtCore.QSortFilterProxyModel, QT_AbstractAttributeModelAPI):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None, /) -> None: ...

class QT_MixerView(PySide6.QtWidgets.QListView):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class QT_PrimTreeView(QT_HighlightTreeView):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class QT_PrototypeGallery(QT_AssetGallery):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...

class QT_PrototypeGalleryModel(QT_AssetGalleryModel):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None, /) -> None: ...

class QT_SearchLineEdit(PySide6.QtWidgets.QLineEdit):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, text: str | None, parent: PySide6.QtWidgets.QWidget | None = ..., /) -> None: ...
    @typing.overload
    def __init__(self, icon: PySide6.QtGui.QIcon, parent: PySide6.QtWidgets.QWidget | None = ..., /) -> None: ...

class QT_Separator(PySide6.QtWidgets.QFrame):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, *args: Never, **kwargs: Never) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class QT_SnapshotGalleryModel(QT_GalleryModel):
    class Status(enum.IntEnum):
        Complete = 2
        Error = -1
        NoStatus = 0
        Paused = 3
        Rendering = 1
        def __format__(self, format_spec: str, /) -> str:
            """Convert to a string according to format_spec."""
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtCore.QObject | None, /) -> None: ...

class QT_SnapshotGalleryRole(enum.IntEnum):
    CloneId = 277
    Data = 276
    OwnsFile = 272
    RenderMethod = 274
    Rendering = 275
    Snapshot = 273
    SnapshotFile = 271
    def __format__(self, format_spec: str, /) -> str:
        """Convert to a string according to format_spec."""

class QT_TestWindow(PySide6.QtWidgets.QWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, /) -> None: ...
