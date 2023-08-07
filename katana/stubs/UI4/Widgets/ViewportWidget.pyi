# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import KatanaResources as KatanaResources
import NodegraphAPI as NodegraphAPI
import PyFnAttribute
import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import UI4.Tabs
import Utils as Utils
import ViewerAPI
import typing
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ViewportWidget(PyQt5.QtWidgets.QOpenGLWidget):
    eventTranslators: ClassVar[dict] = ...
    singleGLContextInitialized: ClassVar[bool] = ...
    def __init__(self, parent: PyQt5.QtWidgets.QWidget | None, viewport: ViewerAPI.Viewport, name: str, postInitCallback: typing.Optional[typing.Callable] = ...) -> None: ...
    def _ViewportWidget__getLocationFromDragOrDropEvent(self, event: PyQt5.QtCore.QDragEvent | PyQt5.QtCore.QDropEvent) -> str | None: ...
    def _ViewportWidget__startDrag(self, event): ...
    def addCamera(self, cameraType: str, name: str, settings: Incomplete | None = ...) -> ViewportCamera: ...
    def addLayer(self, layerType: str, name: str) -> ViewportLayer: ...
    def dragEnterEvent(self, event): ...
    def dropEvent(self, event): ...
    def event(self, event): ...
    def findBaseViewerTab(self) -> UI4.Tabs.BaseViewerTab | None: ...
    def getActiveCamera(self) -> ViewportCamera | None: ...
    def getCameraByIndex(self, index: int) -> ViewportCamera | None: ...
    def getCameraByName(self, name: str) -> ViewportCamera | None: ...
    def getCameraName(self, index: int) -> str | None: ...
    def getLayer(self, name: str) -> ViewportLayer | None: ...
    def getLayerByIndex(self, index: int) -> ViewportLayer | None: ...
    def getLayerName(self, index: int) -> str | None: ...
    def getName(self): ...
    def getNumberOfCameras(self) -> int: ...
    def getNumberOfLayers(self) -> int: ...
    def getOption(self, optionId: int) -> PyFnAttribute.Attribute | None: ...
    def getOptionByName(self, name: str) -> PyFnAttribute.Attribute | None: ...
    def getViewerDelegate(self) -> ViewerAPI.ViewerDelegate: ...
    def getViewport(self) -> ViewerAPI.Viewport: ...
    def initializeGL(self): ...
    def insertLayer(self, layerType: str, name: str, index: int) -> ViewportLayer: ...
    def isDirty(self): ...
    def leaveEvent(self, event): ...
    def mouseMoveEvent(self, event): ...
    def paintEngine(self): ...
    def paintGL(self): ...
    def removeCamera(self, name: str): ...
    def removeCameraByIndex(self, index: int): ...
    def removeLayer(self, name: str): ...
    def removeLayerByIndex(self, index: int): ...
    def resizeGL(self, width, height): ...
    def setActiveCamera(self, camera: ViewportCamera): ...
    def setDirty(self, dirty: bool): ...
    def setOption(self, optionId: int, attr: PyFnAttribute.Attribute): ...
    def setOptionByName(self, name: str, attr: PyFnAttribute.Attribute): ...
    def setStartDragCallback(self, callback: typing.Callable): ...
    def setUnhandledEventCallback(self, callback: typing.Callable): ...
    def setViewport(self, viewport: ViewerAPI.Viewport | None): ...
    def updateBuiltInCamerasFromProjectSettings(self): ...
    def updateCameraFromProjectSettings(self, cameraName: str, isOrthographic: bool = ...): ...
    def writeToFile(self, filepath: str): ...
