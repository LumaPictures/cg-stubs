# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets as QT4FormWidgets
from QT4FormWidgets.GroupFormWidget import GroupFormWidget
from UI4.Widgets.MonitorManipulatorButton import MonitorManipulatorButton as MonitorManipulatorButton
from typing import Set, Tuple

class ManipulatorGroupFormWidget(GroupFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
