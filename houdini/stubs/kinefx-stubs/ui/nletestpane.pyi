import _houqt
import hou
from collections.abc import Sequence
from houtypes import NodeEventKwargs
from hutil.PySide import QtCore, QtGui, QtWidgets
from kinefx.ui.mixerutils import houdiniMotionMixerSourcesMimeType as houdiniMotionMixerSourcesMimeType
from kinefx.ui.nleshotsculptpane import _HipFileEventKwargs
from typing import TypedDict, Unpack

class _DraggedSource(TypedDict):
    name: str

class NleTestSourcesTreeView(QtWidgets.QTreeView):
    """ QTreeView with drag and drop for the Sources QTreeView"""
    dropIndicatorRect: QtCore.QRectF
    dropIndicatorPosition: QtWidgets.QAbstractItemView.DropIndicatorPosition
    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None: ...
    def selectedDraggableIndexes(self) -> list[QtCore.QModelIndex]: ...
    def selectedSources(self, indexes: Sequence[QtCore.QModelIndex] | None = None) -> list[_DraggedSource]: ...
    def startDrag(self, supportedActions: QtCore.Qt.DropAction) -> None:
        """Ported C++ code from QAbstractItemView::startDrag, removing the
        pixmap"""

class NleTestPane(QtWidgets.QWidget):
    """ The main QWidget for the Houdini Python Panel. The file is split into
        multiple files because the class was getting too large."""
    myPaneTab: hou.PythonPanel
    myClipIcon: hou.qt.Icon
    myNodes: list[hou.OpNode]
    myDelayedRebuildNodes: Sequence[hou.Node]
    myDelayedChanges: list[tuple[str, None]]
    myMenuWidget: None
    myTimeline: _houqt.NLE_Timeline
    myTimelineView: _houqt.NLE_QtMotionMixer
    mySourcesTreeView: NleTestSourcesTreeView
    myMainSplitter: QtWidgets.QSplitter
    myModelItems: list[QtGui.QStandardItem]
    myModel: QtGui.QStandardItemModel | None
    @classmethod
    def onCreateInterface(cls, pt: hou.PythonPanel) -> NleTestPane:
        """ Entry point to create the widget and link it to a panel."""
    def __del__(self) -> None:
        """ NleTestPane.__del__ removes the registered callbacks"""
    myLastDelayedTime: float
    myFirstResize: bool
    def __init__(self, pt: hou.PythonPanel) -> None:
        """ NleTestPane.doinit"""
    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None: ...
    def onNleEvent(self, e: _houqt.NLE_Event) -> None:
        """ All NLE events callback."""
    def refreshScene(self) -> None: ...
    def evalSourcesFromStashParm(self, node_path: str) -> list[str]: ...
    def rebuildScene(self, nodes: Sequence[hou.Node] | None) -> None: ...
    def addEventCallback(self, node: hou.OpNode, event_types: Sequence[hou.EnumValue[hou.nodeEventType]], cb: hou._NodeEventCallback) -> None: ...
    def removeEventCallback(self, node: hou.OpNode, event_types: Sequence[hou.EnumValue[hou.nodeEventType]], cb: hou._NodeEventCallback) -> None: ...
    def onInputDataChanged(self, **kwargs: Unpack[NodeEventKwargs]) -> None:
        """ called when the input geometry changes. """
    def onParmTupleChanged(self, **kwargs: Unpack[NodeEventKwargs]) -> None:
        """ called when the node parameters changes. """
    def onParmTupleAnimated(self, **kwargs: Unpack[NodeEventKwargs]) -> None:
        """ called when the node parameters changes. """
    def onSpareParmChanged(self, **kwargs: Unpack[NodeEventKwargs]) -> None:
        """ called when the node spare parameters changes. """
    def onNodePathChanged(self, node: hou.Node | None = None) -> None:
        """ called when current node path changes."""
    def onParmTupleChannelChanged(self, **kwargs: Unpack[NodeEventKwargs]) -> None:
        """ called when the node parameters changes. """
    def delayedRefreshScene(self) -> None: ...
    def postDelayChange(self, change: tuple[str, None]) -> None:
        """ Post a DelayChange event if needed
            @change is a 2 elements tuple, with the first
            element as a type and the second as the data."""
    def onDelayedChanged(self) -> None:
        """ handle the delayed changed events in batch"""
    def onDestroyInterface(self) -> None: ...
    def onActivateInterface(self) -> None: ...
    def onDeactivateInterface(self) -> None: ...
    def onHipFileEvent(self, **kwargs: Unpack[_HipFileEventKwargs]) -> None:
        """ Single event callback for the load,clear,merge,save events"""
    def resizeEventInit(self) -> None: ...
    def resizeEvent(self, e: QtGui.QResizeEvent) -> None:
        """ resize event for the whole panel."""
