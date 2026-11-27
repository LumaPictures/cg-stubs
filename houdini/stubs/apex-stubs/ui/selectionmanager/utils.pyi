import hou
import typing
from apex.animationcatalog import _ControlTree
from apex.scene_2 import Scene as Scene
from apex.ui.selectionmanager.hudpanel import _SelectedSetList, _SelectedSetTree
from apex.ui.selectionmanager.model import SelectionManagerModel as SelectionManagerModel, SelectionManagerModelHandle as SelectionManagerModelHandle
from apex.ui.selectionmanager.modelconfig import _BoolTree, _LabelTree
from apex.utils import timing as timing
from collections.abc import Callable as Callable, Iterable, Mapping, Sequence
from typing import Generic, Literal, Protocol

from typing import ParamSpec
from typing import TypeVar
from typing import ParamSpec
from typing import TypeVar
_P = ParamSpec('_P')
_R = TypeVar('_R')
_TreeT = TypeVar('_TreeT', _ControlTree, _LabelTree)
_ParentT = TypeVar('_ParentT', bound=_BlockParent, default=_BlockParent)
class _BlockParent(Protocol):
    def getBlockManager(self, key: int | str | None = ...) -> BlockLevelManager | None: ...

class _ModelPanel(Protocol):
    def setModel(self, model: SelectionManagerModelHandle | None = ...) -> object: ...

EMPTY_SELECTION: str
PANEL_INTERFACE_NAME: str
SELECTION_SET_KEY: str
DEPTH_TAGS: list[str | None]
SLASH_DELIMITER: str
SEL_SET_ATTRIB: str
MIRROR_USE_RIG_PREF: str
LABEL_KEY: str
ALT_SUBTREE_SUFFIX: str
ALT_SUBTREE_SUFFIX_LEN: int

class Commands:
    RETRIEVE_SEL_CONTROLS: str
    RETRIEVE_ALL_CONTROLS: str
    RETRIEVE_VISIBLE_CONTROLS: str
    RETRIEVE_ALL_CHARS: str
    RETRIEVE_VISIBLE_CHARS: str
    RETRIEVE_VISIBLE_CONSTRAINTS: str
    RETRIEVE_SEL_SETS: str
    RETRIEVE_MODEL: str
    SHOW_CHARS: str
    SHOW_CONSTRAINTS: str
    SELECT_CONTROLS: str
    SHOW_CONTROLS: str
    SHOW_ALL_CONTROLS: str
    SHOW_ALL_CHARS: str
    HIDE_ALL_CONTROLS: str
    HIDE_ALL_CHARS: str
    PIN_CONTROLS: str
    SELECT_ALL_CONTROLS: str
    SELECT_DESCENDANTS: str
    PATTERN_MATCH_CONTROLS: str
    RETRIEVE_RIG_MIRROR_PATTERNS: str
    RELABEL_CONTROL: str
    REMOVE_CONSTRAINTS: str

class TimerBlock:
    """ Used to time code inside the block. Prints when entering and
        exiting the block with a custom message.
    """
    def __init__(self, msg: str) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: object) -> None: ...

def timed(function: Callable[_P, _R]) -> Callable[_P, _R]:
    """ Decorator to wrap a function with a TimerBlock. """
def houColToRGBAInt(col: hou.Color) -> int: ...

class BlockLevelManager:
    """ Manage block levels. """
    def __init__(self) -> None: ...
    def getLevel(self) -> int: ...
    def enterBlock(self) -> None: ...
    def exitBlock(self) -> None: ...
    def inBlock(self) -> bool: ...

class BlockManagers:
    """ Encapsulate having multiple block managers.
        Block managers are associated with a key,
        and their blocks are associated with the same key.
        This way multiple block types can be made, each
        supporting nesting, and each with independent scopes.
    """
    def __init__(self) -> None: ...
    def add(self, key: int | str) -> BlockLevelManager: ...
    def get(self, key: int | str | None) -> BlockLevelManager | None: ...
    def inBlock(self, key: int | str | None) -> bool | None: ...

class GenericBlock(Generic[_ParentT]):
    """
        Used to allow writing state commands in a block
        so that the panel can tell when something occurs
        while a state command is running.

        with GenericBlock(self, key=None):
            ...

        To use this 'parent' must have a 'getBlockManager(key=None)' method.
    """
    parent: _ParentT
    key: int | str | None
    def __init__(self, parent: _ParentT, key: int | str | None = None) -> None: ...
    def getBlockManager(self) -> BlockLevelManager | None: ...
    def inBlock(self) -> bool: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: object) -> None: ...

