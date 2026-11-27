import hou
from typing import Literal, NamedTuple

class MouseState(NamedTuple):
    lmb: bool
    mmb: bool
    rmb: bool

class ModifierState(NamedTuple):
    alt: bool
    ctrl: bool
    shift: bool

class WheelState(NamedTuple):
    pixeldelta: hou.Vector2
    phase: int

class InitializationEvent(NamedTuple):
    editor: hou.NetworkEditor
    eventtype: Literal['initialization']

class MouseEvent(NamedTuple):
    editor: hou.NetworkEditor
    eventtype: Literal['mouseenter', 'mousemove', 'mouseexit', 'mousedown', 'mousedrag', 'mouseup', 'doubleclick', 'mousewheel']
    selected: NetworkComponent
    located: NetworkComponent
    mousepos: hou.Vector2
    mousestartpos: hou.Vector2
    mousestate: MouseState
    dragging: bool
    wheelvalue: int
    modifierstate: ModifierState
    time: float
    wheelstate: WheelState | None = ...

class GestureEvent(NamedTuple):
    editor: hou.NetworkEditor
    eventtype: Literal['gesture']
    located: NetworkComponent
    mousepos: hou.Vector2
    scale: float
    time: float

class KeyboardEvent(NamedTuple):
    editor: hou.NetworkEditor
    eventtype: Literal['keyhit', 'menukeyhit', 'parentkeyhit', 'keydown', 'keyup']
    located: NetworkComponent
    mousepos: hou.Vector2
    mousestate: MouseState
    key: str
    rawkey: str
    modifierstate: ModifierState
    time: float

class ValueEvent(NamedTuple):
    editor: hou.NetworkEditor
    eventtype: Literal['editvalue']
    valueid: int
    value: str

class TimerEvent(NamedTuple):
    editor: hou.NetworkEditor
    eventtype: Literal['timer']
    timerid: int

class ContextEvent(NamedTuple):
    editor: hou.NetworkEditor
    eventtype: Literal['context']
    oldcontext: str
    context: str

class ContextClearEvent(NamedTuple):
    editor: hou.NetworkEditor
    eventtype: Literal['contextclear']
    context: str

class ModalUIEvent(NamedTuple):
    editor: hou.NetworkEditor
    eventtype: Literal['startmodalui', 'endmodalui']
    interfacename: str

class NetworkComponent(NamedTuple):
    item: hou.NetworkItem | NodeDependency | hou.Color | str | int | None
    name: str
    index: int  # type: ignore[assignment]

class WireSegment(NamedTuple):
    conn: hou.NodeConnection
    segment: int

class NodeDependency(NamedTuple):
    node: hou.OpNode
    othernode: hou.OpNode | None
