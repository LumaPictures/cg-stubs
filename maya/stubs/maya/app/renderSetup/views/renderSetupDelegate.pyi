import maya.app.renderSetup.views.baseDelegate as baseDelegate
from _typeshed import Incomplete

kRenderableToolTip: Incomplete
kNonRenderableToolTip: Incomplete
kRenderableSelectionToolTip: Incomplete
kNonRenderableSelectionToolTip: Incomplete

def createFilterPixmaps(): ...

class RenderSetupDelegate(baseDelegate.BaseDelegate):
    HIGHLIGHTED_FILL_OFFSET: int
    INFO_COLOR: Incomplete
    LEFT_NON_TEXT_OFFSET: Incomplete
    RIGHT_NON_TEXT_OFFSET: Incomplete
    DISABLED_IMAGE: Incomplete
    ISOLATE_IMAGE: Incomplete
    INVALID_IMAGE: Incomplete
    DISCLOSURE_IMAGE: Incomplete
    kTooltips: Incomplete
    @staticmethod
    def getFilterIcon(filter): ...
    def __init__(self, treeView) -> None: ...
    def createEditor(self, parent, option, index): ...
    def getTextRect(self, rect, item): ...
    def updateEditorGeometry(self, editor, option, index) -> None: ...
