# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.HintUtils as HintUtils
import QT4FormWidgets.PaintingUtils as PaintingUtils
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from QT4FormWidgets.BaseValueFormWidget import BaseValueFormWidget as BaseValueFormWidget
from QT4FormWidgets.FormWidget import FormWidget as FormWidget
from _typeshed import Incomplete
from typing import Set, Tuple

class CapsuleFormWidget(BaseValueFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _CapsuleFormWidget__setOptionsFromHints(self, hints, appliedHints: Incomplete | None = ...): ...
    def _CapsuleFormWidget__updateCapsule(self, value): ...
    def _assignValue(self, value): ...
    def _buildControlWidget(self, layout): ...
    def _checkControlWidget(self, enabledItems, oldEnabledItems): ...
    def _interpretValue(self, value): ...
    def _lockChanged(self, state): ...
    def _updateControlWidget(self): ...
    def _updateWithHints(self, originalHints, hints): ...
    def getOptions(self): ...
    def setExclusive(self, exclusive): ...
    def setOptions(self): ...
    def setTransitionValidator(self, validator): ...
