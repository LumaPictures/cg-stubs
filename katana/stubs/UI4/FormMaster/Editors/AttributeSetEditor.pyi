# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.FormMaster.Editors.NodeGroup as NodeGroup
import PyFnAttribute as PyFnAttribute
import UI4 as UI4
import UI4.FormMaster.Editors.NodeGroup
import Utils as Utils
from typing import Set, Tuple

class AttributeSetEditor(UI4.FormMaster.Editors.NodeGroup.NodeGroupFormWidget):
    def __init__(self, parent, valuePolicy, widgetFactory) -> None: ...
    def _AttributeSetEditor__attrDropped(self, attr, name): ...

def _GetAttrTypeString(attr): ...
