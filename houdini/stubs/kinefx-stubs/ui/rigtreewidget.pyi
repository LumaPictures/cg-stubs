import hou
import typing
from _kinefx import computeHierarchy as computeHierarchy, computeHierarchyResult as computeHierarchyResult, getPackedFolderPaths as getPackedFolderPaths
from collections.abc import Container, Generator, Mapping, Sequence
from enum import Enum
from hutil.PySide import QtCore, QtGui, QtWidgets
from kinefx import rigtree as rigtree
from kinefx.rigapi import getPointChildren as getPointChildren, getPointDescendants as getPointDescendants
from kinefx.rigtree import GenericTree as GenericTree
from kinefx.ui import rigtreeconfig as rigtreeconfig, rigtreeutils as rigtreeutils
from kinefx.ui.rigtreeconfig import _RigTreeConfig
from kinefx.ui.rigtreedialog import RigTreeViewDialog as RigTreeViewDialog
from kinefx.ui.rigtreeutils import _DragDropKwargs, _GetSelectionKwargs, _ItemId, _RenameKwargs, _SelectKwargs
from types import TracebackType
from typing import Any, Callable, ClassVar, Generic, Iterator, Literal, Self

from typing import TypeAlias
from typing import TypeVar
from collections.abc import Hashable
from kinefx.ui.rigtreeutils import _ActionsKwargs
from kinefx.ui.rigtreeutils import _DeleteKwargs
from kinefx.ui.rigtreeutils import _RigAction
from typing import TypeAlias
from typing import TypeVar
_E = TypeVar('_E', bound=Hashable)
_T = TypeVar('_T', bound=Hashable)
_Role: TypeAlias = int | QtCore.Qt.ItemDataRole
_SelectionHandler: TypeAlias = Callable[[_SelectKwargs], object]
_DragDropHandler: TypeAlias = Callable[[_DragDropKwargs], object]
_RenameHandler: TypeAlias = Callable[[_RenameKwargs], object]
_DeleteHandler: TypeAlias = Callable[[_DeleteKwargs], object]
_RigActionsHandler: TypeAlias = Callable[[_ActionsKwargs], Mapping[str, _RigAction | None] | None]
POINT_LIMIT: int
ITEM_ID_ROLE: QtCore.Qt.ItemDataRole
NAME_ROLE: QtCore.Qt.ItemDataRole
ICON_ROLE: QtCore.Qt.ItemDataRole
DESCRIPTION_ROLE: int
VISIBILITY_ROLE: int
FOLDER_ROLE: int

class Hierarchy(Enum):
    Topology = 0
    FlatList = 1

class SortKey(Enum):
    Topology = 0
    TopologyReversed = 1
    Name = 2
    NameReversed = 3
    @staticmethod
    def fromIndex(index: int) -> SortKey | None: ...
    def isReversed(self) -> bool: ...

class TreeType(Enum):
    Joint = 0
    PackedFolder = 1
    def token(self) -> str: ...

HIERARCHY_MENU_OPTIONS: list[str]
SORT_MENU_OPTIONS: list[str]
TREE_TYPE_MENU_OPTIONS: list[str]
SELECTIONMODE_SINGLESELECTION: QtWidgets.QAbstractItemView.SelectionMode
SELECTIONMODE_MULTISELECTION: QtWidgets.QAbstractItemView.SelectionMode
SELECTIONMODE_NOSELECTION: QtWidgets.QAbstractItemView.SelectionMode
ICON_ANIMATION: hou.qt.Icon
ICON_BONE: hou.qt.Icon
ICON_CHARACTER: hou.qt.Icon
ICON_CHANNEL: hou.qt.Icon
ICON_CONSTRAINT: hou.qt.Icon
ICON_DATA: hou.qt.Icon
ICON_DICTIONARY: hou.qt.Icon
ICON_FOLDER: hou.qt.Icon
ICON_FORCE: hou.qt.Icon
ICON_GRAPH: hou.qt.Icon
ICON_LAYER: hou.qt.Icon
ICON_MOTIONCLIP: hou.qt.Icon
ICON_PACKED_GENERIC: hou.qt.Icon
ICON_PICKER: hou.qt.Icon
ICON_RAGDOLL: hou.qt.Icon
ICON_RIG: hou.qt.Icon
ICON_SHAPE: hou.qt.Icon
ICON_SKELETON: hou.qt.Icon
ICON_TOOL: hou.qt.Icon
EXTENSION_ICON_MAP: dict[str, hou.qt.Icon]
NAME_ICON_MAP: dict[str, hou.qt.Icon]
BADGE_VISIBLE_OFF: hou.qt.Icon
BADGE_VISIBLE_ON: hou.qt.Icon
INSPECT_WINDOW_ATTRIBUTES: list[str]
TRAVERSAL_ERROR_MESSAGES: dict[computeHierarchyResult, str]
HIDDEN_PRIM_GROUP: str
TREATASFOLDER_INTRINSIC_NAME: str

