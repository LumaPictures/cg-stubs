# Houdini stubs generated from Houdini 22.0.466

import hou
from houtypes import ParmCallbackKwargs
from typing import Sequence

def setOutputVolumesFromGeometry(node: hou.CopNode, prim_type: hou.EnumValue[hou.primType] = ...) -> None:
    """
    Sets Geometry To Layer COP's outputs from the input's volumes
    and VDBs.
    """
def setOutputVolumesFromDeep(node: hou.CopNode) -> None:
    """
    Helper function for Flatten Deep COP to set outputs
    based on incoming point attributes    

    To function Flatten Deep needs ix, iy, Z, ZBack, GS_Alpha
    however ix and iy can't be imported at the moment
    Bug ?

    This function first gets a valid list of attributes
    then loops through that list to set the imports
    
    """
def setCameraParmsFromLayer(node: hou.CopNode) -> None:
    """
    Set the parameters on the Camera COP based on the incoming layer    
    """
def setNamesFromInputs(node: hou.CopNode, parmname: str, multiparmindex: int) -> None:
    """
    Populates Cable Pack COP fields with input labels    
    """
def getInputIndex(node: hou.OpNode, input_index_or_name: int | str) -> int: ...
def getOutputIndex(node: hou.OpNode, output_index_or_name: int | str) -> int: ...
def getInputConnector(node: hou.OpNode, input_index_or_name: int | str) -> hou.NodeConnection | None:
    """
    Returns the hou.NodeConnection for the node's input.
    Returns None if the input is unconnected.
    Raises an error if the input does not exist.
    """
def getInputData(node: hou.CopNode, input_index_or_name: int | str) -> hou.ImageLayer | hou.NanoVDB | hou.DetachedAttrib | hou.Geometry | None:
    """
    Returns the node's input data.
    Returns None if the port is unconnected.
    Raises an error if the input does not exist.
    """
def getInputCable(node: hou.CopNode, index_or_name: int | str) -> hou.CopCable | None: ...
def computeInputRange(node: hou.CopNode, input_index_or_name: int | str, channels: int | Sequence[int] | None = None) -> tuple[float, float]:
    """
    Returns the input's range over the given channel(s) as a tuple: (min, max).
    If the channel list is None, all input channels are used.
    Returns (0, 1) if the input is unconnected, or if the input has none of the
    the requested channels. 
    Raises an error if the input port does not exist.
    """
def computeInputLengthRange(node: hou.CopNode, input_index_or_name: int | str) -> tuple[float, float]:
    """
    Returns the input's range over the given channel(s) as a tuple: (min, max).
    The length of each pixel/voxel/element is computed to determine
    range.
    Raises an error if the input port does not exist.
    """
def computeMaskedInputRange(node: hou.CopNode, input_index_or_name: int | str, rgba_mask: int = 15) -> tuple[float, float]:
    """
    Returns the input's range over the given rgba mask as a tuple: (min, max).
    To include the i-th channel, the i-th bit must be set in the provided mask.
    Returns (0, 1) if the input is unconnected, or if the input has none of the
    the requested channels. Raises an error if the input port does not exist.
    """
def getPropertiesAsStringMenu(data_holder: hou.ImageLayer | hou.NanoVDB | hou.DetachedAttrib | None) -> list[str]: ...
def getInputCableNames(node: hou.CopNode | None, index: int = 0) -> list[str]: ...
def getAdjacencyGeometry(node: hou.CopNode, index: int) -> hou.Geometry | None: ...
def getAdjacencyGeometryAttributes(node: hou.CopNode | None, index: int = 0) -> list[str]: ...
def setAttributeFromMiniMenu(kwargs: ParmCallbackKwargs) -> None:
    """
    Used with mini menus on :
    adjacency attrib sample
    geoattribfromlayer
    attribextract

    kwargs needs to contain the 'attribute' key to set the parm correctly

    this also looks for parms on the node: class and outtype
    if the minimenu is in a multiparm then the multiparm index is automatically
    appended
    """
