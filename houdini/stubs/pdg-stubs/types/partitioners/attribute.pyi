import _pdg
from pdg.partitioner import PyPartitioner as PyPartitioner

from typing import TypeAlias
from typing import TypeAlias
_AttributeField: TypeAlias = tuple[int, _pdg.Port, _pdg.Port, _pdg.Port, _pdg.Port, _pdg.Port, _pdg.Port | None, _pdg.Port | None]
class PartitionByAttribute(PyPartitioner):
    """
    Partitioner implementation that groups items based on the prescence of
    one or more attributes
    """
    attributes: list[_AttributeField]
    def __init__(self, node: _pdg.Node) -> None:
        """
        __init__(self, pdg.Node) -> NoneType

        Initializes the partitioner
        """
    @classmethod
    def templateName(cls) -> str:
        """
        templateName(cls) -> str

        Returns the template name
        """
    @classmethod
    def templateBody(cls) -> str: ...
    def onPreCook(self) -> _pdg.result:
        """
        [virtual] Called once before the cook begins. Fetches the int, float
        and string fields from multiparms.
        """
    def onPartition(self, partition_holder: _pdg.PartitionHolder, work_items: _pdg.WorkItemList) -> _pdg.result:
        """
        [virtual] Partitions work items based on the specified attributes
        in the `attributes` parameters
        """

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
