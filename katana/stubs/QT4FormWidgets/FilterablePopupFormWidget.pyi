# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.PaintingUtils as PaintingUtils
import QT4Widgets as QT4Widgets
import ResourceFiles as ResourceFiles
from QT4FormWidgets.BaseValueFormWidget import BaseValueFormWidget as BaseValueFormWidget
from QT4FormWidgets.FormWidget import AlignChildLabelWidths as AlignChildLabelWidths, AlignLeftControlWidths as AlignLeftControlWidths, FormWidget as FormWidget, ScrubbingStates as ScrubbingStates
from QT4Widgets.FilterablePopupButton import FilterablePopupButton
from ResourceFiles.IconManager import ResourceManager as ResourceManager
from _typeshed import Incomplete

class FilterablePopupFormWidget(BaseValueFormWidget):
    class Popup(QT4Widgets.FilterablePopupButton.FilterablePopup):
        def __init__(self, valuePolicy, parent: Incomplete | None = ...): ...
        def _markDirty(self): ...
        def _refreshContents(self): ...
        def _selectCurrentValue(self): ...
        def getValuePolicy(self): ...
        def refresh(self, force: bool = ...): ...
    class PopupButton(FilterablePopupButton):
        def __init__(self, valuePolicy): ...
        def _buildPopupWindow(self): ...
        def getValuePolicy(self): ...
    def _buildControlWidget(self, layout): ...
    def _buildLabel(self, labelText, pos: int = ...): ...
    def _buildPopupButton(self): ...
    def _itemChosen(self, text, meta): ...
    def _lockChanged(self, state): ...
    def _updateControlWidget(self): ...