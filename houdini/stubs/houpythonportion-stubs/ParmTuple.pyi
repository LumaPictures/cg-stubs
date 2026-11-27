import hou
from typing import Self

class ParmTupleIterator:
    """
    Custom iterator created for iterating over a ParmTuple.
    Mainly added to prevent constant breakpoints when ParmTuple.__getitem__ goes 
    out of bounds when iterating over a ParmTuple and being debug attached to the
    houdini process.
    """
    parm_tuple: hou.ParmTuple
    len: int
    idx: int
    def __init__(self, parm_tuple: hou.ParmTuple) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> hou.Parm: ...

def __iter__(self: hou.ParmTuple) -> ParmTupleIterator: ...
def set(self: hou.ParmTuple, value: hou.ParmTupleArgType | hou.ParmTuple, language: hou.EnumValue[hou.exprLanguage] | None = None, follow_parm_references: bool = True) -> None:
    """
set(self, values, language=None, follow_parm_references=True)

    Sets the values of the parameters in the tuple at the current frame.


    values
        A sequence of floats, integers or strings, corresponding to the
        components of this parameter tuple.

        For example, the parameter tuple for translation contains
        hou.Parm objects for translation along each of the axes, tx, ty
        and tz. If set is called with the following tuple of floats,
        (2.5, 4.0, 5.5), then the parameter tx with be set to 2.5, ty
        will be set to 4.0 and tz will be set to 5.5.

        You can also pass in a hou.ParmTuple object for this argument to
        create channel references from the parameters in this tuple to
        the parameters in the passed-in tuple. If this tuple has more
        parameters than the passed-in tuple then no work is performed on
        the extra parameters. If the passed-in tuple has more parameters
        than this tuple then the extra parameters are ignored.

    language
        This option only applies when setting to a hou.ParmTuple value.
        Specifies the expression language to use when creating channel
        references from this parameter tuple to the given parameter
        tuple. Set this option to an hou.exprLanguage object or None to
        choose the default language.

    follow_parm_references
        This option only applies when setting to a hou.Parm value. It
        defines the hou.Parm that gets modified.

        If set to True, this method first follows the current channel
        references on this hou.Parm to determine the hou.Parm to modify.
        It acts to keep the chain of references and sets a new channel
        reference on the hou.Parm that doesn't have one yet.

        If set to False, the current hou.Parm is modified directly and
        the chain of references is broken if there was an existing
        channel reference.

    If this parameter tuple currently contains channel references to
    another parameter tuple, this method will follow the channel
    references and change the value of the referenced parameter tuple.
    If this is not the desired behavior, first delete the channel
    reference for the string parameters that don't have the channel
    reference embedded in their string value using
    hou.Parm.deleteAllKeyframes or hou.Parm.revertToDefaults.

    Raises hou.InvalidSize if values has a different length than this
    parameter tuple. Raises hou.PermissionError if any of the parameters
    in this parameter tuple are not writable.

"""
def saveClip(self: hou.ParmTuple, file_name: str, start: float | None = None, end: float | None = None, sample_rate: float = 0) -> None:
    """
saveClip(self, file_name, start=None, end=None, sample_rate=0)

    Saves the animation associated with the parameters of this tuple to
    the clip file specified by <file_name>. The extension of <file_name>
    determines the format of the saved file.

    You can use one of the following extensions:

  * .clip: save animation as plain text (ASCII) clip file.

  * .bclip: save animation as a bclip (binary clip) file.

  * .bclip.sc: save animation as a bclip file using Blosc compression.

    Set <sample_rate> to a non-zero, non-negative value to specify the
    sample_rate to be used for the clip file. For example, if the
    current frame rate is 24 (hou.fps), and <sample_rate> is set to 12,
    the animation will be sampled every second frame since <sample_rate>
    is half of the current frame rate.

    If <start> is not None, start saving the animation from the
    specified frame (inclusive). Otherwise, the animation will be saved
    from the global start frame (inclusive).

    Similarly, if <end> is not None, stop saving the animation at the
    specified frame (inclusive). Otherwise, the animation will be saved
    until the global end frame (inclusive).

    The global start and end frame are specified in the Global Animation
    Options window.

    Raises a hou.OperationFailed exception if none of the parameters of
    this tuple have animation.

    Raises a hou.OperationFailed exception if there is an error saving
    the animation to file.

    Raises a hou.InvalidInput exception if start >= end. If specifying
    only <start>, ensure that the specified value is less than the
    global end frame. Likewise, if specifying only <end>, ensure it is
    larger than the global start frame.

"""
def loadClip(self: hou.ParmTuple, file_name: str, sample_rate: float = 0, start: float | None = None) -> None:
    """auto-insert ocstring: HOM_ParmTuple::loadClip"""
def setClipData(self: hou.ParmTuple, data: bytes, binary: bool = True, blosc_compressed: bool = True, sample_rate: float = 0, start: float | None = None) -> None:
    """auto-insert ocstring: HOM_ParmTuple::setClipData"""
def clipData(self: hou.ParmTuple, start: float | None = None, end: float | None = None, binary: bool = True, use_blosc_compression: bool = True, sample_rate: float = 0) -> bytes:
    """
clipData(start=None, end=None, binary=True, use_blosc_compression=True,
sample_rate=0) -> str for Python 2, bytes for Python 3

    Returns the clip data for the parameters of this tuple. This method
    is similar to hou.ParmTuple.saveClip, except that it returns the
    clip data (file contents) instead of saving the animation to a clip
    file.

    <start>, <end>, and <sample_rate> behave the same as in
    hou.ParmTuple.saveClip.

    If <binary> is True, return binary clip data otherwise, return plain
    text (ASCII) clip data.

    If <use_blosc_compression> is True, blosc compress the binary clip
    data. This cannot be used for plain text (ASCII) clip data.

    The returned clip data is a bytes object in Python 3 and a str
    object in Python 2. See HOM binary data for more information.

    Raises a hou.OperationFailed exception if none of the parameters of
    this tuple have animation.

    Raises a hou.InvalidInput exception if start >= end. If specifying
    only <start>, ensure that the specified value is less than the
    global end frame. Likewise, if specifying only <end>, ensure it is
    larger than the global start frame.

    Raises a hou.InvalidInput exception if binary = False and
    use_blosc_compression = True.

"""
def pressScriptActionButton(self: hou.ParmTuple, **kwargs: object) -> None: ...
