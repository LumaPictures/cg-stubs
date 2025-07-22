from ._opentime import RationalTime as RationalTime, TimeRange as TimeRange, TimeTransform as TimeTransform
from _typeshed import Incomplete

__all__ = ['RationalTime', 'TimeRange', 'TimeTransform', 'from_frames', 'from_timecode', 'from_time_string', 'from_seconds', 'to_timecode', 'to_nearest_timecode', 'to_frames', 'to_seconds', 'to_time_string', 'range_from_start_end_time', 'range_from_start_end_time_inclusive', 'duration_from_start_end_time', 'duration_from_start_end_time_inclusive']

from_frames: Incomplete
from_timecode: Incomplete
from_time_string: Incomplete
from_seconds: Incomplete
range_from_start_end_time: Incomplete
range_from_start_end_time_inclusive: Incomplete
duration_from_start_end_time: Incomplete
duration_from_start_end_time_inclusive: Incomplete

def to_timecode(rt, rate=None, drop_frame=None):
    """Convert a :class:`~RationalTime` into a timecode string."""
def to_nearest_timecode(rt, rate=None, drop_frame=None):
    """Convert a :class:`~RationalTime` into a timecode string."""
def to_frames(rt, rate=None):
    """Turn a :class:`~RationalTime` into a frame number."""
def to_seconds(rt):
    """Convert a :class:`~RationalTime` into float seconds"""
def to_time_string(rt):
    """
    Convert this timecode to time as used by ffmpeg, formatted as
    ``hh:mm:ss`` where ss is an integer or decimal number.
    """
