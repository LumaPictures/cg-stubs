import hou
from autorigs.modules.advancedFace.character.buildCharacterGuide import CharacterGuide as CharacterGuide
from autorigs.modules.base.autoRigsBaseWidget import BaseParamWidget as BaseParamWidget
from autorigs.ui.uiParamComboBox import UiParamComboBox as UiParamComboBox
from autorigs.ui.uiParamFactory import UiParamFactory as UiParamFactory
from autorigs.ui.uiParamFile import UiParamOperator as UiParamOperator
from autorigs.ui.uiParamFloat import UiParamFloat as UiParamFloat
from autorigs.ui.uiParamLocatorWidget import UiParamLocatorWidget as UiParamLocatorWidget
from autorigs.ui.uiParamMultiParm import ListItem as ListItem, UiParamMultiParm as UiParamMultiParm
from autorigs.ui.uiParamString import UiParamString as UiParamString
from autorigs.utils import buildGuideHelper as buildGuideHelper, faceutils as faceutils
from autorigs.utils.guideParamsHelper import _ParamsJson
from collections import OrderedDict
from hutil.Qt import QtWidgets
from typing import TypedDict

class _FacePresetLocatorJson(TypedDict):
    name: str
    uv: list[float]
    parent_type: int
    parent: str

class _FacePresetParentJson(TypedDict):
    name: str
    uv: list[float]

class _FacePresetJson(TypedDict):
    locators: list[_FacePresetLocatorJson]
    parents: list[_FacePresetParentJson]
    mirror: dict[str, str]
    main_nodes: list[str]

class _CharacterMirrorJson(TypedDict):
    mirror: dict[str, str]
    main_nodes: list[str]

