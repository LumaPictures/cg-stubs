import apex.ui.selectionmanager.modelitem as ssmi
import apex.ui.selectionmanager.utils as ssu
import dbg
import hou
from PySide6 import QtCore as QtCore
from apex.animationcatalog import _ControlTree
from apex.ui.selectionmanager.model import IdentityProxyModel as IdentityProxyModel, SelectionManagerModel as SelectionManagerModel, _Color, _Index, _RigPatternsLookup
from apex.ui.selectionmanager.modelconfig import _ExportedSet, _LabelTree, _Model, _SetDiff, _States
from collections.abc import Collection, Iterable, Sequence
from typing import Literal, Self

from typing import TypeAlias
from typing import TypeAlias
_QtModel: TypeAlias = SelectionManagerModel | IdentityProxyModel
_BlockModel: TypeAlias = _Model | IdentityProxyModel
APPLY_MODE_GUESS: int
APPLY_MODE_CHAR: int
APPLY_MODE_RIG: int
CUR_SEL_ITEM_NAME: str
ALL_CTRL_ITEM_NAME: str
ALL_CONSTR_ITEM_NAME: str
LOADING_BLOCK_KEY: str
MULTI_CHANGE_KEY: str
CURRENT_SELECTION_KEY: str
SORT_DISABLER_KEY: str
RESET_MODEL_KEY: str
LAYOUT_CHANGE_KEY: str
CONFIG_SEL_STATE_KEY: str
CONFIG_VIS_STATE_KEY: str
CONFIG_CHAR_STATE_KEY: str
CONFIG_HIDDEN_SETS_KEY: str
CONFIG_HIDDEN_CONTROLS_KEY: str

def computeSavedTreeDiff(tree_a: Sequence[_ExportedSet], tree_b: Sequence[_ExportedSet]) -> list[_SetDiff]:
    """
    Compute a diff between two json tree descriptions
    of the selection sets.
    """

class VisibilityStatesCache:
    model: ModelImpl
    isolate_enabled: bool
    controls_visible: bool
    def __init__(self, model: ModelImpl) -> None: ...
    def hide(self) -> None: ...
    def show(self) -> None: ...
    def push(self) -> None: ...

class LoadingBlock(ssu.GenericBlock[_Model]):
    """
    Encapsulate a block wrapping the explicit loading of elements
    into the model.

    Prevent auto saving in the loading block if we load something
    that emits a signal that tells us to save while we are loading.
    """
    def __init__(self, parent: _Model) -> None: ...
    def __exit__(self, *args: object) -> None: ...
UpdateDisabler = LoadingBlock

class UpdateCurrentSelectionBlock(ssu.GenericBlock['ModelImpl']):
    """
    A block for disabling updating the current selection while updating it.
    """
    def __init__(self, parent: ModelImpl) -> None: ...

class SortDisabler(ssu.GenericBlock['ModelImpl']):
    """
    A block used for disabling sorting.

    The tree is auto-sorted on layout change. Sorting also
    emits a layout change. This ensures that if the layout is
    changed as a result of sorting, it doesn't try to sort
    again, resulting in an infinite loop.
    """
    def __init__(self, parent: ModelImpl) -> None: ...

class ModelImplBlock(ssu.GenericBlock[_Model]):
    def __init__(self, model_impl: _BlockModel, key: str) -> None: ...
    def enterWithQt(self, model_qt: _QtModel) -> None: ...
    def enterWithImpl(self, model_impl: ModelImpl) -> None: ...
    def exitWithQt(self, model_qt: _QtModel) -> None: ...
    def exitWithImpl(self, model_impl: ModelImpl) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: object) -> None: ...

class LayoutChangeBlock(ModelImplBlock):
    """
    A block wrapping any layout changed.
    Emits a layoutAboutToBeChanged when entered,
    and a layoutChanged when exited.

    Can only be used on a QAbstractItemModel.
    """
    def __init__(self, model_impl: _BlockModel) -> None: ...
    def enterWithQt(self, model_qt: _QtModel) -> None: ...
    @dbg.ZoneScopedDecorator
    def exitWithQt(self, model_qt: _QtModel) -> None: ...
    @dbg.ZoneScopedDecorator
    def exitWithImpl(self, model_impl: ModelImpl) -> None: ...

