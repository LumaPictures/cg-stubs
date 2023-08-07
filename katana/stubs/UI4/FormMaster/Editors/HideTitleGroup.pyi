# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from QT4FormWidgets.GroupFormWidget import GroupFormWidget
from typing import Set, Tuple

class HideTitleGroupFormWidget(GroupFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _buildTopAreaLayout(self, layout): ...
    def hideTitle(self): ...
