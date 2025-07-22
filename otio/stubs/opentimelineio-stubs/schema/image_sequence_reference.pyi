from .. import _otio as _otio
from ..core._core_utils import add_method as add_method

def __str__(self) -> str: ...
def __repr__(self) -> str: ...
def frame_range_for_time_range(self, time_range):
    """Returns first and last frame numbers for
    the given time range in the reference.

    :rtype: tuple[int]
    :raises ValueError: if the provided time range is outside the available range.
    """
def abstract_target_url(self, symbol):
    """
    Generates a target url for a frame where ``symbol`` is used in place
    of the frame number. This is often used to generate wildcard target urls.
    """
