from .. import exceptions as exceptions, opentime as opentime, schema as schema

def track_trimmed_to_range(in_track, trim_range):
    """
    Returns a new track that is a copy of the in_track, but with items
    outside the trim_range removed and items on the ends trimmed to the
    trim_range.

    .. note:: The track is never expanded, only shortened.

    Please note that you could do nearly the same thing non-destructively by
    just setting the :py:class:`.Track`'s source_range but sometimes you want
    to really cut away the stuff outside and that's what this function is meant for.

    :param Track in_track: Track to trim
    :param TimeRange trim_range:
    :returns: New trimmed track
    :rtype: Track
    """
def track_with_expanded_transitions(in_track):
    """Expands transitions such that neighboring clips are trimmed into
    regions of overlap.

    For example, if your track is::

        Clip1, T, Clip2

    will return::

        Clip1', (Clip1_t, T, Clip2_t), Clip2'

    Where ``Clip1'`` is the part of ``Clip1`` not in the transition, ``Clip1_t`` is the
    part inside the transition and so on.

    .. note:: The items used in a transition are encapsulated in tuples.

    :param Track in_track: Track to expand
    :returns: Track
    :rtype: list[Track]
    """
def _expand_transition(target_transition, from_track):
    """ Expand transitions into the portions of pre-and-post clips that
    overlap with the transition.
    """
def _trim_from_transitions(thing, pre=None, post=None):
    """ Trim clips next to transitions. """
