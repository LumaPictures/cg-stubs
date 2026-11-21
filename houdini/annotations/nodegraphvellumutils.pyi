from collections.abc import Iterable, Sequence
from typing import Literal, TypeAlias, TypedDict, TypeGuard

import hou
from nodegraphselectposhooks import _SelectPosContextData
import nodegraph
import nodegraphbase as base
from canvaseventtypes import (
    GestureEvent,
    KeyboardEvent,
    ModalUIEvent,
    MouseEvent,
    NetworkComponent,
    TimerEvent,
    ValueEvent,
)

_UIEvent: TypeAlias = MouseEvent | KeyboardEvent | GestureEvent | ValueEvent | TimerEvent | ModalUIEvent
_WireItem: TypeAlias = hou.Node | hou.NetworkDot | hou.SubnetIndirectInput
_InputWire: TypeAlias = tuple[hou.Node | hou.IndirectInput | None, int, int]
_OutputWire: TypeAlias = tuple[hou.Node | hou.NetworkDot, int, int]

class _VellumConnections(TypedDict):
    inputs: list[_InputWire]
    outputs: list[_OutputWire]

def isVellumNode(node: hou.NetworkMovableItem | None) -> TypeGuard[hou.OpNode]: ...
def findConnectionCandidates(
    vellumnode: _WireItem,
    prevnode: _WireItem,
    searchinput: int,
    nodecenter: object,
    direction: Literal["input", "output"],
) -> list[hou.NodeConnection]: ...
def cross(a: hou.Vector2, b: hou.Vector2, c: hou.Vector2) -> float: ...
def getPointLineDist(point: hou.Vector2, lineA: hou.Vector2, lineB: hou.Vector2) -> float: ...
def getConnectionDist(editor: hou.NetworkEditor, conn: hou.NodeConnection, pos: hou.Vector2 | Sequence[float], vbias: float = ...) -> float: ...
def findVellumOutputInInputs(
    startnode: hou.NetworkMovableItem | None, outputindex: int = ..., includeme: bool = ...
) -> tuple[hou.OpNode | hou.SubnetIndirectInput | None, int]: ...
def findVellumInputInOutputs(
    startnode: hou.NetworkMovableItem | None, inputindex: int = ..., includeme: bool = ...
) -> tuple[hou.Node | None, int]: ...
def getSurroundingVellumNodesAndIndex(
    inputitem: hou.Node | hou.IndirectInput | None,
    outputindex: int | None,
    outputitem: hou.Node | hou.NetworkDot | None,
    inputindex: int | None,
) -> tuple[hou.OpNode | hou.SubnetIndirectInput | None, hou.Node | None, int]: ...
def getVellumNodeConnections(
    inputitem: hou.Node | hou.IndirectInput | None,
    outputindex: int | None,
    outputitem: hou.Node | hou.NetworkDot | None,
    inputindex: int | None,
    editor: hou.NetworkEditor,
    nodecenter: hou.Vector2,
    branch: bool,
    inputs: bool = ...,
    outputs: bool = ...,
) -> _VellumConnections: ...
def setSelectPosContextData(
    editor: hou.NetworkEditor,
    contextdata: _SelectPosContextData,
    locatedconn: NetworkComponent | hou.NodeConnection | None,
    locatedinput: NetworkComponent | None,
    locatedoutput: NetworkComponent | None,
) -> bool: ...
def isPassThroughConnection(index: int) -> bool: ...
def createEventHandler(uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> tuple["NodeVellumMouseHandler | None", bool]: ...

class NodeVellumMouseHandler(nodegraph.NodeMouseHandler):
    def handleEvent(self, uievent: _UIEvent, pending_actions: list[base.PendingAction]) -> base.EventHandler | None: ...

class NodeVellumMoveHandler(nodegraph.NodeMoveHandler):
    def getInputWires(self, editor: hou.NetworkEditor, item: hou.NetworkMovableItem, conn: hou.NodeConnection, pos: hou.Vector2) -> list[_InputWire]: ...
    def getOutputWires(self, editor: hou.NetworkEditor, item: hou.NetworkMovableItem, conn: hou.NodeConnection, pos: hou.Vector2) -> list[_OutputWire]: ...
    def buildPreviewWires(self, editor: hou.NetworkEditor, conn: hou.NodeConnection) -> list[hou.NetworkShapeConnection]: ...
    def handleDrop(self, mouseitem: NetworkComponent, uievent: MouseEvent | KeyboardEvent) -> None: ...
    def makeChainConnections(
        self,
        inconns: Iterable[_InputWire],
        outconns: Iterable[_OutputWire],
        item_chain: Sequence[hou.NetworkMovableItem],
        editor: hou.NetworkEditor,
    ) -> None: ...
