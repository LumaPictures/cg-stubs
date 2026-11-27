import hou
from builtins import zip as zip
from collections.abc import Sequence
from hutil.PySide import QtCore, QtWidgets
from kinefx import rigapi as rigapi
from kinefx.rigtree import GenericTree as GenericTree
from kinefx.ui.rigtreewidget import DESCRIPTION_ROLE as DESCRIPTION_ROLE, DisableSelectionHandler as DisableSelectionHandler, ICON_BONE as ICON_BONE, ICON_CHANNEL as ICON_CHANNEL, ICON_CHARACTER as ICON_CHARACTER, ICON_ROLE as ICON_ROLE, ITEM_ID_ROLE as ITEM_ID_ROLE, NAME_ROLE as NAME_ROLE, RigTreeModel as RigTreeModel, RigTreePushButton as RigTreePushButton, RigTreeView as RigTreeView, _RoleProvider, add_tree_to_model as add_tree_to_model, selection_item as selection_item
from typing import Literal, Required, TypedDict

from typing import TypeAlias
from collections.abc import Callable
from typing import TypeAlias
_DialogCallback: TypeAlias = Callable[[_DialogCallbackArgs], object]
class _DialogCallbackArgs(TypedDict, total=False):
    type: Required[Literal['accept', 'cancel', 'change', 'update_sel_geo']]
    dialog: RigTreeViewDialog
    selection: Sequence[str]
    ret: hou.Geometry

class RigTreeViewDialog(QtWidgets.QDialog):
    """ A simple RigTree Dialog for picking paths directly from strings.
        @parent is the parent window, or the hou.qt.mainWindow when None.
        @paths is the list of available paths. You should include the leafs and the folders.
        @sel_paths is the list of selected paths.
        @abstract_paths is the list of abstract paths. We use it to pin theses paths when interacting with the viewport.
        @cb is a selection callback that will be called with a single kwargs argument.
    """
    _sel_paths: Sequence[str]
    _callback: _DialogCallback | None
    def __init__(self, parent: QtWidgets.QWidget | None = None, paths: Sequence[str] = ..., sel_paths: Sequence[str] = ..., abstract_paths: Sequence[str] = ..., cb: _DialogCallback | None = None) -> None: ...
    def setPaths(self, paths: Sequence[str]) -> None: ...
    def setSelectedPaths(self, sel_paths: Sequence[str]) -> None: ...
    def setAbstractPaths(self, abstract_paths: Sequence[str]) -> None: ...
    def treeview(self) -> RigTreeView: ...
    def isDisabled(self) -> bool: ...
    def _viewSelection(self, geo: hou.Geometry, sel: hou.Selection) -> None: ...
    def tree(self) -> tuple[GenericTree[int], _RoleProvider[int]]: ...
    def updateTreeSelection(self) -> None: ...
    def selectItems(self, index_item_id: QtCore.QModelIndex | list[QtCore.QModelIndex], select_if_true: bool, clear_selection: bool = False, enable_handler: bool = True) -> bool:
        """
        Highlight or un-highlight the specified item in the views
        without triggering the selection handler.

        Returns False if the item wasn't found or if it is not valid, True if the item was found.
        :param index_item_id: QModelIndex or its data(i.e. point number) or a list of those
        :type index_item_id: QtCore.QModelIndex or int or list of (QtCore.QModelIndex or int)

        Selection is idempotent.
        """