class selection_item:
    """
    Store id, name, selected, expanded and whether is current as variables of
    the class for ease of reference. Used mainly for processing selections and
    getting selections.
    """
    id: _ItemId
    name: str
    selected: bool
    expanded: bool
    def __init__(self) -> None: ...

STYLESHEET: str

class _InvalidHierarchy(Exception):
    """
    Custom exception.
    Get error message, as string, from the passed in computeHierarchyResult.
    """
    def __init__(self, code: computeHierarchyResult) -> None: ...
    def text(self) -> str: ...

class _MissingNode(Exception):
    """Custom exception for handling a missing node path."""
    def text(self) -> str: ...

class _MissingGeometry(Exception):
    """
    Custom exception to indicate a node's geometry was expected, but not found.
    """
    def text(self) -> str: ...

class _LimitExceeded(Exception):
    """
    Custom exception raised when the traversal limit has been exceeded.

    E.g. when the network has more than some number of elements.
    """
    def __init__(self, npoints: int, point_limit: int) -> None: ...
    def text(self) -> str: ...

class _RoleProvider(Generic[_E]):
    """
    Holds a dictionary of role-callback pairs. The callback should provide the
    contents to be rendered for the specified role.
    """
    SUPPORTED_ROLES: ClassVar[list[_Role]]
    @staticmethod
    def fromDict(d: Mapping[_Role, Callable[[_T], object]]) -> _RoleProvider[_T]: ...
    _map: dict[_Role, Callable[[_E], object]]
    def __init__(self) -> None: ...
    def __iter__(self) -> Iterator[tuple[_Role, Callable[[_E], object]]]: ...
    def setRole(self, role: _Role, callback: Callable[[_E], object]) -> None: ...

def add_tree_to_model(model: QtGui.QStandardItemModel, tree: GenericTree[_T], provider: _RoleProvider[_T]) -> None:
    """
    Populate model with items.
    """
def _traverse_indexes(model: QtGui.QStandardItemModel) -> Generator[QtCore.QModelIndex, None, None]:
    """
    Yields each index of the model.

    The order is unspecified.
    """

OPTION_FIXED_WIDTH: int
OPTION_FIXED_HEIGHT: int
OPTION_SPACING: int
OPTION_FONT_SIZE: int
LABEL_FONT_SIZE: int
FILTER_HORIZONTAL_MARGIN: int
FILTER_VERTICAL_MARGIN: int
HEADER_SPACING: int
HEADER_HORIZONTAL_MARGIN: int
HEADER_VERTICAL_MARGIN: int
FOOTER_SPACING: int
FOOTER_LEFT_MARGIN: int
FOOTER_RIGHT_MARGIN: int
FOOTER_VERTICAL_MARGIN: int

class RigTreePushButton(QtWidgets.QPushButton):
    def __init__(self, text: str) -> None: ...

class RigTreeIconButton(QtWidgets.QPushButton):
    def __init__(self) -> None: ...

class RigTreeMenuField(QtWidgets.QWidget):
    combobox: hou.qt.ComboBox
    label: QtWidgets.QLabel | None
    activated: ClassVar[QtCore.Signal]
    def __init__(self, items: Sequence[str] | None = None, label_text: str | None = None) -> None: ...
    def currentIndex(self) -> int: ...
    def setCurrentIndex(self, index: int) -> None: ...
    def clear(self) -> None: ...
    def addItems(self, items: Sequence[str]) -> None: ...

class RigTreeLineEdit(QtWidgets.QLineEdit):
    '''
    Custom QLineEdit class so we can overwrite "Enter" and "Esc" key presses.
    We want "Enter" to clear the focus in the parm and "Esc" to clear the
    focus and revert values to before the edit.
    '''
    escapePressed: ClassVar[QtCore.Signal]
    def __init__(self) -> None: ...
    def focusInEvent(self, event: QtGui.QFocusEvent) -> None: ...
    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None: ...

