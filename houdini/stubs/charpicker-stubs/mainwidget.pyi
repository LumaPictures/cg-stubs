# Houdini stubs generated from Houdini 22.0.466

import hou
from . import controlbutton as controlbutton, controlslider as controlslider, cpglobals as cpglobals, tabview as tabview, tabwindow as tabwindow
from .controlbuttonmenu import ControlButtonMenu as ControlButtonMenu
from .imagecatalog import IMAGES_CATALOG_NAME as IMAGES_CATALOG_NAME, ImageCatalog as ImageCatalog
from .menubar import CharacterPickerMenuBar as CharacterPickerMenuBar
from .selectionmanager import ButtonSelectionManager as ButtonSelectionManager, KineFXButtonSelectionManager as KineFXButtonSelectionManager, ObjectButtonSelectionManager as ObjectButtonSelectionManager
from .shaperegistry import SHAPES_CATALOG_NAME as SHAPES_CATALOG_NAME, ShapeCatalog as ShapeCatalog
from charpicker.backgroundimage import _ImageMap
from charpicker.canvaslabel import _LabelMap
from charpicker.controlbutton import _ButtonMap
from charpicker.menubar import CharacterPickerMenuBarBase as CharacterPickerMenuBarBase
from charpicker.tabview import TabViewContextMenu as TabViewContextMenu
from charpicker.tabwindow import TabWindow as TabWindow
from collections.abc import Callable as Callable
from hutil.PySide import QtCore, QtGui, QtWidgets
from typing import Any, NotRequired, TypeAlias, TypedDict


from typing import TypeAlias
CharacterType: TypeAlias = cpglobals.CharacterType
Mode: TypeAlias = cpglobals.Mode
SelectionState: TypeAlias = cpglobals.SelectionState
class _JointInfo(TypedDict):
    node: hou.SopNode
    joint: int

class _ButtonEventKwargs(TypedDict):
    id: str
    targetpaths: list[str]
    buttondefaultbehavior: NotRequired[str]

class _CanvasClipboardEntry(TypedDict):
    type: cpglobals.CanvasItemType
    data: _ButtonMap | _ImageMap | _LabelMap

class _CatalogToolTipFilter(QtCore.QObject):
    def eventFilter(self, obj: QtCore.QObject, event: QtCore.QEvent) -> bool: ...

class EventType:
    """Defines EventTypes that can be passed as the first argument to the callback
    registered with the CharacterPicker via registerEventCallback(callback).

    Check the help docs for charpicker for more details.
    """
    ButtonSelected: int
    ButtonDeselected: int

BUTTON_BEHAVIOR_NONE: str
BUTTON_BEHAVIOR_TRANSLATE: str
BUTTON_BEHAVIOR_SCALE: str
BUTTON_BEHAVIOR_ROTATE: str

def createCharacterPicker() -> CharacterPicker: ...

class CharacterSelector(QtWidgets.QWidget):
    mySelectedLabel: QtWidgets.QLabel
    mySelectedField: QtWidgets.QLineEdit
    mySelectedHistory: QtWidgets.QPushButton | None
    mySelectedHistoryMenu: QtWidgets.QMenu
    CONTROLS_H_SPACING: int
    def __init__(self, parent: QtWidgets.QWidget | None = None, label: str = 'Character', chooser_button: QtWidgets.QToolButton | None = None, add_history_button: bool = True) -> None: ...
    def reset(self) -> None: ...
    def setSelectedPath(self, path: str) -> None: ...
    def setHistoryActionCallback(self, callback: Callable[[QtGui.QAction], object]) -> None: ...
    def setFieldEnteredCallback(self, callback: Callable[[], object]) -> None: ...
    def clearHistory(self, add_clear_action: bool = True) -> None: ...