def copyAttribute(to_geo: hou.Geometry, from_geo: hou.Geometry) -> None:
    """
    Copy the selection set attribute from one geometry to another.

    Can raise hou.GeometryPermissionError if the to_geo is not modifiable.
    """
def preprocessFilterText(text: str) -> tuple[str, str]:
    """ Preprocess the filter text to form the true pattern
        that is used to match lines in the tree.
    """
def splitControl(control: str | list[str], delimiter: str) -> list[str]:
    """ Split a control by a delimiter into a list of pieces. """
def splitControls(controls: Iterable[str], delimiter: str, sort_controls: bool = False) -> list[list[str]]:
    """ Split the controls in controls by delimiter.
    """
def getAltSubtreeName(name: str) -> str: ...
def isAltSubtree(key: str) -> bool: ...
def stripAltSubtreeSuffix(key: str) -> str | None: ...
def cleanupControlTree(root_tree: _ControlTree) -> None:
    """ Remove all empty control subtrees
    """
def addTag(name: str, depth: int) -> str:
    """ Add tag to the name based on the depth in the control tree. """
def addTagsControlTree(tree: _ControlTree, depth: int = 0) -> _ControlTree:
    """ Add tags to all items in the control tree. """
def addTagsList(names_list: Iterable[str], depth: int = 0) -> list[str]:
    """ Add tags to all items in the list.
        Note that it uses the depth info so all names
        must be at the same depth.
    """
def remapControlTree(tree: _ControlTree, parent_path: str, mapping: Mapping[str, str], delimiter: str) -> _ControlTree: ...
def buildControlTree(controls: Iterable[str], delimiter: str, add_tags: bool = False, sort_controls: bool = True) -> _ControlTree:
    """ Build the control tree dictionary from a list of
        controls.

        :controls: A list of control strings.
        :delimiter: A delimiter to use to split the control
            strings into parts.
    """
def filterControlTree(controls_tree: _TreeT, filter_fn: Callable[[str, _TreeT], bool]) -> _TreeT:
    """ Filters items out of a control tree based upon the given filter function
        :param filter_fn: A function that accepts a name and control tree, returning a bool
                          representing whether that item should be included.
                          The control tree is the tree that contains the item in question.
    """
def insertItemToTreeSplit(control_tree: _LabelTree, path_split: Sequence[str], key: str, val: str, in_rig: bool = False) -> None: ...
def insertItemToTree(control_tree: _LabelTree, path: str, key: str, val: str, delimiter: str) -> None: ...
def removeItemFromTreeSplit(control_tree: _LabelTree, path_split: Sequence[str], key: str, in_rig: bool = False) -> None: ...
def removeItemFromTree(control_tree: _LabelTree, path: str, key: str, delimiter: str) -> None: ...
def flattenControlTreeSplit(control_tree: _ControlTree) -> list[list[str]]:
    """ Flatten the control tree into an array of paths, where each path
        is represented as an array of the pieces that form the path.
    """
def removeTag(name: str) -> str:
    """ Remove the tag from a name in the control tree. """
def removeTags(control_tree: _ControlTree) -> _ControlTree:
    """ Remove tags from a control tree. """
def removeTagsList(name_list: Iterable[str]) -> list[str]:
    """ Remove all tags from the names in list. """
def joinSplitControl(split_control: Iterable[str], delimiter: str, prepend: bool = False, remove_tags: bool = False) -> str:
    """ Join the split control from the list using the delimiter
        and possibly also prepending the delimiter.
    """
def flattenControlTree(control_tree: _ControlTree, delimiter: str, prepend: bool = False, remove_tags: bool = False) -> list[str]:
    """ Flatten a control tree into an array of paths, where each
        path part is joined by delimiter.
    """
def mergeControlTrees(tree_a: _TreeT, tree_b: _TreeT) -> _TreeT:
    """ Merge two control trees. """
def mergeControlTreesList(control_tree_list: Sequence[_TreeT]) -> _TreeT:
    """ Merge each of the control trees in the provided list into
        a single tree.
    """
def patternMatchControlTree(patterns_tree: _ControlTree, full_controls_tree: _ControlTree) -> _ControlTree:
    """ Return a filtered full_controls_tree containing all those controls
        matching patterns from the patterns_tree.
    """
def patternMatchPath(path_pattern: Sequence[str], full_controls_tree: _ControlTree) -> _ControlTree:
    """ Given a path represented as an array of parts, each possibly being a
        pattern, and a full controls tree, return a tree containing only those
        elements matching the path_pattern.
    """
def invertBoolTree(bool_tree: _BoolTree, inplace: bool = False) -> _BoolTree:
    """Invert all the boolean leaves of the tree. """
