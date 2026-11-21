import hou
from .cage import buildCageGuide as buildCageGuide
from .character import buildCharacterGuide as buildCharacterGuide
from .eye import buildEyeGuide as buildEyeGuide
from .lip import buildLipGuide as buildLipGuide
from .template import buildTemplateGuide as buildTemplateGuide
from .tongue import buildTongueGuide as buildTongueGuide
from autorigs.asset.autoRigsAsset import AutoRigsAsset as AutoRigsAsset
from autorigs.modules.advancedFace.advancedFaceModule import _AdvancedFaceModuleJson
from autorigs.modules.advancedFace.cage.buildCageGuide import CageGuide as CageGuide
from autorigs.modules.advancedFace.character.buildCharacterGuide import CharacterGuide as CharacterGuide, _CharacterGuideJson
from autorigs.modules.advancedFace.eye.buildEyeGuide import EyeGuide as EyeGuide, _EyeGuideJson
from autorigs.modules.advancedFace.lip.buildLipGuide import LipGuide as LipGuide, _LipGuideJson
from autorigs.modules.advancedFace.template.buildTemplateGuide import TemplateGuide as TemplateGuide
from autorigs.modules.advancedFace.tongue.buildTongueGuide import TongueGuide as TongueGuide
from autorigs.modules.base import buildBaseGuide as buildBaseGuide
from autorigs.modules.base.buildBaseGuide import _GuideNamesJson
from autorigs.modules.geometry import buildGeometryGuide as buildGeometryGuide
from autorigs.modules.geometry.buildGeometryGuide import GeometryGuide as GeometryGuide
from autorigs.modules.jaw import buildJawGuide as buildJawGuide
from autorigs.modules.jaw.buildJawGuide import JawGuide as JawGuide
from autorigs.utils.guideParamsHelper import _ParamsJson
from collections.abc import Mapping
from typing import Any, NotRequired, TypedDict

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
    FACE_ROOT: str
    BUILD_ERROR_MSG: str
    def __init__(self, autorigs_asset: AutoRigsAsset, json: _AdvancedFaceModuleJson) -> None: ...
    def buildFromJsonNew(self, json: _AdvancedFaceGuideJson, paramjson: _ParamsJson) -> None: ...
    def buildFromJsonExisting(self, json: _AdvancedFaceGuideJson) -> None: ...
    def updateParent(self, parent: hou.ObjNode, connect: bool = False) -> None: ...
    def getAutorigsAsset(self) -> AutoRigsAsset: ...
    def getJawGuide(self) -> JawGuide: ...
    def getGeometryGuide(self) -> GeometryGuide: ...
    def getTemplateGuide(self) -> TemplateGuide: ...
    def getCageGuide(self) -> CageGuide: ...
    def getCharacterGuide(self) -> CharacterGuide: ...
    def getEyeGuide(self) -> EyeGuide: ...
    def getLipGuide(self) -> LipGuide: ...
    def getTongueGuide(self) -> TongueGuide: ...
    def generateCageGuides(self) -> None:
        """Generates the cage guides subnet inside the asset"""
    def generateCharacter(self) -> None: ...
    def toJSON(self) -> _AdvancedFaceGuideJson: ...
    def removeGenerateError(self) -> None: ...
    def deleteGuides(self) -> None: ...
