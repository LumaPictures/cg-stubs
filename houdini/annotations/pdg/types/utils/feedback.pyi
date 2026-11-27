import _pdg
from pdg import PyProcessor

class FeedbackBegin(PyProcessor):
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
    def onAddInternalDependencies(
        self,
        dependency_holder: _pdg.DependencyHolder,
        internal_items: _pdg.WorkItemList,
        is_static: bool,
    ) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
