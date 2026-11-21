# Houdini stubs generated from Houdini 22.0.466

from collections.abc import Callable as Callable
from enum import Enum

from typing import TypeVar
from typing import TypeVar
_T = TypeVar('_T')
class NetworkDependencyType(Enum):
    """
    Indicate whether a dependency inside a network of modules
    is a parent input (an input of the network as a whole)
    or the output of some other module inside the same network
    """
    PARENT_INPUT = 0
    NODE_OUTPUT = 1

class NetworkDependency:
    """
    Define a dependency of a network node's module on an input of the network or another network node.

    Don't use directly, instead use parentInput or nodeOutput defined below.
    """
    source_type: NetworkDependencyType
    source_index: int
    output_index: int
    def __init__(self, source_type: NetworkDependencyType, source_index: int, output_index: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...

def parentInput(input_index: int) -> NetworkDependency:
    """
    Create a dependency on a parent input (an input of the network)
    """
def nodeOutput(node_index: int, output_index: int) -> NetworkDependency:
    """
    Create a dependency on a node, and a specific output of that
    node's associated module
    """
def dependencyValue(network_dependency: NetworkDependency, value_from_parent_input_index: Callable[[int], _T], value_from_module_output_index: Callable[[int, int], _T]) -> _T:
    """
    Map a node dependency to a value
    
    value_from_parent_input_index:
        Maps the index of a parent input to a value
    value_from_module_output_index:
        Maps the index of a module output to a value
    """
