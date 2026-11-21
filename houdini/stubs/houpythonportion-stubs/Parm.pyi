from typing import Any
import hou
from hrecipes import rtypes

from typing import TypeAlias
from typing import TypeAlias
_ParmOption: TypeAlias = bool | list[hou.ParmTuple] | list[str] | set[str] | tuple[str, ...]
def set(self: hou.Parm, value: int | float | str | dict[str, str] | hou.Geometry | hou.ImageLayer | hou.NanoVDB | hou.DetachedAttrib | hou.CopCable | hou.Ramp | hou.Parm | None, language: hou.EnumValue[hou.exprLanguage] | None = None, follow_parm_reference: bool | None = None) -> None:
    """
set(self, value, language=None, follow_parm_reference=True)

    Sets the parameter value at the current frame.


    value
        A float, integer, or string to set the parameter value to.

        Pass in a hou.Ramp object, as the parameter value, to set the
        value of a ramp parameter. The ramp object's type needs to match
        the target ramp's type. Note that the hou.Ramp.colorType
        information is ignored since the color type on a ramp parameter
        is read-only.

        Pass in a hou.Geometry object, as the parameter value, to set
        the value of a geometry data parameter.

        Pass in a hou.Parm object to create a channel reference from
        this parameter to the specified parameter.

    language
        This option only applies when setting to a hou.Parm value.
        Specifies the expression language to use when creating a channel
        reference from this parameter to the given parameter. Set this
        option to an hou.exprLanguage object or None to choose the
        default language.

    follow_parm_reference
        If set to True, this method first follows the current channel
        references on this hou.Parm to determine the hou.Parm to modify.
        It acts to keep the chain of references and sets the value on
        the hou.Parm at the end of the chain. If the value is a hou.Parm
        object, then it sets a new channel reference on the hou.Parm
        that doesn't yet have one.

        If set to False, the current hou.Parm is modified directly and
        the chain of references is broken if there was an existing
        channel reference.

    If this parameter currently contains a channel reference to another
    parameter, this method will follow the channel references and change
    the value of the referenced parameter by default. If this is not the
    desired behavior, then set follow_parm_reference to False.
    Alternatively, first delete the channel reference for the string
    parameters that don't have the channel reference embedded in their
    string value using hou.Parm.deleteAllKeyframes or
    hou.Parm.revertToDefaults. If the parameter contains backtick
    expressions, it may be necessary to run parm.setExpression('') first
    to clear it. Then hou.Parm.deleteAllKeyframes can be used to delete
    it.

    Raises TypeError if the type of value does not match the type of
    this parameter. Raises hou.PermissionError if this parameter is not
    writable.

    Raises hou.OperationFailed if the value is None and the
    follow_parm_reference parameter is explicitly specified to True or
    False.

    See also hou.OpNode.setParms.

"""
def setPending(self: hou.Parm, value: int | float | str | dict[str, str] | hou.Geometry | hou.ImageLayer | hou.NanoVDB | hou.DetachedAttrib | hou.CopCable | hou.Ramp | None) -> None:
    """
setPending(self, value)

    Sets the parameter value at the current frame and marks it as
    pending if the parameter is keyed.

    Raises TypeError if the type of value does not match this
    parameter's type. Raises hou.PermissionError if this parameter is
    not writable.

"""
def saveClip(self: hou.Parm, file_name: str, start: float | None = None, end: float | None = None, sample_rate: float = 0) -> None:
    """
saveClip(self, file_name, start=None, end=None, sample_rate=0)

    Saves the animation associated with this parameter to the clip file
    specified by <file_name>. The extension of <file_name> determines
    the format of the saved file.

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

    Raises a hou.OperationFailed exception if the parameter does not
    have animation.

    Raises a hou.OperationFailed exception if there is an error saving
    the animation to file.

    Raises a hou.InvalidInput exception if start >= end. If specifying
    only <start>, ensure that the specified value is less than the
    global end frame. Likewise, if specifying only <end>, ensure it is
    larger than the global start frame.

"""
def loadClip(self: hou.Parm, file_name: str, sample_rate: float = 0, start: float | None = None) -> None:
    """auto-insert ocstring: HOM_Parm::loadClip"""
def setClipData(self: hou.Parm, data: bytes, binary: bool = True, blosc_compressed: bool = True, sample_rate: float = 0, start: float | None = None) -> None:
    """auto-insert ocstring: HOM_Parm::setClipData"""
