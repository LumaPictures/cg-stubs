import _pdgd
import hou
import threading
import weakref
from . import utils as utils
from .paginationhelper import PaginationHelper as PaginationHelper
from .taskgraphtable import TaskGraphTable as TaskGraphTable
from collections.abc import Mapping, Sequence
from hutil.Qt import QtCore
from pdgd.util import PDGDObject
from typing import Any, ClassVar

ICON_SIZE: int
ATTRIBUTE_PREFIX: str
MAX_VISIBLE_COLUMNS: int

def qt_icon(icon_name: str, size: int) -> hou.qt.Icon:
    """Like hou.qt.icon but cached."""
def human_size(num: float, suffix: str = 'B') -> str:
    """ Helper to convert bytes into more readable units """
def safestr(v: object) -> str:
    """ Helper to stringify an unknown object value """

class TaskGraphTableError(Exception):
    """ Base class for task graph table exceptions """
class EmptyQuery(TaskGraphTableError):
    """ Raised when no nodes are selected to build a query """
class WorkItemNotFound(TaskGraphTableError):
    """ Raised when a work item can't be found """

class AttributeEntry:
    name: str
    text: str
    selected: bool
    def __init__(self, name: str, text: str, selected: bool) -> None: ...

class TaskGraphTableModel(QtCore.QAbstractTableModel):
    """ Table model for work items in a set of nodes """
    data_layer: _pdgd.DataLayerInterface
    data_lock: threading.RLock
    task_graph_table: weakref.ref[TaskGraphTable]
    pagination_helper: PaginationHelper
    node_list: Sequence[str] | None
    current_query: str | None
    query_object: PDGDObject | None
    sort_enabled: bool
    sort_property: str
    reverse_sort: bool
    work_item_selected: ClassVar[QtCore.Signal]
    def __init__(self, task_graph_table: TaskGraphTable, data_layer: _pdgd.DataLayerInterface, parent: QtCore.QObject | None = None) -> None: ...
    def clear(self) -> None:
        """ Remove every item """
    def getNodeIcon(self, row: int) -> str | None:
        """ Returns the work item's node icon """
    def getNodeId(self, row: int) -> int | None:
        """ Attempts to retrieve an id representing the TOP node """
    def updateNodes(self, node_list: Sequence[str] | None) -> None: ...
    def query(self) -> None: ...
    def onWorkItemUpdated(self, path: str, wi_object: Mapping[str, object], message: _pdgd.Message | None, just_created: bool = False) -> None:
        """ Called when a work item changes """
    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...) -> str | None:
        """ If horizontal, return the header for the given index. """
    def rowCount(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> int:
        """ Number of rows in the model """
    def columnCount(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex = ...) -> int:
        """ Number of columns in the model """
    def data(self, index: QtCore.QModelIndex | QtCore.QPersistentModelIndex, role: int = ...) -> Any:
        """ Return data for the given role. """
    def attributeSelectionChanged(self, attribute_item: AttributeEntry) -> None:
        """ Called when an attribute visibility has changed """
    @utils.print_exceptions
    def sort(self, ncol: int, order: QtCore.Qt.SortOrder) -> None:
        """ Model sort function """
    def double_click(self, index: QtCore.QModelIndex) -> None:
        """Handle a double click at the given cell.

        This needs to be in the model because only the model can access the
        parameters needed for createWorkItemInfoWindow.
        """
    def pressed(self, index: QtCore.QModelIndex) -> None:
        """Handle a mouse press at the given cell.

        This is used to implement middle-mouse opening of the work item info
        window, just like middle mouse on a workitem dot.
        """
    def current_changed(self, current: QtCore.QModelIndex, previous: QtCore.QModelIndex) -> None:
        """
            Slot for when the current item changes.
            This updates the current selected workitem in TOPs.
        """
    def getItemRow(self, item_id: int) -> int:
        """
            Returns the index row of a given work item id
            Raises WorkItemNotFound if now row has that id
        """
    def nextPage(self) -> None:
        """ Moves to the next page of work items """
    def prevPage(self) -> None:
        """ Moves to the previous page of work items """
    def lastPage(self) -> None:
        """ Moves to the last page of work items """
    def firstPage(self) -> None:
        """ Moves to the first page of work items """
    def setItemsPerPage(self, items_per_page: int) -> None:
        """ Sets the number of work items per page """
    def nextPage10(self) -> None:
        """ Skips 10 pages ahead """
    def nextPage100(self) -> None:
        """ Skips 100 pages ahead """
    def prevPage10(self) -> None:
        """ Skips 10 pages behind """
    def prevPage100(self) -> None:
        """ Skips 100 pages behind """
