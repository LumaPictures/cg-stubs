import hou

def boundmode() -> int:
    """
    Returns the GasResizeDynamic bound mode.
    """
def boundobject(bsop: hou.OpNode | None) -> hou.SopNode | hou.DopNode | None:
    """
    function returning SOP node based on user defined selection > object or geometry.
    """
def currentbounds(type: str = 'min') -> hou.Vector3:
    """
    compute bound information first input
    """
def evalnodeparm(node: hou.OpNode, parmname: str) -> hou.OpNode | None:
    '''" Evaluates the given parm on the node, and then looks up
         the node that the parm is pointing to, being sure to
         do a relative lookup.
    '''
def objectbounds(type: str = 'min') -> list[float] | hou.Vector3:
    """
    Function Returns Minimum and Maximum Bounds based on the selected clamp method
    Initialized values are (-1 1). If conditions are met the new bounds are calculated and used
    """
def compensation(type: str = 'min') -> list[float]:
    """
    compute bound compensation if object is not voxel centered
    """
