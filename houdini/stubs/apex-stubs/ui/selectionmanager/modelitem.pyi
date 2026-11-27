import hou
import typing
from PySide6 import QtCore as QtCore, QtGui as QtGui
from apex.animationcatalog import _ControlTree
from apex.ui.selectionmanager.model import SelectionManagerModel as SelectionManagerModel, _Color, _Index, _RigPatternsLookup
from apex.ui.selectionmanager.modelconfig import _ExportedSet, _ItemType, _LabelTree, _SetDiff
from apex.ui.selectionmanager.modelimpl import ModelImpl as ModelImpl
from apex.utils import timing as timing
from collections.abc import Callable as Callable, Collection, Iterable, Mapping, Sequence
from typing import Concatenate, Literal, Never, TypedDict, Unpack

from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
from typing import ParamSpec
from typing import TypeAlias
from typing import TypeVar
_T = TypeVar('_T')
_P = ParamSpec('_P')
_R = TypeVar('_R')
_ItemT = TypeVar('_ItemT', bound='BaseItem')
_TreeT = TypeVar('_TreeT', _ControlTree, _LabelTree)
_CopyStructure: TypeAlias = Mapping[int | None, '_CopyStructure']
_StateKey: TypeAlias = Literal[0, 1, 2, 3, 4, 5, 6, 7]
class _ItemKwargs(TypedDict, total=False):
    name: str
    model: SelectionManagerModel | None
    unique_id: int | None
    modelimpl: ModelImpl | None

ROOT_ITEM_NAME: str
START_SET_NAME: str
TYPE_ROOT_FOLDER: Literal['Folder']
TYPE_GROUP: Literal['Group']
TYPE_CONTROL_GROUP: Literal['ControlGroup']
TYPE_CONTROL: Literal['Control']
TYPE_CHARACTER: Literal['Character']
TYPE_CONSTRAINT: Literal['Constraint']
TYPE_RIG: Literal['Rig']
TYPE_GEO: Literal['Geo']
TYPE_TOOL_CHAR: Literal['Tool']
TYPE_MULTI_CTRL_CHAR: Literal['MultiCtrl']
TYPE_CHAR_TAG: Literal['char']
TYPE_RIG_TAG: Literal['rig']
TYPE_GEO_TAG: Literal['geo']
TYPE_DIR_TAG: Literal['dir']
TYPE_TOOL_CHAR_TAG: Literal['tool']
TYPE_CONSTRAINT_TAG: Literal['constr']
TYPE_MULTI_CTRL_CHAR_TAG: Literal['ctrl']
HIDDEN_RIG_TYPES: list[str]
NAME_COLUMN: Literal[0]
ISOLATEICON_COLUMN: Literal[1]
VIEWCHARICON_COLUMN: Literal[2]
VIEWCONSTRICON_COLUMN: Literal[3]
VIEWICON_COLUMN: Literal[4]
SELECTICON_COLUMN: Literal[5]
PINICON_COLUMN: Literal[6]
CHAR_ON_TOOLTIP: str
CHAR_OFF_TOOLTIP: str
CONSTR_ON_TOOLTIP: str
CONSTR_OFF_TOOLTIP: str
TOOL_ON_TOOLTIP: str
TOOL_OFF_TOOLTIP: str
GEO_ON_TOOLTIP: str
GEO_OFF_TOOLTIP: str
VIEW_ON_TOOLTIP: str
VIEW_OFF_TOOLTIP: str
SELECT_ON_TOOLTIP: str
SELECT_OFF_TOOLTIP: str
PIN_ON_TOOLTIP: str
PIN_OFF_TOOLTIP: str
ISOLATE_ON_TOOLTIP: str
ISOLATE_OFF_TOOLTIP: str
CONTROLS_SELECTED_KEY: Literal[0]
CONTROLS_VISIBLE_KEY: Literal[1]
CONTROLS_CHARACTER_KEY: Literal[2]
CONTROLS_CONSTRAINT_KEY: Literal[3]
CONTROLS_PINNED_KEY: Literal[4]
CONTROLS_ISOLATE_KEY: Literal[5]
CONTROLS_INTERNAL_ISO_KEY: Literal[6]
CONTROLS_COLOR_KEY: Literal[7]
STATE_OFF: Literal[0]
STATE_PARTIAL: Literal[1]
STATE_ON: Literal[2]

