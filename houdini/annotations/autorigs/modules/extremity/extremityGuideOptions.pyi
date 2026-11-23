from collections.abc import Iterable, Sequence
from typing import NotRequired, TypeAlias, TypedDict

import hou
from PySide6 import QtGui, QtWidgets

from autorigs.modules.arm.armModule import ArmModule
from autorigs.modules.foot.buildFootGuide import FootGuide
from autorigs.modules.hand.buildHandGuide import HandGuide
from autorigs.modules.quadFoot.buildQuadFootGuide import QuadFootGuide
from autorigs.modules.extremity.extremityGuideController import ModuleOptionController
from autorigs.modules.extremity.extremityGuideModel import ModuleOptionModel
from autorigs.modules.leg.legModule import LegModule
from autorigs.modules.limb.limbModule import LimbModule
from autorigs.modules.master.masterModule import MasterModule
from autorigs.modules.quadleg.quadLegModule import QuadLegModule
from autorigs.modules.spine.spineModule import SpineModule
from autorigs.ui.uiParamFloat import UiParamFloat
from autorigs.ui.uiParentComboMenu import UiParentComboMenu
from autorigs.ui.uiToggleButtonsWidget import ToggleButtonsWidget

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

    def __init__(
        self,
        extremityguide: _ExtremityGuide,
        controller: ModuleOptionController,
        model: ModuleOptionModel,
        assetnode: hou.ObjNode,
        mastermodule: MasterModule,
        spinemodules: Iterable[SpineModule],
        limbmodules: Iterable[LimbModule],
    ) -> None: ...
    def onSideChanged(self, side: int) -> None: ...
    def onMirrorChanged(self, viewmirror: bool | int) -> None: ...
    def onDisplayChanged(self, displayid: int) -> None: ...
    def onExtremityTypeChanged(self, extremitytype: int) -> None: ...
    def onMetadigitChanged(self, toggle: bool | int) -> None: ...
    def onBigDigitChanged(self, toggle: bool | int) -> None: ...
    def getBuiltParentInfo(self) -> tuple[_ParentModule, hou.ObjNode]: ...
    def unlinkAllNodes(self) -> None: ...
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
    def updateParentModules(self, limbmodules: Iterable[LimbModule], spinemodules: Iterable[SpineModule]) -> None: ...
    def getMasterParentGuides(self, mastermodule: MasterModule) -> list[hou.ObjNode]: ...

class HandOptionsWidget(ModuleOptionsWidget):
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
    current_parent_module: _ParentModule | None

    def createParentWidget(
        self, spinemodules: Iterable[SpineModule], limbmodules: Iterable[ArmModule]
    ) -> UiParentComboMenu: ...
    def getExistingParents(
        self, limbmodules: Iterable[ArmModule], spinemodules: Iterable[SpineModule]
    ) -> list[tuple[_HandParentModule, list[hou.ObjNode]]]: ...
    def getLimbParentGuides(self, armmodule: ArmModule) -> list[hou.ObjNode]: ...
    def getSpineParentGuides(self, spinemodule: SpineModule) -> list[hou.ObjNode]: ...
    def updateParent(self, module: _HandParentModule, node: hou.ObjNode) -> None: ...
    def setCurrentSelection(self, parentmodule: _HandParentModule, node: hou.ObjNode) -> None: ...

class FootOptionsWidget(ModuleOptionsWidget):
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
    current_parent_module: _ParentModule | None

    def createParentWidget(
        self, spinemodules: Iterable[SpineModule], limbmodules: Iterable[LimbModule]
    ) -> UiParentComboMenu: ...
    def getExistingParents(
        self, limbmodules: Iterable[LimbModule], spinemodules: Iterable[SpineModule]
    ) -> list[tuple[_FootParentModule, list[hou.ObjNode]]]: ...
    def getLegParentGuides(self, legmodule: LegModule) -> list[hou.ObjNode]: ...
    def getArmParentGuides(self, armmodule: ArmModule) -> list[hou.ObjNode]: ...
    def getQuadLegParentGuides(self, quadlegmodule: QuadLegModule) -> list[hou.ObjNode]: ...
    def getSpineParentGuides(self, spinemodule: SpineModule) -> list[hou.ObjNode]: ...
    def updateParent(self, module: _FootParentModule, node: hou.ObjNode) -> None: ...
    def setCurrentSelection(self, parentmodule: _FootParentModule, node: hou.ObjNode) -> None: ...

class QuadFootOptionsWidget(ModuleOptionsWidget):
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
    current_parent_module: _ParentModule | None

    def createParentWidget(
        self, spinemodules: Iterable[SpineModule], limbmodules: Iterable[LimbModule]
    ) -> UiParentComboMenu: ...
    def getExistingParents(
        self, limbmodules: Iterable[LimbModule], spinemodules: Iterable[SpineModule]
    ) -> list[tuple[_FootParentModule, list[hou.ObjNode]]]: ...
    def getLegParentGuides(self, legmodule: LegModule) -> list[hou.ObjNode]: ...
    def getArmParentGuides(self, armmodule: ArmModule) -> list[hou.ObjNode]: ...
    def getQuadLegParentGuides(self, quadlegmodule: QuadLegModule) -> list[hou.ObjNode]: ...
    def getSpineParentGuides(self, spinemodule: SpineModule) -> list[hou.ObjNode]: ...
    def updateParent(self, module: _FootParentModule, node: hou.ObjNode) -> None: ...
