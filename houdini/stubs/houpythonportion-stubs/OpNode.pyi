from typing import Any
import datetime
import hou
from collections.abc import Generator, Iterable, Mapping, Sequence
from hrecipes import rtypes

from typing import TypeAlias
from typing import Literal
from typing import TypeAlias
_ParmOption: TypeAlias = bool | list[hou.ParmTuple] | list[str] | set[str] | tuple[str, ...]
_ParmTemplateOption: TypeAlias = Literal['none', 'spare_only', 'all']
_ParmValue: TypeAlias = hou.ParmArgType | hou.ParmTupleArgType | Sequence[Mapping[str, '_ParmValue']]
_ItemOption: TypeAlias = _ParmOption | _ParmTemplateOption | rtypes.ParsingCallback | None
def addSpareParmTuple(self: hou.OpNode, parm_template: hou.ParmTemplate, in_folder: Sequence[str] = ..., create_missing_folders: bool = False) -> hou.ParmTuple:
    '''
addSpareParmTuple(self, parm_template, in_folder=(),
create_missing_folders=False) -> hou.ParmTuple

    Add a spare parameter tuple to the end of the parameters on the
    node. If in_folder is not an empty sequence, this method adds the
    parameters to the end of the parameters in a particular folder.


    parm_template
        A hou.ParmTemplate subclass instance that specifies the type of
        parameter tuple, the default value, range, etc.

    in_folder
        A sequence of folder names specifying which folder will hold the
        parameter. If this parameter is an empty sequence (e.g. ()),
        Houdini will not put the parameter inside a folder. If it is,
        for example, ("Misc", "Controls"), Houdini puts it inside the
        Controls folder that\'s inside the Misc folder. If it is, for
        example, ("Misc",), Houdini puts it inside the Misc folder.

    create_missing_folders
        If True, and the folder location specified by in_folder does not
        exist, this method creates the missing containing folders.

    Note that this method can add a single folder by passing a
    hou.FolderParmTemplate for parm_template.

    See also the removeSpareParmTuple() and addSpareParmFolder()
    methods.

    This method is deprecated in favor of setParmTemplateGroup.

'''
def replaceSpareParmTuple(self: hou.OpNode, parm_tuple_name: str, parm_template: hou.ParmTemplate) -> hou.ParmTuple:
    """
replaceSpareParmTuple(self, parm_tuple_name, parm_template)

    Replace an existing spare parameter tuple with a new one. The old
    parameter tuple is removed and the new one is added in its place.


    parm_tuple_name
        The name of the spare parameter tuple to replace. Raises
        hou.OperationFailed if no parameter tuple exists with this name,
        or if it is the name of a non-spare parameter.

    parm_template
        A hou.ParmTemplate describing the new parameter tuple.

    The new parameter tuple may or may not have the same name as the old
    one. By providing a parameter tuple with the same name, you can
    modify an existing spare parameter tuple.

    Note that you cannot replace non-spare parameter tuples. However,
    you can change the visibility of non-spare parameters using
    hou.ParmTuple.hide.

    To change a parameter for all instances of digital asset, use
    hou.HDADefinition.replaceParmTuple.

    This method is deprecated in favor of setParmTemplateGroup.

"""
def removeSpareParmTuple(self: hou.OpNode, parm_tuple: hou.ParmTuple) -> None:
    """
removeSpareParmTuple(self, parm_tuple)

    Removes the specified spare parameter tuple.

    See also addSpareParmTuple().

    This method is deprecated in favor of setParmTemplateGroup.

"""
def addControlParmFolder(self: hou.OpNode, folder_name: str | None = None, parm_name: str | None = None) -> None:
    """
addControlParmFolder(self, folder_name=None, parm_name=None)

    Adds a control parameter folder as the front-most folder at the top-
    level. This is used to increase visibility of customized control
    parameters. If a folder of the same name already exists, no new
    folder will be created. If folder_name is None, it will be set as
    'Controls'. If parm_name is None, it will be set as 'folder'.

    If there are no current folders present, the existing parameters
    will be grouped together and stored into a new folder named
    'Parameters' and placed after the new control parameter folder.

"""
def addSpareParmFolder(self: hou.OpNode, folder_name: str, in_folder: Sequence[str] = ..., parm_name: str | None = None, create_missing_folders: bool = False) -> None:
    """
addSpareParmFolder(self, folder_name, in_folder=(), parm_name=None,
create_missing_folders=False)

    Adds a folder to the spare parameters.

    Note that all the folders in a set correspond to one parameter. If
    this is the first folder to go in the set, parm_name will be used as
    the parameter name. Otherwise, parm_name will be ignored and the
    parameter name of the first folder in the set is used.

    If this is the first folder in the set and parm_name is None, it
    will default to 'sparefolder0'. If parm_name is already in use, a
    unique name will be automatically generated.

    If create_missing_folders is True, this method will create the
    folders in in_folder that don't exist. So, this method can be used
    to add spare folders and a spare parameter at the same time.

    Note that you can add folders by passing a hou.FolderParmTemplate to
    the addSpareParmTuple method, so this method is deprecated. Note
    also that addSpareParmTuple is deprecated in favor of
    setParmTemplateGroup.

    See also the removeSpareParmFolder and addSpareParmTuple methods.

    This method is deprecated in favor of setParmTemplateGroup.

"""
def removeSpareParmFolder(self: hou.OpNode, folder: Sequence[str]) -> None:
    '''
removeSpareParmFolder(self, folder)

    Removes an empty folder from the spare parameters.

    folder is a sequence of folder names. So, to remove the Output
    folder, use ("Output",) instead of "Output".

    See also addSpareParmFolder(), hou.ParmTemplateGroup.remove, and
    hou.ParmTemplateGroup.findFolder.

'''
def setParms(self: hou.OpNode, parm_dict: Mapping[str, _ParmValue]) -> None:
    '''
setParms(self, parm_dict)

    Given a dictionary mapping parm names to values, set each of the
    corresponding parms on this node to the given value in the
    dictionary.

    The following example sets the tx and sy parameters at once:

  > >>> node = hou.node("/obj").createNode("geo")
  > >>> node.setParms({"tx": 1, "sy": 3})

    The names are tried against both parameters and parmameter tuples,
    so the base name can also be used:

  > >>> node = hou.node("/obj").createNode("geo")
  > >>> node.setParms({"t": (1, 2, 3), "s": (3, 3, 3)})

    Raises hou.OperationFailed if any of the parameter names are not
    valid.

    See also the setParmExpressions method.

'''
def setParmsPending(self: hou.OpNode, parm_dict: Mapping[str, hou.ParmArgType | hou.ParmTupleArgType]) -> None:
    """
setParmsPending(self, parm_dict)

    Given a dictionary mapping parm names to values, sets the pending
    value of each of the corresponding parms on this node. Supports both
    parameters and parameter tuples.

    Raises hou.OperationFailed if any of the parameter names are not
    valid.

    See also the setPending method.

"""
def setParmExpressions(self: hou.OpNode, parm_dict: Mapping[str, str | Sequence[str]], language: hou.EnumValue[hou.exprLanguage] | None = None, replace_expressions: bool = True) -> None:
    '''
setParmExpressions(self, parm_dict, language=None,
replace_expressions=True)

    Given a dictionary mapping parm names to expression strings, set
    each of the corresponding parms on this node to the given expression
    string in the dictionary.

    See hou.Parm.setExpression for a description of the language and
    replace_expressions parms.

    The following example expressions set the tx and sy parameters at
    once:

  > >>> node = hou.node("/obj").createNode("geo")
  > >>> node.setParmExpressions({"tx": \'ch("ty")\', "sy": "sin($F)"})

    Raises hou.OperationFailed if any of the parameter names are not
    valid.

    See also the setParms method.

'''
def allParms(self: hou.OpNode) -> Generator[hou.Parm, None, None]:
    '''
allParms(self) -> generator of hou.Parm

    Recursively return a sequence of all the parameters on all of the
    nodes contained in this node including this node.

    This method is a generator and does not return a tuple.

    Here is an example of printing out the parameter paths for all nodes
    under /obj:

  > root_node = hou.node("/obj")
  > for parm in root_node.allParms():
  >     print parm.path()
'''
def creationTime(self: hou.OpNode) -> datetime.datetime:
    """
creationTime(self) -> datetime.datetime

    Return the date and time when the node was created.

"""
def modificationTime(self: hou.OpNode) -> datetime.datetime:
    """
modificationTime(self) -> datetime.datetime

    Return the date and time when the node was last modified.

"""
def saveChildrenToFile(self: hou.OpNode, nodes: Iterable[hou.NetworkMovableItem], network_boxes: Iterable[hou.NetworkMovableItem], file_name: str) -> None:
    """
saveChildrenToFile(self, nodes, network_boxes, file_name)

    Combines separate lists of nods and network boxes into a single
    sequence, and calls hou.Node.saveItemsToFile. This method is
    provided for backward compatibility. New code should call
    saveItemsToFile directly.


    nodes
        A sequence of hou.Nodes that are children of this node.

    network_boxes
        A sequence of hou.NetworkBoxes that are contained in this node.
        Note that the contents of the network boxes are not
        automatically saved, so it is up to you to put them in the list
        of nodes.

"""
def loadChildrenFromFile(self: hou.OpNode, file_name: str, ignore_load_warnings: bool = False) -> None:
    """
loadChildrenFromFile(self, file_name, ignore_load_warnings=False)

    Calls hou.Node.loadItemsFromFile. Provided for backward
    compatibility. New code should call loadItemsFromFile directly.

"""
def saveParmClip(self: hou.OpNode, file_name: str, start: float | None = None, end: float | None = None, sample_rate: float = 0, scoped_only: bool = False) -> None:
    """
saveParmClip(self, file_name, start=None, end=None, sample_rate=0,
scoped_only=False)

    Saves the animation associated with the parameters of this node to
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

    If <scoped_only> is True, only the animation associated with scoped
    parameters will be saved. If there are no scoped parameters, the
    animation associated with auto-scoped parameters will be saved.

    If <scoped_only> is False, animation associated with any of the
    parameters of this node will be saved.

    Raises a hou.OperationFailed exception if none of the parameters of
    this node have animation. If <scoped_only> is True, this exception
    can be raised if none of the scoped parameters have animation, or if
    none of the auto-scoped parameters have animation (if the node has
    no scoped parameters).

    Raises a hou.OperationFailed exception if there is an error saving
    the animation to file.

    Raises a hou.InvalidInput exception if start >= end. If specifying
    only <start>, ensure that the specified value is less than the
    global end frame. Likewise, if specifying only <end>, ensure it is
    larger than the global start frame.

"""
def loadParmClip(self: hou.OpNode, file_name: str, sample_rate: float = 0, start: float | None = None) -> None:
    """auto-insert ocstring: HOM_OpNode::loadParmClip"""
