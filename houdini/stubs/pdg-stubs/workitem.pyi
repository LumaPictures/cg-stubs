# Houdini stubs generated from Houdini 22.0.466

import _pdg
from .callback import PythonCallback as PythonCallback
from pdg.scheduler import PyScheduler as PyScheduler

class PyWorkItem(PythonCallback):
    """
    Python wrapper class used to define custom work item types.

    Custom items should subclass from pdg.PyWorkItem and provide implementations
    for all of the virtual methods
    """
    def __init__(self, item: _pdg.WorkItem) -> None:
        """
        __init__(self, _pdg.WorkItem) -> NoneType

        Called when the work item should be initialized. `item` is the
        underyling C++ work item object wrapped by this Python instance
        """
    def __eq__(self, item: object) -> bool:
        """
        __eq__(self, _pdg.PyWorkItem) -> boolean

        Compares this work item and another for equality, using the
        `pdg.PyWorkItem.compare` method
        """
    def __ne__(self, item: object) -> bool:
        """
        __ne__(self, _pdg.PyWorkItem) -> boolean

        Compares this work item and another for inequality, using the
        `pdg.PyWorkItem.compare` method
        """
    def serialize(self, item: PyWorkItem, scheduler: PyScheduler) -> bytes:
        """
        serialize(self, _pdg.PyWorkItem, _pdg.PyScheduler) -> str

        [virtual] Serialises the work item to a string. Must be implemented by
        subclasses.
        """
    def deserialize(self, serialized_str: str) -> str:
        """
        deserialize(self, str) -> str

        [virtual] Deserializes the work item from a string, used by task graph
        serialization. Must be implemented by subclasses.
        """
    def serializeToFile(self, file_name: str, item: PyWorkItem, scheduler: PyScheduler) -> bool:
        """
        serializeToFile(self, str, _pdg.PyWorkItem, _pdg.Scheduler) -> boolean

        Serializes the work item to the specified file path
        """
    def __getitem__(self, key: str) -> _pdg._Attribute: ...