class ResetModelBlock(ModelImplBlock):
    """
    A block wrapping model reset changes.
    """
    def __init__(self, model_impl: _BlockModel) -> None: ...
    def enterWithQt(self, model_qt: _QtModel) -> None: ...
    @dbg.ZoneScopedDecorator
    def exitWithQt(self, model_qt: _QtModel) -> None: ...
    @dbg.ZoneScopedDecorator
    def exitWithImpl(self, model_impl: ModelImpl) -> None: ...

class MultiChangeBlock(ssu.GenericBlock[_Model]):
    """ A block used for disabling full structure updating
    """
    def __init__(self, parent: _Model) -> None: ...

class LightLayoutChangeBlock(MultiChangeBlock):
    """ Use to mute the model's special handling of layout change
        blocks that sorts the rows and updates all icons. This is
        for updating these things in a more precise way inside the
        block and just letting the view pick up the layout change
        to know to update.
    """
    def __enter__(self) -> None: ...
    def __exit__(self, *args: object) -> None: ...

class LayoutMultiChangeBlock(MultiChangeBlock):
    """ Use when doing multiple changes that can emit layout changed or
        structure changed, and you only want to actually handle it once.
    """
    def __enter__(self) -> None: ...
    def __exit__(self, *args: object) -> None: ...