def setParmClipData(self: hou.OpNode, data: bytes, binary: bool = True, blosc_compressed: bool = True, sample_rate: float = 0, start: float | None = None) -> None:
    """auto-insert ocstring: HOM_OpNode::setParmClipData"""
def parmClipData(self: hou.OpNode, start: float | None = None, end: float | None = None, binary: bool = True, use_blosc_compression: bool = True, sample_rate: float = 0, scoped_only: bool = False) -> bytes:
    """
parmClipData(start=None, end=None, binary=True,
use_blosc_compression=True, sample_rate=0, scoped_only=False) -> str for
Python 2, bytes for Python 3

    Returns the clip data for the parameters of this node. This method
    is similar to hou.Node.saveParmClip, except that it returns the clip
    data (file contents) instead of saving the animation to a clip file.

    <start>, <end>, <sample_rate>, and <scoped_only> behave the same as
    in hou.Node.saveParmClip.

    If <binary> is True, return binary clip data otherwise return plain
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
def copyTo(self: hou.OpNode, destination_node: hou.Node) -> hou.OpNode:
    """
copyTo(destination_node) -> hou.Node

    Copy this node to a new place in the node hierarchy. The new node is
    placed inside the given destination node. This method returns the
    new node.

    Raises hou.OperationFailed if the destination node cannot contain
    the new node. Raises hou.PermissionError if the destination node is
    inside a locked asset.