def isCharTypeTag(tag: str | None, include_tools: bool = True, include_motion_paths: bool = True, include_rigs: bool = False) -> bool:
    """ Whether the given tag is a character type.
        Used to determine if the items below it should
        default to being rigs.
    """
def isNameCharTag(name: str, include_tools: bool = True, include_motion_paths: bool = True, include_rigs: bool = False) -> bool: ...
def extractChars(controls_tree: _ControlTree, include_tools: bool = True, include_motion_paths: bool = True, include_rigs: bool = False, depth: int = 0) -> _ControlTree: ...
def filterLabelTree(controls_tree: _TreeT) -> _TreeT: ...
def extractConstraints(controls_tree: _ControlTree) -> _ControlTree: ...
def extractConstraintTree(controls_tree: _ControlTree | None, in_constraint: bool = False) -> _ControlTree: ...
def mirrorExportedSet(export_set_tree: _ExportedSet, left_pattern: str | None = None, right_pattern: str | None = None, left_set_pattern: str | None = None, right_set_pattern: str | None = None, rig_patterns_lookup: _RigPatternsLookup | None = None, rig_path: str | None = None) -> None:
    """ Take the exported json structure for the set, and mirror it. """
def uniqueNameDisabler(fn: Callable[Concatenate[_ItemT, _P], _R]) -> Callable[Concatenate[_ItemT, _P], _R]: ...

