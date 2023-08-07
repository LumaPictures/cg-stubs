# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.FormMaster.Editors.NodeGroup as NodeGroup
import UI4.FormMaster.Editors.PortNameAndOrderWidget as PortNameAndOrderWidget
import PyQt5.QtCore as QtCore
import UI4.FormMaster.Editors.NodeGroup
from typing import Set, Tuple

class MultiInputPortNodeEditor(UI4.FormMaster.Editors.NodeGroup.NodeGroupFormWidget):
    def __init__(self, parent, valuePolicy, widgetFactory) -> None: ...
