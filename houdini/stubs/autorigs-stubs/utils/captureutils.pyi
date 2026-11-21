import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset

AUTORIGS_NODEGROUPS: str
SOLIDEMBED: str
SOLIDCONFORM: str
EMBED_OUT: str
GEO_OUT: str
BIHARMONIC: str
GROUP_DELETE: str
CAPTURE_BOUNDS: str
CAPTURE_CORRECT: str
CAPTURE_BOUNDS_GROUP: str
CAPTURE_BOUNDS_MERGE: str
CAPTURE_OVERRIDE: str
STASH: str
DEFORM: str

def findOrCreateNode_(parent: hou.OpNode, node_type: str, node_name: str) -> tuple[hou.OpNode, bool]: ...
def createCapture_(capture_type: int, parent: hou.OpNode, geo_input: hou.OpNode, deform: hou.OpNode, stash: hou.OpNode, asset: hou.OpNode) -> hou.OpNode: ...
def buildCapture(autorigs_asset: AutoRigsAsset, bonecapture_postfix: str = '', bonegroup: hou.NodeGroup | None = None) -> None: ...
def cookCaptureNetwork(autorigs_asset: AutoRigsAsset) -> None:
    """Cook the capture network by turning on deform"""
def addAutoRigNodeGroupsParm(capture: hou.OpNode, region_parm_name: str, expr: str) -> None:
    """
    Adds a new parm for storing autorigs nodegroups, and drive the given parm with expression
    capture: (hou.Node) the capture node to add a new parm template,
    region_parm_name: (str) the parm name that will be driven by expression,
    expr: (str) the expression to drive
    """
def addBoneGroupToParm(node: hou.OpNode, bonegroup: hou.NodeGroup) -> None:
    """
    Adds the bonegroup to the AutoRigs Node Groups Parameter
    node: the capture node to edit
    bonegroup: the node group to add to the parm
    """
def deleteGroup(geoobj: hou.OpNode, group: str) -> None:
    """
    Deletes the specified group from the geoobj.
    geoobj: (hou.Node) the geometry from which to delete the group,
    group: (str) the group to delete
    """
def overrideCaptureRegion(parent: hou.OpNode, capture_geo: hou.ObjNode, bonegroup: hou.NodeGroup) -> None:
    """
    Overrides the capture region using the same capture override path.
    parent: (hou.Node) the node where the capture network resides,
    capture_geo: (hou.ObjNode) the node that defines the bounding region,
    bonegroup: (hou.NodeGroup) the nodegroup that contains the bones of interest
    """
def createFalloffOverride(geo_obj: hou.OpNode, prefix: str, curve_geo: hou.OpNode, bonegroup: hou.NodeGroup, embed_out: hou.OpNode | None = None, exclude_group: str | None = None) -> None: ...