class BaseItem:
    """
    The base item type for the SelectionManagerModel.
    All items in the tree are derived from this type.
    """
    def __init__(self, name: str, model: SelectionManagerModel | None, unique_id: int | None = None, modelimpl: ModelImpl | None = None) -> None: ...
    def setProperty(self, key: str, val: bool, and_children: bool = False) -> None:
        """ Set properties, these are just extra bits of data,
            that may or may not be saved.
        """
    def removeProperty(self, key: str, and_children: bool = False) -> None:
        """ Remove a property. """
    @typing.overload
    def getProperty(self, *args: Unpack[tuple[str]], **kwargs: Never) -> bool | None: ...
    @typing.overload
    def getProperty(self, *args: Unpack[tuple[str, _T]], **kwargs: Never) -> bool | _T: ...
    def labelsTree(self) -> _LabelTree: ...
    def applyLabels(self, label_tree: _LabelTree, item_tree: Mapping[str, str | _LabelTree] = ..., full_update: bool = False) -> None: ...
    def controlTree(self, include_ancestors: bool = False, filter_pred: Callable[[BaseItem], bool] | None = None) -> _ControlTree:
        """ Build the control tree format from the structure. """
    def copy(self, new_name: str | None = None) -> BaseItem:
        """ Perform a shallow copy of my self and return it. """
    def deepcopy(self, new_name: str | None = None) -> BaseItem:
        """ Perform a deep copy of my self and return it. """
    def copyStructureForChar(self, copy_structure: _CopyStructure, char_name: str, rename_fn: Callable[[str, str], str], all_controls_tree: _ControlTree | None) -> BaseItem | None:
        """ Make a deepcopy of self, with a new name, and only keeping controls
            for the specified character name.
        """
    def resetNumControls(self) -> None:
        """ Reset the number of controls for self and all descendants. """
    def updateNumControls(self, all_controls_tree: _ControlTree) -> None:
        """ Reset the number of controls for all children then
            update the number of controls for self and all descendants
            using the provided tree of all controls to match against.
        """
    def getNumControls(self) -> int:
        """ Get the cached number of controls under this item. """
    def getNumConstraints(self) -> int:
        """ Get the cached number of constraints under this item. """
    def isEditable(self) -> bool:
        """ Whether this item is editable. """
    def setEditable(self, editable: bool, and_children: bool = True) -> None:
        """ Set the editable state of this item and all its descendants. """
    def setColor(self, color: _Color, and_children: bool = False) -> None:
        """ Set the background color for this item, and optionally
            for all descendants as well.
        """
    def color(self) -> QtGui.QColor | int | None:
        """ Get the background color, or None if none has been specified. """
    def colorRGBA(self) -> int: ...
    def acceptsState(self, key: _StateKey) -> bool: ...
    def endsState(self, key: _StateKey) -> bool: ...
    def updateStateTopDown(self, key: _StateKey, control_tree: _ControlTree | None = None, force_state: int | None = None) -> int:
        """ Update the icon states for the states with the given key. """
    def updateSelectStates(self, control_tree: _ControlTree | None = None) -> None:
        """ Update the state of selected icons. """
    def updateVisibleStates(self, control_tree: _ControlTree | None = None) -> None:
        """ Update the state of the control visibility icons. """
    def updateInternalIsolateStates(self, control_tree: _ControlTree | None = None) -> None:
        """ Update the internal isolate visibility state of the controls. """
    def updateCharacterStates(self, control_tree: _ControlTree | None = None) -> None:
        """ Update the state of the character icons. """
    def updateConstraintStates(self, control_tree: _ControlTree | None = None) -> None:
        """ Update the state of the constraint icons. """
    def updatePinStates(self) -> None:
        """ Update the state of the pin icons. """
    def updateIsolateStates(self) -> None:
        """ Update the isolate states. """
    def updateColorStates(self) -> None:
        """ Update whether items have stored colours. """
    def updateStateBottomUp(self, key: _StateKey) -> None:
        """ Update the states of icons that are bottom up. This means
            you explicitly set the state on an item and it propagates
            the partial upwards, as opposed to matching controls based
            on a control tree (top down).

            Note that this assumes that an item has STATE_ON if and only if
            it is considered to be active.
        """
    def updateStateFromChildren(self, key: _StateKey, update_ancestors: bool = True) -> None:
        """ Update the state based on the children, and
            continue propagating upwards.
        """
    def setStateBottomUp(self, key: _StateKey, val: int, update_ancestors: bool = True, check_children: bool = False) -> None:
        """ Set a state in a bottom up way, and propagate upwards. """
    def modifyStateBottomUp(self, key: _StateKey, pick_modifier: hou.EnumValue[hou.pickModifier], update_ancestors: bool = True) -> None:
        """ Modify the state in a bottom up way, and propagate upwards. """
    def clearState(self, key: _StateKey, and_children: bool = True, update_ancestors: bool = True) -> None:
        """ Clear the bottom up state key. """
    def modifyState(self, key: _StateKey, pick_modifier: hou.EnumValue[hou.pickModifier], update_ancestors: bool = True) -> None:
        """ Modify the bottom up state key. """
    def setPin(self, val: int, update_ancestors: bool = True) -> None:
        """ Set the pin state. """
    def modifyPin(self, pick_modifier: hou.EnumValue[hou.pickModifier], update_ancestors: bool = True) -> None:
        """ Modify the pin state based on a pick modifier. """
    def clearPins(self, and_children: bool = True, update_ancestors: bool = True) -> None:
        """ Clear the pins in the hierarchy. """
    def setIsolate(self, val: int, update_ancestors: bool = True) -> None:
        """ Set the pin state. """
    def modifyIsolate(self, pick_modifier: hou.EnumValue[hou.pickModifier], update_ancestors: bool = True) -> None:
        """ Modify the pin state based on a pick modifier. """
    def clearIsolate(self, and_children: bool = True, update_ancestors: bool = True) -> None:
        """ Clear the pins in the hierarchy. """
    def hasModel(self) -> bool:
        """ Whether there is a model. """
    def row(self) -> int:
        """ The index of this item in the parents children list. """
    def setRow(self, row: int) -> None:
        """ Set the index in the parents children list. """
    def parent(self) -> BaseItem | None:
        """ Get the parent item. """
    def topParent(self) -> BaseItem:
        """ Get the top level parent item. """
    def editableAncestor(self) -> BaseItem: ...
    def isValid(self) -> bool | BaseItem | None:
        """ Whether the item is valid. If no parent and not root,
            is invalid and will be deleted.
        """
    def setParent(self, parent: BaseItem | None) -> None:
        """ Set the parent item of this item. """
    def isRoot(self) -> bool:
        """ Whether this item is a root item. """
    def isFolder(self) -> bool:
        """ Whether this item is a root folder type. """
    def isPresent(self) -> bool:
        """ Whether this item is present in the tree. This may be false
            for items like the controls and constraints
        """
    def setPresent(self, present: bool) -> bool:
        """ For types which can act as items or groups like controls and
            constraints, this should be overriden
        """
    def isCharacter(self) -> bool:
        """ Whether this item is a character type. """
    def isControl(self) -> bool:
        """ Whether this item is a control type. """
    def isConstraint(self) -> bool:
        """ Whether this item is a constraint type. """
    def isRig(self) -> bool:
        """ Whether this item is a rig type. """
    def isInRig(self) -> bool:
        """ Whether this item is an object within a rig.
        """
    def isSelectable(self) -> bool:
        """ Whether this item is selectable.
        """
    def enabled(self) -> bool:
        """ Wether this item is enabled. """
    def topSortKey(self) -> int:
        """ The key used to sort when this is a top level item. """
    def addChild(self, child: BaseItem) -> None:
        """ Add a child to this item. """
    def insertChild(self, child: BaseItem, row: int) -> None:
        """ Insert child at row, move the other children up, and
            increment their rows.
        """
    def replaceChild(self, child_row: int, other: BaseItem, copy_unique_id: bool = False) -> None:
        """ Replace myself in the tree with other. """
    def removeChildByIndex(self, index: int) -> None:
        """ Remove a child item by index. """
    def removeChildrenByIndex(self, start_index: int, count: int) -> None:
        """ Remove multiple children by index and count. """
    def updateChildRows(self) -> None:
        """ Update the stored child row indices. """
    def hasNonFolderChildren(self) -> bool:
        """ Whether this item has children which are not folders. """
    def addControlSubTree(self, dict_tree: _ControlTree, depth: int = 0, parent_index: _Index | None = None, use_index: bool = True) -> None:
        """ Add a control sub tree to this item.

            :dict_tree: A dictionary structure representing the control
                        tree to be added under this item.
            :is_root: Whether this item is at the top of the tree.
                      If so, the first level of children will be
                      CharacterItem, otherwise ControlItem.
        """
    def modifyControlSubTree(self, dict_tree: _ControlTree, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None, parent_index: _Index | None = None, modify_patterns: bool = True, use_index: bool = True) -> int:
        """ Modify the control sub tree by adding or removing from it.
            :modify_patterns: Whether to consider children with pattern names
                or just skip over them. Note that removing from sets with this
                turned off will skip over patterns so anything selected by the
                pattern will not be removed.
        """
    def isPersistant(self) -> bool:
        """ Whether this is auto removed when clear is called on a parent."""
    def clear(self, keep_persistant: bool = True) -> None:
        """ Clear the sub trees from this item. """
    def nextChildName(self, base_name: str | None = None, add_number_if_unique: bool = False, skip_child: BaseItem | None = None) -> str:
        """ Get the next default set name. """
    def loadSelectionSets(self, json_tree: Iterable[_ExportedSet], editable: bool = True, replace_char: str | None = None, parent_special: bool = False) -> list['BaseItem']:
        """ Load the selection sets rooted under this item
            from the json tree.
            Assumes that 'self' has already been loaded from the
            tree, and so only the children will be modified.

            :json_tree: An array of dictionaries.
                Each item in the array represents a sub tree.
                In each sub tree, the 'name' key specifies
                the name of the item, and the 'type' key specifies
                the type of the item, which can be one of
                {TYPE_ROOT_FOLDER, TYPE_CONTROL, TYPE_CHARACTER}.
        """
    def childCount(self) -> int:
        """ The number of children. """
    def child(self, row: int) -> BaseItem | None:
        """ Get a specific child by its index. """
    def getTag(self) -> str | None:
        """ Get the tag for this item, or None if no tag. """
    def checkUniqueFolders(self) -> bool: ...
    def updateName(self, name: str) -> None:
        """ Update my name. """
    def updateHasPatternUp(self) -> None:
        """ Update self and its ancestors for whether there are patterns. """
    def updateHasPattern(self) -> bool:
        """ Update whether this sub tree has any patterns. """
    def hasPattern(self) -> bool:
        """ Whether this sub tree has any patterns. """
    def getName(self) -> str:
        """ Get the name. """
    def getSubtreeKey(self) -> str:
        """ Get the key for the subtree """
    def getLabel(self) -> str | None: ...
    def setLabel(self, label: str | None) -> None: ...
    def getUniqueId(self) -> int | None:
        """ A unique identifier for each node. """
    def isNamePattern(self) -> bool:
        """ Whether the name is a pattern. """
    def getDisplayLabel(self, show_tags: bool = False) -> str:
        """ Get the label for displaying the set in the view. """
    def getDescriptionLabel(self, show_count: bool = True, show_patterns: bool = True, unique_ids: bool = False) -> str:
        """ Get the label for displaying the set in the view. """
    def nameInTree(self, control_tree: Collection[str] | None) -> bool:
        """ Whether my name is in the control tree.
            Is my name is a pattern, checks to see if the
            pattern matches any item in the tree, otherwise
            just checks to see if the name exists in the tree.
        """
    @typing.overload
    def getSubTree(self, control_tree: None) -> None: ...
    @typing.overload
    def getSubTree(self, control_tree: _TreeT) -> _TreeT: ...
    def getIcon(self) -> QtGui.QIcon | None:
        """ Get the name icon for this item. """
    def getButtonIcon(self, column: int, model: SelectionManagerModel | None = None) -> hou.qt.Icon | None:
        """ Get the button icons for this item based on the
            state of what each icon represents.
        """
    def getButtonToolTip(self, column: int) -> str | None:
        """ Get the tooltip for the button based on the state of
            the icon.
        """
    def getSelectState(self) -> int:
        """ Get whether this item is selected. """
    def getControlState(self) -> int:
        """ Get whether this item is control visible. """
    def getCharState(self) -> int:
        """ Get whether the characteres in this item are visible. """
    def getConstraintState(self) -> int:
        """ Get whether this item is a visible constraint. """
    def getPinState(self) -> int:
        """ Get the state of the pin icon on this item. """
    def getIncludedInPin(self) -> bool:
        """ Whether the item or any ancestor is pinned. """
    def getIsolateState(self) -> int:
        """ Get the state of the isolate icon on this item. """
    def getInternalIsolateState(self) -> int:
        """ Get the internal isolate vis state of this item. """
    def setPinnable(self, val: bool, and_children: bool = True) -> None:
        """ Set whether this item and its descendants are pinnable. """
    def getChildren(self) -> list['BaseItem']:
        """ Get the child items. """
    def flags(self, column: int) -> QtCore.Qt.ItemFlag | None:
        """ Get the item flags. """
    def sort(self, and_children: bool = False) -> None:
        """ Sort the children of this item.

            :and_children: Whether to recursively call sort on each
                of the children.
        """
    def sortControls(self) -> None:
        """ Sort the controls. """
    def getJSONType(self) -> _ItemType:
        """ The type identifier used in the JSON dictionary. """
    def export(self, unique_ids: bool = False, export_properties: Iterable[str] | None = None, parent_is_persistant: bool = False, export_persistant: bool = False) -> _ExportedSet:
        """ Export my self as json. """
    def exportChildren(self, unique_ids: bool = False, export_properties: Iterable[str] | None = None, parent_is_persistant: bool = False, export_persistant: bool = False) -> list[_ExportedSet]:
        """ Export the children as JSON, return an array
            of the exported children.
        """
    def needsExport(self, parent_is_persistant: bool = False, export_persistant: bool = False) -> bool:
        """ Whether the item needs to be exported. """
    def findChild(self, name: str) -> BaseItem | None:
        """ Find a child by name. """
    @typing.overload
    def findChildByPath(self, path_parts: Sequence[str], include_sets_path: bool = ..., my_index: None = ...) -> BaseItem | None: ...
    @typing.overload
    def findChildByPath(self, path_parts: Sequence[str], include_sets_path: bool, my_index: _Index) -> tuple[BaseItem, _Index] | BaseItem | None: ...
    @typing.overload
    def findChildByPath(self, path_parts: Sequence[str], include_sets_path: bool = ..., *, my_index: _Index) -> tuple[BaseItem, _Index] | BaseItem | None: ...
    @typing.overload
    def findChildByPath(self, path_parts: Sequence[str], include_sets_path: bool = ..., my_index: _Index | None = ...) -> tuple[BaseItem, _Index] | BaseItem | None: ...
    def findChildById(self, unique_id: int | None) -> BaseItem | None:
        """ Find a child by its unique id. """
    @typing.overload
    def findChildByUniqueIdPath(self, unique_id_path: Sequence[int | None], my_index: None = ...) -> BaseItem | None: ...
    @typing.overload
    def findChildByUniqueIdPath(self, unique_id_path: Sequence[int | None], my_index: _Index | None = ...) -> tuple[BaseItem, _Index] | BaseItem | None: ...
    @uniqueNameDisabler
    def applyDiff(self, diff: Iterable[_SetDiff], index: _Index | None = None, reverse: bool = False, use_index: bool = True) -> None:
        """ Apply the diff recursively and update the sub tree with the
            changes stored in the diff.
        """
    def getActiveControl(self, only_valid: bool = True) -> ControlItem | None:
        """ Get the first control marked as active in this set. """
    def getActiveControlPattern(self, only_valid: bool = True) -> list[str] | None:
        """ Get the path to an active control under this item if it exists. """
    def getActiveControlPath(self, all_controls_tree: _ControlTree, only_valid: bool = True) -> list[str] | None:
        """ Get the path to an active control under this item if it exists. """
    def setControlActive(self, val: bool = True) -> None:
        """ Set the current control as active. The base class
            implementation does nothing.
        """
    def findItem(self, path_parts: Sequence[str], include_sets_path: bool = False) -> BaseItem | None:
        """ Find an item given a split control path.

            If include_sets_path is true, path_parts also includes
            any names for the sets.

            Otherwise if include_sets_path is False, path_parts only
            includes the control path, and it will find the first
            control under this item that matches the path.
        """
    def inImportFolder(self) -> bool: ...
    @typing.overload
    def getPath(self, delim: str | None = ..., only_control_path: bool = ..., split: Literal[False] = ...) -> str: ...
    @typing.overload
    def getPath(self, delim: str | None, only_control_path: bool, split: Literal[True]) -> list[str]: ...
    @typing.overload
    def getPath(self, delim: str | None = ..., only_control_path: bool = ..., *, split: Literal[True]) -> list[str]: ...
    @typing.overload
    def getPath(self, delim: str | None = ..., only_control_path: bool = ..., split: bool = ...) -> str | list[str]: ...
    def getUniqueIdPath(self) -> list[int | None]:
        """ Get the path of unique ids from the root down to this item
            and return it as a list.

            This can be used as a unique way of getting back to an item
            from the root without unnecessary searching.
        """
    def getHUDColumns(self) -> list[int]:
        """ Return the columns shown in the HUD panel. """
    def print(self, level: int = 0, depth: int = 3) -> None:
        """ Debug print. """

