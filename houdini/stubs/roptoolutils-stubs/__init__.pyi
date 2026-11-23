import hou

def createRenderNode(rop_type: str = 'ifd', exact_type_name: bool = True) -> hou.RopNode:
    """ Create a render node in /out. 
    
        By default, create a standard Mantra output driver.
    """
