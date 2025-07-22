from typing import Any, overload

class RationalTime:
    """
    The RationalTime class represents a measure of time of :math:`rt.value/rt.rate` seconds.
    It can be rescaled into another :class:`~RationalTime`'s rate.
    """
    def __init__(self, value: float = ..., rate: float = ...) -> None:
        """__init__(self: opentimelineio._opentime.RationalTime, value: float = 0, rate: float = 1) -> None"""
    def almost_equal(self, other: RationalTime, delta: float = ...) -> bool:
        """almost_equal(self: opentimelineio._opentime.RationalTime, other: opentimelineio._opentime.RationalTime, delta: float = 0) -> bool"""
    def ceil(self) -> RationalTime:
        """ceil(self: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime"""
    @staticmethod
    def duration_from_start_end_time(start_time: RationalTime, end_time_exclusive: RationalTime) -> RationalTime:
        """duration_from_start_end_time(start_time: opentimelineio._opentime.RationalTime, end_time_exclusive: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime


        Compute the duration of samples from first to last (excluding last). This is not the same as distance.

        For example, the duration of a clip from frame 10 to frame 15 is 5 frames. Result will be in the rate of start_time.

        """
    @staticmethod
    def duration_from_start_end_time_inclusive(start_time: RationalTime, end_time_inclusive: RationalTime) -> RationalTime:
        """duration_from_start_end_time_inclusive(start_time: opentimelineio._opentime.RationalTime, end_time_inclusive: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime


        Compute the duration of samples from first to last (including last). This is not the same as distance.

        For example, the duration of a clip from frame 10 to frame 15 is 6 frames. Result will be in the rate of start_time.

        """
    def floor(self) -> RationalTime:
        """floor(self: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime"""
    @staticmethod
    def from_frames(frame: float, rate: float) -> RationalTime:
        """from_frames(frame: float, rate: float) -> opentimelineio._opentime.RationalTime

        Turn a frame number and rate into a :class:`~RationalTime` object.
        """
    @overload
    @staticmethod
    def from_seconds(seconds: float, rate: float) -> RationalTime:
        """from_seconds(*args, **kwargs)
        Overloaded function.

        1. from_seconds(seconds: float, rate: float) -> opentimelineio._opentime.RationalTime

        2. from_seconds(seconds: float) -> opentimelineio._opentime.RationalTime
        """
    @overload
    @staticmethod
    def from_seconds(seconds: float) -> RationalTime:
        """from_seconds(*args, **kwargs)
        Overloaded function.

        1. from_seconds(seconds: float, rate: float) -> opentimelineio._opentime.RationalTime

        2. from_seconds(seconds: float) -> opentimelineio._opentime.RationalTime
        """
    @staticmethod
    def from_time_string(time_string: str, rate: float) -> RationalTime:
        """from_time_string(time_string: str, rate: float) -> opentimelineio._opentime.RationalTime

        Convert a time with microseconds string (``HH:MM:ss`` where ``ss`` is an integer or a decimal number) into a :class:`~RationalTime`.
        """
    @staticmethod
    def from_timecode(timecode: str, rate: float) -> RationalTime:
        """from_timecode(timecode: str, rate: float) -> opentimelineio._opentime.RationalTime

        Convert a timecode string (``HH:MM:SS;FRAME``) into a :class:`~RationalTime`.
        """
    def is_invalid_time(self) -> bool:
        """is_invalid_time(self: opentimelineio._opentime.RationalTime) -> bool


        Returns true if the time is invalid. The time is considered invalid if the value or the rate are a NaN value
        or if the rate is less than or equal to zero.

        """
    @staticmethod
    def is_valid_timecode_rate(rate: float) -> bool:
        """is_valid_timecode_rate(rate: float) -> bool

        Returns true if the rate is valid for use with timecode.
        """
    @staticmethod
    def nearest_valid_timecode_rate(rate: float) -> float:
        """nearest_valid_timecode_rate(rate: float) -> float

        Returns the first valid timecode rate that has the least difference from the given value.
        """
    @overload
    def rescaled_to(self, new_rate: float) -> RationalTime:
        """rescaled_to(*args, **kwargs)
        Overloaded function.

        1. rescaled_to(self: opentimelineio._opentime.RationalTime, new_rate: float) -> opentimelineio._opentime.RationalTime

        Returns the time value for time converted to new_rate.

        2. rescaled_to(self: opentimelineio._opentime.RationalTime, other: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime

        Returns the time for time converted to new_rate.
        """
    @overload
    def rescaled_to(self, other: RationalTime) -> RationalTime:
        """rescaled_to(*args, **kwargs)
        Overloaded function.

        1. rescaled_to(self: opentimelineio._opentime.RationalTime, new_rate: float) -> opentimelineio._opentime.RationalTime

        Returns the time value for time converted to new_rate.

        2. rescaled_to(self: opentimelineio._opentime.RationalTime, other: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime

        Returns the time for time converted to new_rate.
        """
    def round(self) -> RationalTime:
        """round(self: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime"""
    def strictly_equal(self, other: RationalTime) -> bool:
        """strictly_equal(self: opentimelineio._opentime.RationalTime, other: opentimelineio._opentime.RationalTime) -> bool"""
    @overload
    def to_frames(self) -> int:
        """to_frames(*args, **kwargs)
        Overloaded function.

        1. to_frames(self: opentimelineio._opentime.RationalTime) -> int

        Returns the frame number based on the current rate.

        2. to_frames(self: opentimelineio._opentime.RationalTime, rate: float) -> int

        Returns the frame number based on the given rate.
        """
    @overload
    def to_frames(self, rate: float) -> int:
        """to_frames(*args, **kwargs)
        Overloaded function.

        1. to_frames(self: opentimelineio._opentime.RationalTime) -> int

        Returns the frame number based on the current rate.

        2. to_frames(self: opentimelineio._opentime.RationalTime, rate: float) -> int

        Returns the frame number based on the given rate.
        """
    @overload
    def to_nearest_timecode(self, rate: float, drop_frame: bool | None) -> str:
        """to_nearest_timecode(*args, **kwargs)
        Overloaded function.

        1. to_nearest_timecode(self: opentimelineio._opentime.RationalTime, rate: float, drop_frame: Optional[bool]) -> str

        Convert to nearest timecode (``HH:MM:SS;FRAME``)

        2. to_nearest_timecode(self: opentimelineio._opentime.RationalTime, rate: float) -> str

        3. to_nearest_timecode(self: opentimelineio._opentime.RationalTime) -> str
        """
    @overload
    def to_nearest_timecode(self, rate: float) -> str:
        """to_nearest_timecode(*args, **kwargs)
        Overloaded function.

        1. to_nearest_timecode(self: opentimelineio._opentime.RationalTime, rate: float, drop_frame: Optional[bool]) -> str

        Convert to nearest timecode (``HH:MM:SS;FRAME``)

        2. to_nearest_timecode(self: opentimelineio._opentime.RationalTime, rate: float) -> str

        3. to_nearest_timecode(self: opentimelineio._opentime.RationalTime) -> str
        """
    @overload
    def to_nearest_timecode(self) -> str:
        """to_nearest_timecode(*args, **kwargs)
        Overloaded function.

        1. to_nearest_timecode(self: opentimelineio._opentime.RationalTime, rate: float, drop_frame: Optional[bool]) -> str

        Convert to nearest timecode (``HH:MM:SS;FRAME``)

        2. to_nearest_timecode(self: opentimelineio._opentime.RationalTime, rate: float) -> str

        3. to_nearest_timecode(self: opentimelineio._opentime.RationalTime) -> str
        """
    def to_seconds(self) -> float:
        """to_seconds(self: opentimelineio._opentime.RationalTime) -> float"""
    def to_time_string(self) -> str:
        """to_time_string(self: opentimelineio._opentime.RationalTime) -> str"""
    @overload
    def to_timecode(self, rate: float, drop_frame: bool | None) -> str:
        """to_timecode(*args, **kwargs)
        Overloaded function.

        1. to_timecode(self: opentimelineio._opentime.RationalTime, rate: float, drop_frame: Optional[bool]) -> str

        Convert to timecode (``HH:MM:SS;FRAME``)

        2. to_timecode(self: opentimelineio._opentime.RationalTime, rate: float) -> str

        3. to_timecode(self: opentimelineio._opentime.RationalTime) -> str
        """
    @overload
    def to_timecode(self, rate: float) -> str:
        """to_timecode(*args, **kwargs)
        Overloaded function.

        1. to_timecode(self: opentimelineio._opentime.RationalTime, rate: float, drop_frame: Optional[bool]) -> str

        Convert to timecode (``HH:MM:SS;FRAME``)

        2. to_timecode(self: opentimelineio._opentime.RationalTime, rate: float) -> str

        3. to_timecode(self: opentimelineio._opentime.RationalTime) -> str
        """
    @overload
    def to_timecode(self) -> str:
        """to_timecode(*args, **kwargs)
        Overloaded function.

        1. to_timecode(self: opentimelineio._opentime.RationalTime, rate: float, drop_frame: Optional[bool]) -> str

        Convert to timecode (``HH:MM:SS;FRAME``)

        2. to_timecode(self: opentimelineio._opentime.RationalTime, rate: float) -> str

        3. to_timecode(self: opentimelineio._opentime.RationalTime) -> str
        """
    @overload
    def value_rescaled_to(self, new_rate: float) -> float:
        '''value_rescaled_to(*args, **kwargs)
        Overloaded function.

        1. value_rescaled_to(self: opentimelineio._opentime.RationalTime, new_rate: float) -> float

        Returns the time value for "self" converted to new_rate.

        2. value_rescaled_to(self: opentimelineio._opentime.RationalTime, other: opentimelineio._opentime.RationalTime) -> float
        '''
    @overload
    def value_rescaled_to(self, other: RationalTime) -> float:
        '''value_rescaled_to(*args, **kwargs)
        Overloaded function.

        1. value_rescaled_to(self: opentimelineio._opentime.RationalTime, new_rate: float) -> float

        Returns the time value for "self" converted to new_rate.

        2. value_rescaled_to(self: opentimelineio._opentime.RationalTime, other: opentimelineio._opentime.RationalTime) -> float
        '''
    def __add__(self, arg0: RationalTime) -> RationalTime:
        """__add__(self: opentimelineio._opentime.RationalTime, arg0: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime"""
    def __copy__(self) -> RationalTime:
        """__copy__(self: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime"""
    def __deepcopy__(self, copier: object = ...) -> RationalTime:
        """__deepcopy__(self: opentimelineio._opentime.RationalTime, copier: object = None) -> opentimelineio._opentime.RationalTime"""
    def __eq__(self, arg0: object) -> bool:
        """__eq__(self: opentimelineio._opentime.RationalTime, arg0: object) -> bool"""
    def __ge__(self, arg0: object) -> bool:
        """__ge__(self: opentimelineio._opentime.RationalTime, arg0: object) -> bool"""
    def __gt__(self, arg0: object) -> bool:
        """__gt__(self: opentimelineio._opentime.RationalTime, arg0: object) -> bool"""
    def __iadd__(self, arg0: RationalTime) -> RationalTime:
        """__iadd__(self: opentimelineio._opentime.RationalTime, arg0: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime"""
    def __le__(self, arg0: object) -> bool:
        """__le__(self: opentimelineio._opentime.RationalTime, arg0: object) -> bool"""
    def __lt__(self, arg0: object) -> bool:
        """__lt__(self: opentimelineio._opentime.RationalTime, arg0: object) -> bool"""
    def __ne__(self, arg0: object) -> bool:
        """__ne__(self: opentimelineio._opentime.RationalTime, arg0: object) -> bool"""
    def __neg__(self) -> RationalTime:
        """__neg__(self: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime"""
    def __sub__(self, arg0: RationalTime) -> RationalTime:
        """__sub__(self: opentimelineio._opentime.RationalTime, arg0: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime"""
    @property
    def rate(self) -> float:
        """(arg0: opentimelineio._opentime.RationalTime) -> float"""
    @property
    def value(self) -> float:
        """(arg0: opentimelineio._opentime.RationalTime) -> float"""