class RootFolderItem(BaseItem):
    """ An item that can hold other folders or control trees. """
    def isFolder(self) -> bool: ...
    def getIcon(self) -> hou.qt.Icon | None: ...
    def getJSONType(self) -> Literal['Folder']: ...
    def flags(self, column: int) -> QtCore.Qt.ItemFlag | None:
        """ Get the item flags. """
    @typing.overload
    def getSubTree(self, controls_tree: None) -> None: ...
    @typing.overload
    def getSubTree(self, controls_tree: _TreeT) -> _TreeT: ...

class GroupItem(BaseItem):
    """ An item that can hold other groups of items in the scene. """
    def isFolder(self) -> bool: ...
    def getHUDColumns(self) -> list[int]:
        """ Return the columns shown in the HUD panel. """
    def getIcon(self) -> hou.qt.Icon | None: ...
    def getJSONType(self) -> Literal['Group']: ...
    def getCharState(self) -> int:
        """ Get whether the characteres in this item are visible. """
    def flags(self, column: int) -> QtCore.Qt.ItemFlag | None:
        """ Get the item flags. """

class RootItem(RootFolderItem):
    """ The hidden root level item. """
    def __init__(self, model: SelectionManagerModel | None, modelimpl: ModelImpl | None = None) -> None: ...
    def isRoot(self) -> bool: ...
    def getPath(self, delim: str | None = None, only_control_path: bool = False, split: bool = False) -> Literal['']: ...
    def isPersistant(self) -> bool:
        """ Whether this is auto removed when clear is called on a parent."""
    def getIncludedInPin(self) -> bool:
        """ Root not included in pins. """

