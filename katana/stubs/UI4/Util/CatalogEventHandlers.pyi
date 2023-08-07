# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CatalogAPI as CatalogAPI
import UI4.Util.CatalogEventReceiver as CatalogEventReceiver
import Nodes2DAPI as Nodes2DAPI
import PyQt5.QtCore
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import PyUtilModule.RenderManager as RenderManager
import UI4.Util.TextureManager as TextureManager
import Utils as Utils
from UI4.Util.CatalogEventReceiver import _CatalogEventReceiver as _CatalogEventReceiver
from typing import Set, Tuple

class RegenerateThumbnailThread(PyQt5.QtCore.QThread):
    def __init__(self) -> None: ...
    @staticmethod
    def _RegenerateThumbnailThread__nodeGraph_loadBegin_CB(*_args, **_kwargs): ...
    def run(self): ...
    def stopThread(self): ...

def EnableCatalogEventHandling(): ...
def RegenerateThumbnail(catalogItem): ...
