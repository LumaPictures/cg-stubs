import apex
import hou

DEBUGGRAPHPATH_PARM: str
DEBUGPARMS_ATTRIB: str
DEBUGPARMS_NODE: str
DEBUGPARMSTRIGGER_NODE: str
DEBUGGRAPH_NODE: str

def findActiveSceneViewers(node: hou.OpNode) -> list[hou.SceneViewer]:
    """Returns the scene viewers of node with an active animate state."""
def getRigDebugParms(node: hou.OpNode) -> apex.Dict:
    """Returns the debug parms of the rig selected in node's animate state."""
