import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import hou
from apex.ui.animationlayers.model import BASE_LAYER_NAME as BASE_LAYER_NAME
from collections.abc import Mapping, Sequence
from enum import Enum
from hutil.PySide import QtCore, QtWidgets
from typing import TypedDict, Unpack

class _MembershipViewKwargs(TypedDict, total=False):
    model: AnimationLayerMembershipModel | None

class MembershipColumn(Enum):
    NAME = 0

class AnimationLayerMembershipModel(QtCore.QAbstractItemModel):
    """The model which contains the parms present in a layer."""
    NAME_COLUMN_LABEL: str
    def __init__(self, scene_viewer: hou.SceneViewer | None = None) -> None: ...
    def sceneViewer(self) -> hou.SceneViewer | None: ...
    def setSceneViewer(self, scene_viewer: hou.SceneViewer | None) -> None: ...
    def setLayer(self, layer: str) -> None: ...
    def isBaseLayer(self) -> bool: ...
    def setParms(self, all_parms: Mapping[str, Sequence[str]]) -> None: ...
    def addParms(self, parms: Mapping[str, Sequence[str]]) -> None: ...
    def removeParms(self, indexes: Sequence[PySide6.QtCore.QModelIndex]) -> None: ...
    def clear(self) -> None: ...
    def columnCount(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> int:
        """Returns the number of columns in the model."""
    def rowCount(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex = ...) -> int:
        """The number of rows in the model rooted under index."""
    def parmNameFromIndex(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex | None) -> str | None:
        """Get the parm from the index."""
    def index(self, row: int, column: int, parent: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex = ...) -> PySide6.QtCore.QModelIndex:
        """ Get the index from the row and column and given parent. """
    def parent(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex) -> PySide6.QtCore.QModelIndex: ...
    def headerData(self, section: int, orientation: PySide6.QtCore.Qt.Orientation, role: int = ...) -> str | PySide6.QtCore.Qt.AlignmentFlag | None:
        """ Get the header data for the given section. """
    def data(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, role: int = ...) -> str | None:
        """Get the data from an index and role."""
    def setData(self, index: PySide6.QtCore.QModelIndex | PySide6.QtCore.QPersistentModelIndex, data: str, role: int = ...) -> bool:
        """ Set the data at an index. """

class AnimationLayerMembershipView(QtWidgets.QTableView):
    """
    Table used for displaying the parm membership of an AnimationLayer
    """
    ROW_HEIGHT: int
    def __init__(self, *args: PySide6.QtWidgets.QWidget | None, **kwargs: Unpack[_MembershipViewKwargs]) -> None: ...
    def resetModel(self, new_model: AnimationLayerMembershipModel | None) -> None:
        """
        Swap the model that the view uses to the new_model.
        Will first disconnect the selectionChanged from the current
        selection model, then change the model, then reset the view,
        then connect the selectionChanged signal for the new model.
        """
    def getModel(self) -> AnimationLayerMembershipModel | None:
        """
        Return the source model used internally.
        Note that this is not the proxy model.
        """
    def getSelectedRows(self) -> list[PySide6.QtCore.QModelIndex]: ...
    def contextMenuEvent(self, event: PySide6.QtGui.QContextMenuEvent) -> None: ...