class RigTreeFilterField(QtWidgets.QGroupBox):
    label: QtWidgets.QLabel
    line_edit: RigTreeLineEdit
    filterChanged: ClassVar[QtCore.Signal]
    def __init__(self, label_text: str) -> None: ...

class DisableSelectionHandler:
    """
    Helper class to use within a 'with' statement to disable selection handling.
    """
    parent_tree: RigTreeView | None
    parent_list: RigFlatView | None
    disable: bool
    saved_tree: _SelectionHandler | None
    saved_list: _SelectionHandler | None
    def __init__(self, parent: RigTreeWidget | RigTreeViewDialog, disable: bool = True) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None) -> None: ...

class RigTreeWidget(QtWidgets.QWidget):
    """
    Widget that encapsulates the rig tree view and model.

    Acts as a controller to the model and view, and hides away the Qt interface
    exposed by the view and model.

    If setNode() is called with an object node, traverses the network
    consisting of all of that object node's siblings (i.e. its parent's
    children).

    If setNode() is called with a SOP node, collects the points produced by the
    SOP node and interprets the hierarchy via the prims generated by that SOP
    node.
    """
    _module: _RigTreeConfig | None
    def __init__(self, panetab: hou.PythonPanel | None = None) -> None: ...
    def showEvent(self, event: QtGui.QShowEvent) -> None: ...
    def currentView(self) -> RigTreeView | RigFlatView: ...
    def changeType(self, new_type_index: int) -> None:
        """
        change the tree type externally, without resetting the pane
        """
    def closeAfterSelectionChanged(self, checked: bool) -> None: ...
    def openBeforeSelectionChanged(self, checked: bool) -> None: ...
    def closeAfterStateChanged(self, checked: bool) -> None: ...
    def openBeforeStateChanged(self, checked: bool) -> None: ...
    def selectItems(self, index_item_ids: int | QtCore.QModelIndex | list[int] | list[_ItemId] | list[QtCore.QModelIndex], select_if_true: bool, clear_selection: bool = False, enable_handler: bool = True) -> bool:
        """
        Highlight or un-highlight the specified item in the views
        without triggering the selection handler.

        Returns False if the item wasn't found or if it is not valid,
        True if the item was found.
        :param index_item_id: QModelIndex or its data (i.e., point number)
            or a list of those
        :type index_item_id: QtCore.QModelIndex or int or list of
            QtCore.QModelIndex or int.

        Selection is idempotent.
        """
    def setCurrentItem(self, index_item_id: int | QtCore.QModelIndex) -> bool:
        """
        Set index_item_id to being current without performing any selection.

        Returns False if the index_item_id wasn't found or is not valid,
        True if the item was found.
        :param index_item_id: QModelIndex or its data (i.e., point number)
            to set as current
        :type index_item_id: QtCore.QModelIndex or int
        """
    @typing.overload
    def selectedItems(self, get_item_name: Literal[False] = ...) -> list[_ItemId]: ...
    @typing.overload
    def selectedItems(self, get_item_name: Literal[True]) -> list[str]: ...
    @typing.overload
    def selectedItems(self, get_item_name: bool) -> list[_ItemId] | list[str]: ...
    def selectedIndexes(self) -> list[QtCore.QModelIndex]:
        """Return list of currently selected indices."""
    def clearSelection(self, enable_handler: bool = True) -> None: ...
    @typing.overload
    def currentItem(self, get_item_name: Literal[False] = ...) -> _ItemId | None: ...
    @typing.overload
    def currentItem(self, get_item_name: Literal[True]) -> str | None: ...
    @typing.overload
    def currentItem(self, get_item_name: bool) -> _ItemId | str | None: ...
    def currentIndex(self) -> QtCore.QModelIndex:
        """Return the current item index."""
    def disableItems(self, item_ids: Container[_ItemId]) -> None:
        """
        Disable indices in the model.

        :param item_ids: list of index data (i.e. point number)
        :type item_ids: list of int
        """
    def indexAtEventPos(self, event: QtGui.QContextMenuEvent) -> QtCore.QModelIndex:
        """Return the index at the current event position."""
    def deleteSelection(self) -> None: ...
    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        """
        Opens the actions context menu.
        """
    def acceptSelection(self) -> None:
        """
        Run the accept_selection method from the config(GroupRigTreeConfig)
        when we Accept the parm selection by pressing Enter in the pane or by
        pressing the Accept button.
        """
    def cancelSelection(self) -> None:
        """
        Run the cancel_selection method from the config (GroupRigTreeConfig)
        when the parm selection is cancelled by pressing Escape in the
        scene viewer or by pressing the Cancel button.
        """
    def inputIndex(self) -> int:
        """
        Return the input index when the rigtree is opened from a
        parm selector button.
        """
    def setInputIndex(self, input_index: int) -> None:
        """
        Set the input index when the rigtree is opened from a
        parm selector button.
        """
    def updateFooterVisibility(self) -> None:
        """Updates the visibility of the footer widgets."""
    def setOverrideConfig(self, config: _RigTreeConfig) -> None:
        """
        Overwrite the rig config when the rigtree is opened from a
        parm selector button.
        """
    def clearConfig(self) -> None:
        """
        Clear the parm selector rig config and allow the pane to
        reinstate the main config on the next setNode call.
        """
    def setSelectionNodePath(self, selection_node: hou.Node) -> None:
        """
        If the rig tree config has a nodePath property, this function
        will update the node path. This is called in response to the name
        of the selection node changing.

        For the GroupRigTreeConfig this makes sense since our selection node
        will usually be an upstream node and we want to make sure we update our
        selection if we rename that node.
        For the StateRigTreeConfig this does not really make sense since the
        selection node should NOT live outside of our current node, but rather
        be inside, which means that we are not worried about renaiming it.
        """
    def getCurrentNodePath(self) -> str | None:
        """
        Get the path to the current node.
        We will return the current node, even if we have a valid
        selection node.
        """
    def setNode(self, node: hou.Node | None) -> None:
        """
        Traverses the given node and updates the tree view to display the
        new network rooted at the node.

        If node is None or we're retraversing using the same node and mode as
        the last traversal, this is a no-op.
        """
    def _setMode(self, mode_type: type[SopRigMode] | type[ObjRigMode], node_path: str | None = None) -> None: ...
    def addRigModeEventCallbacks(self) -> None: ...
    def removeRigModeEventCallbacks(self) -> None: ...
    def updateSelectionFromNode(self, event_type: hou.EnumValue[hou.nodeEventType] | None = None, input_node: hou.OpNode | None = None) -> None:
        """
        Call the get_selection callback to get the inital state.
        """
    def setSelectionModeFromConfig(self) -> None:
        """
        Set the selection mode from the config.
        """
    def setSelectionMode(self, sel_mode: QtWidgets.QAbstractItemView.SelectionMode) -> None:
        """
        Sets the view's selection mode to sel_mode.
        """
    def getSelectionMode(self) -> QtWidgets.QAbstractItemView.SelectionMode:
        """
        Gets the view's selection mode.
        """
    def disablePinned(self, sel_node: hou.NetworkMovableItem | None) -> None: ...
    def setDisabled(self, disable: bool) -> None:
        """
        Disable all items in the model.
        """
    def isDisabled(self) -> bool: ...
    def _loadExpansionState(self) -> dict[str, dict[str, set[_ItemId]]]:
        """Load saved expansion state from the root node's userData."""
    def resetPane(self) -> None:
        """
        Reset the pane by clearing the config and forcing a retraversal.
        """
    def clearPane(self) -> None:
        """
        Clear the current pane.
        We run this onHipFileAfterClear to make sure we clear the pane
        when we opean a new .hip file for example.
        """
    def registerSelectionCallback(self) -> None:
        """
        Add custom selection handling so we can set the pane to disabled
        if it is pinned and we change the the node selection.
        """
    def removeSelectionCallback(self) -> None: ...