class ModelImpl:
    def __init__(self, qt_model: SelectionManagerModel | None = None) -> None: ...
    @property
    def qt_model(self) -> SelectionManagerModel | None: ...
    def setupInitialItems(self) -> None:
        """ Set up the root, all controls, and current selection items. """
    def modelImpl(self) -> Self:
        """ Get the implementation part of the model. """
    def qtModel(self) -> SelectionManagerModel | None:
        """ Get the Qt part of the model if it exists. """
    def qtSourceModel(self) -> SelectionManagerModel:
        """ The source qt part of the model. """
    def parent(self, item: ssmi.BaseItem, index: _Index | None = None) -> tuple[ssmi.BaseItem | None, QtCore.QModelIndex | None]: ...
    def child(self, row: int, item: ssmi.BaseItem, index: _Index | None = None) -> tuple[ssmi.BaseItem, QtCore.QModelIndex | None]: ...
    def addChildByItem(self, item: ssmi.BaseItem, parent_item: ssmi.BaseItem, parent_index: _Index | None = None) -> None:
        """ Add child to item, if Qt model exists sends appropriate signals. """
    def clearSetsByItem(self, item: ssmi.BaseItem, index: _Index | None = None) -> None:
        """ Clear the sets under the parent_item. """
    def removeItem(self, item: ssmi.BaseItem, index: _Index | None = None) -> None:
        """ Remove item. """
    def removeRows(self, row: int, count: int, parent_item: ssmi.BaseItem, parent_index: _Index | None = None) -> None: ...
    def itemFromIndex(self, index: _Index | None) -> ssmi.BaseItem | None:
        """ Get item from index if qt model exists. """
    def findIndexFromItem(self, item: ssmi.BaseItem | None) -> QtCore.QModelIndex | None:
        """ Get an index from item if qt model exists. """
    def getRoot(self) -> ssmi.RootItem:
        """ Get the root item. """
    def getCurSelItem(self) -> ssmi.CurrentSelectionItem:
        """ Get the item for the current selection. """
    def getAllControlsItem(self) -> ssmi.AllControlsItem:
        """ Get the item for all controls. """
    def getAllConstraintsItem(self) -> ssmi.AllConstraintsItem:
        """ Get the item for all constraints. """
    def getSetItems(self) -> list[ssmi.BaseItem]:
        """ Get set items not including current selection or all controls. """
    def getBlockManager(self, key: int | str | None = None) -> ssu.BlockLevelManager | None:
        """ Get a block manager by key. This is needed by ssu.BlockManagers(). """
    def isLoading(self) -> bool:
        """
        Whether we are currently loading the model. While doing this
        we probably don't want to save.
        """
    def isSorting(self) -> bool:
        """ Whether we are currently sorting. """
    def isChangingLayout(self) -> bool:
        """ Whether we are currently changing the layout. """
    def isChangingModel(self) -> bool:
        """
        Whether we are currently performing an operation that will require
        a model reset.
        """
    def sort(self) -> None:
        """ Sort the top level items. """
    def getLoadingBlock(self) -> LoadingBlock:
        """
        Get a loading block to wrap some actions. This prevents
        updating all the states of the items while in the block
        until the end.
        """
    def getResetModelBlock(self) -> ResetModelBlock:
        """ Get a reset model block. """
    def inMultiChangeBlock(self) -> bool:
        """
        Whether the model is doing multiple changes for which we
        want to disable certain auto updates until the changes are done.
        Places where this might be used:
        1. Changing the state of many items.
        2. Restructuring the tree.
        3. Adding or removing many items at a time.
        """
    def isUpdatingCurrentSelection(self) -> bool:
        """ Whether currently updating current selection. """
    def nextUniqueId(self) -> int:
        """
        Get the next unique id to give to an item. Since the names
        can be shared, but that makes some things very hard to keep
        track of, we can associate unique ids with items and use these
        as unique names where needed.
        """
    def getRemapPatterns(self) -> tuple[str, str]:
        """ Get the patterns used when mirroring sets. """
    def setRemapPatterns(self, left_pattern: str, right_pattern: str) -> None:
        """ Set the patterns used when mirroring sets. """
    def getSetRemapPatterns(self) -> tuple[str, str]:
        """ Get the patterns for renaming sets when mirroring sets. """
    def setSetRemapPatterns(self, left_pattern: str, right_pattern: str) -> None:
        """ Set the patterns used for renaming sets when mirroring sets. """
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
        """ Get the top level items in the controls tree that are
            considered characers. This only includes active characters.
        """
    def getAllConstraints(self) -> _ControlTree:
        """ Get the items in the controls tree that are considered constraints.
        """
    def getCharactersInSetsByItems(self, items: Collection[ssmi.BaseItem] | None = None, include_tools: bool = True, include_motion_paths: bool = True, include_rigs: bool = False) -> _ControlTree:
        """ Get all character names that appear in sets, not just those active. """
    def getVisibleChars(self) -> _ControlTree:
        """ Get the visible characters. """
    def getVisibleConstraints(self) -> _ControlTree:
        """ Get the visible constraints. """
    def setCurrentSelection(self, controls_tree: _ControlTree) -> None:
        """ Set the current selection controls tree. """
    def isVisibilitySynced(self) -> bool:
        """ Whether the visibility is up to date. """
    def controlsVisible(self) -> bool:
        """ Whether the controls are visible. """
    def setControlsVisible(self, val: bool) -> None:
        """ Set whether the controls are visible. """
    def setVisibleControls(self, controls_tree: _ControlTree | None) -> None:
        """
        Set the visible controls in the tree. This changes the icon
        for the control visibility.
        """
    def toggleVisible(self, show: bool = True) -> None:
        """ Toggle whether all controls are visible. """
    def isVisibilityTempDisabled(self) -> bool:
        """ Whether showing controls is enabled. """
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
        Set the visible constraints in the tree. This changes the icon
        for the constraint visibility.
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
    def updateHasIsolate(self) -> None:
        """ Update whether there are isolated items. """
    def hasIsolate(self, only_if_enabled: bool = True) -> bool:
        """ Whether there are any isolated items. """
    def setHasIsolateExplicit(self, val: bool) -> None:
        """ Explicitly set whether we have isolated controls. """
    def isolateEnabled(self) -> bool:
        """ Whether isolating is enabled. """
    def setIsolateEnabled(self, val: bool) -> None:
        """ Enable or disable isolating items. """
    def clearIsolate(self) -> None:
        """ Clear all the isolate states in the tree. """
    def retrieveFromState(self) -> None:
        """ Retrieve stuff from the state. """
    def sortControlsByItem(self, item: ssmi.BaseItem) -> None:
        """ Sort the controls under parent_index. """
    def renameItem(self, item: ssmi.BaseItem, name: str) -> None:
        """ Rename the item. """
    def deleteSetsByItems(self, items: Iterable[ssmi.BaseItem]) -> None:
        """ Remove rows by items if editable. """
    def setRowColorByItem(self, items: Iterable[ssmi.BaseItem], color: _Color) -> None:
        """ Set the background colour of the specified rows. """
    def modifyPinByItem(self, item: ssmi.BaseItem, pick_modifier: hou.EnumValue[hou.pickModifier]) -> None:
        """ Modify the pin state for this item. """
    def modifyIsolateByItem(self, item: ssmi.BaseItem | None, pick_modifier: hou.EnumValue[hou.pickModifier]) -> None:
        """ Modify the isolate state for this item. """
    def clearPins(self) -> None:
        """ Clear all the pin states in the tree. """
    def expandPatternsByItem(self, item: ssmi.BaseItem | None) -> None:
        """ Expand the patterns under index. """
    def expandPatternsItems(self, items: Iterable[ssmi.BaseItem | None]) -> None:
        """ Expand the patterns under index. """
    def separateCharsByItem(self, item: ssmi.BaseItem | None) -> None:
        """
        API Function for separating characters under an index,
        will also wrap it in the necessary blocks for efficiency.
        """
    def separateCharsItems(self, items: Iterable[ssmi.BaseItem | None]) -> None:
        """
        API Function for separating characters under indexes,
        will also wrap it in the necessary blocks for efficiency.
        Use this for multiple rows as it will wrap the calls in
        a more efficient way.
        """
    def separateCharsIntoSetsByItems(self, items: Iterable[ssmi.BaseItem | None], remove_originals: bool = False) -> None:
        """ Make separate sets (recursively) for each character. """
    def replaceCharactersByItems(self, items: Iterable[ssmi.BaseItem | None], replace_chars_list: Collection[str], new_char_name: str) -> None:
        """
        Replace (possibly inactive) characters in sets with new_char_name.

        :indexes: A list of indexes to do the replace operation on.
        :replace_chars_list: A list of character names to replace.
        :new_char_name: The new character name to replace with.
        """
    def applyToCharsItems(self, items: Iterable[ssmi.BaseItem | None], chars_list: Sequence[str] | None = None, mode: Literal[0, 1, 2] | None = None) -> None:
        """
        API functuin for applying sets under an index to the
        provided characters. Use this version when working with
        multiple indexes as it will wrap the calls in a more
        efficient way.
        """
    def nextChildName(self, parent_item: ssmi.BaseItem | None = None, base_name: str | None = None, add_number_if_unique: bool = False) -> str:
        """ Get the next default set name. """
    def exportStates(self, filter_chars_tree: _ControlTree | None = None, filter_controls_tree: _ControlTree | None = None, override_chars: Iterable[str] | None = None) -> _States:
        """ Pack the states into a dictionary and then turn into a json string. """
    def exportStatesToJSON(self, filter_chars_tree: _ControlTree | None = None, filter_controls_tree: _ControlTree | None = None, override_chars: Iterable[str] | None = None) -> str:
        """ Pack the states into a dictionary and then turn into a json string. """
    def exportSelectionSetsByItems(self, unique_ids: bool = False, items: Sequence[ssmi.BaseItem | None] | None = None, export_properties: Collection[str] | None = None, export_persistant: bool = False) -> list[_ExportedSet]:
        """
        Package the selection sets into a JSON-Compatible
        format and return it.
        """
    def exportToJSONByItems(self, items: Sequence[ssmi.BaseItem | None] | None = None, export_properties: Collection[str] | None = None, export_persistant: bool = False) -> str:
        """ Create a json string representation of the sets. """
    def loadSelectionSetsByItem(self, sel_sets_dict: Iterable[_ExportedSet], clear: bool = True, editable: bool = True, undo: bool = False, replace_char: str | None = None, root_item: ssmi.BaseItem | None = None) -> list[ssmi.BaseItem]:
        """
        Load the selection sets from a stored selection sets
        dictionary.
        """
    def importFromJSONByItem(self, json_string: str | None, clear: bool = True, editable: bool = True, undo: bool = False, replace_char: str | None = None, root_item: ssmi.BaseItem | None = None) -> list[ssmi.BaseItem]:
        """ Given a json representation of the sets, load them. """
    def importFromGeometryByItem(self, geometry: hou.Geometry, clear: bool = True, editable: bool = True, undo: bool = False, load_states: bool = False, load_character_sets: bool = False, char_geometry: hou.Geometry | None = None, parent_item: ssmi.BaseItem | None = None) -> None:
        """ Import selection sets from a geometry with the proper attribute. """
    def applyDiff(self, diff: Iterable[_SetDiff], reverse: bool = False) -> None:
        """ Apply a diff at the root level to update the tree. """
    def updateColorStates(self, item: ssmi.BaseItem | None = None) -> None:
        """ Update colour states for all items under item. """
    def createControlSetByItem(self, controls_tree: _ControlTree, name: str | None = None, parent: ssmi.BaseItem | None = None, active_control_path: Sequence[str] | None = None, parent_index: _Index | None = None) -> ssmi.RootFolderItem:
        """
        Create a new controls set from the controls_tree within the set.

        :controls_tree: The tree of controls to put in the set.
        :name: An optional name to give to the new set. If left None,
               will use the next default child name.
        """
    def modifyControlSetByItem(self, controls_tree: _ControlTree, item: ssmi.BaseItem | None, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None, modify_patterns: bool = True, update_states: bool = True, parent_index: _Index | None = None) -> None:
        """ Add or remove elements from a set. """
    def duplicateSetsByItems(self, items: Iterable[ssmi.BaseItem]) -> list[ssmi.BaseItem]:
        """ Duplicate the sets in the provided indexes. """
    def mirrorSetsByItems(self, items: Iterable[ssmi.BaseItem], rig_patterns_lookup: _RigPatternsLookup | None = None) -> list[ssmi.BaseItem]:
        """ Mirror the sets in the provided indexes. """
    def patternRenameSetsByItems(self, from_pattern: str, to_pattern: str, items: Iterable[ssmi.BaseItem | None]) -> None:
        """
        Rename the sets with the given indexes matching from_pattern
        to to_pattern.
        """
    def patternRenameAllSetsByItem(self, from_pattern: str, to_pattern: str, parent_item: ssmi.BaseItem | None = None) -> None:
        """
        Rename all sets under the parent index matching the from_pattern
        to to_pattern.
        """
    def setControlActiveSingleByItem(self, paths: Sequence[str], root_item: ssmi.BaseItem | None, val: bool) -> None:
        """
        Set the control found by following paths from root_item
        to be active.
        """
    def setSetActiveControlByItem(self, new_active_control: ssmi.BaseItem | None) -> None:
        """ Set the control with the given index to be active. """
    def setActiveControl(self, control: list[str]) -> None:
        """ Set the active control given a control path. """
    def activeControl(self) -> list[str]:
        """ The control path for the item that currently has the handle. """
    @dbg.ZoneScopedDecorator
    def _updateStateTopDown(self, item: ssmi.BaseItem | None = None, selected_state: bool = True, visibility_state: bool = True, character_state: bool = True, constraint_state: bool = True, pin_state: bool = True, control_count: bool = True, has_pattern: bool = True, isolate_state: bool = True, while_loading: bool = False) -> None:
        """ Update the state of all items rooted under item. """
