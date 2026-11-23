import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset

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
def createCapture_(
    capture_type: int, parent: hou.OpNode, geo_input: hou.OpNode, deform: hou.OpNode, stash: hou.OpNode, asset: hou.OpNode
) -> hou.OpNode: ...
def buildCapture(autorigs_asset: AutoRigsAsset, bonecapture_postfix: str = ..., bonegroup: hou.NodeGroup | None = ...) -> None: ...
def cookCaptureNetwork(autorigs_asset: AutoRigsAsset) -> None: ...
def addAutoRigNodeGroupsParm(capture: hou.OpNode, region_parm_name: str, expr: str) -> None: ...
def addBoneGroupToParm(node: hou.OpNode, bonegroup: hou.NodeGroup) -> None: ...
def deleteGroup(geoobj: hou.OpNode, group: str) -> None: ...
def overrideCaptureRegion(parent: hou.OpNode, capture_geo: hou.ObjNode, bonegroup: hou.NodeGroup) -> None: ...
def createFalloffOverride(
    geo_obj: hou.OpNode,
    prefix: str,
    curve_geo: hou.OpNode,
    bonegroup: hou.NodeGroup,
    embed_out: hou.OpNode | None = ...,
    exclude_group: str | None = ...,
) -> None: ...
