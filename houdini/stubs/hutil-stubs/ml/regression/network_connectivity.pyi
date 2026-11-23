from collections.abc import Sequence
from hutil.ml.regression.network_dependency import NetworkDependency as NetworkDependency

class NetworkConnectivity:
    """
    Specifies nodes, inputs and outputs and dependencies between
    dependencies of these three types of objects.

    The entire specification is in terms of indices (instead of strings).
    The contained network is topologically sorted.
    This allows straightforward, efficient training of the network.
    """
    network: Sequence[tuple[int, Sequence[NetworkDependency]]]
    output_dependencies: Sequence[NetworkDependency]
    def __init__(self, network: Sequence[tuple[int, Sequence[NetworkDependency]]], output_dependencies: Sequence[NetworkDependency]) -> None:
        """
            network: 
            A list of pairs, where each first entry is a module index and
            each second entry is a list of dependencies.
            Each dependency is either an input index or the index of another
            node in the network.
            These dependencies must be topologically sorted;
            each node #j that node #i depends on must have j < i.
        """
    def __eq__(self, other: object) -> bool: ...