class CharacterItem(BaseItem):
    """ Top level items in a control tree. """
    def getIcon(self) -> QtGui.QIcon | None: ...
    def getJSONType(self) -> Literal['Character', 'Tool', 'MultiCtrl']: ...
    def getTag(self) -> str: ...
    def isCharacter(self) -> bool: ...
    def acceptsState(self, key: _StateKey) -> bool: ...
    def endsState(self, key: _StateKey) -> bool: ...
    def getHUDColumns(self) -> list[int]:
        """ Return the columns shown in the HUD panel. """
    def flags(self, column: int) -> QtCore.Qt.ItemFlag | None:
        """ Get the item flags. """

class ToolItem(CharacterItem):
    """ Character level item for tools. """
    def getIcon(self) -> QtGui.QIcon | None: ...
    def getJSONType(self) -> Literal['Tool']: ...
    def getTag(self) -> Literal['tool']: ...
    def getButtonIcon(self, column: int, model: SelectionManagerModel | None = None) -> hou.qt.Icon | None:
        """ Get the button icons for this item based on the
            state of what each icon represents.
        """
    def getButtonToolTip(self, column: int) -> str | None:
        """ Get the tooltip for the button based on the state of
            the icon.
        """

class MultiCtrlItem(CharacterItem):
    """ Character level item for multi ctrls. """
    def getJSONType(self) -> Literal['MultiCtrl']: ...
    def getTag(self) -> Literal['ctrl']: ...
    def acceptsState(self, key: _StateKey) -> bool: ...

