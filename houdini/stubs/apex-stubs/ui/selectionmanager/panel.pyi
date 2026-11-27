import apex.ui.selectionmanager.modelitem as ssmi
import apex.ui.selectionmanager.utils as ssu
import dbg
import hou
import typing
from apex.animationcatalog import _ControlTree
from apex.ui.animationlayers.view import _DelegateKwargs
from apex.ui.selectionmanager.hudpanel import SelectionSetHUDWidget as SelectionSetHUDWidget, _SelectedSetList, _SelectedSetTree
from apex.ui.selectionmanager.model import SelectionManagerModel as SelectionManagerModel, SelectionManagerModelHandle as SelectionManagerModelHandle, _Color, _Index
from apex.utils import timing as timing
from collections.abc import Callable as Callable, Collection, Iterable
from houtypes import NodeEventKwargs
from hutil.PySide import QtCore, QtGui, QtWidgets
from typing import ClassVar, Literal, Protocol, ReadOnly, Required, TypedDict, Unpack

from typing import TypeAlias
from typing import TypeAlias
_ParentPanel: TypeAlias = 'SelectionSetPanel | SelectionSetHUDWidget'
class _TreeKwargs(TypedDict, total=False):
    parent_panel: Required[ReadOnly[_ParentPanel]]
    model: SelectionManagerModelHandle | None
    scene_viewer: hou.SceneViewer | None

class _NodeEventCallback(Protocol):
    def __call__(self, **kwargs: Unpack[NodeEventKwargs]) -> object: ...

ADD_FOLDER_ICON: hou.qt.Icon
VIEW_COL_PREFS: dict[int, str]
AUTO_EXPAND_PREF: str
AUTO_REMAP_IMPORT_PREF: str
AUTO_SEP_SETS_PREF: str
AUTO_REM_ORIG_PREF: str
VIEW_TAGS_PREF: str
VIEW_RIGS_PREF: str
VIEW_IMPORT_CHARS_PREF: str
VIEW_FILTER_HUD_PREF: str
DEFAULT_EXPANDED_PREF: str
DEFAULT_EXPAND_ALL_CONTROLS_PREF: str
REMAP_CHOICE_SEL: int
REMAP_CHOICE_ALL: int
REMAP_CHOICE_REPLACE: int
REMAP_CHOICE_KEEP: int
CHARS_GEO_OUTPUT_NODES: tuple[str]
NODE_EVENT_TYPES: list[hou.EnumValue[hou.nodeEventType]]

def getDefaultExpandedPref() -> bool: ...
def getExpandAllControlsPref() -> bool: ...
def checkDisplayHotkeyManager(hotkey: str) -> bool: ...
def getViewColumnPref(column: int) -> bool:
    """ Get the toggle for showing the given column. """
def setViewColumnPref(column: int, checked: bool) -> None:
    """ Set the toggle for showing the given column. """
def getIconPickModifier(icon_state: int, remap_toggle: bool = True) -> hou.EnumValue[hou.pickModifier]:
    """ Get the pick modifier for clicking items that are semantically
        tied to visibility.
        This handles the pick modifier for both the character visibility
        and control visibility icons.
    """
def displayInvalidModelMessage() -> None: ...
def displayInvalidRemoveMessage() -> None: ...

class NodeEventHandler:
    external_cb: _NodeEventCallback | None
    event_queued: bool
    def __init__(self) -> None: ...
    def bindCallback(self, cb: _NodeEventCallback) -> None: ...
    def nodeEventCallback(self, **kwargs: Unpack[NodeEventKwargs]) -> None: ...

STATE_COMMAND_KEY: int
AUTO_SELECT_KEY: int
RECURSIVE_EXPANDING_KEY: int

class StateCommandBlock(ssu.GenericBlock[_ParentPanel]):
    """ Block wrapping anything that sends a command to the
        state. Used because there can potentially be cases
        where the command to the state sends something that
        feeds back and we would like to know that.
    """
    def __init__(self, parent: _ParentPanel) -> None: ...

class AutoSelectDisabler(ssu.GenericBlock[_ParentPanel]):
    """ Block for wrapping certain actions where we programmatically
        change the selection in the tree, where we do not
        want to send the selection back to the state.
    """
    def __init__(self, parent: _ParentPanel) -> None: ...

