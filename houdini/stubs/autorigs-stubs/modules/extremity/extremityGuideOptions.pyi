import hou
from . import extremityGuideModel as extremityGuideModel
from autorigs.modules.arm import armModule as armModule
from autorigs.modules.arm.armModule import ArmModule as ArmModule
from autorigs.modules.extremity.extremityGuideController import ModuleOptionController as ModuleOptionController
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel as ModuleOptionModel
from autorigs.modules.foot.buildFootGuide import FootGuide as FootGuide
from autorigs.modules.hand.buildHandGuide import HandGuide as HandGuide
from autorigs.modules.leg import legModule as legModule
from autorigs.modules.leg.legModule import LegModule as LegModule
from autorigs.modules.limb.limbModule import LimbModule as LimbModule
from autorigs.modules.master import masterModule as masterModule
from autorigs.modules.master.masterModule import MasterModule as MasterModule
from autorigs.modules.quadFoot.buildQuadFootGuide import QuadFootGuide as QuadFootGuide
from autorigs.modules.quadleg import quadLegModule as quadLegModule
from autorigs.modules.quadleg.quadLegModule import QuadLegModule as QuadLegModule
from autorigs.modules.spine import spineModule as spineModule
from autorigs.modules.spine.spineModule import SpineModule as SpineModule
from autorigs.ui import uiParentComboMenu as uiParentComboMenu
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.ui.uiParentComboMenu import UiParentComboMenu as UiParentComboMenu
from autorigs.ui.uiToggleButtonsWidget import ToggleButtonsWidget as ToggleButtonsWidget
from autorigs.utils import guideOptionsHelper as guideOptionsHelper
from collections.abc import Iterable, Sequence
from hutil.Qt import QtGui, QtWidgets
from typing import NotRequired, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_ParentModule: TypeAlias = MasterModule | LimbModule | SpineModule
_HandParentModule: TypeAlias = MasterModule | ArmModule | SpineModule
_FootParentModule: TypeAlias = MasterModule | LimbModule | SpineModule
_ExtremityGuide: TypeAlias = HandGuide | FootGuide | QuadFootGuide
class _ExtremityOptionsJson(TypedDict):
    parent: Sequence[str]
    mirror: int
    side: int
    type: int
    has_thumb: NotRequired[int]
    numfingers: NotRequired[int]
    has_metacarpals: NotRequired[int]
    metacarpal_length: NotRequired[float]
    has_bigtoe: NotRequired[int]
    numtoes: NotRequired[int]
    has_metatarsals: NotRequired[int]
    metatarsal_length: NotRequired[float]

class ModuleOptionsWidget(QtWidgets.QWidget):
    extremityguide: _ExtremityGuide
    controller: ModuleOptionController
    model: ModuleOptionModel
    mainlayout: QtWidgets.QVBoxLayout
    widgets: list[QtWidgets.QWidget]
    mastermodule: MasterModule
    current_parent_module: _ParentModule | None
    parentwidget: UiParentComboMenu
    mirror_toggle: QtWidgets.QCheckBox
    mirror_hbox: QtWidgets.QHBoxLayout
    current_mirror: bool
    first_time_fingers: bool
    side_widget: ToggleButtonsWidget
    type_widget: ToggleButtonsWidget
    current_type: int
    display_widget: ToggleButtonsWidget
    extremityoptions: QtWidgets.QGroupBox
    bigdigit_widget: QtWidgets.QPushButton
    numdigits_widget: ToggleButtonsWidget
    moredigits_textfield: QtWidgets.QLineEdit
    current_numdigits: int
    metadigit_toggle: QtWidgets.QCheckBox
    widthoption: UiParamFloat
    modulenode: hou.ObjNode
    moduletype: hou.OpNodeType
    extremitytype: str
    TYPE_FULL: int
    TYPE_DIGITS: int
    TYPE_DEFAULT: int
    SIDE_LEFT: int
    SIDE_RIGHT: int
    DISPLAY_ALL: int
    DISPLAY_BASE: int
    DISPLAY_DIGITS: int
    DISPLAY_DEFAULT: int
    DIGITS_COUNT_MORE: int
    DIGITS_ZERO: int
    HIGHLIGHT_COLOR: QtGui.QColor
    DEFAULT_PARENT_PATH: str
    SIDE_BUTTON_LABELS: list[str]
    DISPLAY_LABEL: str
    def __init__(self, extremityguide: _ExtremityGuide, controller: ModuleOptionController, model: ModuleOptionModel, assetnode: hou.ObjNode, mastermodule: MasterModule, spinemodules: Iterable[SpineModule], limbmodules: Iterable[LimbModule]) -> None: ...
    def onSideChanged(self, side: int) -> None: ...
    def onMirrorChanged(self, viewmirror: bool | int) -> None: ...
    def onDisplayChanged(self, displayid: int) -> None: ...
    def onExtremityTypeChanged(self, extremitytype: int) -> None: ...
    def onMetadigitChanged(self, toggle: bool | int) -> None: ...
    def onBigDigitChanged(self, toggle: bool | int) -> None: ...
    def getBuiltParentInfo(self) -> tuple[_ParentModule, hou.ObjNode]: ...
    def onDigitsCountChanged(self, numdigits: int) -> None: ...
    def onHasBigDigitChanged(self, hasbigdigit: bool | int) -> None: ...
    def onDigitsButtonChanged(self, buttonid: int) -> None: ...
    def onChangeDigitsCount(self, count: int) -> None: ...
    def getDefaultParentPath(self) -> str: ...
    def onTypeChanged(self, buttonid: int) -> None: ...
    def onMetadigitToggleChanged(self, toggle: bool | int) -> None: ...
    def getAllWidgets(self) -> list[QtWidgets.QWidget]: ...
    def toJSON(self) -> _ExtremityOptionsJson: ...
    def fromJSON(self, json: _ExtremityOptionsJson) -> bool: ...
    def getHasBigDigit(self) -> bool: ...
    def unlinkAllNodes(self) -> None: ...
    def updateParentModules(self, limbmodules: Iterable[LimbModule], spinemodules: Iterable[SpineModule]) -> None: ...
    def getMasterParentGuides(self, mastermodule: MasterModule) -> list[hou.ObjNode]: ...

