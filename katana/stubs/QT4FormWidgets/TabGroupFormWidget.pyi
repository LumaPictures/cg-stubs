# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.PaintingUtils as PaintingUtils
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from QT4FormWidgets.FWidget import FBoxLayout as FBoxLayout, FButton as FButton, FDisclosureTriangle as FDisclosureTriangle, FLabel as FLabel, FLockIcon as FLockIcon, FMenu as FMenu, FPixmap as FPixmap, FSpacer as FSpacer, FStateBadge as FStateBadge, FSvgIcon as FSvgIcon, FToggleStateBadge as FToggleStateBadge, FWidget as FWidget
from QT4FormWidgets.FormWidget import AlignChildLabelWidths as AlignChildLabelWidths, AlignLeftControlWidths as AlignLeftControlWidths, FormWidget as FormWidget, ScrubbingStates as ScrubbingStates
from QT4FormWidgets.NumberFormWidget import CreateSensitivityMenu as CreateSensitivityMenu, FormatNumber as FormatNumber, NumberFormWidget as NumberFormWidget
from QT4FormWidgets.StringFormWidget import StringFormWidget as StringFormWidget
from QT4FormWidgets.ValuePolicy import ValuePolicyEvent as ValuePolicyEvent, ValuePolicyProxy as ValuePolicyProxy
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class TabGroupFormWidget(FormWidget):
    _TabGroupFormWidget__STYLEMAP: ClassVar[dict] = ...
    def __init__(self, parent, policy, factory) -> None: ...
    def _TabGroupFormWidget__getTabWidgetPolicy(self, tabIndex): ...
    def _TabGroupFormWidget__syncChildren(self): ...
    def _TabGroupFormWidget__tabIconClicked_CB(self, tabIndex): ...
    def _TabGroupFormWidget__tabValueChanged(self, ev): ...
    def _TabGroupFormWidget__updateTabStateBadges(self, onlyUpdateIndex: Incomplete | None = ...): ...
    def _buildControlWidget(self, layout): ...
    def _buildTopAreaLayout(self, layout): ...
    def _createChildWidget(self, policy, parentWidget, factory, index): ...
    def _firstChildFormWidgetIndex(self): ...
    def _freeze(self): ...
    def _participatesInLabelAlignment(self): ...
    def _popdownCreated(self, popdown): ...
    def _thaw(self): ...
    def alignChildLabelWidths(self): ...
    def getPopdownIndent(self): ...
    def paintEvent(self, event): ...
    def showPopdown(self, value): ...
    def valueChangedEvent(self, event): ...
