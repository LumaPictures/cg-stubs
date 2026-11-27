import _pdg
from pdg.partitioner import PyPartitioner as PyPartitioner

class PythonPartitioner(PyPartitioner):
    """
    Python partitioner implementation
    """
    def __init__(self, node: _pdg.Node) -> None:
        """
        __init__(self, pdg.Node) -> NoneType

        Initializes the partitioner with a C++ node referencee
        """
    @classmethod
    def templateName(cls) -> str: ...
    def onPartition(self, partitions: _pdg.PartitionHolder, work_items: _pdg.WorkItemList) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
