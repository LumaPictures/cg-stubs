# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from QT4FormWidgets.GroupFormWidget import GroupFormWidget
from QT4FormWidgets.MultiFormWidget import MultiFormWidget
from typing import Set, Tuple

class PageGroupBoxWidget(GroupFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _buildTopAreaLayout(self, layout): ...
    def _popdownCreated(self, popdown): ...

class PageGroupWidget(MultiFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _buildControlWidget(self, controlLayout): ...
    def _buildLabel(self, labelText, pos: int = ...): ...
    def _buildTopAreaLayout(self, layout): ...
    def _popdownCreated(self, popdown): ...
