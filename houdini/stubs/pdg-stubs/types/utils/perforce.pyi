import _pdg
from pdg.processor import PyProcessor as PyProcessor

DURING_GENERATE: int
DURING_COOK_IN: int
DURING_COOK_OUT: int
PERFORCE_OP_STATUS: int
PERFORCE_OP_UPDATE: int
PERFORCE_OP_SYNC: int
PERFORCE_OP_EDIT: int
PERFORCE_OP_SUBMIT: int
PERFORCE_OP_ADD: int
PERFORCE_OP_CHANGE: int
PERFORCE_OP_PRINT_VERSION: int

class Perforce(PyProcessor):
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...
    def onPrepareTask(self, work_item: _pdg.WorkItem) -> None: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
