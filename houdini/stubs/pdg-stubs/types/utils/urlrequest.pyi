import _pdg
import pdg

class URLRequest(pdg.PyProcessor):
    ParamsNone: int
    ParamsAttrib: int
    ParamsMulti: int
    PayloadNone: int
    PayloadAttrib: int
    PayloadFile: int
    PayloadCustom: int
    ClientCertNone: int
    ClientCertSingle: int
    ClientCertPair: int
    SaveNone: int
    SaveAttrib: int
    SaveFile: int
    AttribString: int
    AttribJSON: int
    AttribDict: int
    FailureError: int
    FailureWarn: int
    FailureIgnore: int
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onCookTask(self, work_item: _pdg.WorkItem) -> _pdg.result: ...
    def onConfigureNode(self, node_options: _pdg.NodeOptions) -> _pdg.result: ...
    def onGenerate(self, item_holder: _pdg.WorkItemHolder, upstream_items: _pdg.WorkItemList, generation_type: _pdg.generationType) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
