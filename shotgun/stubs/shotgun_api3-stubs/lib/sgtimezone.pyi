from _typeshed import Incomplete
from datetime import tzinfo

class SgTimezone:
    """
    Shotgun's server infrastructure is configured for Coordinated Universal
    Time (UTC). In order to provide relevant local timestamps to users, we wrap
    the datetime module's tzinfo to provide convenient conversion methods.
    """
    ZERO: Incomplete
    STDOFFSET: Incomplete
    DSTOFFSET: Incomplete
    DSTOFFSET = STDOFFSET
    DSTDIFF: Incomplete
    utc: Incomplete
    local: Incomplete
    def __init__(self) -> None: ...
    @classmethod
    def UTC(cls):
        """
        For backwards compatibility, from when UTC was a nested class,
        we allow instantiation via SgTimezone
        """
    @classmethod
    def LocalTimezone(cls):
        """
        For backwards compatibility, from when LocalTimezone was a nested
        class, we allow instantiation via SgTimezone
        """

class UTC(tzinfo):
    """
    Implementation of datetime's tzinfo to provide consistent calculated
    offsets against Coordinated Universal Time (UTC)
    """
    def utcoffset(self, dt): ...
    def tzname(self, dt): ...
    def dst(self, dt): ...

class LocalTimezone(tzinfo):
    """
    Implementation of datetime's tzinfo to provide convenient conversion
    between Shotgun server time and local user time
    """
    def utcoffset(self, dt):
        """
        Difference between the user's local timezone and UTC timezone in seconds
        """
    def dst(self, dt):
        """
        Daylight savings time (dst) offset in seconds
        """
    def tzname(self, dt):
        """
        Name of the user's local timezone, including a reference
        to daylight savings time (dst) if applicable
        """
    def _isdst(self, dt):
        """
        Calculate whether the timestamp in question was in daylight savings
        """
