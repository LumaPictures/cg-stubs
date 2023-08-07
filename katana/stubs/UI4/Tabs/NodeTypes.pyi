# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import NodegraphAPI as NodegraphAPI
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
import Utils as Utils
from PyUtilModule.VirtualKatana import FormMaster as FormMaster
from UI4.Tabs.BaseTab import BaseTab as BaseTab
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

NodeTypes: list
PluginRegistry: list
nodeType: str
nodeTypesValue: str

class CustomNodeTypeTab(NodeTypeTab):
    NodeType: ClassVar[str] = ...

class NodeTypePanel(NodeTypeTab): ...

class NodeTypeTab(BaseTab):
    def __init__(self, parent) -> None: ...
    def _NodeTypeTab__on_combobox_activated(self, text): ...
    def doNodesChanged(self, args: Incomplete | None = ...): ...
    def hideEvent(self, event): ...
    def registerHandlers(self, state): ...
    def showEvent(self, event): ...

class ScrollingParameters(PyQt5.QtWidgets.QScrollArea):
    def __init__(self, parent, param) -> None: ...
