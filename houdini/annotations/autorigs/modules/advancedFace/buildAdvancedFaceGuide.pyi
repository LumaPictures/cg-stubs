from collections.abc import Mapping
from typing import Any, NotRequired, TypedDict

import hou
from autorigs.asset.autoRigsAsset import AutoRigsAsset
from autorigs.modules.base import buildBaseGuide
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.advancedFace.character.buildCharacterGuide import _CharacterGuideJson
from autorigs.modules.advancedFace.eye.buildEyeGuide import _EyeGuideJson
from autorigs.modules.advancedFace.lip.buildLipGuide import _LipGuideJson
from autorigs.modules.geometry.buildGeometryGuide import GeometryGuide
from autorigs.modules.jaw.buildJawGuide import JawGuide
from autorigs.modules.advancedFace.cage.buildCageGuide import CageGuide
from autorigs.modules.advancedFace.character.buildCharacterGuide import CharacterGuide
from autorigs.modules.advancedFace.eye.buildEyeGuide import EyeGuide
from autorigs.modules.advancedFace.lip.buildLipGuide import LipGuide
from autorigs.modules.advancedFace.template.buildTemplateGuide import TemplateGuide
from autorigs.modules.advancedFace.tongue.buildTongueGuide import TongueGuide
from autorigs.modules.advancedFace.advancedFaceModule import _AdvancedFaceModuleJson
from autorigs.utils.guideParamsHelper import _ParamsJson

class _AdvancedFaceGuideJson(TypedDict):
    guidenames: Mapping[str, str]
    geometry: _GuideNamesJson
    jaw: _GuideNamesJson
    template: _GuideNamesJson
    cageguides: NotRequired[_GuideNamesJson]
    character: NotRequired[_CharacterGuideJson]
    lip: _LipGuideJson
    eye: _EyeGuideJson
    tongue: _GuideNamesJson

class AdvancedFaceGuide(buildBaseGuide.BaseGuide[_AdvancedFaceGuideJson]):
    autorigs_asset: AutoRigsAsset
    json: _AdvancedFaceModuleJson
    assetnode: hou.ObjNode
    guidenodesdata: dict[str, list[Any]]
    geometryguides: GeometryGuide
    jawguides: JawGuide
    templateguides: TemplateGuide
    cageguides: CageGuide
    characterguides: CharacterGuide
    tongueguides: TongueGuide
    eyeGuide: EyeGuide
    lipGuide: LipGuide
    def __init__(self, autorigs_asset: AutoRigsAsset, json: _AdvancedFaceModuleJson) -> None: ...
    def buildFromJsonNew(self, json: _AdvancedFaceGuideJson, paramjson: _ParamsJson) -> None: ...
    def buildFromJsonExisting(self, json: _AdvancedFaceGuideJson) -> None: ...
    def updateParent(self, parent: hou.ObjNode, connect: bool = ...) -> None: ...
    def getAutorigsAsset(self) -> AutoRigsAsset: ...
    def getJawGuide(self) -> JawGuide: ...
    def getGeometryGuide(self) -> GeometryGuide: ...
    def getTemplateGuide(self) -> TemplateGuide: ...
    def getCageGuide(self) -> CageGuide: ...
    def getCharacterGuide(self) -> CharacterGuide: ...
    def getEyeGuide(self) -> EyeGuide: ...
    def getLipGuide(self) -> LipGuide: ...
    def getTongueGuide(self) -> TongueGuide: ...
    def generateCageGuides(self) -> None: ...
    def generateCharacter(self) -> None: ...
    def toJSON(self) -> _AdvancedFaceGuideJson: ...
    def removeGenerateError(self) -> None: ...
    def deleteGuides(self) -> None: ...
