# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import UI4.FormMaster.Editors.NodeGroup as NodeGroup
import NodegraphAPI as NodegraphAPI
import PyQt5.QtWidgets as QtWidgets
import UI4.FormMaster.Editors.NodeGroup
import Utils as Utils
from typing import Set, Tuple

class DotNodeEditor(UI4.FormMaster.Editors.NodeGroup.NodeGroupFormWidget):
    def __init__(self, parent, valuePolicy, widgetFactory) -> None: ...
    def _DotNodeEditor__clicked(self): ...
