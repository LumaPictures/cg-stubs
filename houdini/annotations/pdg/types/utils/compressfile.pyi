import _pdg
from pdg.processor import PyProcessor

class FileDecompress(PyProcessor):
    FILEPATH: int
    RESULTDATA: int
    EXPECTED_NONE: int
    EXPECTED_OUTPUT: int
    EXPECTED_ARCHIVE: int
    EXPECTED_ATTR: int
    EXPECTED_LIST: int
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(
        self,
        item_holder: _pdg.WorkItemHolder,
        upstream_items: _pdg.WorkItemList,
        generation_type: _pdg.generationType,
    ) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
