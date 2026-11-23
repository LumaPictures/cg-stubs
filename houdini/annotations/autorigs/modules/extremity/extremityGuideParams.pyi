from collections.abc import Iterable, Sequence
from typing import TypeAlias, TypedDict

import hou
from houtypes import JSONLike
from PySide6 import QtWidgets

from autorigs.modules.extremity.buildExtremityGuide import ExtremityGuide
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel
from autorigs.ui.uiParamColor import UiParamColor
from autorigs.ui.uiParamFloat import UiParamFloat
from autorigs.ui.uiParamInt import UiParamInt

# One guide's params ({"translate": (x, y, z), "size": 0.1, ...}): toJSON writes parmTuple().eval()
# tuples and parm().eval() numbers, the shipped defaults have lists and numbers as strings.
_ExtremityParamJson: TypeAlias = dict[str, JSONLike]
# {"hand"/"foot": ..., "<guide>": params, ..., "fingerparams"/"toeparams": [{"<digit guide>": params}]}
_ExtremityParamsJson: TypeAlias = dict[str, _ExtremityParamJson | list[dict[str, _ExtremityParamJson]]]

class _ParamDetail(TypedDict):
    label: str
    jsonlabel: str
    nodes: Sequence[hou.ObjNode]
    params: list[int]

class _DigitGuideTab(TypedDict):
    tablabel: str
    tabdetail: list[_ParamDetail]

class ModuleParamsWidget(QtWidgets.QWidget):
    LABEL_PARAM_BIG_DIGIT_GUIDES: list[str]
    LABEL_PARAM_DIGITS_GUIDES: list[str]
    JSON_PARAM_BIG_DIGIT_GUIDES: list[str]
    JSON_PARAM_DIGITS_GUIDES: list[str]

    extremityguide: ExtremityGuide
    widget: QtWidgets.QWidget
    mainlayout: QtWidgets.QVBoxLayout
    tabs: QtWidgets.QTabWidget
    hasbigdigittab: bool
    extremitytype: str
    model: ModuleOptionModel
    scroll: QtWidgets.QScrollArea
    vLayout: QtWidgets.QVBoxLayout
    moduletype: hou.OpNodeType
    modulenode: hou.ObjNode

    def __init__(self, extremityguide: ExtremityGuide, model: ModuleOptionModel) -> None: ...
    def getExtremityType(self) -> str: ...
    def updateParmUI(self) -> None: ...
    def unlinkAllNodes(self) -> None: ...
    def getDigitGuideTabObj(
        self,
        tablabel: str,
        controls: Sequence[hou.ObjNode],
        controllabels: Sequence[str],
        controljsonlabels: Sequence[str],
    ) -> _DigitGuideTab: ...
    def createTab(
        self, tabdetail: Iterable[_ParamDetail], digitwidgetsdst: dict[str, str | dict[int, UiParamFloat | UiParamColor | UiParamInt]] | None = ...
    ) -> QtWidgets.QScrollArea: ...
    def addTab(self, tablabel: str, tabscroll: QtWidgets.QWidget, insertidx: int | None = ...) -> None: ...
    def updateNumDigit(self, numdigits: int) -> None: ...
    def updateHasBigDigit(self, hasbigdigit: bool | int) -> None: ...
    def toJSON(self) -> _ExtremityParamsJson: ...
    def getJsonDigitGuides(self, i: int) -> list[str]: ...
    def fromJSON(self, json: _ExtremityParamsJson) -> bool: ...

class HandParamsWidget(ModuleParamsWidget):
    LABEL_PARAM_CENTER: str
    LABEL_PARAM_ROOT: str
    LABEL_PARAM_ROTATE_ROOT: str
    LABEL_PARAM_EXTREMITY_START: str
    LABEL_PARAM_EXTREMITY_ROLL: str
    LABEL_PARAM_DIGIT_ROLL: str
    LABEL_DIGIT: str
    LABEL_DIGIT_ROOT: str
    LABEL_PARAM_BIG_DIGIT: str
    LABEL_PARAM_DIGIT_FORMAT: str
    LABEL_FULL: str
    JSON_CENTER: str
    JSON_FULL: str
    JSON_ROOT: str
    JSON_ROTATE_ROOT: str
    JSON_EXTREMITY_START: str
    JSON_EXTREMITY_ROLL: str
    JSON_DIGIT_ROLL: str
    JSON_DIGITS: str
    JSON_DIGITS_ROOT: str
    JSON_DIGIT_ALL: str
    JSON_DIGIT_PARAMS: str
    JSON_BIG_DIGIT: str
    JSON_DIGIT_FORMAT: str
    def __init__(self, extremityguide: ExtremityGuide, model: ModuleOptionModel) -> None: ...

class FootParamsWidget(ModuleParamsWidget):
    LABEL_PARAM_CENTER: str
    LABEL_PARAM_ROOT: str
    LABEL_PARAM_TRANSLATE_ROOT: str
    LABEL_PARAM_ROTATE_ROOT: str
    LABEL_PARAM_EXTREMITY_START: str
    LABEL_PARAM_EXTREMITY_ROLL: str
    LABEL_PARAM_DIGIT_ROLL: str
    LABEL_DIGIT: str
    LABEL_DIGIT_ROOT: str
    LABEL_PARAM_BIG_DIGIT: str
    LABEL_PARAM_DIGIT_FORMAT: str
    LABEL_FULL: str
    JSON_CENTER: str
    JSON_FULL: str
    JSON_ROOT: str
    JSON_ROTATE_ROOT: str
    JSON_EXTREMITY_START: str
    JSON_EXTREMITY_ROLL: str
    JSON_DIGIT_ROLL: str
    JSON_DIGITS: str
    JSON_DIGITS_ROOT: str
    JSON_DIGIT_ALL: str
    JSON_DIGIT_PARAMS: str
    JSON_BIG_DIGIT: str
    JSON_DIGIT_FORMAT: str
    def __init__(self, extremityguide: ExtremityGuide, model: ModuleOptionModel) -> None: ...

class QuadFootParamsWidget(ModuleParamsWidget):
    LABEL_PARAM_CENTER: str
    LABEL_PARAM_ROOT: str
    LABEL_PARAM_TRANSLATE_ROOT: str
    LABEL_PARAM_ROTATE_ROOT: str
    LABEL_PARAM_EXTREMITY_START: str
    LABEL_PARAM_EXTREMITY_ROLL: str
    LABEL_PARAM_DIGIT_ROLL: str
    LABEL_DIGIT: str
    LABEL_DIGIT_ROOT: str
    LABEL_PARAM_BIG_DIGIT: str
    LABEL_PARAM_DIGIT_FORMAT: str
    LABEL_FULL: str
    JSON_CENTER: str
    JSON_FULL: str
    JSON_ROOT: str
    JSON_ROTATE_ROOT: str
    JSON_EXTREMITY_START: str
    JSON_EXTREMITY_ROLL: str
    JSON_DIGIT_ROLL: str
    JSON_DIGITS: str
    JSON_DIGITS_ROOT: str
    JSON_DIGIT_ALL: str
    JSON_DIGIT_PARAMS: str
    JSON_BIG_DIGIT: str
    JSON_DIGIT_FORMAT: str
    def __init__(self, extremityguide: ExtremityGuide, model: ModuleOptionModel) -> None: ...
