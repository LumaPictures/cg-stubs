from .callback import *
import _pdg
from .callback import PythonCallback as PythonCallback

class PyDependency(PythonCallback):
    """
    Base class for external dependencies implemented in Python
    """
    def __init__(self, dependency: _pdg.Dependency, key: str) -> None:
        """
        __init__(self, _pdg.Dependency, str) -> NoneType

        Initializes the Dependency with a C++ dependency reference and key
        """
    def isResolved(self, context: _pdg.GraphContext, node: _pdg.Node) -> bool:
        """
        isResolved(self, _pdg.GraphContext, _pdg.PyNode) -> boolean

        [virtual] Should return True if the dependency was satisfied

        All PyDependency subclasses must implement this method
        """
    def onResolve(self, context: _pdg.GraphContext, node: _pdg.Node) -> bool:
        """
        onResolve(self, _pdg.GraphContext, _pdg.PyNode) -> boolean

        [virtual] Called when the dependency should resolve. Returns True on
        success and False on failure.

        All PyDependency subclasses must implement this method
        """
