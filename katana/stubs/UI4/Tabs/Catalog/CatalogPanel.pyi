# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import CatalogAPI as CatalogAPI
import UI4.Tabs.Catalog.ImageImportDialog as ImageImportDialog
import UI4.KatanaPrefs as KatanaPrefs
import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import Utils as Utils
import typing
from PyUtilModule.VirtualKatana import RenderManager as RenderManager
from UI4.Tabs.BaseTab import BaseTab as BaseTab
from UI4.Tabs.Catalog.CatalogWidget import CatalogWidget as CatalogWidget
from typing import ClassVar, Set, Tuple

class CatalogPanel(BaseTab):
    MODE_SLOT_VIEW: ClassVar[int] = ...
    MODE_TIME_VIEW: ClassVar[int] = ...
    tabPressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, *args) -> None: ...
    def _CatalogPanel__catalog_memoryUsageChanged_CB(self, eventType, eventID, **kwargs): ...
    def _CatalogPanel__doImportSequence(self): ...
    def _CatalogPanel__editMenu_aboutToShow(self): ...
    def _CatalogPanel__exportCatalogMenu_aboutToShow(self): ...
    def _CatalogPanel__lock2dCheckbox_stateChanged_CB(self, state): ...
    def _CatalogPanel__modeCapsule_valueChanged_CB(self, enabledItems, oldEnabledItems): ...
    def _CatalogPanel__populateMenuBar(self): ...
    def _CatalogPanel__renderManager_buffer2DAutoLockUpdate_CB(self, *args, **kwargs): ...
    def _CatalogPanel__saveAndPublishCatalogItem(self, catalogItems, filePathOrAssetId, extraOptions: dict = ...): ...
    def applySettings(self, settings: dict): ...
    def deleteCatalog(self, mode): ...
    def event(self, event): ...
    def exportCatalog(self, mode): ...
    def getCatalogWidget(self) -> CatalogWidget: ...
    def getMenuBar(self) -> PyQt5.QtWidgets.QMenuBar | None: ...
    def getMode(self): ...
    def getSettings(self) -> dict: ...
    def setMode(self, mode): ...

class _SyncToProjectSettingsCheckbox(PyQt5.QtWidgets.QCheckBox):
    def __init__(self, parent) -> None: ...
    def _SyncToProjectSettingsCheckbox__onPrefChanged(self, eventType: str | None, eventID: typing.Hashable, prefKey: str, prefValue: object): ...
    def _SyncToProjectSettingsCheckbox__onStateChanged(self, state): ...
