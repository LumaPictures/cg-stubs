from typing import TypeAlias

import _pdg
from pdg.partitioner import PyPartitioner

# (index, enable, type, name, enableindex, index, value, vector) of an `attributes` multiparm entry.
_AttributeField: TypeAlias = tuple[
    int,
    _pdg.Port,
    _pdg.Port,
    _pdg.Port,
    _pdg.Port,
    _pdg.Port,
    _pdg.Port | None,
    _pdg.Port | None,
]

class PartitionByAttribute(PyPartitioner):
    attributes: list[_AttributeField]
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onPreCook(self) -> _pdg.result: ...
    def onPartition(
        self, partition_holder: _pdg.PartitionHolder, work_items: _pdg.WorkItemList
    ) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
