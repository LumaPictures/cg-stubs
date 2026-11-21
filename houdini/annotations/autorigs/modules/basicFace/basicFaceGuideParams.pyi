from PySide6 import QtWidgets
from autorigs.utils.guideParamsHelper import _ParamsJson

from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget
from autorigs.modules.basicFace.basicFaceGuideModel import BasicFaceGuideModel
from autorigs.modules.basicFace.buildBasicFaceGuide import BasicFaceGuide
from autorigs.modules.basicFace.eye import eyeGuideParams
from autorigs.modules.jaw import jawGuideParams

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
