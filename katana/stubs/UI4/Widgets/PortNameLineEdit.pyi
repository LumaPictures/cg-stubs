# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
import QT4FormWidgets as QT4FormWidgets
import QT4FormWidgets.InputWidgets
import Utils as Utils
from typing import Set, Tuple

class PortNameLineEdit(QT4FormWidgets.InputWidgets.InputLineEdit):
    def __init__(self, node: NodegraphAPI.Node, portIndex, *args) -> None: ...
    def _PortNameLineEdit__renameInputPort_CB(self, messageType, nodePtr, **kwargs): ...
    def _PortNameLineEdit__updateText(self): ...
    def doReturnPressed(self): ...
    def getNode(self) -> NodegraphAPI.Node: ...
    def getPortIndex(self): ...
    def setIndex(self, index): ...
