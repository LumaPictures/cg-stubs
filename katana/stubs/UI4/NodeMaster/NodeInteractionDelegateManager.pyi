# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
from typing import Set, Tuple

class Delegate:
    def acceptsDrop(self, targetNode, event): ...
    def addToContextMenu(self, targetNode, menu): ...
    def addToNodeSpecificShelfEnvironment(self, targetNode, editor, envDict): ...
    def getLastContextMenuNode(self): ...
    def processDrop(self, targetNode, event): ...

def AcceptsDrop(targetNode, event): ...
def AddToContextMenu(targetNode, menu): ...
def AddToNodeSpecificShelfEnvironment(targetNode, editor, envDict): ...
def ProcessDrop(targetNode, event): ...
def RegisterDelegate(nodeType, delegate): ...
