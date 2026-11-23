import _pdg
import hou
from .node import PyNode as PyNode

class PyMapper(PyNode):
    """
    Base mapper implementation
    """
    def __init__(self, node: _pdg.Node) -> None:
        """
        __init__(self, _pdg.Node) -> NoneType

        Initializes the mapper with a C++ node reference
        """

def saveToPython(node: hou.OpNode, classname: str = '', description: str = '', file_path: str = '', tab_submenu: str = 'Custom') -> None: ...
