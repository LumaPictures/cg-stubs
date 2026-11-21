# Houdini stubs generated from Houdini 22.0.466

import _pdgd
import hou
import pdgd.util
from .houparmtuplehandler import HouParmTupleHandler as HouParmTupleHandler
from _pdgd import _PythonValue
from collections.abc import Callable
from typing import ClassVar

from typing import TypeVar
from typing import TypeVar
_F = TypeVar('_F', bound=Callable[..., object])
class EventHandlerBase(pdgd.util.SimpleHandler):
    event_handlers: ClassVar[dict[hou.EnumValue[hou.nodeEventType], Callable[..., object]]]
    def __init__(self, handler: _pdgd.SubscriptionHandler) -> None: ...
    @classmethod
    def eventHandler(cls, event_type: hou.EnumValue[hou.nodeEventType]) -> Callable[[_F], Callable[[], _F]]: ...

class HouNodeHandler(EventHandlerBase):
    """
    Provides access to hou nodes data and operations
    """
    geometry_handler: str | None
    parmTuples: dict[str, _pdgd.PySubscriptionHandler]
    node: hou.OpNode
    def __init__(self, handler: _pdgd.SubscriptionHandler, handler_name: str | None = None) -> None:
        """
        Initializes the node handler, we use node ids
        instead of names, because names can change in
        a session
        """
    def __del__(self) -> None:
        """
        Perform any necessary cleanup
        """
    def getPath(self, params: _PythonValue) -> str: ...
    def createGeometryHandler(self, params: _PythonValue) -> str: ...
    def eventCallback(self, event_type: hou.EnumValue[hou.nodeEventType], **kwargs: object) -> None:
        """
        Ensure we process and send required messages
        """
    def onChildCreated(self, child_node: hou.OpNode, **kwargs: object) -> None:
        """
        Called when a child node was created
        """
    def onChildDeleted(self, child_node: hou.OpNode, **kwargs: object) -> None:
        """
        Called when a child node was deleted
        """
    def onParmTupleChanged(self, parm_tuple: hou.ParmTuple | None, **kwargs: object) -> None:
        """
        A parm has been changed
        """
    def createChildNodeHandler(self, child_node: hou.OpNode) -> None:
        """
        Creates a child handler for the child node
        """
    def removeChildNodeHandler(self, child_node: hou.OpNode) -> None:
        """
        Removes a child handler
        """
    def addParmTuple(self, parmTuple: hou.ParmTuple) -> None:
        """
        Adds parm information
        """
    def removeParmTuple(self, parmTuple: hou.ParmTuple) -> None:
        """
        Removes parm information
        """