class RigMode:
    """
    Inheritance for the SopRigMode and ObjRigMode.
    """
    def __init__(self, node_path: str) -> None: ...
    def widget(self) -> RigTreeWidget | None: ...
    def setWidget(self, w: RigTreeWidget) -> None:
        """Back pointer to the parent widget"""
    def useSubnetOutputs(self) -> bool: ...
    def setUseSubnetOutputs(self, on: bool) -> None: ...
    def get_default_drag_drop(self) -> Callable[[_DragDropKwargs], bool] | None: ...
    def get_default_rename(self) -> Callable[[_RenameKwargs], bool] | None: ...
    def get_default_select(self) -> Callable[[_SelectKwargs], None]: ...
    def get_default_get_selection(self) -> Callable[[_GetSelectionKwargs], bool]: ...
    def setTreeUpdateHandler(self, handler: Callable[[], object] | None) -> None:
        """
        Register a handler to be called when there is a tree update.
        """
    def setHeaderUpdateHandler(self, handler: Callable[[], object] | None) -> None:
        """
        Register a handler to be called when there is a header update.
        """
    def addEventCallbacks(self) -> None:
        """Default method for adding events to the node of interest."""
    def removeEventCallbacks(self) -> None:
        """Default method for removing events from the node of interest."""

class SopRigMode(RigMode):
    """
    Build tree from a SOP node.
    """
    def __init__(self, sop_node_path: str) -> None: ...
    def addEventCallbacks(self) -> None: ...
    def removeEventCallbacks(self) -> None: ...
    def connectSelectionNodePath(self, selection_node_path: str) -> None: ...
    def nodePath(self) -> str: ...
    def selectionNodePath(self) -> str | None: ...
    def selectionNode(self) -> hou.SopNode | None: ...
    def stateName(self) -> str:
        """
        Get the state name from the selected node.

        If the node is not an hda, we just get the node type name and format it
        like we format the state names.
        """
    def header(self) -> str: ...
    def selectOutput(self, output_index: int) -> None: ...
    def outputNames(self) -> list[str]:
        """
        Retrieve the list of connection names expected by selectOutput.
        """
    @staticmethod
    def treeType() -> TreeType: ...
    def tree(self) -> tuple[GenericTree[int], _RoleProvider[int]]: ...