class RecursiveExpandDisabler(ssu.GenericBlock[_ParentPanel]):
    """ Disable recursive expanding of items on shift click
        when inside this block.
    """
    def __init__(self, parent: _ParentPanel) -> None: ...

class UpdateDisablerBlock:
    """ Disable UI updates in the block. """
    def __init__(self, qt_object: QtWidgets.QWidget) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *args: object) -> None: ...

class ToolButton(QtWidgets.QToolButton):
    """ A Tool button with an up arrow. Used for the button to
        make a new selection set from the current selection.
    """
    def __init__(self, *args: QtWidgets.QWidget | None, icon: QtGui.QIcon | None = None, tooltip: str | None = None) -> None: ...

CLICK_REGION_PLUS: int

class NameDelegate(QtWidgets.QStyledItemDelegate):
    """ A delegate for drawing the name column.

        Will first draw the background as usual, then draw the icon,
        then draw the colour circle, then the name text, then the
        description label.
    """
    def __init__(self, *args: QtCore.QObject | None, **kwargs: Unpack[_DelegateKwargs]) -> None: ...
    def numIcons(self, index: _Index) -> int:
        """ The number of icons drawn before this items name. """
    def iconIndexIsPlus(self, icon_idx: int | None) -> bool:
        """ Whether the icon at this index is the plus to expand. """
    def getClickRegion(self, option: QtWidgets.QStyleOptionViewItem, index: _Index, rel_pos: QtCore.QPoint) -> int | None:
        """ Get the index of the icon clicked before the name or None
            if no icon was clicked.
        """
    def getClickInBounds(self, option: QtWidgets.QStyleOptionViewItem, index: _Index, rel_pos: QtCore.QPoint) -> bool:
        """ Whether the click is in the legal bounds. """
    def updateEditorGeometry(self, editor: QtWidgets.QWidget, option: QtWidgets.QStyleOptionViewItem, index: _Index) -> None:
        """ Qt callback to set the size and position of the editor. """
    def initStyleOption(self, option: QtWidgets.QStyleOptionViewItem, index: _Index) -> None:
        """ Qt Override to customize what the base class paint
            method does.
        """
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: _Index) -> None:
        """ Qt override to draw the name column. """
    def _gap(self) -> int:
        """ The gap between icons. """
    def _startGap(self) -> int:
        """ The px gap before the first icon. """
    def _paintIcons(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: _Index, rect: QtCore.QRect, text_pen: QtGui.QPen, x0: int) -> int:
        """ Draw the decoration (icon). """

class IconDelegate(QtWidgets.QStyledItemDelegate):
    """ Custom drawing for the icons in the icon columns. """
    def initStyleOption(self, option: QtWidgets.QStyleOptionViewItem, index: _Index) -> None:
        """ Qt Override to customize what the base class paint
            method does.
        """
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: _Index) -> None:
        """ Qt override to draw the name column. """

