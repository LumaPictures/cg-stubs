# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyUtilModule.RenderManager.RenderGlobals as RenderGlobals
import PyUtilModule.RenderManager as RenderManager
import Utils as Utils
from UI4.Util.IconManager import GetPixmap as GetPixmap
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from typing import Set, Tuple

class LiveRenderViewerCameraButton(ToolbarButton):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget, viewportWidget: ViewportWidget) -> None: ...
    def _LiveRenderViewerCameraButton__on_toggled(self): ...
    def _LiveRenderViewerCameraButton__on_viewer_liveRenderFromViewerCameraChanged(self, eventType: str, eventID: object, followViewportCamera: Bool, viewportWidget: ViewportWidget): ...
