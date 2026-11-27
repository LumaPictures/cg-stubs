from collections.abc import Callable, Sequence
from typing import Literal, Required, TypeAlias, TypedDict

import hou
from hutil.PySide import QtCore, QtWidgets
from kinefx.rigtree import GenericTree
from kinefx.ui.rigtreewidget import RigTreeView, _RoleProvider

# What the dialog passes its callback: on accept, cancel or a tree view selection change; the
# motion mixer state also asks it for a new selection geometry ("update_sel_geo"), which the
# callback returns as "ret".
class _DialogCallbackArgs(TypedDict, total=False):
    type: Required[Literal["accept", "cancel", "change", "update_sel_geo"]]
    dialog: "RigTreeViewDialog"
    selection: Sequence[str]
    ret: hou.Geometry

_DialogCallback: TypeAlias = Callable[[_DialogCallbackArgs], object]

class RigTreeViewDialog(QtWidgets.QDialog):
    _sel_paths: Sequence[str]
    _callback: _DialogCallback | None
    def __init__(self, parent: QtWidgets.QWidget | None = ..., paths: Sequence[str] = ..., sel_paths: Sequence[str] = ..., abstract_paths: Sequence[str] = ..., cb: _DialogCallback | None = ...) -> None: ...
    def setPaths(self, paths: Sequence[str]) -> None: ...
    def setSelectedPaths(self, sel_paths: Sequence[str]) -> None: ...
    def setAbstractPaths(self, abstract_paths: Sequence[str]) -> None: ...
    def treeview(self) -> RigTreeView: ...
    def isDisabled(self) -> bool: ...
    def _viewSelection(self, geo: hou.Geometry, sel: hou.Selection) -> None: ...
    def tree(self) -> tuple[GenericTree[int], _RoleProvider[int]]: ...
    # An item id (or a list of them) would need the _findIndex the dialog lacks.
    def selectItems(self, index_item_id: QtCore.QModelIndex | list[QtCore.QModelIndex], select_if_true: bool, clear_selection: bool = ..., enable_handler: bool = ...) -> bool: ...
