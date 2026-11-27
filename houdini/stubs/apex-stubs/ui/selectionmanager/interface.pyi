import hou
import typing
from apex.animationcatalog import _ControlTree
from apex.ui.selectionmanager.modelconfig import _Model
from apex.ui.selectionmanager.modelitem import BaseItem as BaseItem
from collections.abc import Collection, Iterable, Sequence
from hutil.Qt import QtCore as QtCore
from typing import Literal, NoReturn

def controlListToControlTree(control_list: Iterable[str], sort_controls: bool = False) -> _ControlTree:
    '''
    Given a list of control names, return a control tree.

    This is the form of the selection provided to the
    selection set APIs.

    :control_list: The list of control paths i.e. ["/electra.char/Base.rig/ctrl_name",...].
    '''
def controlTreeToControlList(control_tree: _ControlTree) -> list[str]:
    '''
    Given a control tree, return the control list.

    :control_tree: The tree of controls, i.e. { "electra.char" : { "Base.rig" : { "ctrl1" : {}, "ctrl2" : {} } } }
    '''

class SetContents:
    """ A wrapper around a control selection. """
    def __init__(self, control_tree: _ControlTree) -> None: ...
    @staticmethod
    def fromList(control_list: Iterable[str], sort_controls: bool = False) -> SetContents:
        """
        Make a SetContents object from a control list.

        :control_list: The list of controls to create the contents object from.
        """
    @staticmethod
    def fromTree(control_tree: _ControlTree) -> SetContents:
        """
        Make a SetContents object from a control tree.

        :control_tree: The tree of controls to create the contents object from.
        """
    def asList(self) -> list[str]:
        """ Return the SetContents as a control list. """
    def asTree(self) -> _ControlTree:
        """ Return the SetContents as a control tree. """
    def mergeTree(self, control_tree: _ControlTree) -> None:
        """
        Update the controls tree by merging in control_tree.

        :control_tree: The tree of controls to merge in to this object.
        """
    def mergeList(self, control_list: Iterable[str], sort_controls: bool = False) -> None:
        """
        Update the controls list by merging in control_list.

        :control_list: The list of controls to merge in to this object.
        """
    def merge(self, other_contents: SetContents) -> None:
        """
        Merge this SetContents object with another SetContents object.

        :other_contents: The other SetContents object to merge in with this object.
        """

class SelectionSet:
    """ An item in the selection sets. """
    item: BaseItem
    model: _Model
    def __init__(self, item: BaseItem, model: _Model) -> None: ...
    def modelIndex(self) -> QtCore.QModelIndex | None:
        """ Find and return the index for this item in the model. """
    def isValid(self) -> bool:
        """
        Check whether the item is still valid by trying to get its
        index and checking if the index is valid.
        """
    def getChildren(self) -> list['SelectionSet']:
        """ Get the child sets. """
    def getContents(self) -> SetContents:
        """ Get the contents of the set as a SetContents object. """
    def getPath(self) -> str:
        """ Get the path to this item. """
    def getSplitPath(self) -> list[str]:
        """ Get the split path to this item returned as a list. """
    def getName(self) -> str:
        """ Get this items name. """
    def getParent(self) -> SelectionSet | None:
        """ Get the parent item or None. """
    def isRoot(self) -> bool:
        """ Check if this item is the root item. """
    def isFolder(self) -> bool:
        """ Check if this item is a folder item. """
    def addToSet(self, set_contents: SetContents) -> None:
        """
        Add the contents of the SetContents object provided to this set.

        :set_contents: The SetContents object to add in to this set.
        """
    def removeFromSet(self, set_contents: SetContents) -> None:
        """
        Remove the controls in the set_contents from this set.

        :set_contents: The SetContents object to remove form this set.
        """
    def clearSet(self) -> None:
        """ Clear the contents of this set. """
    def expandPatterns(self) -> None:
        """ Expand the patterns in this set. """
    def separateCharsIntoSets(self, remove_originals: bool = False) -> None:
        """
        Separate the characters in this set into new sets,
        one for each character, and also optionally remove
        the original set.

        WARNING: If remove_originals is true, the item this is
        called on will be invalid afterwards.

        :remove_originals: Whether to remove the original sets after creating new ones for
                           individual characters.
        """
    def replaceCharacters(self, chars_to_replace: Collection[str], new_char_name: str) -> None:
        """
        Replace any instances of character names found in chars_to_replace
        with new_char_name inside this set.

        :chars_to_replace: The character named to replace.
        :new_char_name: The single new character name to replace with.
        """
    def duplicate(self) -> SelectionSet | None:
        """
        Duplicate this set.
        Returns the created set or None if no set could be created.
        """
    def mirror(self) -> SelectionSet | None:
        """
        Mirror this set.
        Returns the created set or None if no set could be created.
        """
    def applyToChars(self, chars: Sequence[str] | None) -> None:
        """
        Apply the contents of this set to the list of characters.
        If chars is None, will apply to all characters tracked
        by the model.

        :chars: The character names to apply the set to.
        """
    def applyToRig(self) -> None:
        """
        Apply the contents of this set to the rig level by removing the
        character name level in the heirarchy.
        """
    def rename(self, name: str) -> None:
        """
        Rename the set using the new name.

        :name: The new name to rename the set with.
        """
    def setColor(self, col: hou.Color) -> None:
        """
        Set the color of this item. This is the color that will
        be shown before the name.

        :col: The color to be given to this set. This is visible as a color chip
              in the UI of the selection sets.
        """
    def sortControls(self) -> None:
        """
        Sort the controls inside this set.
        """

