import collections
import hou
import typing
from autorigs.modules.base import buildBaseGuide as buildBaseGuide
from autorigs.utils.buildGuideHelper import _GuideNames
from collections.abc import Mapping, Sequence
from typing import Literal, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_GuideData: TypeAlias = tuple[hou.ObjNode, bool, bool]
_EyelidGuides: TypeAlias = dict[str, _GuideData]
_GuideNodesData: TypeAlias = dict[str, _GuideData | _EyelidGuides]
_EyelidName: TypeAlias = Literal['eyelid_center', 'eyelid_inner', 'eyelid_outer']
_NodeGuideName: TypeAlias = Literal['eyesroot', 'eyeroot', 'lookat_guidecurve', 'eyelid_captureline', 'master_lookat', 'capture_guide', 'eyelid_guide', 'lookat_root', 'lookat']
class _EyeGuideNamesJson(TypedDict):
    eyesroot: str
    eyeroot: str
    lookat_guidecurve: str
    eyelid_captureline: str
    master_lookat: str
    capture_guide: str
    eyelid_guide: str
    lookat_root: str
    lookat: str
    eyelid_center: Mapping[str, str]
    eyelid_inner: Mapping[str, str]
    eyelid_outer: Mapping[str, str]

class _EyeGuideJson(TypedDict):
    guidenames: _EyeGuideNamesJson
    mirror_guidenames: _EyeGuideNamesJson

class EyeGuide(buildBaseGuide.BaseGuide[collections.OrderedDict[str, _GuideNames]]):
    assetnode: hou.ObjNode
    mirror: bool
    guidenodesdata: _GuideNodesData
    mguidenodesdata: _GuideNodesData
    EYES_ROOT: Literal['eyesroot']
    EYE_ROOT: Literal['eyeroot']
    LOOKAT_GUIDECURVE: Literal['lookat_guidecurve']
    EYELID_CAPTURELINE: Literal['eyelid_captureline']
    MASTER_LOOKAT: Literal['master_lookat']
    CAPTURE_GUIDE: Literal['capture_guide']
    EYELID_CENTER: Literal['eyelid_center']
    EYELID_INNER: Literal['eyelid_inner']
    EYELID_OUTER: Literal['eyelid_outer']
    GUIDE_CURVE: str
    CLOSED_GUIDE: str
    OPENED_TOP: str
    OPENED_BOT: str
    UPPERLID: str
    LOWERLID: str
    EYELID_GUIDE: Literal['eyelid_guide']
    EYELID_CLOSE_COLOR: tuple[int, int, int]
    EYELID_OPEN_COLOR: tuple[int, int, int]
    EYELID_CAPTURE_COLOR: tuple[int, int, int]
    LOOKAT_ROOT: Literal['lookat_root']
    LOOKAT: Literal['lookat']
    SIDE_LEFT: int
    SIDE_RIGHT: int
    SIDE_DEFAULT: int
    DEFAULT_CENTER_RANGE: tuple[int, int]
    DEFAULT_INNER_RANGE: tuple[int, int]
    DEFAULT_OUTER_RANGE: tuple[int, int]
    RX_DRIVER: str
    def __init__(self, assetnode: hou.ObjNode) -> None: ...
    def buildFromJsonNew(self, json: _EyeGuideJson, parent: hou.ObjNode | None = None) -> _GuideNodesData: ...
    def buildEyelidGuides(self, gdn: Mapping[str, str], mgdn: Mapping[str, str], parent: hou.ObjNode, mirror_parent: hou.ObjNode, curve_range: tuple[int, int]) -> tuple[_EyelidGuides, _EyelidGuides]:
        """Build the eyelid guides for one position (i.e. inner, center, outer)
        gdn: guidenodesdata
        mgdn: mirror_guidendoesdata
        parent: parent for main
        mirror_parent: parent for mirror
        curve_range: the range for the guide curve to rotate (about y)
        """
    def buildFromJsonExisting(self, json: _EyeGuideJson) -> _GuideNodesData: ...
    def buildEyelidGuidesFromExisting(self, gdn: Mapping[str, str]) -> _EyelidGuides: ...
    def createCaptureGuide(self, gdn: _EyeGuideNamesJson) -> hou.ObjNode:
        """Creates the capture region guide for the eye"""
    def createEyelidCaptureLines(self, gdn: _EyeGuideNamesJson, eye_root: hou.ObjNode, eyelid_guides: Sequence[hou.ObjNode]) -> hou.ObjNode:
        """Creates the capture lines from eye root to each eyelid guide"""
    def createEyelidSOP(self, parent: hou.ObjNode, gdn: Mapping[str, str], curve_range: tuple[int, int], negative: bool = False) -> _EyelidGuides:
        """Creates the SOP for the eyelid guide curve"""
    def createEyelidGuideAlongCircle(self, name: str, parent: hou.ObjNode, circle: hou.SopNode, flip: bool = False, r_range: tuple[int, int] = (0, 60), offset: int = 0, translate: bool = False) -> hou.ObjNode:
        """Creates an eyelid guide that orbits around createNodethe center of the circle"""
    def createSimpleParentCHOP(self, node: hou.ObjNode, parent: hou.ObjNode, maskvalue: int) -> hou.OpNode:
        """Creates a simple parent blend constraint
        node: the node to be parented
        parent: the parent node
        maskvalue: the mask value to apply on the blend
        """
    def createEyelidGuideCHOP(self, node: hou.ObjNode, center_guide: hou.ObjNode) -> hou.OpNode:
        """Creates proportional parent blend constraint to the center_gudie for eyelid guide"""
    def createLookAtCHOP(self, node: hou.ObjNode, master_lookat: hou.ObjNode, eyeroot: hou.ObjNode) -> hou.OpNode:
        """Creates the CHOP network for the lookat guide"""
    def updateMirror(self, value: bool) -> None: ...
    def updateSide(self, value: int) -> None: ...
    def flipAngleParm(self, node: hou.ObjNode) -> None:
        """Flip the angle parm to mirror the angle properly"""
    def snapEyeToGeometry(self, node: hou.ObjNode | hou.SopNode, geo: hou.Geometry, primgrp: str | None = None) -> None:
        """Snap the eye_root to the eye geometry
        node: the obj node of the geometry
        geometry: the geometry data (hou.Geometry)
        primgrp: the primitive group for bounding box
        """
    def addRadiusParamter(self, node: hou.ObjNode) -> None:
        """Adds a radius paramter to the interface"""
    def toJSON(self) -> collections.OrderedDict[str, _GuideNames]: ...
    @typing.overload
    def getGuideObject(self, guidename: _EyelidName, ismain: bool = ...) -> _EyelidGuides | None: ...
    @typing.overload
    def getGuideObject(self, guidename: _NodeGuideName, ismain: bool = ...) -> hou.ObjNode | None: ...
    @typing.overload
    def getGuideObject(self, guidename: str, ismain: bool = ...) -> hou.ObjNode | _EyelidGuides | None: ...
    def deleteGuides(self) -> None: ...
    def showGuides(self, display: bool) -> None: ...
    def lockGuides(self, lock: bool) -> None: ...
