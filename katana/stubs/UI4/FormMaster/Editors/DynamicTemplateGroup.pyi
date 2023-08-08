# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import PyXmlIO as PyXmlIO
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4.Widgets.SortablePanel as SortablePanel
import UI4 as UI4
import UI4.FormMaster.Editors.UserParametersDialogs
import UI4.Widgets.SortablePanel
import Naming as UniqueName
import Utils as Utils
from UI4.FormMaster.Editors.UserParametersDialogs import ParameterRenameDialog as ParameterRenameDialog
from typing import Set, Tuple

class CopyChildrenDialog(PyQt5.QtWidgets.QDialog):
    def __init__(self, children) -> None: ...
    def _CopyChildrenDialog__selectionChanged(self): ...
    def accept(self): ...

class DynamicTemplateGroupFormWidget(UI4.Widgets.SortablePanel.SortablePanelFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _DynamicTemplateGroupFormWidget__addTemplate(self, templateName): ...
    def _DynamicTemplateGroupFormWidget__copy(self): ...
    def _DynamicTemplateGroupFormWidget__paste(self): ...
    def _childPanelsShouldAddWrench(self): ...
    def alignChildLabelWidths(self): ...
    def buildAddMenu(self, menu): ...
    def panelDeleted(self, index): ...
    def panelReordered(self, oldPos, newPos): ...
    def showPopdown(self, value): ...
    def updatePanels(self): ...

class TemplateGroupPanel(UI4.Widgets.SortablePanel.SortablePanelBase):
    def __init__(self, parent, name, policy, widgetFactory, addWrench) -> None: ...
    def _TemplateGroupPanel__getLabelBaseName(self, inputName): ...
    def _TemplateGroupPanel__nameChangedEvent(self, event): ...
    def _TemplateGroupPanel__policyNameChanged(self, event): ...
    def _TemplateGroupPanel__renameAction(self): ...
    def _TemplateGroupPanel__setName(self, value): ...
    def _TemplateGroupPanel__wrenchMenuAboutToShow(self): ...
    def _freeze(self): ...
    def _thaw(self): ...
    def getValuePolicy(self): ...
    def getWidget(self): ...
    def hideEvent(self, event): ...
    def showEvent(self, event): ...

class TemplateInstanceNameDialog(UI4.FormMaster.Editors.UserParametersDialogs.ParameterRenameDialog):
    def __init__(self, startingName, peerNames, templateType) -> None: ...
    def _getAdjustedFieldValue(self, text): ...
    def _getAdjustedUniqueDisplayName(self, text): ...
    def _isTextValid(self, text): ...