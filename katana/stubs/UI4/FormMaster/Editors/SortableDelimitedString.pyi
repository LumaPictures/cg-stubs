# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import UI4.Widgets.SortablePanel
from UI4.Widgets.SortablePanel import ParameterExpressionPanel as ParameterExpressionPanel, ParameterSortablePanel as ParameterSortablePanel, ParameterSortablePanelFormWidget as ParameterSortablePanelFormWidget, SortablePanelBase as SortablePanelBase, SortablePanelFormWidget as SortablePanelFormWidget
from typing import Set, Tuple

class SortableDelimitedStringFormWidget(UI4.Widgets.SortablePanel.SortablePanelFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _SortableDelimitedStringFormWidget__setValue(self): ...
    def _SortableDelimitedStringFormWidget__toggleExpression(self): ...
    def buildAddMenu(self, menu): ...
    def newEntry(self): ...
    def panelDeleted(self, index): ...
    def panelReordered(self, oldPos, newPos): ...
    def panelValueChanged(self, index): ...
    def updatePanels(self): ...

class StringPanel(UI4.Widgets.SortablePanel.SortablePanelBase):
    def __init__(self, parent, value, numbers, factory, hints) -> None: ...
    def _StringPanel__valueChanged(self, *args, **kwds): ...
    def getValue(self): ...
    def setValue(self, text): ...