class SelectionSetPanel(QtWidgets.QFrame):
    """ The main panel used for the selection sets. """
    node: hou.OpNode | None
    def __init__(self, *args: QtWidgets.QWidget | None, node: hou.OpNode | None = None) -> None: ...
    def getModel(self) -> SelectionManagerModel | None:
        """ Get the tree model used for the tree view. """
    def hasValidModel(self) -> bool:
        """ Whether there is a valid model. """
    def setModel(self, model: SelectionManagerModelHandle | None = None, pane_closed: bool = False) -> None:
        """
        Set the model that the view uses. If set to None, will set to
        a default empty model, otherwise will change the model to point
        to the one provided.

        If there was an old model, its structureUpdated signal will be
        disconnected, and the panel then connects to the new panels
        structureUpdated signal.

        :param model: The model to set. Or None to reset to an inactive model.
        :param pane_closed: Whether the panel has just been closed.
        """
    def getBlockManager(self, key: int | str | None = None) -> ssu.BlockLevelManager | None:
        """ Manditory to allow using StateCommandBlock(self). """
    def inStateCommandBlock(self) -> bool:
        """ Whether we are inside a StateCommandBlock(self). """
    def inAutoSelectDisabler(self) -> bool:
        """ Whether we are inside a AutoSelectDisabler(self). """
    def inRecursiveExpandDisabler(self) -> bool:
        """ Whether we are currently recursively expanding. """
    def getCurrentSelection(self) -> _ControlTree:
        """ Retrieve the current selection tree. """
    def groupCurrentSelection(self, *args: object) -> None:
        """ Create a selection set from the current selection. """
    def emptySetAction(self, *args: object) -> None:
        """ Create a new empty set. """
    def exportToFileAction(self, *args: object) -> None:
        """ Export the selection sets to a file on disk. """
    def exportSelToFileAction(self, *args: object) -> None:
        """ Export the selected selection sets to a file on disk. """
    def importFromFileAction(self, *args: object) -> None:
        """ Import selection sets from a file on disk. """
    def importFromNodeAction(self, *args: object) -> None:
        """ Copy selection sets in from another node. """
    def specifyMirrorRemapPatterns(self, *args: object) -> None:
        """ Edit the current patterns used or remapping left and right. """
    def specifySetRemapPatterns(self, *args: object) -> None:
        """ Edit the current patterns used or remapping left and right. """
    def patternRenameAction(self, *args: object) -> None:
        """ Pattern rename the selected sets. """
    def getFilterChars(self) -> Collection[str] | None:
        """ Get the filter character names. """
    def setFilterChars(self, char_names: Collection[str] | None = None) -> None:
        """ Set the filter character names. """
    def chooseFilterCharsAction(self) -> None:
        """ Choose the characters to filter from a list. """
    def clearFilterCharsAction(self) -> None:
        """ Clear the filtered characters. """
    def onFilter(self, *args: object) -> None:
        """ Update the trees based on the filter. """
    def setVisualSize(self, visual_size: int) -> None:
        """ Needed to put into a HUD Window. """
    def reloadModel(self) -> None:
        """ Reload the controls and the selected controls from the state. """
    def showPaletteAll(self) -> None:
        """
        Show colour palette that when a colour is clicked all selected
        sets get changed.
        """
    def showPaletteSingle(self) -> None:
        """
        Show colour palette that when a colour is clicked only the
        context action item gets changed.
        """
    def _paneActivated(self, pane_tab: hou.PythonPanel) -> None:
        """ Called when the python panel pane is activated. """
    def _paneDeactivated(self) -> None:
        """ Called when the python panel pane is deactivated. """
    def _paneClosed(self) -> None:
        """ Called when the python panel pane is closed. """
    def _panePathChanged(self, node: hou.OpNode | None) -> None:
        """ Called when the pane path changes. """

