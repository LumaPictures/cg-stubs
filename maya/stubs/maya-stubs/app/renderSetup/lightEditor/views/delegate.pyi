import maya.app.renderSetup.views.renderSetupDelegate as renderSetupDelegate
from _typeshed import Incomplete

class DataDelegate:
    def draw(self, painter, rect, data, mapped) -> None: ...

class FloatDelegate(DataDelegate):
    def draw(self, painter, rect, data, mapped) -> None: ...

class IntDelegate(DataDelegate):
    def draw(self, painter, rect, data, mapped) -> None: ...

class BoolDelegate(DataDelegate):
    def draw(self, painter, rect, data, mapped) -> None: ...

class ColorDelegate(DataDelegate):
    COLOR_SWATCH_WIDTH: Incomplete
    def draw(self, painter, rect, data, mapped) -> None: ...

class LightEditorDelegate(renderSetupDelegate.RenderSetupDelegate):
    LIGHT_ICON_SIZE: Incomplete
    LIGHT_ICON_OFFSET_X: Incomplete
    LIGHT_ICON_OFFSET_Y: Incomplete
    TEXT_LEFT_OFFSET: Incomplete
    TEXT_RIGHT_OFFSET: Incomplete
    LIGHT_ATTR_WIDTH: Incomplete
    OVERRIDDEN_COLOR: Incomplete
    BOLD_STYLE_OFFSET_X: Incomplete
    dataDelegates: Incomplete
    kToolTipDisableLight: Incomplete
    kToolTipDisableGroup: Incomplete
    lightTypeIcon: Incomplete
    def __init__(self, treeView) -> None: ...
    def getTextRect(self, rect, item): ...
    def updateEditorGeometry(self, editor, option, index) -> None: ...
