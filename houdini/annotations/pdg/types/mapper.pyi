import _pdg
from pdg.mapper import PyMapper

class PythonMapper(PyMapper):
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    def onMapStatic(
        self,
        dependency_holder: _pdg.DependencyHolder,
        downstream_items: _pdg.WorkItemList,
        upstream_items: _pdg.WorkItemList,
    ) -> _pdg.result: ...
    def onMapDynamic(
        self,
        dependency_holder: _pdg.DependencyHolder,
        downstream_items: _pdg.WorkItemList,
        upstream_items: _pdg.WorkItemList,
    ) -> _pdg.result: ...

class MapByExpression(PyMapper):
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    def onMapDynamic(
        self,
        dependency_holder: _pdg.DependencyHolder,
        downstream_items: _pdg.WorkItemList,
        upstream_items: _pdg.WorkItemList,
    ) -> _pdg.result: ...
    def onMapStatic(
        self,
        dependency_holder: _pdg.DependencyHolder,
        downstream_items: _pdg.WorkItemList,
        upstream_items: _pdg.WorkItemList,
    ) -> _pdg.result: ...

class MapByRange(PyMapper):
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    @classmethod
    def templateBody(cls) -> str: ...
    def onMapDynamic(
        self,
        dependency_holder: _pdg.DependencyHolder,
        downstream_items: _pdg.WorkItemList,
        upstream_items: _pdg.WorkItemList,
    ) -> _pdg.result: ...
    def onMapStatic(
        self,
        dependency_holder: _pdg.DependencyHolder,
        downstream_items: _pdg.WorkItemList,
        upstream_items: _pdg.WorkItemList,
    ) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
