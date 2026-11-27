import apex.stateutils_2 as asu
import apex.ui.selectionmanager.modelconfig as sscfg
import apex.ui.selectionmanager.modelimpl as ssimpl
import apex.ui.selectionmanager.modelitem as ssmi
import apex.ui.selectionmanager.utils as ssu
import hou
from apex.animationcatalog import _ControlTree
from apex.ui.selectionmanager.modelconfig import _ExportedSet, _LabelTree, _SetDiff, _States
from collections.abc import Callable as Callable, Collection, Iterable, Sequence
from hutil.Qt import QtCore, QtGui
from hutil.qt.objecthandle import QtObjectHandle
from poselib.itemlibrary import IdentityProxyModel as plIdentityProxyModel
from typing import ClassVar, Concatenate, Final, Literal, Never, Self, TypeAlias, TypedDict, Unpack

from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
from collections.abc import Mapping
from typing import ParamSpec
from typing import TypeVar
_Index: TypeAlias = QtCore.QModelIndex | QtCore.QPersistentModelIndex
_IndexT = TypeVar('_IndexT', QtCore.QModelIndex, QtCore.QPersistentModelIndex)
_ModelT = TypeVar('_ModelT', bound='SelectionManagerModel')
_P = ParamSpec('_P')
_R = TypeVar('_R')
_ItemData: TypeAlias = str | int | list[int] | QtGui.QColor | QtGui.QIcon | QtCore.QSize | QtCore.Qt.AlignmentFlag | QtGui.QIcon.Mode | None
_Color: TypeAlias = QtGui.QColor | hou.Color | int | None
_RigPatternsLookup: TypeAlias = Mapping[str, Sequence[tuple[str, str]]]
LayoutChangeBlock: TypeAlias = ssimpl.LayoutChangeBlock
ResetModelBlock: TypeAlias = ssimpl.ResetModelBlock
MultiChangeBlock: TypeAlias = ssimpl.MultiChangeBlock
LightLayoutChangeBlock: TypeAlias = ssimpl.LightLayoutChangeBlock
LayoutMultiChangeBlock: TypeAlias = ssimpl.LayoutMultiChangeBlock
ModelConfig: TypeAlias = sscfg.ModelConfig
ModelGeometryConfig: TypeAlias = sscfg.ModelGeometryConfig
ModelFileConfig: TypeAlias = sscfg.ModelFileConfig
ModelDictConfig: TypeAlias = sscfg.ModelDictConfig
class _ModelKwargs(TypedDict, total=False):
    scene_viewer: hou.SceneViewer | None
    hotkeys: asu.Hotkeys | None
NAME_COLUMN_LABEL: str
SIZE20: int
ICON_SIZE: int
HEADER_TOOLTIPS: dict[int, str]
UNDO_LABEL: str
UNDO_TAG: str
MULTI_CHANGE_KEY: str
EDIT_MODE_LABEL: int
EDIT_MODE_NAME: int

class TreeUndo:
    """ An undo class for handling undos on the selection set tree. """
    def __init__(self, undo_mgr: UndoManager, diff: Sequence[_SetDiff]) -> None: ...
    def undo(self) -> None: ...
    def redo(self) -> None: ...

class UndoManager:
    """ An undo manager for handling setting up undos for the selection set
        tree.
    """
    def __init__(self, model: SelectionManagerModel) -> None: ...
    def saveForUndo(self) -> None:
        """ Save the tree state for undo. Compares the current tree
            with the previously stored tree and computes a diff between
            the two. Then stores the diff in an undo block.
        """
    def removeUndos(self) -> None:
        """ Remove all undos added by this manager. Hypothetically
            we want to remove all undos when we change node or
            leave a panel or really whenever they are no longer valid.
        """
    def applyDiff(self, diff: Sequence[_SetDiff], reverse: bool = False) -> None:
        """ Apply a diff stored in an undo block to modify the tree. """

def setsUpdated(fn: Callable[Concatenate[_ModelT, _P], _R]) -> Callable[Concatenate[_ModelT, _P], _R]: ...

