from PySide6 import QtWidgets
from autorigs.utils.guideParamsHelper import _ParamsJson
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget
from autorigs.modules.jaw import jawGuideParams
from autorigs.modules.advancedFace.advancedFaceGuideModel import AdvancedFaceGuideModel
from autorigs.modules.advancedFace.buildAdvancedFaceGuide import AdvancedFaceGuide
from autorigs.modules.advancedFace.cage import cageGuideParams
from autorigs.modules.advancedFace.cage.buildCageGuide import CageGuide
from autorigs.modules.advancedFace.character import characterGuideParams
from autorigs.modules.advancedFace.character.buildCharacterGuide import CharacterGuide
from autorigs.modules.advancedFace.eye import eyeGuideParams
from autorigs.modules.advancedFace.lip import lipGuideParams
from autorigs.modules.advancedFace.template import templateGuideParams
from autorigs.modules.advancedFace.template.buildTemplateGuide import TemplateGuide
from autorigs.modules.advancedFace.tongue import tongueGuideParams

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, AdvancedFaceGuide]):
    model: AdvancedFaceGuideModel
    templateguides: TemplateGuide
    cageguides: CageGuide
    characterguides: CharacterGuide
    jawparams: jawGuideParams.ModuleParamsWidget
    lipparams: lipGuideParams.ModuleParamsWidget
    eyeparams: eyeGuideParams.ModuleParamsWidget
    tongueparams: tongueGuideParams.ModuleParamsWidget
    cageparams: cageGuideParams.ModuleParamsWidget | None
    characterparams: characterGuideParams.ModuleParamsWidget | None
    component_tab: QtWidgets.QTabWidget
    def __init__(self, faceguide: AdvancedFaceGuide, model: AdvancedFaceGuideModel) -> None: ...
    def toJSON(self) -> _ParamsJson: ...
    def fromJSON(self, json: _ParamsJson) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def addCageTab(self) -> None: ...
    def addCharacterTab(self) -> None: ...
    def getTemplateParams(self) -> templateGuideParams.ModuleParamsWidget: ...
    def getCageParams(self) -> cageGuideParams.ModuleParamsWidget | None: ...
    def getCharacterParams(self) -> characterGuideParams.ModuleParamsWidget | None: ...
