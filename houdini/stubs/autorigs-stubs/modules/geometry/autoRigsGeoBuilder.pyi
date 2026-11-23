import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.base.autoRigsBaseBuilder import AutoRigsBaseBuilder as AutoRigsBaseBuilder
from autorigs.modules.geometry.buildGeometryGuide import GeometryGuide as GeometryGuide
from autorigs.utils import captureutils as captureutils, geometryutils as geometryutils

class AutoRigsGeoBuilder:
    autorigs_asset: AutoRigsAsset
    assetnode: hou.ObjNode
    buildguide: GeometryGuide
    geoskin: hou.ObjNode | None
    geo_out: hou.SopNode | None
    embed_out: hou.SopNode | None
    geo_obj: hou.SopNode
    group_delete: hou.SopNode
    deform: hou.SopNode
    stash: hou.SopNode
    capture: hou.SopNode
    GEO_FILE_NAME_POSTFIX: str
    SOLIDEMBED: str
    SOLIDCONFORM: str
    BIHARMONIC: str
    STASH: str
    DEFORM: str
    def __init__(self, autorigs_asset: AutoRigsAsset, buildguide: GeometryGuide) -> None: ...
    def placeGeometry(self) -> None: ...
    def setGeoObj(self, node: hou.SopNode) -> None: ...
    def getGeoObj(self) -> hou.SopNode: ...
    def getGeoSkin(self) -> hou.ObjNode | None: ...
    def buildCapture(self) -> None: ...
    def addAutoRigNodeGroupsParm(self, region_parm_name: str, expr: str) -> None: ...
    def addBoneGroup(self, bonegroup: hou.NodeGroup) -> None: ...
    def createFalloffOverride(self, prefix: str, curve_geo: hou.OpNode, bonegroup: hou.NodeGroup) -> None: ...
    def cookCaptureNetwork(self) -> None:
        """Cook the capture network by turning on deform"""
    def deleteGroup(self, group: str) -> None: ...
