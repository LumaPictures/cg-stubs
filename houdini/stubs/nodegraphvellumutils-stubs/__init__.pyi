import hou
import nodegraph
import nodegraphbase as base
from canvaseventtypes import KeyboardEvent, MouseEvent, NetworkComponent as NetworkComponent
from collections.abc import Iterable, Sequence
from nodegraphselectposhooks import _SelectPosContextData
from typing import Literal, TypeGuard, TypedDict

from typing import TypeAlias
from canvaseventtypes import GestureEvent
from canvaseventtypes import ModalUIEvent
from canvaseventtypes import TimerEvent
from canvaseventtypes import ValueEvent
from typing import TypeAlias
_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
_WireItem: TypeAlias = hou.Node | hou.NetworkDot | hou.SubnetIndirectInput
_InputWire: TypeAlias = tuple[hou.Node | hou.IndirectInput | None, int, int]
_OutputWire: TypeAlias = tuple[hou.Node | hou.NetworkDot, int, int]
class _VellumConnections(TypedDict):
    inputs: list[_InputWire]
    outputs: list[_OutputWire]

def isVellumNode(node: hou.NetworkMovableItem | None) -> TypeGuard[hou.OpNode]: ...
def findConnectionCandidates(vellumnode: _WireItem, prevnode: _WireItem, searchinput: int, nodecenter: object, direction: Literal['input', 'output']) -> list[hou.NodeConnection]: ...
def cross(a: hou.Vector2, b: hou.Vector2, c: hou.Vector2) -> float: ...
def getPointLineDist(point: hou.Vector2, lineA: hou.Vector2, lineB: hou.Vector2) -> float: ...
def getConnectionDist(editor: hou.NetworkEditor, conn: hou.NodeConnection, pos: hou.Vector2 | Sequence[float], vbias: float = 1.5) -> float: ...
def findVellumOutputInInputs(startnode: hou.NetworkMovableItem | None, outputindex: int = -1, includeme: bool = False) -> tuple[hou.OpNode | hou.SubnetIndirectInput | None, int]:
    """ Finds a vellum node output in the inputs of 'startnode' and returns
        (foundnode, outputindex), where 'foundnode' is the found vellum node and
        outputindex is the index of the output by which the search reached the
        node.

        Note that vellumnode may be a hou.SubnetIndirectInput since we stop at
        subnet boundaries and these are treated as vellum nodes.

        If includeme is True the first node will be returned if it is a vellum
        node. In that case the outputindex by which the startnode was reached
        should be supplied.

        Returns (None, -1) when no vellum node was found.
    """
def findVellumInputInOutputs(startnode: hou.NetworkMovableItem | None, inputindex: int = -1, includeme: bool = False) -> tuple[hou.OpNode | None, int]:
    """ Finds a vellum node input in the outputs of 'startnode' and returns
        (foundnode, inputindex), where 'foundnode' is the found vellum node and
        inputindex is the index of the input by which the search reached the
        node.

        If includeme is True the first node will be returned if it is a vellum
        node. In that case the inputindex by which the startnode was reached
        should be supplied.

        Returns (None, -1) when no vellum node was found.
    """
def getSurroundingVellumNodesAndIndex(inputitem: hou.Node | hou.IndirectInput | None, outputindex: int | None, outputitem: hou.Node | hou.NetworkDot | None, inputindex: int | None) -> tuple[hou.OpNode | hou.SubnetIndirectInput | None, hou.OpNode | None, int]: ...
def getVellumNodeConnections(inputitem: hou.Node | hou.IndirectInput | None, outputindex: int | None, outputitem: hou.Node | hou.NetworkDot | None, inputindex: int | None, editor: hou.NetworkEditor, nodecenter: hou.Vector2, branch: bool, inputs: bool = True, outputs: bool = True) -> _VellumConnections: ...
def setSelectPosContextData(editor: hou.NetworkEditor, contextdata: _SelectPosContextData, locatedconn: NetworkComponent | hou.NodeConnection | None, locatedinput: NetworkComponent | None, locatedoutput: NetworkComponent | None) -> bool: ...
def isPassThroughConnection(index: int) -> bool: ...
def createEventHandler(uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> tuple[NodeVellumMouseHandler | None, bool]: ...

class NodeVellumMouseHandler(nodegraph.NodeMouseHandler):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NodeVellumMoveHandler(nodegraph.NodeMoveHandler):
    def getInputWires(self, editor: hou.NetworkEditor, item: hou.NetworkMovableItem, conn: hou.NodeConnection, pos: hou.Vector2) -> list[_InputWire]: ...
    def getOutputWires(self, editor: hou.NetworkEditor, item: hou.NetworkMovableItem, conn: hou.NodeConnection, pos: hou.Vector2) -> list[_OutputWire]: ...
    def buildPreviewWires(self, editor: hou.NetworkEditor, conn: hou.NodeConnection) -> list[hou.NetworkShapeConnection]: ...
    def handleDrop(self, mouseitem: NetworkComponent, uievent: MouseEvent | KeyboardEvent) -> None: ...
    def makeChainConnections(self, inconns: Iterable[_InputWire], outconns: Iterable[_OutputWire], item_chain: Sequence[hou.NetworkMovableItem], editor: hou.NetworkEditor) -> None: ...
