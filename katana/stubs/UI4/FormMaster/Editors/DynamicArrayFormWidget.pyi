# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import UI4.Widgets.SortablePanel
from UI4.Widgets.SortablePanel import SortablePanelBase as SortablePanelBase, SortablePanelFormWidget as SortablePanelFormWidget
from _typeshed import Incomplete
from typing import Set, Tuple

class ArraySliceProxyPolicy:
    def __init__(self, policy, sliceStart, sliceEnd, overrideHints: Incomplete | None = ...) -> None: ...
    def getArrayChild(self, index): ...
    def getArraySize(self): ...
    def getOpenStateKey(self): ...
    def getOverrideHints(self): ...
    def getPolicy(self): ...
    def getSliceEnd(self): ...
    def getSliceSize(self): ...
    def getSliceStart(self): ...
    def getWidgetHints(self): ...
    def shouldDisplayState(self): ...
    def updateSlice(self, sliceStart, sliceEnd): ...
    def __eq__(self, other) -> bool: ...
    def __getattr__(self, name): ...
    def __lt__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...

class DynamicArrayFormWidget(UI4.Widgets.SortablePanel.SortablePanelFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def buildAddMenu(self, menu: PyQt5.QtWidgets.QMenu): ...
    def on_newEntryAction_triggered(self): ...
    def panelDeleted(self, index: int): ...
    def panelReordered(self, oldIndex: int, newIndex: int): ...
    def updatePanels(self): ...

class DynamicArrayPanel(UI4.Widgets.SortablePanel.SortablePanelBase):
    def __init__(self, parent, policy, factory) -> None: ...
    def getPolicy(self): ...
    def setPolicy(self, policy): ...