class SelectionManagerModel(QtCore.QAbstractItemModel):
    """ The tree model used for the selection manager. """
    GROUP_ICON: ClassVar[hou.qt.Icon]
    COLOR_ICON: ClassVar[hou.qt.Icon]
    ALL_HANDLES_ICON: ClassVar[hou.qt.Icon]
    ALL_CONSTRAINTS_ICON: ClassVar[hou.qt.Icon]
    CURVE_ICON: ClassVar[hou.qt.Icon]
    PINNED_MIXED_ICON: ClassVar[hou.qt.Icon]
    PINNED_OFF_ICON: ClassVar[hou.qt.Icon]
    PINNED_ON_ICON: ClassVar[hou.qt.Icon]
    CHAR_VISIBLE_MIXED_ICON: ClassVar[hou.qt.Icon]
    CHAR_VISIBLE_OFF_ICON: ClassVar[hou.qt.Icon]
    CHAR_VISIBLE_ON_ICON: ClassVar[hou.qt.Icon]
    CHARACTER_ICON: ClassVar[hou.qt.Icon]
    FOLDER_SEL_ICON: ClassVar[hou.qt.Icon]
    FOLDER_SEL_ACTIVE_ICON: ClassVar[hou.qt.Icon]
    HANDLE_ICON: ClassVar[hou.qt.Icon]
    HANDLE_ACTIVE_ICON: ClassVar[hou.qt.Icon]
    HANDLE_VISIBLE_MIXED_ICON: ClassVar[hou.qt.Icon]
    HANDLE_VISIBLE_OFF_ICON: ClassVar[hou.qt.Icon]
    HANDLE_VISIBLE_ON_ICON: ClassVar[hou.qt.Icon]
    HANDLE_VISIBLE_OFF_DISABLED_ICON: ClassVar[QtGui.QIcon]
    CONSTRAINT_VISIBLE_MIXED_ICON: ClassVar[hou.qt.Icon]
    CONSTRAINT_VISIBLE_OFF_ICON: ClassVar[hou.qt.Icon]
    CONSTRAINT_VISIBLE_ON_ICON: ClassVar[hou.qt.Icon]
    CONSTRAINT_ICON: ClassVar[hou.qt.Icon]
    SELECTED_MIXED_ICON: ClassVar[hou.qt.Icon]
    SELECTED_OFF_ICON: ClassVar[hou.qt.Icon]
    SELECTED_ON_ICON: ClassVar[hou.qt.Icon]
    SHOW_ALL_ICON: ClassVar[hou.qt.Icon]
    SHOW_GHOSTED_ICON: ClassVar[hou.qt.Icon]
    ISOLATE_MIXED_ICON: ClassVar[hou.qt.Icon]
    ISOLATE_OFF_ICON: ClassVar[None]
    ISOLATE_ON_ICON: ClassVar[hou.qt.Icon]
    GEO_ICON: ClassVar[hou.qt.Icon]
    TOOL_ICON: ClassVar[hou.qt.Icon]
    TOOL_VISIBLE_MIXED_ICON: ClassVar[hou.qt.Icon]
    TOOL_VISIBLE_OFF_ICON: ClassVar[hou.qt.Icon]
    TOOL_VISIBLE_ON_ICON: ClassVar[hou.qt.Icon]
    HEADER_ICONS: ClassVar[dict[int, hou.qt.Icon | None]]
    SELECT_ICONS: ClassVar[list[hou.qt.Icon]]
    VISIBILITY_ICONS: ClassVar[list[hou.qt.Icon]]
    CHAR_ICONS: ClassVar[list[hou.qt.Icon]]
    TOOL_ICONS: ClassVar[list[hou.qt.Icon]]
    CONSTRAINT_ICONS: ClassVar[list[hou.qt.Icon | None]]
    PIN_ICONS: ClassVar[list[hou.qt.Icon]]
    ISOLATE_ICONS: ClassVar[list[hou.qt.Icon | None]]
    scene_viewer: hou.SceneViewer | None
    modelimpl: ssimpl.ModelImpl
    savedStructureUpdated: ClassVar[QtCore.Signal]
    structureUpdated: ClassVar[QtCore.Signal]
    currentSelectionUpdated: ClassVar[QtCore.Signal]
    setsUpdatedSignal: ClassVar[QtCore.Signal]
    hudFilterVisUpdated: ClassVar[QtCore.Signal]
    saveExpanded: ClassVar[QtCore.Signal]
    loadExpanded: ClassVar[QtCore.Signal]
    COLOR_ROLE: ClassVar[int]
    DESCRIPTION_ROLE: ClassVar[int]
    VISIBILITY_ROLE: ClassVar[int]
    BUTTON_VIS_ROLE: ClassVar[int]
    BUTTON_PIN_ROLE: ClassVar[int]
    BUTTON_CHAR_ROLE: ClassVar[int]
    BUTTON_CONSTR_ROLE: ClassVar[int]
    HUD_COLS_ROLE: ClassVar[int]
    ICON_MODE_ROLE: ClassVar[int]
    SELECTION_ROLE: ClassVar[int]
    ITEM_EDITABLE_FLAG: ClassVar[QtCore.Qt.ItemFlag]
    NO_ITEM_FLAGS_FLAG: ClassVar[QtCore.Qt.ItemFlag]
    ITEM_DRAG_ENABLED_FLAG: ClassVar[QtCore.Qt.ItemFlag]
    ITEM_DROP_ENABLED_FLAG: ClassVar[QtCore.Qt.ItemFlag]
    hotkeys: asu.Hotkeys | None
    def __init__(self, scene_viewer: hou.SceneViewer | None = None, hotkeys: asu.Hotkeys | None = None) -> None: ...
    def modelImpl(self) -> ssimpl.ModelImpl:
        """ The implementation part of the model. """
    def qtModel(self) -> Self:
        """ The qt part of the model. """
    def qtSourceModel(self) -> Self:
        """ The source qt part of the model. """
    def setEditMode(self, mode: int) -> None:
        """ Set the editor mode. """
    def editMode(self) -> int:
        """ Get the editor mode. """
    def setEditModeLabels(self) -> None:
        """ Set the edit mode to edit labels. """
    def setEditModeName(self) -> None:
        """ Set the edit mode to edit names. """
    def getRemapPatterns(self) -> tuple[str, str]:
        """ Get the patterns used when mirroring sets. """
    def setRemapPatterns(self, left_pattern: str, right_pattern: str) -> None:
        """ Set the patterns used when mirroring sets. """
    def getSetRemapPatterns(self) -> tuple[str, str]:
        """ Get the patterns for renaming sets when mirroring sets. """
    def setSetRemapPatterns(self, left_pattern: str, right_pattern: str) -> None:
        """ Set the patterns used for renaming sets when mirroring sets. """
    def setToolIcon(self, icon: QtGui.QIcon | None) -> None:
        """
        Set the icon for the active tool. This is used for .tool
        characters.
        """
    def getToolIcon(self) -> QtGui.QIcon:
        """ Get the tool icon used for .tool characters. """
    def nextUniqueId(self) -> int:
        """
        Get the next unique id to give to an item. Since the names
        can be shared, but that makes some things very hard to keep
        track of, we can associate unique ids with items and use these
        as unique names where needed.
        """
    def getRoot(self) -> ssmi.RootItem:
        """ Get the root item. """
    def getRootIndex(self) -> QtCore.QModelIndex:
        """ Get the root item index. """
    def getCurSelItem(self) -> ssmi.CurrentSelectionItem:
        """ Get the current selection item. """
    def getCurrentSelectionIndex(self) -> QtCore.QModelIndex:
        """ Get the index of the current selection special item. """
    def getAllControlsItem(self) -> ssmi.AllControlsItem:
        """ Get the item for all controls. """
    def getAllControlsIndex(self) -> QtCore.QModelIndex:
        """ Get the index of the all controls special item. """
    def getAllConstraintsItem(self) -> ssmi.AllConstraintsItem:
        """ Get the item for all constraints. """
    def getAllConstraintsIndex(self) -> QtCore.QModelIndex:
        """ Get the index of the all constraints special item. """
    def getLastSetIndex(self) -> QtCore.QModelIndex:
        """ Get the index of the last selection set. """
    def getCurrentSelection(self) -> _ControlTree:
        """ Get the stored current selection tree. """
    def getControlsTree(self) -> _ControlTree:
        """ Get the stored tree of all controls. """
    def generateControlsTree(self) -> _ControlTree:
        """
        Attempt to return the control tree, or if it does not exist,
        generate it from the existing controls in all sets.
        """
    def getVisibleTree(self) -> _ControlTree:
        """ Get the stored visible tree. """
    def getAllChars(self, include_tools: bool = True, include_motion_paths: bool = True, include_rigs: bool = False) -> _ControlTree:
        """
        Get the top level items in the controls tree that are
        considered characers. This only includes active characters.
        """
    def getCharactersInSetsByItems(self, items: Collection[ssmi.BaseItem] | None = None, include_tools: bool = True, include_motion_paths: bool = True, include_rigs: bool = False) -> _ControlTree:
        """ Get all character names that appear in sets, not just those active. """
    def getCharactersInSets(self, indexes: Iterable[_Index | None] | None = None, include_tools: bool = True, include_motion_paths: bool = True, include_rigs: bool = False) -> _ControlTree:
        """ Get all character names that appear in sets, not just those active. """
    def getSetIndexes(self) -> list[QtCore.QModelIndex]:
        """ Get indexes of set items not including current selection or all controls. """
    def getSetItems(self) -> list[ssmi.BaseItem]:
        """ Get set items not including current selection or all controls. """
    def getVisibleChars(self) -> _ControlTree:
        """ Get the visible characters. """
    def removeUndos(self) -> None:
        """
        Clear the undos created by the undo manager.
        This should be done when the undos no longer make
        sense, like if the node has changed and all the selection
        sets with it.
        """
    def getBlockManager(self, key: int | str | None = None) -> ssu.BlockLevelManager | None:
        """
        Get a block manager by key. This is needed by
        ssu.BlockManagers().
        """
    def isLoading(self) -> bool:
        """
        Whether we are currently loading the model. While doing this
        we probably don't want to save.
        """
    def getLoadingBlock(self) -> ssimpl.LoadingBlock:
        """
        Get a loading block to wrap some actions. This prevents
        updating all the states of the items while in the block
        until the end.
        """
    def getResetModelBlock(self) -> ResetModelBlock:
        """ Get a reset model block. """
    def isUpdatingCurrentSelection(self) -> bool:
        """ Whether currently updating current selection. """
    def inMultiChangeBlock(self) -> bool:
        """
        Whether the model is doing multiple changes for which we
        want to disable certain auto updates until the changes are done.
        Places where this might be used:
        1. Changing the state of many items.
        2. Restructuring the tree.
        3. Adding or removing many items at a time.
        """
    def isSorting(self) -> bool:
        """ Whether we are currently sorting. """
    def nextChildName(self, parent_item: ssmi.BaseItem | None = None, base_name: str | None = None, add_number_if_unique: bool = False) -> str:
        """ Get the next default set name. """
    def getLabelTree(self) -> _LabelTree:
        """ Get the tree of item labels. """
    def setLabelTree(self, label_tree: _LabelTree, full_update: bool = True) -> None:
        """ Set the tree of item labels. """
    def addLabel(self, control_path: str, label: str) -> None:
        """ Add a label for an item. """
    def removeLabel(self, control_path: str) -> None:
        """ Remove a label for an item. """
    def setControlTree(self, controls_tree: _ControlTree) -> None:
        """ Set the tree of all the controls. """
    def setCurrentSelection(self, controls_tree: _ControlTree) -> None:
        """ Set the current selection controls tree. """
    def isVisibilitySynced(self) -> bool:
        """ Whether the visibility is up to date. """
    def setVisibleControls(self, controls_tree: _ControlTree | None) -> None:
        """
        Set the visible controls in the tree. This changes the icon
        for the control visibility.
        """
    def cacheVisibleControls(self) -> None:
        """ Store the current visible control tree. """
    def hasCachedVisibleControls(self) -> bool:
        """ Whether we have a visibility tree cached. """
    def resetToCachedVisibleControls(self) -> bool:
        """ Reset the visible controls to what is cached. """
    def setVisibleChars(self, char_names: list[str] | _ControlTree) -> None:
        """
        Set the visible characters in the tree. This changes the icon
        for the character visibility.
        """
    def setVisibleConstraints(self, constraints: list[str] | _ControlTree) -> None:
        """
        Set the visible constraints in the tree.
        """
    def setHiddenSets(self, set_names: Iterable[str] | None) -> None:
        """ Set the list of selection set names to hide by default. """
    def getHiddenSets(self) -> list[str] | None:
        """ Get the list of selection set names to hide by default. """
    def addHiddenSets(self, set_names: Iterable[str]) -> None:
        """ Add selection set names to the hidden list. """
    def setHiddenControls(self, control_names: Iterable[str] | None) -> None:
        """ Set the list of control names to hide by default. """
    def getHiddenControls(self) -> list[str] | None:
        """ Get the list of control names to hide by default. """
    def addHiddenControls(self, control_names: Iterable[str]) -> None:
        """ Add control names to the hidden list. """
    def setPinnedControls(self, controls_tree: _ControlTree) -> None:
        """ Set the controls pinned in the tree. This changes the pin icon. """
    def getPinnedTree(self, patterns_tree: bool = False) -> _ControlTree:
        """ Get the tree of pinned controls. """
    def getIsolateTree(self, patterns_tree: bool = False) -> _ControlTree:
        """ Get the tree of isolated controls. """
    def getIsolateOrVisibleTree(self) -> _ControlTree:
        """
        Return the isolate tree if there are isolated controls and
        isolating is enabled, otherwise, return the visible tree.
        """
    def setControlActiveSingleByItem(self, paths: Sequence[str], root_item: ssmi.BaseItem | None, val: bool) -> None:
        """
        Set the control found by following paths from root_index
        to be active.
        """
    def setControlActiveSingle(self, paths: Sequence[str], root_index: _Index | None, val: bool) -> None:
        """
        Set the control found by following paths from root_index
        to be active.
        """
    def setSetActiveControlByItem(self, new_active_control: ssmi.BaseItem | None) -> None:
        """ Set the control with the given index to be active. """
    def setSetActiveControl(self, control_index: _Index | None) -> None:
        """ Set the control with the given index to be active. """
    def setActiveControl(self, control: list[str]) -> None:
        """ Set the active control given a control path. """
    def activeControl(self) -> list[str]:
        """ The control path for the item that currently has the handle. """
    def createControlSet(self, controls_tree: _ControlTree, name: str | None = None, parent_index: _Index | None = ..., active_control_path: Sequence[str] | None = None) -> ssmi.RootFolderItem:
        """
        Create a new controls set from the controls_tree within the set.

        :controls_tree: The tree of controls to put in the set.
        :name: An optional name to give to the new set. If left None,
               will use the next default child name.
        """
    @setsUpdated
    def createControlSetByItem(self, controls_tree: _ControlTree, name: str | None = None, parent: ssmi.BaseItem | None = None, active_control_path: Sequence[str] | None = None, parent_index: _Index | None = None) -> ssmi.RootFolderItem:
        """
        Create a new controls set from the controls_tree within the set.

        :controls_tree: The tree of controls to put in the set.
        :name: An optional name to give to the new set. If left None,
               will use the next default child name.
        """
    def createControlSetFromSel(self, name: str | None = None, parent_index: _Index | None = ...) -> ssmi.RootFolderItem:
        """ Create a new selection set from the current selection. """
    def createControlSetFromSelByItem(self, name: str | None = None, parent: ssmi.BaseItem | None = None) -> ssmi.RootFolderItem:
        """ Create a new selection set from the current selection. """
    def setHasNonFolderChildren(self, index: _Index) -> bool:
        """ Whether a set has descendants that are not folders. """
    def modifyControlSet(self, controls_tree: _ControlTree, index: _Index, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None, modify_patterns: bool = True, update_states: bool = True) -> None:
        """ Add or remove elements from a set. """
    @setsUpdated
    def modifyControlSetByItem(self, control_tree: _ControlTree, item: ssmi.BaseItem | None, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None, modify_patterns: bool = True, update_states: bool = True, parent_index: _Index | None = None) -> None:
        """ Add or remove elements from a set. """
    @setsUpdated
    def clearSets(self, parent_index: _Index = ...) -> None:
        """ Clear the sets under the parent_index. """
    def clearSetsByItem(self, item: ssmi.BaseItem | None, index: _Index | None = None) -> None:
        """ Clear the sets under the parent_item. """
    def removeItem(self, item: ssmi.BaseItem, index: _Index | None = None) -> None:
        """ Remove item. """
    @setsUpdated
    def loadSelectionSetsByItem(self, sel_sets_dict: Iterable[_ExportedSet], clear: bool = True, editable: bool = True, undo: bool = False, replace_char: str | None = None, root_item: ssmi.BaseItem | None = None) -> list[ssmi.BaseItem]:
        """ Load the selection sets from a stored selection sets dictionary. """
    def loadSelectionSets(self, sel_sets_dict: Iterable[_ExportedSet], clear: bool = True, editable: bool = True, undo: bool = False, replace_char: str | None = None, parent_index: _Index = ...) -> list[ssmi.BaseItem]:
        """ Load the selection sets from a stored selection sets dictionary. """
    @setsUpdated
    def sortControlsByItem(self, item: ssmi.BaseItem) -> None:
        """ Sort the controls under parent_index. """
    def sortControls(self, parent_index: _Index) -> None:
        """ Sort the controls under parent_index. """
    def exportSelectionSetsByItems(self, unique_ids: bool = False, items: Sequence[ssmi.BaseItem | None] | None = None, export_properties: Collection[str] | None = None, export_persistant: bool = False) -> list[_ExportedSet]:
        """
        Package the selection sets into a JSON-Compatible
        format and return it.
        """
    def exportSelectionSets(self, unique_ids: bool = False, indexes: Collection[_Index | None] | None = None, export_properties: Collection[str] | None = None, export_persistant: bool = False) -> list[_ExportedSet]:
        """
        Package the selection sets into a JSON-Compatible
        format and return it.
        """
    def retrieveFromState(self) -> None:
        """ Retrieve stuff from the state. """
    def exportToJSONByItems(self, items: Sequence[ssmi.BaseItem | None] | None = None, export_properties: Collection[str] | None = None, export_persistant: bool = False) -> str:
        """ Create a json string representation of the sets. """
    def exportToJSON(self, indexes: Collection[_Index | None] | None = None, export_properties: Collection[str] | None = None, export_persistant: bool = False) -> str:
        """ Create a json string representation of the sets. """
    def exportStates(self, filter_chars_tree: _ControlTree | None = None, filter_controls_tree: _ControlTree | None = None, override_chars: Iterable[str] | None = None) -> _States:
        """ Pack the states into a dictionary and then turn into a json string. """
    def exportStatesToJSON(self, filter_chars_tree: _ControlTree | None = None, filter_controls_tree: _ControlTree | None = None, override_chars: Iterable[str] | None = None) -> str:
        """ Pack the states into a dictionary and then turn into a json string. """
    @setsUpdated
    def importFromJSONByItem(self, json_string: str | None, clear: bool = True, editable: bool = True, undo: bool = False, replace_char: str | None = None, root_item: ssmi.BaseItem | None = None) -> list[ssmi.BaseItem]:
        """ Given a json representation of the sets, load them. """
    def importFromJSON(self, json_string: str | None, clear: bool = True, editable: bool = True, undo: bool = False, replace_char: str | None = None, parent_index: _Index = ...) -> list[ssmi.BaseItem]:
        """ Given a json representation of the sets, load them. """
    @setsUpdated
    def importFromGeometryByItem(self, geometry: hou.Geometry, clear: bool = True, editable: bool = True, undo: bool = False, load_states: bool = False, load_character_sets: bool = False, char_geometry: hou.Geometry | None = None, parent_item: ssmi.BaseItem | None = None) -> None:
        """ Import selection sets from a geometry with the proper attribute. """
    @setsUpdated
    def importFromGeometry(self, geometry: hou.Geometry, clear: bool = True, editable: bool = True, undo: bool = False, load_states: bool = False, load_character_sets: bool = False, char_geometry: hou.Geometry | None = None, parent_index: _Index = ...) -> None:
        """ Import selection sets from a geometry with the proper attribute. """
    @setsUpdated
    def applyDiff(self, diff: Iterable[_SetDiff], reverse: bool = False) -> None:
        """ Apply a diff at the root level to update the tree. """
    @setsUpdated
    def expandPatternsByItem(self, item: ssmi.BaseItem | None) -> None:
        """ Expand the patterns under index. """
    def expandPatterns(self, index: _Index) -> None:
        """ Expand the patterns under index. """
    @setsUpdated
    def expandPatternsItems(self, items: Iterable[ssmi.BaseItem | None]) -> None:
        """ Expand the patterns under indexes. """
    def expandPatternsIndexes(self, indexes: Iterable[_Index]) -> None:
        """ Expand the patterns under indexes. """
    @setsUpdated
    def separateCharsByItem(self, item: ssmi.BaseItem | None) -> None:
        """
        API Function for separating characters under an index,
        will also wrap it in the necessary blocks for efficiency.
        """
    def separateChars(self, index: _Index) -> None:
        """
        API Function for separating characters under an index,
        will also wrap it in the necessary blocks for efficiency.
        """
    @setsUpdated
    def separateCharsItems(self, items: Iterable[ssmi.BaseItem | None]) -> None:
        """
        API Function for separating characters under indexes,
        will also wrap it in the necessary blocks for efficiency.
        Use this for multiple rows as it will wrap the calls in
        a more efficient way.
        """
    def separateCharsIndexes(self, indexes: Iterable[_Index]) -> None:
        """
        API Function for separating characters under indexes,
        will also wrap it in the necessary blocks for efficiency.
        Use this for multiple rows as it will wrap the calls in
        a more efficient way.
        """
    @setsUpdated
    def separateCharsIntoSetsByItems(self, items: Iterable[ssmi.BaseItem | None], remove_originals: bool = False) -> None:
        """ Make separate sets (recursively) for each character. """
    def separateCharsIntoSets(self, indexes: Iterable[_Index], remove_originals: bool = False) -> None:
        """ Make separate sets (recursively) for each character. """
    @setsUpdated
    def applyToCharsItems(self, items: Iterable[ssmi.BaseItem | None], chars_list: Sequence[str] | None = None, mode: Literal[0, 1, 2] | None = None) -> None:
        """
        API functuin for applying sets under an index to the
        provided characters. Use this version when working with
        multiple indexes as it will wrap the calls in a more
        efficient way.
        """
    def applyToCharsIndexes(self, indexes: Iterable[_Index], chars_list: Sequence[str] | None = None, mode: Literal[0, 1, 2] | None = None) -> None:
        """
        API functuin for applying sets under an index to the
        provided characters. Use this version when working with
        multiple indexes as it will wrap the calls in a more
        efficient way.
        """
    @setsUpdated
    def replaceCharactersByItems(self, items: Iterable[ssmi.BaseItem | None], replace_chars_list: Collection[str], new_char_name: str) -> None:
        """
        Replace (possibly inactive) characters in sets with new_char_name.

        :indexes: A list of indexes to do the replace operation on.
        :replace_chars_list: A list of character names to replace.
        :new_char_name: The new character name to replace with.
        """
    def replaceCharacters(self, indexes: Iterable[_Index], replace_chars_list: Collection[str], new_char_name: str) -> None:
        """
        Replace (possibly inactive) characters in sets with new_char_name.

        :indexes: A list of indexes to do the replace operation on.
        :replace_chars_list: A list of character names to replace.
        :new_char_name: The new character name to replace with.
        """
    @setsUpdated
    def mirrorSetsByItems(self, items: Iterable[ssmi.BaseItem], rig_patterns_lookup: _RigPatternsLookup | None = None) -> list[ssmi.BaseItem]:
        """ Mirror the sets in the provided items. """
    def mirrorSets(self, indexes: Iterable[_Index], rig_patterns_lookup: _RigPatternsLookup | None = None) -> list[ssmi.BaseItem]:
        """ Mirror the sets in the provided indexes. """
    @setsUpdated
    def duplicateSetsByItems(self, items: Iterable[ssmi.BaseItem]) -> list[ssmi.BaseItem]:
        """ Duplicate the sets in the provided indexes. """
    def duplicateSets(self, indexes: Iterable[_Index]) -> list[ssmi.BaseItem]:
        """ Duplicate the sets in the provided indexes. """
    @setsUpdated
    def patternRenameSetsByItems(self, from_pattern: str, to_pattern: str, items: Iterable[ssmi.BaseItem | None]) -> None:
        """
        Rename the sets with the given indexes matching from_pattern
        to to_pattern.
        """
    def patternRenameSets(self, from_pattern: str, to_pattern: str, indexes: Iterable[_Index]) -> None:
        """
        Rename the sets with the given indexes matching from_pattern
        to to_pattern.

        If indexes is None, renames everything that is a set.
        """
    @setsUpdated
    def patternRenameAllSetsByItem(self, from_pattern: str, to_pattern: str, parent_item: ssmi.BaseItem | None = None) -> None:
        """
        Rename all sets under the parent index matching the from_pattern
        to to_pattern.
        """
    def patternRenameAllSets(self, from_pattern: str, to_pattern: str, parent_index: _Index = ...) -> None:
        """
        Rename all sets under the parent index matching the from_pattern
        to to_pattern.
        """
    @setsUpdated
    def setRowColorByItem(self, items: Iterable[ssmi.BaseItem], color: _Color) -> None:
        """ Set the background colour of the specified rows. """
    def setRowColor(self, indexes: Iterable[_Index], color: _Color) -> None:
        """ Set the background colour of the specified rows. """
    def modifyPinByItem(self, item: ssmi.BaseItem, pick_modifier: hou.EnumValue[hou.pickModifier]) -> None:
        """ Modify the pin state for this item. """
    def modifyPin(self, index: _Index, pick_modifier: hou.EnumValue[hou.pickModifier]) -> None:
        """ Modify the pin state for this item. """
    def modifyIsolateByItem(self, item: ssmi.BaseItem | None, pick_modifier: hou.EnumValue[hou.pickModifier]) -> None:
        """ Modify the isolate state for this item. """
    def modifyIsolate(self, index: _Index, pick_modifier: hou.EnumValue[hou.pickModifier]) -> None:
        """ Modify the isolate state for this item. """
    def clearPins(self) -> None:
        """ Clear all the pin states in the tree. """
    def clearIsolate(self) -> None:
        """ Clear all the isolate states in the tree. """
    def updateHasIsolate(self) -> None:
        """ Update whether there are isolated items. """
    def hasIsolate(self, only_if_enabled: bool = True) -> bool:
        """ Whether there are any isolated items. """
    def isolateEnabled(self) -> bool:
        """ Whether isolating is enabled. """
    def setIsolateEnabled(self, val: bool) -> None:
        """ Enable or disable isolating items. """
    def controlsVisible(self) -> bool:
        """ Whether the controls are visible. """
    def setControlsVisible(self, val: bool) -> None:
        """ Set whether the controls are visible. """
    def toggleVisible(self, show: bool = True) -> None:
        """ Toggle whether all controls are visible. """
    def isVisibilityTempDisabled(self) -> bool:
        """ Whether showing controls is enabled. """
    @setsUpdated
    def deleteSetsByItems(self, items: Iterable[ssmi.BaseItem]) -> None:
        """ Remove rows by items if editable. """
    def deleteSets(self, indexes: Iterable[_Index]) -> None:
        """ Remove rows by indexes if editable. """
    @setsUpdated
    def deleteSet(self, index: QtCore.QModelIndex) -> None:
        """ Remove row by index if editable. """
    def findIndex(self, path_parts: Sequence[str], root_index: QtCore.QModelIndex = ..., include_sets_path: bool = False) -> QtCore.QModelIndex | None:
        """ Find the control index given a control path and a root index. """
    def findIndexFromUniqueIdPath(self, unique_id_path: Sequence[int], root_index: QtCore.QModelIndex = ...) -> QtCore.QModelIndex | None:
        """
        Given a unique id path returned from item.getUniqueIdPath(),
        find the item corresponding to this id path and return
        its model index.
        """
    def findIndexFromItem(self, item: ssmi.BaseItem | None, root_index: QtCore.QModelIndex = ...) -> QtCore.QModelIndex | None:
        """ Given an item in the model, find and return its model index. """
    def sort(self) -> None:
        """ Sort the top level items. """
    def columnCount(self, index: _Index) -> int:
        """
        The number of columns in the model. Currently there are four,
        Name, Character Visibility, Control Visibility, and Selection.
        """
    def rowCount(self, index: _Index | None = ...) -> int:
        """ The number of rows in the model rooted under index. """
    def beginInsertRows(self, *args: Unpack[tuple[_Index, int, int]], **kwargs: Never) -> None: ...
    def endInsertRows(self) -> None: ...
    def addChildren(self, items: Collection[ssmi.BaseItem], parent_index: _Index = ...) -> None:
        """ Add children to the model. """
    def addChild(self, item: ssmi.BaseItem, parent_index: _Index = ...) -> None:
        """ Add a child to the model. """
    def addChildByItem(self, item: ssmi.BaseItem, parent_item: ssmi.BaseItem | None, parent_index: _Index | None = None) -> None:
        """ Add a child to the model. """
    def insertChild(self, item: ssmi.BaseItem, row: int, parent_index: _Index = ...) -> None:
        """ Add a child to the model. """
    def index(self, row: int, column: int, parent: _Index = ...) -> QtCore.QModelIndex:
        """ Get the index from the row and column and given parent. """
    def parent(self, index: _Index) -> QtCore.QModelIndex:
        """ Get the parent index from an index. """
    def topAncestor(self, index: _IndexT) -> _IndexT | QtCore.QModelIndex:
        """ Find the top ancestor above index. """
    def editableAncestor(self, index: _Index) -> QtCore.QModelIndex:
        """ Find the first editable ancestor above index. """
    def child(self, row: int, parent: _Index = ...) -> QtCore.QModelIndex:
        """ Get the child of parent at row w.r.t. parent. """
    def itemFromIndex(self, index: _Index | None) -> ssmi.BaseItem | None:
        """ Get the item from the index. """
    def colorFromRgba(self, col: int) -> QtGui.QColor: ...
    def data(self, index: _Index, role: int = ...) -> _ItemData:
        """ Get the data from an index and given role. """
    def setData(self, index: _Index, data: str, role: int = ...) -> bool:
        """ Set the data at an index. """
    @setsUpdated
    def renameItem(self, item: ssmi.BaseItem, name: str) -> None:
        """ Rename the item. """
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...) -> str | QtGui.QIcon | QtCore.QSize | QtCore.Qt.AlignmentFlag | None:
        """ Get the header data for the given section. """
    def flags(self, index: _Index) -> QtCore.Qt.ItemFlag:
        """ Get the flags at an index. """
    def removeRows(self, row: int, count: int, parent_index: _Index = ...) -> bool:
        """ Remove count rows starting at row from parent. """
    def removeRowsByItem(self, row: int, count: int, parent_item: ssmi.BaseItem | None, parent_index: _Index | None = None) -> None: ...
    def insertRows(self, row: int, count: int, parent: _Index) -> bool:
        """
        Insert rows beginning at row, and ending at row+count-1 under
        the item with index 'parent'.
        """
    def removeChildren(self, index: _Index) -> None:
        """ Clear the children from index. """
    def supportedDropActions(self) -> QtCore.Qt.DropAction:
        """
        Qt override to return the supported actions for dragging
        and dropping in the trees.
        """
    def getDropItems(self) -> list[ssmi.BaseItem]:
        """ Return the new items created during the drop. """
    def mimeData(self, indexes: Sequence[QtCore.QModelIndex]) -> QtCore.QMimeData:
        """
        Qt reimplement to handle storing the items that will be
        internal moved.
        """
    def canDropMimeData(self, data: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent: _Index) -> bool:
        """
        Qt reimplement for telling it if it can drop the data
        at the given spot.

        Use this to disable dragging items past the persistent
        sets: the current selection, and the all controls set.
        """
    def dropMimeData(self, data: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent: _Index) -> bool:
        """ Qt reimplement to handle dropping internal moves. """
    def onPostDrop(self) -> None: ...
    def updateColorStates(self, item: ssmi.BaseItem | None = None) -> None:
        """ Update colour states for all items under item. """
    def _emitDecorationChanged(self, item: ssmi.BaseItem | None) -> None: ...
    def _updateStateTopDown(self, item: ssmi.BaseItem | None = None, selected_state: bool = True, visibility_state: bool = True, character_state: bool = True, pin_state: bool = True, control_count: bool = True, has_pattern: bool = True, isolate_state: bool = True, while_loading: bool = False) -> None:
        """ Update the state of all items rooted under item. """

