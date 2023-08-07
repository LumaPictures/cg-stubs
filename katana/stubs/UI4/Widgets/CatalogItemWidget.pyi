# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
from UI4.Widgets.CatalogChannelsWidget import CatalogChannelsWidget as CatalogChannelsWidget
from UI4.Widgets.CatalogFrameRangeWidget import CatalogFrameRangeWidget as CatalogFrameRangeWidget
from UI4.Widgets.CatalogLockWidget import CatalogLockWidget as CatalogLockWidget
from UI4.Widgets.CatalogNameWidget import CatalogNameWidget as CatalogNameWidget
from UI4.Widgets.CatalogProgressWidget import CatalogProgressWidget as CatalogProgressWidget
from UI4.Widgets.CatalogResolutionWidget import CatalogResolutionWidget as CatalogResolutionWidget
from UI4.Widgets.CatalogStopWidget import CatalogStopWidget as CatalogStopWidget
from UI4.Widgets.CatalogThumbnailWidget import CatalogThumbnailWidget as CatalogThumbnailWidget
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class CatalogItemWidget(PyQt5.QtWidgets.QWidget):
    catalogItemDropped: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def _CatalogItemWidget__catalogItemDropped_CB(self, item): ...
    def getLockLayout(self) -> PyQt5.QtWidgets.QHBoxLayout: ...
    def getNameLayout(self) -> PyQt5.QtWidgets.QHBoxLayout: ...
    def setCatalogItem(self, item): ...
