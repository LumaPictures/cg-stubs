import hou
from typing import Never

def getBlendShapeChannels(geo: hou.Geometry | None, force_variablename: bool = False) -> list[str]:
    """
    Returns an array with the string of each blend shape channel in the geometry.
    """
def getBlendShapeNames(geo: hou.Geometry | None) -> list[str]:
    """
    Returns an array with the string of each blend shape name in the geometry.
    """
def getBlendShapeInBetweenNames(geo: hou.Geometry | None) -> list[str]:
    """
    Returns an array with the string of each blend shape in between name in the geometry.
    """
def getBlendShapeChannelsFromSkeleton(geo: hou.Geometry | None, read_clipchannels_only: bool = False) -> list[str] | tuple[str, ...]:
    """
    Returns an array with the string of each blend shape channel under the clipchannels detail attribute (normally found on the skeleton).
    If no clipchannels attrib exists, it returns a list with all detail float attributes, if read_clipchannels_only is set to False.
    """
def generateBlendShapeMenu(node: hou.SopNode, inputindex: int = 0, force_variablename: bool = False, use_channels: bool = False, duplicate_names: bool = True) -> list[str]:
    """
    Returns a sorted menu (string array) featuring all blend shape names found on the node's inputindex geometry.
    """
def generateBlendShapeInBetweenMenu(node: hou.SopNode, inputindex: int = 0) -> list[str]:
    """
    Returns a sorted menu (string array) featuring all blend shape in between names found on the node's inputindex geometry.
    """
def selectBlendShape(node: hou.SopNode, parmtuple: hou.ParmTuple, inputindex: int = 0, exclusive: bool = True) -> dict[str, Never] | None:
    """
    Open a tree chooser to select a blendshape name.
    """
def selectBlendShapeInBetween(node: hou.SopNode, parmtuple: hou.ParmTuple, inputindex: int = 0, exclusive: bool = True) -> dict[str, Never] | None:
    """
    Open a tree chooser to select a blendshape in between name.
    """
