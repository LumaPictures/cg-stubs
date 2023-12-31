# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets as QT4FormWidgets
import UI4.FormMaster.Editors.SortableArray as SortableArray
import UI4.FormMaster.Editors.SortableArray
import Utils as Utils
from QT4FormWidgets.StringFormWidget import StringFormWidget
from typing import Set, Tuple

class AttributeNameArrayEditor(UI4.FormMaster.Editors.SortableArray.SortableArrayEditor):
    def addButtonCheckDragEvent(self, event): ...
    def addButtonDropEvent(self, event): ...

class AttributeNameEditor(StringFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def dragEnterEvent(self, event): ...
    def dropEvent(self, event): ...
    def setLocked(self, value, checkLockOps: bool = ...): ...