class ObjRigMode(RigMode):
    """
    See the hierarchy of the OBJ-level rigs in the view.
    See 'geo' obj level nodes in the view as well.
    """
    def __init__(self, obj_node_path: str) -> None: ...
    def addEventCallbacks(self) -> None: ...
    def removeEventCallbacks(self) -> None: ...
    def nodePath(self) -> str: ...
    def header(self) -> str: ...
    def selectOutput(self, index: int) -> None: ...
    def outputNames(self) -> list[str]: ...
    def tree(self) -> tuple[GenericTree[str], _RoleProvider[str]]:
        """Traverse obj_node's children network."""
    def get_default_rename(self) -> Callable[[_RenameKwargs], bool]: ...
    def get_default_drag_drop(self) -> Callable[[_DragDropKwargs], bool]: ...

class FoldersSelectionHandler:
    """
    Helper class to manage selections when using the rig tree pane in packed
    folders mode.
    """
    def __init__(self, node_path: str) -> None: ...
    def select(self, kwargs: _SelectKwargs) -> None: ...
    def get_selection(self, kwargs: _GetSelectionKwargs) -> Literal[True]: ...

class FoldersRigMode(SopRigMode):
    """
    See the hierarchy of a packed folders structure in rig tree view
    """
    def __init__(self, node_path: str) -> None: ...
    @staticmethod
    def treeType() -> TreeType: ...
    def tree(self) -> tuple[GenericTree[str], _RoleProvider[str]]:
        """Build a GU_PackedFolders object and build a tree with file paths"""
    def stateName(self) -> str: ...

