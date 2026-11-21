import _pdg
import hou

class PyMapper:
    def __init__(self, node: _pdg.Node) -> None: ...

def saveToPython(
    node: hou.OpNode,
    classname: str = ...,
    description: str = ...,
    file_path: str = ...,
    tab_submenu: str = ...,
) -> None: ...
