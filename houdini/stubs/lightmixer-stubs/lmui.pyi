import hou
import husdui.models
import husdui.prefs
import husdui.views
import husdui.widgets
from . import lmmixer as lmmixer
from collections.abc import Iterable, Sequence
from hutil.PySide import QtCore, QtGui, QtWidgets
from pxr import Sdf, Usd as Usd
from typing import TypeAlias

from typing import TypeAlias
TransformableProxy: TypeAlias = husdui.models.ValidProxy
theToolMenuXmlFilename: str
theAddLightMenuXmlFilename: str
theSheetViewMenuXmlFilename: str
theConfigFilename: str
HOTKEY_LIGHTMIXER_SHOW_EDITOR_NODE: str
HOTKEY_ADD_TO_MIXER: str
PANEL_ICON: hou.qt.Icon
SLIDERS_ICON: hou.qt.Icon
SHEET_ICON: hou.qt.Icon
XFORM_ICON: hou.qt.Icon

class MixableProxy(husdui.models.ItemModelProxyBase):
    def filterAcceptsRow(self, row: int, parent_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool: ...
    def dropMimeData(self, mimedata: QtCore.QMimeData, action: QtCore.Qt.DropAction, row: int, column: int, parent_index: QtCore.QModelIndex | QtCore.QPersistentModelIndex) -> bool: ...

class EditTreeOverlay(husdui.views.IndicatorOverlay):
    def __init__(self, parent: QtWidgets.QAbstractItemView) -> None: ...
    def setModel(self, model: husdui.models.ItemModelProxyBase) -> None: ...
    def model(self) -> husdui.models.ItemModelProxyBase: ...
    def eventFilter(self, source: QtCore.QObject, event: QtCore.QEvent) -> bool: ...
    def parentDragEnterEvent(self, source: QtCore.QObject, event: QtGui.QDragEnterEvent) -> bool: ...
    def parentDragMoveEvent(self, source: QtCore.QObject, event: QtGui.QDragMoveEvent) -> bool: ...
    def parentDragLeaveEvent(self, source: QtCore.QObject, event: QtGui.QDragLeaveEvent) -> bool: ...
    def parentDropEvent(self, source: QtCore.QObject, event: QtGui.QDropEvent) -> None: ...

class LightTreeWidget(husdui.widgets.PrimTreeWidget):
    """
    This widget is used to show a light source tree.
    """
    def __init__(self, prim_search_paths: Sequence[str] = ..., collection_search_paths: Sequence[str] = ..., enable_create_collections: bool = True, parent: QtWidgets.QWidget | None = None, attr_names: Sequence[str] = ['$solo', '$mute', '$active'], prefs: husdui.prefs.Prefs | None = None) -> None:
        """
            :param enable_create_collections: Enables adding/creating collections
            :param prim_search_paths: list of paths to search for collections under.
            :param collection_search_paths: list of prim paths to search for collections in.
            :param parent: The widget's parent
            :param prefs: module/attribute prefereces in a husdui.prefs.Prefs object.
        """

class LightMixer(QtWidgets.QWidget):
    NodeEventTypes: tuple[hou.EnumValue[hou.nodeEventType], ...]
    NetworkEventTypes: tuple[hou.EnumValue[hou.nodeEventType], ...]
    NothingDirty: int
    LayoutDirty: int
    ValuesDirty: int
    StructureDirty: int
    NeedsReset: int
    def __init__(self, pane: hou.PathBasedPaneTab | None = None, parent: QtWidgets.QWidget | None = None) -> None: ...
    def __del__(self) -> None: ...
    def showSourceView(self, show: bool | None = None) -> None: ...
    def showParmView(self, show: bool | None = None) -> None: ...
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: ...
    def orientation(self) -> QtCore.Qt.Orientation: ...
    def setOrientation(self, orientation: QtCore.Qt.Orientation) -> None: ...
    def sourceNode(self) -> hou.LopNode | None: ...
    def sourceNetwork(self) -> hou.Node | None: ...
    def setSourceNetwork(self, network: hou.Node | None) -> None: ...
    def suggestSourceNode(self, new_network: hou.Node, new_node: hou.Node | None) -> None:
        """
        This is called when the pane's current node changes. It checks if the
        node is suitable to be displayed in the UI, and if so, calls
        setSourceNode() with it.
        """
    def setSourceNode(self, node: hou.Node | None) -> None: ...
    def reset(self) -> None: ...
    def clear(self) -> None: ...
    def showParmViewForNode(self, node: hou.LopNode, show: bool | None = True, select_prims: bool = True) -> None:
        """
        Set the parmview pane to a spcific node and show it.  The primpath will be blank.
        """
    def setParmViewPaths(self, item_paths: Iterable[str | Sdf.Path]) -> None:
        """
        Set the parmview pane to the last editor of the last item in a list of prims.
        """
    def activate(self, pane_tab: hou.PaneTab | None) -> None: ...
    def deactivate(self) -> None: ...
    def processHotkey(self, hotkey_symbol: str, str_data: str) -> bool | None:
        """
        Processes a hotkey for a given index.
        Returns True if this routine has accepted the hotkey, not that
        processing the hotkey was necessarily successful.
        Returns False if the hotkey should be processed by another function.
        """
