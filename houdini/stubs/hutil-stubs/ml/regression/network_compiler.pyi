from collections.abc import Iterable, Mapping, MutableSequence, Sequence
from hutil.ml.regression.module_class_interface import outputNamesFromInterface as outputNamesFromInterface
from hutil.ml.regression.module_configuration import ModuleConfigurationAtomic as ModuleConfigurationAtomic, moduleConfigurationAtomic as moduleConfigurationAtomic
from hutil.ml.regression.network_connectivity import NetworkConnectivity as NetworkConnectivity
from hutil.ml.regression.network_dependency import NetworkDependency as NetworkDependency, nodeOutput as nodeOutput, parentInput as parentInput
from typing import Any

from typing import TypeAlias
from typing import TypeVar
from collections.abc import Hashable
from typing import TypeAlias
from typing import TypeVar
_K = TypeVar('_K', bound=Hashable)
_NamedDependency: TypeAlias = str | tuple[str, str]
_NamedNetwork: TypeAlias = Mapping[str, tuple[str, Sequence[_NamedDependency]]]
def integrityNamedModuleConfigurations(named_module_configurations: object) -> tuple[bool, str]: ...
def integrityNamedDependency(named_dependency: object) -> tuple[bool, str]: ...
def integrityNamedInputs(named_inputs: object) -> tuple[bool, str]: ...
def integrityNamedNetwork(named_network: object) -> tuple[bool, str]: ...
def integrityNamedOutputs(named_outputs: object) -> tuple[bool, str]: ...

class NetworkCompilationError(Exception):
    """
    Exception type that gets thrown if a network cannot be compiled.
    """
    message: str
    def __init__(self, message: str) -> None: ...

def nameLookup(name_from_index: Iterable[_K]) -> dict[_K, int]: ...
def compileModuleConfigurations(module_class_lookup: Mapping[str, int], named_module_configurations: Mapping[str, tuple[str, Mapping[str, Any]]]) -> tuple[list[ModuleConfigurationAtomic], dict[str, int]]:
    """
    Construct a lookup from module_configuration names to their indices
    and a list that maps these indices to compiled module configurations
    
    See comments of compileNetwork below for descriptions of
    module_class_lookup and named_module_configurations
    """
def selectNextNodeTopological(post_from_pre_index: MutableSequence[int], pre_from_post_index: MutableSequence[int], named_network: _NamedNetwork, pre_node_names: list[str], pre_node_lookup: Mapping[str, int], post_node_index: int) -> bool: ...
def topologicalSortIterative(named_network: _NamedNetwork) -> tuple[list[str], dict[str, int]]:
    """
    Iterative algorithm for topological sort (not optimal)
    that selects a node for each index of the final ordering.
    """
def topologicalSort(named_network: _NamedNetwork) -> tuple[list[str], dict[str, int]]: ...
def compileDependency(module_output_lookup: Mapping[str, Mapping[str, int]], input_lookup: Mapping[str, int], named_network: _NamedNetwork, node_lookup: Mapping[str, int], output_lookup: Mapping[str, int], named_dependency: _NamedDependency) -> NetworkDependency: ...
def compileNetwork(module_class_interfaces: Sequence[Sequence[str]], module_class_lookup: Mapping[str, int], named_module_configurations: dict[str, tuple[str, dict[str, Any]]], named_inputs: list[str], named_network: dict[str, tuple[str, list[_NamedDependency]]], named_outputs: list[tuple[str, _NamedDependency]]) -> tuple[list[ModuleConfigurationAtomic], NetworkConnectivity]:
    """
    Convert a neural network description in terms of strings into
    a topologically sorted computation graph consisting of modules.
    
    module_class_lookup:
        Map from a module class name to a corresponding index
    
    named_module_configurations: 
        Dictionary that maps each module configuration name to
        a module class name and keyword arguments for
        constructing the module class
        
    named_inputs:
        Ordered list of input tensor names
        
    named_network:
        Dictionary that maps each network node name to a pair that consists of
        a module_configuration name and a list of named dependencies.
        Each named dependency is itself may be an input name, a network node name,
        or a pair consisting of a network node name and an output name
        (of the module associated with that node)
        
    named_outputs:
        Ordered list of pairs, each pair consisting of an output name
        and a named dependency.
        See named_network above for a description of named dependency.
    """
