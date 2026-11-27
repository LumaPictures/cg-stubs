import _pdg
from pdg.mapper import PyMapper as PyMapper

class PythonMapper(PyMapper):
    def __init__(self, node: _pdg.Node) -> None: ...
    @classmethod
    def templateName(cls) -> str: ...
    def onMapStatic(self, dependency_holder: _pdg.DependencyHolder, downstream_items: _pdg.WorkItemList, upstream_items: _pdg.WorkItemList) -> _pdg.result: ...
    def onMapDynamic(self, dependency_holder: _pdg.DependencyHolder, downstream_items: _pdg.WorkItemList, upstream_items: _pdg.WorkItemList) -> _pdg.result: ...

class MapByExpression(PyMapper):
    """
    Mapper implementation that uses parameters w/ expressions to
    define the static and dynamic mapping.
    """
    def __init__(self, node: _pdg.Node) -> None:
        """
        __init__(self, pdg.Node) -> NoneType

        Initializes the expression mapper
        """
    @classmethod
    def templateName(cls) -> str:
        '''
        templateName(cls) -> str

        Returns the ExpressionMapper template name: "expression_mapper"
        '''
    def onMapDynamic(self, dependency_holder: _pdg.DependencyHolder, downstream_items: _pdg.WorkItemList, upstream_items: _pdg.WorkItemList) -> _pdg.result:
        """
        onMapDynamic(self, pdg.EvaluationContext, pdg.WorkItemHolder, list, list) -> pdg.Result

        [virtual] Maps dynamic items by evaluating the `mapdynamic` parameter
        and treating the result as a boolean. The expression can use the
        variables `downstream_item` and `upstream_item`, which refer to the item being
        mapped and the upstream dyanmic item.
        """
    def onMapStatic(self, dependency_holder: _pdg.DependencyHolder, downstream_items: _pdg.WorkItemList, upstream_items: _pdg.WorkItemList) -> _pdg.result:
        """
        onMapStatic(self, pdg.EvaluationContext, pdg.WorkItemHolder, list, list) -> pdg.Result

        [virtual] Maps static items by evaluating the `mapstatic` parameter
        and treating the result as a boolean. The expression can use the
        variables `downstream_item` and `upstream_item`, which refer to the item being
        mapped and the upstream static item.
        """

class MapByRange(PyMapper):
    """
    Mapper implementation that maps upstream items to downstream items based on
    a range defined by the parameters on the node
    """
    def __init__(self, node: _pdg.Node) -> None:
        """
        __init__(self, pdg.Node) -> NoneType

        Initializes the mapper
        """
    @classmethod
    def templateName(cls) -> str:
        """
        templateName(cls) -> str
        """
    @classmethod
    def templateBody(cls) -> str: ...
    def onMapDynamic(self, dependency_holder: _pdg.DependencyHolder, downstream_items: _pdg.WorkItemList, upstream_items: _pdg.WorkItemList) -> _pdg.result: ...
    def onMapStatic(self, dependency_holder: _pdg.DependencyHolder, downstream_items: _pdg.WorkItemList, upstream_items: _pdg.WorkItemList) -> _pdg.result: ...

def registerTypes(type_registry: _pdg.TypeRegistry) -> None: ...