def updateBoolTree(bool_tree: _BoolTree, update_bool_tree: _BoolTree, inplace: bool = False) -> _BoolTree:
    """ Update the valules in bool_tree with those in update_bool_tree. """
def controlsTreeToBoolTree(controls_tree: _ControlTree, set_val_tree: _ControlTree | None = None, in_val: bool = True, out_val: bool = False) -> _BoolTree:
    """ Take a controls tree, and a filtered tree, and create a bool tree,
        which is like a controls tree except it contains everything and stores
        a true/false value for whether things are included or not included.

        in_val is the value given to controls considered in the tree.
        out_val is the value given to controls considered not in the tree.
    """
def boolTreeToControlsTree(controls_tree: _ControlTree, bool_tree: _BoolTree | None = None, default_include: bool = True) -> _ControlTree:
    """ Take a controls_tree to filter, and a bool_tree, which is like a control
        tree except that the leaf levels store a true/false value, and
        return the fitlered controls_tree to include only that represented
        by the bool tree.

        In the bool tree, there is the possibility for parts of the
        controls_tree to be missing, these are treated as included if
        default_include is true, otherwise are treated as not included.
    """
def getBoolTreeTrackedControls(bool_tree: _BoolTree) -> _ControlTree:
    """ Get the control tree of all tracked controls in the bool_tree. """
def leafCount(controls_tree: _ControlTree, suffix: str | None = None) -> int:
    """ Count the number of leaves in the tree with an optional suffix. """
def firstPath(controls_tree: _ControlTree) -> list[str]:
    """ Extract the first path in the tree. This is for finding an
        arbitrary control in a tree.
    """
def isStringPattern(pattern: str) -> bool:
    """ Whether the given string is a pattern. """