class SelectionManagerTree(QtWidgets.QTreeView):
    """ Tree view used for the selection manager panel. """
    _ignore_drag: bool
    treeUpdated: ClassVar[QtCore.Signal]
    class ExpandedCache:
        def __init__(self, tree_view: SelectionManagerTree) -> None: ...
        def save(self) -> None: ...
        def load(self) -> None: ...
    expanded_cache: SelectionManagerTree.ExpandedCache
    def __init__(self, *args: QtWidgets.QWidget | None, **kwargs: Unpack[_TreeKwargs]) -> None: ...
    def close(self) -> None:
        """ Called when the panel is closed to cleanup contents in preparation
            for deletion.
        """
    def setExpandedPropertyOnItems(self) -> None:
        """ Set the expanded property on any expanded item in the tree. """
    def expandFromPropertyOnItems(self) -> None:
        """ Set items expanded from the expand property on the items. """
    def hasValidModel(self) -> bool:
        """ Whether we have a valid model that we can use, or if it
            is just a placeholder.
        """
    def resetModel(self, new_model: SelectionManagerModelHandle | None) -> None:
        """ Swap the model that the view uses to the new_model.
            Will first disconnect the selectionChanged from the current
            selection model, then change the model, then reset the view,
            then connect the selectionChanged signal for the new model.
        """
    def startDrag(self, supported_drag_actions: QtCore.Qt.DropAction) -> None:
        """
        Workaround for a Qt bug involving drag and drop in which
        it will always delete all selected rows, including those
        not flagged for drag and drop. As a result these rows just
        get completely lost.

        See https://stackoverflow.com/questions/43283252/when-dragging-multiple-items-from-qlistwidget-non-draggable-items-get-removed.
        """
    def dropEvent(self, event: QtGui.QDropEvent) -> None:
        """ Override to reselect indexes after drop. """
    def selectIndexes(self, proxy_indexes: Iterable[_Index]) -> None:
        """
        Set the selection to these indexes.
        NOTE: Will emit a selection changed for each row
        selected and once for clearing at the start.
        """
    def getModel(self) -> SelectionManagerModel | None:
        """
        Return the source model used internally.
        Note that this is not the proxy model.
        """
    @typing.overload
    def getSelectedSets(self, controls_in_tree_format: Literal[True] = ...) -> dict[str, _SelectedSetTree]: ...
    @typing.overload
    def getSelectedSets(self, controls_in_tree_format: Literal[False]) -> dict[str, _SelectedSetList]: ...
    @typing.overload
    def getSelectedSets(self, controls_in_tree_format: bool = ...) -> dict[str, _SelectedSetTree] | dict[str, _SelectedSetList]: ...
    def viewMenuCallback(self, column: int) -> Callable[[bool], None]:
        """
        Return the callback for checking the view 'X' column
        in the view menu.
        The callback sets the column hidden or visible, then
        stores the value to a custom preference.
        """
    def viewTagsCallback(self, checked: bool) -> None:
        """ Callback for the view tags toggle. """
    def setShowRigs(self, on: bool) -> None:
        """ Set whether rig items are shown in the tree. """
    def setShowImportChars(self, on: bool) -> None: ...
    def viewRigsCallback(self, checked: bool) -> None:
        """ Callback for the show rigs toggle. """
    def viewImportCharsCallback(self, checked: bool) -> None: ...
    def setShowTags(self, val: bool) -> None:
        """ Set whether tags are shown beside names. """
    def defaultExpandedCallback(self, checked: bool) -> None:
        """ Callback for the view > Expand New Sets toggle. """
    def defaultExpandAllControlsCallback(self, checked: bool) -> None:
        """ Callback for the view > Expand New Sets toggle. """
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Override to handle mouse press events. This is
        currently only used to disable selecting an item on
        right click if another item is already selected.
        """
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Override to handle mouse press events. This is
        currently only used to disable selecting an item on
        right click if another item is already selected.
        """
    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Qt reimplement, turn off ignoring drags here. """
    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        """ Qt reimplement, ignore the drag if dragging. """
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> Literal[False] | None:
        """ Qt reimplement, workaround to disable keyboard search. """
    def clearPinsAction(self) -> None:
        """ Clear the pins. """
    def setControlTree(self, controls_tree: _ControlTree) -> None:
        """ Override to handle setting all controls. """
    def getCurrentSelection(self) -> _ControlTree:
        """ Get the currently selected controls list. """
    def groupCurrentSelection(self) -> None:
        """ Create a selection set from the current selection. """
    def makeActiveAction(self) -> None:
        """ Make the context action item the active control in the set. """
    def emptySetAction(self) -> None:
        """ Create a new empty set. """
    def nestedCurrentSelectionAction(self) -> None:
        """ Create a new set from the current selection nested under the
            item that was hovered when the context menu was created.
        """
    def addCurrentSelectionAction(self) -> None:
        """ Add the current selection to the set. """
    def removeCurrentSelectionAction(self) -> None:
        """ Remove the current selection from the set. """
    def resetCurrentIndex(self, proxy_index: _Index) -> None:
        """
        Either set the current index to 'proxy_index' if it is not set
        to that, or just call reselect on the selected rows
        if the current index matches index and there is only
        one thing selected.
        """
    def deleteSetAction(self) -> None:
        """ Remove the selection set. """
    def removeSelectedSetsAction(self) -> None:
        """ Remove the selected sets. """
    def clearSetsAction(self) -> None:
        """ Clear sets in the model. """
    def sortControlsAction(self) -> None:
        """ Sort the controls under the context action src index. """
    @dbg.ZoneScopedDecorator
    def onFilter(self, text: str, filter_chars: Collection[str] | None) -> None:
        """ Update the visible items in the tree based on the filter. """
    def reloadModel(self) -> None:
        """ Reload all the controls. """
    def selectedRowIndexes(self) -> list[QtCore.QModelIndex]:
        """ Return a filtered list of selected indexes containing only those
            in the first column.
        """
    def selectRows(self, selected_rows: bool = True, row_indexes: Collection[_Index] | None = None, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None, filter_fn: Callable[[ssmi.BaseItem], bool] | None = None) -> None:
        """ Select all controls in selected sets. """
    def selectAction(self) -> None:
        """ Select controls in hovered set. """
    def deselectAction(self) -> None:
        """ Deselect all controls in hovered set. """
    def selectSelAction(self) -> None:
        """ Select all controls in selected sets. """
    def deselectSelAction(self) -> None:
        """ Deselect all controls in selected sets. """
    def clearSelectionAction(self) -> None:
        """ Clear all selected controls. """
    def showAction(self) -> None:
        """ Show all controls in hovered set. """
    def hideAction(self) -> None:
        """ Hide all controls in hovered set. """
    def showSelAction(self) -> None:
        """ Show all items in selected sets. """
    def hideSelAction(self) -> None:
        """ Hide all items in selected sets. """
    def isolateAction(self) -> None:
        """ Isolate all controls in hovered set. """
    def deisolateAction(self) -> None:
        """ Isolate all controls in hovered set. """
    def clearIsolateAction(self) -> None:
        """ Clear the isolated controls. """
    def isolateSelAction(self) -> None:
        """ Isolate the selected sets. """
    def deisolateSelAction(self) -> None:
        """ De-Isolate the selected sets. """
    def revertControlVisibility(self) -> None:
        """ Revert to default control visibility. """
    def showAllAction(self) -> None:
        """ Show all controls in the scene. """
    def showAllCharsAction(self) -> None:
        """ Show all characters visible in the tree. """
    def hideAllCharsAction(self) -> None:
        """ Hide all characters in the tree. """
    def hideAllControls(self) -> None:
        """ Hide all controls in the tree. """
    def selectAllControls(self) -> None:
        """ Select all controls in the tree. """
    def selectDescendants(self) -> None:
        """ Select descendant controls of the current selection. """
    def showCharsAction(self) -> None:
        """ Show the characters in the context action item set. """
    def hideCharsAction(self) -> None:
        """ Hide the characters in the context action item set. """
    def showSelCharsAction(self) -> None:
        """ Show all characters in the selected sets. """
    def hideSelCharsAction(self) -> None:
        """ Show all characters in the selected sets. """
    def pinAction(self) -> None:
        """ Pin the hovered control. """
    def unpinAction(self) -> None:
        """ Unpin the hovered control. """
    def pinSelAction(self) -> None:
        """ Pin all selected sets. """
    def unpinSelAction(self) -> None:
        """ Unpin all selected sets. """
    def showConstraintsAction(self, indexes: Collection[_Index] | None = None) -> None:
        """ Show constraints under the hovered item. """
    def hideConstraintsAction(self, indexes: Collection[_Index] | None = None) -> None:
        """ Hide constraints under the hovered item. """
    def selectConstraintsAction(self, indexes: Collection[_Index] | None = None) -> None:
        """ Select constraints under the hovered item. """
    def deselectConstraintsAction(self, indexes: Collection[_Index] | None = None) -> None:
        """ Deselect constraints under the hovered item. """
    def removeConstraintsAction(self, indexes: Collection[_Index] | None = None) -> None:
        """ Remove constraints under the hovered item. """
    def expandSubTree(self) -> None:
        """
        Recursively expand the subtrees rooted at the item under
        the cursor when the context menu was opened.
        """
    def expandSelSubTrees(self) -> None:
        """ Recursively expand the selected sub trees. """
    def collapseSubTree(self) -> None:
        """
        Recursively collapse the subtrees rooted at the item under
        the cursor when the context menu was opened.
        """
    def collapseSelSubTrees(self) -> None:
        """ Recursively collapse the selected sub trees. """
    def generalizeAction(self) -> None:
        """ Generalize the sub tree. """
    def applyToCharsAction(self) -> None:
        """ Generalize the sub tree to apply to the selected characters."""
    def applyToAllCharsAction(self) -> None:
        """ Generalize the sub tree to apply to all characters. """
    def applySelToCharsAction(self) -> None:
        """ Generalize the sub trees to apply to the selected characters. """
    def applySelToAllCharsAction(self) -> None:
        """ Generalize the sub trees to apply to all characters. """
    def separateCharsAction(self) -> None:
        """
        Separate a generalized character item into separate trees for
        each character.
        """
    def separateSelCharsAction(self) -> None:
        """
        Separate a generalized character item into separate trees for
        each character.
        """
    def separateCharsSetsAction(self) -> None:
        """ Separate the characters in the right clicked set into separate sets. """
    def separateCharsSetsSelAction(self) -> None:
        """ Separate the characters in the selected rows into separate sets. """
    def expandPatternsAction(self) -> None:
        """ Expand all the patterns rooted at an item. """
    def expandSelPatternsAction(self) -> None:
        """ Expand all patterns in the selected rows. """
    def remapCharactersAction(self) -> None:
        """ Remap all characters. """
    def remapCharactersInSelAction(self) -> None:
        """ Remap characters in selected rows. """
    def remapCharacterSingleAction(self) -> None:
        """ Remap charactes in right clicked set. """
    def mirrorAction(self) -> None:
        """ Create a new set that is a mirrored copy of the right clicked item. """
    def mirrorSelAction(self) -> None:
        """ Create mirror sets of the selected rows. """
    def duplicateAction(self) -> None:
        """ Create a new set that is a copy of the right clicked item. """
    def duplicateSetsAction(self) -> None:
        """ Create new sets that are copied of the selected sets. """
    def clearColsAction(self) -> None:
        """ Clear the applied colours from hovered set. """
    def clearSelectedColsAction(self) -> None:
        """ Clear the applied colours from the selected sets. """
    def setRowColor(self, color: _Color, selected_rows: bool = True, indexes: Iterable[_Index] | None = None) -> None:
        """ Set the background color of the selected rows. """
    def exportToFile(self, file_path: str, only_selected: bool = False) -> None:
        """ Export the selection sets in the model to the given file. """
    def importFromFile(self, file_path: str) -> None:
        """ Import selection sets from the given file. """
    def copyFromNode(self, node_path: str) -> None:
        """ Copy selection sets in from the given node. """
    def getRemapPatterns(self) -> tuple[str, str]:
        """ Get the current remap patterns for left and right. """
    def setRemapPatterns(self, left_pattern: str, right_pattern: str) -> None:
        """ Set the remap patterns for left and right. """
    def getSetRemapPatterns(self) -> tuple[str, str]:
        """ Get the left/right remap patterns for renaming sets when mirroring. """
    def setSetRemapPatterns(self, left_pattern: str, right_pattern: str) -> None:
        """ Set the remap patterns for renaming sets when mirroring. """
    def patternRename(self, from_pattern: str, to_pattern: str) -> None:
        """ Pattern rename the selected sets. """
    def renameAction(self) -> None:
        """ Open the editor on the context action item. """
    def relabelAction(self) -> None:
        """ Open the editor to change a label for the context action item. """
    def _handleClickViewControl(self, source_index: _Index, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None) -> None:
        """ Handle clicking on view control icon. """
    def _handleClickCharacter(self, source_index: _Index, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None) -> None:
        """ Handle clicking on the view character icon. """
    def _handleClickConstraint(self, source_index: _Index, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None) -> None:
        """ Handle clicking on the view constraint icon. """
    def _handleClickPin(self, source_index: _Index, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None) -> None:
        """ Handle clicking on the pin icon. """
    def _handleClickIsolate(self, source_index: _Index, pick_modifier: hou.EnumValue[hou.pickModifier] | None = None) -> None:
        """ Handle clicking on the isolate icon. """
    def _itemAt(self, pos: QtCore.QPoint) -> ssmi.BaseItem | None:
        """
        Get the item at the specific position.
        See QTreeView::indexAt(pos).
        """
    def _mapToSource(self, proxy_index: _Index) -> QtCore.QModelIndex:
        """ Given a proxy_index return the corresponding source_index. """
    def _viewOption(self, index: _Index) -> QtWidgets.QStyleOptionViewItem:
        """ Get a view option for the index. """
    def _updateFilterByControlTree(self, filter_tree: _ControlTree, row: int, parent_src_index: _Index, apply_to_persistant: bool = True, only_show: bool = False) -> bool:
        """
        Update the filter on all items under and including parent_src_index[row],
        return true if visible, or false if not.

        :filter_tree: The control tree to filter by.
        :row: The row under the parent that the current item is at
        :parent_src_index: The Q index of the parent.
        """
    def _setDelegates(self, kwargs: _TreeKwargs) -> None:
        """ Set the delegates used for the name and icon columns. """
    def _setupUI(self, kwargs: _TreeKwargs) -> None:
        """ Setup the UI for the Tree Widget. """
