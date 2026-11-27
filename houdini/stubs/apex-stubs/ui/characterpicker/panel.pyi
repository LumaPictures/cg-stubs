import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import hou
from .autogen_dialog import AutogenLayoutDialog as AutogenLayoutDialog
from .selectionmanager import ApexButtonSelectionManager as ApexButtonSelectionManager
from .utils import retrieveLayout as retrieveLayout, saveLayout as saveLayout
from apex.characterpicker.commands import ControlsFilter as ControlsFilter, ProjectionDirection as ProjectionDirection, sendProjectRigControls as sendProjectRigControls
from apex.ui.characterpicker.utils import _PickerSource
from apex.ui.statecommandutils import buildPathRefs as buildPathRefs, getControlColors as getControlColors, inAnimateState as inAnimateState, switchHandleTool as switchHandleTool
from apex.utils import prependCharToControlPath as prependCharToControlPath
from charpicker import cpglobals
from charpicker.controlbuttonmenu import ControlButtonMenu
from charpicker.mainwidget import CharacterPicker
from charpicker.menubar import CharacterPickerMenuBarBase
from charpicker.tabview import TabView, TabViewContextMenu
from collections.abc import Iterable, Mapping
from enum import Enum
from hutil.PySide import QtWidgets
from typing import NotRequired, TypeAlias, TypedDict

from typing import TypeAlias
Mode: TypeAlias = cpglobals.Mode
class _SelectControlsArgs(TypedDict):
    controls_in_tree_format: bool
    controls: list[str]
    pick_modifier: hou.EnumValue[hou.pickModifier]
    resolve_groups: bool
    run_control_callbacks: NotRequired[bool]
    active_control: NotRequired[list[str]]
ADD_BUTTON_TOOLTIP: str
ADD_BUTTONS_FROM_CONTROLS: str
ADD_BUTTONS_FROM_SELECTION_SETS: str
HELP_LINK: dict[str, str]
AUTOGEN_BUTTON_SIZE: int
AUTOGEN_CANVAS_PADDING: int

class ReplaceMode(Enum):
    SELECTED_BUTTONS = 0
    CURRENT_TAB = 1
    ALL_TABS = 2

class SelectModeButton(QtWidgets.QToolButton):
    """
    A menu button, used for the selection mode option.
    """
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None, icon: PySide6.QtGui.QIcon | None = None, tooltip: str | None = None) -> None: ...
    def isBoxPickEnabled(self) -> bool: ...
    def isLassoPickEnabled(self) -> bool: ...
    def mousePressEvent(self, event: PySide6.QtGui.QMouseEvent) -> None: ...

class APEXCharacterPickerMenuBar(CharacterPickerMenuBarBase):
    _char_picker: ApexCharacterPicker
    def __init__(self, picker: ApexCharacterPicker, edit_only: bool = False) -> None: ...
    def isBoxPickActionEnabled(self) -> bool: ...
    def isLassoPickActionEnabled(self) -> bool: ...
    def handleEditModeToggled(self, is_active: bool) -> None: ...

class APEXControlButtonMenu(ControlButtonMenu):
    def __init__(self, picker: ApexCharacterPicker, edit_mode: bool) -> None: ...

class APEXTabViewContextMenu(TabViewContextMenu):
    addButtonsFromControlsTriggered: PySide6.QtCore.Signal
    addButtonsFromSelectionSetsTriggered: PySide6.QtCore.Signal
    def __init__(self) -> None: ...

def createApexCharacterPicker(edit_only: bool = False) -> ApexCharacterPicker: ...

class RigChooserButton(QtWidgets.QToolButton):
    rig_selected: PySide6.QtCore.Signal
    def __init__(self) -> None:
        """auto-insert docstring: HOM_qt_NodeChooserButton::HOM_qt_NodeChooserButton"""
    def setNode(self, node: hou.OpNode) -> None: ...

class ApexSelection:
    def __init__(self) -> None: ...
    def setPrimaryControl(self, control: str) -> None: ...
    def setBehavior(self, behavior: str) -> None: ...
    def addControls(self, control_paths: Iterable[str]) -> None: ...
    def addCallbackControls(self, control_paths: Iterable[str]) -> None: ...
    def removeControls(self, control_paths: Iterable[str]) -> None: ...
    def asCommands(self) -> tuple[list[_SelectControlsArgs], list[_SelectControlsArgs]]: ...
    def behavior(self) -> str | None: ...

class ApexCharacterPicker(CharacterPicker):
    """Character Picker used with APEX Characters"""
    TOOL_MODE_FOR_BUTTON_BEHAVIOR: dict[str, str]
    def __init__(self, parent: PySide6.QtWidgets.QWidget | None = None, mode: cpglobals.Mode = ...) -> None: ...
    def setLayoutAndSceneViewer(self, layouts: Mapping[str, _PickerSource] | None, scene_viewer: hou.SceneViewer | None) -> None: ...
    def activate(self, pane: hou.PaneTab | None) -> None:
        """
        Called by the python panel whenever this panel is activated.
        Sets the mode and selects the current character based on the panel and
        current node type, which will adjust the UI accordingly.
        """
    def deactivate(self, pane: hou.PaneTab | None) -> None:
        """
        Called by the python panel whenever this panel is deactivated.
        If the panel is in edit only mode, ensure that the current layout is
        saved.
        """
    def enable(self, enabled: bool) -> None: ...
    def getApexControlPaths(self) -> tuple[list[str], dict[str, str]]:
        '''
        Fetch the list of control paths from the state.
        Called by the ButtonSelectionManager.

        Returns a tuple of (display_paths, display_to_actual_map).
        Group members are nested under their parent group path as
        "{group_path}/{member_name}" for display in the tree dialog.
        The mapping translates these display paths back to the actual
        control paths for storage.
        '''
    def openAutogenDialog(self) -> None:
        """Open the dialog for configuring picker layout autogeneration."""
    def generateLayoutFromRig(self, rig_path: str, controls_filter: ControlsFilter = ..., projection_direction: ProjectionDirection = ..., create_new_tab: bool = False) -> None:
        """Generate a picker layout by projecting rig control positions to 2D.

        Adds the generated buttons to the active view of the current tab, or
        to a new tab if `create_new_tab` is set (or there is no active
        TabView to add to).
        """
    def importLayout(self, replace: bool = False) -> None:
        """
        Import a layout from a json file
        :param file_path: Path to the layout file to load.
        :param replace: Whether the layout should replace the existing one, or
                        be added as new tabs
        """
    def exportLayout(self, current_tab_only: bool = False) -> None: ...
    def replaceCharacters(self, mode: ReplaceMode) -> None: ...
    def mirrorSelectedButtons(self) -> None: ...
    def getSelectedControlPaths(self) -> list[str]: ...
    def showControls(self, show: bool) -> None: ...
    def addButtonsFromControls(self, tab_view: TabView) -> None: ...
    def addButtonsFromSelectionSets(self, tab_view: TabView) -> None: ...
    def patternRenameSelectedButtons(self) -> None: ...
