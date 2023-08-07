# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.FormMaster.Editors.NodeGroup as NodeGroup
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtWidgets as QtWidgets
import UI4.FormMaster.Editors.NodeGroup
from typing import Set, Tuple

class ChannelsNodeFormWidget(UI4.FormMaster.Editors.NodeGroup.NodeGroupFormWidget):
    def _createChildWidget(self, policy, parentWidget, factory, index): ...
    def _popdownCreated(self, popdown): ...
    def getPopdownWidget(self): ...
