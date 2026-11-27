from collections.abc import Collection, Sequence
from typing import Protocol, TypeAlias, TypedDict

from PySide6 import QtGui, QtWidgets

# A rename or delete: (old path, new path), the new one empty to delete. Paths are lists of folder
# names under /animation (a rig path's last item is the rig path).
_PathEdit: TypeAlias = tuple[list[str], list[str]]

class _ApplyFn(Protocol):
    # active_clip is None on a refresh.
    def __call__(
        self, active_clip: str | None, edits_folders: list[_PathEdit], edits_rigpaths: list[_PathEdit], refresh: bool
    ) -> object: ...

# apexsoputils.editStashedAnimation()'s description of the stash.
class _EditPathsArgs(TypedDict, total=False):
    # (packed path, its rig_path, '' for a clip folder)
    edit_paths: Sequence[tuple[str, str]]
    valid_rig_paths: Collection[str]
    valid_clips: Sequence[str]
    active_clip: str

class AnimationTreeView(QtWidgets.QTreeView):
    def __init__(self, parent: QtWidgets.QWidget | None = ...) -> None: ...

class EditAnimationDialog(QtWidgets.QDialog):
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
    # Tree items by their "/"-joined path of labels; set by updateFromPaths().
    myModelItems: dict[str, QtGui.QStandardItem]
    def __init__(self) -> None: ...
    # The item also gets a myDefaultIcon attribute, the icon it reverts to.
    def createItem(self, icon: QtGui.QIcon, label: str) -> QtGui.QStandardItem: ...
    def onContextMenu(self) -> None: ...
    def selectedItems(self) -> list[QtGui.QStandardItem]: ...
    def setItemDeleteOrKeep(self, item: QtGui.QStandardItem, delete_or_keep: bool) -> None: ...
    def onDelete(self) -> None: ...
    def onKeep(self) -> None: ...
    def onSetActiveClip(self) -> None: ...
    def setActiveClip(self, copy_active_to_stash: bool) -> None: ...
    def onCopyToStash(self) -> None: ...
    def onClose(self) -> None: ...
    def updateItemFromData(self, item: QtGui.QStandardItem) -> None: ...
    def itemParent(self, item: QtGui.QStandardItem) -> QtGui.QStandardItem | None: ...
    def itemPath(self, item: QtGui.QStandardItem) -> list[str]: ...
    def itemPathFixed(self, item: QtGui.QStandardItem) -> list[str]: ...
    def saveExpandSelect(self) -> None: ...
    def onApply(self) -> None: ...
    def apply(self, refresh: bool, edits_folders: list[_PathEdit]) -> None: ...
    def setApplyFn(self, fn: _ApplyFn | None) -> None: ...
    def onRefresh(self) -> None: ...
    def onGroupToggled(self, checked: bool) -> None: ...
    def updateFromPaths(self, args: _EditPathsArgs = ...) -> None: ...
