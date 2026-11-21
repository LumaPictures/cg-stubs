# Houdini stubs generated from Houdini 22.0.466

import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import hou
import husdui.prefs
from collections.abc import Iterable, Sequence
from hutil.PySide import QtWidgets
from pxr import Sdf as Sdf, Usd as Usd
from typing import ClassVar

CONDENSEDTREE_ICON: hou.qt.Icon
FULLTREE_ICON: hou.qt.Icon
ADD_COLLECTION_ICON: hou.qt.Icon

class PrimTreeWidget(QtWidgets.QWidget):
    """
    This widget is used to show a prim source tree.
    The view can be switched between list style view grouped by parent or a full hierarchy.
    """
    NodeEventTypes: tuple[hou.EnumValue[hou.nodeEventType], ...]
    NetworkEventTypes: tuple[hou.EnumValue[hou.nodeEventType], ...]
    NothingDirty: int
    ValuesDirty: int
    StructureDirty: int
    NeedsReset: int
    ViewMode_List: int
    ViewMode_Tree: int
    treeSelectionChanged: ClassVar[PySide6.QtCore.Signal]
    hotkeyInvoked: ClassVar[PySide6.QtCore.Signal]
    itemDropped: ClassVar[PySide6.QtCore.Signal]
    collectionCreated: ClassVar[PySide6.QtCore.Signal]
    collectionsDeleted: ClassVar[PySide6.QtCore.Signal]
    contextMenuAboutToOpen: ClassVar[PySide6.QtCore.Signal]
    def __init__(self, prim_search_paths: Sequence[str] | None = ('/',), collection_search_paths: Sequence[str | None] | None = ..., prim_types: Sequence[type[Usd.SchemaBase]] = ..., enable_create_collections: bool = True, parent: PySide6.QtWidgets.QWidget | None = None, collection_prim_path: str = ..., attr_names: Sequence[str] = ..., prefs: husdui.prefs.Prefs | None = None, enable_show_inactive: bool = True, traversal_demands: int = ...) -> None:
        """
            :param enable_create_collections: Enables adding/creating collections
            :param prim_search_paths: list of paths to search for prims under.
            :param collection_search_paths: list of prim paths to search for collections in.
            :param prim_types: list of prim types to show in the view.
            :param parent: The widget's parent
            :param collection_prim_path: Path to the default prim where collections will be authored.
            :param prefs: module/attribute prefereces in a husdui.prefs.Prefs object.
            :param enable_show_inactive: Enables showing inactive prims.
        """
    def setObjectName(self, name: str) -> None: ...
    def setCollectionsPrimPath(self, path: str) -> None: ...
    def setTitle(self, title: str) -> None: ...
    def title(self) -> str: ...
    def setAlternatingRowColors(self, value: bool) -> None: ...
    def alternatingRowColors(self, value: bool) -> bool: ...
    def clear(self) -> None: ...
    def setFollowNetworkSelection(self, follow: bool) -> None:
        """
        Whether the widget subscribes to the lopnet selection automatically.
        Off by default; the owner applies the selection as it sees fit.
        """
    def followNetworkSelection(self) -> bool: ...
    def setIgnoreSelectionChanged(self, ignore: bool) -> None: ...
    def ignoreSelectionChanged(self) -> bool: ...
    def primTypes(self) -> Sequence[type[Usd.SchemaBase]]: ...
    def toolBarPrependWidget(self, widget: PySide6.QtWidgets.QWidget) -> PySide6.QtGui.QAction:
        """
        Prepend a widget to the last spot a widget was prepended.
        Do not try to access the toolbar directly.
        """
    def toolBarPrependAction(self, action: PySide6.QtGui.QAction) -> None:
        """
        Prepend an action to the last spot a widget was prepended.
        Do not try to access the toolbar directly.
        """
    def toolBarAddWidget(self, widget: PySide6.QtWidgets.QWidget) -> PySide6.QtGui.QAction:
        """
        Append a widget to the toolbar.
        Do not try to access the toolbar directly.
        """
    def toolBarAddAction(self, action: PySide6.QtGui.QAction) -> None:
        """
        Append an action to the toolbar.
        Do not try to access the toolbar directly.
        """
    def keyPressEvent(self, event: PySide6.QtGui.QKeyEvent) -> None: ...
    def sourceNode(self) -> hou.LopNode | None: ...
    def sourceNetwork(self) -> hou.Node | None: ...
    def setSourceNode(self, node: hou.Node | None) -> None: ...
    def reset(self) -> None: ...
    def updateFromSource(self) -> None: ...
    def initialExpand(self) -> None: ...
    def expandToDepth(self, depth: int) -> None: ...
    def highlightItemsByFullPath(self, items: Iterable[str | Sdf.Path], top_level_only: bool = True, parent: PySide6.QtCore.QModelIndex = ..., auto_expand: bool = False, interruptible_op: hou.InterruptableOperation | None = None) -> None: ...
    def selectItemsByFullPath(self, items: Iterable[str | Sdf.Path], top_level_only: bool = True, parent: PySide6.QtCore.QModelIndex = ..., auto_expand: bool = False, interruptible_op: hou.InterruptableOperation | None = None) -> None: ...
    def getSelected(self, column: int = -1) -> list[PySide6.QtCore.QModelIndex]: ...
    def getSelectedPaths(self) -> list[str]: ...
    def activate(self) -> None: ...
    def deactivate(self) -> None: ...
    def processHotkey(self, hotkey_symbol: str, str_data: str) -> bool:
        """
        Processes a hotkey for a given index.
        Returns True if this routine has accepted the hotkey, not that
        processing the hotkey was necessarily successful.
        Returns False if the hotkey should be processed by another function.
        """