"""
def asData(self: hou.OpNode, **item_opts: _ItemOption) -> rtypes.NetworkItemData:
    '''
asData(nodes_only=False, children=False, editables=False, inputs=False,
position=False, flags=False, parms: Union[bool, Sequence[hou.ParmTuple],
Sequence[str]]=True, default_parmvalues=False,
evaluate_parmvalues=False, parms_as_brief=True,
parmtemplates="spare_only", metadata=False, verbose=False) -> dict[str,
Any]

    Returns a JSON-like data structure representing this node.


    nodes_only
        If this is True, the capture process only saves nodes, ignoring
        sticky notes, network boxes, and dots.

    children
        If this is False, the capture process only saves the top level
        nodes, ignoring nodes inside subnets and unlocked assets.

    editables
        If this is False, the capture process ignores nodes inside
        editable dive target networks inside assets.

    inputs
        If this is True, the capture process saves input connections.

    position
        If this is True, the capture process saves the node position.

    flags
        If this is True, the capture process saves flag states.

    parms
        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    default_parmvalues
        Normally, when parms is True, the capture process only saves
        parameters with non-default values. If this is True, the capture
        process also saves parameters set to the default value. If the
        parms argument is a list of parameters to capture, this is
        ignored.

    evaluate_parmvalues
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    parms_as_brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    parmtemplates
        If this is "spare_only", the capture process only saves spare
        parameter templates so it can recreate them. This is helpful to
        ensure minimal change to the parameter interface on nodes where
        additional parameters were added. If this is "all", the capture
        process saves template data for all parameters.

    parmfilter
        This captures the settings used for the parameter filter and
        search bar for each node.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

'''
def setFromData(self: hou.OpNode, data: rtypes.NetworkItemData, **item_set_opts: bool) -> dict[str, hou.NetworkMovableItem]:
    """
