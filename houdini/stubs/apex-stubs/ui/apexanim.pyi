from collections.abc import Collection, Sequence
from hutil.PySide import QtGui, QtWidgets
from typing import Protocol, TypedDict

from typing import TypeAlias
from typing import TypeAlias
_PathEdit: TypeAlias = tuple[list[str], list[str]]
class _ApplyFn(Protocol):
    def __call__(self, active_clip: str | None, edits_folders: list[_PathEdit], edits_rigpaths: list[_PathEdit], refresh: bool) -> object: ...

class _EditPathsArgs(TypedDict, total=False):
    edit_paths: Sequence[tuple[str, str]]
    valid_rig_paths: Collection[str]
    valid_clips: Sequence[str]
    active_clip: str

class AnimationTreeView(QtWidgets.QTreeView):
    """ QTreeView with drag and drop for the Animation QTreeView"""
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...

class EditAnimationDialog(QtWidgets.QDialog):
    """ A dialog to rename apex animation .clip and rigpath."""
    myPaths: Sequence[tuple[str, str]]
    myValidRigPaths: Collection[str]
    myValidClips: Sequence[str]
    myActiveClip: str
    myApplyFn: _ApplyFn | None
    mySaveExpanded: set[str]
    mySaveSelected: set[str]
    myTreeView: AnimationTreeView
    myModel: QtGui.QStandardItemModel
    iconSize: int
    myFolderIcon: QtGui.QIcon
    myClipInstIcon: QtGui.QIcon
    myClipCurrentIcon: QtGui.QIcon
    myChannelIcon: QtGui.QIcon
    myCharIcon: QtGui.QIcon
    myToolIcon: QtGui.QIcon
    myWarningIcon: QtGui.QIcon
    myNoIcon: QtGui.QIcon
    myItemFont: QtGui.QFont
    myItemFontStrike: QtGui.QFont
    myItemFontBold: QtGui.QFont
    myItemFontBoldStrike: QtGui.QFont
    bottom_row: QtWidgets.QHBoxLayout
    keep_toggle: QtWidgets.QCheckBox
    group_toggle: QtWidgets.QCheckBox
    refresh_button: QtWidgets.QPushButton
    apply_button: QtWidgets.QPushButton
    close_button: QtWidgets.QPushButton
    layout: QtWidgets.QVBoxLayout
    mySetActiveClipAction: QtGui.QAction
    myCopyClipAction: QtGui.QAction
    myDeleteAction: QtGui.QAction
    myKeepAction: QtGui.QAction
    myClipMenu: QtWidgets.QMenu
    myInputClipMenu: QtWidgets.QMenu
    myFolderMenu: QtWidgets.QMenu
    myModelItems: dict[str, QtGui.QStandardItem]
    def __init__(self) -> None: ...
    def createItem(self, icon: QtGui.QIcon, label: str) -> QtGui.QStandardItem: ...
    def onContextMenu(self) -> None: ...
    def selectedItems(self) -> list[QtGui.QStandardItem]:
        """ Returns the selected items. """
    def setItemDeleteOrKeep(self, item: QtGui.QStandardItem, delete_or_keep: bool) -> None:
        """ Mark an item for delete or keep.
            @delete_or_keep=True means to delete.
            @delete_or_keep=False means to keep.
        """
    def onDelete(self) -> None:
        """ Delete Action callback."""
    def onKeep(self) -> None:
        """ Keep Action callback."""
    def onSetActiveClip(self) -> None:
        """ Set Active Clip Action callback."""
    def setActiveClip(self, copy_active_to_stash: bool) -> None: ...
    def onCopyToStash(self) -> None:
        """ Copy To Stash Action callback."""
    def onClose(self) -> None:
        """ Close button simply hides the dialog. """
    def updateItemFromData(self, item: QtGui.QStandardItem) -> None:
        """ Change the icon and font based on the item's data."""
    def itemParent(self, item: QtGui.QStandardItem) -> QtGui.QStandardItem | None:
        """ Returns the item parent folder in the treeview."""
    def itemPath(self, item: QtGui.QStandardItem) -> list[str]:
        """ Returns the item path as a list of strings. This uses the names we
            see in the UI."""
    def itemPathFixed(self, item: QtGui.QStandardItem) -> list[str]: ...
    def saveExpandSelect(self) -> None:
        """ Save the expanded state of items."""
    def onApply(self) -> None:
        """ Apply button callback. Extract back the edited paths and call back
            myApplyFn."""
    def apply(self, refresh: bool, edits_folders: list[_PathEdit]) -> None:
        """ Apply button callback. Extract back the edited paths and call back
            myApplyFn."""
    def setApplyFn(self, fn: _ApplyFn | None) -> None:
        """ Set the apply callback doing the real work in apexsoputils.py."""
    def onRefresh(self) -> None:
        """ Refresh button"""
    def onGroupToggled(self, checked: bool) -> None: ...
    def updateFromPaths(self, args: _EditPathsArgs = ...) -> None:
        """ Rebuild the treeview from a list of path tuples.
            @paths If None, reuse self.myPaths
        """
