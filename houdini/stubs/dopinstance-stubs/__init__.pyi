# Houdini stubs generated from Houdini 22.0.466

import hou

def pathcheck(parm: hou.Parm, node: hou.OpNode) -> hou.OpNode | None:
    """
    Function evaluates a path bound to a parameter and returns the node if found
    Otherwise None
    """
def defaults(hda: hou.OpNode = ..., attrib: str = 'scale') -> tuple[float, float, float] | list[float]:
    """
    Retrieves Fluid or Smoke object defaults, defined by the node
    Default is scale.
    """
def containersize(hda: hou.OpNode = ..., index: int = 0, attrib: str = 'scale') -> float:
    """ 
    If Instancing is enabled, fetch the point geometry of the object to instance containers on,
    Get the Current Point to Fetch Position and Size and apply these settings to the container
    Otherwise use Asset Defined values
    """
def objectactivation(hda: hou.OpNode = ...) -> int:
    """
    If Instancing is enabled and continuous, create object relative to available points that frame,
    If Instancing is enabled but not continuous, create objects for points available at creation frame
    Otherwise use Asset Defined values
    """
def objectcount(hda: hou.OpNode = ...) -> int:
    """ 
    If Instancing is enabled, number of objects = number of available points,
    Else objects = asset defined values
    """
def objectname(hda: hou.OpNode = ...) -> str:
    """
    If Instancing is enabled, set name using objectname + objid
    """
