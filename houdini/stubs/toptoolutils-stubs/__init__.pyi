import hou
from houtypes import ShelfToolKwargs

def genericTool(scriptargs: ShelfToolKwargs, nodetypename: str, nodename: str | None = None, exact_node_type: bool = True) -> hou.OpNode:
    """ Calls the generic tool handler for all nodes, which allows the
        user to lay down a node in the network editor. If no network editor
        pane is specified, use the first one found
    """
def getTopnet() -> hou.TopNode: ...
def getLastTopnet() -> hou.TopNode: ...
def getCamera(createCamera: bool = False) -> hou.ObjNode | None: ...
def overlaytextTool(kwargs: ShelfToolKwargs) -> None:
    """ Creates a ROP Composite setup to do a simple text overlay
        on the incoming work item
    """
def generatorCommandTool(kwargs: ShelfToolKwargs, idx: int) -> None:
    """ Creates a Generic Generator setup to perform
        various USD command line functions
    """
def buildBlockPair(scriptargs: ShelfToolKwargs, name: str, begintype: str, endtype: str) -> tuple[hou.OpNode, hou.OpNode]:
    """ Builds a pair of block nodes, a begin and an end, and links
        them together nicely.
    """
def buildWedgeGeo(scriptargs: ShelfToolKwargs) -> None: ...
def buildRenderSetup(scriptargs: ShelfToolKwargs) -> None: ...
def installCheckTool(kwargs: ShelfToolKwargs) -> None: ...
def convertImagesTool(kwargs: ShelfToolKwargs) -> None: ...
def outputFileTool(kwargs: ShelfToolKwargs) -> None: ...
