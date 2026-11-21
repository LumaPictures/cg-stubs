from hutil.Qt import QtCore
from typing import ClassVar

class PaginationHelper(QtCore.QObject):
    """ Helper to calculate pagination """
    items_per_page: int
    current_page: int
    source: list[str]
    visible_items_changed: ClassVar[QtCore.Signal]
    page_changed: ClassVar[QtCore.Signal]
    def __init__(self, parent: QtCore.QObject | None) -> None: ...
    def ensureCurrentPageIsValid(self) -> None:
        """
            If the current page is past the last possible page,
            sets it to the last page
        """
    def updateVisibleItems(self) -> None:
        """ Emits the visible_items_changed signal """
    def nextPage(self, count: int = 1) -> None:
        """ Move to the next page """
    def prevPage(self, count: int = 1) -> None:
        """ Move to the previous page """
    def lastPage(self) -> None:
        """ Moves to the last page """
    def firstPage(self) -> None:
        """ Moves to the first page """
    def getPaginatedList(self) -> list[str]:
        """ Return the subset of items in the current page """
    def setSource(self, source: list[str]) -> None:
        """ Sets the source list """
    def setItemsPerPage(self, items_per_page: int) -> None:
        """ Sets the number of visible items per page """
