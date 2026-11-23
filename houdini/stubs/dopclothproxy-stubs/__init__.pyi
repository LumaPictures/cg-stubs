import hou
from houtypes import ShelfToolKwargs

def findOptimalRadius(high_res: hou.ObjNode, low_res: hou.ObjNode) -> float: ...
def selectAndCreateCustomizedClothObjectsWithProxy(scriptargs: ShelfToolKwargs) -> hou.OpNode | None:
    """ For a selection of objects to render and a selection of
    objects to use as proxies for physics simulation, ensure that
    corresponding DOP Cloth Objects with a specific behaviour exist.
    """
def selectAndEmbedHighresObject(scriptargs: ShelfToolKwargs, behavior: str) -> hou.OpNode | None:
    """ Embed geometry into a simulated
    """
