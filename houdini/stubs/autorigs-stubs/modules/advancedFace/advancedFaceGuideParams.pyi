# Houdini stubs generated from Houdini 22.0.466

from .advancedFaceGuideModel import AdvancedFaceGuideModel as AdvancedFaceGuideModel
from .cage import cageGuideParams as cageGuideParams
from .character import characterGuideParams as characterGuideParams
from .eye import eyeGuideParams as eyeGuideParams
from .lip import lipGuideParams as lipGuideParams
from .template import templateGuideParams as templateGuideParams
from .tongue import tongueGuideParams as tongueGuideParams
from autorigs.modules.advancedFace.buildAdvancedFaceGuide import AdvancedFaceGuide as AdvancedFaceGuide
from autorigs.modules.advancedFace.cage.buildCageGuide import CageGuide as CageGuide
from autorigs.modules.advancedFace.character.buildCharacterGuide import CharacterGuide as CharacterGuide
from autorigs.modules.advancedFace.template.buildTemplateGuide import TemplateGuide as TemplateGuide
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget as BaseParamWidget
from autorigs.modules.jaw import jawGuideParams as jawGuideParams
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.utils.guideParamsHelper import _ParamsJson
from hutil.Qt import QtWidgets

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
