# Houdini stubs generated from Houdini 22.0.466

import hou
from .eye import buildEyeGuide as buildEyeGuide
from autorigs.modules.base import buildBaseGuide as buildBaseGuide
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.basicFace.basicFaceModule import _BasicFaceModuleJson
from autorigs.modules.basicFace.eye.buildEyeGuide import EyeGuide as EyeGuide, _EyeGuideJson
from autorigs.modules.jaw import buildJawGuide as buildJawGuide
from autorigs.modules.jaw.buildJawGuide import JawGuide as JawGuide
from autorigs.utils.guideParamsHelper import _ParamsJson
from collections.abc import Mapping
from typing import TypedDict

class _BasicFaceGuideJson(TypedDict):
    guidenames: Mapping[str, str]
    jaw: _GuideNamesJson
    eye: _EyeGuideJson

class BasicFaceGuide(buildBaseGuide.BaseGuide[_BasicFaceGuideJson]):
    jawguides: JawGuide
    eyeguides: EyeGuide
    assetnode: hou.ObjNode
    json: _BasicFaceModuleJson
    face_root: hou.ObjNode
    guidenodesdata: dict[str, list[hou.ObjNode | bool]]
    FACE_ROOT: str
    def __init__(self, assetnode: hou.ObjNode, json: _BasicFaceModuleJson) -> None: ...
    def buildFromJsonNew(self, json: _BasicFaceGuideJson, paramjson: _ParamsJson) -> None: ...
    def buildFromJsonExisting(self, json: _BasicFaceGuideJson) -> None: ...
    def updateParent(self, parent: hou.ObjNode, connect: bool = False) -> None: ...
    def getJawGuide(self) -> JawGuide: ...
    def getEyeGuide(self) -> EyeGuide: ...
    def toJSON(self) -> _BasicFaceGuideJson: ...