class ModuleParamsWidget(BaseParamWidget[_ParamsJson, CharacterGuide]):
    mirror: dict[hou.ObjNode, hou.ObjNode]
    main_nodes: set[hou.ObjNode]
    parent_widgets: OrderedDict[str, QtWidgets.QWidget]
    parent_index: int
    lpc_character: hou.ObjNode
    assetnode: hou.ObjNode
    relative_node: hou.ObjNode
    locator_name: UiParamString
    locator_mirror: QtWidgets.QCheckBox
    parent_name: UiParamString
    parent_mirror: QtWidgets.QCheckBox
    parent_type: UiParamComboBox
    list_tab: QtWidgets.QTabWidget
    locator_tab: QtWidgets.QWidget
    locator_list: UiParamMultiParm
    parent_tab: QtWidgets.QWidget
    parent_list: QtWidgets.QWidget
    parent_layout: QtWidgets.QVBoxLayout
    PRESETS_PATH: str
    PRESETS_FILES: list[str]
    PRESETS_JSON: list[_FacePresetJson | None]
    PRESETS_MENU_ITEMS: list[list[int | str]]
    PARENT_TYPE_ITEMS: list[str]
    PARENT_TYPE_NONE: int
    PARENT_TYPE_NURBS: int
    PARENT_TYPE_CUSTOM: int
    MIRROR_PREFIX: str
    def __init__(self, characterguide: CharacterGuide) -> None: ...
    def setupUI(self) -> None: ...
    def createLocatorListTab(self) -> QtWidgets.QWidget: ...
    def createParentListTab(self) -> QtWidgets.QWidget: ...
    def fromJSON(self, json: _ParamsJson) -> None: ...
    def toJSON(self) -> _ParamsJson: ...
    def initializeAfterJson(self, json: _CharacterMirrorJson) -> None: ...
    def toggleParentWidgetVisibility(self, index: int, widget: QtWidgets.QWidget) -> None: ...
    def toggleParmVisibility(self, toggle: int) -> None: ...
    def createLocatorPresets(self, index: int) -> None: ...
    def clearGuides(self) -> None: ...
    def onWidgetCreated(self, index: int, item_widget: ListItem) -> None:
        """Set up the callbacks when a new instance of UiParamLocatorWidget in the UiParamMultiParm is created"""
    def onWidgetDeleted(self, index: int, item_widget: ListItem) -> None:
        """Do necessary cleanup work when a multiparm instance is deleted"""
    def deleteLocator(self, locator: hou.ObjNode) -> None: ...
    def deleteNode(self, node: hou.ObjNode) -> None:
        """Deletes a node and removes it from all data structures"""
    def shiftLocators(self, index: int) -> None:
        """Resets the labels and constraints of the locators/UiParamMultiParm instances
        that come after a locator that was inserted/deleted. i.e If a UiParamMultiParm instance
        is deleted at index 10 out of 20, then instances 11 to 20 will have to be reset with the correct label
        and linked parameters"""
    def linkUvwParm(self, index: int, uvw_widget: UiParamFloat) -> None: ...
    def createCustomParent(self, uv: hou.Vector3 | None = None, name: str = '') -> hou.ObjNode | None: ...
    def addCustomParentToLocator(self, mirror: bool = False) -> hou.ObjNode | None: ...
    def createNurbsParent(self, prim_id: int) -> hou.ObjNode: ...
    def addParentToLocator(self, index: int, parent_type: int = ..., mirror: bool = False, parent_path: str = '') -> None: ...
    def updateParent(self, index: int) -> None: ...
    def createParentWidget(self, parent: hou.ObjNode, key: str) -> None:
        """Creates the ui parameters for a parent guide"""
    def popParentWidget(self, key: str) -> None:
        """Pops the parent widget referenced by key and deletes the parent guide"""
    def clearParentWidgets(self) -> None: ...
    def generateNurbsParents(self) -> None:
        """Once the user hits generate rig, generates the necessary NURBS parent controls"""
    def addMirrorPair(self, node: hou.ObjNode, mirror_node: hou.ObjNode) -> None: ...
    def getRelativePath(self, node: hou.NetworkMovableItem) -> str: ...
    def getParentWidgetKeyAtIndex(self, index: int) -> str: ...
    def getLocatorWidget(self, index: int) -> UiParamLocatorWidget: ...
    def createSurfaceLocator(self, index: int) -> None:
        """
        Creates a locator on the specified UV position of the surface.
        """
    def createMultiSurfaceParents(self) -> None: ...
    def createMultiSurfaceLocators(self) -> None:
        """
        Creates multiple surface locators where the user clicks
        """
    def setMirrorLocatorExpressions(self, locator: hou.ObjNode, mirror_locator: hou.ObjNode) -> None: ...
    def addLocatorSlot(self) -> int: ...
    def createLocatorAtIndex(self, idx: int, prim: float, uv: hou.Vector3, isMirror: bool = False, name: str = '', parent_type: int | None = None, parent_path: str = '') -> hou.ObjNode:
        """
        Create a locator at the specified index slot with the given prim and uv.
        """
    def changeLocatorReferences(self, old_locator: hou.ObjNode | None, new_locator: hou.ObjNode | None, index: int) -> None: ...
    def clearLocatorReferences(self, locator: hou.ObjNode, index: int) -> None: ...
    def setLocatorReferences(self, locator: hou.ObjNode, index: int) -> None:
        """Links the locator to a multiparm instance at index in the lpc character node"""
    def setConstraintsPath(self, locator: hou.ObjNode, index: int) -> None:
        """Sets up the uv surface constraint for the locator"""
    def getMirrorName(self, name: str) -> str: ...
    def getMirrorNode(self, node: hou.ObjNode) -> hou.ObjNode: ...
    def getLocator(self, index: int) -> hou.ObjNode | None: ...
    def getLocatorUVW(self, index: int) -> list[float]: ...
    def getLocatorParentType(self, index: int) -> int: ...
    def getLocatorParent(self, index: int) -> hou.ObjNode | None: ...
    def getLocatorList(self) -> UiParamMultiParm: ...
    def getParent(self, parent_key: str) -> hou.ObjNode | None: ...
    def getParentWidgets(self) -> OrderedDict[str, QtWidgets.QWidget]: ...
