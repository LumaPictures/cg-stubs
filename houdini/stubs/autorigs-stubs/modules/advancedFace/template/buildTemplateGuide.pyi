# Houdini stubs generated from Houdini 22.0.466

import hou
from autorigs.modules.advancedFace.cage.buildCageGuide import CageGuide as CageGuide
from autorigs.modules.base import buildBaseGuide as buildBaseGuide
from autorigs.modules.base.buildBaseGuide import _BaseGuideJson, _GuideNamesJson
from autorigs.modules.geometry.buildGeometryGuide import GeometryGuide as GeometryGuide
from collections.abc import MutableMapping, MutableSequence
from houtypes import NodeEventKwargs
from typing import Any, Protocol, Unpack

class _NodeEventCallback(Protocol):
    def __call__(self, **kwargs: Unpack[NodeEventKwargs]) -> None: ...

class TemplateGuide(buildBaseGuide.BaseGuide[_BaseGuideJson]):
    assetnode: hou.ObjNode
    guidenodesdata: dict[str, list[hou.OpNode | bool | None]]
    geometryguides: GeometryGuide
    default_guide_names: list[str]
    center_guide_callbacks: dict[hou.OpNode, tuple[list[hou.EnumValue[hou.nodeEventType]], _NodeEventCallback]]
    template: hou.ObjNode
    LPC_TEMPLATE_PATH: str
    JSON_KEY: str
    LPC_TEMPLATE: str
    DO_NOT_TOUCH: str
    SWITCH: str
    BLENDSHAPES: str
    POINTS_FILE: str
    POLY_OUT: str
    OUT: str
    CAGE_WRANGLE: str
    RAY: str
    DEFAULT_CAGE_GUIDES_NAME: str
    UPPER_LIP_GROUP_NAME: str
    LOWER_LIP_GROUP_NAME: str
    LEFT_UPPER_EYE_GROUP_NAME: str
    LEFT_LOWER_EYE_GROUP_NAME: str
    RIGHT_UPPER_EYE_GROUP_NAME: str
    RIGHT_LOWER_EYE_GROUP_NAME: str
    def __init__(self, assetnode: hou.ObjNode, geometryguides: GeometryGuide) -> None: ...
    def buildFromJsonNew(self, json: _GuideNamesJson, parent: hou.ObjNode | None = None) -> None: ...
    def buildFromJsonExisting(self, json: _GuideNamesJson) -> None: ...
    def getRootKey(self) -> str: ...
    def getRootNode(self) -> hou.ObjNode | None: ...
    def getCagePoints(self) -> tuple[hou.Point, ...]: ...
    def getDefaultGuideNames(self) -> list[str]: ...
    def generateCageGuides(self, cageguides: CageGuide, guidesdata: MutableMapping[str, list[Any]], guideslist: MutableSequence[str]) -> None:
        """Generates the cage guides subnet inside the asset"""
    def cageGuideFromPoint(self, point: hou.Point, parent: hou.OpNode) -> hou.ObjNode: ...
    def resetCageGuides(self, cageguides: CageGuide) -> None:
        """Resets cage guides back to their default positions"""
    def resnapCageGuides(self, cageguides: CageGuide) -> None:
        """Snaps cage guides back to the current position of the points"""
    def resnapCageGuide(self, point: hou.Point, guide: hou.ObjNode, position: hou.Vector3) -> None: ...
    def setGuideParams(self, point: hou.Point, guide: hou.OpNode) -> None: ...
    def toggleLinkToGuides(self, value: bool | int) -> None: ...
    def isLinked(self) -> bool: ...
    def linkToGuides(self) -> None: ...
    def unlinkToGuides(self) -> None: ...
    def changeSwitch(self, index: int) -> None: ...
    def setOutputFlags(self, node_key: str, flag: bool) -> None: ...
    def hasValidGeometry(self) -> bool: ...
    def deleteGuides(self) -> None: ...
    def addResetXCallback(self, guide: hou.OpNode, x: float) -> None:
        '''We want to "lock" the x coordinates
            of the center cage guides without removing
            free translate control in the viewport.
            So add a callback to that resets the x value of the guide
            every time it\'s changed'''
    def resetX(self, event_type: hou.EnumValue[hou.nodeEventType], x: float, **kwargs: Any) -> None: ...
    def generateLPC(self) -> None: ...
