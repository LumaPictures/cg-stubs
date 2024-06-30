# mypy: disable-error-code="misc, override, no-redef"

from _typeshed import Incomplete
from types import ModuleType
from typing import ClassVar

class FrameSpecIterator:
    """
    A simple iterator object that handles splitting multiple comma-separated
    FrameSpecs into their equivalent UsdUtils.TimeCodeRanges, and then yields
    all of the time codes in all of those ranges sequentially when iterated.
    
    This object also stores the minimum floating point precision required to
    disambiguate any neighboring time codes in the FrameSpecs given. This can
    be used to validate that the frame placeholder in a frame format string has
    enough precision to uniquely identify every frame without collisions.
    """
    FRAMESPEC_SEPARATOR: ClassVar[str] = ...
    UsdUtils: ClassVar[ModuleType] = ...
    def __init__(self, frameSpec) -> None: ...
    def __iter__(self): ...
    @property
    def minFloatPrecision(self): ...

def AddCmdlineArgs(argsParser, altDefaultTimeHelpText: str = ..., altFramesHelpText: str = ...):
    """
    Adds frame-related command line arguments to argsParser.

    The resulting 'frames' argument will be an iterable of UsdTimeCodes.

    If no command-line arguments are given, 'frames' will be a list containing
    only Usd.TimeCode.EarliestTime(). If '--defaultTime' is given, 'frames'
    will be a list containing only Usd.TimeCode.Default(). Otherwise,
    '--frames' must be given a FrameSpec (or a comma-separated list of
    multiple FrameSpecs), and 'frames' will be a FrameSpecIterator which when
    iterated will yield the time codes specified by the FrameSpec(s).
    """
def ConvertFramePlaceholderToFloatSpec(frameFormat):
    """
    Converts the frame placeholder in a frame format string to a Python
    {}-style float specifier for use with string.format().

    This function expects the input frameFormat string to contain exactly one
    frame placeholder. The placeholder must be composed of exactly one or two
    groups of one or more hashes ('#'), and if there are two, they must be
    separated by a dot ('.').

    The hashes after the dot indicate the floating point precision to use in
    the frame numbers inserted into the frame format string. If there is only
    a single group of hashes, the precision is zero and the inserted frame
    numbers will be integer values.

    The overall width of the frame placeholder specifies the minimum width to
    use when inserting frame numbers into the frame format string. Formatted
    frame numbers smaller than the minimum width will be zero-padded on the
    left until they reach the minimum width.

    If the input frame format string does not contain exactly one frame
    placeholder, this function will return None, indicating that this frame
    format string cannot be used when operating with a frame range.
    """
def GetFramePlaceholder(frameFormat):
    """
    Gets the frame placeholder in a frame format string.

    This function expects the input frameFormat string to contain exactly one
    frame placeholder. The placeholder must be composed of exactly one or two
    groups of one or more hashes ('#'), and if there are two, they must be
    separated by a dot ('.').

    If no such placeholder exists in the frame format string, None is returned.
    """
def ValidateCmdlineArgs(argsParser, args, frameFormatArgName: Incomplete | None = ...):
    """
    Validates the frame-related arguments in args parsed by argsParser.

    This populates 'frames' with the appropriate iterable based on the
    command-line arguments given, so it should be called after parse_args() is
    called on argsParser.

    When working with frame ranges, particularly when writing out images for
    each frame, it is common to also have command-line arguments such as an
    output image path for specifying where those images should be written. The
    value given to this argument should include a frame placeholder so that it
    can have the appropriate time code inserted. If the application has such an
    argument, its name can be specified using frameFormatArgName. That arg will
    be checked to ensure that it has a frame placeholder and it will be given
    a value with that placeholder replaced with a Python format specifier so
    that the value is ready to use with the str.format(frame=<timeCode>)
    method. If a frame range is not provided as an argument, then it is an
    error to include a frame placeholder in the frame format string.
    """
def _GetFloatStringPrecision(floatString):
    """
    Gets the floating point precision specified by floatString.

    floatString can either contain an actual float in string form, or it can be
    a frame placeholder. We simply split the string on the dot (.) and return
    the length of the part after the dot, if any.

    If there is no dot in the string, a precision of zero is assumed.
    """
