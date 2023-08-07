# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Widgets.MessageBox as MessageBox
import NodegraphAPI as NodegraphAPI
import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4.Widgets.SortablePanel
from QT4Widgets.MenuButton import MenuButton as MenuButton
from UI4.Widgets.SortablePanel import SortablePanelBase as SortablePanelBase, SortablePanelFormWidget as SortablePanelFormWidget
from typing import ClassVar, Set, Tuple

class ForkVariablesEditor(UI4.Widgets.SortablePanel.SortablePanelFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _ForkVariablesEditor__addNumberVariable(self): ...
    def _ForkVariablesEditor__addStringVariable(self): ...
    def _ForkVariablesEditor__getNewVariableName(self, typeid): ...
    def _ForkVariablesEditor__getNode(self): ...
    def addOutput(self): ...
    def buildAddMenu(self, menu): ...
    def deletePanel(self, index): ...
    def deleteVariable(self, name): ...
    def panelDeleted(self, index): ...
    def panelReordered(self, oldPos, newPos): ...
    def renameVariable(self, oldName, newName): ...
    def updatePanels(self): ...

class OutputVariablePanel(UI4.Widgets.SortablePanel.SortablePanelBase):
    class _OutputVariablePanel__VariableWidget(PyQt5.QtWidgets.QFrame):
        variableDelete: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
        variableRename: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
        def __init__(self, parent, policy, factory) -> None: ...
        def _VariableWidget__copyExpression(self): ...
        def _VariableWidget__deleteCallback(self): ...
        def _VariableWidget__renameVariable(self): ...
        def getWidgetLabelWidth(self): ...
        def setWidgetLabelWidth(self, width): ...
    def __init__(self, parent, name, policy, factory) -> None: ...
    def _OutputVariablePanel__deleteVariable(self, name): ...
    def _OutputVariablePanel__renameVariable(self, name): ...