class RigItem(BaseItem):
    """ Second level item, used for rig items in the tree. """
    def getCharState(self) -> int:
        """ Get whether the characteres in this item are visible. """
    def getHUDColumns(self) -> list[int]:
        """ Return the columns shown in the HUD panel. """
    def getButtonIcon(self, column: int, model: SelectionManagerModel | None = None) -> hou.qt.Icon | None:
        """ Get the button icons for this item based on the
            state of what each icon represents.
        """
    def getButtonToolTip(self, column: int) -> str | None:
        """ Get the tooltip for the button based on the state of
            the icon.
        """
    def getIcon(self) -> hou.qt.Icon | None: ...
    def getJSONType(self) -> Literal['Rig', 'Control', 'Constraint', 'Geo']: ...
    def getTag(self) -> str | None: ...
    def isRig(self) -> bool: ...
    def updateStateTopDown(self, key: _StateKey, control_tree: _ControlTree | None = None, force_state: int | None = None) -> int:
        """ Update the states for the 'key' state. """
    def flags(self, column: int) -> QtCore.Qt.ItemFlag | None:
        """ Get the item flags. """

class RigSubItem(RigItem):
    """ Non-top level items in a control tree. """
    def __init__(self, *args: str | SelectionManagerModel | int | ModelImpl | None, **kwargs: Unpack[_ItemKwargs]) -> None: ...
    def getTag(self) -> str | None: ...
    def isRig(self) -> bool: ...
    def isInRig(self) -> bool: ...
    def getSubtreeKey(self) -> str: ...
    def isPresent(self) -> bool: ...
    def setPresent(self, present: bool) -> bool: ...