setFromData(data: dict[str, Any], clear_content=False,
force_item_creation=True, parms=True, parmtemplates=True, children=True,
editables=True, skip_notes=False) -> None

    Updates the parameters, options, and contents of this node from
    data, as returned by OpNode.asData().


    data
        The network item data that describes a network item as data.



    force_item_creation
        If this is False and parent has an item with a matching name in
        the data, instead of creating the item, the existing item is
        used.

    parms
        If this is False, do not apply any parameter value stored in the
        data to the node.

    parmtemplates
        If this is False, do not recreate any spare parameters stored in
        the data.

    children
        If this is False, do not recursively recreate any child network
        stored in the data.

    editables
        If this is False, do not recreate the contents of any editable
        dive targets stored in the data.

    skip_notes
        If this is True, do not recreate any sticky notes stored in the
        data.

"""
def parmsAsData(self: hou.OpNode, **parms_opts: _ParmOption | rtypes.ParsingCallback | None) -> rtypes.ParmDataDict:
    """
parmsAsData(values=True, parms=True, default_values=False,
evaluate_values=False, locked=True, brief=True,
multiparm_instances=True, metadata=False, verbose: bool=False) ->
dict[str, Any]

    Returns a JSON-like data structure representing this node's
    parameters.


    values
        If this is True, the capture process saves the values of the
        parameters.

    parms
        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

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
def setParmsFromData(self: hou.OpNode, data: rtypes.ParmDataDict) -> None:
    """
setParmsFromData(data: dict[str, Any]) -> None

    Updates the parameters on this node from data, as returned by
    OpNode.parmsAsData().


    data
        The parm data dictionary that describes a set of parameters as
        data.

"""
def childrenAsData(self: hou.OpNode, **items_opts: _ItemOption | hou.Vector2) -> rtypes.NetworkItemDataDict | None:
    '''
childrenAsData(nodes_only=False, children=True, editables=True,
inputs=True, position=True, flags=True, parms=True,
default_parmvalues=False, evaluate_parmvalues=False,
parms_as_brief=True, parmtemplates="spare_only", metadata=False,
verbose=False) -> dict[str, Any]

    Returns a JSON-like data structure representing the contents of this
    node.


    nodes_only
        If this is True, the capture process only saves nodes, ignoring
        sticky notes, network boxes, and dots.

    children
        If this is False, the capture process only saves the top level
        nodes, ignoring nodes inside subnets and unlocked assets.

    editables
        If this is False, the capture process ignores nodes inside
        editable dive target networks inside assets.

    inputs
        If this is True, the capture process saves input connections.

    position
        If this is True, the capture process saves the node position.

    flags
        If this is True, the capture process saves flag states.

    parms
        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    default_parmvalues
        Normally, when parms is True, the capture process only saves
        parameters with non-default values. If this is True, the capture
        process also saves parameters set to the default value. If the
        parms argument is a list of parameters to capture, this is
        ignored.

    evaluate_parmvalues
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    parms_as_brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    parmtemplates
        If this is "spare_only", the capture process only saves spare
        parameter templates so it can recreate them. This is helpful to
        ensure minimal change to the parameter interface on nodes where
        additional parameters were added. If this is "all", the capture
        process saves template data for all parameters.

    parmfilter
        This captures the settings used for the parameter filter and
        search bar for each node.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

'''
def setChildrenFromData(self: hou.OpNode, data: rtypes.NetworkItemDataDict, **children_set_opts: bool | hou.Vector2) -> dict[str, hou.NetworkMovableItem]:
    """
setChildrenFromData(clear_content=True, force_item_creation=True,
offset_position: hou.Vector2=hou.Vector2(0, 0),
external_connections=True, parms=True, parmtemplates=True, children=True
editables=True, skip_notes=False) -> None

    Replaces or updates the content of this node using data, as returned
    by OpNode.childrenAsData().


    clear_content
        If this is True, the content of parent is destroyed before item
        creation.

    force_item_creation
        If this is False and parent has an item with a matching name in
        the data, instead of creating the item, the existing item is
        used.

    offset_position
        A hou.Vector2 that offsets the position of all items recreated
        by the data.

    external_connections
        The external connections are wires that connect to other
        hou.NetworkMovableItem but were not captured as part of the
        recipe. If this is True, those connections are re-created to
        existing nodes with the same name.

    parms
        If this is False, do not apply any parameter value stored in the
        data to the node.

    parmtemplates
        If this is False, do not recreate any spare parameters stored in
        the data.

    children
        If this is False, do not recursively recreate any child network
        stored in the data.

    editables
        If this is False, do not recreate the contents of any editable
        dive targets stored in the data.

    skip_notes
        If this is True, do not recreate any sticky notes stored in the
        data.

"""
def editablesAsData(self: hou.OpNode, **items_opts: _ItemOption) -> rtypes.NetworkItemDataDict | None:
    '''
editablesAsData(nodes_only=False, children=True, editables=True,
inputs=True, position=True, flags=True, parms=True,
default_parmvalues=False, evaluate_parmvalues=False,
parms_as_brief=True, parmtemplates="spare_only", metadata=False,
verbose=False) -> dict[str, Any]

    Returns a JSON-like data structure representing the contents of any
    editable dive targets inside this node.


    nodes_only
        If this is True, the capture process only saves nodes, ignoring
        sticky notes, network boxes, and dots.

    children
        If this is False, the capture process only saves the top level
        nodes, ignoring nodes inside subnets and unlocked assets.

    editables
        If this is False, the capture process ignores nodes inside
        editable dive target networks inside assets.

    inputs
        If this is True, the capture process saves input connections.

    position
        If this is True, the capture process saves the node position.

    flags
        If this is True, the capture process saves flag states.

    parms
        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    default_parmvalues
        Normally, when parms is True, the capture process only saves
        parameters with non-default values. If this is True, the capture
        process also saves parameters set to the default value. If the
        parms argument is a list of parameters to capture, this is
        ignored.

    evaluate_parmvalues
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    parms_as_brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    parmtemplates
        If this is "spare_only", the capture process only saves spare
        parameter templates so it can recreate them. This is helpful to
        ensure minimal change to the parameter interface on nodes where
        additional parameters were added. If this is "all", the capture
        process saves template data for all parameters.

    parmfilter
        This captures the settings used for the parameter filter and
        search bar for each node.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

'''
def setEditablesFromData(self: hou.OpNode, data: rtypes.NetworkItemDataDict, **editables_set_opts: bool | hou.Vector2) -> dict[str, hou.NetworkMovableItem]:
    """
setEditablesFromData(clear_content=True, force_item_creation=True,
offset_position: hou.Vector2=hou.Vector2(0, 0),
external_connections=True, parms=True, parmtemplates=True, children=True
editables=True, skip_notes=False) -> None

    Replaces or updates the content of any editable dive targets inside
    this node using data, as returned by OpNode.childrenAsData().


    clear_content
        If this is True, the content of parent is destroyed before item
        creation.

    force_item_creation
        If this is False and parent has an item with a matching name in
        the data, instead of creating the item, the existing item is
        used.

    offset_position
        A hou.Vector2 that offsets the position of all items recreated
        by the data.

    external_connections
        The external connections are wires that connect to other
        hou.NetworkMovableItem but were not captured as part of the
        recipe. If this is True, those connections are re-created to
        existing nodes with the same name.

    parms
        If this is False, do not apply any parameter value stored in the
        data to the node.

    parmtemplates
        If this is False, do not recreate any spare parameters stored in
        the data.

    children
        If this is False, do not recursively recreate any child network
        stored in the data.

    editables
        If this is False, do not recreate the contents of any editable
        dive targets stored in the data.

    skip_notes
        If this is True, do not recreate any sticky notes stored in the
        data.

"""
def createDecorationItemsFromData(self: hou.OpNode, data: rtypes.NetworkItemDataDict, target_name_in_data: str, **descendentitems_set_opts: bool | hou.Vector2) -> dict[str, hou.NetworkMovableItem]:
    '''
createDecorationItemsFromData(items: Sequence[hou.NetworkMovableItems],
frame_nodes: Sequence[hou.NetworkMovableItem]=None, selected_nodes:
Sequence[hou.NetworkMovableItem]=None, current_node:
hou.NetworkMovableItem=None, flags: bool=True, nodes_only: bool=False,
target_children: bool=False, children: bool=True, target_editables:
bool=False, editables: bool=True, target_parms: Union[bool,
Sequence[hou.ParmTuple], Sequence[str]]=True, parms: bool=True,
default_parmvalues: bool=False, evaluate_parmvalues: bool=False,
parms_as_brief: bool=True, parmtemplates: str="spare_only", metadata:
bool=False, verbose: bool=False) -> dict[str, Any]

    Create the network items represented by data as decorations with
    this node as the target. See decoration recipes for more
    information.


    items
        A sequence of hou.NetworkMovableItem instances to capture that
        are created when the data is applied.



    flags
        If this is True, the capture process saves flag states.

    nodes_only
        If this is True, the capture process only saves nodes, ignoring
        sticky notes, network boxes, and dots.

    target_children
        Whether to recursively save the contents of the
        target/central/anchor node (if it is a subnetwork or unlocked
        asset).

    children
        If this is False, the capture process only saves the top level
        nodes, ignoring nodes inside subnets and unlocked assets.

    target_editables
        Whether to save the contents of editable dive targets inside the
        target/central/anchor node, if any.

    editables
        If this is False, the capture process ignores nodes inside
        editable dive target networks inside assets.

    target_parms
        Whether to save parameter values on the target/central/anchor
        node, if any.

        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    parms
        If this is True, based on default_parmvalues argument, the
        capture process saves any non-default parameter values or all
        parameter values. If this is False, no parameters are saved.
        Alternatively, to save a custom set of parameter values you can
        specify a list of hou.ParmTuple or hou.Parm instances, or
        strings representing names of parameters to capture.

    default_parmvalues
        Normally, when parms is True, the capture process only saves
        parameters with non-default values. If this is True, the capture
        process also saves parameters set to the default value. If the
        parms argument is a list of parameters to capture, this is
        ignored.

    evaluate_parmvalues
        If this is True, the capture process saves the evaluated value
        of the parameters at the current time (including expanding
        variables in strings), instead of saving expressions and
        keyframe animation.

    parms_as_brief
        Normally, the parm data that stores values for each parameter is
        saved in a compact form where possible. If this is False, it
        stores the parm data with full structure. This option mainly
        exists for debugging. See parm data dict for more information.

    parmtemplates
        If this is "spare_only", the capture process only saves spare
        parameter templates so it can recreate them. This is helpful to
        ensure minimal change to the parameter interface on nodes where
        additional parameters were added. If this is "all", the capture
        process saves template data for all parameters.

    metadata
        If this is True, the capture process saves additional
        information about nodes and parameters.

    verbose
        Normally, the capture process tries to omit and simplify various
        data structures. If this is True, the capture process saves
        everything with full structure. This option mainly exists for
        debugging.

'''
def parmTemplatesAsData(self: hou.OpNode, name: str = '', children: bool = True, **parmtemplates_opts: bool | rtypes.ParsingCallback | None) -> rtypes.ParmTemplateDataDict | None:
    '''
parmTemplatesAsData(name: str = "", children=True,
parmtemplate_order=False) -> dict[str, Any]

    Returns a JSON-like data structure representing the parameter
    template of the named parameter of this node.


    name
        The name of the parameter on this node to save.

    children
        Whether to recursively save the contents of nested parm
        templates.

    parmtemplate_order
        If this is True, an additional ordering_index key is saved for
        each parmtemplate data.

'''
def parmTemplateChildrenAsData(self: hou.OpNode, name: str, **parmtemplates_opts: bool | rtypes.ParsingCallback | None) -> rtypes.ParmTemplateDataDict | None:
    '''
parmTemplateChildrenAsData(name: str = "", parmtemplate_order=False) ->
dict[str, Any]

    Returns a JSON-like data structure representing the child parameter
    templates of the named parameter on this node.


    name
        The name of the parameter with child parameters on this node to
        save.

    parmtemplate_order
        If this is True, an additional ordering_index key is saved for
        each parmtemplate data.

'''
def appendParmTemplatesFromData(self: hou.OpNode, data: rtypes.ParmTemplateDataDict, rename_conflicts: bool = True) -> dict[str, hou.ParmTuple]:
    """
appendParmTemplatesFromData(data: dict[str, Any], rename_conflicts=True)
-> dict[str, hou.parmTuple]

    Creates spare parameters from the data (as returned by
    OpNode.parmTemplatesAsData()), and adds them to this node after
    existing parameters. Returns a dictionary that maps the names in the
    data to the created hou.ParmTuple objects.


    data
        The parm templates data dictionary that describes a sequence of
        parameter templates as data.

    rename_conflicts
        Whether to rename the newly created parm templates when they
        conflict with existing templates.

"""
def replaceParmTemplatesFromData(self: hou.OpNode, data: rtypes.ParmTemplateDataDict) -> dict[str, hou.ParmTuple]:
    """
replaceParmTemplatesFromData(data: dict[str, Any]) -> dict[str,
hou.parmTuple]

    Creates spare parameters from the data (as returned by
    OpNode.parmTemplatesAsData()), and replaces any existing parameters
    with the same names on this node. Returns a dictionary that maps the
    names in the data to the created hou.ParmTuple objects.


    data
        The parm templates data dictionary that describes a sequence of
        parameter templates as data.

"""
def insertParmTemplatesBeforeFromData(self: hou.OpNode, data: rtypes.ParmTemplateDataDict, parm_name: str, rename_conflicts: bool = True) -> dict[str, hou.ParmTuple]:
    """
insertParmTemplatesBeforeFromData(data: dict[str, Any], parm_name: str,
rename_conflicts=True) -> dict[str, hou.parmTuple]

    Creates spare parameters from the data (as returned by
    OpNode.parmTemplatesAsData()), and inserts them before the parameter
    named <parm_name>. Returns a dictionary that maps the names in the
    data to the created hou.ParmTuple objects.


    data
        The parm templates data dictionary that describes a sequence of
        parameter templates as data.

    parm_name
        The name of the parameter before which to insert the parm
        templates from data.

    rename_conflicts
        Whether to rename the newly created parm templates when they
        conflict with existing templates.

"""
def insertParmTemplatesAfterFromData(self: hou.OpNode, data: rtypes.ParmTemplateDataDict, parm_name: str, rename_conflicts: bool = True) -> dict[str, hou.ParmTuple]:
    """
insertParmTemplatesAfterFromData(data: dict[str, Any], parm_name: str,
rename_conflicts=True) -> dict[str, hou.parmTuple]

    Creates spare parameters from the data (as returned by
    OpNode.parmTemplatesAsData()), and inserts them after the parameter
    named <parm_name>. Returns a dictionary that maps the names in the
    data to the created hou.ParmTuple objects.


    data
        The parm templates data dictionary that describes a sequence of
        parameter templates as data.

    parm_name
        The name of the parameter after which to insert the parm
        templates from data.

    rename_conflicts
        Whether to rename the newly created parm templates when they
        conflict with existing templates.

"""
def appendParmTemplatesToFolderFromData(self: hou.OpNode, data: rtypes.ParmTemplateDataDict, parm_name: str, rename_conflicts: bool = True) -> dict[str, hou.ParmTuple]:
    """
appendParmTemplatesToFolderFromData(data: dict[str, Any], parm_name:
str, rename_conflicts=True) -> dict[str, hou.parmTuple]

    Creates spare parameters from the data (as returned by
    OpNode.parmTemplatesAsData()), and inserts them at the end of the
    folder named <parm_name>. Returns a dictionary that maps the names
    in the data to the created hou.ParmTuple objects.


    data
        The parm templates data dictionary that describes a sequence of
        parameter templates as data.

    parm_name
        The name of the folder parameter in which to insert the parm
        templates from data.

    rename_conflicts
        Whether to rename the newly created parm templates when they
        conflict with existing templates.

"""
def prependParmTemplatesToFolderFromData(self: hou.OpNode, data: rtypes.ParmTemplateDataDict, parm_name: str, rename_conflicts: bool = True) -> dict[str, hou.ParmTuple]:
    """
prependParmTemplatesToFolderFromData(data: dict[str, Any], parm_name:
str, rename_conflicts=True) -> dict[str, hou.parmTuple]

    Creates spare parameters from the data (as returned by
    OpNode.parmTemplatesAsData()), and inserts at the start of the
    folder named <parm_name>. Returns a dictionary that maps the names
    in the data to the created hou.ParmTuple objects.


    data
        The parm templates data dictionary that describes a sequence of
        parameter templates as data.

    parm_name
        The name of the folder parameter in which to insert the parm
        templates from data.

    rename_conflicts
        Whether to rename the newly created parm templates when they
        conflict with existing templates.

"""
def inputsAsData(self: hou.OpNode | hou.OpIndirectInput | hou.NetworkDot, ignore_network_dots: bool = False, ignore_subnet_indirect_inputs: bool = False, use_names: bool = False) -> rtypes.NetworkItemInputDataList:
    """
inputsAsData(ignore_network_dots=False,
ignore_subnet_indirect_inputs=False, use_names=False) ->
Sequence[dict[str, Any]]

    Returns a JSON-like data structure representing this node's input
    connections.


    ignore_network_dots
        If this is True, hou.NetworkDot items will be ignored.

    ignore_subnet_indirect_inputs
        If this is True, hou.SubnetIndirectInput items will be ignored.

    use_names
        Whether to return the index or the name for the connections.

"""
def outputsAsData(self: hou.OpNode | hou.OpIndirectInput | hou.NetworkDot, ignore_network_dots: bool = False, use_names: bool = False) -> rtypes.NetworkItemOutputDataList:
    """
outputsAsData(ignore_network_dots=False,
ignore_subnet_indirect_inputs=False, use_names=False) ->
Sequence[dict[str, Any]]

    Returns a JSON-like data structure representing this node's output
    connections.


    ignore_network_dots
        If this is True, hou.NetworkDot items will be ignored.

    ignore_subnet_indirect_inputs
        If this is True, hou.SubnetIndirectInput items will be ignored.

    use_names
        Whether to return the index or the name for the connections.

"""
def setInputsFromData(self: hou.OpNode | hou.OpIndirectInput | hou.NetworkDot, data: rtypes.NetworkItemInputDataList) -> None:
    """
setInputsFromData(data: dict[str, Any]) -> None

    Creates input wires on this node from data, as returned by
    OpNode.inputsAsData().


    data
        The input connection data that describes a sequence of
        connections.

"""
def setOutputsFromData(self: hou.OpNode | hou.OpIndirectInput | hou.NetworkDot, data: rtypes.NetworkItemOutputDataList) -> None:
    """
setOutputsFromData(data: dict[str, Any]) -> None

    Creates output wires on this node from data, as returned by
    OpNode.inputsAsData().


    data
        The output connection data that describes a sequence of
        connections.

"""
def inputsWithIndices(self: hou.Node | hou.NetworkDot, ignore_network_dots: bool = False, ignore_subnet_indirect_inputs: bool = False, use_names: bool = False) -> list[tuple[hou.NetworkMovableItem, int | str, int | str]]:
    """
inputsWithIndices(ignore_network_dots=False,
ignore_subnet_indirect_inputs=False, use_names=False) ->
Sequence[hou.OpNode, int | str, int | str]]

    Returns a sequence of tuples representing each connected input of
    this node, where each tuple has three items:

  * A hou.OpNode instance representing the node connected to this input.

  * An int representing the index (or a string representing the internal
    name, depending on the use_names argument) of the upstream node's
    output that is connected to this input.

  * An int representing the index (or a string representing the internal
    name, depending on the use_names argument) of this input.


    ignore_network_dots
        Ignore any network dots connected to each input and return the
        nearest upstream node instead.

    ignore_subnet_indirect_inputs
        If an input is connected to a subnet input, return the node
        connected to the subnet in the parent network instead of the
        subnet input pseudo-node.

    use_names
        Return the internal names of the connections instead of their
        indices.

"""
def outputsWithIndices(self: hou.Node | hou.NetworkDot, ignore_network_dots: bool = False, use_names: bool = False) -> list[tuple[hou.NetworkMovableItem, int | str, int | str]]:
    """
outputsWithIndices(ignore_network_dots=False, use_names=False) ->
Sequence[hou.OpNode, int | str, int | str]]

    Returns a sequence of tuples representing each connected output of
    this node, where each tuple has three items:

  * A hou.OpNode instance representing the node connected to this
    output.

  * An int representing the index (or a string representing the internal
    name, depending on the use_names argument) of the output.

  * An int representing the index (or a string representing the internal
    name, depending on the use_names argument) of the downstream node's
    input that is connected to this input.


    ignore_network_dots
        Ignore any network dots connected to each input and return the
        nearest upstream node instead.

    use_names
        Return the internal names of the connections instead of their
        indices.

"""
