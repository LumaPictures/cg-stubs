from _typeshed import Incomplete

def main() -> None:
    """otiotool main program.
    This function is resposible for executing the steps specified
    by all of the command line arguments in the right order.
    """
def parse_arguments(): ...
def read_inputs(input_paths):
    """Read one or more timlines from the list of file paths given.
    If a file path is '-' then a timeline is read from stdin.
    """
def keep_only_video_tracks(timeline) -> None:
    """Remove all tracks except for video tracks from a timeline."""
def keep_only_audio_tracks(timeline) -> None:
    """Remove all tracks except for audio tracks from a timeline."""
def filter_transitions(timelines):
    """Return a copy of the input timelines with all transitions removed.
    The overall duration of the timelines should not be affected."""
def _filter(item, names, patterns):
    """This is a helper function that returns the input item if
    its name matches the list of names given (if any), or matches any of the
    patterns given (if any). If the item's name does not match any of the
    given names or patterns, then None is returned."""
def filter_tracks(only_tracks_with_name, only_tracks_with_index, timelines):
    """Return a copy of the input timelines with only tracks that match
    either the list of names given, or the list of track indexes given."""
def filter_clips(only_clips_with_name, only_clips_with_name_regex, timelines):
    """Return a copy of the input timelines with only clips with names
    that match either the given list of names, or regular expression patterns."""
def stack_timelines(timelines):
    """Return a single timeline with all of the tracks from all of the input
    timelines stacked on top of each other. The resulting timeline should be
    as long as the longest input timeline."""
def concatenate_timelines(timelines):
    """Return a single timeline with all of the input timelines concatenated
    end-to-end. The resulting timeline should be as long as the sum of the
    durations of the input timelines."""
def flatten_timeline(timeline, which_tracks: str = 'video', keep: bool = False) -> None:
    """Replace the tracks of this timeline with a single track by flattening.
    If which_tracks is specified, you may choose 'video', 'audio', or 'all'.
    If keep is True, then the old tracks are retained and the new one is added
    above them instead of replacing them. This can be useful to see and
    understand how flattening works."""
def time_from_string(text, rate):
    '''This helper function turns a string into a RationalTime. It accepts
    either a timecode string (e.g. "HH:MM:SS:FF") or a string with a floating
    point value measured in seconds. The second argument to this function
    specifies the rate for the returned RationalTime.'''
def trim_timeline(start, end, timeline) -> None:
    '''Return a copy of the input timeline trimmed to the start and end
    times given. Each of the start and end times can be specified as either
    a timecode string (e.g. "HH:MM:SS:FF") or a string with a floating
    point value measured in seconds.'''
def remove_metadata_key(timeline, key) -> None: ...

__counters: Incomplete

def _counter(name):
    """This is a helper function for returning redacted names, based on a name."""
def redact_timeline(timeline) -> None:
    """Remove all metadata, names, or other identifying information from this
    timeline. Only the structure, schema and timing will remain."""
def copy_media(url, destination_path): ...
def relink_by_name(timeline, path):
    """Relink clips in the timeline to media files discovered at the
    given folder path."""
def copy_media_to_folder(timeline, folder) -> None:
    """Copy or download all referenced media to this folder, and relink media
    references to the copies."""
def print_timeline_stats(timeline) -> None:
    """Print some statistics about the given timeline."""
def inspect_timelines(name_regex, timeline) -> None:
    """Print some detailed information about the item(s) in the timeline with names
    that match the given regular expression."""
def summarize_timeline(list_tracks, list_clips, list_media, verify_media, list_markers, timeline) -> None:
    """Print a summary of a timeline, optionally listing the tracks, clips, media,
    and/or markers inside it."""
def write_output(output_path, output) -> None:
    """Write the given OTIO object to a file path. If the file path given is
    the string '-' then the output is written to stdout instead."""
