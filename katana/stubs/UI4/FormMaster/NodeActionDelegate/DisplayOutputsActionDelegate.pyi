# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import UI4.FormMaster.NodeActionDelegate.NodeActionDelegate as NodeActionDelegate
import NodegraphAPI
import PyQt5.QtWidgets
import PyQt5.QtWidgets as QtWidgets
import Utils as Utils
from UI4.FormMaster.NodeActionDelegate.BaseNodeActionDelegate import BaseNodeActionDelegate as BaseNodeActionDelegate
from _typeshed import Incomplete
from typing import Set, Tuple

class DisplayOutputsActionDelegate(BaseNodeActionDelegate):
    class _DisplayOutputsAction(PyQt5.QtWidgets.QAction):
        def __init__(self, parent, node: NodegraphAPI.Node) -> None: ...
        def _DisplayOutputsAction__toggled(self, state): ...
    def addToWrenchMenu(self, menu, node: NodegraphAPI.Node, hints: Incomplete | None = ...): ...
