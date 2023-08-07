# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI as CatalogAPI
import PyFnAttribute as FnAttribute
import UI4.Widgets.MonitorLayer.Utils as MonitorLayerUtils
import PyOpenColorIO as OCIO
import PyFnAttribute
import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import PyUtilModule.RenderManager as RenderManager
import UI4 as UI4
import Utils as Utils
import QT4Widgets.WidgetUtils as WidgetUtils
import typing
from Callbacks.Callbacks import Callbacks as Callbacks
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

MONITOR_LAYER_DEFAULT: bool

class AOVSelector(PyQt5.QtCore.QObject):
    aovsChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    currentAOVChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    currentAOVIndexChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    selectedAOVChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    useSelectedAOVChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    aovs: Incomplete
    selectedAOV: Incomplete
    useSelectedAOV: Incomplete
    def __init__(self) -> None: ...
    def _AOVSelector__shiftSelectedAOV(self, shift): ...
    def _AOVSelector__updateCurrentAOV(self): ...
    def selectNextAOV(self): ...
    def selectPreviousAOV(self): ...
    @property
    def currentAOV(self): ...
    @property
    def currentAOVIndex(self): ...
    @property
    def selectedAOVIndex(self): ...

class MonitorLayerDropdownButton(PyQt5.QtWidgets.QPushButton):
    def __init__(self, text, toolTip, defaultPixmapPath, activePixmapPath, height, parent: Incomplete | None = ...) -> None: ...
    def _MonitorLayerDropdownButton__sizeHint(self, size): ...
    def enterEvent(self, ev): ...
    def leaveEvent(self, ev): ...
    def minimumSizeHint(self): ...
    def paintEvent(self, ev): ...
    def sizeHint(self): ...

class ToggleButton(_ToggleButton):
    MONITOR_LAYER_PIXMAPS: ClassVar[tuple] = ...
    def __init__(self, parent, size) -> None: ...

class ToolBar(PyQt5.QtWidgets.QFrame):
    class AovToolControl(tuple):
        _field_defaults: ClassVar[dict] = ...
        _fields: ClassVar[tuple] = ...
        _fields_defaults: ClassVar[dict] = ...
        def __init__(self, _cls, button, menu) -> None: ...
        def _asdict(self): ...
        @classmethod
        def _make(cls, iterable): ...
        def _replace(self, _self, **kwds): ...
        def __getnewargs__(self): ...
        @property
        def button(self): ...
        @property
        def menu(self): ...

    class ViewTransformControl(tuple):
        _field_defaults: ClassVar[dict] = ...
        _fields: ClassVar[tuple] = ...
        _fields_defaults: ClassVar[dict] = ...
        def __init__(self, _cls, toggle, button, menu) -> None: ...
        def _asdict(self): ...
        @classmethod
        def _make(cls, iterable): ...
        def _replace(self, _self, **kwds): ...
        def __getnewargs__(self): ...
        @property
        def button(self): ...
        @property
        def menu(self): ...
        @property
        def toggle(self): ...
    AOV_TOOLTIP_TEMPLATE: ClassVar[str] = ...
    COPY_TO_CEL_PIXMAPS: ClassVar[tuple] = ...
    DOWN_ARROW_PIXMAPS: ClassVar[tuple] = ...
    ID_BUFFER_PIXMAPS: ClassVar[tuple] = ...
    MAX_TEXT_LENGTH: ClassVar[int] = ...
    NO_AOVS_TEXT: ClassVar[str] = ...
    NO_AOVS_TOOLTIP: ClassVar[str] = ...
    ROI_PIXMAPS: ClassVar[tuple] = ...
    ROI_RESET_HANDLE_PIXMAPS: ClassVar[tuple] = ...
    ROI_SHOW_HANDLE_PIXMAPS: ClassVar[tuple] = ...
    SELECT_AND_EXPAND_PIXMAPS: ClassVar[tuple] = ...
    SWITCH_VIEW_PIXMAPS: ClassVar[tuple] = ...
    def __init__(self, tab, buttonSize) -> None: ...
    def _ToolBar__buildIdBufferToolTip(self) -> str: ...
    def _ToolBar__createAOVToolControl(self, buttonSize): ...
    def _ToolBar__createIdBufferToggle(self, buttonSize): ...
    def _ToolBar__createROIWidgets(self, buttonSize: int): ...
    def _ToolBar__createSwitchViewMenu(self): ...
    def _ToolBar__createToggle(self, name, defaultPixmap, activePixmap, buttonSize): ...
    def _ToolBar__createViewTransformControl(self, buttonSize): ...
    def _ToolBar__onAOVMenuOpened(self, checked): ...
    def _ToolBar__onAOVSelected(self, action): ...
    def _ToolBar__onAOVsChanged(self): ...
    def _ToolBar__onCurrentAOVChanged(self): ...
    def _ToolBar__onCurrentAOVIndexChanged(self): ...
    def _ToolBar__onIdBufferToggled(self, checked): ...
    def _ToolBar__onSelectedAOVChanged(self): ...
    def _ToolBar__onUseSelectedAOVChanged(self): ...
    def _ToolBar__onViewMenuOpened(self, checked): ...
    def _ToolBar__onViewSelected(self, action): ...
    def _ToolBar__onViewToggled(self, checked): ...
    def _ToolBar__on_catalog_clientSlotUpdate(self, eventType, eventID): ...
    def _ToolBar__on_catalog_externalBufferLoaded(self, eventType, eventID, item, **kwargs): ...
    def _ToolBar__on_catalog_itemDelete(self, eventType, eventID, item): ...
    def _ToolBar__on_catalog_itemPropertyUpdate(self, args): ...
    def _ToolBar__on_catalog_rebuild(self, eventType, eventID): ...
    def _ToolBar__on_pref_changed(self, eventType: str | None, eventID: typing.Hashable, prefKey: str, prefValue: object): ...
    def _ToolBar__on_renderManager_roiChanged(self, eventType, eventID): ...
    def _ToolBar__on_roiMenu_aboutToShow(self): ...
    def _ToolBar__on_roiShowHandleAction_triggered(self, checked: bool): ...
    def _ToolBar__populateAOVMenuActions(self, menu): ...
    def _ToolBar__populateAOVToolTipWithShortcuts(self): ...
    def _ToolBar__setMonitorAOVLayerIndex(self, index): ...
    @staticmethod
    def _ToolBar__setStyleSheetProperty(widget, propertyName, propertyValue): ...
    def _ToolBar__updateAOVButton(self): ...
    def _ToolBar__updateAOVsFromCatalog(self): ...
    def allowIDBuffer(self, allow): ...
    def defaultAOV(self): ...
    def getCurrentAOV(self): ...
    def isIDBufferEnabled(self) -> bool: ...
    def nextAOV(self): ...
    def onResetROICallback(self, attr: PyFnAttribute.Attribute): ...
    def onSetROICallback(self, attr: PyFnAttribute.GroupAttribute): ...
    def previousAOV(self): ...
    def setIDBufferEnabled(self, enabled: bool): ...
    def toggleSelectedAOV(self): ...
    def toggleViewTransform(self): ...
    def updateROI(self, enabled: Incomplete | None = ...): ...
    @property
    def _ToolBar__viewerDelegate(self): ...

class _ToggleButton(ToolbarButton):
    stateChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, toolTip, parent, buttonSize, normalPixmap, onPixmap, rolloverPixmap: Incomplete | None = ..., onRolloverPixmap: Incomplete | None = ..., defaultValue: bool = ...) -> None: ...
    def _ToggleButton__clicked(self): ...
