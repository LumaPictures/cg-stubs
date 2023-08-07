# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CacheManager as CacheManager
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import KatanaResources as KatanaResources
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import PyFnAttribute
import PyFnGeolib
import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4.Widgets.ViewportWidget
import UI4.Widgets.ViewportWidget
import UI4.Util as Util
import Utils as Utils
import ViewerAPI as ViewerAPI
import _weakrefset
import typing
from Callbacks.Callbacks import Callbacks as Callbacks
from Nodes3DAPI.PortOpClient import PortOpClient
from PyUtilModule.VirtualKatana import FaceSelectionManager as FaceSelectionManager, LiveRenderAPI as LiveRenderAPI, RenderGlobals as RenderGlobals, RenderManager as RenderManager, ScenegraphManager as ScenegraphManager, WorkingSetManager as WorkingSetManager
from PyUtilModule.WorkingSet import WorkingSet as WorkingSet
from PyUtilModule.WorkingSetManager import WSM as WSM
from UI4.Tabs.BaseTab import BaseTab as BaseTab
from UI4.Widgets.ViewportWidget import ViewportWidget as ViewportWidget
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class BaseViewerTab(BaseTab):
    ManipulationFreezePeriod: ClassVar[int] = ...
    UpdateTimer: ClassVar[None] = ...
    UpdateTimerInterval: ClassVar[float] = ...
    _BaseViewerTab__instances: ClassVar[_weakrefset.WeakSet] = ...
    viewOpChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent: PyQt5.QtWidgets.QWidget | None, flags: int = ...) -> None: ...
    def _BaseViewerTab__activeManipulatorsChangedCallback(self, attrs): ...
    def _BaseViewerTab__cleanup(self): ...
    def _BaseViewerTab__configureWorkingSets(self, viewerDelegate): ...
    def _BaseViewerTab__getSelectedLocationsCallback(self, emptyMessage): ...
    def _BaseViewerTab__getViewerDelegates(self, onlyFollowingViewNode: bool = ...): ...
    def _BaseViewerTab__getViewerProxyLoaderOp(self, proxyAttr: PyFnAttribute.GroupAttribute) -> PyFnAttribute.GroupAttribute: ...
    def _BaseViewerTab__onExpansionStateChanged(self, locationStateChanges: list[tuple], workingSet: WorkingSet, sender: object): ...
    def _BaseViewerTab__onPinnedStateChanged(self, locationStateChanges: list[tuple], workingSet: WorkingSet, sender: object): ...
    def _BaseViewerTab__onTabCreated(self, objectHash: int | None, tab: PyQt5.QtWidgets.QWidget): ...
    def _BaseViewerTab__onVisibilityStateChanged(self, _locationStateChanges, _workingSet, _sender): ...
    @staticmethod
    def _BaseViewerTab__on_destroyed(tab): ...
    def _BaseViewerTab__registerDestructionCallback(self): ...
    def _BaseViewerTab__selectFacesCallback(self, selectionAttr: PyFnAttribute.GroupAttribute): ...
    def _BaseViewerTab__selectLocationsCallback(self, locationsAttr): ...
    def _BaseViewerTab__setCursorPosition(self, groupAttr: PyFnAttribute.GroupAttribute, viewerDelegate: ViewerAPI.ViewerDelegate): ...
    def _BaseViewerTab__setCursorVisibility(self, visibleAttr: PyFnAttribute.IntAttribute): ...
    def _BaseViewerTab__setUpdateTimerConnectionEnabled(self, enabled: bool): ...
    def _BaseViewerTab__updateFromProjectSettings(self): ...
    def _applyViewerPluginExtensionTerminalOps(self, txn: PyFnGeolib.GeolibRuntimeTransaction, op: PyFnGeolib.GeolibRuntimeOp | None, viewerDelegate: ViewerAPI.ViewerDelegate) -> PyFnGeolib.GeolibRuntimeOp: ...
    @staticmethod
    def _checkGLVersion(requiredMajorVersion: int, requiredMinorVersion: int): ...
    def _cleanup(self): ...
    def _onUpdateEvent(self): ...
    def _on_cacheManager_flush(self, _eventType: str | None, _eventID: object, isNodeGraphLoading: bool = ...): ...
    def _on_implicitResolversToggled(self, eventType: str | None, eventID: object, implicitResolversActive: bool): ...
    def _on_lookThroughLocation_changeRequested(self, viewportName: str, location: str): ...
    def _on_lookThroughLocation_changed(self, viewportName: str, location: str, attrs: PyFnAttribute.GroupAttribute): ...
    def _on_lookThroughLocation_cooked(self, viewportName: str, location: str, attrs: PyFnAttribute.GroupAttribute): ...
    def _on_lookThroughLocation_doesNotExist(self, viewportName: str, location: str): ...
    def _on_node_setLocked(self, eventType: str | None, eventID: object, node: NodegraphAPI.Node, locked: bool): ...
    def _on_nodegraph_setCurrentTime(self, _eventType: str | None, _eventID: object, currentTime: float): ...
    def _on_nodegraph_setRootNode(self): ...
    def _on_parameter_setValue(self, args: seq): ...
    def _on_scenegraphManager_selectionChanged(self, eventType: str | None, eventID: object, selectedLocations, deselectedLocations, sender: object | None): ...
    def _on_selectedEnabledLocations_changed(self, delegate: ViewerAPI.ViewerDelegate): ...
    def _on_selectedLocations_cooked(self, delegate: ViewerAPI.ViewerDelegate): ...
    def _on_viewer_liveRenderFromViewerCameraChanged(self, eventType: str, eventID: object, followViewportCamera: bool, viewportWidget: ViewportWidget): ...
    def _on_viewer_visibilityFollowsWorkingSetChanged(self, _eventType: str | None, _eventID: object, visibilityFollowsWorkingSet: bool): ...
    def _on_viewportView_frozenStateChanged(self, viewportName: str, isViewFrozen: bool): ...
    def _resolveViewportWidget(self, viewport: Tuple[int, str, ViewportWidget | ViewerAPI.Viewport], viewerDelegate: ViewerAPI.ViewerDelegate) -> ViewportWidget: ...
    def _unregisterWorkingSetCallbacks(self): ...
    def _updateHook(self): ...
    def aboutToQuit(self): ...
    def activeManipulatorsChanged(self, viewportName: str, manipulatorName: str): ...
    def addViewerDelegate(self, delegateType: str, followsViewNode: bool = ...) -> ViewerAPI.ViewerDelegate: ...
    def addViewport(self, viewportType: str, viewportName: str, viewerDelegate: ViewerAPI.ViewerDelegate, postInitCallback: typing.Optional[typing.Callable] = ..., layers: Incomplete | None = ...) -> UI4.Widgets.ViewportWidget: ...
    def applyTerminalOps(self, txn: PyFnGeolib.GeolibRuntimeTransaction, op: PyFnGeolib.GeolibRuntimeOp | None, viewerDelegate: ViewerAPI.ViewerDelegate) -> PyFnGeolib.GeolibRuntimeOp: ...
    def closeEvent(self, event: PyQt5.QtGui.QCloseEvent): ...
    def filterManipulator(self, manipulatorName: str, selectedLocations: list, viewerDelegate: ViewerDelegate) -> bool: ...
    def flushCaches(self): ...
    @classmethod
    def flushInstanceCaches(cls): ...
    def freeze(self): ...
    def getNumberOfViewerDelegates(self) -> int: ...
    def getSelectedLocations(self) -> list[str]: ...
    def getViewOp(self, viewerDelegate): ...
    def getViewerDelegateByIndex(self, index: int) -> ViewerDelegate: ...
    def getViewportWidget(self, viewport: Tuple[int, str | ViewerAPI.Viewport], viewerDelegate: ViewerAPI.ViewerDelegate) -> UI4.Widgets.ViewportWidget.ViewportWidget | None: ...
    def getViewportWidgetByIndex(self, viewportIndex: int, viewerDelegate: ViewerAPI.ViewerDelegate) -> UI4.Widgets.ViewportWidget.ViewportWidget | None: ...
    def getViewportWidgetByName(self, viewportName: str, viewerDelegate: ViewerAPI.ViewerDelegate) -> UI4.Widgets.ViewportWidget.ViewportWidget | None: ...
    def getViewports(self, viewerDelegate: ViewerAPI.ViewerDelegate) -> typing.Iterator[Viewport]: ...
    def hideEvent(self, event: PyQt5.QtGui.QHideEvent): ...
    def installManipulatorFilter(self, filter_): ...
    def isViewerDelegateFollowingViewNode(self, index: int) -> bool: ...
    def loadViewerPluginExtensions(self): ...
    def removeManipulatorFilter(self, filter_: object): ...
    def removeViewport(self, viewportName, viewerDelegate: ViewerAPI.ViewerDelegate): ...
    def removeViewportByIndex(self, viewportIndex: int, viewerDelegate: ViewerAPI.ViewerDelegate): ...
    def setActiveLiveRenderCamera(self, useSameAsViewer: bool, path: str = ..., viewportCamera: Incomplete | None = ...): ...
    def setCamera(self, viewport: Tuple[int, str, ViewportWidget | ViewerAPI.Viewport], nameOrPath: str): ...
    def setDelegateViewOp(self, txn: PyFnGeolib.GeolibRuntimeTransaction, op: PyFnGeolib.GeolibRuntimeOp | None, viewerDelegate: ViewerAPI.ViewerDelegate) -> PyFnGeolib.GeolibRuntimeOp: ...
    def setEventHandlersEnabled(self, enabled: bool, isFreezeOrThaw: bool = ...): ...
    @classmethod
    def setUpdateTimerInterval(cls, interval: float): ...
    def setViewedNode(self, viewedNode: NodegraphAPI.Node | None, viewerDelegate: ViewerAPI.ViewerDelegate) -> PyFnGeolib.GeolibRuntimeOp: ...
    def setViewportWidgetUpdatesEnabled(self, viewportWidget: ViewportWidget, enabled: bool): ...
    def showEvent(self, event: PyQt5.QtGui.QShowEvent): ...
    def thaw(self): ...
    def updateLiveRenderCamera(self, location, camera): ...

class _ViewerDelegatePortOpClient(PortOpClient):
    _abc_impl: ClassVar[_abc_data] = ...
    __abstractmethods__: ClassVar[frozenset] = ...
    def __init__(self, viewerDelegate, port: NodegraphAPI.Port, updateOpCallback: typing.Callable) -> None: ...
    def modifyPostTraversalGraphState(self, graphState: NodegraphAPI.GraphState): ...
    def opChanged(self, op, graphState: NodegraphAPI.GraphState, txn): ...
    @property
    def op(self): ...
    @property
    def systemArgs(self): ...

def _FlushBaseViewerTabCaches(): ...