class CharacterPicker(QtWidgets.QFrame):
    CP_TAG: str
    hdaSource: hou.HDADefinition | None
    jsonPath: str | None
    myEditMode: bool
    myTabWindow: TabWindow
    ignore_selections: bool
    joints_map: dict[str, _JointInfo]
    joint_paths_map: dict[hou.SopNode, dict[int, str]]
    preserveButtonSizesChanged: QtCore.Signal
    myMenuBar: CharacterPickerMenuBarBase | None
    def __init__(self, parent: QtWidgets.QWidget | None = None, mode: cpglobals.Mode = ..., autosave: bool = False) -> None: ...
    def setupUI(self, menu_bar: CharacterPickerMenuBarBase | None = None, character_selector: CharacterSelector | None = None, edit_button_menu: ControlButtonMenu | None = None, button_menu: ControlButtonMenu | None = None, tab_view_context_menu: TabViewContextMenu | None = None) -> None: ...
    def setSelectionManager(self, selection_manager: ButtonSelectionManager) -> None: ...
    def getSelectionManager(self) -> ButtonSelectionManager: ...
    def getControlButtonMenu(self, edit_mode: bool) -> ControlButtonMenu | None: ...
    def hideTearOffMenus(self) -> None:
        """Hide any visible torn-off control button menus."""
    def getTabViewContextMenu(self) -> TabViewContextMenu | None: ...
    def getLastLabelFontSize(self) -> int: ...
    def setLastLabelFontSize(self, size: int) -> None: ...
    def getCanvasClipboard(self) -> list[_CanvasClipboardEntry]: ...
    def setCanvasClipboard(self, entries: list[_CanvasClipboardEntry]) -> None: ...
    def isTooltipMembersShown(self) -> bool: ...
    def setTooltipMembersShown(self, shown: bool) -> None: ...
    def groupHandlesMode(self) -> bool: ...
    def setGroupHandlesMode(self, enabled: bool) -> None: ...
    def preserveButtonSizes(self) -> bool: ...
    def setPreserveButtonSizes(self, enabled: bool) -> None: ...
    def getImageCatalog(self) -> ImageCatalog: ...
    def getShapeCatalog(self) -> ShapeCatalog: ...
    def getMode(self) -> cpglobals.Mode: ...
    def setIsEditingButton(self, editing: bool) -> None: ...
    def isEditingButton(self) -> bool: ...
    def isEditingCanvasSize(self) -> bool: ...
    def isBoxPickEnabled(self) -> bool: ...
    def isLassoPickEnabled(self) -> bool: ...
    def cleanup(self) -> None:
        """This is called by the Python Panel when the interface is
            about to be destroyed. Removes parent, event filters, and
            signal-slot connections to allow for complete cleanup upon garbage
            collection.
        """
    def reset(self) -> None:
        """Resets the Character Picker to its default state."""
    def setHelpText(self, text: str, link: dict[str, str] | None = None) -> None:
        """Set the help text shown when the layout is empty or disabled.

        Args:
            text: The message text to display.
            link: Optional dict with 'text' and 'url' keys for the link
                  displayed below the message.
        """
    def showHelp(self) -> None: ...
    def handleHipFileEvent(self, event_type: hou.EnumValue[hou.hipFileEventType]) -> None:
        """Callback handler for .hip file events."""
    def handleHDAEvent(self, event_type: hou.EnumValue[hou.hdaEventType], **kwargs: Any) -> None:
        """Callback handler for HDA events."""
    def historyAction(self, action: QtGui.QAction) -> None:
        """Called when an item from the history list is selected"""
    def clearAllTabs(self) -> None:
        """Clears all of the tabs from myTabWindow."""
    def characterType(self) -> cpglobals.CharacterType: ...
    def fieldEntered(self) -> None:
        """Sets the inputted character based on the entered path in the
        Character text field.
        """
    def selectCharacter(self, path: str) -> None: ...
    def getSelectedCharacterPath(self) -> str | None:
        """Returns the path to the currently selected character node.

        If no node has been selected, returns None.
        """
    def getCharacterHistory(self) -> list[str]:
        """Returns a list of character paths that have been selected since the last clear.

        Ordered with the first entry being the latest, the last entry being the oldest.
        """
    def toggleEditMode(self, is_active: bool | None = None) -> None:
        """Sets the edit mode attribute for ALL sub widgets and displays
        or hides all of the related content, i.e. the button drop down menu and the
        TabView tool bar. Both the TabView widget and ControlButton widget have `myEditMode`
        boolean attributes that have to be updated in order to activate the menu displays.
        """
    def createJSONString(self, pretty_print: bool = False, current_tab_only: bool = False) -> str:
        """Iterates through all of the tabs and constructs the json encoded string given
        all of the parameters of the child widgets.
        """
    def saveToFile(self, path: str | None = None) -> bool:
        """Writes the json string to a file
        """
    def saveToHDA(self) -> bool:
        """Writes the json string to the section in the HDA
        """
    def promptToSave(self) -> None:
        """Prompt the user to save the current character picker layout
        if there are unsaved changes."""
    def save(self) -> bool:
        """
        Save the character picker layout. Children with custom saving logic
        should override the _doSave method.
        """
    def postSave(self) -> None: ...
    def duplicateCurrentTab(self) -> None: ...
    def registerEventCallback(self, callback: Callable[[int, _ButtonEventKwargs], object] | None) -> None:
        """See the documentation for EventType for more details."""
    def enableCanvasResizeMode(self, enabled: bool, update_button: bool = True) -> None: ...
    def activeLayer(self) -> cpglobals.Layer: ...
    def selectedShapeName(self) -> str:
        """Return the currently selected shape name from the catalog."""
    def selectedImageCatalogRef(self) -> str | None:
        """Return the catalog ref of the selected image in the catalog."""
    def getKinefxJointsMap(self) -> dict[str, _JointInfo] | None: ...
    def getKinefxJoints(self) -> tuple[list[str], list[str]]: ...
    def loadFromJSONFile(self, fileName: str | None = None) -> None:
        """Loads in the json string from the supplied file
        """
    def loadFromHDA(self, path: str) -> None:
        """Loads in the json string from the supplied HDA."""
    def eventFilter(self, obj: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """Handles click focus and Edit Mode shortcut when shortcut event is
        not triggered.
        """
    def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None: ...
    def dropEvent(self, event: QtGui.QDropEvent) -> None: ...
