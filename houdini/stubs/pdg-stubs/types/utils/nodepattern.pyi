import _pdg
from pdg import PyProcessor as PyProcessor

class NodePattern(PyProcessor):
    """
    Generates work items for each matched node a pattern
    """
    SortNone: int
    SortName: int
    SortPath: int
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
