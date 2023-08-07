# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import UI4.Widgets.SceneGraphView.SceneGraphViewIconManager as SceneGraphViewIconManager
import Nodes3DAPI.ScenegraphManager as ScenegraphManager
import Utils as Utils
from UI4.Widgets.ToolbarButton import ToolbarButton as ToolbarButton
from _typeshed import Incomplete
from typing import Set, Tuple

class ViewerWorkingSetButton(ToolbarButton):
    def __init__(self, parent: PyQt5.QtWidgets.QWidget, viewerManager: Incomplete | None = ...) -> None: ...
    def _ViewerWorkingSetButton__on_toggled(self): ...
    def _ViewerWorkingSetButton__on_viewer_visibilityFollowsWorkingSetChanged(self, eventType, eventID, visibilityFollowsWorkingSet): ...
