import collections
from collections.abc import Mapping, Sequence
from typing import Literal, TypeAlias, TypedDict, overload

import hou

from autorigs.modules.base import buildBaseGuide
from autorigs.utils.buildGuideHelper import _GuideNames

_GuideData: TypeAlias = tuple[hou.ObjNode, bool, bool]
_EyelidGuides: TypeAlias = dict[str, _GuideData]
_GuideNodesData: TypeAlias = dict[str, _GuideData | _EyelidGuides]
_EyelidName: TypeAlias = Literal["eyelid_center", "eyelid_inner", "eyelid_outer"]
_NodeGuideName: TypeAlias = Literal[
    "eyesroot",
    "eyeroot",
    "lookat_guidecurve",
    "eyelid_captureline",
    "master_lookat",
    "capture_guide",
    "eyelid_guide",
    "lookat_root",
    "lookat",
]

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
    EYES_ROOT: Literal["eyesroot"]
    EYE_ROOT: Literal["eyeroot"]
    LOOKAT_GUIDECURVE: Literal["lookat_guidecurve"]
    EYELID_CAPTURELINE: Literal["eyelid_captureline"]
    MASTER_LOOKAT: Literal["master_lookat"]
    CAPTURE_GUIDE: Literal["capture_guide"]
    EYELID_CENTER: Literal["eyelid_center"]
    EYELID_INNER: Literal["eyelid_inner"]
    EYELID_OUTER: Literal["eyelid_outer"]
    GUIDE_CURVE: str
    CLOSED_GUIDE: str
    OPENED_TOP: str
    OPENED_BOT: str
    UPPERLID: str
    LOWERLID: str
    EYELID_GUIDE: Literal["eyelid_guide"]
    EYELID_CLOSE_COLOR: tuple[int, int, int]
    EYELID_OPEN_COLOR: tuple[int, int, int]
    EYELID_CAPTURE_COLOR: tuple[int, int, int]
    LOOKAT_ROOT: Literal["lookat_root"]
    LOOKAT: Literal["lookat"]
    SIDE_LEFT: int
    SIDE_RIGHT: int
    SIDE_DEFAULT: int
    DEFAULT_CENTER_RANGE: tuple[int, int]
    DEFAULT_INNER_RANGE: tuple[int, int]
    DEFAULT_OUTER_RANGE: tuple[int, int]
    RX_DRIVER: str

    assetnode: hou.ObjNode
    mirror: bool
    guidenodesdata: _GuideNodesData
    mguidenodesdata: _GuideNodesData

    def __init__(self, assetnode: hou.ObjNode) -> None: ...
    def buildFromJsonNew(self, json: _EyeGuideJson, parent: hou.ObjNode | None = ...) -> _GuideNodesData: ...
    def buildEyelidGuides(
        self,
        gdn: Mapping[str, str],
        mgdn: Mapping[str, str],
        parent: hou.ObjNode,
        mirror_parent: hou.ObjNode,
        curve_range: tuple[int, int],
    ) -> tuple[_EyelidGuides, _EyelidGuides]: ...
    def buildFromJsonExisting(self, json: _EyeGuideJson) -> _GuideNodesData: ...
    def buildEyelidGuidesFromExisting(self, gdn: Mapping[str, str]) -> _EyelidGuides: ...
    def createCaptureGuide(self, gdn: _EyeGuideNamesJson) -> hou.ObjNode: ...
    def createEyelidCaptureLines(
        self, gdn: _EyeGuideNamesJson, eye_root: hou.ObjNode, eyelid_guides: Sequence[hou.ObjNode]
    ) -> hou.ObjNode: ...
    def createEyelidSOP(
        self, parent: hou.ObjNode, gdn: Mapping[str, str], curve_range: tuple[int, int], negative: bool = ...
    ) -> _EyelidGuides: ...
    def createEyelidGuideAlongCircle(
        self,
        name: str,
        parent: hou.ObjNode,
        circle: hou.SopNode,
        flip: bool = ...,
        r_range: tuple[int, int] = ...,
        offset: int = ...,
        translate: bool = ...,
    ) -> hou.ObjNode: ...
    def createSimpleParentCHOP(self, node: hou.ObjNode, parent: hou.ObjNode, maskvalue: int) -> hou.OpNode: ...
    def createEyelidGuideCHOP(self, node: hou.ObjNode, center_guide: hou.ObjNode) -> hou.OpNode: ...
    def createLookAtCHOP(self, node: hou.ObjNode, master_lookat: hou.ObjNode, eyeroot: hou.ObjNode) -> hou.OpNode: ...
    def updateMirror(self, value: bool) -> None: ...
    def updateSide(self, value: int) -> None: ...
    def flipAngleParm(self, node: hou.ObjNode) -> None: ...
    def snapEyeToGeometry(self, node: hou.ObjNode | hou.SopNode, geo: hou.Geometry, primgrp: str | None = ...) -> None: ...
    def addRadiusParamter(self, node: hou.ObjNode) -> None: ...
    def toJSON(self) -> collections.OrderedDict[str, _GuideNames]: ...
    @overload
    def getGuideObject(self, guidename: _EyelidName, ismain: bool = ...) -> _EyelidGuides | None: ...
    @overload
    def getGuideObject(self, guidename: _NodeGuideName, ismain: bool = ...) -> hou.ObjNode | None: ...
    @overload
    def getGuideObject(self, guidename: str, ismain: bool = ...) -> hou.ObjNode | _EyelidGuides | None: ...
    def getGuideObject(self, guidename: str, ismain: bool = ...) -> hou.ObjNode | _EyelidGuides | None: ...
    def deleteGuides(self) -> None: ...
    def showGuides(self, display: bool) -> None: ...
    def lockGuides(self, lock: bool) -> None: ...
