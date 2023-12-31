# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import PyQt5.QtWidgets
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import Utils as Utils
from PyUtilModule.VirtualKatana import FormMaster as FormMaster
from UI4.Tabs.BaseTab import BaseTab as BaseTab
from UI4.Widgets.PanelScrollArea import PanelScrollArea
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class ParameterPanel(BaseTab):
    def __init__(self, parent) -> None: ...
    def _ParameterPanel__findParameterActionCallback(self): ...
    def _ParameterPanel__findPolicyForParameter(self, policy, parameter): ...
    def _ParameterPanel__navigationCallback(self, nodeNames, isBack): ...
    def _ParameterPanel__node_setEdited_callback(self, args: Incomplete | None = ...): ...
    def dragEnterEvent(self, event): ...
    def dropEvent(self, event): ...
    def getPointedWidget(self) -> PyQt5.QtWidgets.QWidget | None: ...
    def parameterEditor_exposeParameter_callback(self, args): ...
    @staticmethod
    def registerKeyboardShortcuts(): ...

class TearoffParameterPanel(PanelScrollArea):
    NonPersistantPanel: ClassVar[bool] = ...
    def __init__(self, parent) -> None: ...
    def _TearoffParameterPanel__node_delete_callback(self, eventName, eventId, **eventArgs): ...
    def getNode(self) -> NodegraphAPI.Node | None: ...
    def setFromWidget(self, widget): ...
    def setNode(self, node: NodegraphAPI.Node): ...

class TearoffParameterTab(BaseTab):
    def __init__(self, parent) -> None: ...
    def getTabTitle(self) -> str | None: ...
    def setFromWidget(self, widget): ...
    def setNode(self, node: NodegraphAPI.Node): ...