class HandOptionsWidget(ModuleOptionsWidget):
    current_parent_module: _ParentModule | None
    PARENT_LABEL: str
    PREFIX_DEFAULT_LABEL: str
    SIDE_LABEL: str
    TYPE_LABEL: str
    TYPE_BUTTON_LABELS: list[str]
    DISPLAY_BUTTON_LABELS: list[str]
    DIGITS_COUNT_LABEL: str
    HAS_BIG_DIGIT_LABEL: str
    META_TOGGLE_LABEL: str
    JSON_HAS_BIG_DIGIT: str
    JSON_NUM_DIGITS: str
    JSON_HAS_METADIGITS: str
    JSON_METADIGIT_LENGTH: str
    def createParentWidget(self, spinemodules: Iterable[SpineModule], limbmodules: Iterable[ArmModule]) -> UiParentComboMenu: ...
    def getExistingParents(self, limbmodules: Iterable[ArmModule], spinemodules: Iterable[SpineModule]) -> list[tuple[_HandParentModule, list[hou.ObjNode]]]: ...
    def getLimbParentGuides(self, armmodule: ArmModule) -> list[hou.ObjNode]: ...
    def getSpineParentGuides(self, spinemodule: SpineModule) -> list[hou.ObjNode]: ...
    def updateParent(self, module: _HandParentModule, node: hou.ObjNode) -> None: ...
    def setCurrentSelection(self, parentmodule: _HandParentModule, node: hou.ObjNode) -> None: ...

class FootOptionsWidget(ModuleOptionsWidget):
    current_parent_module: _ParentModule | None
    PARENT_LABEL: str
    PREFIX_DEFAULT_LABEL: str
    SIDE_LABEL: str
    TYPE_LABEL: str
    TYPE_BUTTON_LABELS: list[str]
    DISPLAY_BUTTON_LABELS: list[str]
    DIGITS_COUNT_LABEL: str
    HAS_BIG_DIGIT_LABEL: str
    META_TOGGLE_LABEL: str
    JSON_HAS_BIG_DIGIT: str
    JSON_NUM_DIGITS: str
    JSON_HAS_METADIGITS: str
    JSON_METADIGIT_LENGTH: str
    def createParentWidget(self, spinemodules: Iterable[SpineModule], limbmodules: Iterable[LimbModule]) -> UiParentComboMenu: ...
    def getExistingParents(self, limbmodules: Iterable[LimbModule], spinemodules: Iterable[SpineModule]) -> list[tuple[_FootParentModule, list[hou.ObjNode]]]: ...
    def getLegParentGuides(self, legmodule: LegModule) -> list[hou.ObjNode]: ...
    def getArmParentGuides(self, armmodule: ArmModule) -> list[hou.ObjNode]: ...
    def getQuadLegParentGuides(self, quadlegmodule: QuadLegModule) -> list[hou.ObjNode]: ...
    def getSpineParentGuides(self, spinemodule: SpineModule) -> list[hou.ObjNode]: ...
    def updateParent(self, module: _FootParentModule, node: hou.ObjNode) -> None: ...
    def setCurrentSelection(self, parentmodule: _FootParentModule, node: hou.ObjNode) -> None: ...

class QuadFootOptionsWidget(ModuleOptionsWidget):
    current_parent_module: _ParentModule | None
    PARENT_LABEL: str
    PREFIX_DEFAULT_LABEL: str
    SIDE_LABEL: str
    TYPE_LABEL: str
    TYPE_BUTTON_LABELS: list[str]
    DISPLAY_BUTTON_LABELS: list[str]
    DIGITS_COUNT_LABEL: str
    HAS_BIG_DIGIT_LABEL: str
    META_TOGGLE_LABEL: str
    JSON_HAS_BIG_DIGIT: str
    JSON_NUM_DIGITS: str
    JSON_HAS_METADIGITS: str
    JSON_METADIGIT_LENGTH: str
    def createParentWidget(self, spinemodules: Iterable[SpineModule], limbmodules: Iterable[LimbModule]) -> UiParentComboMenu: ...
    def getExistingParents(self, limbmodules: Iterable[LimbModule], spinemodules: Iterable[SpineModule]) -> list[tuple[_FootParentModule, list[hou.ObjNode]]]: ...
    def getLegParentGuides(self, legmodule: LegModule) -> list[hou.ObjNode]: ...
    def getArmParentGuides(self, armmodule: ArmModule) -> list[hou.ObjNode]: ...
    def getQuadLegParentGuides(self, quadlegmodule: QuadLegModule) -> list[hou.ObjNode]: ...
    def getSpineParentGuides(self, spinemodule: SpineModule) -> list[hou.ObjNode]: ...
    def updateParent(self, module: _FootParentModule, node: hou.ObjNode) -> None: ...
