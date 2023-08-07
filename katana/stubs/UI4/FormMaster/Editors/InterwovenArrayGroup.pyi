# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.FormMaster.Editors.SortableArray
import UI4.Widgets.SortablePanel
import Utils as Utils
from UI4.FormMaster.Editors.SortableArray import SortableArrayEditor as SortableArrayEditor
from UI4.Widgets.SortablePanel import SortablePanelBase as SortablePanelBase
from typing import Set, Tuple

class InterwovenArrayGroupEditor(UI4.FormMaster.Editors.SortableArray.SortableArrayEditor):
    def __init__(self, parent, policy, factory) -> None: ...
    def _InterwovenArrayGroupEditor__childValueChanged(self, event): ...
    def _InterwovenArrayGroupEditor__idle_callback(self, *args, **kwds): ...
    def _InterwovenArrayGroupEditor__update(self): ...
    def _freeze(self): ...
    def _thaw(self): ...
    def newEntry(self): ...
    def panelDeleted(self, index): ...
    def panelReordered(self, oldPos, newPos): ...
    def updatePanels(self): ...

class InterwovenArrayPanel(UI4.Widgets.SortablePanel.SortablePanelBase):
    def __init__(self, parent, policies, factory) -> None: ...