class TimeRange:
    """
    The TimeRange class represents a range in time. It encodes the start time and the duration,
    meaning that :meth:`end_time_inclusive` (last portion of a sample in the time range) and
    :meth:`end_time_exclusive` can be computed.
    """
    def __init__(self, start_time: RationalTime = ..., duration: RationalTime = ...) -> None:
        """__init__(self: opentimelineio._opentime.TimeRange, start_time: opentimelineio._opentime.RationalTime = None, duration: opentimelineio._opentime.RationalTime = None) -> None"""
    def before(self, *args, **kwargs):
        """before(*args, **kwargs)
        Overloaded function.

        1. before(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.RationalTime, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The end of `this` strictly precedes `other` by a value >= `epsilon_s`.
        ::

                     other
                       ↓
           [ this ]    *



        2. before(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The end of `this` strictly equals the start of `other` and
        the start of `this` strictly equals the end of `other`.
        ::

           [this][other]

        The converse would be ``other.meets(this)``

        """
    @overload
    def begins(self, other: RationalTime, epsilon_s: float = ...) -> bool:
        """begins(*args, **kwargs)
        Overloaded function.

        1. begins(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.RationalTime, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The start of `this` strictly equals `other`.
        ::

           other
             ↓
             *
             [ this ]



        2. begins(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The start of `this` strictly equals the start of `other`.
        The end of `this` strictly precedes the end of `other` by a value >= `epsilon_s`.
        ::

           [ this ]
           [    other    ]

        The converse would be ``other.begins(this)``

        """
    @overload
    def begins(self, other: TimeRange, epsilon_s: float = ...) -> bool:
        """begins(*args, **kwargs)
        Overloaded function.

        1. begins(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.RationalTime, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The start of `this` strictly equals `other`.
        ::

           other
             ↓
             *
             [ this ]



        2. begins(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The start of `this` strictly equals the start of `other`.
        The end of `this` strictly precedes the end of `other` by a value >= `epsilon_s`.
        ::

           [ this ]
           [    other    ]

        The converse would be ``other.begins(this)``

        """
    @overload
    def begins(self, this) -> Any:
        """begins(*args, **kwargs)
        Overloaded function.

        1. begins(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.RationalTime, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The start of `this` strictly equals `other`.
        ::

           other
             ↓
             *
             [ this ]



        2. begins(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The start of `this` strictly equals the start of `other`.
        The end of `this` strictly precedes the end of `other` by a value >= `epsilon_s`.
        ::

           [ this ]
           [    other    ]

        The converse would be ``other.begins(this)``

        """
    @overload
    def clamped(self, other: RationalTime) -> RationalTime:
        """clamped(*args, **kwargs)
        Overloaded function.

        1. clamped(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime


        Clamp 'other' (:class:`~RationalTime`) according to
        :attr:`start_time`/:attr:`end_time_exclusive` and bound arguments.


        2. clamped(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.TimeRange


        Clamp 'other' (:class:`~TimeRange`) according to
        :attr:`start_time`/:attr:`end_time_exclusive` and bound arguments.

        """
    @overload
    def clamped(self, other: TimeRange) -> TimeRange:
        """clamped(*args, **kwargs)
        Overloaded function.

        1. clamped(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime


        Clamp 'other' (:class:`~RationalTime`) according to
        :attr:`start_time`/:attr:`end_time_exclusive` and bound arguments.


        2. clamped(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.TimeRange


        Clamp 'other' (:class:`~TimeRange`) according to
        :attr:`start_time`/:attr:`end_time_exclusive` and bound arguments.

        """
    def contains(self, *args, **kwargs):
        """contains(*args, **kwargs)
        Overloaded function.

        1. contains(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.RationalTime) -> bool


        The start of `this` precedes `other`.
        `other` precedes the end of `this`.
        ::

                 other
                   ↓
                   *
           [      this      ]



        2. contains(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The start of `this` precedes start of `other`.
        The end of `this` antecedes end of `other`.
        ::

                [ other ]
           [      this      ]

        The converse would be ``other.contains(this)``

        """
    def duration_extended_by(self, other: RationalTime) -> TimeRange:
        """duration_extended_by(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.TimeRange"""
    def end_time_exclusive(self) -> RationalTime:
        """end_time_exclusive(self: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.RationalTime


        Time of the first sample outside the time range.

        If start frame is 10 and duration is 5, then end_time_exclusive is 15,
        because the last time with data in this range is 14.

        If start frame is 10 and duration is 5.5, then end_time_exclusive is
        15.5, because the last time with data in this range is 15.

        """
    def end_time_inclusive(self) -> RationalTime:
        """end_time_inclusive(self: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.RationalTime


        The time of the last sample containing data in the time range.

        If the time range starts at (0, 24) with duration (10, 24), this will be
        (9, 24)

        If the time range starts at (0, 24) with duration (10.5, 24):
        (10, 24)

        In other words, the last frame with data, even if the last frame is fractional.

        """
    def extended_by(self, other: TimeRange) -> TimeRange:
        """extended_by(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.TimeRange

        Construct a new :class:`~TimeRange` that is this one extended by other.
        """
    def finishes(self, *args, **kwargs):
        """finishes(*args, **kwargs)
        Overloaded function.

        1. finishes(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.RationalTime, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The end of `this` strictly equals `other`.
        ::

                other
                  ↓
                  *
           [ this ]



        2. finishes(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The start of `this` strictly antecedes the start of `other` by a value >= `epsilon_s`.
        The end of `this` strictly equals the end of `other`.
        ::

                   [ this ]
           [     other    ]

        The converse would be ``other.finishes(this)``

        """
    def intersects(self, other: TimeRange, epsilon_s: float = ...) -> bool:
        """intersects(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The start of `this` precedes or equals the end of `other` by a value >= `epsilon_s`.
        The end of `this` antecedes or equals the start of `other` by a value >= `epsilon_s`.
        ::

           [    this    ]           OR      [    other    ]
                [     other    ]                    [     this    ]

        The converse would be ``other.finishes(this)``

        """
    @overload
    def meets(self, other: TimeRange, epsilon_s: float = ...) -> bool:
        """meets(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The end of `this` strictly equals the start of `other` and
        the start of `this` strictly equals the end of `other`.
        ::

           [this][other]

        The converse would be ``other.meets(this)``

        """
    @overload
    def meets(self, this) -> Any:
        """meets(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The end of `this` strictly equals the start of `other` and
        the start of `this` strictly equals the end of `other`.
        ::

           [this][other]

        The converse would be ``other.meets(this)``

        """
    def overlaps(self, *args, **kwargs):
        """overlaps(*args, **kwargs)
        Overloaded function.

        1. overlaps(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.RationalTime) -> bool


        `this` contains `other`.
        ::

                other
                 ↓
                 *
           [    this    ]



        2. overlaps(self: opentimelineio._opentime.TimeRange, other: opentimelineio._opentime.TimeRange, epsilon_s: float = 2.6041666666666666e-06) -> bool


        The start of `this` strictly precedes end of `other` by a value >= `epsilon_s`.
        The end of `this` strictly antecedes start of `other` by a value >= `epsilon_s`.
        ::

           [ this ]
               [ other ]

        The converse would be ``other.overlaps(this)``

        """
    @staticmethod
    def range_from_start_end_time(start_time: RationalTime, end_time_exclusive: RationalTime) -> TimeRange:
        """range_from_start_end_time(start_time: opentimelineio._opentime.RationalTime, end_time_exclusive: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.TimeRange


        Creates a :class:`~TimeRange` from start and end :class:`~RationalTime`\\s (exclusive).

        For example, if start_time is 1 and end_time is 10, the returned will have a duration of 9.

        """
    @staticmethod
    def range_from_start_end_time_inclusive(start_time: RationalTime, end_time_inclusive: RationalTime) -> TimeRange:
        """range_from_start_end_time_inclusive(start_time: opentimelineio._opentime.RationalTime, end_time_inclusive: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.TimeRange


        Creates a :class:`~TimeRange` from start and end :class:`~RationalTime`\\s (inclusive).

        For example, if start_time is 1 and end_time is 10, the returned will have a duration of 10.

        """
    def __copy__(self) -> TimeRange:
        """__copy__(self: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.TimeRange"""
    def __deepcopy__(self, arg0: object) -> TimeRange:
        """__deepcopy__(self: opentimelineio._opentime.TimeRange, arg0: object) -> opentimelineio._opentime.TimeRange"""
    def __eq__(self, arg0: TimeRange) -> bool:  # type: ignore[override]
        """__eq__(self: opentimelineio._opentime.TimeRange, arg0: opentimelineio._opentime.TimeRange) -> bool"""
    def __ne__(self, arg0: TimeRange) -> bool:  # type: ignore[override]
        """__ne__(self: opentimelineio._opentime.TimeRange, arg0: opentimelineio._opentime.TimeRange) -> bool"""
    @property
    def duration(self) -> RationalTime:
        """(arg0: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.RationalTime"""
    @property
    def start_time(self) -> RationalTime:
        """(arg0: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.RationalTime"""