class ControlItem(RigSubItem):
    """ Non-top level items in a control tree. """
    def acceptsState(self, key: _StateKey) -> bool: ...
    def getIcon(self) -> hou.qt.Icon | None: ...
    def getJSONType(self) -> Literal['Control', 'Constraint', 'Geo']: ...
    def getActiveControl(self, only_valid: bool = True) -> ControlItem | None:
        """ Return self if active, otherwise look at children. """
    def setControlActive(self, val: bool = True) -> None:
        """ Set self as active control. """
    def isControl(self) -> bool: ...
    def flags(self, column: int) -> QtCore.Qt.ItemFlag | None:
        """ Get the item flags. """

class ConstraintItem(ControlItem):
    """ Non-top level items in a control tree. """
    def isControl(self) -> bool: ...
    def isConstraint(self) -> bool: ...
    def getTag(self) -> Literal['constr']: ...
    def acceptsState(self, key: _StateKey) -> bool: ...
    def getJSONType(self) -> Literal['Constraint']: ...
    def getIcon(self) -> hou.qt.Icon | None: ...
    def getHUDColumns(self) -> list[int]:
        """ Return the columns shown in the HUD panel. """
    def getButtonIcon(self, column: int, model: SelectionManagerModel | None = None) -> hou.qt.Icon | None:
        """ Get the button icons for this item based on the
            state of what each icon represents.
        """

