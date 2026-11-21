import hou
from . import rigutils as rigutils

def createFKControls(prefix: str, startbone: hou.ObjNode, endbone: hou.ObjNode) -> list[hou.ObjNode]:
    """ Creates FK controls for each bone from start bone to end bone with the name
        prefix + fkcontrol
    """
