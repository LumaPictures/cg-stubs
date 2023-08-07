# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.FormMaster.Editors.PolicyFindPopup as PolicyFindPopup
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
from QT4FormWidgets.GroupFormWidget import GroupFormWidget
from typing import Set, Tuple

class FindingGroupFormWidget(GroupFormWidget):
    def _buildLock(self, layout): ...
    def showFindPopup(self): ...