def retrieveControlSelection(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> _ControlTree:
    """ Send a state command to the state 'retrieveSelectedControls'.
        The state is then responsible for setting the 'ret' element
        of the args dictionary to the current control tree.
        This control tree is then returned.
    """
def retrieveAllControls(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> _ControlTree:
    """ Send a state command to the state 'retrieveAllControls'.
        The state is then responsible for setting the 'ret' element
        of the args dictionary to the full control tree.
        This control tree is then returned.
    """
def retrieveVisibleControls(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> _ControlTree:
    """ Send a state command to the state 'retrieveVisibleControls'.
        The state is then responsible for setting the 'ret' element
        of the args dictionary to the visible controls tree.
    """
def retrieveAllChars(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> _ControlTree:
    """ Send a state command to the state 'retrieveVisibleChars'.
        The state is then responsible for setting the 'ret' element
        of the args dictionary to the visible charactes.

        The returned characters can just be a flat list of character names.
    """
def retrieveVisibleChars(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> _ControlTree:
    """ Send a state command to the state 'retrieveVisibleChars'.
        The state is then responsible for setting the 'ret' element
        of the args dictionary to the visible charactes.

        The returned characters can just be a flat list of character names.
    """
def retrieveVisibleConstraints(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> _ControlTree:
    """ Send a state command to the state 'retrieveVisibleConstraints'.
        The state is then responsible for setting the 'ret' element
        of the args dictionary to the visible constraints.
    """
@typing.overload
def retrieveSelectedSelectionSets(model: SelectionManagerModel | None = ..., controls_in_tree_format: Literal[True] = ..., scene_viewer: hou.SceneViewer | None = ...) -> dict[str, _SelectedSetTree]: ...
@typing.overload
def retrieveSelectedSelectionSets(model: SelectionManagerModel | None = ..., *, controls_in_tree_format: Literal[False], scene_viewer: hou.SceneViewer | None = ...) -> dict[str, _SelectedSetList]: ...
@typing.overload
def retrieveSelectedSelectionSets(model: SelectionManagerModel | None, controls_in_tree_format: Literal[False], scene_viewer: hou.SceneViewer | None = ...) -> dict[str, _SelectedSetList]: ...
@typing.overload
def retrieveSelectedSelectionSets(model: SelectionManagerModel | None = ..., controls_in_tree_format: bool = ..., scene_viewer: hou.SceneViewer | None = ...) -> dict[str, _SelectedSetTree] | dict[str, _SelectedSetList]: ...
def retrieveModel(scene_viewer: hou.SceneViewer | None = None) -> SelectionManagerModelHandle | None:
    """ Send a state command to the state 'retrieveModel'.
        The state is then responsible for setting the 'ret' element
        of the args dictionary to the model.
    """
def sendControlSelection(control_names: _ControlTree | Iterable[str], model: SelectionManagerModel | None = None, pick_modifier: hou.EnumValue[hou.pickModifier] = ..., active_control: Sequence[str] | None = None, scene_viewer: hou.SceneViewer | None = None, controls_in_tree_format: bool = True, run_control_callbacks: bool = False) -> None:
    """ Send the controls selection to the state. Utilizes a
        'selectControls' command.

        :control_names: A list of control name strings.
        :pick_modifier: Whether to replace the current selection,
            add to it, subtract from it, or toggle entries.
        :active_control: The path to the control to put the xform on.
    """
def sendControlVisibility(control_names: _ControlTree, model: SelectionManagerModel | None = None, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None, scene_viewer: hou.SceneViewer | None = None, initialize: bool = False) -> None:
    """ Send the controls visibility to the state. Utilizes a
        'showControls' command.

        :control_names: A list of control name strings.
        :pick_modifier: Whether to replace the visible controls,
            add to them, subtract from them, or toggle visibility
            of controls.
        :scene_viewer: The scene viewer the state is running in.
        :initialize: Only hide the control group members within control_names.
    """
def sendPinControls(control_names: _ControlTree, model: SelectionManagerModel | None = None, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """ Send a 'pinControls' command to the state. """
def sendRelabelControl(control_path: str, label: str | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """ Sends a 'relabelControl' command to the state to inform it that
        a control has been relabel

        :control_path: The path of the control.
        :label: The new label for the control. A value of None indicates that
            the label has been cleared
    """
def sendShowAllControls(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """ Send a 'showAllControls' command to the state. """
def sendShowAllChars(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """ Send a 'showAllChars' command to the state. """
def sendHideAllControls(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """ Send a 'hideAllControls' command to the state. """
def sendHideAllChars(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """ Send a 'hideAllChars' command to the state. """
def sendSelectAllControls(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """ Send a 'selectAllControls' command to the state. """
def sendSelectDescendants(model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """ Send a 'selectDescendants' command to the state. """
def sendCharacterVisibility(character_names: _ControlTree, model: SelectionManagerModel | None = None, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """ Send a 'showCharacters' command to the state. """
def sendConstraintVisibility(constraint_tree: _ControlTree, model: SelectionManagerModel | None = None, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """ Send a 'showConstraints' command to the state. """
def sendRemoveConstraints(constraint_tree: _ControlTree, model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> None:
    """ Send a 'removeConstraints' command to the state. """
def patternMatchControlPaths(pattern: str, rig_paths: Iterable[str] | None = None, model: SelectionManagerModel | None = None, scene_viewer: hou.SceneViewer | None = None) -> list[str] | None: ...
def getContiguousIntegerRuns(the_arr: Sequence[int]) -> list[tuple[int, int, int]]:
    """ Given an array of integers in increasing order,
        return a new array of tuples (start_index, start_value, count),
        where start_index is the index into the_arr where
        the run begins, and count is the number of items
        in the run.
    """
def getControlListFromGeo(geo: hou.Geometry | None, include_internal: bool = True) -> list[str]:
    """ Given a geometry containing a scene that the APEX Animate
        state accepts and can parse, return the list of controls
        in the rigs.
    """
def getControlTreeFromGeo(geo: hou.Geometry | None, include_internal: bool = True) -> _ControlTree:
    """ Given a geometry containing a scene that the APEX Animate
        state accepts and can parse, return the control tree
        of all controls in the rigs.
    """
def updateModel(model: SelectionManagerModelHandle | None, hud_panel: _ModelPanel | None = None) -> None:
    """ Update the model in the active selection manager panels with
        a new model.
    """
def selectionSetPrefName(name: str) -> str:
    """ Get the custom pref name for this name for the panel. """
def setSelectionSetBoolPref(name: str, on: bool) -> None:
    """ Set a selection set bool preference. """
def getSelectionSetBoolPref(name: str, default_val: bool) -> bool:
    """ Get a selection set bool preference. """
def setMirrorUseRigPatterns(on: bool) -> None:
    """
    Set the preference to tell it whether to use mirror patterns
    from the rig when mirroring.
    """
def getMirrorUseRigPatterns() -> bool:
    """
    Get the preference telling it whether to use mirror patterns
    from the rig when mirroring.
    """
def getRigMirrorPatternsFromState(rig_path: str, scene_viewer: hou.SceneViewer | None = None) -> list[tuple[str, str]]:
    """ Get the mirror patterns for the rig path from the state. """
def getMirrorPatternsMapFromState(scene_viewer: hou.SceneViewer | None = None) -> dict[str, list[tuple[str, str]]]:
    """ Query the state to find a dictionary of rig path to mirror patterns. """