class GeoItem(ControlItem):
    """ Top level item in control tree, with .geo tag.
        Treated just like characters, but with different icons.
    """
    def getIcon(self) -> hou.qt.Icon | None:
        """ Get the icon used for geometry chars. """
    def getJSONType(self) -> Literal['Geo']:
        """ Get the json type for geometry characters. """
    def getTag(self) -> Literal['geo']:
        """ Get the tag for geometry characters. """

class ImmutableRootFolderItem(RootFolderItem):
    """ A root folder type that you cannot edit the name of
        or the names of items rooted under it.
    """
    def isEditable(self) -> bool:
        """ Whether this item is editable. """
    def flags(self, column: int) -> QtCore.Qt.ItemFlag | None: ...

class ImportRootFolderItem(ImmutableRootFolderItem):
    """ A folder used for importing sets from characters.
        - Is placed right before the current selection set.
        - Is immutable
        - Is not saved to the attribute.
    """
    def topSortKey(self) -> int: ...
    def isPersistant(self) -> bool:
        """ Whether this is auto removed when clear is called on a parent."""
    def inImportFolder(self) -> bool: ...

class CurrentSelectionItem(ImmutableRootFolderItem):
    """ A special item for the current selection. """
    def getIcon(self) -> hou.qt.Icon | None: ...
    def topSortKey(self) -> int: ...
    def isPersistant(self) -> bool:
        """ Whether this is auto removed when clear is called on a parent."""

class AllControlsItem(ImmutableRootFolderItem):
    """ A special item for all of the controls. """
    def getIcon(self) -> hou.qt.Icon | None: ...
    def topSortKey(self) -> int: ...
    def isPersistant(self) -> bool:
        """ Whether this is auto removed when clear is called on a parent."""

class AllConstraintsItem(ImmutableRootFolderItem):
    """ A special item for all of the constraints. """
    def getHUDColumns(self) -> list[int]:
        """ Return the columns shown in the HUD panel. """
    def getIcon(self) -> hou.qt.Icon | None: ...
    def topSortKey(self) -> int: ...
    def isPersistant(self) -> bool:
        """ Whether this is auto removed when clear is called on a parent."""
