from .. import _otio as _otio, opentime as opentime, schema as schema
from _typeshed import Incomplete

__doc__: str  # type: ignore[no-redef]

def top_clip_at_time(in_stack, t):
    """Return the topmost visible child that overlaps with time ``t``.

    Example::

        tr1: G1, A, G2
        tr2: [B------]
        G1, and G2 are gaps, A and B are clips.

    If ``t`` is within ``A``, ``A`` will be returned. If ``t`` is within ``G1`` or
    ``G2``, ``B`` will be returned.

    :param Stack in_stack: Stack
    :param RationalTime t: Time
    :returns: Top clip
    :rtype: Clip
    """

flatten_stack: Incomplete
