# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnGeolibServices.ExpressionMath as ExpressionMath
import PyFnGeolibServices as FnGeolibServices
import NodegraphAPI as NodegraphAPI
import PyFCurve as PyFCurve
import PyQt5.QtCore
import QT4Browser as QT4Browser
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.MultiStateBadge
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
from QT4FormWidgets.NumberFormWidget import NumberFormWidget
from typing import ClassVar, Set, Tuple

class DualInputKatanaNumberFormWidget(KatanaNumberFormWidget):
    def _DualInputKatanaNumberFormWidget__altPolicyValueChanged(self, event): ...
    def _DualInputKatanaNumberFormWidget__evalConversion(self, expr, value): ...
    def _buildControlWidget(self, layout): ...
    def _updateControlWidget(self): ...
    def valueChangedEvent(self, event): ...

class EditSignalingNumberFormWidget(KatanaNumberFormWidget):
    class _SignalingToggleStateBadge(QT4FormWidgets.MultiStateBadge.ToggleStateBadge):
        pressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
        def mousePressEvent(self, event): ...
    userEdited: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def _EditSignalingNumberFormWidget__userEdited(self, *args): ...
    def _buildControlWidget(self, layout): ...
    def _buildStateBadge(self, policy): ...
    def _popdownCreated(self, popdown): ...
    def labelSliderDrag(self, pos, modifiers): ...
    def labelSliderEnd(self, pos, modifiers): ...
    def supportsStickyScrub(self) -> bool: ...

class KatanaNumberFormWidget(NumberFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _KatanaNumberFormWidget__bakeToFCurve(self): ...
    def _KatanaNumberFormWidget__exportCurveToFCurveXML(self): ...
    def _KatanaNumberFormWidget__importCurveFromFCurveFile(self): ...
    def _addExportMenuActions(self, menu): ...
    def _addExtraMenuAction(self, menu): ...
    def _addImportMenuActions(self, menu): ...
