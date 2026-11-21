import hou
from .. import rtypes as rtypes
from collections.abc import Collection

def portNameToIndex(item: hou.NetworkMovableItem, name: str | int, port_type: str = 'in') -> int | None:
    """
    Converts a named input/output into index. If name is already an integer index, it returns it unchanged.
    """
def setParmInputName(item: hou.OpNode, idx: int, input_name: str, input_parm_name: str | None = None) -> None:
    """Sets the input paramater of a node at idx to input_parm_name if given, otherwise to input_name.
    """
def isVopNode(item: hou.NetworkMovableItem) -> bool | None: ...
def isCopNode(item: hou.NetworkMovableItem) -> bool | None: ...
def areInputsAsNeeded(node: hou.Node) -> bool | None:
    """
    Checks if a node's (Vop) last input ends with 'next'.
    """
def shouldSaveWithName(item: hou.NetworkMovableItem) -> bool:
    """
    When working with Vop nodes, we should be saving the input/output names rather than indexes.
    This method decided if this is the case.
    """
def inputsWithIndices(item: hou.NetworkMovableItem, ignore_network_dots: bool = True, ignore_subnet_indirect_inputs: bool = True, use_names: bool = False, names_as_label: bool = False) -> list[tuple[hou.NetworkMovableItem, int | str, int | str]]:
    """
    Returns a list of tuples with information about the node's inputs, including the input item,
    the source and destination indexes/names.

    This is for the extension of hou.Node HOM module, as there is no hou.Node function that would provide
    all this information with options to ignore/consider network dots or subnet indirect inputs.
    """
def outputsWithIndices(item: hou.NetworkMovableItem, ignore_network_dots: bool = False, use_names: bool = False, names_as_label: bool = False) -> list[tuple[hou.NetworkMovableItem, int | str, int | str]]:
    """
    Returns a list of tuples with information about the node's outputs, including the output item,
    the source and destination indexes/names.

    This is for the extension of hou.Node HOM module, as there is no hou.Node function that would provide
    all this information with options to ignore/consider network dots or subnet indirect inputs.
    """
def inputsAsData(item: hou.NetworkMovableItem, ignore_network_dots: bool = False, ignore_subnet_indirect_inputs: bool = False, use_names: bool = False, names_as_label: bool = False) -> rtypes.NetworkItemInputDataList:
    """
    Gets the inputs as data strucutre for the given item.
    """
def outputsAsData(item: hou.NetworkMovableItem, ignore_network_dots: bool = False, use_names: bool = False, names_as_label: bool = False) -> rtypes.NetworkItemOutputDataList:
    """
    Gets the outputs as data structure for the given item.
    """
def setInputFromData(item: hou.NetworkMovableItem | None, data: rtypes.NetworkItemInputData, input_parm_name: str | None = None) -> bool | None:
    """Handles setting inputs from a given input data.

    """
def setInputsFromData(item: hou.NetworkMovableItem, data: rtypes.NetworkItemInputDataList, allowed_names: Collection[str] | None = None) -> None: ...
def setOutputFromData(item: hou.NetworkMovableItem, data: rtypes.NetworkItemOutputData) -> None: ...
def setOutputsFromData(item: hou.NetworkMovableItem, data: rtypes.NetworkItemOutputDataList, allowed_names: Collection[str] | None = None) -> None: ...
def _connectionData(input_or_output_data: rtypes.NetworkItemInputData | rtypes.NetworkItemOutputData, node_name: str, allowed_names: Collection[str] | None = ...) -> rtypes.ConnectionData | None: ...
def _connectionDataFromInputsOutputsData(input_or_output_data: rtypes.NetworkItemInputDataList | rtypes.NetworkItemOutputDataList, node_name: str, allowed_names: Collection[str] | None = ...) -> rtypes.ConnectionDataList: ...
def _connectionsForItemsData(items_dict_data: rtypes.NetworkItemDataDict, allowed_names: Collection[str] | None = ...) -> rtypes.ConnectionDataList: ...
def _inputDataIndex(input_data_list: rtypes.NetworkItemInputDataList, input_name: int | str) -> int | None:
    """Finds the index of the input data in a list of input data dictionaries,
    in which the 'to_index' key is matching 'input_name'.
    """
def lookupParameterInputName(items_dict_data: rtypes.NetworkItemDataDict, item_name: str, input_name: int | str, filter_types: Collection[str] = ...) -> str | None:
    """Finds the name of the input as it would be set on the multiparm instance.
    """
def setVopInputsFromData(items_dict_data: rtypes.NetworkItemDataDict, container: hou.Node, allowed_names: Collection[str] | None = ...) -> None:
    """
    This is kinda silly, but necessary for VOPs where inputs and even
    outputs can be dynamic: if any wiring's succeeded, keep looping over
    the failures, because the successes might have created the needed
    ports, until there are no successes, or no failures
    wires = connectionsForItemsData(items_dict_data)

    Some nodes like VOP/snippet and VOP/null use a hidden multiparm parm used to set the name of each input/output by the user.
    This only becomes visible when at least one input is connected.

    By the point when this function is called, the parameters of nodes are set. For VOP/snippet, it means that 'namesnum'
    multiparm, and its instance parameters are set to the expected input names. This puts the VOP/snippet in a 'limbo' state
    as the input handles do not yet exist.

    And this is where we have a major flaw in the current VOP design:
    As soon as a connection is made to a VOP/snippet in this limbo state, the multiparm instances are cleared, and we lose
    all of our input names.

    Further complicates things when connections cannot be made in the same order as declared by the multiparm.
    In which case, there will be a mismatch between the already set input names and their input connection.

    Therefore, with lookupParameterInputName(), we can search and find the name of the input (in the data) that has to be
    set on the multiparm for a given input connection.

    This name then can be passed to the setInputFromData(), which will also set the name of the input on the multiparm.
    """