USE_QT_DEFAULT: bool

class SelectionSets:
    """ A selection sets object. """
    model: _Model
    use_qt: bool
    def __init__(self, model: _Model | None = None, use_qt: bool = ...) -> None: ...
    def setModel(self, model: _Model | None = None) -> _Model:
        """
        Set the internal model for the selection sets.

        :model: The internal model to use for the selection sets.
        """
    def getModel(self) -> _Model:
        """ Get the internal selection set model. """
    def findItem(self, item_path: str) -> SelectionSet | None:
        """
        Find an item in the tree given a path to it.
        E.g. set1
             set1/mychar.char
             set1/mychar.char/Base.rig/main

        :item_path: The path to the item to find.
        """
    def findItems(self, item_pattern: str) -> NoReturn:
        """
        Return items in the heirarchy matching the item_pattern.

        :item_pattern: The pattern of items to find.
        """
    def getRootItem(self) -> SelectionSet:
        """ Return the root item. """
    def getItemFromModelIndex(self, model_index: QtCore.QModelIndex) -> SelectionSet:
        """
        Get an item from a model index.

        :model_index: The model index to return the item of.
        """
    def loadModelFromFile(self, file_path: str, load_states: bool = False) -> None:
        """
        Load a fresh selection set model from file.

        :file_path: The file to import selection sets from.
        :load_states: Whether to load in the states, including control visibility,
                      character visibility and select state.
        """
    def loadModelFromGeometry(self, geo: hou.Geometry, load_controls: bool = True, load_states: bool = False) -> None:
        """
        Load a fresh selection set model from geometry attribute.

        :geo: The geometry to load the model from.
        :load_controls: Whether to load in controls from the geometry.
        :load_states: Whether to load in the states stored in the selection sets,
                      including control visibility, character visibility, and select state.
        """
    def loadModelFromJSON(self, json_str: str) -> None:
        """
        Load a fresh selection set model from JSON.

        :json_str: The JSON string to load the model from.
        """
    def loadModelFromState(self) -> None:
        """ Load the model from the running animate state. """
    def importSetsFromFile(self, file_path: str, load_states: bool = False) -> None:
        """
        Import sets into the existing model from a file.

        :file_path: The file path of the .sets object to import.
        :load_states: Whether to load in states stored in the selection sets,
                      including control visibility, character visibility, and select state.
        """
    def importSetsFromGeometry(self, geo: hou.Geometry, load_controls: bool = False, load_states: bool = False) -> None:
        """
        Import sets into an existing model from geometry attribute.

        :geo: The geometry to import selection sets from.
        :load_controls: Whether to load in the set of all controls from the geometry.
        :load_states: Whether to load in states stores in the selection sets,
                      including control visibility, character visibility, and select state.
        """
    def importSetsFromJSON(self, json_str: str) -> None:
        """
        Import sets into the existing model from JSON.

        :json_str: The JSON string to load selection sets from.
        """
    def exportSetsToFile(self, file_path: str, export_states: bool = False, export_special_sets: bool = False) -> None:
        """
        Export the selection sets to a file.

        :file_path: The file path to save the file to.
        :export_states: Whether to also export states to the file, including
                        control visibility, character visibility, and select state.
        :export_special_sets: Whether to export data in the All Controls and
                              Current Selection special sets for isolate and
                              pinning information. This is not normally stored
                              when exporting to files.
        """
    def exportSetsToGeometry(self, geo: hou.Geometry, export_states: bool = False, export_special_sets: bool = True) -> None:
        """
        Export the selection sets to a geometry attribute.

        :geo: The geometry to write the selection sets to.
        :export_states: Whether to also export states to the geometry, including
                        control visibility, character visibility, and select state.
        :export_special_sets: Whether to export data in the All Controls and
                              Current Selection special sets for isolate and
                              pinning information.
        """
    def exportSetsToJSON(self) -> str:
        """ Export the selection sets to JSON. """
    def exportStatesToJSON(self) -> str:
        """ Export the states to JSON. """
    def getControlMirrorPatterns(self) -> tuple[str, str]:
        """ Get the stored mirror patterns matching left and right
            control names.
        """
    def setControlMirrorPatterns(self, left_pattern: str, right_pattern: str) -> None:
        """
        Set the stored mirror patterns matching left and right control names.

        :left_pattern: The mirror pattern for the LEFT controls.
        :right_pattern: The mirror pattern for the RIGHT controls.
        """
    def getSetMirrorPatterns(self) -> tuple[str, str]:
        """
        Get the stored mirror patterns specifying when sets are
        for the left or right controls.

        When sets are mirrored, if the names match one of the
        set patterns, it will be pattern renamed to the other
        side.
        """
    def setSetMirrorPatterns(self, left_pattern: str, right_pattern: str) -> None:
        """
        Set the stored mirror patterns specifying when sets are
        for the left or right controls.

        When sets are mirrored, if the names match one of the
        set patterns, it will be pattern renamed to the other
        side.

        :left_pattern: The pattern to use to rename LEFT sets.
        :right_pattern: The patern to use to rename RIGHT sets.
        """
    def setControls(self, set_contents: SetContents) -> None:
        """
        Set the list of all controls using the SetContents object
        provided containing all controls from the scene.

        :set_contents: The SetContents object to use to set the 'all controls'
                       in the selection set model.
        """
    def setCurrentSelection(self, set_contents: SetContents) -> None:
        """
        Set the current selection using the SetContents
        object provided containing the controls in the
        current selection.

        :set_contents: The SetContents object to use to set the current selection.
        """
    def setVisibleControls(self, set_contents: SetContents) -> None:
        """
        Set the visible controls using the SetContents object
        provided containing the controls to be set as visible.

        :set_contents: The SetContents object to use to set the visible controls.
        """
    def setVisibleChars(self, char_names: list[str]) -> None:
        """
        Set the visible characters.

        :char_names: The character names to set as visible.
        """
    def setHiddenSets(self, set_names: Iterable[str]) -> None:
        '''
        Set selection set names that should be hidden by default
        when no saved visibility state exists.

        :set_names: A list of selection set name strings to hide
                    (e.g. ["LOD_3", "LOD_2"]).
        '''
    def getHiddenSets(self) -> list[str] | None:
        """
        Get the list of selection set names to hide by default.
        Returns None if not set.
        """
    def setHiddenControls(self, control_names: Iterable[str]) -> None:
        '''
        Set control names that should be hidden by default when
        no saved visibility state exists. Names are leaf control
        names without character/rig prefix.

        :control_names: A list of control name strings to hide
                        (e.g. ["C_main", "C_pelvis_ctrl"]).
        '''
    def getHiddenControls(self) -> list[str] | None:
        """
        Get the list of control names to hide by default.
        Returns None if not set.
        """
    def getControls(self) -> SetContents:
        """ Get all the controls in the model as a SetContents. """
    def getCurrentSelection(self) -> SetContents:
        """ Reutrn a SetContents object containing the current selection. """
    def getVisibleControls(self) -> SetContents:
        """ Return a SetContents object containing the visible controls. """
    @typing.overload
    def getVisibleChars(self, as_list: Literal[True] = ...) -> list[str]: ...
    @typing.overload
    def getVisibleChars(self, as_list: Literal[False]) -> _ControlTree: ...
    @typing.overload
    def getVisibleChars(self, as_list: bool = ...) -> list[str] | _ControlTree: ...
    def createSelectionSet(self, set_contents: SetContents, name: str | None = None, parent: SelectionSet | None = None) -> SelectionSet:
        """
        Create a control set from a SetContents object.

        Optionally, set the name of the set, and provide a parent
        if you want the set to be nested.

        :set_contents: The SetContents object to use to create the selection set.
        :name: The name to give to the selection set.
        :parent: The parent set to next this selection set under.
        """
    def clearSets(self) -> None:
        """ Clear all selection sets. """
    def removeSet(self, the_set: SelectionSet) -> None:
        """
        Remove the selection set.

        :the_set: The set to remove.
        """
    def patternRenameSets(self, from_pattern: str, to_pattern: str, sets: Iterable[SelectionSet] | None = None) -> None:
        """
        Pattern rename the selection sets from from_pattern to to_pattern.

        If sets is None, pattern renames all sets in the model.

        :from_pattern: The pattern to rename from.
        :to_pattern: The pattern to rename to.
        :sets: An optional list of sets to rename. If None, renames all.
        """
    def patternRenameChildSets(self, from_pattern: str, to_pattern: str, parent_set: SelectionSet | None = None) -> None:
        """
        Pattern rename the selection sets from from_pattern to to_pattern.
        Will rename all sets UNDER parent_set but not including parent_set.
        If parent_set is None, will rename all sets in the model.

        :from_pattern: The pattern to rename from.
        :to_pattern: The pattern to rename to.
        :parent_set: The parent set to rename all descendants of.
        """
    def replaceCharacters(self, chars_to_replace: Collection[str], new_char_name: str, sets: Iterable[SelectionSet] | None = None) -> None:
        """
        Replace any instance of character names in chars_to_replace with
        the new_char_name in all sets in sets, or if sets is None, in all
        selection sets in the model.

        :chars_to_replace: The list of characters to replace.
        :new_char_name: The character to replace with.
        :sets: The sets to replace characters in. If None replaces in all sets.
        """
    def setLabel(self, control_path: str, label: str | None) -> None:
        """
        Set or remove a label for a control, rig, or character item.

        :control_path: The path for the control, rig, or character in the scene.
        :label: The label to give to the item.
        """

def selectionSetsFromFile(file_path: str, load_states: bool = False, use_qt: bool = False) -> SelectionSets:
    """
    Create and load a selection sets object from a file.

    :file_path: The file path to load the selection sets from.
    :load_states: Whether to also load in the states including control
                  visibility, character visibility, and select state.
    """
def selectionSetsFromGeometry(geo: hou.Geometry, load_controls: bool = True, load_states: bool = False, use_qt: bool = False) -> SelectionSets:
    """
    Create and load a selection sets object from geometry.

    :geo: The geometry to load selection sets from.
    :load_controls: Whether to load in the 'all controls' using the geometry.
    :load_states: Whether to also load in the states including control
                  visibility, character visibility, and select state.
    """
def selectionSetsFromJSON(json_str: str, use_qt: bool = False) -> SelectionSets:
    """
    Create and load a selection sets object from JSON.

    :json_str: The JSON string to load the selection sets from.
    """
def selectionSetsFromState() -> SelectionSets:
    """
    Create a SelectionSets object using the model from the
    running animate state.

    NOTE: This will send a state command to the active state.
    """