def clipData(self: hou.Parm, start: float | None = None, end: float | None = None, binary: bool = True, use_blosc_compression: bool = True, sample_rate: float = 0) -> bytes:
    """
clipData(start=None, end=None, binary=True, use_blosc_compression=True,
sample_rate=0) -> str for Python 2, bytes for Python 3

    Returns the clip data for this parameter. This method is similar to
    hou.Parm.saveClip, except that it returns the clip data (file
    contents) instead of saving the animation to a clip file.

    <start>, <end>, and <sample_rate> behave the same as in
    hou.Parm.saveClip.

    If <binary> is True, return binary clip data otherwise return plain
    text (ASCII) clip data.

    If <use_blosc_compression> is True, blosc compress the binary clip
    data. This cannot be used for plain text (ASCII) clip data.

    The returned clip data is a bytes object in Python 3 and a str
    object in Python 2. See HOM binary data for more information.

    Raises a hou.OperationFailed exception if the parameter does not
    have animation.

    Raises a hou.InvalidInput exception if start >= end. If specifying
    only <start>, ensure that the specified value is less than the
    global end frame. Likewise, if specifying only <end>, ensure it is
    larger than the global start frame.

    Raises a hou.InvalidInput exception if binary = False and
    use_blosc_compression = True.

"""
def valueAsData(self: hou.Parm | hou.ParmTuple, **parm_value_opts: bool) -> rtypes.ParmValueData:
    """
valueAsData(evaluate=True, verbose=True) -> Union[int, str, float, dict,
list]

    Returns a JSON-like value representing the value of this parameter.


    evaluate
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

"""
def setValueFromData(self: hou.Parm | hou.ParmTuple, data: rtypes.ParmValueData) -> None:
    """
setValueFromData(data: Union[int, str, float, dict, list]) -> None

    Updates the value of this parameter from the given data (as returned
    by Parm.valueAsData()).


    data
        The parm value data that describes a parameter's value as data.

"""
def asData(self: hou.Parm | hou.ParmTuple, **parm_opts: bool) -> rtypes.ParmUnionData:
    """
asData(value=True, evaluate_value=False, locked=True, brief=True,
multiparm_instances=True, metadata=False, verbose=False) ->
dict[str,Any]

    Returns a JSON-like structure representing this parameter.


    value
        If this is True, the capture process saves the values of the
        parameters.

    evaluate_value
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    locked
        If this is True, the capture process saves the locked state of
        the parameters.

    brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    multiparm_instances
        If this is True, the capture processes multiparm instances of
        multiparm parent parameters.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

"""
def setFromData(self: hou.Parm | hou.ParmTuple, data: rtypes.ParmUnionData) -> None:
    """
setFromData(data: dict[str, Any]) -> None

    Updates the settings and value of this parameter from the given data
    (as returned by Parm.asData()).


    data
        The parm data that describes a parameter as data.

"""
def childrenAsData(self: hou.Parm | hou.ParmTuple, **parms_opts: _ParmOption | rtypes.ParsingCallback | None) -> rtypes.ParmDataDict:
    """
childrenAsData(values=True, default_values=False, evaluate_values=False,
locked=True, brief=True, multiparm_instances=True, metadata=False,
verbose: bool=False) -> dict[str, Any]

    When this parameter is a folder parameter, it returns a JSON-like
    structure representing any parameters inside that folder. Otherwise,
    it returns an empty dictionary.


    default_values
        Normally, when parms is True, the capture process only saves
        parameters with non-default values. If this is True, the capture
        process also saves parameters set to the default value. If the
        parms argument is a list of parameters to capture, this is
        ignored.

    evaluate_values
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    locked
        If this is True, the capture process saves the locked state of
        the parameters.

    brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

"""
def multiParmInstancesAsData(self: hou.Parm | hou.ParmTuple, start_index: int = 0, end_index: int = -1, **multiparm_instance_opts: bool) -> rtypes.MultiParmInstanceDataList | None:
    """
multiParmInstancesAsData(start_index: int=0, end_index: int=-1,
value=True, evaluate_value=False, links=True, locked=True, brief=True,
metadata=False, verbose=False) -> Sequence[dict[str, Any]]

    Returns a JSON-like structure representing any child instances of
    this multiparm.


    start_index
        The index from which to save the multiparm instances as data.

    end_index
        The index until which to save the multiparm instances as data.

    value
        If this is True, the capture process saves the values of the
        parameters.

    evaluate_value
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    links
        If this is True, reference links are also saved alongside the
        data.

    locked
        If this is True, the capture process saves the locked state of
        the parameters.

    brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

"""
def setMultiParmInstancesFromData(self: hou.Parm | hou.ParmTuple, data: rtypes.MultiParmInstanceDataList, index: int = -1) -> None:
    """
setMultiParmInstancesFromData(data: Sequence[dict[str, Any]]) -> None

    Sets the child instances of this multiparm from the given data (as
    returned by Parm.multiParmInstancesAsData()).


    data
        The data that describes the multiparm instances as data.

"""
def insertMultiParmInstancesFromData(self: hou.Parm | hou.ParmTuple, data: rtypes.MultiParmInstanceDataList, index: int = 0) -> None:
    """
insertMultiParmInstancesFromData(data: Sequence[dict[str, Any]], index:
int=0) -> None

    Inserts child instances into this multiparm at the given index from
    data (as returned by Parm.multiParmInstancesAsData()).


    data
        The data that describes the multiparm instances as data.

    index
        The index number at which to insert the new instances from data.

"""
def appendMultiParmInstancesFromData(self: hou.Parm | hou.ParmTuple, data: rtypes.MultiParmInstanceDataList) -> None:
    """
appendMultiParmInstancesFromData(data: Sequence[dict[str, Any]]) -> None

    Appends child instances into this multiparm from the given data (as
    returned by Parm.multiParmInstancesAsData()).


    data
        The data that describes the multiparm instances as data.

"""
def rampPointsAsData(self: hou.Parm | hou.ParmTuple, **ramppoints_opts: bool) -> rtypes.RampPointDataList | None:
    """
rampPointsAsData(evaluate=True, metadata=False, verbose=False)) ->
Sequence[dict[str, Any]]

    Returns a JSON-like structure representing the points of this ramp
    parameter.


    evaluate
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

"""
def setRampPointsFromData(self: hou.Parm | hou.ParmTuple, data: rtypes.RampPointDataList) -> None:
    """
setRampPointsFromData(data: Sequence[dict[str, Any]]) -> None

    Sets the points of this ramp parameter from the given data (as
    returned by Parm.rampPointsAsData()).


    data
        The data that describes the ramp points as data.

"""
def templateAsData(self: hou.Parm | hou.ParmTuple, children: bool = True, **parmtemplate_opts: bool | rtypes.ParsingCallback | None) -> rtypes.ParmTemplateDataDict | None:
    """
templateAsData(children=True, parmtemplate_order=False) -> dict[str,
Any]

    Returns a JSON-like structure representing the parent tuple's
    template.


    children
        Whether to recursively save the contents of nested parm
        templates.

    parmtemplate_order
        If this is True, an additional ordering_index key is saved for
        each parmtemplate data.

"""
def templateChildrenAsData(self: hou.Parm | hou.ParmTuple, **parmtemplate_opts: bool | rtypes.ParsingCallback | None) -> rtypes.ParmTemplateDataDict | None:
    """
templateChildrenAsData(parmtemplate_order=False) -> dict[str, Any]

    Returns a JSON-like structure representing the children of the
    parent tuple's template.


    parmtemplate_order
        If this is True, an additional ordering_index key is saved for
        each parmtemplate data.

"""
def insertTemplatesFromData(self: hou.Parm | hou.ParmTuple, data: rtypes.ParmTemplateDataDict, operation: str = 'insert_after', rename_conflicts: bool = True) -> dict[str, hou.ParmTuple]:
    '''
insertTemplatesFromData(data: dict[str, Any], operation="insert_after",
rename_conflicts=True) -> None

    Inserts spare parameters relative to this parameter, from the given
    data.


    data
        The parm templates data dictionary that describes a sequence of
        parameter templates as data.

    operation
        Controls how to combine the templates from the data with the
        existing parameter templates.


        insert_before
            Inserts the templates from this data before this parameter.

        insert_after
            Inserts the templates from this data after this parameter.

        insert_first
            Inserts the templates from this data at the start of this
            folder parameter.

        append_to_folder
            Inserts the templates from this data at the end of this
            folder parameter.

    rename_conflicts
        Whether to rename the newly created parm templates when they
        conflict with existing templates.

'''
