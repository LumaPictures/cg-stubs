import enum
import hou
from PySide6 import QtGui
from collections import namedtuple as namedtuple
from collections.abc import Generator
from typing import Any, Callable as Callable, NamedTuple

class MessageDefinition(NamedTuple):
    id: str
    severity: hou.EnumValue[hou.severityType]
    title: str
    data: Any
    format_func: Callable[[MessageDefinition, MessageFormat], str] | None

class MessageFormat(enum.Enum):
    shortFormat = ...
    mediumFormat = ...
    longFormat = enum.auto()

MISSING_NODE_TYPES_ID: str
DOP_LICENSE_REQUIRED_ID: str
MESSAGES: dict[str, MessageDefinition]

def formatMessage(msg_def: MessageDefinition, msg_format: MessageFormat = ...) -> str: ...
def messageIcon(msg_def: MessageDefinition) -> QtGui.QIcon: ...
def registerMessage(msg_id: str, severity: hou.EnumValue[hou.severityType], title: str, data: Any = None, format_func: Callable[[MessageDefinition, MessageFormat], str] | None = None) -> bool:
    """Add a custom message definition."""
def messageDefinitions() -> list[MessageDefinition]:
    """ Returns list of MessageDefinition tuples
    """

class MessageStore:
    """ Message store used for managing recipe runtime messages.
    """
    def __init__(self) -> None: ...
    def addMessage(self, msgid: str, data: Any = None) -> None:
        """
        Add a message definition instance to the store.
        `msgid`: Message identifier.
        `data`: optional data logged with the message.
        """
    def removeMessage(self, msg_id: str) -> None: ...
    def clearMessages(self) -> None:
        """ Clear all runtime messages.
        """
    def isEmpty(self) -> bool: ...
    def messages(self, severity: hou.EnumValue[hou.severityType] | None = None) -> Generator[MessageDefinition, None, None]:
        """
        Generator to iterate over messages. If a severity type is 
        provided, only messages with that severity are returned.
        """
    def message(self, msg_id: str) -> MessageDefinition | None:
        """ Return specific message definition
        """
    def collectMessages(self, msg_format: MessageFormat = ..., first_msg: bool = False, severity: hou.EnumValue[hou.severityType] | None = None) -> list[str]:
        """ Retrieves all messages from the store and applies the 
            specified formatting using msg_format.
            msg_format: formatting option.
            severity: Type of messages to collect. If None, all 
                      messages are collected.
            first_msg: returns the first message only if True.
        """
    def hasError(self) -> bool: ...
    def hasWarning(self) -> bool: ...
    def hasInfoMessage(self) -> bool: ...