class FlatViewProxyModel(QtCore.QSortFilterProxyModel):
    """
    Converts the tree model into a flat list model for display in the QListView
    and performs filtering and flat list sorting.

    The model is sorted first and then filtered to prevent sorting the original
    model after each filter action.

    NOTE: This class inherits from QSortFilterProxyModel instead of
    QAbstractProxyModel to access invalidate(), mapSelectionFromSource(),
    mapSelectionToSource() and signals for free.
    """
    source_indices: list[QtCore.QModelIndex]
    def __init__(self) -> None: ...
    def updateModel(self, model: QtGui.QStandardItemModel | None) -> None: ...
    def setSourceModel(self, model: QtGui.QStandardItemModel) -> None: ...
    def mapFromSource(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex: ...
    def mapToSource(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex: ...
    def columnCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> int: ...
    def rowCount(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> int: ...
    def index(self, row: int, column: int, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex | None) -> QtCore.QModelIndex: ...
    def parent(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex: ...
    def sibling(self, row: int, column: int, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.QModelIndex: ...
    def setPattern(self, pattern: str) -> None: ...
    def filter(self) -> Literal[True]: ...
    def sort(self, sort_key: SortKey) -> bool:
        """
        Sorts the proxy model by the given sort key.

        :param sort_key: key to sort by.
        :type sort_type: SortKey
        """

class RigTreeFilterProxyModel(QtCore.QSortFilterProxyModel):
    """
    Filter the source model based on the 'Filter By' parm string and return the
    result as another model. We do not want to rebuild the mode
    every time we filter.
    """
    def __init__(self) -> None: ...
    def setPattern(self, pattern: str) -> None: ...
    def hasChildren(self, parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> bool: ...
    def filterAcceptsRow(self, source_row: int, source_parent: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool: ...

class RigTreeModel(QtGui.QStandardItemModel):
    """
    Holds resolved rig tree data.

    Encapsulates drag-drop and rename operations.

    For the time being, drag-drop is limited to single items only.
    """
    delete_handler: _DeleteHandler | None
    rig_actions_handler: _RigActionsHandler | None
    treeUpdateSignal: ClassVar[QtCore.Signal]
    def __init__(self, parent: RigTreeWidget | RigTreeViewDialog) -> None: ...
    def setDragDropHandler(self, handler: _DragDropHandler | None) -> None:
        """Register handler called for each drag, drop event.

        The handler is passed the item data of what's being dragged, the old
        parent data, and the new parent data.

        For SOP networks, the item data would be the index of the point. For OBJ
        networks, the item data would be the object node's full path before the
        swap (i.e. with the old parent).

        """
    def setRenameHandler(self, handler: _RenameHandler | None) -> None:
        """The rename handler is called whenever the user renames an item.

        The handler is passed 3 arguments: the id of the item being renamed
        (i.e. node path or point number for the object rig and SOP rig cases
        respectively), the old name, and the new name.

        """
    def getRenameHandler(self) -> _RenameHandler | None: ...
    def setDeleteHandler(self, handler: _DeleteHandler | None) -> None: ...
    def getDeleteHandler(self) -> _DeleteHandler | None: ...
    def setRigActionsHandler(self, handler: _RigActionsHandler | None) -> None: ...
    def getRigActionsHandler(self) -> _RigActionsHandler | None: ...
    def setDisabled(self, disabled: bool) -> None: ...
    def isDisabled(self) -> bool: ...
    def setDisabledItems(self, items: Container[_ItemId]) -> None:
        """
        Store a subset of items to disable.

        :param items: we store the items as a list of index data
            (i.e., point numbers)
        :type items: list of int
        """
    def dropMimeData(self, data: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, col: int, parent_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool: ...
    def mimeData(self, indexes: Sequence[QtCore.QModelIndex]) -> QtCore.QMimeData: ...
    def flags(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtCore.Qt.ItemFlag: ...
    def setData(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, value: Any, role: int = ...) -> bool:
        """
        Overridden such that edit role updates are passed to the rename
        handler.
        """
    def mapFromSource(self, index: QtCore.QModelIndex) -> QtCore.QModelIndex:
        """Returns the index directly since it's not a proxy."""
    def mapToSource(self, index: QtCore.QModelIndex) -> QtCore.QModelIndex:
        """Return the index directly since it's not a proxy."""

class RigTreeViewDelegate(QtWidgets.QStyledItemDelegate):
    """
    A delegate to draw the rig tree row and react to QLineEdit editor open/close
    when renaming.
    """
    PADDING: ClassVar[int]
    MARGIN: ClassVar[int]
    HIDDEN_TEXT_COLOR: ClassVar[QtGui.QColor]
    DESCRIPTION_TEXT_COLOR: ClassVar[QtGui.QColor]
    BADGE_SIZE: ClassVar[int]
    BADGE_COLUMN_COUNT: int
    def __init__(self, parent: RigTreeView | RigFlatView) -> None: ...
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...
    def initStyleOption(self, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...
    def createEditor(self, parent: QtWidgets.QWidget | None, option: QtWidgets.QStyleOptionViewItem, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> QtWidgets.QWidget: ...
    def destroyEditor(self, editor: QtWidgets.QWidget, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> None: ...

class RigTreeView(QtWidgets.QTreeView):
    """
    Tree view of an arbitrary rig hierarchy.
    """
    _selection_handler: _SelectionHandler | None
    ignore_key_events_outside_window: bool
    def __init__(self) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def expandSubTree(self, root_index: QtCore.QModelIndex, expand: bool) -> None:
        """Expand or collapse all nodes of the subtree rooted at root_index.

        :param root_index: QModelIndex belonging to the tree's model.
        :param expand: expands if True, collapses all if False.
        """
    def setExpanded(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, expand: bool, convert_index: bool = True) -> None:
        """
        Set the index to expanded.
        Convert the passed in index to the one from the proxy model.

        :param convert_index: if called from within the view, there might be no
            need to perform the conversion since we can get the correct index
            directly from the self.model()(taht pints to the proxy model) if
            called from outside, the passed in index will be from the base model
            and not from the proxy model.
        :type convert_index: bool
        """
    def selectSubTree(self, root_index: QtCore.QModelIndex, select: bool) -> None:
        """Select or deselect all nodes of the subtree rooted at root_index."""
    def setSelectionHandler(self, handler: _SelectionHandler | None) -> None:
        """
        The selection handler is called whenever an item is selected in
        the view.

        The handler accepts two arguments:
        1. A list of items selected by ID (either the node path or point index)
        2. A list of items deselected.
        """
    def getSelectionHandler(self) -> _SelectionHandler | None: ...
    def selectionChanged(self, selected: QtCore.QItemSelection, deselected: QtCore.QItemSelection) -> None: ...
    def select(self, index: QtCore.QModelIndex | QtCore.QItemSelection | list[QtCore.QModelIndex], select_if_true: bool, clear: bool = False, convert_index: bool = True) -> None:
        """
        Select or deselect the item at `index`.

        :param convert_index: If called from within the view, there might be no
            need to perform the conversion since the correct index can be
            acquired directly from self.model() (points to the proxy model).
            If called from outside the view, the index will originate from the
            base model rather than the proxy model.
        :type convert_index: bool
        """
    def setCurrent(self, index: QtCore.QModelIndex, convert_index: bool = True) -> None:
        """
        Set the item at `index` as current. This method does not perform any
        selections, only setting the index as current.

        :param convert_index: If called from within the view, there might be no
            need to perform the conversion since the correct index can be
            acquired directly from self.model() (points to the proxy model).
            If called from outside the view, the index will originate from the
            base model rather than the proxy model.
        :type convert_index: bool
        """
    def reselectSelected(self) -> None:
        """
        Re-send the currently selected items to the handler.
        If no handler has been registered, then no-op.
        """

class RigFlatView(QtWidgets.QListView):
    """
    Flattened list view of an arbitrary rig hierarchy.
    """
    ignore_key_events_outside_window: bool
    _selection_handler: _SelectionHandler | None
    def __init__(self) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def keyReleaseEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def mouseDoubleClickEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def setSelectionHandler(self, handler: _SelectionHandler | None) -> None:
        """
        The selection handler is called whenever an item is selected in
        the view.

        The handler accepts two arguments:
        1. A list of items selected by ID (either the node path or point index)
        2. A list of items deselected.
        """
    def getSelectionHandler(self) -> _SelectionHandler | None: ...
    def selectionChanged(self, selected: QtCore.QItemSelection, deselected: QtCore.QItemSelection) -> None: ...
    def select(self, index: QtCore.QModelIndex | QtCore.QItemSelection | list[QtCore.QModelIndex], select_if_true: bool, clear: bool = False, convert_index: bool = True) -> None:
        """
        Select or deselect the item at `index`.

        :param convert_index: If called from within the view, there might be no
            need to perform the conversion since the correct index can be
            acquired directly from self.model() (points to the proxy model).
            If called from outside the view, the index will originate from the
            base model rather than the proxy model.
        :type convert_index: bool
        """
    def setCurrent(self, index: QtCore.QModelIndex, convert_index: bool = True) -> None:
        """
        Set the item at `index` as current. This method does not perform any
        selections, only setting the index as current.

        :param convert_index: If called from within the view, there might be no
            need to perform the conversion since the correct index can be
            acquired directly from self.model() (points to the proxy model).
            If called from outside the view, the index will originate from the
            base model rather than the proxy model.
        :type convert_index: bool
        """
    def reselectSelected(self) -> None:
        """
        Re-send the currently selected items to the handler.
        If no handler has been registered, then no-op.
        """
    def sort(self, sort_key: SortKey) -> None:
        """
        Sort the list view and convert the selection to the new proxy model
        following the sort.
        """
