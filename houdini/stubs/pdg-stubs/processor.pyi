# Houdini stubs generated from Houdini 22.0.466

import _pdg
import hou
import logging
from .node import PyNode as PyNode

logger: logging.Logger

class PyProcessor(PyNode):
    """
    Base processor implementation
    """
    def __init__(self, node: _pdg.Node) -> None:
        """
        __init__(self, _pdg.Node) -> NoneType

        Initializes the processor with a C++ node reference
        """

def saveToPython(node: hou.OpNode, classname: str = '', description: str = '', file_path: str = '', tab_submenu: str = 'Custom') -> None: ...