class TimeTransform:
    """1D transform for :class:`~RationalTime`. Has offset and scale."""
    def __init__(self, offset: RationalTime = ..., scale: float = ..., rate: float = ...) -> None:
        """__init__(self: opentimelineio._opentime.TimeTransform, offset: opentimelineio._opentime.RationalTime = otio.opentime.RationalTime(value=0, rate=1), scale: float = 1, rate: float = -1) -> None"""
    @overload
    def applied_to(self, other: TimeRange) -> TimeRange:
        """applied_to(*args, **kwargs)
        Overloaded function.

        1. applied_to(self: opentimelineio._opentime.TimeTransform, other: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.TimeRange

        2. applied_to(self: opentimelineio._opentime.TimeTransform, other: opentimelineio._opentime.TimeTransform) -> opentimelineio._opentime.TimeTransform

        3. applied_to(self: opentimelineio._opentime.TimeTransform, other: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime
        """
    @overload
    def applied_to(self, other: TimeTransform) -> TimeTransform:
        """applied_to(*args, **kwargs)
        Overloaded function.

        1. applied_to(self: opentimelineio._opentime.TimeTransform, other: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.TimeRange

        2. applied_to(self: opentimelineio._opentime.TimeTransform, other: opentimelineio._opentime.TimeTransform) -> opentimelineio._opentime.TimeTransform

        3. applied_to(self: opentimelineio._opentime.TimeTransform, other: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime
        """
    @overload
    def applied_to(self, other: RationalTime) -> RationalTime:
        """applied_to(*args, **kwargs)
        Overloaded function.

        1. applied_to(self: opentimelineio._opentime.TimeTransform, other: opentimelineio._opentime.TimeRange) -> opentimelineio._opentime.TimeRange

        2. applied_to(self: opentimelineio._opentime.TimeTransform, other: opentimelineio._opentime.TimeTransform) -> opentimelineio._opentime.TimeTransform

        3. applied_to(self: opentimelineio._opentime.TimeTransform, other: opentimelineio._opentime.RationalTime) -> opentimelineio._opentime.RationalTime
        """
    def __copy__(self) -> TimeTransform:
        """__copy__(self: opentimelineio._opentime.TimeTransform) -> opentimelineio._opentime.TimeTransform"""
    def __deepcopy__(self, memo: dict) -> TimeTransform:
        """__deepcopy__(self: opentimelineio._opentime.TimeTransform, memo: dict) -> opentimelineio._opentime.TimeTransform"""
    def __eq__(self, arg0: TimeTransform) -> bool:  # type: ignore[override]
        """__eq__(self: opentimelineio._opentime.TimeTransform, arg0: opentimelineio._opentime.TimeTransform) -> bool"""
    def __ne__(self, arg0: TimeTransform) -> bool:  # type: ignore[override]
        """__ne__(self: opentimelineio._opentime.TimeTransform, arg0: opentimelineio._opentime.TimeTransform) -> bool"""
    @property
    def offset(self) -> RationalTime:
        """(arg0: opentimelineio._opentime.TimeTransform) -> opentimelineio._opentime.RationalTime"""
    @property
    def rate(self) -> float:
        """(arg0: opentimelineio._opentime.TimeTransform) -> float"""
    @property
    def scale(self) -> float:
        """(arg0: opentimelineio._opentime.TimeTransform) -> float"""
