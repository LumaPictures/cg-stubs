# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4Color.Globals as Globals
import PyQt5.QtCore
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.ValuePolicy
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import ResourceFiles as ResourceFiles
import ValuePolicy
import Utils.WeakMethod as WeakMethod
from QT4Color.ColorDropWidget import ColorDropWidget as ColorDropWidget
from QT4Color.ColorPolicy import DoesColorPolicyEnableFilmlook as DoesColorPolicyEnableFilmlook, DoesColorPolicyEnableNoFilmlookColorSpace as DoesColorPolicyEnableNoFilmlookColorSpace, DoesColorPolicyHaveAlpha as DoesColorPolicyHaveAlpha, GetColorPolicyChildren as GetColorPolicyChildren, GetColorPolicyRGBA as GetColorPolicyRGBA, GetDefaultColorComponentTab as GetDefaultColorComponentTab, SetColorPolicyRGBA as SetColorPolicyRGBA
from QT4Color.ColorTextWidget import ColorTextWidget as ColorTextWidget
from QT4Color.DropType import BuildDragDataFromInfo as BuildDragDataFromInfo, GetColorInfoFromDragObject as GetColorInfoFromDragObject, GetColorPolicyDragDict as GetColorPolicyDragDict
from QT4Color.Gradient1D import LinearGradientWidget as LinearGradientWidget
from QT4FormWidgets.GroupFormWidget import GroupFormWidget
from ResourceFiles.IconManager import ResourceManager as ResourceManager
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ColorComponentTabGroup(PyQt5.QtWidgets.QTabWidget):
    valueChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent, policy, factory, enableFilmlook: Incomplete | None = ..., enableNoFilmlookColorSpace: Incomplete | None = ..., readOnly: bool = ..., rgbaTab: bool = ..., hslTab: bool = ..., hsvTab: bool = ..., tmlTab: bool = ..., tabToSelect: str = ...) -> None: ...
    def _ColorComponentTabGroup__colorComponentValuePolicy_CB(self, incomingPolicy, rawComponentValue, final): ...
    def _ColorComponentTabGroup__gradWidgetValueChangedCB(self, color, final): ...
    def _ColorComponentTabGroup__handleCurrentChanged(self, index): ...
    def eventFilter(self, obj, event): ...
    def getComponentFormWidgets(self): ...
    def setColor(self, color): ...
    def setColorPolicy(self, colorPolicy: ValuePolicy.AbstractValuePolicy): ...
    def setFilmlookEnabled(self, enabled): ...
    def setNoFilmlookColorSpaceEnabled(self, enabled): ...
    def setReadOnly(self, readOnly): ...
    def updateComponentReadOnlyStates(self): ...

class ColorFormWidget(GroupFormWidget):
    _ColorFormWidget__WARNING_PIXMAP_NAME: ClassVar[str] = ...
    def __init__(self, parent, policy, factory) -> None: ...
    def _ColorFormWidget__addUpdateThrottlerCallbackToChildPolicies(self): ...
    def _ColorFormWidget__colorComponent_valueChanged_CB(self, color, final): ...
    def _ColorFormWidget__colorDropWidget_dropEvent_CB(self, dropEvent): ...
    def _ColorFormWidget__colorTextWidget_valueChanged_CB(self, color): ...
    def _ColorFormWidget__update(self): ...
    def _buildAdditionalControlWidgets(self, layout): ...
    def _buildControlWidget(self, layout): ...
    def _buildInfoWidget(self): ...
    def _buildLabel(self, labelText, pos: int = ...): ...
    def _createChildWidget(self, policy, parentWidget, factory, index): ...
    def _freeze(self): ...
    def _lockChanged(self, state): ...
    def _participatesInLabelAlignment(self): ...
    def _popdownCreated(self, popdown): ...
    def _thaw(self): ...
    def execColorPicker(self): ...
    def getColorComponentTabGroup(self): ...
    def getDragDict(self, policy): ...
    def isDropOnlyMode(self): ...
    def isMiniMode(self): ...
    def setColor_RGBA(self, color, final: bool = ...): ...
    def showPopdown(self, value): ...
    def valueChangedEvent(self, event): ...

class ThinValuePolicy(QT4FormWidgets.ValuePolicy.AbstractValuePolicy):
    def __init__(self, name, hints) -> None: ...
    def _setInternalValue(self, value, final: bool = ...): ...
    def getName(self): ...
    def getType(self): ...
    def getValue(self): ...
    def getWidgetHints(self): ...
    def setCallback(self, callback): ...
    def setValue(self, value, final: bool = ...): ...

class UpdateThrottler(PyQt5.QtCore.QObject):
    updateSignal: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, parent: Incomplete | None = ...) -> None: ...
    def _UpdateThrottler__update(self): ...
    def update(self, *args): ...
