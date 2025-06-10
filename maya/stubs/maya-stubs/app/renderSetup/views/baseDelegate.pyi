from PySide6.QtWidgets import QStyledItemDelegate
from _typeshed import Incomplete

def createPixmap(fileName): ...

class BaseDelegate(QStyledItemDelegate):
    ARROW_COLOR: Incomplete
    DISABLED_BACKGROUND_IMAGE: Incomplete
    DISABLED_HIGHLIGHT_IMAGE: Incomplete
    COLOR_BAR_WIDTH: Incomplete
    TEXT_LEFT_OFFSET: Incomplete
    TEXT_RIGHT_OFFSET: Incomplete
    LAYER_TEXT_RIGHT_OFFSET: Incomplete
    COLLECTION_TEXT_RIGHT_OFFSET: Incomplete
    GROUP_TEXT_RIGHT_OFFSET: Incomplete
    BOTTOM_GAP_OFFSET: Incomplete
    EXPANDED_ARROW_OFFSET: Incomplete
    COLLAPSED_ARROW_OFFSET: Incomplete
    EXPANDED_ARROW: Incomplete
    COLLAPSED_ARROW: Incomplete
    LAST_ICON_RIGHT_OFFSET: Incomplete
    ICON_WIDTH: Incomplete
    WARNING_ICON_WIDTH: Incomplete
    ICON_TOP_OFFSET: Incomplete
    ACTION_BORDER: Incomplete
    ACTION_WIDTH: Incomplete
    BACKGROUND_RECT_LENGTH: Incomplete
    BACKGROUND_RECT_LEFT_OFFSET: Incomplete
    VISIBILITY_IMAGE: Incomplete
    RENDERABLE_IMAGE: Incomplete
    WARNING_IMAGE: Incomplete
    treeView: Incomplete
    lastHitAction: Incomplete
    def __init__(self, treeView) -> None: ...
    def getTextRect(self, rect, item): ...
    def drawToolbarFrame(self, painter, rect, toolbarCount) -> None: ...
    def drawPixmap(self, painter, pixmap, left, top) -> None: ...
    def drawAction(self, painter, actionName, pixmap, left, top, highlightedColor, drawDisclosure, borderColor) -> None: ...
    def paint(self, painter, option, index) -> None: ...