class SelectionManagerModelHandle(QtObjectHandle[SelectionManagerModel]):
    """ A wrapper class used to hold and manage the life cycle
        of an SelectionManagerModel
    """
    def __init__(self, *args: Unpack[tuple[()]], **kwargs: Unpack[_ModelKwargs]) -> None: ...

class IdentityProxyModel(plIdentityProxyModel):
    """ Subclass the identity proxy model from the poselib to add in
        callbacks for sending out layout changed signals.
    """
    def setSourceModel(self, model: SelectionManagerModel) -> None:
        """ Override to set the source model. """
    def modelImpl(self) -> ssimpl.ModelImpl:
        """ The implementation part of the model. """
    def qtModel(self) -> Self:
        """ The qt part of the model. """
    def qtSourceModel(self) -> SelectionManagerModel:
        """ The source qt part of the model. """
    def sourceModel(self) -> SelectionManagerModel: ...

class TreeProxyModel(IdentityProxyModel):
    """ A proxy model for the tree view that will let us customize
        what is shown in individual panels.
    """
    def __init__(self, *args: Unpack[tuple[QtCore.QObject | None, SelectionManagerModel]]) -> None: ...
    def setShowRigs(self, val: bool) -> None:
        """ Set whether to show rig items in the tree.
            When rigs are set to not be shown the controls
            will be shown directly under the character item.
        """
    def setShowImportChars(self, val: bool) -> None: ...
    def setShowTags(self, val: bool) -> None:
        """ Set whether tags are visible in the names of items with them. """
    def setShowCount(self, val: bool) -> None:
        """ Set whether we show the count next to the name. """
    def setShowPatterns(self, val: bool) -> None:
        """ Set whether we show the patterns after the name. """
    def setShowIds(self, val: bool) -> None:
        """ Set whether we show unique ids after the name. This
            is for debug purposes only.
        """
    def data(self, proxy_index: _Index, role: int = ...) -> _ItemData:
        """ Get the data from an index and given role. """
    def mapFromSource(self, source_index: _Index, filtered: bool = True) -> QtCore.QModelIndex:
        """ Map the source index to a proxy index. """
    def index(self, row: int, column: int, parent: _Index = ...) -> QtCore.QModelIndex:
        """ Get the proxy index under parent at row, column. """
    def parent(self, proxy_index: _Index) -> QtCore.QModelIndex:
        """ Get the parent proxy index of proxy_index. """
    def rowCount(self, parent: _Index = ...) -> int:
        """ Get the number of children under parent. """
    def removeRows(self, row: int, count: int, parent: _Index = ...) -> bool:
        """ Remove count rows starting at row under parent. """
    def itemFromIndex(self, proxy_index: _Index) -> ssmi.BaseItem | None:
        """ Get the item from the proxy index. """
    def canDropMimeData(self, data: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent_proxy_index: _Index) -> bool: ...
    def dropMimeData(self, data: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent_proxy_index: _Index) -> bool: ...

class TreeProxyModelHandle(QtObjectHandle[TreeProxyModel]):
    """ A wrapper class used to hold and manage the life cycle
        of an TreeProxyModel
    """
    def __init__(self, *args: Unpack[tuple[QtCore.QObject | None, SelectionManagerModel]], **kwargs: Never) -> None: ...

def createIcon(name: str, size: int = ...) -> hou.qt.Icon: ...
def reloadIcons() -> None: ...

APPLY_MODE_GUESS: Final[Literal[0]]
APPLY_MODE_CHAR: Final[Literal[1]]
APPLY_MODE_RIG: Final[Literal[2]]
SEL_MGR_VERSION: int
CONFIG_SETS_KEY: str
CONFIG_VERSION_KEY: str
CONFIG_STATES_KEY: str
CONFIG_REMAP_KEY: str
CONFIG_LABELS_KEY: str
CONFIG_SEL_STATE_KEY: str
CONFIG_VIS_STATE_KEY: str
CONFIG_CHAR_STATE_KEY: str
CONFIG_PIN_STATE_KEY: str
DEFAULT_CONFIG_KEYS: list[str]
EXPAND_PROPERTY: str
SEL_SET_ATTRIB: str
