from .eye import eyeGuideParams as eyeGuideParams
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget as BaseParamWidget
from autorigs.modules.basicFace.basicFaceGuideModel import BasicFaceGuideModel as BasicFaceGuideModel
from autorigs.modules.basicFace.buildBasicFaceGuide import BasicFaceGuide as BasicFaceGuide
from autorigs.modules.jaw import jawGuideParams as jawGuideParams
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.utils import guideParamsHelper as guideParamsHelper
from autorigs.utils.guideParamsHelper import _ParamsJson
from hutil.Qt import QtWidgets

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, BasicFaceGuide]):
    model: BasicFaceGuideModel
    jawparams: jawGuideParams.ModuleParamsWidget
    eyeparams: eyeGuideParams.ModuleParamsWidget
    component_tab: QtWidgets.QTabWidget
    def __init__(self, faceguide: BasicFaceGuide, model: BasicFaceGuideModel) -> None: ...
    def updateSize(self, index: int) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def toJSON(self) -> _ParamsJson: ...
    def fromJSON(self, json: _ParamsJson) -> None: ...
    def hasUnsavedChanges(self) -> None: ...
