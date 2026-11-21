# Houdini stubs generated from Houdini 22.0.466

import hou
from . import rigutils as rigutils
from collections.abc import Sequence

def createFKControls(nameslist: Sequence[str], startbone: hou.ObjNode, endbone: hou.ObjNode, inchain: bool = False) -> list[hou.ObjNode]:
    """ Creates FK controls for each bone from start bone to end bone with the name
        prefix + 'fkcontrol'

        required type:
        nameslist should be in reverse order of the bone chain
        inchain specifies whether the fk controls should be part of the bone chain or off to the side
    """
